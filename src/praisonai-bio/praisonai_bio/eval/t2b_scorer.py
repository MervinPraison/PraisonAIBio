"""T2B parity benchmark scorers."""

from __future__ import annotations

import re
from typing import Any


def infer_tool_from_prompt(prompt: str) -> str:
    """Deterministic keyword router for offline benchmark scoring (not self-score)."""
    p = prompt.lower()
    rules = [
        (r"\bsearch\b|\bfind\b|\bcurated\b", "search_models"),
        (r"\bmetadata\b|\bmodelinfo\b|\binfo for\b", "get_modelinfo"),
        (r"\bload\b", "load_biomodel"),
        (r"\bplot\b|\bchart\b|\bvisuali[sz]e\b", "custom_plotter"),
        (r"\bannotation", "get_annotation"),
        (r"\borganism\b|\bask\b|\bwhat\b|\bwho\b", "ask_question"),
        (r"\bsteady", "steady_state"),
        (r"\bparameter scan\b|\bscan\b", "parameter_scan"),
        (r"\bsimulat", "simulate_model"),
        (r"\bsave\b", "save_model"),
    ]
    for pattern, tool in rules:
        if re.search(pattern, p):
            return tool
    return "search_models"


def tool_selection_score(expected: str, actual: str) -> float:
    return 1.0 if expected == actual else 0.0


def score_case(case: dict[str, Any], tool_used: str | None = None) -> dict[str, Any]:
    expected = case.get("expected_tool", "")
    actual = tool_used or infer_tool_from_prompt(case.get("prompt", ""))
    return {
        "case": case.get("id"),
        "score": tool_selection_score(expected, actual),
        "expected": expected,
        "actual": actual,
    }


def ranking_hit_at_k(expected_ids: list[str], ranked_ids: list[str], k: int = 3) -> float:
    if not expected_ids:
        return 0.0
    top = set(ranked_ids[:k])
    hits = sum(1 for e in expected_ids if e in top)
    return hits / len(expected_ids)
