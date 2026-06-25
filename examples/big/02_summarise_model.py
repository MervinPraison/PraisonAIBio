import praisonai_bio
from praisonaiagents import Agent
print(Agent(name="analyst", toolsets=["sbml_analysis"], llm="gpt-4o-mini").start("Summarise BIOMD0000000206"))
