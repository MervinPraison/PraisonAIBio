from praisonaiagents import tool

from praisonai_bio.adapters.biomodels_api import BioModelsClient
from praisonai_bio.tools._helpers import as_json, extract_models, get_client


@tool
def search_models(
    query: str,
    num_results: int = 10,
    offset: int = 0,
    curated_only: bool = True,
) -> str:
    """Search BioModels.org for curated SBML models matching a query."""
    client = get_client()
    q = BioModelsClient.curated_filter(query, curated_only=curated_only)
    result = client.search(query=q, offset=offset, num_results=num_results)
    models = extract_models(result)
    if models:
        return as_json({"query": q, "count": len(models), "models": models})
    return as_json(result)
