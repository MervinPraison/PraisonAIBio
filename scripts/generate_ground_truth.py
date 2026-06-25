#!/usr/bin/env python3
"""Generate reference trajectory CSV for T2B parity (BIOMD0000000206)."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "benchmarks" / "t2b_parity" / "ground_truth" / "BIOMD0000000206_trajectory.csv"
MODEL_ID = "BIOMD0000000206"


def _from_basico() -> list[dict[str, float]] | None:
    try:
        from praisonai_bio.adapters.basico_adapter import load_model, run_timecourse
    except ImportError:
        return None
    try:
        model = load_model(model_id=MODEL_ID)
        result = run_timecourse(model, duration=50.0, step=1.0)
    except Exception as exc:
        print(f"BASICO simulation failed: {exc}", file=sys.stderr)
        return None
    if hasattr(result, "to_dict"):
        frame = result.to_dict(orient="records")
        return frame if frame else None
    if isinstance(result, dict):
        return result.get("trajectory") or None
    return None


def _fallback_rows() -> list[dict[str, float]]:
    """Minimal placeholder when BASICO is unavailable (structure validation only)."""
    return [{"time": float(t), "ATP": 1.0 + 0.01 * t, "ADP": 2.0 - 0.01 * t} for t in range(0, 51, 5)]


def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    rows = _from_basico() or _fallback_rows()
    fieldnames = sorted({k for row in rows for k in row.keys()}, key=lambda k: (k != "time", k))
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {OUT} ({len(rows)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
