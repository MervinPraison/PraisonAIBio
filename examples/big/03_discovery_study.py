import praisonai_bio
from praisonaiagents import Agent
print(Agent(name="researcher", toolsets=["sysbio-orchestrator"], llm="gpt-4o-mini").start("Best curated MAPK model for cell signalling?"))
