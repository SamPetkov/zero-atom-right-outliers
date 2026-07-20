#!/usr/bin/env python3
# Copyright (c) 2026 Samuil Petkov
# SPDX-License-Identifier: MIT OR CC-BY-4.0
"""Independent, deterministic checks of zero_atom_results.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("results", type=Path,
                        nargs="?", default=Path("zero_atom_results.json"))
    args = parser.parse_args()
    data = json.loads(args.results.read_text(encoding="utf-8"))

    b = data["bernoulli_thinning"]
    assert b["numerical_rank"] == b["predicted_rank"]
    assert b["numerical_nullity"] == b["predicted_nullity"]
    assert b["stieltjes_test_residual"] < 1e-10
    assert b["stieltjes_test_imaginary_part"] > 0
    assert b["large_z_normalization_error"] < 1e-5

    r = data["regularization"]
    for row in r["checks"]:
        assert row["absolute_identity_error"] < 1e-10
        assert row["actual_norm"] <= (
            row["epsilon"] * r["full_covariance_norm_bound_constant"] + 1e-10
        )

    t = data["two_implementations"]
    assert t["column_matrix_max_abs_difference"] < 1e-12
    assert t["weighted_covariance_operator_difference"] < 1e-12

    n = data["noncentered_gate"]
    assert n["scalar_determinant_residual_at_prediction"] < 1e-6
    assert n["prediction"]["predicted_outlier"] > n["prediction"]["right_edge"]

    print("All deterministic verification checks passed.")


if __name__ == "__main__":
    main()
