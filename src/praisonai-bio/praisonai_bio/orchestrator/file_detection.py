"""Detect input type for orchestrator routing."""

from __future__ import annotations

import re
from pathlib import Path


def detect_input_kind(text: str) -> str:
    text = text.strip()
    if re.search(r"BIOMD\d+", text, re.I):
        return "biomodel_id"
    if Path(text).suffix.lower() in {".sbml", ".xml"}:
        return "sbml_file"
    if text.lower().endswith(".pdf"):
        return "pdf"
    return "natural_language"
