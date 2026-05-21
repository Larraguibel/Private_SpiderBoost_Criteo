"""Private SpiderBoost on Criteo (CTR prediction) — implementation in JAX.

Modules
-------
datasets           : Unified ``load_dataset(name, ...)`` entry point.
criteo_loader      : Criteo parquet loader and preprocessing (dataset-specific).
data_utils         : ``TabularSplit`` container and split helpers.
device             : Resolve a device-name string (``cpu``/``cuda``/``gpu``).
model              : Vanilla JAX MLP with LayerNorm.
private_spiderboost: Algorithm 2 of Arora et al. (ICML 2023).
privacy_accountant : Noise scale computation and (optional) RDP verification.
train              : Training loop and evaluation utilities.
visualization      : All plotting functions.
"""
