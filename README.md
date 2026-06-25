# PraisonAIBio

Open-source AI agents for systems biology: discover, simulate, and compare curated models from [BioModels.org](https://www.biomodels.org) using [PraisonAI](https://github.com/MervinPraison/PraisonAI).

**New here?** → [Documentation](https://mervinpraison.github.io/PraisonAIBio/) · [Get started](docs/get-started.md) · [examples/](examples/)

Build docs locally: `pip install -r docs/requirements.txt && mkdocs serve`

## Quick start

```bash
pip install -e "src/praisonai-bio[simulation]"
python -c "import praisonai_bio"  # registers toolsets
praisonai run --agent biomodels-scout --prompt "Find glycolysis models"
```

Or run the glycolysis cookbook:

```bash
praisonai workflow run workflows/cookbooks/glycolysis_demo.yaml
```

## Features

- **BioModels.org integration** — search, metadata, SBML download via REST
- **T2B tool parity** — 11 Talk2BioModels-compatible tools on PraisonAI
- **Multi-agent workflows** — discovery, assumption review, simulation, perturbation, comparison
- **Toolsets** — `sysbio-core`, `simulation`, `sysbio-full`, `sysbio-orchestrator`, and more
- **Reproducibility** — bundle helpers and benchmark scaffolds
- **CLI / YAML / Python** — same workflows in all three modes

## Install

```bash
pip install praisonai-bio
# Optional simulation (BASICO/COPASI)
pip install "praisonai-bio[simulation,plot]"
```

## Toolsets

| Toolset | Purpose |
|---------|---------|
| `biomodels-readonly` | Search and metadata (safe) |
| `sbml_analysis` | Load and summarise SBML |
| `sysbio-core` | Phase 0 demo (5 core tools + discovery) |
| `simulation` | BASICO simulation and plotting |
| `sysbio-full` | All 11 T2B tools + discovery |
| `sysbio-orchestrator` | Multi-agent pipeline |
| `sysbio-safe` | Read-only, no simulation |

**Important:** `import praisonai_bio` before using toolsets in YAML or CLI.

## Phase 0 demo model

`BIOMD0000000206` — Teusink et al. yeast glycolysis (glycolysis cookbook).

## Development

```bash
pip install -e "src/praisonai-bio[dev,simulation]"
pytest tests/unit -q
python scripts/validate_repo.py   # plan completeness check
praisonai-bio validate check
praisonai-bio tools validate
```

## Tools (21)

T2B parity (11): `search_models`, `get_modelinfo`, `load_biomodel`, `simulate_model`, `ask_question`, `steady_state`, `parameter_scan`, `custom_plotter`, `get_annotation`, `query_article`, `save_model`

Discovery & extras: `rank_models`, `trust_scorecard`, `compare_models`, `preview_outcomes`, `sbml_summarise`, `sbml_validate`, `sedml_parse`, `simulate_perturbation`, `compare_simulations`, `repro_export`

## MCP

```bash
python mcp/sysbio-server/server.py      # all T2B tools
python mcp/biomodels-server/server.py   # read-only
```

## Licence

MIT

## Links

- [BioModels.org](https://www.biomodels.org)
- [PraisonAI](https://github.com/MervinPraison/PraisonAI)
- [Talk2BioModels](https://github.com/coinse/talk2biomodels)
