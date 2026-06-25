"""Plan multi-step tool chains for common sysbio tasks."""

from __future__ import annotations

from praisonai_bio.orchestrator.routing_table import route_input

CHAINS: dict[str, list[str]] = {
    "discover_and_simulate": ["search_models", "rank_models", "get_modelinfo", "simulate_model"],
    "assumption_then_sim": ["sbml_summarise", "sbml_validate", "simulate_model"],
    "repro_bundle": ["get_modelinfo", "query_article", "repro_export"],
}


def plan_chain(user_input: str) -> list[str]:
    first = route_input(user_input)
    if first == "search_models":
        return CHAINS["discover_and_simulate"]
    if first == "load_biomodel":
        return CHAINS["assumption_then_sim"]
    if first == "repro_export":
        return CHAINS["repro_bundle"]
    return [first]
