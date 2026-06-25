"""Agent finds curated models — 3 lines of setup."""
import praisonai_bio
from praisonaiagents import Agent

agent = Agent(
    name="scout",
    instructions="Search BioModels.org. Reply with model IDs only.",
    toolsets=["biomodels-readonly"],
    llm="gpt-4o-mini",
)
print(agent.start("Find curated yeast glycolysis models"))
