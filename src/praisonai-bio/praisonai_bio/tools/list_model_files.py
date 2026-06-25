from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


@tool
def list_model_files(model_id: str) -> str:
    """List all files attached to a BioModels entry (SBML, SED-ML, figures, archives)."""
    try:
        client = get_client()
        model_id = normalise_model_id(model_id)
        files = client.list_files(model_id)
        if isinstance(files, list):
            return as_json({"model_id": model_id, "files": files, "count": len(files)})
        entries = files.get("files", files.get("entries", []))
        return as_json({"model_id": model_id, "files": entries, "count": len(entries), "raw": files})
    except Exception as exc:
        return as_json({"error": str(exc)})
