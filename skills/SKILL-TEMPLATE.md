# Skill name (title case)

One sentence: what this skill helps the agent do.

## When to use

- User asks for …
- Need …

## Prerequisites (optional)

```bash
pip install -e "src/praisonai-bio[simulation]"   # only if simulation tools needed
python -c "import praisonai_bio"
```

## Tools

List PraisonAI tools the agent should use (must match `@tool` parameters):

- `tool_name(arg1, arg2=default)`
- `other_tool(...)`

## Toolset

Recommend one toolset: `biomodels-readonly`, `sbml_analysis`, `simulation`, `sysbio-orchestrator`, etc.

## Example

```python
import praisonai_bio
from praisonaiagents import Agent

agent = Agent(
    name="assistant",
    instructions=open("skills/your-skill-id/SKILL.md").read(),
    toolsets=["biomodels-readonly"],
    llm="gpt-4o-mini",
)
agent.start("Your example prompt here")
```

## Demo model (optional)

`BIOMD0000000206` — Teusink yeast glycolysis
