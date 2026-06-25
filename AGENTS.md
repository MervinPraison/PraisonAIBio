# PraisonAIBio — Agent Guide

Extension package for PraisonAI systems biology workflows.

## Layout

- `src/praisonai-bio/praisonai_bio/` — pip package (tools, adapters, toolsets)
- `workflows/` — YAML multi-agent workflows
- `skills/` — SKILL.md + catalog.json (ClawBio-style)
- `recipes/bio/` — PraisonAI wrapper recipes
- `benchmarks/` — T2B parity and orchestrator benchmarks

## Rules

1. Always `import praisonai_bio` before YAML/CLI toolsets
2. BioModels base URL: `https://www.biomodels.org` (override with `BIOMODELS_BASE_URL`)
3. BASICO is optional — lazy import in `adapters/basico_adapter.py`
4. Keep public docs general — no internal funding or private proposal content

## Tool naming

T2B parity: `search_models`, `get_modelinfo`, `load_biomodel`, `simulate_model`, `ask_question`, `steady_state`, `parameter_scan`, `custom_plotter`, `get_annotation`, `query_article`, `save_model`

Discovery extras: `rank_models`, `trust_scorecard`, `compare_models`, `preview_outcomes`, `sbml_summarise`
