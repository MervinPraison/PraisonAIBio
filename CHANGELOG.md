# Changelog

## 0.2.0 — 2026-06-25

### Added
- SBML adapter, `sbml_to_graph`, and BioModels API extensions (`list_model_files`, `download_model_file`, `advanced_search`, `sedml_simulate`)
- Agent presets (`config/presets.py`), `wire_bio_hooks()`, policy pack loader, JSONL trace sink
- Five Jupyter notebooks, examples 05–10, Gadkar lifecycle workflows, T2B cookbooks
- 11 additional skills (16 total in catalog), MCP `sysbio-full` toolset (26 tools)
- CI workflow, benchmark `run_all.py`, EvalSuite deterministic runner
- Release workflow for TestPyPI/PyPI

### Changed
- Policy packs migrated to PraisonAI `PolicyEngine` YAML format
- `query_article` uses local publication index
- Glycolysis demo runs simulation via `SIMULATION_AGENT` preset

## 0.1.0

Initial release — 21 tools, 10 toolsets, discovery workflows, T2B parity scaffold.
