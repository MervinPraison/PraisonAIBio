from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


def _extract_model_level_annotations(info: dict) -> dict:
    """Parse structured BioModels modelLevelAnnotations and Identifiers.org URIs."""
    out: dict = {"terms": [], "identifiers": [], "resources": []}
    annotations = info.get("modelLevelAnnotations") or info.get("modelLevelAnnotation") or []
    if isinstance(annotations, dict):
        annotations = [annotations]
    for block in annotations if isinstance(annotations, list) else []:
        if not isinstance(block, dict):
            continue
        for key in ("is", "isDescribedBy", "hasTaxon", "isDerivedFrom", "occursIn"):
            if key in block:
                out["terms"].append({key: block[key]})
        for uri_key in ("identifier", "uri", "resource"):
            if uri_key in block:
                val = block[uri_key]
                if isinstance(val, str) and "identifiers.org" in val:
                    out["identifiers"].append(val)
                elif isinstance(val, str):
                    out["resources"].append(val)
    # Flat MIRIAM-style keys on root metadata
    for key in ("is", "isDescribedBy", "hasTaxon", "isDerivedFrom"):
        if key in info and key not in out:
            out["terms"].append({key: info[key]})
    return out


@tool
def get_annotation(model_id: str, enrich_ols: bool = False) -> str:
    """Retrieve structured MIRIAM / modelLevelAnnotations for a BioModels model."""
    client = get_client()
    model_id = normalise_model_id(model_id)
    info = client.get_model_info(model_id)
    structured = _extract_model_level_annotations(info) if isinstance(info, dict) else {}
    result = {
        "model_id": model_id,
        "modelLevelAnnotations": structured,
        "curationStatus": info.get("curationStatus") if isinstance(info, dict) else None,
        "name": info.get("name") if isinstance(info, dict) else None,
    }
    if enrich_ols:
        try:
            from praisonai_bio.adapters.ols_adapter import enrich_terms

            result["ols_enrichment"] = enrich_terms(structured.get("identifiers", []))
        except ImportError:
            result["ols_enrichment"] = {"note": "OLS adapter unavailable"}
    return as_json(result)
