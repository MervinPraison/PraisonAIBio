from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


@tool
def sbml_validate(model_id: str | None = None, sbml_path: str | None = None) -> str:
    """Validate SBML structure and basic unit consistency."""
    import xml.etree.ElementTree as ET
    from pathlib import Path

    try:
        if sbml_path:
            content = Path(sbml_path).read_bytes()
        elif model_id:
            client = get_client()
            content = client.download_sbml(normalise_model_id(model_id))
        else:
            return as_json({"valid": False, "error": "Provide model_id or sbml_path"})

        root = ET.fromstring(content)
        tag = root.tag.split("}")[-1] if "}" in root.tag else root.tag
        species = root.findall(".//{*}species") or root.findall(".//species")
        reactions = root.findall(".//{*}reaction") or root.findall(".//reaction")
        issues = []
        if tag.lower() != "sbml":
            issues.append(f"Root element is {tag}, expected sbml")
        for sp in species:
            if not (sp.get("id") or sp.get("name")):
                issues.append("Species missing id/name")
                break
        return as_json(
            {
                "valid": len(issues) == 0,
                "species_count": len(species),
                "reaction_count": len(reactions),
                "issues": issues,
            }
        )
    except ET.ParseError as exc:
        return as_json({"valid": False, "error": str(exc)})
    except Exception as exc:
        return as_json({"valid": False, "error": str(exc)})
