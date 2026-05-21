"""Training loop and evaluation utilities for Private SpiderBoost.

The Python-side outer loop dispatches between two JIT-compiled kernels
(anchor / variation) and orchestrates Poisson subsampling, history
tracking, periodic evaluation, and the random output rule of Algorithm 2.
"""

from __future__ import annotations

import math
import time
from dataclasses import dataclass, field
from typing import Callable, NamedTuple

import jax
import jax.numpy as jnp
import numpy as np
from sklearn.metrics import roc_auc_score

from . import model as model_mod
from . import private_spiderboost as psb
from .device import resolve_device
from .privacy_accountant import NoiseScales


# ---------------------------------------------------------------------------
# Poisson subsampling with padded fixed-size batches
# ---------------------------------------------------------------------------


def _poisson_padded_batch_size(b_expected: int, n: int,
                               margin_sigmas: float = 6.0) -> int:
    """Choose a padding cap ``b_max`` for a Poisson-subsampled batch.

    Sets ``b_max = b_expected + margin_sigmas * sqrt(b_expected * (1 - p))``
    where ``p = b_expected / n``. With ``margin_sigmas = 6`` the probability
    of a draw exceeding the cap is below ``10^-9`` for the parameter range
    used in this demo.
    """
    p = b_expected / n
    std = math.sqrt(b_expected * max(1.0 - p, 0.0))
    return int(math.ceil(b_expected + margin_sigmas * std + 4))


def _sample_poisson_padded(rng: np.random.Generator, n: int, p: float,
                           b_max: int) -> tuple[np.ndarray, np.ndarray]:
    """Draw one Poisson-subsampled batch padded to ``b_max``.

    Returns
    -------
    indices : np.ndarray, shape (b_max,), dtype int64
        Padded indices into the training set. Padding entries are 0.
    mask : np.ndarray, shape (b_max,), dtype float32
        1.0 for real entries, 0.0 for padding.
    """
    bern = rng.random(n) < p
    idx = np.flatnonzero(bern)
    k = idx.size
    if k > b_max:
        idx = rng.choice(idx, size=b_max, replace=False)
        k = b_max
    pad = b_max - k
    indices = np.concatenate([idx, np.zeros(pad, dtype=np.int64)])
    mask = np.concatenate(
        [np.ones(k, dtype=np.float32), np.zeros(pad, dtype=np.float32)]
    )
    return indices, mask


# ---------------------------------------------------------------------------
# Configuration and history containers
# ---------------------------------------------------------------------------


@dataclass
class TrainConfig:
    """Hyperparameters for one Private SpiderBoost run.

    Attributes
    ----------
    epsilon, delta : float
        Target privacy budget.
    L0, L1 : float
        Per-sample gradient and gradient-difference clipping bounds (also
        the assumed Lipschitz constants).
    T : int
        Total iterations.
    q : int
        Phase length.
    b1, b2 : int
        Expected anchor / variation Poisson batch sizes.
    eta : float
        Learning rate.
    hidden_dims : tuple[int, ...]
        Widths of MLP hidden layers. Default ``(64, 32)``.
    seed : int
        Master seed.
    eval_every_steps : int or None
        How often to evaluate test ROC-AUC (in steps). If ``None``, defaults
        to ``q``.
    device : str
        Target JAX device for all training computation. Accepts ``"cpu"``,
        ``"gpu"``, or ``"cuda"`` (see :func:`src.device.resolve_device`).
    """

    epsilon: float = 3.0
    delta: float = 1e-5
    L0: float = 1.0
    L1: float = 1.0
    T: int = 1000
    q: int = 50
    b1: int = 8192
    b2: int = 512
    eta: float = 0.05
    hidden_dims: tuple[int, ...] = (64, 32)
    seed: int = 0
    eval_every_steps: int | None = None
    device: str = "cpu"
    output_dim: int = 1
    eval_metric: str = "auc"


@dataclass
class TrainHistory:
    """Per-run histories returned by :func:`train`.

    Attributes
    ----------
    train_loss : list[float]
        Mean BCE on the *anchor* mini-batch at each step (cheap proxy that
        does not require an extra pass over the data).
    grad_norm : list[float]
        Global ``l_2`` norm of the running estimate ``∇_t`` at each step.
    eval_steps : list[int]
        Step indices at which test ROC-AUC was computed.
    eval_auc : list[float]
        Test ROC-AUC values (aligned with ``eval_steps``).
    test_loss_steps : list[int]
        Step indices at which mean BCE on the full test set was computed.
    test_loss : list[float]
        Mean BCE on the test set (aligned with ``test_loss_steps``).
    noise_scales : NoiseScales or None
        Computed noise scales for the run.
    wall_time_s : float
        Total training wall-clock time in seconds.
    """

    train_loss: list[float] = field(default_factory=list)
    grad_norm: list[float] = field(default_factory=list)
    eval_steps: list[int] = field(default_factory=list)
    eval_auc: list[float] = field(default_factory=list)
    test_loss_steps: list[int] = field(default_factory=list)
    test_loss: list[float] = field(default_factory=list)
    noise_scales: NoiseScales | None = None
    wall_time_s: float = 0.0


class TrainResult(NamedTuple):
    """Final outputs of :func:`train`.

    Attributes
    ----------
    params_random : pytree
        ``w̄`` — uniformly sampled from ``{w_1, ..., w_T}`` (Algorithm 2).
    params_final : pytree
        ``w_T`` — the last iterate, kept for comparison.
    history : TrainHistory
        Per-step / per-eval logs.
    config : TrainConfig
        Echoed configuration.
    """

    params_random: object
    params_final: object
    history: TrainHistory
    config: TrainConfig


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------


def evaluate_loss(params, x_test: jnp.ndarray, y_test: jnp.ndarray,
                  batch_loss_fn: Callable | None = None,
                  batch_size: int = 16384) -> float:
    """Mean BCE on the full test set, streamed in batches.

    Parameters
    ----------
    params : pytree
        Model parameters.
    x_test : jnp.ndarray, shape (n_test, d)
    y_test : jnp.ndarray, shape (n_test,)
    batch_size : int, default 16384
        Inference batch size.

    Returns
    -------
    loss : float
        ``(1 / n_test) * sum_i BCE(forward(params, x_i), y_i)``.
    """
    if batch_loss_fn is None:
        batch_loss_fn = model_mod.batch_bce_loss
    n = x_test.shape[0]
    total = 0.0
    for start in range(0, n, batch_size):
        end = min(start + batch_size, n)
        b = end - start
        total += b * float(batch_loss_fn(params, x_test[start:end], y_test[start:end]))
    return total / n


def evaluate_auc(params, x_test: jnp.ndarray, y_test: jnp.ndarray,
                 forward_fn: Callable | None = None,
                 batch_size: int = 16384) -> float:
    """Compute test ROC-AUC by streaming logits in batches.

    Parameters
    ----------
    params : pytree
        Model parameters.
    x_test : jnp.ndarray, shape (n_test, d)
    y_test : jnp.ndarray, shape (n_test,)
    batch_size : int, default 16384
        Inference batch size.

    Returns
    -------
    auc : float
        ``sklearn.metrics.roc_auc_score(y_true, y_scores)`` on logits.
    """
    if forward_fn is None:
        forward_fn = model_mod.forward
    n = x_test.shape[0]
    logits = []
    for start in range(0, n, batch_size):
        end = min(start + batch_size, n)
        logits.append(np.asarray(forward_fn(params, x_test[start:end])))
    y_scores = np.concatenate(logits)
    y_true = np.asarray(y_test)
    return float(roc_auc_score(y_true, y_scores))


# ---------------------------------------------------------------------------
# Training loop
# ---------------------------------------------------------------------------


def train(
    x_train: jnp.ndarray,
    y_train: jnp.ndarray,
    x_test: jnp.ndarray,
    y_test: jnp.ndarray,
    config: TrainConfig,
    noise_scales: NoiseScales,
    per_sample_loss_fn: Callable | None = None,
    batch_loss_fn: Callable | None = None,
    forward_fn: Callable | None = None,
    init_params: object | None = None,
    progress_every: int = 50,
) -> TrainResult:
    """Run Private SpiderBoost end-to-end and return histories + final iterates.

    Parameters
    ----------
    x_train, y_train : jnp.ndarray
        Training arrays of shape ``(n, d)`` and ``(n,)``.
    x_test, y_test : jnp.ndarray
        Test arrays of shape ``(n_test, d)`` and ``(n_test,)``.
    config : TrainConfig
        Hyperparameters.
    noise_scales : NoiseScales
        Output of :func:`privacy_accountant.compute_noise_scales`.
    progress_every : int, default 50
        How many steps between text progress lines (disabled if 0).

    Returns
    -------
    TrainResult
        See class docstring.

    Notes
    -----
    The two step kernels are JIT-compiled once each (anchor / variation)
    over fixed padded batch shapes ``(b1_max, d)`` and ``(b2_max, d)``.
    Poisson subsampling lives on the host side using NumPy: a Bernoulli
    mask of length ``n`` is drawn each step, the actual indices are
    gathered, and the result is padded to the JIT-fixed shape with a
    secondary mask passed to the kernel.
    """
    per_sample_loss_resolved = (
        per_sample_loss_fn if per_sample_loss_fn is not None
        else model_mod.per_sample_bce_loss
    )
    batch_loss_resolved = (
        batch_loss_fn if batch_loss_fn is not None
        else model_mod.batch_bce_loss
    )
    forward_resolved = (
        forward_fn if forward_fn is not None else model_mod.forward
    )

    dev = resolve_device(config.device)
    x_train = jax.device_put(x_train, dev)
    y_train = jax.device_put(y_train, dev)
    x_test = jax.device_put(x_test, dev)
    y_test = jax.device_put(y_test, dev)

    n, d = x_train.shape
    rng = np.random.default_rng(config.seed)
    key = jax.random.PRNGKey(config.seed + 1)

    key, sub = jax.random.split(key)
    if init_params is None:
        params = model_mod.init_params(sub, d, config.hidden_dims)
    else:
        params = init_params
    params = jax.tree.map(lambda a: jax.device_put(a, dev), params)

    per_sample_grad_fn = jax.vmap(
        jax.grad(per_sample_loss_resolved),
        in_axes=(None, 0, 0),
    )
    anchor_step = psb.make_anchor_step(per_sample_grad_fn)
    variation_step = psb.make_variation_step(per_sample_grad_fn)
    anchor_step_jit = jax.jit(anchor_step)
    variation_step_jit = jax.jit(variation_step)
    batch_loss_jit = jax.jit(batch_loss_resolved)

    b1_max = _poisson_padded_batch_size(config.b1, n)
    b2_max = _poisson_padded_batch_size(config.b2, n)
    p1 = config.b1 / n
    p2 = config.b2 / n

    eval_every = config.eval_every_steps if config.eval_every_steps is not None else config.q
    history = TrainHistory(noise_scales=noise_scales)

    # Algorithm 2's output rule: w̄ ~ Uniform({w_1, ..., w_T}).
    # Since T is fixed in advance, draw the index up front and snapshot.
    output_step = int(rng.integers(low=1, high=config.T + 1))
    params_random: object | None = None
    params_final = params

    grad_estimate = psb.pytree_zeros_like(params)
    params_prev = params

    t0 = time.perf_counter()
    for t in range(config.T + 1):
        is_anchor = (t % config.q == 0)

        if is_anchor:
            indices, mask_np = _sample_poisson_padded(rng, n, p1, b1_max)
            idx_dev = jax.device_put(jnp.asarray(indices), dev)
            x_batch = x_train[idx_dev]
            y_batch = y_train[idx_dev]
            mask = jax.device_put(jnp.asarray(mask_np), dev)
            key, sub = jax.random.split(key)
            out = anchor_step_jit(
                params, x_batch, y_batch, mask,
                config.b1, config.L0, noise_scales.sigma1, sub,
            )
            grad_estimate = out.grad_estimate
            grad_norm = float(out.grad_norm)
            train_loss_val = float(batch_loss_jit(params, x_batch, y_batch))
        else:
            indices, mask_np = _sample_poisson_padded(rng, n, p2, b2_max)
            idx_dev = jax.device_put(jnp.asarray(indices), dev)
            x_batch = x_train[idx_dev]
            y_batch = y_train[idx_dev]
            mask = jax.device_put(jnp.asarray(mask_np), dev)
            key, sub = jax.random.split(key)
            out = variation_step_jit(
                params, params_prev, grad_estimate,
                x_batch, y_batch, mask,
                config.b2, config.L1,
                noise_scales.sigma2, noise_scales.sigma2_hat, sub,
            )
            grad_estimate = out.grad_estimate
            grad_norm = float(out.grad_norm)
            train_loss_val = float(batch_loss_jit(params, x_batch, y_batch))

        history.grad_norm.append(grad_norm)
        history.train_loss.append(train_loss_val)

        # ||w_t - w_{t-1}|| — the step distance the variation kernel used to
        # scale its Gaussian noise. Captured before the swap below. Kept as a
        # lazy JAX scalar; only forced to host at progress steps.
        delta_w_jax = psb.pytree_global_norm(psb.pytree_sub(params, params_prev))

        # Update: w_{t+1} = w_t - eta * grad_estimate
        params_prev = params
        params = psb.sgd_update(params, grad_estimate, config.eta)

        # Snapshot for the random output rule and final iterate.
        if t == output_step:
            params_random = jax.tree.map(jnp.copy, params)
        params_final = params

        # Periodic evaluation (after applying step t's update).
        if t > 0 and (t % eval_every == 0 or t == config.T):
            if config.eval_metric == "auc":
                auc = evaluate_auc(params, x_test, y_test, forward_resolved)
                history.eval_steps.append(t)
                history.eval_auc.append(auc)

        if progress_every and (t % progress_every == 0 or t == config.T):
            test_loss_val = evaluate_loss(params, x_test, y_test, batch_loss_resolved)
            history.test_loss_steps.append(t)
            history.test_loss.append(test_loss_val)
            # Realized Gaussian noise std added at *this* step:
            #   anchor   : sigma1 (constant).
            #   variation: min(sigma2 * ||w_t - w_{t-1}||, sigma2_hat).
            delta_w = float(delta_w_jax)
            kind = "ANCHOR" if is_anchor else "var"
            if is_anchor:
                realized_noise_std = float(noise_scales.sigma1)
            else:
                realized_noise_std = float(
                    min(noise_scales.sigma2 * delta_w, noise_scales.sigma2_hat)
                )
            if config.eval_metric == "auc":
                last_auc = history.eval_auc[-1] if history.eval_auc else float("nan")
                metric_str = f"last_auc={last_auc:.4f}"
            else:
                metric_str = "metric=N/A"
            print(
                f"  step {t:4d}/{config.T}  [{kind:6s}]  "
                f"loss={train_loss_val:.4f}  test_loss={test_loss_val:.4f}  "
                f"||∇_t||={grad_norm:.4f}  ||Δw||={delta_w:.4e}  "
                f"noise_std={realized_noise_std:.4e}  {metric_str}"
            )

    history.wall_time_s = time.perf_counter() - t0

    if params_random is None:
        params_random = jax.tree.map(jnp.copy, params_final)

    return TrainResult(
        params_random=params_random,
        params_final=params_final,
        history=history,
        config=config,
    )
