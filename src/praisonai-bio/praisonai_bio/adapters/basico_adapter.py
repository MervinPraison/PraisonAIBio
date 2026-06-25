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
        from praisonai_bio.tools._helpers import get_client, normalise_model_id

        client = get_client()
        sbml_bytes = client.download_sbml(normalise_model_id(model_id))
        path = write_temp_sbml(sbml_bytes)
        return basico_load(Path(path))
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
    from basico import run_time_course

    step_number = max(int(duration / step), 1)
    return run_time_course(model=model, duration=duration, step_number=step_number)


def run_steady_state(model: Any) -> dict[str, Any]:
    ok, msg = check_basico_available()
    if not ok:
        raise ImportError(msg)
    from basico import run_steadystate

    status = run_steadystate(model=model)
    return {"steady_state_status": status, "ok": status == 1}


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
