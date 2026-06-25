# Examples

Copy, run, done.

---

## Before you run

```bash
pip install -e "src/praisonai-bio"
python -c "import praisonai_bio"
```

Agent examples also need:

```bash
export OPENAI_API_KEY=sk-...
```

---

## Small — no AI agent

One tool, a few lines, no API key.

| Script | What it does |
|--------|--------------|
| `examples/small/01_search.py` | Search BioModels.org |
| `examples/small/02_model_info.py` | Metadata for one model |
| `examples/small/03_trust_score.py` | Curation trust score |
| `examples/small/04_validate_sbml.py` | Validate SBML structure |

```bash
python examples/small/01_search.py
```

---

## Big — AI agent

| Script | What it does |
|--------|--------------|
| `examples/big/01_find_models.py` | Agent search |
| `examples/big/02_summarise_model.py` | Agent summary |
| `examples/big/03_discovery_study.py` | Search + rank + recommend |
| `examples/big/04_glycolysis_demo.py` | Full glycolysis walkthrough |

```bash
python examples/big/04_glycolysis_demo.py
```

---

## YAML — no Python

```bash
praisonai workflow run workflows/cookbooks/glycolysis_demo.yaml
```

See [Workflows](concepts/workflows.md) and [Quick tasks](quick-tasks.md).
