# Examples

Runnable scripts with **recorded sample output** (captured from live runs against BioModels.org).

---

## Before you run

```bash
cd PraisonAIBio
pip install -e "src/praisonai-bio"
python -c "import praisonai_bio"
```

Agent examples (`big/`) also need:

```bash
export OPENAI_API_KEY=sk-...
pip install -e "src/praisonai-bio[simulation]"   # optional — for simulation in glycolysis demo
```

Regenerate all saved outputs:

```bash
./scripts/capture_example_outputs.sh
python scripts/generate_example_docs.py
```

**Shortest scripts:** [minimal/](minimal/index.md) (2 lines each).

**Not sure which to run?** → [Interactive guide](../interactive-guide.md)

---

## Small — direct tools (no AI)

No API key. One BioModels call per script. Each doc page has **Tested output** (expand accordion).

| Example | Script | Docs |
|---------|--------|------|
| Search models | `examples/small/01_search.py` | [01 — Search](small/01-search.md) |
| Model metadata | `examples/small/02_model_info.py` | [02 — Model info](small/02-model-info.md) |
| Trust score | `examples/small/03_trust_score.py` | [03 — Trust score](small/03-trust-score.md) |
| Validate SBML | `examples/small/04_validate_sbml.py` | [04 — Validate SBML](small/04-validate-sbml.md) |
| Simulate | `examples/small/05_simulate.py` | [05 — Simulate](small/05-simulate.md) *(BASICO)* |
| Perturb | `examples/small/06_perturb.py` | [06 — Perturb](small/06-perturb.md) *(BASICO)* |
| Compare models | `examples/small/07_compare_models.py` | [07 — Compare models](small/07-compare-models.md) |
| Compare sims | `examples/small/08_compare_sims.py` | [08 — Compare sims](small/08-compare-sims.md) *(offline)* |
| Repro export | `examples/small/09_repro_export.py` | [09 — Repro export](small/09-repro-export.md) |
| SBML graph | `examples/small/10_sbml_graph.py` | [10 — SBML graph](small/10-sbml-graph.md) |

---

## Notebooks

Five Jupyter notebooks — [overview](notebooks/index.md)

---

## Big — AI agent

Uses `gpt-4o-mini` and PraisonAI toolsets. Each doc includes **Tested output**.

| Example | Script | Docs |
|---------|--------|------|
| Find models | `examples/big/01_find_models.py` | [01 — Find models](big/01-find-models.md) |
| Summarise model | `examples/big/02_summarise_model.py` | [02 — Summarise](big/02-summarise-model.md) |
| Discovery study | `examples/big/03_discovery_study.py` | [03 — Discovery](big/03-discovery-study.md) |
| Glycolysis demo | `examples/big/04_glycolysis_demo.py` | [04 — Glycolysis](big/04-glycolysis-demo.md) |

!!! note "Agent output varies"
    LLM replies differ slightly each run. Saved `output.txt` files show a real capture; your text may differ but structure should match.

---

## YAML workflows

```bash
praisonai workflow run workflows/cookbooks/glycolysis_demo.yaml
```

See [Workflows](../concepts/workflows.md).
