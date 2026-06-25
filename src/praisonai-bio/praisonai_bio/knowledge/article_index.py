"""Local publication index with optional PraisonAI KnowledgeConfig bridge."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

_INDEX_DIR = Path.home() / ".praisonai" / "biomodels-articles"


def _knowledge_search(query: str, limit: int = 5) -> list[dict[str, Any]] | None:
    """Use SDK Knowledge when available."""
    try:
        from praisonaiagents import KnowledgeConfig, Knowledge

        knowledge = Knowledge(config=KnowledgeConfig(sources=[str(_INDEX_DIR)]))
        if hasattr(knowledge, "search"):
            return knowledge.search(query, limit=limit)  # type: ignore[attr-defined]
    except Exception:
        return None
    return None


def index_path(model_id: str) -> Path:
    _INDEX_DIR.mkdir(parents=True, exist_ok=True)
    return _INDEX_DIR / f"{model_id.strip().upper()}.json"


def index_publication(model_id: str, metadata: dict[str, Any]) -> dict[str, Any]:
    """Persist publication metadata for later query_article lookups."""
    model_id = model_id.strip().upper()
    path = index_path(model_id)
    record = {"model_id": model_id, **metadata}
    path.write_text(json.dumps(record, indent=2, default=str), encoding="utf-8")
    try:
        from praisonaiagents import KnowledgeConfig, Knowledge

        knowledge = Knowledge(config=KnowledgeConfig(sources=[str(_INDEX_DIR)]))
        if hasattr(knowledge, "index"):
            knowledge.index(str(path))  # type: ignore[attr-defined]
    except Exception:
        pass
    return {"model_id": model_id, "indexed": True, "path": str(path)}


def lookup_publication(model_id: str) -> dict[str, Any] | None:
    path = index_path(model_id)
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def search_index(query: str, limit: int = 5) -> list[dict[str, Any]]:
    """Search indexed publications — KnowledgeConfig first, substring fallback."""
    hits = _knowledge_search(query, limit=limit)
    if hits:
        return hits
    if not _INDEX_DIR.exists():
        return []
    query_lower = query.lower()
    results: list[dict[str, Any]] = []
    for path in sorted(_INDEX_DIR.glob("BIOMD*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if query_lower in json.dumps(record).lower():
            results.append(record)
        if len(results) >= limit:
            break
    return results
