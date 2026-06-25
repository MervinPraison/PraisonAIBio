"""Lazy BASICO/COPASI adapter for SBML simulation."""

from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Any


def check_basico_available() -> tuple[bool, str]:
    try:
        import basico  # noqa: F401
        return True, ""
    except ImportError:
        return False, "Install simulation support: pip install praisonai-bio[simulation]"


def load_model(model_id: str | None = None, sbml_path: str | None = None) -> Any:
    ok, msg = check_basico_available()
    if not ok:
        raise ImportError(msg)
    from basico import load_model as basico_load

    if sbml_path:
        return basico_load(Path(sbml_path))
    if model_id:
        from basico.biomodels import load_biomodel
        return load_biomodel(model_id)
    raise ValueError("Provide model_id or sbml_path")


def run_timecourse(
    model: Any,
    duration: float = 100.0,
    step: float = 0.1,
    use_reactions: bool = False,
) -> Any:
    ok, msg = check_basico_available()
    if not ok:
        raise ImportError(msg)
    from basico import run_timecourse as basico_run

    return basico_run(model, duration=duration, step=step, use_reactions=use_reactions)


def run_steady_state(model: Any) -> dict[str, Any]:
    ok, msg = check_basico_available()
    if not ok:
        raise ImportError(msg)
    from basico import get_steady_state_concentrations

    conc = get_steady_state_concentrations(model)
    return {"steady_state": conc.to_dict() if hasattr(conc, "to_dict") else str(conc)}


def save_sbml(model: Any, path: str) -> str:
    ok, msg = check_basico_available()
    if not ok:
        raise ImportError(msg)
    from basico import save_model

    save_model(model, path)
    return path


def write_temp_sbml(content: bytes) -> str:
    fd, path = tempfile.mkstemp(suffix=".xml")
    with open(fd, "wb") as f:
        f.write(content)
    return path
