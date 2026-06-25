import praisonai_bio
from praisonaiagents import Agent
print(Agent(name="sim", toolsets=["simulation"], llm="gpt-4o-mini").start("Simulate BIOMD0000000206 for 10 time units"))
