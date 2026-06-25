from praisonaiagents import tool

from praisonai_bio.knowledge.article_index import index_publication, lookup_publication, search_index
from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


@tool
def query_article(model_id: str, query: str | None = None) -> str:
    """Return publication metadata linked to a BioModels model; optional local index search."""
    model_id = normalise_model_id(model_id)
    cached = lookup_publication(model_id)
    client = get_client()
    info = client.get_model_info(model_id)
    pub = {}
    if isinstance(info, dict):
        for key in ("publication", "publications", "reference", "doi", "pubmedId", "authors"):
            if key in info:
                pub[key] = info[key]
        if not pub:
            pub = {k: v for k, v in info.items() if "pub" in k.lower() or "doi" in k.lower()}
    if pub:
        index_publication(model_id, {"publication": pub})
    result = {"model_id": model_id, "publication": pub or info, "cached": cached is not None}
    if query:
        result["index_hits"] = search_index(query)
    return as_json(result)
