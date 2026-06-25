from pathlib import Path

from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id
from praisonai_bio.tools.sbml_to_graph import sbml_to_graph


@tool
def get_reaction_graph(
    model_id: str,
    filename: str | None = None,
    output_dir: str | None = None,
) -> str:
    """Download BioModels auto-generated reaction graph (PNG/SVG) or fall back to sbml_to_graph."""
    model_id = normalise_model_id(model_id)
    client = get_client()
    try:
        files = client.list_files(model_id)
        candidates = files if isinstance(files, list) else files.get("files", [])
        graph_names = []
        for item in candidates:
            name = item.get("filename") or item.get("name") or ""
            lower = name.lower()
            if lower.endswith(".png") or lower.endswith(".svg") or "graph" in lower:
                graph_names.append(name)
        chosen = filename or (graph_names[0] if graph_names else None)
        if chosen:
            content = client.download_file(model_id, chosen)
            if output_dir:
                out = Path(output_dir)
                out.mkdir(parents=True, exist_ok=True)
                dest = out / Path(chosen).name
                dest.write_bytes(content)
                return as_json({"model_id": model_id, "file": str(dest), "format": Path(chosen).suffix})
            return as_json(
                {
                    "model_id": model_id,
                    "filename": chosen,
                    "size_bytes": len(content),
                    "note": "Set output_dir to save the graph file locally",
                }
            )
    except Exception as exc:
        fallback = sbml_to_graph.run(model_id=model_id)
        return as_json({"model_id": model_id, "download_error": str(exc), "sbml_graph": fallback})
    return sbml_to_graph.run(model_id=model_id)
