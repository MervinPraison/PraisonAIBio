#!/usr/bin/env python3
"""Convert a Jupyter notebook to a repro bundle manifest snippet."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def notebook_cells(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    cells = []
    for cell in data.get("cells", []):
        if cell.get("cell_type") == "code":
            source = cell.get("source", [])
            if isinstance(source, list):
                cells.append("".join(source))
            else:
                cells.append(source)
    return cells


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract code cells from a notebook for repro export")
    parser.add_argument("notebook", type=Path)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    cells = notebook_cells(args.notebook)
    manifest = {"notebook": str(args.notebook), "code_cells": cells}
    text = json.dumps(manifest, indent=2)
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
