"""SBML read/write policy."""

from __future__ import annotations

from pathlib import Path


def allow_sbml_read(path: str) -> bool:
    return Path(path).suffix.lower() in {".sbml", ".xml", ""}


def allow_sbml_write(path: str) -> bool:
    p = Path(path)
    if p.suffix.lower() not in {".sbml", ".xml"}:
        return False
    blocked = ("/etc/", "/usr/", "/bin/")
    s = str(p.resolve()) if p.exists() else str(p)
    return not any(b in s for b in blocked)
