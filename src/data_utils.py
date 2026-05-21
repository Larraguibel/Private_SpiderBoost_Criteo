"""Generic data containers and utilities shared across datasets."""

from __future__ import annotations

from typing import NamedTuple

import jax
import jax.numpy as jnp
import numpy as np

from .device import resolve_device


class TabularSplit(NamedTuple):
    """Generic train/test split container for tabular data.

    Attributes
    ----------
    x_train : jnp.ndarray, shape (n_train, d)
    y_train : jnp.ndarray, shape (n_train,)
    x_test  : jnp.ndarray, shape (n_test, d)
    y_test  : jnp.ndarray, shape (n_test,)
    metadata : dict
        Free-form dict for dataset-specific extras (e.g. feature_means,
        feature_stds, vocabulary sizes, column names). Datasets that don't
        need it return an empty dict.
    """

    x_train: jnp.ndarray
    y_train: jnp.ndarray
    x_test: jnp.ndarray
    y_test: jnp.ndarray
    metadata: dict


def arrays_to_split(
    x_train_np: np.ndarray,
    y_train_np: np.ndarray,
    x_test_np: np.ndarray,
    y_test_np: np.ndarray,
    device: str = "cpu",
    metadata: dict | None = None,
) -> TabularSplit:
    """Move pre-split NumPy arrays onto ``device`` and build a TabularSplit."""
    dev = resolve_device(device)
    return TabularSplit(
        x_train=jax.device_put(jnp.asarray(x_train_np), dev),
        y_train=jax.device_put(jnp.asarray(y_train_np), dev),
        x_test=jax.device_put(jnp.asarray(x_test_np), dev),
        y_test=jax.device_put(jnp.asarray(y_test_np), dev),
        metadata=metadata if metadata is not None else {},
    )


def make_tabular_split(
    x: np.ndarray,
    y: np.ndarray,
    test_fraction: float = 0.2,
    seed: int = 0,
    device: str = "cpu",
    metadata: dict | None = None,
) -> TabularSplit:
    """Split pre-processed NumPy arrays into train/test and move to device.

    This is the canonical place where the train/test permutation and the
    device transfer happen. Dataset-specific loaders should do all their
    preprocessing (NaN-filling, normalization, encoding, ...) and then
    call this function to produce the final TabularSplit.
    """
    n = len(x)
    rng = np.random.default_rng(seed)
    perm = rng.permutation(n)
    n_test = int(round(n * test_fraction))
    test_idx = perm[:n_test]
    train_idx = perm[n_test:]
    return arrays_to_split(
        x[train_idx],
        y[train_idx],
        x[test_idx],
        y[test_idx],
        device=device,
        metadata=metadata,
    )
