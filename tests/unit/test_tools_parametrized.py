"""Parametrised smoke tests for bio tools (mocked client)."""

from __future__ import annotations

import importlib

import pytest

TOOL_CASES = [
    ("get_modelinfo", {"model_id": "BIOMD0000000206"}),
    ("get_annotation", {"model_id": "BIOMD0000000206"}),
    ("query_article", {"model_id": "BIOMD0000000206"}),
    ("compare_models", {"model_id_a": "BIOMD0000000206", "model_id_b": "BIOMD0000000064", "include_structure": False}),
    ("sbml_summarise", {"model_id": "BIOMD0000000206"}),
    ("list_model_files", {"model_id": "BIOMD0000000206"}),
    ("advanced_search", {"query": "glycolysis"}),
    ("search_parameters", {"query": "ATP"}),
    ("get_reaction_graph", {"model_id": "BIOMD0000000206"}),
]


@pytest.mark.parametrize("tool_name,kwargs", TOOL_CASES)
def test_tool_run_mocked(tool_name, kwargs, mock_biomodels_client, monkeypatch):
    import praisonai_bio  # noqa: F401

    mod = importlib.import_module(f"praisonai_bio.tools.{tool_name}")
    monkeypatch.setattr(mod, "get_client", lambda: mock_biomodels_client)
    tool_fn = getattr(mod, tool_name)
    out = tool_fn.run(**kwargs)
    assert out
    assert "BIOMD" in out or "parameters" in out or "glycolysis" in out.lower()
