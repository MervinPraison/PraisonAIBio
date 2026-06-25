from pathlib import Path

from praisonaiagents import tool

from praisonai_bio.adapters.basico_adapter import load_model, write_temp_sbml
from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


@tool
def load_biomodel(model_id: str, save_path: str | None = None) -> str:
    """Download and load an SBML model from BioModels.org."""
    client = get_client()
    model_id = normalise_model_id(model_id)
    sbml_bytes = client.download_sbml(model_id)
    path = save_path or write_temp_sbml(sbml_bytes)
    if save_path:
        Path(save_path).write_bytes(sbml_bytes)
    try:
        model = load_model(sbml_path=path)
        return as_json({"model_id": model_id, "path": path, "loaded": True, "model": str(model)})
    except ImportError as exc:
        return as_json({"model_id": model_id, "path": path, "loaded": False, "note": str(exc)})
