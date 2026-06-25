# Examples

Copy, run, done. Start with **small** — one tool, no agent. Try **big** when you want an AI assistant.

## Before you run

```bash
pip install -e "src/praisonai-bio"
export OPENAI_API_KEY=your-key   # only for big/ agent examples
```

Always run this once per session:

```bash
python -c "import praisonai_bio"
```

---

## Small (no AI agent)

| File | What it does |
|------|----------------|
| [small/01_search.py](small/01_search.py) | Find models on BioModels.org |
| [small/02_model_info.py](small/02_model_info.py) | Read one model’s details |
| [small/03_trust_score.py](small/03_trust_score.py) | Check if a model is well curated |
| [small/04_validate_sbml.py](small/04_validate_sbml.py) | Check SBML structure |

```bash
python examples/small/01_search.py
```

---

## Big (AI agent)

| File | What it does |
|------|----------------|
| [big/01_find_models.py](big/01_find_models.py) | Agent searches for pathway models |
| [big/02_summarise_model.py](big/02_summarise_model.py) | Agent summarises one model |
| [big/03_discovery_study.py](big/03_discovery_study.py) | Agent runs discovery + ranking |
| [big/04_glycolysis_demo.py](big/04_glycolysis_demo.py) | End-to-end glycolysis demo |

```bash
python examples/big/01_find_models.py
```

---

## YAML (no Python)

```bash
praisonai workflow run workflows/cookbooks/glycolysis_demo.yaml
```

See [docs/quick-tasks.md](../docs/quick-tasks.md).
