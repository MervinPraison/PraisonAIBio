# Session and persistence

PraisonAIBio uses a **dual persistence** model aligned with the PraisonAI backbone.

## SDK session (conversation / workflow memory)

```yaml
workflow:
  memory:
    backend: file
    session_id: "biomodels-{{ run_id }}"
```

Python agents:

```python
from praisonaiagents import Agent, MemoryConfig
import praisonai_bio

agent = Agent(
    name="scout",
    toolsets=["biomodels-readonly"],
    memory=MemoryConfig(auto_save="biomodels-discovery"),
)
```

## Bio artefacts (files)

`repro_export` writes manifests and bundles under:

`~/.praisonai/biomodels-runs/{run_id}/`

Set a run id:

```bash
export BIOMODELS_RUN_ID=my-study-001
```

## Trace JSONL

When `BIOMODELS_RUN_ID` is set, hooks write structured events via `trace/jsonl_sink.py`.

See [Workflows](workflows.md) and presets in `praisonai_bio/config/presets.py`.
