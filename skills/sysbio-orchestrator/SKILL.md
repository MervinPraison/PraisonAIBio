# SysBio Orchestrator

Multi-agent discovery pipeline for BioModels.org.

## Workflow

1. Intake → decompose question
2. Scout → rank models
3. Curation review → trust scorecard
4. SBML analyst → assumptions
5. Simulation engineer → baseline
6. Report writer → final output

## Run

```bash
import praisonai_bio
praisonai workflow run workflows/discovery/biomodels_discovery_pipeline.yaml
export PRAISONAI_RECIPE_PATH=recipes/bio && praisonai recipe run biomodels-discovery
```

## Toolset

`sysbio-orchestrator` — discovery tools plus optional SDK `schedule_add` for longitudinal studies.

## SDK Skills bridge

Register bio skills via `PRAISONAI_SKILLS_PATH=skills` or point SDK `SkillsConfig` at this repo's `skills/catalog.json`.
