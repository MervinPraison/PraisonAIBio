"""Knowledge index tests."""

from __future__ import annotations

import json


def test_index_publication_writes_file(tmp_path, monkeypatch):
    from praisonai_bio.knowledge import article_index

    monkeypatch.setattr(article_index, "_INDEX_DIR", tmp_path)
    result = article_index.index_publication(
        "BIOMD0000000999",
        {"title": "Test model", "doi": "10.0000/test"},
    )
    assert result["indexed"] is True
    path = tmp_path / "BIOMD0000000999.json"
    assert path.exists()
    data = json.loads(path.read_text())
    assert data["title"] == "Test model"


def test_search_index_finds_record(tmp_path, monkeypatch):
    from praisonai_bio.knowledge import article_index

    monkeypatch.setattr(article_index, "_INDEX_DIR", tmp_path)
    article_index.index_publication("BIOMD0000000999", {"title": "Glycolysis yeast"})
    hits = article_index.search_index("glycolysis")
    assert hits
    assert hits[0]["model_id"] == "BIOMD0000000999"
