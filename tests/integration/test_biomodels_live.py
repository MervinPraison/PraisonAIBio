"""Integration test — requires network."""

import os

import pytest

pytestmark = pytest.mark.integration


@pytest.mark.skipif(os.environ.get("SKIP_NETWORK") == "1", reason="Network tests disabled")
def test_live_search_glycolysis():
    from praisonai_bio.adapters.biomodels_api import BioModelsClient

    client = BioModelsClient()
    q = BioModelsClient.curated_filter("glycolysis")
    result = client.search(q, num_results=3)
    assert result is not None
