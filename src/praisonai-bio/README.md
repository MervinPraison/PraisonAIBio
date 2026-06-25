# praisonai-bio

PraisonAI domain plugin for BioModels.org systems biology.

## Install

```bash
pip install praisonai-bio
# or from source
pip install -e ".[simulation,plot,rag,dev]"
```

## Quick start

```python
import praisonai_bio
from praisonaiagents import Agent
from praisonai_bio.config.presets import DISCOVERY_AGENT

agent = Agent(name="scout", **DISCOVERY_AGENT)
print(agent.start("Find curated glycolysis models"))
```

## Workflows and recipes

```bash
import praisonai_bio  # required before YAML/CLI toolsets
praisonai workflow run workflows/cookbooks/full_platform_pipeline.yaml
export PRAISONAI_RECIPE_PATH=recipes/bio
praisonai recipe run biomodels-discovery --policy bio-public
```

## MCP

```bash
praisonai-bio-mcp
```

Exposes the full `sysbio-full` toolset (26 tools).

## Docs

https://bio.praison.ai
