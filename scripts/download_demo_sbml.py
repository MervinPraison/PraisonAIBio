#!/usr/bin/env python3
"""Download demo SBML files and refresh bundle checksums."""

from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SBML_DIR = ROOT / "demo_data" / "sbml"
BUNDLE = ROOT / "demo_data" / "bundles" / "glycolysis_demo"

DEMO_IDS = ["BIOMD0000000206", "BIOMD0000000012"]


def main() -> None:
    from praisonai_bio.adapters.biomodels_api import BioModelsClient

    SBML_DIR.mkdir(parents=True, exist_ok=True)
    client = BioModelsClient()
    for model_id in DEMO_IDS:
        data = client.download_sbml(model_id)
        path = SBML_DIR / f"{model_id}.xml"
        path.write_bytes(data)
        print(f"Saved {path} ({len(data)} bytes)")

    lines = []
    for p in sorted(BUNDLE.iterdir()):
        if p.is_file() and p.name != "checksums.sha256":
            lines.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}")
    (BUNDLE / "checksums.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Updated {BUNDLE / 'checksums.sha256'}")


if __name__ == "__main__":
    main()
