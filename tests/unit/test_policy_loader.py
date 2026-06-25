"""Policy pack loader tests."""

from __future__ import annotations

import pytest


def test_load_bio_public_policy():
    from praisonai_bio.policy.loader import check_tool_allowed, load_bio_policy

    engine = load_bio_policy("bio-public")
    assert engine.get_policy("bio-public") is not None
    allowed, _ = check_tool_allowed("search_models", "bio-public")
    assert allowed is True
    allowed, reason = check_tool_allowed("save_model", "bio-public")
    assert allowed is False
    assert "save_model" in reason


def test_load_bio_lab_allows_save():
    from praisonai_bio.policy.loader import check_tool_allowed

    allowed, _ = check_tool_allowed("save_model", "bio-lab")
    assert allowed is True
