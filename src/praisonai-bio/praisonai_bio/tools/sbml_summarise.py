from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


@tool
def sbml_summarise(model_id: str) -> str:
    """Summarise species, compartments, and reactions from SBML metadata."""
    client = get_client()
    info = client.get_model_info(normalise_model_id(model_id))
    summary = {"model_id": model_id}
    if isinstance(info, dict):
        for key in ("species", "reactions", "compartments", "parameters", "name", "description"):
            if key in info:
                summary[key] = info[key]
        if len(summary) == 1:
            summary["metadata"] = info
    return as_json(summary)
