import praisonai_bio
from praisonaiagents import Agent
print(Agent(name="scout", toolsets=["biomodels-readonly"], llm="gpt-4o-mini").start("Find curated yeast glycolysis models"))
