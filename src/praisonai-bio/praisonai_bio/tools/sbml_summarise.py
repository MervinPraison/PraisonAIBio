from praisonaiagents import tool

from praisonai_bio.adapters.sbml_adapter import parse_structure, to_graph
from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


@tool
def sbml_summarise(model_id: str, include_graph: bool = False) -> str:
    """Summarise species, compartments, reactions, and parameters from SBML."""
    client = get_client()
    model_id = normalise_model_id(model_id)
    info = client.get_model_info(model_id)
    summary: dict = {"model_id": model_id}

    if isinstance(info, dict):
        for key in ("name", "description", "curationStatus", "species", "reactions", "compartments", "parameters"):
            if key in info:
                summary[key] = info[key]
        if len(summary) == 1:
            summary["metadata"] = info

    try:
        structure = parse_structure(client.download_sbml(model_id))
        summary["structure"] = structure.get("counts", {})
        summary["model_element_id"] = structure.get("model_id")
        if include_graph:
            summary["graph"] = to_graph(structure)
    except Exception as exc:
        summary["structure_error"] = str(exc)

    return as_json(summary)
