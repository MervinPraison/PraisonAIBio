from pathlib import Path

from praisonaiagents import tool

from praisonai_bio.adapters.basico_adapter import load_model, save_sbml
from praisonai_bio.tools._helpers import as_json, normalise_model_id


@tool
def save_model(model_id: str, output_path: str) -> str:
    """Save a loaded BioModels SBML model to disk."""
    try:
        model = load_model(model_id=normalise_model_id(model_id))
        path = save_sbml(model, output_path)
        return as_json({"model_id": model_id, "saved_to": str(Path(path).resolve())})
    except ImportError as exc:
        return as_json({"error": str(exc)})
    except Exception as exc:
        return as_json({"error": str(exc)})
