"""Hook handlers for BioModels API and simulation events."""

from __future__ import annotations

import logging

logger = logging.getLogger("praisonai_bio.hooks")


def log_biomodels_call(event: dict) -> None:
    logger.info("BioModels call: %s", event.get("tool_name", "unknown"))


def log_simulation_complete(event: dict) -> None:
    logger.info("Simulation complete: %s", event.get("result", "")[:200])
