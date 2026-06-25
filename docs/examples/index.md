# Examples

Runnable scripts with **recorded sample output** (captured from live runs against BioModels.org).

<div class="grid cards" markdown="1">

-   :material-lightning-bolt:{ .lg .middle } **Minimal — 2 lines**

    ---

    Shortest possible scripts. Same tools, fewer lines.

    [:octicons-arrow-right-24: Minimal examples](minimal/index.md)

-   :material-database:{ .lg .middle } **Small — no AI**

    ---

    10 direct tool calls. No API key. Fastest learning path.

    [:octicons-arrow-right-24: Small examples](small/index.md)

-   :material-robot:{ .lg .middle } **Agent — with AI**

    ---

    PraisonAI agents using `gpt-4o-mini` and BioModels toolsets.

    [:octicons-arrow-right-24: Agent examples](big/index.md)

-   :material-notebook:{ .lg .middle } **Notebooks**

    ---

    Five Jupyter notebooks for interactive workflows.

    [:octicons-arrow-right-24: Notebooks](notebooks/index.md)

</div>

---

## Before you run

```bash
cd PraisonAIBio
pip install -e "src/praisonai-bio"
python -c "import praisonai_bio"
```

Agent examples also need:

```bash
export OPENAI_API_KEY=sk-...
pip install -e "src/praisonai-bio[simulation]"   # optional — for BASICO simulation
```

Regenerate all saved outputs:

```bash
./scripts/capture_example_outputs.sh
```

**Not sure which to run?** → [Interactive guide](../interactive-guide.md)

---

## All examples

### Small — direct tools

| Example | Script | Docs |
|---------|--------|------|
| Search models | `examples/small/01_search.py` | [01 — Search](small/01-search.md) |
| Model metadata | `examples/small/02_model_info.py` | [02 — Model info](small/02-model-info.md) |
| Trust score | `examples/small/03_trust_score.py` | [03 — Trust score](small/03-trust-score.md) |
| Validate SBML | `examples/small/04_validate_sbml.py` | [04 — Validate SBML](small/04-validate-sbml.md) |
| Simulate | `examples/small/05_simulate.py` | [05 — Simulate](small/05-simulate.md) |
| Perturb | `examples/small/06_perturb.py` | [06 — Perturb](small/06-perturb.md) |
| Compare models | `examples/small/07_compare_models.py` | [07 — Compare models](small/07-compare-models.md) |
| Compare sims | `examples/small/08_compare_sims.py` | [08 — Compare sims](small/08-compare-sims.md) |
| Repro export | `examples/small/09_repro_export.py` | [09 — Repro export](small/09-repro-export.md) |
| SBML graph | `examples/small/10_sbml_graph.py` | [10 — SBML graph](small/10-sbml-graph.md) |

### Agent — with AI

| Example | Script | Docs |
|---------|--------|------|
| Find models | `examples/big/01_find_models.py` | [01 — Find models](big/01-find-models.md) |
| Summarise model | `examples/big/02_summarise_model.py` | [02 — Summarise](big/02-summarise-model.md) |
| Discovery study | `examples/big/03_discovery_study.py` | [03 — Discovery](big/03-discovery-study.md) |
| Glycolysis demo | `examples/big/04_glycolysis_demo.py` | [04 — Glycolysis](big/04-glycolysis-demo.md) |

!!! note "Agent output varies"
    LLM replies differ slightly each run. Saved `output.txt` files show a real capture.

---

## YAML workflows

```bash
praisonai workflow run workflows/cookbooks/glycolysis_demo.yaml
```

See [Workflows](../concepts/workflows.md).
