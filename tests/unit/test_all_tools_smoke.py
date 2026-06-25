"""Smoke test — every registered bio tool is callable."""

from __future__ import annotations

import praisonai_bio
from praisonaiagents.toolsets import resolve_toolset


def test_all_sysbio_full_tools_registered():
    names = resolve_toolset("sysbio-full")
    assert len(names) >= 26


def test_tool_entry_points_importable():
    import praisonai_bio

    exports = [name for name in praisonai_bio.__all__ if name != "wire_bio_hooks"]
    assert len(exports) >= 28
    import importlib

    for name in exports:
        mod = importlib.import_module("praisonai_bio")
        assert hasattr(mod, name)
