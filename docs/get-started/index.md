# Get started

Three steps. No biology coding required.

---

## Step 1 — Install

```bash
cd PraisonAIBio
pip install -e "src/praisonai-bio"
python -c "import praisonai_bio"
```

Full guide: [Install](../install.md)

---

## Step 2 — Try a search (no AI)

```bash
python examples/small/01_search.py
```

**You get:** a list of curated models matching “glycolysis”.

---

## Step 3 — Ask an agent (optional)

Set your OpenAI key, then:

```bash
export OPENAI_API_KEY=sk-...
python examples/big/01_find_models.py
```

**You get:** a short answer with recommended model IDs.

---

## What next?

| Goal | Link |
|------|------|
| Interactive walkthrough | [Interactive guide](../interactive-guide.md) |
| Copy-paste task menu | [Quick tasks](../quick-tasks.md) |
| For lab scientists | [For researchers](../for-researchers.md) |
| All examples | [Examples](../examples/index.md) |
| FAQ | [FAQ](../faq.md) |

---

## Quick commands

| Goal | Command |
|------|---------|
| Check one model | `python examples/small/02_model_info.py` |
| Trust / curation score | `python examples/small/03_trust_score.py` |
| Validate SBML | `python examples/small/04_validate_sbml.py` |
| Full glycolysis walkthrough | `python examples/big/04_glycolysis_demo.py` |
| YAML workflow (no Python) | `praisonai workflow run workflows/cookbooks/glycolysis_demo.yaml` |
