from praisonaiagents import tool

from praisonai_bio.adapters.sbml_adapter import parse_structure, to_graph
from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


@tool
def sbml_to_graph(model_id: str | None = None, sbml_path: str | None = None) -> str:
    """Convert SBML species–reaction structure into a graph (nodes and edges)."""
    from pathlib import Path

    try:
        if sbml_path:
            content = Path(sbml_path).read_bytes()
        elif model_id:
            client = get_client()
            content = client.download_sbml(normalise_model_id(model_id))
        else:
            return as_json({"error": "Provide model_id or sbml_path"})

        structure = parse_structure(content)
        graph = to_graph(structure)
        return as_json({"model_id": model_id, "graph": graph})
    except Exception as exc:
        return as_json({"error": str(exc)})
