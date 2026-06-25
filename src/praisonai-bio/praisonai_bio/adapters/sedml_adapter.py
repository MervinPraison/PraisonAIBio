"""Extract simulation parameters from SED-ML documents."""

from __future__ import annotations

import xml.etree.ElementTree as ET
from typing import Any


def parse_simulation_params(content: bytes) -> dict[str, Any]:
    """Parse duration and step from the first uniformTimeCourse in SED-ML."""
    root = ET.fromstring(content)
    for sim in root.findall(".//{*}uniformTimeCourse"):
        initial = sim.get("initialTime") or sim.get("initial")
        end = sim.get("outputEndTime") or sim.get("end")
        step = sim.get("outputStepSize") or sim.get("step")
        try:
            duration = float(end) - float(initial) if end is not None and initial is not None else None
            step_f = float(step) if step is not None else None
        except (TypeError, ValueError):
            duration, step_f = None, None
        return {
            "initial_time": initial,
            "end_time": end,
            "step": step_f,
            "duration": duration,
            "task_ids": [el.get("id") for el in root.findall(".//{*}task") if el.get("id")],
        }
    return {"duration": None, "step": None, "task_ids": []}
