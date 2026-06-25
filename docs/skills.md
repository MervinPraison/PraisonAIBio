# Skills

Optional **Cursor / agent skills** under `skills/` — focused instructions for common BioModels tasks.

Catalog: `skills/catalog.json`

---

## Available skills

| Skill | ID | Use when |
|-------|-----|----------|
| Search BioModels | `search-models` | Find curated models for a pathway or keyword |
| Load BioModels SBML | `load-biomodel` | Download and inspect SBML on disk |
| Simulate Model | `simulate-model` | Run BASICO time-course or steady state |
| SysBio Orchestrator | `sysbio-orchestrator` | Multi-step discovery → simulate pipeline |
| Reproducibility Enforcer | `repro-enforcer` | Export repro bundles with checksums |

Each skill lives in `skills/<id>/SKILL.md`.

---

## Use with Cursor

Copy or symlink a skill into your Cursor skills folder, or reference the repo path when configuring agents.

Example — point an agent at the search skill:

```text
Read skills/search-models/SKILL.md and search BioModels for MAPK models.
```

---

## Use with PraisonAI agents

Skills complement **toolsets**, not replace them:

```python
import praisonai_bio
from praisonaiagents import Agent

agent = Agent(
    name="scout",
    instructions=open("skills/search-models/SKILL.md").read(),
    toolsets=["biomodels-readonly"],
    llm="gpt-4o-mini",
)
agent.start("Find curated p53 models")
```

Always run `import praisonai_bio` first.

---

## See also

- [Toolsets](toolsets.md)
- [Workflows](concepts/workflows.md)
- [Recipes](recipes.md)
