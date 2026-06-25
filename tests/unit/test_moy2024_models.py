"""MOY2024 Model of the Year integration test stubs."""

from __future__ import annotations

import pytest

MOY2024_MODELS = [
    {"id": "BIOMD0000000537", "domain": "IL-6 immune signalling"},
    {"id": "BIOMD0000000064", "domain": "MAPK hysteresis"},
    {"id": "BIOMD0000000206", "domain": "Glycolysis ODE"},
]


@pytest.mark.parametrize("case", MOY2024_MODELS)
def test_moy_model_metadata_smoke(case, mocker):
    from praisonai_bio.tools.get_modelinfo import get_modelinfo

    mocker.patch(
        "praisonai_bio.tools.get_modelinfo.get_client",
        return_value=mocker.Mock(
            get_model_info=mocker.Mock(return_value={"id": case["id"], "name": case["domain"]})
        ),
    )
    out = get_modelinfo.run(model_id=case["id"])
    assert case["id"] in out or case["domain"] in out
