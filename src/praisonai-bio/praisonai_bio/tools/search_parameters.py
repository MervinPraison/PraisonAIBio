from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json, get_client


@tool
def search_parameters(query: str, num_results: int = 10, offset: int = 0) -> str:
    """Search the BioModels Parameters database."""
    client = get_client()
    result = client.search_parameters(query, offset=offset, num_results=num_results)
    return as_json(result)
