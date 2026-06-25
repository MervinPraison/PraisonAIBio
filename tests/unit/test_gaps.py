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
        out = repro_export.run(model_id="BIOMD0000000206", output_dir=str(tmp_path))
        data = json.loads(out)
        assert (tmp_path / "commands.sh").exists()
        assert (tmp_path / "checksums.sha256").exists()
