"""Keyword router must not cheat with expected_tool."""

from __future__ import annotations

from praisonai_bio.eval.t2b_scorer import infer_tool_from_prompt, score_case


def test_infer_tool_from_prompt_search():
    assert infer_tool_from_prompt("Search for curated glycolysis models") == "search_models"


def test_score_case_without_mock_tool():
    case = {"id": "x", "prompt": "Simulate BIOMD0000000206", "expected_tool": "simulate_model"}
    result = score_case(case)
    assert result["score"] == 1.0
    assert result["actual"] == "simulate_model"


def test_infer_plot_and_annotation():
    assert infer_tool_from_prompt("Plot simulation results") == "custom_plotter"
    assert infer_tool_from_prompt("Annotations for BIOMD0000000206") == "get_annotation"
