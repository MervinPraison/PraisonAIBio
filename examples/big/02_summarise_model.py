"""Agent summarises one BioModels entry."""
import praisonai_bio
from praisonaiagents import Agent

agent = Agent(
    name="analyst",
    instructions="Summarise the model in plain language for a biologist.",
    toolsets=["sbml_analysis"],
    llm="gpt-4o-mini",
)
print(agent.start("Summarise BIOMD0000000206"))
