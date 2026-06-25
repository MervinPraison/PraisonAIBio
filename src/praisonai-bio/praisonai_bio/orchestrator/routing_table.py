"""SysBio orchestrator routing (ClawBio bio-orchestrator pattern)."""

from __future__ import annotations

import re
from typing import Callable

ROUTES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"BIOMD\d+", re.I), "load_biomodel"),
    (re.compile(r"\.sbml$|\.xml$", re.I), "load_biomodel"),
    (re.compile(r"simulate|run|timecourse", re.I), "simulate_model"),
    (re.compile(r"steady\s*state", re.I), "steady_state"),
    (re.compile(r"scan|sensitivity", re.I), "parameter_scan"),
    (re.compile(r"annotat", re.I), "get_annotation"),
    (re.compile(r"plot|visual", re.I), "custom_plotter"),
    (re.compile(r"save|export", re.I), "save_model"),
    (re.compile(r"repro|bundle", re.I), "repro_export"),
    (re.compile(r"search|find|discover", re.I), "search_models"),
]


def route_input(text: str) -> str:
    """Return suggested tool name for user input."""
    for pattern, tool in ROUTES:
        if pattern.search(text):
            return tool
    return "ask_question"
