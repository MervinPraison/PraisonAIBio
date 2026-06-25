import json
from unittest.mock import MagicMock, patch

import pytest

from praisonai_bio.adapters.biomodels_api import BioModelsClient
from praisonai_bio.tools._helpers import extract_models


def test_curated_filter_adds_token():
    q = BioModelsClient.curated_filter("glycolysis")
    assert "Manually curated" in q


def test_curated_filter_idempotent():
    q = 'glycolysis AND curationstatus:"Manually curated"'
    assert BioModelsClient.curated_filter(q) == q


def test_extract_models_from_dict():
    data = {"models": [{"id": "BIOMD1"}]}
    assert extract_models(data)[0]["id"] == "BIOMD1"


@patch("httpx.Client")
def test_search_calls_biomodels(mock_client_cls):
    mock_response = MagicMock()
    mock_response.headers = {"content-type": "application/json"}
    mock_response.json.return_value = {"models": [{"id": "BIOMD0000000206"}]}
    mock_response.raise_for_status = MagicMock()
    mock_client = MagicMock()
    mock_client.__enter__ = MagicMock(return_value=mock_client)
    mock_client.__exit__ = MagicMock(return_value=False)
    mock_client.get.return_value = mock_response
    mock_client_cls.return_value = mock_client

    client = BioModelsClient(base_url="https://www.biomodels.org")
    result = client.search("glycolysis", num_results=5)
    assert "models" in result or isinstance(result, dict)
    mock_client.get.assert_called()


def test_search_models_tool():
    import praisonai_bio  # noqa: F401
    from praisonai_bio.tools.search_models import search_models

    with patch("praisonai_bio.tools.search_models.get_client") as mock_get:
        mock_client = MagicMock()
        mock_client.search.return_value = {"models": [{"id": "BIOMD0000000206"}]}
        mock_get.return_value = mock_client
        out = search_models.run(query="glycolysis", num_results=5)
        data = json.loads(out)
        assert data["count"] == 1


def test_get_modelinfo_tool():
    from praisonai_bio.tools.get_modelinfo import get_modelinfo

    with patch("praisonai_bio.tools.get_modelinfo.get_client") as mock_get:
        mock_client = MagicMock()
        mock_client.get_model_info.return_value = {"name": "Teusink glycolysis"}
        mock_get.return_value = mock_client
        out = get_modelinfo.run(model_id="BIOMD0000000206")
        assert "Teusink" in out


def test_toolsets_registered():
    import praisonai_bio  # noqa: F401
    from praisonaiagents.toolsets import resolve_toolset

    tools = resolve_toolset("sysbio-core")
    assert "search_models" in tools
    assert "simulate_model" in tools


def test_sysbio_full_has_t2b_tools():
    import praisonai_bio  # noqa: F401
    from praisonaiagents.toolsets import resolve_toolset

    tools = resolve_toolset("sysbio-full")
    for name in [
        "search_models",
        "get_modelinfo",
        "load_biomodel",
        "simulate_model",
        "ask_question",
        "steady_state",
        "parameter_scan",
        "custom_plotter",
        "get_annotation",
        "query_article",
        "save_model",
    ]:
        assert name in tools
