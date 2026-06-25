# PraisonAIBio

**Find, check, and simulate curated systems-biology models** from [BioModels.org](https://www.biomodels.org) — with plain Python, AI agents, or YAML workflows.

Built on [PraisonAI](https://github.com/MervinPraison/PraisonAI).

📖 **Full documentation:** [bio.praison.ai](https://bio.praison.ai)

---

## What you need

| | Required | Optional |
|---|----------|----------|
| **Python 3.10+** | Yes | |
| **`praisonai-bio` package** | Yes | |
| **`import praisonai_bio`** | Yes — registers tools for agents/YAML | |
| **Internet** | Yes — live BioModels.org API | |
| **`OPENAI_API_KEY`** | Only for AI agent examples | |
| **`praisonai` CLI** | Only for YAML workflows | `pip install praisonai` |
| **`[simulation]` extra** | Only to run ODE simulations (BASICO) | `pip install -e "src/praisonai-bio[simulation]"` |

---

## Install (minimum)

```bash
git clone https://github.com/MervinPraison/PraisonAIBio.git
cd PraisonAIBio
pip install -e "src/praisonai-bio"
python -c "import praisonai_bio"
```

Verify:

```bash
praisonai-bio validate check
```

---

## Try it — pick one path

### 1. Direct tool (no AI, no API key)

Search BioModels for glycolysis models:

```bash
python examples/small/01_search.py
```

Sample output: JSON list of curated model IDs and names.  
→ [More small examples](docs/examples/index.md)

### 2. AI agent (needs `OPENAI_API_KEY`)

```bash
export OPENAI_API_KEY=sk-...
python examples/big/01_find_models.py
```

Sample output: plain-English answer with recommended model IDs.  
→ [All agent examples](docs/examples/index.md)

### 3. YAML workflow (needs `praisonai` CLI + API key)

```bash
pip install praisonai
export OPENAI_API_KEY=sk-...
python -c "import praisonai_bio"
praisonai workflow run workflows/cookbooks/glycolysis_demo.yaml
```

Three agents in sequence: find → summarise → simulate **BIOMD0000000206**.  
→ [Workflow guide](docs/concepts/workflows.md)

---

## Demo model

**BIOMD0000000206** — Teusink yeast glycolysis. Used in examples, cookbooks, and docs.

---

## What it includes

- **21 tools** — search, rank, validate SBML, simulate, export repro bundles
- **10 toolsets** — e.g. `biomodels-readonly` (safe), `sysbio-full` (everything)
- **YAML workflows** — discovery pipelines, cookbooks, multi-agent teams
- **MCP servers** — use tools from Cursor / Claude Desktop

Details: [Tools](https://bio.praison.ai/tools-at-a-glance/) · [Toolsets](https://bio.praison.ai/toolsets/) · [Examples with sample output](https://bio.praison.ai/examples/)

---

## Python one-liner

```python
import praisonai_bio
from praisonai_bio.tools.search_models import search_models

print(search_models.run(query="glycolysis", num_results=5))
```

---

## For developers

```bash
pip install -e "src/praisonai-bio[dev,simulation]"
./scripts/test_all.sh
python scripts/validate_repo.py
```

Build docs locally:

```bash
pip install -r docs/requirements.txt && mkdocs serve
```

→ [Development](docs/development.md) · [AGENTS.md](AGENTS.md)

---

## Licence

MIT

## Links

- [Documentation](https://bio.praison.ai)
- [BioModels.org](https://www.biomodels.org)
- [PraisonAI](https://github.com/MervinPraison/PraisonAI)
