import praisonai_bio
from praisonaiagents import Agent

from praisonai_bio.config.presets import DISCOVERY_AGENT
from praisonai_bio.skills.bridge import skills_config_kwargs

agent = Agent(model="gpt-4o-mini", **DISCOVERY_AGENT, **skills_config_kwargs())
print(agent.start("Search BioModels for curated glycolysis models and name one ID."))
