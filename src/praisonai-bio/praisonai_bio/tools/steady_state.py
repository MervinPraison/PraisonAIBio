from praisonaiagents import tool

from praisonai_bio.adapters.basico_adapter import load_model, run_steady_state
from praisonai_bio.tools._helpers import as_json, normalise_model_id


@tool
def steady_state(model_id: str | None = None, sbml_path: str | None = None) -> str:
    """Compute steady-state concentrations for an SBML model."""
    try:
        model = load_model(
            model_id=normalise_model_id(model_id) if model_id else None,
            sbml_path=sbml_path,
        )
        return as_json(run_steady_state(model))
    except ImportError as exc:
        return as_json({"error": str(exc)})
    except Exception as exc:
        return as_json({"error": str(exc)})
