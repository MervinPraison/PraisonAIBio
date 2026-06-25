"""Skills catalog CI validation."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_catalog_skills_exist():
    catalog = json.loads((ROOT / "skills/catalog.json").read_text(encoding="utf-8"))
    skills = catalog.get("skills", [])
    assert len(skills) >= 16
    for entry in skills:
        path = ROOT / entry["path"]
        assert path.exists(), f"missing skill file: {entry['path']}"
        assert "SKILL.md" in path.name
