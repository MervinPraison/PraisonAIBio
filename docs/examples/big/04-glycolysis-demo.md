# Example — Glycolysis walkthrough

**Category:** Big (AI agent) · **Script:** [`examples/big/04_glycolysis_demo.py`](https://github.com/MervinPraison/PraisonAIBio/blob/main/examples/big/04_glycolysis_demo.py)

End-to-end walkthrough of **BIOMD0000000206** — find, summarise, and preview simulation.

---

## How to run

```bash
pip install -e "src/praisonai-bio[simulation]"
export OPENAI_API_KEY=sk-...
python -c "import praisonai_bio"
python examples/big/04_glycolysis_demo.py
```

Uses toolset `sysbio-core`. Simulation preview needs BASICO (`[simulation]` extra).

---

## Sample output

```
The Teusink Yeast Glycolysis Model investigates glycolytic oscillations in
Saccharomyces cerevisiae.

Model Overview
- Title: Wolf2000 Glycolytic Oscillations
- Purpose: oscillatory dynamics of ATP and NADH; synchronization via acetaldehyde

Simulation Outcomes (100 time units)
- ATP: fluctuates ~1.6 to 3.0 (periodic oscillations)
- NAD: oscillatory behaviour from ~0.6
- Acetaldehyde: minor fluctuations as signaling metabolite
```

With `[simulation]` installed, the agent can call `preview_outcomes` or `simulate_model` and report time-course values.

??? "Full captured output"
    [`output.txt`](04-glycolysis-demo/output.txt)

---

## Related workflow

Same demo as YAML (3 agent steps):

```bash
praisonai workflow run workflows/cookbooks/glycolysis_demo.yaml
```

---

[← All examples](../index.md)
