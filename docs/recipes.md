# Recipes

Packaged workflows under `recipes/bio/` — same automation via PraisonAI recipe commands.

| Recipe | Workflow |
|--------|----------|
| `biomodels-discovery` | Discovery pipeline → shortlist |
| `biomodels-research` | Full research workflow |
| `biomodels-simulate` | Baseline simulation |
| `biomodels-perturb` | Perturbation study |
| `biomodels-report` | Comparison report |

---

## Run

```bash
praisonai workflow run workflows/discovery/biomodels_discovery_pipeline.yaml
```

Or point PraisonAI at the recipe folder:

```bash
export PRAISONAI_RECIPE_PATH=recipes/bio
```

Recipe files live in each subfolder as `recipe.yaml`.

---

## Cookbooks

Ready-made demos in `workflows/cookbooks/`:

```bash
praisonai workflow run workflows/cookbooks/glycolysis_demo.yaml
praisonai workflow run workflows/cookbooks/mapk_p53_discovery.yaml
```
