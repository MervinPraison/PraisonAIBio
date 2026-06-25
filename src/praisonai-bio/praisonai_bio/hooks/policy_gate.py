"""Export path policy gate for write tools."""

from __future__ import annotations

import os
from typing import Any

from praisonai_bio.policy.export_policy import is_allowed_export_path

_WRITE_TOOLS = frozenset({"save_model", "repro_export", "custom_plotter"})
_PATH_KEYS = ("output_dir", "output_path", "path", "filename", "save_path")
_DEFAULT_POLICY = "bio-lab"
_LAB_ONLY_TOOLS = frozenset({"simulate_perturbation", "parameter_scan", "save_model"})


def _active_policy_name() -> str:
    return os.environ.get("PRAISONAI_POLICY_PACK", _DEFAULT_POLICY)


def _extract_path(tool_input: dict[str, Any]) -> str:
    for key in _PATH_KEYS:
        value = tool_input.get(key)
        if value:
            return str(value)
    return ""


def bio_policy_gate(event: Any) -> Any:
    """Block tools denied by bio policy packs and disallowed export paths."""
    try:
        from praisonaiagents.hooks.types import HookResult
    except ImportError:
        return None

    tool_name = getattr(event, "tool_name", "") or event.extra.get("tool_name", "")
    policy_name = _active_policy_name()

    try:
        from praisonai_bio.policy.loader import check_tool_allowed

        allowed, reason = check_tool_allowed(tool_name, policy_name)
        if not allowed:
            return HookResult.block(reason or f"Tool {tool_name} denied by {policy_name}")
        if policy_name == "bio-public" and tool_name in _LAB_ONLY_TOOLS:
            return HookResult.block(f"Tool {tool_name} requires bio-lab policy")
    except FileNotFoundError:
        pass

    if tool_name not in _WRITE_TOOLS:
        return HookResult.allow()

    tool_input = getattr(event, "tool_input", None) or event.extra.get("tool_input") or {}
    path = _extract_path(tool_input)
    if path and not is_allowed_export_path(path):
        return HookResult.block(f"Export path not allowed by bio policy: {path}")
    return HookResult.allow()
