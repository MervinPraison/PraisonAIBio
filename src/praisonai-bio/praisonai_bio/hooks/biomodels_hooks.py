"""Hook handlers for BioModels API and simulation events."""

from __future__ import annotations

import logging

logger = logging.getLogger("praisonai_bio.hooks")


def log_biomodels_call(event) -> None:
    tool_name = getattr(event, "tool_name", None) or getattr(event, "extra", {}).get("tool_name", "unknown")
    logger.info("BioModels call: %s", tool_name)
    import os

    run_id = (
        getattr(event, "run_id", None)
        or getattr(event, "extra", {}).get("run_id")
        or os.environ.get("BIOMODELS_RUN_ID", "")
    )
    if run_id:
        from praisonai_bio.trace.jsonl_sink import append_span

        append_span(run_id, "after_tool", {"tool_name": tool_name})


def log_simulation_complete(event: dict) -> None:
    logger.info("Simulation complete: %s", event.get("result", "")[:200])
