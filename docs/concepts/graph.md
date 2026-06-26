# Model graph

Turn SBML into a **reaction graph** for assumption review and reporting.

## Tool

```python
import praisonai_bio
print(praisonai_bio.sbml_to_graph.run(model_id="BIOMD0000000206"))
```

CLI via agent toolset `sbml_analysis` or `sysbio-full`.

## Graph JSON shape

```json
{
  "model_id": "BIOMD0000000206",
  "nodes": [{"id": "s1", "type": "species"}],
  "edges": [{"source": "s1", "target": "v1", "role": "reactant"}],
  "counts": {"species": 15, "reactions": 10}
}
```

## Example

```bash
python examples/small/10_sbml_graph.py
```

Docs: [10 — SBML graph](../examples/small/10-sbml-graph.md)

Used in `workflows/cookbooks/full_platform_pipeline.yaml` (Graph pillar).
