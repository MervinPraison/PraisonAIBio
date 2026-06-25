# Plan validation report

Automated audit of PraisonAIBio against the gap-closure plan (Phase 0–1).

Run checks:

```bash
bash scripts/check_no_submission.sh
python scripts/validate_repo.py
python -m pytest tests/unit -q
python benchmarks/t2b_parity/eval_suite_runner.py
```

## Summary

| Area | Status | Notes |
|------|--------|-------|
| Package + tools | **PASS** | 28 tools, 10 toolsets, entry points OK |
| MCP | **PASS** | `sysbio-full` exposes all 28 tools |
| Workflows | **PASS** | Discovery, lifecycle, platform, cookbooks, eight-pillar pipeline |
| Skills | **PARTIAL** | 16 skills in catalog; not all 28 tools covered |
| Docs + examples | **PASS** | MkDocs, captured outputs, interactive guide |
| Hooks + policy | **PASS** | `wire_bio_hooks()`, SDK policy packs, policy gate |
| Benchmarks | **PASS** | 10-case T2B parity via prompt router (no self-score cheat) |
| Session / repro | **PASS** | `repro_export` writes manifests under run dir |
| Knowledge / RAG | **PARTIAL** | Bridge code; full RAG when optional deps installed |
| Phase 2 backlog | **DEFERRED** | OLS adapter, MCP Docker, 312-Q suite, PyPI publish |

## Benchmark integrity

T2B parity cases are scored with `infer_tool_from_prompt()` — **not** by echoing `expected_tool`. CI runs `eval_suite_runner.py` (mean score must be ≥ 0.9).

```bash
python benchmarks/t2b_parity/eval_suite_runner.py
python benchmarks/run_all.py
```

## Phase 2 (intentionally deferred)

- `ols_adapter.py` (stub)
- `mcp/sysbio-server/Dockerfile`
- Full ClawBio bridge
- 312-question T2B benchmark import
- PyPI publish (release workflow ready; needs tag)

## Last validated

Re-run `python scripts/validate_repo.py` after any structural change.
