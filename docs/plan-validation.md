# Plan validation report

Multi-agent audit of the [PraisonAIBio master plan](https://github.com/MervinPraison/PraisonAIBio) against the repository (Phase 0/1).

Run automated checks:

```bash
python scripts/validate_repo.py
./scripts/test_all.sh
```

## Summary

| Area | Status | Notes |
|------|--------|-------|
| Package + tools | **PASS** | 21 tools, 10 toolsets, entry points OK |
| Workflows (scaffold) | **PASS** | Discovery, orchestration, platform, cookbooks |
| Skills + MCP | **PASS** | 5 skills; MCP exposes 11 T2B tools |
| Docs + examples | **PASS** | MkDocs, captured outputs, skills guide |
| Session persistence | **PASS** | `repro_export` writes to `~/.praisonai/biomodels-runs/` |
| Discovery route | **PASS** | `route:` after domain classifier |
| HITL in full pipeline | **PARTIAL** | Gate via linked platform workflow (see below) |
| Handoffs | **PASS** | Agent `handoffs:` in full research workflow |
| Recipes | **PASS** | `TEMPLATE.yaml` per recipe |
| Benchmark ground truth | **PARTIAL** | Generate with `scripts/generate_ground_truth.py` |
| MCP resources/prompts | **DEFERRED** | Markdown spec only; Phase 2 server wiring |
| Knowledge/RAG | **STUB** | `article_index.py` returns `indexed: False` |
| Phase 2 items | **DEFERRED** | OLS, Docker, ClawBio bridge, PyPI |

## Critical gaps — resolution

### CONTRIBUTING + ROADMAP

Added at repo root per plan §802–805.

### Session persistence

`repro_export(model_id, output_dir, run_id=...)` saves manifest JSON under:

`~/.praisonai/biomodels-runs/{run_id}/repro_manifest.json`

### HITL between assumption review and simulation

The full 7-phase workflow references the platform gate:

```bash
# Phase 3 → HITL → Phase 4
praisonai workflow run workflows/platform/approval_assumption_gate.yaml
praisonai workflow run workflows/discovery/biomodels_full_research_workflow.yaml --var question="..."
```

The full research YAML includes an inline `approve` step where the workflow engine supports it; the platform gate remains the canonical HITL path for non-interactive CI.

### Route in discovery pipeline

`workflows/discovery/biomodels_discovery_pipeline.yaml` includes a `route:` step after domain classification (pathway / disease / drug / general).

### Handoffs

`workflows/discovery/biomodels_full_research_workflow.yaml` agents declare `handoffs:` for intake → scout → analyst → simulation chain.

### Recipes

Each recipe under `recipes/bio/*/TEMPLATE.yaml` points to the workflow file for `praisonai recipe run`:

```bash
praisonai recipe run /path/to/PraisonAIBio/recipes/bio/biomodels-discovery
```

### Ground truth trajectories

```bash
pip install "praisonai-bio[simulation]"
python scripts/generate_ground_truth.py
# writes benchmarks/t2b_parity/ground_truth/BIOMD0000000206_trajectory.csv
```

## Phase 2 (intentionally deferred)

- `ols_adapter.py`
- `mcp/sysbio-server/Dockerfile`
- Full ClawBio bridge
- BotOS production deployment
- PyPI publish

## Last validated

Re-run `python scripts/validate_repo.py` after any structural change.
