"""Experiment helpers for the Kaprekar observatory workflow."""

from __future__ import annotations

from typing import Any

from observatory.transformers.kaprekar import UniversalKaprekarTransformer


def base_sweep(start_base: int = 2, end_base: int = 16, n_digits: int = 4) -> list[dict[str, Any]]:
    """Run a small sweep over bases and summarize the resulting fixed-point rates."""
    rows: list[dict[str, Any]] = []
    for base in range(start_base, end_base + 1):
        transformer = UniversalKaprekarTransformer(n_digits=n_digits, base=base)
        fixed_points = 0
        total = 0
        for value in range(1, 1000):
            result = transformer.orbit(value, max_steps=50)
            total += 1
            if result["converged"] and result["fixed_point"] is not None:
                fixed_points += 1
        rows.append(
            {
                "base": base,
                "n_digits": n_digits,
                "fixed_point_rate": fixed_points / total,
                "fixed_points": fixed_points,
                "samples": total,
            }
        )
    return rows


def summarize_base_sweep(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Summarize the sweep rows into a compact report."""
    if not rows:
        return {"max_rate_base": None, "max_rate": None, "rows": []}

    best = max(rows, key=lambda row: row["fixed_point_rate"])
    return {
        "max_rate_base": best["base"],
        "max_rate": best["fixed_point_rate"],
        "rows": rows,
    }
