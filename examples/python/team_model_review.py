"""AgentTeam model review — Python API parity with team_model_review.yaml."""
import praisonai_bio
from praisonaiagents import Agent, AgentTeam, Task

from praisonai_bio.config.presets import DISCOVERY_AGENT, SIMULATION_AGENT

scout = Agent(**{**DISCOVERY_AGENT, "name": "scout", "instructions": "Search and rank BioModels."})
analyst = Agent(name="analyst", instructions="Summarise SBML structure.", toolsets=["sbml_analysis"])
engineer = Agent(**{**SIMULATION_AGENT, "name": "engineer", "instructions": "Run baseline simulation."})

tasks = [
    Task(name="search", description="Find curated glycolysis models", agent=scout),
    Task(name="analyse", description="Summarise top model SBML", agent=analyst),
    Task(name="simulate", description="Simulate BIOMD0000000206 for 50 time units", agent=engineer),
]

team = AgentTeam(agents=[scout, analyst, engineer], tasks=tasks, llm="gpt-4o-mini")
print(team.run())
