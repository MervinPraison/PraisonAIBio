"""Smoke tests for all PraisonAIBio tools and modules."""

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(autouse=True)
def _import_bio():
    import praisonai_bio  # noqa: F401


def test_all_entry_points_importable():
    from importlib.metadata import entry_points

    eps = entry_points(group="praisonaiagents.tools")
    bio = [e for e in eps if e.module.startswith("praisonai_bio")]
    assert len(bio) >= 26
    for ep in bio:
        obj = ep.load()
        assert obj is not None


def test_orchestrator_modules():
    from praisonai_bio.orchestrator.chain_planner import plan_chain
    from praisonai_bio.orchestrator.file_detection import detect_input_kind
    from praisonai_bio.orchestrator.routing_table import route_input

    assert detect_input_kind("BIOMD0000000206") == "biomodel_id"
    assert route_input("simulate model") == "simulate_model"
    assert "search_models" in plan_chain("find glycolysis models")


def test_state_and_guardrails():
    from praisonai_bio.guardrails.simulation_output import validate_simulation_output
    from praisonai_bio.state.model_state import ModelState
    from praisonai_bio.state.session import run_dir

    st = ModelState(model_id="BIOMD0000000206")
    assert st.to_dict()["model_id"] == "BIOMD0000000206"
    ok, _ = validate_simulation_output({"result_preview": {}})
    assert ok
    assert run_dir("test-run-id").name == "test-run-id"


def test_eval_and_trace():
    from praisonai_bio.eval.simulation_accuracy import trajectory_rmse
    from praisonai_bio.eval.t2b_scorer import tool_selection_score
    from praisonai_bio.trace.bio_spans import BIO_SPAN_ATTRS

    assert tool_selection_score("a", "a") == 1.0
    assert trajectory_rmse([1.0, 2.0], [1.0, 2.0]) == 0.0
    assert "BIOMODELS_SEARCH" in BIO_SPAN_ATTRS


def test_rank_and_trust_tools():
    from praisonai_bio.tools.rank_models import rank_models
    from praisonai_bio.tools.trust_scorecard import trust_scorecard

    with patch("praisonai_bio.tools.rank_models.get_client") as mock_get:
        mock_get.return_value.search.return_value = {"models": [{"id": "BIOMD1", "name": "glycolysis"}]}
        out = json.loads(rank_models.run(query="glycolysis", research_question="glycolysis"))
        assert out["ranked"]

    with patch("praisonai_bio.tools.trust_scorecard.get_client") as mock_get:
        mock_get.return_value.get_model_info.return_value = {"curationStatus": "Manually curated", "name": "x"}
        out = json.loads(trust_scorecard.run(model_id="BIOMD0000000206"))
        assert out["trust_score"] >= 40


def test_sedml_parse_mock():
    from praisonai_bio.tools.sedml_parse import sedml_parse

    sedml = b'<?xml version="1.0"?><sedML><listOfTasks><task id="t1"/></listOfTasks></sedML>'
    with patch("praisonai_bio.tools.sedml_parse.get_client") as mock_get:
        mock = MagicMock()
        mock.list_files.return_value = {"files": [{"filename": "x.sedml"}]}
        mock.download_sedml.return_value = sedml
        mock_get.return_value = mock
        out = json.loads(sedml_parse.run(model_id="BIOMD0000000206"))
        assert out.get("tasks") == ["t1"] or "tasks" in out


def test_compare_simulations_tool():
    from praisonai_bio.tools.compare_simulations import compare_simulations

    base = json.dumps({"result_preview": {"t": [1, 2]}})
    pert = json.dumps({"result_preview": {"t": [1, 3]}, "parameter": "v1"})
    out = json.loads(compare_simulations.run(baseline_json=base, perturbation_json=pert))
    assert out["status"] == "compared"


def test_all_discovery_workflow_yaml_parseable():
    discovery = ROOT / "workflows" / "discovery"
    for path in discovery.glob("*.yaml"):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert data is not None, path.name


def test_all_orchestration_workflow_yaml_parseable():
    orch = ROOT / "workflows" / "orchestration"
    for path in orch.glob("*.yaml"):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert data is not None, path.name


def test_basico_availability_check():
    from praisonai_bio.adapters.basico_adapter import check_basico_available

    ok, msg = check_basico_available()
    assert isinstance(ok, bool)
    assert isinstance(msg, str)


def test_simulate_model_without_basico_returns_hint():
    from praisonai_bio.tools.simulate_model import simulate_model

    with patch("praisonai_bio.tools.simulate_model.load_model", side_effect=ImportError("no basico")):
        out = json.loads(simulate_model.run(model_id="BIOMD0000000206"))
        assert "error" in out or "hint" in out
