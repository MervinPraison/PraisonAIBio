"""Real agentic test — requires OPENAI_API_KEY or configured LLM."""

import os

import pytest

pytestmark = pytest.mark.agentic


@pytest.mark.skipif(not os.environ.get("OPENAI_API_KEY"), reason="OPENAI_API_KEY not set")
def test_agent_search_glycolysis():
    import praisonai_bio  # noqa: F401
    from praisonaiagents import Agent

    agent = Agent(
        name="bio-scout",
        instructions="Search BioModels for curated glycolysis models. Reply with one model ID.",
        model="gpt-4o-mini",
        toolsets=["biomodels-readonly"],
    )
    result = agent.start("Find a curated yeast glycolysis model on BioModels.org")
    assert result
    print(result)
