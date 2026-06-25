# Quick tasks

Pick a task. Copy the command. Run it.

---

## Task 1 — Find models

**Question:** *“What glycolysis models exist?”*

```bash
python examples/small/01_search.py
```

No API key needed.

---

## Task 2 — Inspect one model

**Question:** *“What is BIOMD0000000206?”*

```bash
python examples/small/02_model_info.py
```

Demo model: Teusink yeast glycolysis.

---

## Task 3 — Is this model trustworthy?

**Question:** *“Is this model curated and published?”*

```bash
python examples/small/03_trust_score.py
```

---

## Task 4 — Let AI search for you

**Question:** *“Find MAPK models for me.”*

```bash
export OPENAI_API_KEY=sk-...
python examples/big/01_find_models.py
```

---

## Task 5 — Full discovery study

**Question:** *“Which model should I use for MAPK signalling?”*

```bash
export OPENAI_API_KEY=sk-...
python examples/big/03_discovery_study.py
```

---

## Task 6 — Glycolysis demo (agent)

```bash
export OPENAI_API_KEY=sk-...
python examples/big/04_glycolysis_demo.py
```

---

## Task 7 — Workflow file (multi-step team)

No Python — uses PraisonAI workflow YAML:

```bash
praisonai workflow run workflows/cookbooks/glycolysis_demo.yaml
```

Agents work in sequence: find → summarise → simulate.

---

## Task 8 — Reproducibility bundle

```bash
python -c "
import praisonai_bio
from praisonai_bio.tools.repro_export import repro_export
print(repro_export.run(model_id='BIOMD0000000206', output_dir='/tmp/glycolysis_bundle'))
"
```

Creates `model.sbml`, metadata, and `commands.sh` in the folder.
