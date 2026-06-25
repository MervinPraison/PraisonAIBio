import json

from praisonaiagents import tool

from praisonai_bio.eval.simulation_accuracy import compare_trajectories
from praisonai_bio.tools._helpers import as_json


def _series_dict(data: dict) -> dict[str, list[float]]:
    preview = data.get("result_preview", data)
    if not isinstance(preview, dict):
        return {}
    out: dict[str, list[float]] = {}
    for key, val in preview.items():
        if isinstance(val, list) and val and all(isinstance(x, (int, float)) for x in val[:3]):
            out[key] = [float(x) for x in val]
        elif isinstance(val, dict):
            for sub_key, sub_val in val.items():
                if isinstance(sub_val, list) and sub_val:
                    try:
                        out[f"{key}.{sub_key}"] = [float(x) for x in sub_val]
                    except (TypeError, ValueError):
                        continue
    return out


@tool
def compare_simulations(
    baseline_json: str,
    perturbation_json: str,
    step: float = 1.0,
) -> str:
    """Compare baseline vs perturbation simulation outputs with RMSE, peak time, and AUC."""
    try:
        baseline = json.loads(baseline_json) if isinstance(baseline_json, str) else baseline_json
        perturbed = json.loads(perturbation_json) if isinstance(perturbation_json, str) else perturbation_json
        b_prev = _series_dict(baseline if isinstance(baseline, dict) else {})
        p_prev = _series_dict(perturbed if isinstance(perturbed, dict) else {})
        metrics = compare_trajectories(b_prev, p_prev, step=step)
        return as_json(
            {
                "baseline_keys": list(b_prev.keys()),
                "perturbation_keys": list(p_prev.keys()),
                "parameter_changed": perturbed.get("parameter") if isinstance(perturbed, dict) else None,
                "metrics": metrics,
                "status": "compared",
            }
        )
    except Exception as exc:
        return as_json({"error": str(exc)})
