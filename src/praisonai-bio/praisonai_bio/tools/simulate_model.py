from praisonaiagents import tool

from praisonai_bio.adapters.basico_adapter import load_model, run_timecourse
from praisonai_bio.tools._helpers import as_json, normalise_model_id


@tool
def simulate_model(
    model_id: str | None = None,
    sbml_path: str | None = None,
    duration: float = 100.0,
    step: float = 0.1,
) -> str:
    """Run a time-course simulation on a BioModels SBML model."""
    try:
        model = load_model(model_id=normalise_model_id(model_id) if model_id else None, sbml_path=sbml_path)
        result = run_timecourse(model, duration=duration, step=step)
        if hasattr(result, "to_dict"):
            data = result.to_dict()
        elif hasattr(result, "head"):
            data = result.head(20).to_dict()
        else:
            data = str(result)
        return as_json({"model_id": model_id, "duration": duration, "result_preview": data})
    except ImportError as exc:
        return as_json({"error": str(exc), "hint": "pip install praisonai-bio[simulation]"})
    except Exception as exc:
        return as_json({"error": str(exc)})
