from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


@tool
def query_article(model_id: str) -> str:
    """Return publication and citation metadata linked to a BioModels model."""
    client = get_client()
    info = client.get_model_info(normalise_model_id(model_id))
    pub = {}
    if isinstance(info, dict):
        for key in ("publication", "publications", "reference", "doi", "pubmedId", "authors"):
            if key in info:
                pub[key] = info[key]
        if not pub:
            pub = {k: v for k, v in info.items() if "pub" in k.lower() or "doi" in k.lower()}
    return as_json({"model_id": model_id, "publication": pub or info})
