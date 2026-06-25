import praisonai_bio
from praisonaiagents import Agent
print(Agent(name="glycolysis", toolsets=["sysbio-full"], llm="gpt-4o-mini").start("Summarise and simulate BIOMD0000000206 briefly"))
