# Prompt for Claude Code

I want to implement the **Private SpiderBoost** algorithm (Algorithm 2 from Arora et al. 2023, "Faster Rates of Convergence to Stationary Points in Differentially Private Optimization") in JAX, applied to CTR prediction on the Criteo dataset. Please create this as a self-contained mini-project.

## Project location

The dataset is already at `implementaciones/private_spider_boost_criteo/data/criteo_1M.parquet` (1M samples). The paper PDF is at `implementaciones/private_spider_boost_criteo/data/Faster Rates of Convergence to Stationary Points in Differentially Private Optimization.pdf` — consult it if needed. Please verify both files exist before assuming the paths.

## Suggested folder structure

```
private_spider_boost_criteo/
├── data/
│   ├── criteo_1M.parquet                        # already exists
│   └── Faster Rates of Convergence ...pdf       # already exists
├── src/
│   ├── __init__.py
│   ├── data_loader.py              # Criteo loading + preprocessing
│   ├── model.py                    # MLP model definition
│   ├── private_spiderboost.py      # the main algorithm
│   ├── privacy_accountant.py       # noise scale computation
│   ├── train.py                    # training loop and evaluation logic
│   └── visualization.py           # all plotting functions
├── notebooks/
│   └── train_private_spiderboost.ipynb
├── figs/                           # output figures (ROC curves, training curves)
└── README.md
```

## Algorithm reference (Algorithm 2 from the paper)

```
Input: Dataset S ∈ X^n, function f, learning rate η, phase size q,
       batch sizes b1, b2, privacy params (ε, δ), iterations T

w_0 = 0
σ_1 = (c·L_0·√log(1/δ) / ε) · max{1/b1, √T / (q·n) }
σ_2 = (c·L_1·√log(1/δ) / ε) · max{1/b2, √T / n}
σ̂_2 = (2c·L_0·√log(1/δ) / ε) · max{1/b2, √T / n}

for t = 0, ..., T:
    if t mod q == 0:                    # ANCHOR step (start of phase)
        Sample batch S_t of size b1
        g_t ~ N(0, σ_1² · I_d)
        ∇_t = (1/b1) Σ_{x ∈ S_t} ∇f(w_t; x) + g_t
    else:                                # VARIATION step
        Sample batch S_t of size b2
        noise_var = min{σ_2² · ‖w_t - w_{t-1}‖², σ̂_2²}
        g_t ~ N(0, noise_var · I_d)
        Δ_t = (1/b2) Σ_{x ∈ S_t} [∇f(w_t; x) - ∇f(w_{t-1}; x)] + g_t
        ∇_t = ∇_{t-1} + Δ_t
    w_{t+1} = w_t - η ∇_t

Return w̄ uniformly at random from {w_1, ..., w_T}
```

## Key implementation details

### 1. Data loading (`data_loader.py`)
- Load `criteo_1M.parquet`.
- **For this first iteration, use only the 13 integer/numerical features** `"I1"–"I13"`. Ignore the 26 categorical columns entirely.
- Numerical features: log-transform `log(1 + x)` for non-negative values (Criteo convention), then standardize (zero mean, unit variance). Handle NaNs by filling with column median before transforming.
- Target column: `"label"`.
- Train/test split (80/20), fixed seed.
- Return JAX arrays.

### 2. Model (`model.py`)
- A vanilla MLP for binary classification, implemented to be compatible with JAX's functional style and the training schedule (parameters as a pytree, no stateful objects in the hot loop).
- The number of hidden layers and hidden dimension should be **hyperparameters** (e.g. `hidden_dims: list[int]`). A default of `[64, 32]` gives two hidden layers.
- Architecture: input(13) → [Dense → LayerNorm → ReLU] × num_layers → Dense(1).
- Use LayerNorm, not BatchNorm. No dropout.
- Loss: sigmoid binary cross-entropy. Expose a `per_sample_loss(params, x, y)` function that returns a scalar, suitable for `jax.vmap(jax.grad(...))`.
- Use Flax or Equinox — your call, but explain the choice in the README. Prefer Flax `linen` if compatibility is a concern.

### 3. Per-sample gradients (`private_spiderboost.py`)
- Use `jax.vmap(jax.grad(loss_fn))` to compute per-sample gradients. The result is a pytree of arrays with an extra leading batch dimension.
- Clip each per-sample gradient pytree to global ℓ₂ norm `L_0` before averaging (Algorithm 2, Section 4.1 of the paper). Clipping must be applied per-sample, before averaging — not on the mean.
- For the variation step, compute per-sample gradient differences `∇f(w_t; x_i) - ∇f(w_{t-1}; x_i)` for the same mini-batch, and clip each difference pytree to norm `L_1 · ‖w_t - w_{t-1}‖` (Section 4.1, sensitivity of the gradient variation estimator). Add noise of the appropriate scale.
- Handle pytree operations (clipping, norm computation, noise addition) using `jax.tree_util` so the code generalises to any model architecture without hardcoding layer names.

### 4. Privacy accountant (`privacy_accountant.py`)
- Implement the noise scale formulas exactly as in Algorithm 2 of the paper.
- Use **Poisson subsampling** for batch selection (each datapoint is included independently with probability `b/n`), not shuffled minibatches (Section 4.1 and Theorem B.2 of the paper).
- Provide a function `compute_noise_scales(L0, L1, epsilon, delta, T, q, n, b1, b2) -> (sigma1, sigma2, sigma2_hat)`. Use `c = 1` as the universal constant; document this.
- Optionally verify the resulting ε using `dp_accounting` or Opacus's RDP accountant as a sanity check.

### 5. Training loop (`train.py`)
- Separate the training loop logic and evaluation logic from the notebook. The notebook should only call high-level functions from this module.
- Track and return histories of:
  - Per-step training loss
  - Empirical gradient norm `‖∇_t‖` (the running estimate, not the true gradient — available for free from the algorithm state) logged every step
  - Test ROC-AUC computed every `q` steps on the test set
- The final output `w̄` is selected uniformly at random from `{w_1, ..., w_T}` (per the algorithm). Also return the final iterate separately for comparison.
- For ROC-AUC, pass logits (not binary predictions) to `roc_auc_score`.
- JIT-compile the inner gradient step.

### 6. Visualization (`visualization.py`)
- All plotting logic lives here. The notebook imports and calls these functions.
- Implement the following functions, each saving its figure to `figs/` and also returning the matplotlib figure object:
  - `plot_training_loss(loss_history, save_path)`: training loss vs. step
  - `plot_gradient_norm(grad_norm_history, save_path)`: empirical gradient norm vs. step, log y-axis
  - `plot_roc_curve(y_true, y_scores, auc_value, save_path)`: ROC curve on test set
  - `plot_hyperparameter_summary(config: dict, save_path)`: a text/table figure summarising the run's hyperparameters (ε, δ, T, q, b1, b2, η, L0, L1, architecture) — useful for reproducibility
- Use NumPy docstrings throughout, including `Parameters`, `Returns`, and `Notes` sections with explicit shapes.

### 7. Notebook (`train_private_spiderboost.ipynb`)
- Hyperparameters should be defined in a single config cell at the top, easy to change:
  - `ε = 3.0`, `δ = 1e-5`
  - `L_0 = 1.0`, `L_1 = 1.0`
  - `hidden_dims = [64, 32]`
  - `T = 1000`, `q = 50`, `b_1 = 8192`, `b_2 = 512`, `η = 0.05`
- Call functions from `train.py` and `visualization.py` — do not put training or plotting logic directly in the notebook.
- Print the final test ROC-AUC and final empirical gradient norm in the last cell.

## Code quality requirements

- **NumPy-style docstrings** on every function, including `Parameters`, `Returns`, `Notes` sections with explicit array shapes (e.g. `gradients : Array, shape (batch_size, d)`).
- Type hints on all function signatures.
- A module-level docstring at the top of `private_spiderboost.py` summarising the algorithm and citing the paper (Arora et al., ICML 2023).
- Where an implementation choice is directly taken from the paper, add a short reference comment, e.g. `# Algorithm 2, line 12` or `# Theorem B.2`. No need to explain the reasoning inline — just the reference is enough.
- Use JAX idioms: `jax.jit` on the hot loop, `jax.vmap` for per-sample gradients, explicit PRNG key threading via `jax.random.split`.
- Be careful with the following potential pitfalls:
  - Pytree clipping: compute the global ℓ₂ norm across all leaves before clipping, not per-leaf
  - Clipping is applied per-sample before averaging, not on the mean gradient
  - Poisson subsampling: implement it correctly (independent Bernoulli draws, not fixed-size sampling)

## README

Write a short README explaining:
- What Private SpiderBoost is (one paragraph)
- The phase structure: anchor steps vs. variation steps
- How to run the notebook
- Hyperparameter explanations
- A note on the gap between theory and practice — the paper's optimal parameter settings (Theorem 4.2) are dimension-dependent and asymptotically motivated; the values above are heuristic defaults for the demo
- Any framework or design choices that were not fully specified in this prompt

## Deliverable

Create the folder, all source files, and the notebook. Run the notebook end-to-end to verify it works, and save the output figures to `figs/`. Report the final test ROC-AUC and the final empirical gradient norm in your summary. If any choice was ambiguous, document it in the README rather than asking — but flag it in your final summary.
