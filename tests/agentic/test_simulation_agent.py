"""Agentic simulation test — requires OPENAI_API_KEY."""

from __future__ import annotations

import os

import pytest


@pytest.mark.agentic
@pytest.mark.skipif(not os.environ.get("OPENAI_API_KEY"), reason="OPENAI_API_KEY not set")
def test_simulation_agent_smoke():
    import praisonai_bio
    from praisonaiagents import Agent

    agent = Agent(
        name="simulation-agent",
        instructions="Use simulate_model on BIOMD0000000206 for 10 time units.",
        toolsets=["simulation"],
        model="gpt-4o-mini",
    )
    result = agent.start("Run a short baseline simulation")
    assert result
    assert len(str(result)) > 20
