"""Hook and policy gate tests."""

from __future__ import annotations

from types import SimpleNamespace


def _event(tool_name: str, tool_input: dict | None = None):
    return SimpleNamespace(
        tool_name=tool_name,
        tool_input=tool_input or {},
        extra={"tool_name": tool_name, "tool_input": tool_input or {}},
    )


def test_bio_policy_gate_blocks_save_under_public(monkeypatch):
    monkeypatch.setenv("PRAISONAI_POLICY_PACK", "bio-public")
    from praisonai_bio.hooks.policy_gate import bio_policy_gate

    result = bio_policy_gate(_event("save_model", {"output_path": "/tmp/out.sbml"}))
    assert result is not None
    assert result.decision == "block"


def test_bio_policy_gate_allows_search(monkeypatch):
    monkeypatch.setenv("PRAISONAI_POLICY_PACK", "bio-public")
    from praisonai_bio.hooks.policy_gate import bio_policy_gate

    result = bio_policy_gate(_event("search_models", {"query": "glycolysis"}))
    assert result is not None
    assert result.decision == "allow"


def test_bio_policy_gate_allows_lab_save(monkeypatch):
    monkeypatch.setenv("PRAISONAI_POLICY_PACK", "bio-lab")
    from praisonai_bio.hooks.policy_gate import bio_policy_gate

    result = bio_policy_gate(_event("save_model", {"output_path": "/tmp/out.sbml"}))
    assert result is not None
    assert result.decision == "allow"
