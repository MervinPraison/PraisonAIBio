"""Session state helpers for multi-phase BioModels runs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def run_dir(run_id: str) -> Path:
    base = Path.home() / ".praisonai" / "biomodels-runs" / run_id
    base.mkdir(parents=True, exist_ok=True)
    return base


def save_json(run_id: str, name: str, data: Any) -> Path:
    path = run_dir(run_id) / name
    path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
    return path


def load_json(run_id: str, name: str) -> Any:
    path = run_dir(run_id) / name
    return json.loads(path.read_text(encoding="utf-8"))
