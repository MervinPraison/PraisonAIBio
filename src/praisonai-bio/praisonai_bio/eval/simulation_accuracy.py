"""Simulation accuracy scoring (Phase 1 scaffold)."""

from __future__ import annotations


def trajectory_rmse(reference: list[float], actual: list[float]) -> float:
    if not reference or not actual:
        return float("inf")
    n = min(len(reference), len(actual))
    return sum((reference[i] - actual[i]) ** 2 for i in range(n)) ** 0.5 / n
