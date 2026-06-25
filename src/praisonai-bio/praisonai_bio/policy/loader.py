"""Load BioModels policy packs into the PraisonAI PolicyEngine."""

from __future__ import annotations

import os
from pathlib import Path

_PACK_DIR = Path(__file__).resolve().parents[4] / "policy" / "packs"


def pack_path(name: str = "bio-public") -> Path:
    """Resolve a policy pack YAML path by name."""
    return _PACK_DIR / f"{name}.yaml"


def load_bio_policy(name: str | None = None) -> "PolicyEngine":
    """Load a bio policy pack into a PolicyEngine instance."""
    from praisonaiagents.policy.engine import PolicyEngine

    pack_name = name or os.environ.get("PRAISONAI_POLICY_PACK", "bio-public")
    path = pack_path(pack_name)
    if not path.exists():
        raise FileNotFoundError(f"Bio policy pack not found: {path}")
    engine = PolicyEngine()
    engine.load_from_yaml(str(path))
    return engine


def check_tool_allowed(tool_name: str, policy_name: str | None = None) -> tuple[bool, str]:
    """Return (allowed, reason) for a tool under the given bio policy."""
    engine = load_bio_policy(policy_name)
    result = engine.check(f"tool:{tool_name}", {})
    if result.allowed:
        return True, ""
    return False, result.reason or "denied by policy"
