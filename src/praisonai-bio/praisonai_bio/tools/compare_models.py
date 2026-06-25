from praisonaiagents import tool

from praisonai_bio.adapters.sbml_adapter import parse_structure
from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


def _summary_fields(info: dict) -> dict:
    keys = ("name", "description", "curationStatus", "species", "reactions", "compartments", "parameters")
    return {k: info[k] for k in keys if k in info}


def _entity_ids(structure: dict) -> tuple[set[str], set[str]]:
    species = {s["id"] for s in structure.get("species", []) if s.get("id")}
    reactions = {r["id"] for r in structure.get("reactions", []) if r.get("id")}
    return species, reactions


@tool
def compare_models(model_id_a: str, model_id_b: str, include_structure: bool = False) -> str:
    """Compare metadata, curation, and optional SBML structure of two BioModels entries."""
    client = get_client()
    a_id = normalise_model_id(model_id_a)
    b_id = normalise_model_id(model_id_b)
    info_a = client.get_model_info(a_id)
    info_b = client.get_model_info(b_id)

    comparison = {
        "model_a": {"id": a_id, "summary": _summary_fields(info_a) if isinstance(info_a, dict) else info_a},
        "model_b": {"id": b_id, "summary": _summary_fields(info_b) if isinstance(info_b, dict) else info_b},
        "same_name": (
            isinstance(info_a, dict)
            and isinstance(info_b, dict)
            and info_a.get("name") == info_b.get("name")
        ),
    }

    if include_structure:
        try:
            struct_a = parse_structure(client.download_sbml(a_id))
            struct_b = parse_structure(client.download_sbml(b_id))
            sp_a, rx_a = _entity_ids(struct_a)
            sp_b, rx_b = _entity_ids(struct_b)
            comparison["structure"] = {
                "species_delta": struct_a["counts"]["species"] - struct_b["counts"]["species"],
                "reaction_delta": struct_a["counts"]["reactions"] - struct_b["counts"]["reactions"],
                "model_a_counts": struct_a["counts"],
                "model_b_counts": struct_b["counts"],
                "shared_species_ids": sorted(sp_a & sp_b),
                "shared_reaction_ids": sorted(rx_a & rx_b),
                "unique_species_a": sorted(sp_a - sp_b)[:20],
                "unique_species_b": sorted(sp_b - sp_a)[:20],
            }
        except Exception as exc:
            comparison["structure_error"] = str(exc)

    return as_json(comparison)
