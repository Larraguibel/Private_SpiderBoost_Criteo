"""Private SpiderBoost on Criteo (CTR prediction) — implementation in JAX.

Modules
-------
data_loader        : Criteo parquet loader and preprocessing.
model              : Vanilla JAX MLP with LayerNorm.
private_spiderboost: Algorithm 2 of Arora et al. (ICML 2023).
privacy_accountant : Noise scale computation and (optional) RDP verification.
train              : Training loop and evaluation utilities.
visualization      : All plotting functions.
"""
