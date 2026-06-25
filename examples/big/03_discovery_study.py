"""Agent: search, rank, and recommend a model."""
import praisonai_bio
from praisonaiagents import Agent

agent = Agent(
    name="researcher",
    instructions="Search BioModels, rank candidates, pick the best one. Be brief.",
    toolsets=["sysbio-orchestrator"],
    llm="gpt-4o-mini",
)
question = "Which curated MAPK model best fits cell signalling studies?"
print(agent.start(question))
