"""Private SpiderBoost — Algorithm 2 of Arora et al. (ICML 2023).

Reference
---------
R. Arora, R. Bassily, T. González, C. Guzmán, M. Menart, E. Ullah,
"Faster Rates of Convergence to Stationary Points in Differentially Private
Optimization", *Proceedings of the 40th International Conference on Machine
Learning*, 2023.

Overview
--------
SpiderBoost runs in *phases* of length ``q``. The first step in each phase
is an **anchor step**: a fresh privatized mini-batch gradient is computed
from scratch, with batch size ``b_1`` and noise std ``sigma1``. Each
subsequent step in the phase is a **variation step**: a privatized
gradient *difference* ``∇f(w_t) - ∇f(w_{t-1})`` is computed on a smaller
batch ``b_2`` and added to the running estimate. Because gradient
differences scale with ``||w_t - w_{t-1}||`` (Lipschitz-gradient
assumption), the variation noise can shrink as the iterates settle, which
yields the faster ``O(1 / T^{1/3})`` rate to stationary points.

This module exposes only the *math* of one anchor step and one variation
step. Subsampling, clipping, and the outer loop live in :mod:`train`. The
two step kernels here are pure functions over a parameter pytree and are
JIT-compiled at the call site.
"""

from __future__ import annotations

from typing import NamedTuple

import jax
import jax.numpy as jnp


# ---------------------------------------------------------------------------
# Pytree utilities
# ---------------------------------------------------------------------------


def pytree_global_norm(pytree) -> jax.Array:
    """Global ``l_2`` norm of a pytree (across all leaves and dimensions).

    Parameters
    ----------
    pytree : pytree of jax.Array
        Any nested structure of arrays.

    Returns
    -------
    norm : jax.Array, shape ()
        ``sqrt(sum(leaf**2 for leaf in leaves))``.
    """
    leaves = jax.tree_util.tree_leaves(pytree)
    return jnp.sqrt(sum(jnp.sum(leaf ** 2) for leaf in leaves))


def per_sample_norms(per_sample_pytree) -> jax.Array:
    """Per-sample ``l_2`` norms across all leaves and non-batch dims.

    Parameters
    ----------
    per_sample_pytree : pytree of jax.Array
        Each leaf has shape ``(B, *param_shape)`` — the leading axis
        indexes samples.

    Returns
    -------
    norms : jax.Array, shape (B,)
        ``sqrt(sum_leaves sum_non_batch_dims (leaf ** 2))``.
    """
    leaves = jax.tree_util.tree_leaves(per_sample_pytree)
    sq = [jnp.sum(leaf.reshape(leaf.shape[0], -1) ** 2, axis=1) for leaf in leaves]
    return jnp.sqrt(sum(sq))


def per_sample_clip(per_sample_pytree, clip_norm: float):
    """Clip every per-sample pytree to a global ``l_2`` norm of ``clip_norm``.

    Parameters
    ----------
    per_sample_pytree : pytree of jax.Array
        Each leaf has shape ``(B, *param_shape)``.
    clip_norm : float
        Maximum permitted global norm per sample.

    Returns
    -------
    clipped : pytree of jax.Array
        Same structure as the input. Each per-sample slice has been
        rescaled so its global ``ℓ_2`` norm is at most ``clip_norm``.
    """
    norms = per_sample_norms(per_sample_pytree)
    factor = jnp.minimum(1.0, clip_norm / (norms + 1e-12))  # (B,)

    def _scale(leaf):
        shape = (leaf.shape[0],) + (1,) * (leaf.ndim - 1)
        return leaf * factor.reshape(shape)

    return jax.tree.map(_scale, per_sample_pytree)


def per_sample_apply_mask(per_sample_pytree, mask: jax.Array):
    """Multiply each per-sample slice by ``mask[i]`` (used for Poisson masks).

    Parameters
    ----------
    per_sample_pytree : pytree of jax.Array
        Each leaf has shape ``(B, *param_shape)``.
    mask : jax.Array, shape (B,)
        Float mask, typically in {0.0, 1.0}.

    Returns
    -------
    masked : pytree of jax.Array
        Each per-sample slice has been multiplied by the mask.
    """

    def _apply(leaf):
        shape = (leaf.shape[0],) + (1,) * (leaf.ndim - 1)
        return leaf * mask.reshape(shape)

    return jax.tree.map(_apply, per_sample_pytree)


def pytree_sum_over_batch(per_sample_pytree):
    """Sum a per-sample pytree along the leading (batch) axis."""
    return jax.tree.map(lambda leaf: jnp.sum(leaf, axis=0), per_sample_pytree)


def pytree_scale(pytree, scale: float | jax.Array):
    """Multiply every leaf by ``scale``."""
    return jax.tree.map(lambda leaf: leaf * scale, pytree)


def pytree_add(a, b):
    """Element-wise sum of two pytrees with identical structure."""
    return jax.tree.map(lambda x, y: x + y, a, b)


def pytree_sub(a, b):
    """Element-wise difference of two pytrees with identical structure."""
    return jax.tree.map(lambda x, y: x - y, a, b)


def pytree_zeros_like(pytree):
    """Pytree of zeros with the same structure and shapes as ``pytree``."""
    return jax.tree.map(jnp.zeros_like, pytree)


def add_pytree_gaussian_noise(pytree, key: jax.Array, std: float | jax.Array):
    """Add iid ``N(0, std^2)`` noise of matching shape to every leaf.

    Parameters
    ----------
    pytree : pytree of jax.Array
        Reference pytree (the noise has the same shapes as its leaves).
    key : jax.Array
        PRNG key.
    std : float or jax.Array (scalar)
        Noise standard deviation.

    Returns
    -------
    noisy : pytree of jax.Array
        ``pytree + Gaussian noise``.
    """
    leaves, treedef = jax.tree_util.tree_flatten(pytree)
    keys = jax.random.split(key, len(leaves))
    noisy_leaves = [
        leaf + std * jax.random.normal(k, leaf.shape, dtype=leaf.dtype)
        for leaf, k in zip(leaves, keys)
    ]
    return jax.tree_util.tree_unflatten(treedef, noisy_leaves)


# ---------------------------------------------------------------------------
# Step kernels
# ---------------------------------------------------------------------------


class StepOutput(NamedTuple):
    """Return value of one SpiderBoost step.

    Attributes
    ----------
    grad_estimate : pytree
        New running gradient estimate ``∇_t``.
    grad_norm : jax.Array, shape ()
        Global ``ℓ_2`` norm of ``grad_estimate`` (logged every step).
    """

    grad_estimate: object
    grad_norm: jax.Array


def make_anchor_step(per_sample_grad_fn):
    """Build an anchor-step kernel for a given per-sample gradient function.

    Parameters
    ----------
    per_sample_grad_fn : callable
        Vmapped per-sample gradient: ``(params, x_batch, y_batch) -> pytree``
        with leaves of shape ``(B, *param_shape)``.

    Returns
    -------
    anchor_step : callable
        ``anchor_step(params, x_batch, y_batch, mask, b1, L0, sigma1, key)
        -> StepOutput``. ``mask`` is a (B,) Poisson mask; ``b1`` is the
        *expected* batch size used for averaging.

    Notes
    -----
    Algorithm 2, anchor branch (``t mod q == 0``)::

        g_t  ~ N(0, sigma1^2 I)
        ∇_t  = (1 / b1) * sum_{x in S_t} clip(∇f(w_t; x), L0)  +  g_t
    """

    def anchor_step(params, x_batch, y_batch, mask, b1, L0, sigma1, key):
        per_sample = per_sample_grad_fn(params, x_batch, y_batch)
        per_sample = per_sample_clip(per_sample, L0)            # Algorithm 2, Section 4.1
        per_sample = per_sample_apply_mask(per_sample, mask)    # Poisson subsampling
        summed = pytree_sum_over_batch(per_sample)
        averaged = pytree_scale(summed, 1.0 / b1)
        noisy = add_pytree_gaussian_noise(averaged, key, sigma1)
        return StepOutput(grad_estimate=noisy, grad_norm=pytree_global_norm(noisy))

    return anchor_step


def make_variation_step(per_sample_grad_fn):
    """Build a variation-step kernel for a given per-sample gradient function.

    Parameters
    ----------
    per_sample_grad_fn : callable
        Vmapped per-sample gradient: ``(params, x_batch, y_batch) -> pytree``
        with leaves of shape ``(B, *param_shape)``.

    Returns
    -------
    variation_step : callable
        ``variation_step(params_t, params_prev, prev_grad_est, x_batch,
        y_batch, mask, b2, L1, sigma2, sigma2_hat, key) -> StepOutput``.

    Notes
    -----
    Algorithm 2, variation branch (``t mod q != 0``)::

        delta_w  = ||w_t - w_{t-1}||
        clip_c   = L1 * delta_w
        g_t      ~ N(0, min(sigma2 * delta_w, sigma2_hat)^2 I)
        Δ_t      = (1 / b2) * sum_{x in S_t}
                   clip(∇f(w_t; x) - ∇f(w_{t-1}; x), clip_c)  +  g_t
        ∇_t      = ∇_{t-1} + Δ_t
    """

    def variation_step(params_t, params_prev, prev_grad_est, x_batch, y_batch,
                       mask, b2, L1, sigma2, sigma2_hat, key):
        delta_w = pytree_global_norm(pytree_sub(params_t, params_prev))

        per_sample_t = per_sample_grad_fn(params_t, x_batch, y_batch)
        per_sample_prev = per_sample_grad_fn(params_prev, x_batch, y_batch)
        per_sample_diff = jax.tree.map(lambda a, b: a - b, per_sample_t, per_sample_prev)

        clip_c = L1 * delta_w
        per_sample_diff = per_sample_clip(per_sample_diff, clip_c)   # Algorithm 2, Section 4.1
        per_sample_diff = per_sample_apply_mask(per_sample_diff, mask)
        summed = pytree_sum_over_batch(per_sample_diff)
        averaged = pytree_scale(summed, 1.0 / b2)

        noise_std = jnp.minimum(sigma2 * delta_w, sigma2_hat)
        noisy_delta = add_pytree_gaussian_noise(averaged, key, noise_std)

        new_grad_est = pytree_add(prev_grad_est, noisy_delta)
        return StepOutput(
            grad_estimate=new_grad_est,
            grad_norm=pytree_global_norm(new_grad_est),
        )

    return variation_step


def sgd_update(params, grad_estimate, lr: float):
    """Apply one ``params <- params - lr * grad`` update.

    Parameters
    ----------
    params : pytree
    grad_estimate : pytree
        Same structure as ``params``.
    lr : float
        Learning rate.

    Returns
    -------
    new_params : pytree
    """
    return jax.tree.map(lambda p, g: p - lr * g, params, grad_estimate)
