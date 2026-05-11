"""Noise scale computation for Private SpiderBoost.

Implements the closed-form noise multipliers from Algorithm 2 of
Arora et al. (ICML 2023, "Faster Rates of Convergence to Stationary Points
in Differentially Private Optimization") and provides an optional sanity
check against an RDP accountant from ``dp_accounting``.
"""

from __future__ import annotations

import math
from typing import NamedTuple

import numpy as np

# Universal constant that hides the absolute factor in the privacy proof.
# The paper presents the noise scales up to a constant ``c``; we use c = 1
# as the working default, consistent with the algorithm box. This is a
# heuristic choice — to be conservative in practice, set ``c`` larger and
# verify the resulting epsilon with an RDP accountant (see
# :func:`verify_epsilon`).
DEFAULT_C: float = 1.0


class NoiseScales(NamedTuple):
    """Noise standard deviations for the three Gaussian mechanisms.

    Attributes
    ----------
    sigma1 : float
        Standard deviation of the noise added to the anchor-step gradient.
    sigma2 : float
        Multiplier of ``||w_t - w_{t-1}||`` for the variation-step noise.
    sigma2_hat : float
        Cap on the variation-step noise standard deviation.
    """

    sigma1: float
    sigma2: float
    sigma2_hat: float


def compute_noise_scales(
    L0: float,
    L1: float,
    epsilon: float,
    delta: float,
    T: int,
    q: int,
    n: int,
    b1: int,
    b2: int,
    c: float = DEFAULT_C,
) -> NoiseScales:
    """Closed-form noise multipliers for Algorithm 2.

    The formulas are taken verbatim from the algorithm box (Section 4.1 of
    Arora et al. 2023):

    .. math::

        \\sigma_1     &= \\frac{c \\, L_0 \\, \\sqrt{\\log(1/\\delta)}}{\\epsilon}
                        \\cdot \\max\\left\\{ \\frac{1}{b_1},\\, \\frac{\\sqrt{T}}{q n} \\right\\} \\\\
        \\sigma_2     &= \\frac{c \\, L_1 \\, \\sqrt{\\log(1/\\delta)}}{\\epsilon}
                        \\cdot \\max\\left\\{ \\frac{1}{b_2},\\, \\frac{\\sqrt{T}}{n} \\right\\} \\\\
        \\hat\\sigma_2 &= \\frac{2 c \\, L_0 \\, \\sqrt{\\log(1/\\delta)}}{\\epsilon}
                        \\cdot \\max\\left\\{ \\frac{1}{b_2},\\, \\frac{\\sqrt{T}}{n} \\right\\}

    Parameters
    ----------
    L0 : float
        Per-sample gradient clipping bound (sensitivity of one anchor grad).
    L1 : float
        Lipschitz constant of the gradient (used in the variation-step
        sensitivity ``L1 * ||w_t - w_{t-1}||``).
    epsilon : float
        Target overall privacy budget.
    delta : float
        Target privacy failure probability.
    T : int
        Total number of SpiderBoost steps.
    q : int
        Phase length (number of steps per anchor cycle).
    n : int
        Training set size.
    b1 : int
        Expected anchor-step batch size (Poisson-subsampled).
    b2 : int
        Expected variation-step batch size (Poisson-subsampled).
    c : float, default ``DEFAULT_C``
        Universal constant from the privacy proof (set to 1; document as
        heuristic).

    Returns
    -------
    NoiseScales
        Standard deviations to plug into the per-step Gaussian mechanisms.

    Notes
    -----
    These scales correspond to the noise *added to the averaged gradient*
    (already including the ``1/b`` factor); see the algorithm box. Calibrate
    by verifying with :func:`verify_epsilon` if your trust budget allows
    only the well-known RDP bounds.
    """
    log_inv_delta = math.log(1.0 / delta)
    sqrt_T = math.sqrt(T)

    factor_anchor = max(1.0 / b1, sqrt_T / (q * n))
    factor_var = max(1.0 / b2, sqrt_T / n)

    base = c * math.sqrt(log_inv_delta) / epsilon
    sigma1 = base * L0 * factor_anchor
    sigma2 = base * L1 * factor_var
    sigma2_hat = base * 2.0 * L0 * factor_var

    return NoiseScales(sigma1=sigma1, sigma2=sigma2, sigma2_hat=sigma2_hat)


def verify_epsilon(
    L0: float,
    epsilon_target: float,
    delta: float,
    T: int,
    q: int,
    n: int,
    b1: int,
    b2: int,
    sigma1: float,
    sigma2_hat: float,
) -> float | None:
    """Sanity-check the realised epsilon with an RDP accountant.

    Treats the algorithm as a composition of two Poisson-subsampled Gaussian
    mechanisms: the anchor mechanism (sampling rate ``b1/n``, noise
    multiplier ``sigma1 * b1 / L0``) and the variation mechanism (sampling
    rate ``b2/n``, noise multiplier ``sigma2_hat * b2 / (2 * L0)`` — using
    the cap ``sigma2_hat`` upper-bounds the actual noise). The anchor
    mechanism fires ``ceil(T / q) + 1`` times; the variation mechanism
    fires the rest.

    Parameters
    ----------
    L0 : float
        Per-sample clipping bound.
    epsilon_target : float
        The target epsilon (only echoed back for context; not used in the
        bound itself).
    delta : float
        Target failure probability.
    T : int
        Total iterations.
    q : int
        Phase length.
    n : int
        Training set size.
    b1, b2 : int
        Expected batch sizes.
    sigma1, sigma2_hat : float
        Noise scales returned by :func:`compute_noise_scales`.

    Returns
    -------
    epsilon_rdp : float or None
        Epsilon implied by the RDP composition at the given ``delta``, or
        ``None`` if ``dp_accounting`` is not available.

    Notes
    -----
    The RDP bound here is intentionally loose — Algorithm 2's privacy
    analysis uses tighter accounting (Theorem B.2). A *small* RDP
    epsilon does not contradict the heuristic ``c = 1`` choice, but a
    *large* RDP epsilon is a warning sign worth investigating.
    """
    try:
        from dp_accounting import dp_event, rdp
    except ImportError:
        return None

    # Convert noise std (added to averaged gradient) to the canonical
    # noise multiplier ``z = std * b / sensitivity`` used by accountants.
    z_anchor = sigma1 * b1 / L0
    # For the variation step the sensitivity is ``2 * L0`` (since each
    # per-sample term in the sum is bounded by ``2 * L0`` after both
    # gradient clippings); using the cap ``sigma2_hat`` upper-bounds the
    # actual per-step noise.
    z_var = sigma2_hat * b2 / (2.0 * L0)

    n_anchor = math.ceil(T / q) + 1
    n_var = max(0, T + 1 - n_anchor)

    accountant = rdp.RdpAccountant()
    if n_anchor > 0:
        accountant.compose(
            dp_event.PoissonSampledDpEvent(
                sampling_probability=b1 / n,
                event=dp_event.GaussianDpEvent(noise_multiplier=z_anchor),
            ),
            count=n_anchor,
        )
    if n_var > 0:
        accountant.compose(
            dp_event.PoissonSampledDpEvent(
                sampling_probability=b2 / n,
                event=dp_event.GaussianDpEvent(noise_multiplier=z_var),
            ),
            count=n_var,
        )
    return float(accountant.get_epsilon(target_delta=delta))
