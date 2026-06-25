import json
from unittest.mock import MagicMock, patch

from praisonai_bio.orchestrator.routing_table import route_input
from praisonai_bio.tools.sbml_validate import sbml_validate


def test_route_biomodel_id():
    assert route_input("Load BIOMD0000000206") == "load_biomodel"


def test_route_search():
    assert route_input("Find glycolysis models") == "search_models"


def test_sbml_validate_with_mock_sbml():
    minimal = b'<?xml version="1.0"?><sbml><model><listOfSpecies><species id="s1"/></listOfSpecies><listOfReactions/></model></sbml>'
    with patch("praisonai_bio.tools.sbml_validate.get_client") as mock_get:
        mock_client = MagicMock()
        mock_client.download_sbml.return_value = minimal
        mock_get.return_value = mock_client
        out = sbml_validate.run(model_id="BIOMD0000000206")
        data = json.loads(out)
        assert data["valid"] is True
        assert data["species_count"] >= 1


def test_repro_export(tmp_path):
    from praisonai_bio.tools.repro_export import repro_export

    with patch("praisonai_bio.tools.repro_export.get_client") as mock_get:
        mock_client = MagicMock()
        mock_client.download_sbml.return_value = b"<sbml/>"
        mock_client.get_model_info.return_value = {"name": "test"}
        mock_get.return_value = mock_client
        out = repro_export.run(model_id="BIOMD0000000206", output_dir=str(tmp_path), run_id="test-run-001")
        data = json.loads(out)
        assert (tmp_path / "commands.sh").exists()
        assert (tmp_path / "checksums.sha256").exists()
        assert data.get("session_dir")
        manifest = data["session_dir"] + "/repro_manifest.json"
        from pathlib import Path

        assert Path(manifest).exists()


def test_basico_load_model_downloads_sbml():
    import sys
    from praisonai_bio.adapters import basico_adapter

    mock_basico = MagicMock()
    mock_basico.load_model.return_value = "model"
    sys.modules["basico"] = mock_basico
    try:
        with patch.object(basico_adapter, "check_basico_available", return_value=(True, "")):
            with patch("praisonai_bio.tools._helpers.get_client") as mock_get:
                mock_client = MagicMock()
                mock_client.download_sbml.return_value = b"<sbml/>"
                mock_get.return_value = mock_client
                with patch("praisonai_bio.adapters.basico_adapter.write_temp_sbml", return_value="/tmp/x.xml"):
                    result = basico_adapter.load_model(model_id="BIOMD0000000206")
                    mock_client.download_sbml.assert_called_once_with("BIOMD0000000206")
                    mock_basico.load_model.assert_called_once()
                    assert result == "model"
    finally:
        sys.modules.pop("basico", None)
