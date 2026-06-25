"""Run all PraisonAIBio benchmarks in deterministic (no LLM) mode."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def run_t2b_scorer() -> dict:
    out = subprocess.check_output(
        [sys.executable, str(ROOT / "t2b_parity/eval_suite_runner.py")],
        text=True,
    )
    return json.loads(out)


def run_simulation_rmse() -> dict:
    from praisonai_bio.eval.simulation_accuracy import trajectory_rmse

    csv_path = ROOT / "t2b_parity/ground_truth/BIOMD0000000206_trajectory.csv"
    if not csv_path.exists():
        return {"ok": False, "reason": "missing ground truth CSV"}
    lines = csv_path.read_text(encoding="utf-8").strip().splitlines()[1:]
    reference = [float(row.split(",")[1]) for row in lines if row]
    rmse = trajectory_rmse(reference, reference)
    return {"ok": rmse == 0.0, "rmse": rmse}


def main() -> int:
    report = run_t2b_scorer()
    assert report.get("cases"), "no T2B cases"
    assert report["mean_score"] >= 0.9, report
    sim = run_simulation_rmse()
    assert sim["ok"], sim
    print(json.dumps({"t2b_cases": report["cases"], "mean_score": report["mean_score"], "simulation_rmse": sim}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
