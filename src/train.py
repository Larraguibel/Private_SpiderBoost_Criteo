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


@dataclass
class TrainHistory:
    """Per-run histories returned by :func:`train`.

    Attributes
    ----------
    train_loss : list[float]
        Mean BCE on the *anchor* mini-batch at each step (cheap proxy that
        does not require an extra pass over the data).
    grad_norm : list[float]
        Global ``ℓ_2`` norm of the running estimate ``∇_t`` at each step.
    eval_steps : list[int]
        Step indices at which test ROC-AUC was computed.
    eval_auc : list[float]
        Test ROC-AUC values (aligned with ``eval_steps``).
    noise_scales : NoiseScales or None
        Computed noise scales for the run.
    wall_time_s : float
        Total training wall-clock time in seconds.
    """

    train_loss: list[float] = field(default_factory=list)
    grad_norm: list[float] = field(default_factory=list)
    eval_steps: list[int] = field(default_factory=list)
    eval_auc: list[float] = field(default_factory=list)
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


def evaluate_auc(params, x_test: jnp.ndarray, y_test: jnp.ndarray,
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
    n = x_test.shape[0]
    logits = []
    for start in range(0, n, batch_size):
        end = min(start + batch_size, n)
        logits.append(np.asarray(model_mod.forward(params, x_test[start:end])))
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
    n, d = x_train.shape
    rng = np.random.default_rng(config.seed)
    key = jax.random.PRNGKey(config.seed + 1)

    key, sub = jax.random.split(key)
    params = model_mod.init_params(sub, d, config.hidden_dims)

    per_sample_grad_fn = jax.vmap(
        jax.grad(model_mod.per_sample_loss),
        in_axes=(None, 0, 0),
    )
    anchor_step = psb.make_anchor_step(per_sample_grad_fn)
    variation_step = psb.make_variation_step(per_sample_grad_fn)
    anchor_step_jit = jax.jit(anchor_step)
    variation_step_jit = jax.jit(variation_step)
    batch_loss_jit = jax.jit(model_mod.batch_loss)

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
            x_batch = x_train[jnp.asarray(indices)]
            y_batch = y_train[jnp.asarray(indices)]
            mask = jnp.asarray(mask_np)
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
            x_batch = x_train[jnp.asarray(indices)]
            y_batch = y_train[jnp.asarray(indices)]
            mask = jnp.asarray(mask_np)
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

        # Update: w_{t+1} = w_t - eta * grad_estimate
        params_prev = params
        params = psb.sgd_update(params, grad_estimate, config.eta)

        # Snapshot for the random output rule and final iterate.
        if t == output_step:
            params_random = jax.tree.map(jnp.copy, params)
        params_final = params

        # Periodic evaluation (after applying step t's update).
        if t > 0 and (t % eval_every == 0 or t == config.T):
            auc = evaluate_auc(params, x_test, y_test)
            history.eval_steps.append(t)
            history.eval_auc.append(auc)

        if progress_every and (t % progress_every == 0 or t == config.T):
            kind = "ANCHOR" if is_anchor else "var"
            last_auc = history.eval_auc[-1] if history.eval_auc else float("nan")
            print(
                f"  step {t:4d}/{config.T}  [{kind:6s}]  "
                f"loss={train_loss_val:.4f}  ||∇_t||={grad_norm:.4f}  "
                f"last_auc={last_auc:.4f}"
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
