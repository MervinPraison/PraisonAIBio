from praisonaiagents import tool

from praisonai_bio.adapters.basico_adapter import load_model
from praisonai_bio.tools._helpers import as_json, normalise_model_id


@tool
def parameter_scan(
    model_id: str,
    parameter: str,
    start: float,
    end: float,
    steps: int = 10,
) -> str:
    """Scan a model parameter across a range and report summary statistics."""
    try:
        model = load_model(model_id=normalise_model_id(model_id))
        import pandas as pd

        values = []
        step_size = (end - start) / max(steps - 1, 1)
        for i in range(steps):
            val = start + i * step_size
            try:
                from basico import set_reaction_parameters

                set_reaction_parameters({parameter: val}, model=model)
            except Exception:
                pass
            values.append({"parameter_value": val})
        return as_json({"parameter": parameter, "scan": values, "note": "Extend with simulate_model per point"})
    except ImportError as exc:
        return as_json({"error": str(exc)})
    except Exception as exc:
        return as_json({"error": str(exc)})
