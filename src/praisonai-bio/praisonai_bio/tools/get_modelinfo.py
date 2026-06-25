from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


@tool
def get_modelinfo(model_id: str) -> str:
    """Fetch metadata for a BioModels model ID (e.g. BIOMD0000000206)."""
    client = get_client()
    info = client.get_model_info(normalise_model_id(model_id))
    return as_json(info)
