# Skills

**Cursor / agent instruction packs** for BioModels tasks — ClawBio-style layout, lighter than full [ClawBio](https://github.com/ClawBio/ClawBio) skills (no separate Python runner required; uses PraisonAI **toolsets**).

Catalog: `skills/catalog.json`

---

## Available skills (16)

| Skill | Use when |
|-------|----------|
| Search BioModels | Find models by keyword |
| Get model info | Metadata for one ID |
| Load BioModels SBML | Download SBML file |
| Simulate model | Time-course or steady state |
| Ask question | Plain-English Q&A about a model |
| Steady state | Equilibrium concentrations |
| Parameter scan | Sweep a parameter range |
| SBML summarise | Structure overview |
| SBML validate | Check SBML file |
| Compare models | Two models side by side |
| Rank models | Sort search results |
| Trust scorecard | Curation quality |
| Query article | Linked publications |
| SED-ML parse | Read experiment definitions |
| SysBio orchestrator | Multi-step pipeline |
| Repro enforcer | Export study bundle |

<details markdown="1">
<summary>Developer: how skills are registered</summary>

Catalog: `skills/catalog.json` · Template: `skills/SKILL-TEMPLATE.md`

See sections below for adding new skills.
</details>

---

## Legacy table (core five)

| Skill | ID | Use when |
|-------|-----|----------|
| Search BioModels | `search-models` | Find curated models for a pathway or keyword |
| Load BioModels SBML | `load-biomodel` | Download and inspect SBML on disk |
| Simulate Model | `simulate-model` | Run BASICO time-course or steady state |
| SysBio Orchestrator | `sysbio-orchestrator` | Multi-step discovery → simulate pipeline |
| Reproducibility Enforcer | `repro-enforcer` | Export repro bundles with checksums |

---

## PraisonAIBio vs ClawBio skills

| | **PraisonAIBio** | **ClawBio** (`~/ClawBio`) |
|---|------------------|---------------------------|
| Purpose | Systems biology / BioModels / SBML | Genomics, WES, RNA-seq, etc. |
| Implementation | Markdown + PraisonAI `@tool` functions | Often `SKILL.md` + Python script + tests |
| Registration | `skills/catalog.json` via `generate_catalog.py` | `catalog.json` + `clawbio.py` aliases |
| Scaffold | Copy `SKILL-TEMPLATE.md` | Use `skill-builder` meta-skill |
| Bridge | `mcp/clawbio-bridge/` (v2) | N/A |

For heavy genomics pipelines, use ClawBio directly. For BioModels discovery and simulation, use PraisonAIBio skills + toolsets.

---

## How to add a new skill

### 1. Create the folder

Use a **kebab-case** id (matches directory name):

```bash
mkdir -p skills/my-skill-id
cp skills/SKILL-TEMPLATE.md skills/my-skill-id/SKILL.md
```

### 2. Edit `SKILL.md`

Required sections (see template):

1. **Title** — first line `# Title` (used as display name in catalog)
2. **When to use** — trigger scenarios for the agent
3. **Tools** — list tools with **parameters** (agents only see parameters, not env vars)
4. **Toolset** — which prebuilt toolset to attach (`biomodels-readonly`, `simulation`, …)
5. **Example** — minimal `Agent` snippet loading this skill as `instructions`

Optional: prerequisites (`[simulation]` extra), demo model ID.

!!! tip
    Copy an existing skill as a starting point:
    `cp -r skills/search-models skills/my-skill-id`

### 3. Regenerate the catalog

```bash
python scripts/generate_catalog.py
```

This scans `skills/*/SKILL.md` and rewrites `skills/catalog.json`.

### 4. Validate

```bash
python scripts/validate_repo.py   # skills section must stay OK
python -c "import praisonai_bio"
praisonai-bio validate check
```

### 5. Test with an agent

```python
import praisonai_bio
from praisonaiagents import Agent

agent = Agent(
    name="test",
    instructions=open("skills/my-skill-id/SKILL.md").read(),
    toolsets=["biomodels-readonly"],  # match your SKILL.md
    llm="gpt-4o-mini",
)
print(agent.start("Your test prompt"))
```

### 6. Document and submit

- Add a row to the table above (this page) if the skill is public
- Open a pull request with `SKILL.md`, updated `catalog.json`, and any tests

**Optional extras** (like ClawBio, but not required for PraisonAIBio):

```
skills/my-skill-id/
├── SKILL.md           # required
├── examples/          # optional sample prompts or output
└── tests/             # optional pytest for helper scripts
```

---

## Use with Cursor

1. Copy or symlink the skill folder into your Cursor skills directory, **or**
2. Reference the repo path in chat:

```text
Read skills/search-models/SKILL.md and search BioModels for MAPK models.
```

---

## Use with PraisonAI agents

Skills supply **instructions**; toolsets supply **capabilities**:

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

## YAML workflows

Point agent instructions at a skill file in `.praisonai/agents/` or inline in workflow YAML:

```yaml
agents:
  scout:
    role: BioModels Scout
    instructions_file: skills/search-models/SKILL.md
    toolsets:
      - biomodels-readonly
```

(If your PraisonAI version uses `instructions:` instead of `instructions_file:`, paste or load the markdown content.)

---

## See also

- [Toolsets](toolsets.md)
- [Tools reference](tools-reference.md)
- [Workflows](concepts/workflows.md)
- ClawBio skill builder: `~/ClawBio/skills/skill-builder/SKILL.md`
