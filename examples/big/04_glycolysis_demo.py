"""Glycolysis end-to-end — Teusink model BIOMD0000000206."""
import praisonai_bio
from praisonaiagents import Agent

agent = Agent(
    name="glycolysis",
    instructions="Use BioModels tools. Find, summarise, and preview BIOMD0000000206.",
    toolsets=["sysbio-core"],
    llm="gpt-4o-mini",
)
print(agent.start("Walk me through the Teusink yeast glycolysis model"))
