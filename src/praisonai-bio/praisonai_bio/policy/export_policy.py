"""Export path policy — restrict writes outside bundle directories."""

from __future__ import annotations

from pathlib import Path

ALLOWED_ROOTS = [
    Path.home() / ".praisonai" / "biomodels-runs",
    Path("demo_data"),
    Path("bundles"),
]


def is_allowed_export_path(path: str) -> bool:
    target = Path(path).resolve()
    for root in ALLOWED_ROOTS:
        try:
            root.resolve()
            if str(target).startswith(str(root.resolve())):
                return True
        except OSError:
            continue
    return target.name.endswith(".png") or target.name.endswith(".sbml")
