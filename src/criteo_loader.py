"""Criteo-specific data loader.

Loads the 1M-row Criteo parquet, keeps the 13 numerical features
``I1``..``I13``, applies ``log(1 + x)`` and per-feature standardisation,
and returns a :class:`TabularSplit` via :func:`arrays_to_split`.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from .data_utils import TabularSplit, arrays_to_split

INT_COLS: list[str] = [f"I{i}" for i in range(1, 14)]
LABEL_COL: str = "label"


def load_criteo(
    parquet_path: str | Path,
    test_fraction: float = 0.2,
    seed: int = 0,
    device: str = "cpu",
) -> TabularSplit:
    """Load the Criteo parquet, preprocess numerical features, and split.

    Parameters
    ----------
    parquet_path : str or pathlib.Path
        Path to ``criteo_1M.parquet``.
    test_fraction : float, default 0.2
        Fraction of rows to hold out for evaluation.
    seed : int, default 0
        Seed used for the deterministic train/test shuffle.
    device : str, default ``"cpu"``
        Target JAX device for the returned arrays. Accepts ``"cpu"``,
        ``"gpu"``, or ``"cuda"`` (see :func:`src.device.resolve_device`).

    Returns
    -------
    TabularSplit
        Train/test arrays. The standardisation statistics are exposed via
        ``split.metadata["feature_means"]`` and
        ``split.metadata["feature_stds"]``.

    Notes
    -----
    Preprocessing steps, in order:

    1. Select columns ``I1``..``I13`` and ``label``.
    2. Fill NaN entries with the per-column median (computed on the training
       split to avoid test leakage).
    3. Apply ``log(1 + x)`` element-wise. Negative values are clipped to 0
       beforehand.
    4. Standardise to zero mean and unit variance using statistics from the
       training split.
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

    return arrays_to_split(
        x_train_np,
        y_train,
        x_test_np,
        y_test,
        device=device,
        metadata={"feature_means": means, "feature_stds": stds},
    )
