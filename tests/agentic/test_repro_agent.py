"""Agentic repro export test — requires OPENAI_API_KEY."""

from __future__ import annotations

import os

import pytest


@pytest.mark.agentic
@pytest.mark.skipif(not os.environ.get("OPENAI_API_KEY"), reason="OPENAI_API_KEY not set")
def test_repro_agent_smoke(tmp_path):
    import praisonai_bio
    from praisonaiagents import Agent

    agent = Agent(
        name="publisher",
        instructions="Use repro_export for BIOMD0000000206.",
        toolsets=["repro"],
        model="gpt-4o-mini",
    )
    result = agent.start(f"Export repro bundle to {tmp_path / 'bundle'} with run_id agentic-repro-test")
    assert result
