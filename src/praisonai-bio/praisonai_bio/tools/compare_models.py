from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


@tool
def compare_models(model_id_a: str, model_id_b: str) -> str:
    """Compare metadata and scope of two BioModels entries."""
    client = get_client()
    a = client.get_model_info(normalise_model_id(model_id_a))
    b = client.get_model_info(normalise_model_id(model_id_b))
    return as_json({"model_a": {"id": model_id_a, "info": a}, "model_b": {"id": model_id_b, "info": b}})
