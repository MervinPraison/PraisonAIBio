from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json, normalise_model_id


@tool
def simulate_perturbation(
    model_id: str,
    parameter: str,
    value: float,
    duration: float = 100.0,
) -> str:
    """Run a simulation with a single parameter override (perturbation scenario)."""
    try:
        from praisonai_bio.adapters.basico_adapter import load_model, run_timecourse

        model = load_model(model_id=normalise_model_id(model_id))
        try:
            from basico import set_reaction_parameters

            set_reaction_parameters({parameter: value}, model=model)
        except Exception:
            pass
        result = run_timecourse(model, duration=duration)
        preview = result.head(10).to_dict() if hasattr(result, "head") else str(result)
        return as_json(
            {
                "model_id": model_id,
                "parameter": parameter,
                "value": value,
                "duration": duration,
                "result_preview": preview,
            }
        )
    except ImportError as exc:
        return as_json({"error": str(exc), "hint": "pip install praisonai-bio[simulation]"})
    except Exception as exc:
        return as_json({"error": str(exc)})
