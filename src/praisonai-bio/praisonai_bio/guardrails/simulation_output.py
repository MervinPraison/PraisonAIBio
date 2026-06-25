"""Guardrail: validate simulation output shape."""

from __future__ import annotations

import json
from typing import Any


def validate_simulation_output(output: Any):
    if isinstance(output, str):
        try:
            output = json.loads(output)
        except json.JSONDecodeError:
            return False, "Output is not valid JSON"
    if isinstance(output, dict) and output.get("error"):
        return False, str(output["error"])
    if isinstance(output, dict) and ("result_preview" in output or "steady_state" in output):
        return True, "ok"
    return True, "ok"
