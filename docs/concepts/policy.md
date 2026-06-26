# Policy

Simulation and export tools respect **SDK PolicyEngine** packs in `policy/packs/`.

## Packs

| Pack | Use case |
|------|----------|
| `bio-public` | Read-only discovery, no save/simulation writes |
| `bio-lab` | Simulation, perturbation, export allowed |

## Enable a pack

```bash
export PRAISONAI_POLICY_PACK=bio-lab
python examples/small/09_repro_export.py
```

Or in workflows:

```yaml
env:
  PRAISONAI_POLICY_PACK: bio-lab
```

## How enforcement works

1. `import praisonai_bio` calls `wire_bio_hooks()`
2. `bio_policy_gate` runs on `before_tool` via `policy/loader.py`
3. Export paths checked with `policy/export_policy.py`

## Recipes

```bash
export PRAISONAI_RECIPE_PATH="/path/to/PraisonAIBio/recipes/bio"
praisonai recipe run biomodels-simulate --policy bio-lab
```

See [Recipes](../recipes.md) and [CLI](../cli.md).
