from praisonaiagents import tool

from praisonai_bio.adapters.sbml_adapter import parse_structure
from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


@tool
def sbml_validate(model_id: str | None = None, sbml_path: str | None = None) -> str:
    """Validate SBML structure and basic unit consistency."""
    from pathlib import Path

    try:
        if sbml_path:
            content = Path(sbml_path).read_bytes()
        elif model_id:
            client = get_client()
            content = client.download_sbml(normalise_model_id(model_id))
        else:
            return as_json({"valid": False, "error": "Provide model_id or sbml_path"})

        structure = parse_structure(content)
        issues = []
        if structure.get("root", "").lower() != "sbml":
            issues.append(f"Root element is {structure.get('root')}, expected sbml")
        for sp in structure.get("species", []):
            if not (sp.get("id") or sp.get("name")):
                issues.append("Species missing id/name")
                break
        counts = structure.get("counts", {})
        return as_json(
            {
                "valid": len(issues) == 0,
                "species_count": counts.get("species", 0),
                "reaction_count": counts.get("reactions", 0),
                "issues": issues,
            }
        )
    except Exception as exc:
        return as_json({"valid": False, "error": str(exc)})
