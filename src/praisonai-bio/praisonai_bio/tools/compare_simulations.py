import json

from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json


@tool
def compare_simulations(baseline_json: str, perturbation_json: str) -> str:
    """Compare baseline vs perturbation simulation outputs (JSON strings)."""
    try:
        baseline = json.loads(baseline_json) if isinstance(baseline_json, str) else baseline_json
        perturbed = json.loads(perturbation_json) if isinstance(perturbation_json, str) else perturbation_json
        b_prev = baseline.get("result_preview", baseline)
        p_prev = perturbed.get("result_preview", perturbed)
        return as_json(
            {
                "baseline_keys": list(b_prev.keys()) if isinstance(b_prev, dict) else [],
                "perturbation_keys": list(p_prev.keys()) if isinstance(p_prev, dict) else [],
                "parameter_changed": perturbed.get("parameter"),
                "status": "compared",
            }
        )
    except Exception as exc:
        return as_json({"error": str(exc)})
