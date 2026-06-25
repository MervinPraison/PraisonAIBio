# Recipes

Packaged workflows under `recipes/bio/` — same automation as YAML workflows, with metadata for discovery.

| Recipe | Folder | Workflow |
|--------|--------|----------|
| `biomodels-discovery` | `recipes/bio/biomodels-discovery/` | Discovery pipeline → shortlist |
| `biomodels-research` | `recipes/bio/biomodels-research/` | Full research workflow |
| `biomodels-simulate` | `recipes/bio/biomodels-simulate/` | Baseline simulation |
| `biomodels-perturb` | `recipes/bio/biomodels-perturb/` | Perturbation study |
| `biomodels-report` | `recipes/bio/biomodels-report/` | Comparison report |

Each folder contains `recipe.yaml` pointing at a workflow under `workflows/discovery/`.

---

## Run (recommended)

Recipes wrap existing workflows — run the workflow directly:

```bash
cd PraisonAIBio
python -c "import praisonai_bio"

# Discovery shortlist
praisonai workflow run workflows/discovery/biomodels_discovery_pipeline.yaml

# Full research (7 phases)
praisonai workflow run workflows/discovery/biomodels_full_research_workflow.yaml

# Baseline simulation
praisonai workflow run workflows/discovery/biomodels_baseline_simulation.yaml

# Perturbation study
praisonai workflow run workflows/discovery/biomodels_perturbation_study.yaml

# Comparison report
praisonai workflow run workflows/discovery/biomodels_comparison_report.yaml
```

---

## Recipe path (optional)

Point PraisonAI at the recipe catalog:

```bash
export PRAISONAI_RECIPE_PATH="$(pwd)/recipes/bio"
```

Then use PraisonAI recipe commands if your wrapper version supports them; otherwise use the workflow paths above.

---

## Cookbooks

Ready-made demos in `workflows/cookbooks/`:

```bash
praisonai workflow run workflows/cookbooks/glycolysis_demo.yaml
praisonai workflow run workflows/cookbooks/mapk_p53_discovery.yaml
```

Demo model: **BIOMD0000000206** (yeast glycolysis).

See [Workflows](concepts/workflows.md) and [For researchers](for-researchers.md).
