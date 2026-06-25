"""Shared helpers for PraisonAIBio tools."""

from __future__ import annotations

import json
from typing import Any

from praisonai_bio.adapters.biomodels_api import BioModelsClient


def get_client() -> BioModelsClient:
    return BioModelsClient()


def as_json(data: Any) -> str:
    if isinstance(data, str):
        return data
    return json.dumps(data, indent=2, default=str)


def normalise_model_id(model_id: str) -> str:
    return model_id.strip().upper()


def extract_models(search_result: Any) -> list[dict[str, Any]]:
    if isinstance(search_result, list):
        return search_result
    if isinstance(search_result, dict):
        for key in ("models", "results", "entries", "data"):
            if key in search_result and isinstance(search_result[key], list):
                return search_result[key]
    return []
