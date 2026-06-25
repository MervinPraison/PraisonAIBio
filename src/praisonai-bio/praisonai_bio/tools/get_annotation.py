from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


@tool
def get_annotation(model_id: str) -> str:
    """Retrieve annotations (RDF/MIRIAM) for a BioModels model."""
    client = get_client()
    info = client.get_model_info(normalise_model_id(model_id))
    annotations = {}
    if isinstance(info, dict):
        for key in ("annotations", "isDescribedBy", "is", "hasTaxon", "isDerivedFrom"):
            if key in info:
                annotations[key] = info[key]
        if not annotations:
            annotations["metadata"] = info
    return as_json({"model_id": model_id, "annotations": annotations})
