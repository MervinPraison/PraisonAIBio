"""Shared mocks for PraisonAIBio unit tests."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest


@pytest.fixture
def mock_biomodels_client():
    client = MagicMock()
    client.get_model_info.return_value = {
        "id": "BIOMD0000000206",
        "name": "Teusink glycolysis",
        "curationStatus": "Manually curated",
        "modelLevelAnnotations": [{"is": "http://identifiers.org/go/GO:0006096"}],
    }
    client.search.return_value = {"models": [{"id": "BIOMD0000000206"}]}
    client.download_sbml.return_value = b'<?xml version="1.0"?><sbml xmlns="http://www.sbml.org/sbml/level3/version2/core"><model id="m"><listOfSpecies><species id="s1"/></listOfSpecies><listOfReactions><reaction id="r1"/></listOfReactions></model></sbml>'
    client.list_files.return_value = {"files": [{"filename": "BIOMD0000000206.sedml"}]}
    client.download_file.return_value = b"<sedML><listOfSimulations><simulation id='s1'><uniformTimeCourse initialTime='0' outputEndTime='100' outputStepSize='0.1'/></simulation></listOfSimulations></sedML>"
    client.download_combine_archive.return_value = b"PK\x03\x04"
    client.search_advanced.return_value = {"models": [{"id": "BIOMD0000000206"}]}
    client.search_parameters.return_value = {"parameters": []}
    return client
