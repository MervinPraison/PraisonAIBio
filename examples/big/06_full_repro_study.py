import praisonai_bio
from praisonaiagents import Agent

print(
    Agent(
        name="repro-publisher",
        toolsets=["repro"],
        model="gpt-4o-mini",
    ).start("Export a repro bundle for BIOMD0000000206 with run_id demo-repro-study")
)
