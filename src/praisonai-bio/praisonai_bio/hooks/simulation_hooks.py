"""Simulation lifecycle hooks."""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger("praisonai_bio.hooks.simulation")


def _model_id_from_event(event) -> str:
    tool_input = getattr(event, "tool_input", None) or getattr(event, "extra", {}).get("tool_input") or {}
    if isinstance(tool_input, dict):
        return tool_input.get("model_id") or tool_input.get("modelId") or "unknown"
    return "unknown"


def before_simulation(event) -> None:
    logger.info("Starting simulation: model=%s", _model_id_from_event(event))


def after_simulation(event) -> None:
    logger.info("Simulation finished: model=%s", _model_id_from_event(event))


def approval_gate(event) -> Any:
    """Log high-risk simulation tools; block when PRAISONAI_REQUIRE_APPROVAL=1 and not approved."""
    import os

    try:
        from praisonaiagents.hooks.types import HookResult
    except ImportError:
        return None

    tool_name = getattr(event, "tool_name", "") or getattr(event, "extra", {}).get("tool_name", "")
    if tool_name not in {"parameter_scan", "simulate_perturbation"}:
        return HookResult.allow()
    if os.environ.get("PRAISONAI_REQUIRE_APPROVAL") != "1":
        logger.info("Approval recommended for %s (set PRAISONAI_REQUIRE_APPROVAL=1 to enforce)", tool_name)
        return HookResult.allow()
    approved = getattr(event, "approved", None) or getattr(event, "extra", {}).get("approved", False)
    if not approved:
        return HookResult.block(f"Approval required before {tool_name}")
    return HookResult.allow()
