from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


@tool
def trust_scorecard(model_id: str) -> str:
    """Score model trustworthiness from curation status, publication, and metadata."""
    client = get_client()
    info = client.get_model_info(normalise_model_id(model_id))
    score = 0
    reasons = []
    if isinstance(info, dict):
        curation = str(info.get("curationStatus", info.get("curationstatus", ""))).lower()
        if "curated" in curation:
            score += 40
            reasons.append("Manually curated on BioModels")
        if info.get("publication") or info.get("doi"):
            score += 30
            reasons.append("Linked publication")
        if info.get("authors"):
            score += 15
            reasons.append("Author metadata present")
        if info.get("name"):
            score += 15
            reasons.append("Named model entry")
    return as_json({"model_id": model_id, "trust_score": min(score, 100), "reasons": reasons, "metadata": info})
