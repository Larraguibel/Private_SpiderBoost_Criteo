# Private SpiderBoost on Criteo

A self-contained JAX implementation of **Algorithm 2** of
Arora, Bassily, González, Guzmán, Menart, Ullah,
*Faster Rates of Convergence to Stationary Points in Differentially
Private Optimization*, ICML 2023, applied to CTR prediction on the
Criteo display-ads dataset (numerical features only).

## What Private SpiderBoost is

Private SpiderBoost is a variance-reduced DP first-order method that
attains a faster rate of convergence to stationary points (in expected
gradient norm) than DP-SGD: roughly `Õ(1 / T^{1/3})` vs
`Õ(1 / T^{1/4})` under the same `(ε, δ)`-DP budget for non-convex
Lipschitz-gradient losses. The variance reduction comes from the
**SPIDER**/SpiderBoost trick: replace many expensive fresh
estimates by one anchor and many cheap *gradient differences*, whose
sensitivity scales with `‖w_t - w_{t-1}‖` and therefore can be noised
much less aggressively as the iterates settle.

### Phase structure (anchor vs. variation)

Training is divided into phases of length `q`. Within each phase:

- **Anchor step** (`t mod q == 0`): draw a fresh Poisson mini-batch of
  expected size `b_1`, compute per-sample gradients of the loss, clip
  each to ‖·‖₂ ≤ `L₀`, average, and add Gaussian noise of std `σ_1`.
  This is a fresh privatized gradient estimate.
- **Variation steps** (the next `q - 1` steps): draw a smaller Poisson
  mini-batch of expected size `b_2`, compute per-sample gradient
  *differences* `∇f(w_t; x) − ∇f(w_{t-1}; x)`, clip each to
  ‖·‖₂ ≤ `L₁ · ‖w_t − w_{t-1}‖`, average, and add Gaussian noise of std
  `min(σ_2 · ‖w_t − w_{t-1}‖, σ̂_2)`. Add this to the running estimate.

Both step types use **Poisson subsampling** (each datapoint is included
independently with probability `b/n`), which is what the privacy proof
requires.

The output rule is `w̄ ~ Uniform({w_1, …, w_T})` (snapshotted up front
since `T` is fixed). The final iterate `w_T` is also returned for
comparison.

## Project layout

```
private_spider_boost_criteo/
├── data/
│   ├── criteo_1M.parquet
│   └── Faster Rates of Convergence ...pdf
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── model.py
│   ├── private_spiderboost.py
│   ├── privacy_accountant.py
│   ├── train.py
│   └── visualization.py
├── notebooks/
│   └── train_private_spiderboost.ipynb
├── figs/
└── README.md
```

## How to run

From the repository root, with a Python env that has
`jax`, `pandas`, `pyarrow`, `scikit-learn`, `matplotlib`, `dp-accounting`,
and `jupyter`:

```bash
JAX_PLATFORMS=cpu jupyter nbconvert --to notebook --execute --inplace \
    implementaciones/private_spider_boost_criteo/notebooks/train_private_spiderboost.ipynb
```

Or open the notebook interactively. Output figures are written to
`figs/`.

## Hyperparameters (default)

| name           | default | meaning                                                                |
| -------------- | ------- | ---------------------------------------------------------------------- |
| `ε`            | 3.0     | Total privacy budget                                                   |
| `δ`            | 1e-5    | Privacy failure probability                                            |
| `L_0`          | 1.0     | Per-sample gradient clipping bound (anchor step)                       |
| `L_1`          | 1.0     | Lipschitz constant of the gradient (used in variation-step clipping)   |
| `T`            | 1000    | Total iterations                                                       |
| `q`            | 50      | Phase length                                                           |
| `b_1`          | 8192    | Expected anchor batch size (Poisson)                                   |
| `b_2`          | 512     | Expected variation batch size (Poisson)                                |
| `η`            | 0.05    | Learning rate                                                          |
| `hidden_dims`  | (64,32) | MLP hidden-layer widths (LayerNorm + ReLU)                             |

Noise multipliers are derived from these via the closed-form
expressions in Algorithm 2; see [src/privacy_accountant.py](src/privacy_accountant.py).

## Theory vs. practice

The paper's optimal parameter settings (Theorem 4.2) are
**dimension-dependent and asymptotically motivated** — they are tuned
to make the rate's leading constants match. The defaults above are
**heuristic working values for a demo**, not the theoretically optimal
ones. In particular:

- The universal constant `c` in the noise-scale formulas is set to
  `c = 1`. The paper carries an unspecified constant from the
  Gaussian-mechanism privacy proof; setting `c = 1` is the typical
  empirical convention (and matches the algorithm box). For a
  production privacy claim you would either inflate `c` to be
  conservative or recalibrate `σ_1, σ̂_2` against an RDP / PRV
  accountant. The notebook prints an RDP-derived ε for sanity, using
  `dp_accounting`.
- We use **only the 13 numerical features** (`I1`..`I13`), ignoring
  the 26 categorical columns. This is intentional for a first
  iteration; categorical features need a privacy-aware embedding
  treatment (e.g. private hashed embeddings) which is out of scope.

## Implementation choices not pinned down by the prompt

- **Framework**: vanilla JAX with parameters as a plain dict pytree.
  `jax.vmap(jax.grad(per_sample_loss))` gives per-sample gradients
  cleanly, and pytree clipping/noising is handled with
  `jax.tree_util` so the code is layer-name-agnostic. Flax/Equinox
  would have added a dependency without simplifying anything for this
  use case (no stateful layers, no parameter scoping needed).
- **Poisson subsampling with fixed shapes**: Poisson sampling produces
  variable batch sizes, which would cause JIT recompiles. We sample
  the Bernoulli mask in NumPy, gather indices, and pad to a fixed
  `b_max ≈ b + 6·σ_binomial` together with a `(b_max,)` float mask
  passed to the JIT'd kernel. The Gaussian noise added to the *mean*
  uses the divisor `b` (the *expected* batch size), not the realised
  batch size — this is what the privacy bound in the paper covers.
- **Two JIT'd kernels** (anchor + variation), dispatched from a thin
  Python loop. Cleaner than a single `lax.cond` step and lets the two
  branches have different padded batch shapes.
- **Random output rule**: instead of reservoir sampling, draw
  `t* ~ Uniform({1,…,T})` up front and snapshot `w_{t*}` when reached.
  Equivalent for a fixed `T` and avoids per-step pytree copies.
- **Train loss on batch**: logged as the mean BCE on the current
  Poisson mini-batch (not the full training set) — a cheap per-step
  proxy. ROC-AUC on the held-out test set is logged every `q` steps.
- **LayerNorm, not BatchNorm**: BatchNorm would entangle samples in
  the gradient computation and break per-sample gradients in the DP
  setting. LayerNorm operates per-example.

## Files at a glance

- [src/data_loader.py](src/data_loader.py) — Criteo loading,
  `log(1+x)` and standardisation, 80/20 split.
- [src/model.py](src/model.py) — vanilla-JAX MLP with LayerNorm and a
  numerically-stable BCE loss; exposes `per_sample_loss(params, x, y)`
  for use with `jax.vmap(jax.grad(...))`.
- [src/private_spiderboost.py](src/private_spiderboost.py) — pytree
  utilities (per-sample clipping, mask, sum, scale, noise) and the two
  step kernels (`anchor_step`, `variation_step`).
- [src/privacy_accountant.py](src/privacy_accountant.py) — closed-form
  noise scales and an `dp_accounting`-backed RDP sanity check.
- [src/train.py](src/train.py) — Poisson padded batching, JIT
  compilation, history tracking, periodic AUC eval, output rule.
- [src/visualization.py](src/visualization.py) — training-loss,
  gradient-norm, ROC, AUC-history, and config-summary plots.
- [notebooks/train_private_spiderboost.ipynb](notebooks/train_private_spiderboost.ipynb)
  — driver: a config cell, a few function calls, and a final summary.
