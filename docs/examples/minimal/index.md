# Minimal examples (2 lines)

Same tools as [small examples](../small/01-search.md) — fewer lines.

```bash
pip install -e "src/praisonai-bio"
python examples/minimal/search.py
```

| Script | Tested output |
|--------|---------------|
| [search.py](https://github.com/MervinPraison/PraisonAIBio/blob/main/examples/minimal/search.py) | [output.txt](minimal/search/output.txt) |
| [info.py](https://github.com/MervinPraison/PraisonAIBio/blob/main/examples/minimal/info.py) | same as [02-model-info](../small/02-model-info.md) |
| [trust.py](https://github.com/MervinPraison/PraisonAIBio/blob/main/examples/minimal/trust.py) | same as [03-trust-score](../small/03-trust-score.md) |
| [validate.py](https://github.com/MervinPraison/PraisonAIBio/blob/main/examples/minimal/validate.py) | same as [04-validate-sbml](../small/04-validate-sbml.md) |
| [graph.py](https://github.com/MervinPraison/PraisonAIBio/blob/main/examples/minimal/graph.py) | same as [10-sbml-graph](../small/10-sbml-graph.md) |
| [compare_runs.py](https://github.com/MervinPraison/PraisonAIBio/blob/main/examples/minimal/compare_runs.py) | below |

## Tested output — compare_runs (offline)

??? "Click to expand"
    ```text
    --8<-- "docs/examples/minimal/compare-runs/output.txt"
    ```

## Tested output — search

??? "Click to expand"
    ```text
    --8<-- "docs/examples/minimal/search/output.txt"
    ```

Regenerate all captures: `./scripts/capture_example_outputs.sh`

[← All examples](../index.md)
