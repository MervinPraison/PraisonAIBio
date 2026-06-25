"""Tests for compare_simulations metrics."""

from __future__ import annotations

import json

from praisonai_bio.tools.compare_simulations import compare_simulations


def test_compare_simulations_rmse_metrics():
    baseline = json.dumps({"result_preview": {"ATP": [1.0, 0.9, 0.8]}})
    variant = json.dumps({"result_preview": {"ATP": [1.0, 0.85, 0.75]}, "parameter": "vGAPD"})
    out = json.loads(compare_simulations.run(baseline_json=baseline, perturbation_json=variant))
    assert "ATP" in out["metrics"]
    assert out["metrics"]["ATP"]["rmse"] > 0
