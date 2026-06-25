"""BioModels.org REST API client (https://www.biomodels.org)."""

from __future__ import annotations

import os
from typing import Any
from urllib.parse import quote

DEFAULT_BASE_URL = "https://www.biomodels.org"


def get_base_url() -> str:
    return os.environ.get("BIOMODELS_BASE_URL", DEFAULT_BASE_URL).rstrip("/")


class BioModelsClient:
    """Thin REST client for BioModels.org."""

    def __init__(self, base_url: str | None = None, timeout: float = 30.0) -> None:
        self.base_url = (base_url or get_base_url()).rstrip("/")
        self.timeout = timeout

    def _get(self, path: str, params: dict[str, Any] | None = None) -> Any:
        import httpx

        url = f"{self.base_url}/{path.lstrip('/')}"
        with httpx.Client(timeout=self.timeout, follow_redirects=True) as client:
            response = client.get(url, params=params or {})
            response.raise_for_status()
            if "json" in (response.headers.get("content-type") or ""):
                return response.json()
            return response.text

    def search(
        self,
        query: str,
        offset: int = 0,
        num_results: int = 10,
        sort: str | None = None,
    ) -> dict[str, Any]:
        params: dict[str, Any] = {
            "query": query,
            "offset": offset,
            "numResults": num_results,
            "format": "json",
        }
        if sort:
            params["sort"] = sort
        return self._get("search", params)

    def get_model_info(self, model_id: str) -> dict[str, Any]:
        model_id = model_id.strip().upper()
        return self._get(model_id, {"format": "json"})

    def list_files(self, model_id: str) -> dict[str, Any]:
        model_id = model_id.strip().upper()
        return self._get(f"model/files/{model_id}", {"format": "json"})

    def download_sbml(self, model_id: str, filename: str | None = None) -> bytes:
        import httpx

        model_id = model_id.strip().upper()
        if not filename:
            files = self.list_files(model_id)
            candidates = files if isinstance(files, list) else files.get("files", [])
            for item in candidates:
                name = item.get("filename") or item.get("name") or ""
                if name.endswith(".xml") or name.endswith(".sbml"):
                    filename = name
                    break
            if not filename:
                filename = f"{model_id}_url.xml"
        url = f"{self.base_url}/model/download/{model_id}"
        with httpx.Client(timeout=self.timeout, follow_redirects=True) as client:
            response = client.get(url, params={"filename": filename})
            response.raise_for_status()
            return response.content

    def download_sedml(self, model_id: str, filename: str) -> bytes:
        import httpx

        model_id = model_id.strip().upper()
        url = f"{self.base_url}/model/download/{model_id}"
        with httpx.Client(timeout=self.timeout, follow_redirects=True) as client:
            response = client.get(url, params={"filename": filename})
            response.raise_for_status()
            return response.content

    @staticmethod
    def curated_filter(query: str, curated_only: bool = True) -> str:
        if not curated_only:
            return query
        token = 'curationstatus:"Manually curated"'
        if token.lower() in query.lower():
            return query
        return f"{query} AND {token}" if query else token
