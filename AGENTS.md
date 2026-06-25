# PraisonAIBio — Agent Guide

Extension package for PraisonAI systems biology workflows.

## PraisonAI backbone (do not reimplement)

PraisonAI (`praisonaiagents` + `praisonai` wrapper) is the **execution backbone**; PraisonAIBio is the **domain plugin**.

| PraisonAI owns | PraisonAIBio owns |
|----------------|-------------------|
| Agent, AgentTeam, Task, handoffs, workflows (route/parallel/loop/approve) | BioModels REST adapter, BASICO simulation |
| Hooks, EventBus, trace, PolicyEngine, GuardrailConfig, ApprovalConfig | 26 `@tool` functions + entry points |
| MemoryConfig, Session, KnowledgeConfig, RAG | Repro bundles, ground-truth CSVs |
| EvalSuite, MCP launcher, recipes, scheduler, BotOS | Tool implementations, biomodels-runs artefacts |

**Integration (three paths, one backbone):**

```bash
import praisonai_bio
praisonai workflow run workflows/discovery/biomodels_discovery_pipeline.yaml
export PRAISONAI_RECIPE_PATH=recipes/bio && praisonai recipe run biomodels-discovery
```

```python
from praisonaiagents import Agent
from praisonai_bio.config.presets import DISCOVERY_AGENT
import praisonai_bio  # noqa: F401 — registers tools + wire_bio_hooks()

agent = Agent(name="scout", **DISCOVERY_AGENT)
```

**Do not build:** `praisonai-bio workflow run` or `praisonai-bio recipe run`. Bio CLI stays: `init`, `validate`, `tools validate`, `doctor`, `bench`.

Agent presets live in `praisonai_bio/config/presets.py`. Hooks register via `wire_bio_hooks()` on import.

## Layout

- `src/praisonai-bio/praisonai_bio/` — pip package (tools, adapters, toolsets)
- `workflows/` — YAML multi-agent workflows
- `skills/` — SKILL.md + catalog.json (ClawBio-style)
- `recipes/bio/` — PraisonAI wrapper recipes
- `benchmarks/` — T2B parity and orchestrator benchmarks
- `examples/` — small (tools only) and big (agents)
- `docs/` — researcher-friendly guides

---

## Key rules (PraisonAI — general)

Adapted from the main PraisonAI `AGENTS.md`. Apply these when changing this repo.

### Philosophy

- **Agent-centric** — agents, workflows, sessions, tools, and memory come first
- **Minimal API** — few parameters, sensible defaults, explicit overrides only when needed
- **Three-way parity** — every feature should work via **Python**, **YAML**, and **CLI** where applicable
- **Copy-paste examples** — shortest path that runs; include imports; realistic demo data

### Engineering

- **Protocol first, adapter second** — interfaces in `protocols/`, implementations in `adapters/`
- **Lazy optional deps** — no module-level imports of BASICO, matplotlib, etc.; import inside functions
- **DRY** — reuse PraisonAI toolsets, hooks, and adapters; do not duplicate SDK logic here
- **Backward compatible** — public tool names and entry points are stable; deprecate before removing
- **Safe defaults** — new behaviour is opt-in; read-only toolsets for discovery (`sysbio-safe`, `biomodels-readonly`)
- **Multi-agent safe** — no shared mutable global state; sessions under `~/.praisonai/biomodels-runs/`

### Code style

- Follow existing conventions in the file you edit
- Test changes (unit + integration; agentic test when touching agent flows)
- Be concise in docs — especially `docs/` for non-developers
- British English in user-facing text

### Naming

- Tools: verb phrases (`search_models`, `get_modelinfo`) — match T2B where applicable
- Protocols: suffix `Protocol` (e.g. `BioModelsAdapterProtocol`)
- Adapters: suffix or folder `adapters/` (e.g. `biomodels_api.py`)
- Config: `register_toolset`, `get_client`, entry points in `pyproject.toml`

---

## PraisonAIBio-specific rules

1. Always `import praisonai_bio` before YAML/CLI toolsets
2. BioModels base URL: `https://www.biomodels.org` (override with `BIOMODELS_BASE_URL`)
3. BASICO is optional — lazy import in `adapters/basico_adapter.py`
4. Keep public docs product-focused only (BioModels, tools, workflows — no private or funding-submission material)
5. Plugin pattern — tools via `[project.entry-points."praisonaiagents.tools"]`, not forked SDK code

---

## Tool naming

**T2B parity:** `search_models`, `get_modelinfo`, `load_biomodel`, `simulate_model`, `ask_question`, `steady_state`, `parameter_scan`, `custom_plotter`, `get_annotation`, `query_article`, `save_model`

**Discovery extras:** `rank_models`, `trust_scorecard`, `compare_models`, `preview_outcomes`, `sbml_summarise`, `sbml_validate`, `sbml_to_graph`, `sedml_parse`, `sedml_simulate`, `simulate_perturbation`, `compare_simulations`, `repro_export`, `list_model_files`, `download_model_file`, `advanced_search`

---

## Tests

```bash
pytest tests/unit -q
pytest tests/integration -q          # network
pytest tests/agentic -q              # needs OPENAI_API_KEY
./scripts/test_all.sh
python scripts/validate_repo.py
```

New tools: unit test (mocked) + agentic test when the agent path changes.

---

## Quick references

- Main SDK guide: [PraisonAI AGENTS.md](https://github.com/MervinPraison/PraisonAI/blob/main/src/praisonai-agents/AGENTS.md)
- Plugin template: [plugin_template](https://github.com/MervinPraison/PraisonAI/tree/main/examples/python/plugin_template)
- Correct CLI: `praisonai run --agent <name>` · `praisonai workflow run <file.yaml>`
