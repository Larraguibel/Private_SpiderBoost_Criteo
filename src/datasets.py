"""Dataset registry: load named datasets through a single entry point.

Currently supported names:
    "criteo_1M" — 1M-row Criteo CTR sample, 13 numerical features.

To add a new dataset, write a loader function that returns a TabularSplit
and register it in _DATASET_REGISTRY below.
"""

from __future__ import annotations

from pathlib import Path
from typing import Callable

from .criteo_loader import load_criteo
from .data_utils import TabularSplit


def _load_criteo_1M(
    data_dir: str | Path,
    test_fraction: float = 0.2,
    seed: int = 0,
    device: str = "cpu",
) -> TabularSplit:
    """Resolve ``criteo_1M.parquet`` under ``data_dir`` and delegate."""
    parquet_path = Path(data_dir) / "criteo_1M.parquet"
    return load_criteo(
        parquet_path, test_fraction=test_fraction, seed=seed, device=device
    )


_DATASET_REGISTRY: dict[str, Callable[..., TabularSplit]] = {
    "criteo_1M": _load_criteo_1M,
}


def list_datasets() -> list[str]:
    """Names of all registered datasets."""
    return sorted(_DATASET_REGISTRY.keys())


def load_dataset(
    name: str,
    data_dir: str | Path = "data",
    test_fraction: float = 0.2,
    seed: int = 0,
    device: str = "cpu",
    **kwargs,
) -> TabularSplit:
    """Load a named dataset.

    Parameters
    ----------
    name : str
        Registered dataset name. See ``list_datasets()`` for the current
        options.
    data_dir : str or Path, default ``"data"``
        Directory containing the dataset's raw files. The convention is
        relative to the project root.
    test_fraction, seed, device
        Forwarded to the underlying loader.
    **kwargs
        Forwarded to the underlying loader for dataset-specific options.

    Raises
    ------
    ValueError
        If ``name`` is not registered. The error message lists the
        available names.
    """
    if name not in _DATASET_REGISTRY:
        raise ValueError(
            f"Unknown dataset {name!r}. Available datasets: "
            f"{list_datasets()}"
        )
    loader = _DATASET_REGISTRY[name]
    return loader(
        data_dir=data_dir,
        test_fraction=test_fraction,
        seed=seed,
        device=device,
        **kwargs,
    )
