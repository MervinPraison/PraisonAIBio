from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


@tool
def sedml_parse(model_id: str, filename: str | None = None) -> str:
    """Parse SED-ML tasks, models, and data generators from a BioModels bundle."""
    import xml.etree.ElementTree as ET

    try:
        client = get_client()
        model_id = normalise_model_id(model_id)
        if not filename:
            files = client.list_files(model_id)
            candidates = files if isinstance(files, list) else files.get("files", [])
            for item in candidates:
                name = item.get("filename") or item.get("name") or ""
                if name.endswith(".sedml") or name.endswith(".sedml.xml"):
                    filename = name
                    break
            if not filename:
                return as_json({"model_id": model_id, "sedml": None, "note": "No SED-ML file found"})
        content = client.download_sedml(model_id, filename)
        root = ET.fromstring(content)
        tasks = [el.get("id") for el in root.findall(".//{*}task") if el.get("id")]
        models = [el.get("id") for el in root.findall(".//{*}model") if el.get("id")]
        generators = [el.get("id") for el in root.findall(".//{*}dataGenerator") if el.get("id")]
        return as_json(
            {
                "model_id": model_id,
                "filename": filename,
                "tasks": tasks,
                "models": models,
                "data_generators": generators,
            }
        )
    except Exception as exc:
        return as_json({"error": str(exc)})
