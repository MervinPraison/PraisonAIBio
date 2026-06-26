import praisonai_bio
from praisonaiagents import Agent

print(
    Agent(
        name="perturb-analyst",
        toolsets=["simulation"],
        model="gpt-4o-mini",
    ).start("Compare baseline vs perturbed simulation for BIOMD0000000206 using compare_simulations")
)
