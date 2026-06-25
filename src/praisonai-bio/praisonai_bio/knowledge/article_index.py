"""Article index stub for RAG over linked publications (Phase 1)."""

from __future__ import annotations

from typing import Any


def index_publication(model_id: str, metadata: dict[str, Any]) -> dict[str, Any]:
    return {"model_id": model_id, "indexed": False, "note": "Use praisonai index in Phase 1"}
