from praisonaiagents import tool

from praisonai_bio.adapters.sedml_adapter import parse_simulation_params
from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


@tool
def sedml_simulate(
    model_id: str,
    filename: str | None = None,
    duration: float | None = None,
    step: float | None = None,
) -> str:
    """Run simulation using SED-ML uniformTimeCourse parameters when available."""
    import json

    from praisonai_bio.tools.sedml_parse import sedml_parse

    try:
        model_id = normalise_model_id(model_id)
        client = get_client()
        parsed = json.loads(sedml_parse.run(model_id=model_id, filename=filename))
        if parsed.get("error"):
            return as_json(parsed)

        sedml_duration, sedml_step = duration, step
        sedml_filename = parsed.get("filename")
        if sedml_filename:
            try:
                sedml_bytes = client.download_sedml(model_id, sedml_filename)
                params = parse_simulation_params(sedml_bytes)
                if params.get("duration") is not None and sedml_duration is None:
                    sedml_duration = float(params["duration"])
                if params.get("step") is not None and sedml_step is None:
                    sedml_step = float(params["step"])
                parsed["simulation_params"] = params
            except Exception as exc:
                parsed["simulation_params_error"] = str(exc)

        sedml_duration = sedml_duration if sedml_duration is not None else 100.0
        sedml_step = sedml_step if sedml_step is not None else 0.1

        from praisonai_bio.tools.simulate_model import simulate_model

        sim = json.loads(simulate_model.run(model_id=model_id, duration=sedml_duration, step=sedml_step))
        return as_json(
            {
                "model_id": model_id,
                "sedml": parsed,
                "duration": sedml_duration,
                "step": sedml_step,
                "simulation": sim,
                "mode": "sedml_faithful" if parsed.get("tasks") else "sbml_fallback",
            }
        )
    except ImportError as exc:
        return as_json({"error": str(exc), "hint": "pip install praisonai-bio[simulation]"})
    except Exception as exc:
        return as_json({"error": str(exc)})
