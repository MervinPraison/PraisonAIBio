"""OLS ontology enrichment (optional Phase 7 backend)."""

from __future__ import annotations

from typing import Any


def enrich_terms(identifiers: list[str]) -> list[dict[str, Any]]:
    """Return placeholder enrichment for Identifiers.org URIs until OLS client is wired."""
    enriched = []
    for uri in identifiers:
        enriched.append({"uri": uri, "label": None, "enriched": False, "source": "ols_stub"})
    return enriched
