"""Append BioModels tool spans to a per-run JSONL trace file."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from praisonai_bio.state.session import run_dir


def trace_path(run_id: str) -> Path:
    return run_dir(run_id) / "trace.jsonl"


def append_span(run_id: str, event: str, payload: dict[str, Any]) -> None:
    """Append one trace line under ~/.praisonai/biomodels-runs/{run_id}/trace.jsonl."""
    if not run_id:
        return
    record = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "event": event,
        **payload,
    }
    path = trace_path(run_id)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, default=str) + "\n")
