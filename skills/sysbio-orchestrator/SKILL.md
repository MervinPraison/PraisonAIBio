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
praisonai workflow run workflows/discovery/biomodels_discovery_pipeline.yaml
```

## Toolset

`sysbio-orchestrator`
