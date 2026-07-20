#!/usr/bin/env python3
# Copyright (c) 2026 Samuil Petkov
# SPDX-License-Identifier: MIT OR CC-BY-4.0
"""Reproducible checks for the zero-atom outlier theorem.

The computations are diagnostic only; the theorem is proved analytically in the
companion report.  No network access is required.

Usage
-----
python zero_atom_checks.py --outdir results
"""

from __future__ import annotations

import argparse
import json
import math
import platform
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.linalg import eigh
from scipy.stats import norm


MASTER_SEED = 20260720


def stieltjes_bernoulli(z: complex, phi: float, pi: float, lam: float) -> complex:
    """Physical solution of
       z S^2 + (1 + lam*phi*z - phi*pi) S + lam*phi = 0.
    """
    coeff_b = 1.0 + lam * phi * z - phi * pi
    disc = coeff_b * coeff_b - 4.0 * z * lam * phi
    root_disc = np.sqrt(disc)
    roots = [(-coeff_b + root_disc) / (2.0 * z),
             (-coeff_b - root_disc) / (2.0 * z)]
    if z.imag > 0:
        candidates = [r for r in roots if r.imag > 0]
        if candidates:
            return min(candidates, key=lambda r: abs(1.0 + z * r))
    return min(roots, key=lambda r: abs(1.0 + z * r))


def bernoulli_edges(phi: float, pi: float, lam: float) -> tuple[float, float]:
    c = phi * pi
    return ((1.0 - math.sqrt(c)) ** 2 / (lam * phi),
            (1.0 + math.sqrt(c)) ** 2 / (lam * phi))


def covariance_eigenvalues(y: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """Eigenvalues of (1/n) Y diag(weights) Y^T."""
    n = y.shape[1]
    yw = y * np.sqrt(weights)[None, :]
    return np.linalg.eigvalsh((yw @ yw.T) / n)


def top_eigenpair(y: np.ndarray, weights: np.ndarray) -> tuple[float, np.ndarray]:
    n = y.shape[1]
    yw = y * np.sqrt(weights)[None, :]
    matrix = (yw @ yw.T) / n
    values, vectors = eigh(matrix, subset_by_index=[matrix.shape[0] - 1,
                                                    matrix.shape[0] - 1])
    return float(values[0]), vectors[:, 0]


def simulate_centered_columns(rng: np.random.Generator, d: int, n: int,
                              lam: float) -> np.ndarray:
    return rng.standard_normal((d, n)) / math.sqrt(lam)


def run_bernoulli_thinning(rng: np.random.Generator, outdir: Path) -> dict:
    d, n = 320, 640
    phi, pi, lam = n / d, 0.40, 1.50
    y = simulate_centered_columns(rng, d, n, lam)
    active = rng.random(n) < pi
    eig = covariance_eigenvalues(y, active.astype(float))
    n_active = int(active.sum())
    numerical_rank = int(np.count_nonzero(eig > 1e-10))
    nullity = d - numerical_rank
    edge_minus, edge_plus = bernoulli_edges(phi, pi, lam)

    x = np.linspace(max(0.0, edge_minus - 0.2), edge_plus + 0.3, 700)
    eta = 2.5e-3
    density = np.array([stieltjes_bernoulli(complex(t, eta), phi, pi, lam).imag
                        / math.pi for t in x])

    fig, ax = plt.subplots(figsize=(8.4, 5.2))
    positive = eig[eig > 1e-10]
    ax.hist(positive, bins=45, density=True, alpha=0.55,
            label="positive empirical eigenvalues")
    ax.plot(x, density / max(1e-15, (1.0 - max(0.0, 1.0 - phi * pi))),
            linewidth=1.8, label="continuous bulk, renormalized")
    ax.axvline(edge_plus, linestyle="--", linewidth=1.4,
               label="predicted right edge")
    ax.set_xlabel("eigenvalue")
    ax.set_ylabel("density")
    ax.set_title("Independent Bernoulli thinning: 1/n normalization")
    ax.legend()
    fig.tight_layout()
    fig.savefig(outdir / "bernoulli_bulk_check.png", dpi=180)
    plt.close(fig)

    test_z = complex(1.3, 0.7)
    s = stieltjes_bernoulli(test_z, phi, pi, lam)
    residual = 1.0 + test_z * s - phi * pi * s / (lam * phi + s)
    z_large = complex(1e6, 1e6)
    s_large = stieltjes_bernoulli(z_large, phi, pi, lam)

    return {
        "d": d,
        "n": n,
        "phi": phi,
        "pi": pi,
        "lambda": lam,
        "N_active": n_active,
        "active_fraction": n_active / n,
        "numerical_rank": numerical_rank,
        "predicted_rank": min(d, n_active),
        "numerical_nullity": nullity,
        "predicted_nullity": d - min(d, n_active),
        "predicted_zero_mass": max(0.0, 1.0 - phi * pi),
        "empirical_zero_mass": nullity / d,
        "edge_minus": edge_minus,
        "edge_plus": edge_plus,
        "largest_nonoutlying_eigenvalue": float(eig[-1]),
        "stieltjes_test_residual": abs(residual),
        "stieltjes_test_imaginary_part": s.imag,
        "large_z_normalization_error": abs(z_large * s_large + 1.0),
    }


def run_centered_gate(rng: np.random.Generator, outdir: Path) -> dict:
    d, n = 320, 640
    phi, lam = n / d, 1.0
    y = simulate_centered_columns(rng, d, n, lam)
    gate = y[0, :] > 0.0
    independent = rng.random(n) < 0.5
    eig_gate = covariance_eigenvalues(y, gate.astype(float))
    y_ind = simulate_centered_columns(rng, d, n, lam)
    eig_ind = covariance_eigenvalues(y_ind, independent.astype(float))
    q = np.linspace(0.0, 1.0, d)
    _, edge_plus = bernoulli_edges(phi, 0.5, lam)

    fig, ax = plt.subplots(figsize=(8.4, 5.2))
    ax.plot(q, eig_gate, label="pure gate quantiles")
    ax.plot(q, eig_ind, label="independent Bernoulli quantiles")
    ax.axhline(edge_plus, linestyle="--", linewidth=1.4,
               label="common predicted right edge")
    ax.set_xlabel("empirical quantile")
    ax.set_ylabel("eigenvalue")
    ax.set_title("Centered pure gate versus independent thinning")
    ax.legend()
    fig.tight_layout()
    fig.savefig(outdir / "centered_gate_check.png", dpi=180)
    plt.close(fig)

    return {
        "d": d,
        "n": n,
        "phi": phi,
        "lambda": lam,
        "gate_fraction": float(gate.mean()),
        "independent_fraction": float(independent.mean()),
        "predicted_right_edge": edge_plus,
        "pure_gate_top_eigenvalue": float(eig_gate[-1]),
        "independent_thinning_top_eigenvalue": float(eig_ind[-1]),
        "mean_absolute_quantile_difference": float(np.mean(np.abs(eig_gate - eig_ind))),
        "pure_gate_zero_mass": float(np.mean(eig_gate < 1e-10)),
        "independent_zero_mass": float(np.mean(eig_ind < 1e-10)),
    }


def noncentered_prediction(phi: float, lam: float, m: float,
                           a: float, b: float) -> dict:
    if b == 0.0:
        raise ValueError("b must be nonzero")
    delta = a / abs(b)
    sign_b = 1.0 if b > 0.0 else -1.0
    pi = float(norm.cdf(delta))
    pdf = float(norm.pdf(delta))
    kappa = pdf / pi
    e_g_cond = sign_b * kappa
    e_g2_cond = 1.0 - delta * kappa
    beta = lam * m * m + 2.0 * math.sqrt(lam) * m * e_g_cond + e_g2_cond
    c = phi * pi
    threshold = 1.0 + 1.0 / math.sqrt(c)
    edge_plus = (1.0 + math.sqrt(c)) ** 2 / (lam * phi)
    if beta > threshold:
        z_out = (pi / lam) * beta * (1.0 + 1.0 / (c * (beta - 1.0)))
    else:
        z_out = None
    return {
        "delta": delta,
        "pi": pi,
        "normal_pdf_delta": pdf,
        "conditional_mean_g": e_g_cond,
        "conditional_second_moment_g": e_g2_cond,
        "beta": beta,
        "bbp_threshold": threshold,
        "right_edge": edge_plus,
        "predicted_outlier": z_out,
    }


def run_noncentered_gate(rng: np.random.Generator, outdir: Path) -> dict:
    phi, lam, m, a, b = 2.0, 1.0, 2.0, 0.0, 1.0
    prediction = noncentered_prediction(phi, lam, m, a, b)
    dimensions = [100, 160, 240, 340]
    empirical_top = []
    overlaps = []
    active_fractions = []

    for d in dimensions:
        n = int(round(phi * d))
        g = rng.standard_normal(n)
        w = rng.standard_normal((d - 1, n))
        y = np.vstack([m + g / math.sqrt(lam), w / math.sqrt(lam)])
        gate = (a + b * g) > 0.0
        top, u = top_eigenpair(y, gate.astype(float))
        empirical_top.append(top)
        overlaps.append(float(u[0] ** 2))
        active_fractions.append(float(gate.mean()))

    fig, ax = plt.subplots(figsize=(8.4, 5.2))
    ax.plot(dimensions, empirical_top, marker="o", label="empirical top eigenvalue")
    ax.axhline(prediction["predicted_outlier"], linestyle="--", linewidth=1.4,
               label="effective outlier prediction")
    ax.axhline(prediction["right_edge"], linestyle=":", linewidth=1.4,
               label="bulk right edge")
    ax.set_xlabel("dimension d")
    ax.set_ylabel("largest eigenvalue")
    ax.set_title("Noncentered one-dimensional pure gate")
    ax.legend()
    fig.tight_layout()
    fig.savefig(outdir / "noncentered_outlier_check.png", dpi=180)
    plt.close(fig)

    z_pred = prediction["predicted_outlier"]
    s_real = stieltjes_bernoulli(complex(z_pred, 1e-9),
                                phi, prediction["pi"], lam)
    second_unconditional = (
        prediction["pi"] * m * m
        + 2.0 * m * prediction["normal_pdf_delta"] / math.sqrt(lam)
        + (prediction["pi"]
           - prediction["delta"] * prediction["normal_pdf_delta"]) / lam
    )
    f_at_z = (lam * phi / (lam * phi + s_real)) * second_unconditional

    return {
        "parameters": {"phi": phi, "lambda": lam, "m": m, "a": a, "b": b},
        "prediction": prediction,
        "dimensions": dimensions,
        "empirical_top_eigenvalues": empirical_top,
        "summary_direction_squared_overlaps": overlaps,
        "active_fractions": active_fractions,
        "scalar_determinant_residual_at_prediction": abs(z_pred - f_at_z),
    }


def run_regularization(rng: np.random.Generator, outdir: Path) -> dict:
    d, n, lam = 260, 520, 1.0
    y = simulate_centered_columns(rng, d, n, lam)
    gate = y[0, :] > 0.0
    inactive = (~gate).astype(float)
    delta_base = (y * inactive[None, :]) @ y.T / n
    delta_norm = float(eigh(delta_base,
                            subset_by_index=[d - 1, d - 1],
                            eigvals_only=True)[0])
    full_norm_bound = float(np.linalg.norm(y, ord=2) ** 2 / n)
    epsilons = np.array([0.005, 0.01, 0.02, 0.05, 0.10])
    exact_norms = epsilons * delta_norm
    upper_bounds = epsilons * full_norm_bound

    fig, ax = plt.subplots(figsize=(8.4, 5.2))
    ax.plot(epsilons, exact_norms, marker="o", label="exact perturbation norm")
    ax.plot(epsilons, upper_bounds, marker="s", label=r"$\epsilon\|A\|^2/n$ bound")
    ax.set_xlabel(r"$\epsilon$")
    ax.set_ylabel("operator norm")
    ax.set_title("Fixed-epsilon zero-column regularization")
    ax.legend()
    fig.tight_layout()
    fig.savefig(outdir / "regularization_check.png", dpi=180)
    plt.close(fig)

    identities = []
    base_weights = gate.astype(float)
    base_matrix = (y * base_weights[None, :]) @ y.T / n
    for eps, expected in zip(epsilons, exact_norms):
        reg_weights = base_weights + eps * inactive
        reg_matrix = (y * reg_weights[None, :]) @ y.T / n
        actual = float(eigh(reg_matrix - base_matrix,
                            subset_by_index=[d - 1, d - 1],
                            eigvals_only=True)[0])
        identities.append({
            "epsilon": float(eps),
            "actual_norm": actual,
            "epsilon_times_inactive_norm": float(expected),
            "absolute_identity_error": abs(actual - float(expected)),
        })

    return {
        "d": d,
        "n": n,
        "inactive_fraction": float(inactive.mean()),
        "inactive_covariance_norm": delta_norm,
        "full_covariance_norm_bound_constant": full_norm_bound,
        "checks": identities,
    }


def run_two_implementations(rng: np.random.Generator) -> dict:
    d, n, q, lam = 80, 150, 3, 1.7
    raw = rng.standard_normal((d, d))
    qmat, _ = np.linalg.qr(raw)
    l = qmat[:, :q]
    l_perp = qmat[:, q:]
    m = np.array([0.8, -0.4, 0.2])
    z = rng.standard_normal((d, n))
    g = l.T @ z
    w = l_perp.T @ z
    y_direct = l @ m[:, None] + z / math.sqrt(lam)
    y_decomposed = l @ (m[:, None] + g / math.sqrt(lam)) + l_perp @ (
        w / math.sqrt(lam)
    )
    weights = ((0.3 + g[0, :] - 0.5 * g[1, :]) > 0.0).astype(float)
    matrix_direct = (y_direct * weights[None, :]) @ y_direct.T / n
    matrix_decomposed = (
        (y_decomposed * weights[None, :]) @ y_decomposed.T / n
    )
    return {
        "column_matrix_max_abs_difference": float(
            np.max(np.abs(y_direct - y_decomposed))
        ),
        "weighted_covariance_operator_difference": float(
            np.linalg.norm(matrix_direct - matrix_decomposed, ord=2)
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", type=Path, default=Path("."))
    args = parser.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)

    root_rng = np.random.default_rng(MASTER_SEED)
    child_seeds = root_rng.integers(0, 2**63 - 1, size=5, dtype=np.int64)
    rngs = [np.random.default_rng(int(seed)) for seed in child_seeds]

    results = {
        "metadata": {
            "master_seed": MASTER_SEED,
            "child_seeds": [int(x) for x in child_seeds],
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "matplotlib": matplotlib.__version__,
        },
        "bernoulli_thinning": run_bernoulli_thinning(rngs[0], args.outdir),
        "centered_pure_gate": run_centered_gate(rngs[1], args.outdir),
        "noncentered_gate": run_noncentered_gate(rngs[2], args.outdir),
        "regularization": run_regularization(rngs[3], args.outdir),
        "two_implementations": run_two_implementations(rngs[4]),
    }

    result_path = args.outdir / "zero_atom_results.json"
    result_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))
    print(f"\nWrote {result_path}")


if __name__ == "__main__":
    main()
