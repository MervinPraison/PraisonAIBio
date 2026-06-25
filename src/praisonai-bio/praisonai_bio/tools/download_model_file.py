import base64

from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


@tool
def download_model_file(model_id: str, filename: str | None = None, as_text: bool = False) -> str:
    """Download a specific file or COMBINE archive from a BioModels entry."""
    try:
        client = get_client()
        model_id = normalise_model_id(model_id)
        if filename:
            content = client.download_file(model_id, filename)
            kind = "file"
        else:
            content = client.download_combine_archive(model_id)
            kind = "combine_archive"
        if as_text:
            try:
                payload = content.decode("utf-8")
            except UnicodeDecodeError:
                payload = base64.b64encode(content).decode("ascii")
                kind = f"{kind}_base64"
        else:
            payload = base64.b64encode(content).decode("ascii")
            kind = f"{kind}_base64"
        return as_json(
            {
                "model_id": model_id,
                "filename": filename,
                "kind": kind,
                "size_bytes": len(content),
                "content": payload[:8000] if len(payload) > 8000 else payload,
                "truncated": len(payload) > 8000,
            }
        )
    except Exception as exc:
        return as_json({"error": str(exc)})
