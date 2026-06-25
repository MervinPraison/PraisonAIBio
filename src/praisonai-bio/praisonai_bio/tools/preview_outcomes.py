from praisonaiagents import tool

from praisonai_bio.tools.simulate_model import simulate_model


@tool
def preview_outcomes(model_id: str, duration: float = 50.0) -> str:
    """Run a short baseline simulation to preview expected dynamic outcomes."""
    return simulate_model(model_id=model_id, duration=duration, step=1.0)
