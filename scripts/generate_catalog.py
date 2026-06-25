#!/usr/bin/env python3
"""Regenerate skills/catalog.json from SKILL.md directories."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"


def main() -> None:
    entries = []
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        title = skill_md.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()
        entries.append(
            {
                "id": skill_dir.name,
                "name": title,
                "path": str(skill_dir.relative_to(ROOT) / "SKILL.md"),
            }
        )
    catalog = {"version": "0.1.0", "skills": entries}
    out = SKILLS_DIR / "catalog.json"
    out.write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out} ({len(entries)} skills)")


if __name__ == "__main__":
    main()
