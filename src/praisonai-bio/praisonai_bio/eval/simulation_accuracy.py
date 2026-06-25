"""Simulation accuracy metrics and evaluators."""

from __future__ import annotations

from typing import Any


def trajectory_rmse(reference: list[float], actual: list[float]) -> float:
    if not reference or not actual:
        return float("inf")
    n = min(len(reference), len(actual))
    if n == 0:
        return float("inf")
    return (sum((float(reference[i]) - float(actual[i])) ** 2 for i in range(n)) / n) ** 0.5


def peak_time(series: list[float], step: float = 1.0) -> float | None:
    if not series:
        return None
    idx = max(range(len(series)), key=lambda i: float(series[i]))
    return idx * step


def trapezoid_auc(series: list[float], step: float = 1.0) -> float:
    if len(series) < 2:
        return 0.0
    total = 0.0
    for i in range(len(series) - 1):
        total += (float(series[i]) + float(series[i + 1])) * 0.5 * step
    return total


def compare_trajectories(
    baseline: dict[str, list[float]],
    variant: dict[str, list[float]],
    step: float = 1.0,
) -> dict[str, Any]:
    """Compare numeric time series with RMSE, peak time, and AUC deltas."""
    metrics: dict[str, Any] = {}
    shared = set(baseline.keys()) & set(variant.keys())
    for key in sorted(shared):
        b_series, v_series = baseline[key], variant[key]
        if not isinstance(b_series, list) or not isinstance(v_series, list):
            continue
        metrics[key] = {
            "rmse": trajectory_rmse(b_series, v_series),
            "peak_time_baseline": peak_time(b_series, step),
            "peak_time_variant": peak_time(v_series, step),
            "auc_baseline": trapezoid_auc(b_series, step),
            "auc_variant": trapezoid_auc(v_series, step),
        }
    return metrics


class TrajectoryRMSEEvaluator:
    """Thin evaluator wrapper for benchmark runners (SDK EvalSuite compatible shape)."""

    name = "trajectory_rmse"

    def __init__(self, reference: list[float], actual: list[float], threshold: float = 0.05) -> None:
        self.reference = reference
        self.actual = actual
        self.threshold = threshold

    def run(self) -> dict[str, Any]:
        rmse = trajectory_rmse(self.reference, self.actual)
        passed = rmse <= self.threshold
        return {"name": self.name, "score": 1.0 if passed else 0.0, "rmse": rmse, "passed": passed}
