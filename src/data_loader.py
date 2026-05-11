"""Criteo data loader for the Private SpiderBoost demo.

This module loads the 1M-row Criteo parquet, keeps only the 13 numerical
features ``I1``..``I13`` (categorical features are ignored in this iteration),
applies a ``log(1 + x)`` transform followed by per-feature standardisation,
and returns JAX arrays split 80/20 into train and test.
"""

from __future__ import annotations

from pathlib import Path
from typing import NamedTuple

import jax.numpy as jnp
import numpy as np
import pandas as pd

INT_COLS: list[str] = [f"I{i}" for i in range(1, 14)]
LABEL_COL: str = "label"


class CriteoData(NamedTuple):
    """Container for the train/test split.

    Attributes
    ----------
    x_train : jnp.ndarray, shape (n_train, 13)
        Standardised numerical features for training.
    y_train : jnp.ndarray, shape (n_train,)
        Binary labels in {0., 1.} for training.
    x_test : jnp.ndarray, shape (n_test, 13)
        Standardised numerical features for evaluation.
    y_test : jnp.ndarray, shape (n_test,)
        Binary labels in {0., 1.} for evaluation.
    feature_means : np.ndarray, shape (13,)
        Per-feature means used in standardisation (computed on train).
    feature_stds : np.ndarray, shape (13,)
        Per-feature standard deviations used in standardisation.
    """

    x_train: jnp.ndarray
    y_train: jnp.ndarray
    x_test: jnp.ndarray
    y_test: jnp.ndarray
    feature_means: np.ndarray
    feature_stds: np.ndarray


def load_criteo(
    parquet_path: str | Path,
    test_fraction: float = 0.2,
    seed: int = 0,
) -> CriteoData:
    """Load the Criteo parquet, preprocess numerical features, and split.

    Parameters
    ----------
    parquet_path : str or pathlib.Path
        Path to ``criteo_1M.parquet``.
    test_fraction : float, default 0.2
        Fraction of rows to hold out for evaluation.
    seed : int, default 0
        Seed used for the deterministic train/test shuffle.

    Returns
    -------
    CriteoData
        Train/test arrays plus the standardisation statistics. See the class
        docstring for shapes.

    Notes
    -----
    Preprocessing steps, in order:

    1. Select columns ``I1``..``I13`` and ``label``.
    2. Fill NaN entries with the per-column median (computed on the training
       split to avoid test leakage).
    3. Apply ``log(1 + x)`` element-wise. Negative values are clipped to 0
       beforehand (Criteo specifies that integer features are non-negative,
       but a small number of NaN-filled rows could otherwise produce
       non-physical inputs).
    4. Standardise to zero mean and unit variance using statistics from the
       training split.

    The 80/20 split is performed by a fixed-seed permutation of the row
    indices.
    """
    parquet_path = Path(parquet_path)
    if not parquet_path.exists():
        raise FileNotFoundError(f"Criteo parquet not found at {parquet_path}")

    df = pd.read_parquet(parquet_path, columns=INT_COLS + [LABEL_COL])

    rng = np.random.default_rng(seed)
    n = len(df)
    perm = rng.permutation(n)
    n_test = int(round(n * test_fraction))
    test_idx = perm[:n_test]
    train_idx = perm[n_test:]

    x_train_df = df.iloc[train_idx][INT_COLS]
    x_test_df = df.iloc[test_idx][INT_COLS]
    y_train = df.iloc[train_idx][LABEL_COL].to_numpy(dtype=np.float32)
    y_test = df.iloc[test_idx][LABEL_COL].to_numpy(dtype=np.float32)

    medians = x_train_df.median(numeric_only=True)
    x_train_np = x_train_df.fillna(medians).to_numpy(dtype=np.float32)
    x_test_np = x_test_df.fillna(medians).to_numpy(dtype=np.float32)

    x_train_np = np.log1p(np.clip(x_train_np, a_min=0.0, a_max=None))
    x_test_np = np.log1p(np.clip(x_test_np, a_min=0.0, a_max=None))

    means = x_train_np.mean(axis=0)
    stds = x_train_np.std(axis=0)
    stds = np.where(stds < 1e-8, 1.0, stds)

    x_train_np = (x_train_np - means) / stds
    x_test_np = (x_test_np - means) / stds

    return CriteoData(
        x_train=jnp.asarray(x_train_np),
        y_train=jnp.asarray(y_train),
        x_test=jnp.asarray(x_test_np),
        y_test=jnp.asarray(y_test),
        feature_means=means,
        feature_stds=stds,
    )
