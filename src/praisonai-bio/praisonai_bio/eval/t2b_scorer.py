"""T2B parity benchmark scorers."""

from __future__ import annotations

from typing import Any


def tool_selection_score(expected: str, actual: str) -> float:
    return 1.0 if expected == actual else 0.0


def ranking_hit_at_k(expected_ids: list[str], ranked_ids: list[str], k: int = 3) -> float:
    if not expected_ids:
        return 0.0
    top = set(ranked_ids[:k])
    hits = sum(1 for e in expected_ids if e in top)
    return hits / len(expected_ids)
