from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json, extract_models, get_client
from praisonai_bio.adapters.biomodels_api import BioModelsClient


@tool
def rank_models(query: str, num_results: int = 10, research_question: str = "") -> str:
    """Rank BioModels search results by relevance to a research question."""
    client = get_client()
    q = BioModelsClient.curated_filter(query)
    raw = client.search(query=q, num_results=num_results)
    models = extract_models(raw)
    ranked = []
    question_tokens = set(research_question.lower().split()) if research_question else set()
    for m in models:
        text = " ".join(str(v) for v in m.values()).lower() if isinstance(m, dict) else str(m).lower()
        score = sum(1 for t in question_tokens if t in text) if question_tokens else 1
        ranked.append({"model": m, "relevance_score": score})
    ranked.sort(key=lambda x: x["relevance_score"], reverse=True)
    return as_json({"query": q, "research_question": research_question, "ranked": ranked})
