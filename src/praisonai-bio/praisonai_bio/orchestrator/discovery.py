"""Multi-agent discovery orchestrator helpers."""

from __future__ import annotations

from typing import Any


def build_discovery_context(research_question: str, model_ids: list[str]) -> dict[str, Any]:
    """Build a minimal context dict for discovery workflows."""
    return {
        "research_question": research_question,
        "model_ids": model_ids,
        "pipeline": [
            "intake",
            "decompose",
            "scout",
            "review",
            "analyse",
            "report",
        ],
    }
