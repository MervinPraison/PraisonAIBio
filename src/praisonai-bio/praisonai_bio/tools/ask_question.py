from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


@tool
def ask_question(model_id: str, question: str) -> str:
    """Answer a natural-language question about a BioModels model using its metadata."""
    client = get_client()
    model_id = normalise_model_id(model_id)
    info = client.get_model_info(model_id)
    summary = {
        "model_id": model_id,
        "question": question,
        "metadata": info,
        "answer_hint": (
            "Use metadata above with an LLM agent for full reasoning. "
            "Key fields: name, description, authors, publication, species, reactions."
        ),
    }
    return as_json(summary)
