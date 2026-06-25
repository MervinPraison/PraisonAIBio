from praisonaiagents import tool

from praisonai_bio.adapters.biomodels_api import BioModelsClient
from praisonai_bio.tools._helpers import as_json, extract_models, get_client


@tool
def advanced_search(
    query: str,
    num_results: int = 10,
    offset: int = 0,
    sort: str | None = None,
    curated_only: bool = True,
    field: str | None = None,
) -> str:
    """Advanced BioModels search with field filters and sorting."""
    try:
        client = get_client()
        q = BioModelsClient.curated_filter(query, curated_only=curated_only)
        if field and field not in q.lower():
            q = f'{field}:"{query}"' if query else q
        result = client.search_advanced(query=q, offset=offset, num_results=num_results, sort=sort)
        models = extract_models(result)
        if models:
            return as_json({"query": q, "count": len(models), "models": models, "sort": sort})
        return as_json(result)
    except Exception as exc:
        return as_json({"error": str(exc)})
