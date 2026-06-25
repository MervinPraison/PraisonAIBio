"""Comprehensive PraisonAIBio plan compliance validator."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# --- Plan: repository structure (Phase 0 + Phase 1 scaffold) ---

PLAN_PATHS: dict[str, list[str]] = {
    "root": ["README.md", "AGENTS.md", "llms.txt", "LICENSE", "pyproject.toml", "pytest.ini"],
    "package": [
        "src/praisonai-bio/pyproject.toml",
        "src/praisonai-bio/praisonai_bio/__init__.py",
        "src/praisonai-bio/praisonai_bio/cli/main.py",
        "src/praisonai-bio/praisonai_bio/mcp/server.py",
    ],
    "adapters": [
        "src/praisonai-bio/praisonai_bio/adapters/biomodels_api.py",
        "src/praisonai-bio/praisonai_bio/adapters/basico_adapter.py",
    ],
    "protocols": [
        "src/praisonai-bio/praisonai_bio/protocols/biomodels.py",
        "src/praisonai-bio/praisonai_bio/protocols/simulation.py",
        "src/praisonai-bio/praisonai_bio/protocols/repro_bundle.py",
    ],
    "orchestrator": [
        "src/praisonai-bio/praisonai_bio/orchestrator/routing_table.py",
        "src/praisonai-bio/praisonai_bio/orchestrator/file_detection.py",
        "src/praisonai-bio/praisonai_bio/orchestrator/chain_planner.py",
        "src/praisonai-bio/praisonai_bio/orchestrator/discovery.py",
        "src/praisonai-bio/praisonai_bio/orchestrator/comparison.py",
    ],
    "hooks_policy_guardrails": [
        "src/praisonai-bio/praisonai_bio/hooks/biomodels_hooks.py",
        "src/praisonai-bio/praisonai_bio/hooks/simulation_hooks.py",
        "src/praisonai-bio/praisonai_bio/policy/export_policy.py",
        "src/praisonai-bio/praisonai_bio/policy/sbml_policy.py",
        "src/praisonai-bio/praisonai_bio/guardrails/simulation_output.py",
    ],
    "state_knowledge_eval_trace": [
        "src/praisonai-bio/praisonai_bio/state/session.py",
        "src/praisonai-bio/praisonai_bio/state/model_state.py",
        "src/praisonai-bio/praisonai_bio/knowledge/article_index.py",
        "src/praisonai-bio/praisonai_bio/eval/t2b_scorer.py",
        "src/praisonai-bio/praisonai_bio/eval/simulation_accuracy.py",
        "src/praisonai-bio/praisonai_bio/trace/bio_spans.py",
    ],
    "t2b_tools_11": [
        "src/praisonai-bio/praisonai_bio/tools/search_models.py",
        "src/praisonai-bio/praisonai_bio/tools/get_modelinfo.py",
        "src/praisonai-bio/praisonai_bio/tools/load_biomodel.py",
        "src/praisonai-bio/praisonai_bio/tools/simulate_model.py",
        "src/praisonai-bio/praisonai_bio/tools/ask_question.py",
        "src/praisonai-bio/praisonai_bio/tools/steady_state.py",
        "src/praisonai-bio/praisonai_bio/tools/parameter_scan.py",
        "src/praisonai-bio/praisonai_bio/tools/custom_plotter.py",
        "src/praisonai-bio/praisonai_bio/tools/get_annotation.py",
        "src/praisonai-bio/praisonai_bio/tools/query_article.py",
        "src/praisonai-bio/praisonai_bio/tools/save_model.py",
    ],
    "discovery_tools": [
        "src/praisonai-bio/praisonai_bio/tools/rank_models.py",
        "src/praisonai-bio/praisonai_bio/tools/trust_scorecard.py",
        "src/praisonai-bio/praisonai_bio/tools/compare_models.py",
        "src/praisonai-bio/praisonai_bio/tools/preview_outcomes.py",
        "src/praisonai-bio/praisonai_bio/tools/sbml_summarise.py",
        "src/praisonai-bio/praisonai_bio/tools/sbml_validate.py",
        "src/praisonai-bio/praisonai_bio/tools/sedml_parse.py",
        "src/praisonai-bio/praisonai_bio/tools/simulate_perturbation.py",
        "src/praisonai-bio/praisonai_bio/tools/compare_simulations.py",
        "src/praisonai-bio/praisonai_bio/tools/repro_export.py",
    ],
    "discovery_workflows": [
        "workflows/discovery/biomodels_full_research_workflow.yaml",
        "workflows/discovery/biomodels_discovery_pipeline.yaml",
        "workflows/discovery/biomodels_assumption_review.yaml",
        "workflows/discovery/biomodels_baseline_simulation.yaml",
        "workflows/discovery/biomodels_perturbation_study.yaml",
        "workflows/discovery/biomodels_comparison_report.yaml",
    ],
    "orchestration_workflows": [
        "workflows/orchestration/sysbio_route_by_input.yaml",
        "workflows/orchestration/parallel_sensitivity_scan.yaml",
        "workflows/orchestration/precision_medicine_loop.yaml",
        "workflows/orchestration/team_model_review.yaml",
        "workflows/orchestration/full_platform_showcase.yaml",
    ],
    "platform_workflows": [
        "workflows/platform/approval_assumption_gate.yaml",
        "workflows/platform/approval_parameter_scan.yaml",
        "workflows/platform/policy_guarded_simulation.yaml",
        "workflows/platform/mcp_sysbio_server.yaml",
        "workflows/platform/eval_regression_gate.yaml",
        "workflows/platform/botos_sysbio_telegram.yaml",
    ],
    "cookbooks": [
        "workflows/cookbooks/glycolysis_demo.yaml",
        "workflows/cookbooks/mapk_p53_discovery.yaml",
    ],
    "recipes_all_5": [
        "recipes/bio/biomodels-discovery/recipe.yaml",
        "recipes/bio/biomodels-research/recipe.yaml",
        "recipes/bio/biomodels-simulate/recipe.yaml",
        "recipes/bio/biomodels-perturb/recipe.yaml",
        "recipes/bio/biomodels-report/recipe.yaml",
    ],
    "skills": [
        "skills/catalog.json",
        "skills/search-models/SKILL.md",
        "skills/simulate-model/SKILL.md",
        "skills/load-biomodel/SKILL.md",
        "skills/sysbio-orchestrator/SKILL.md",
        "skills/repro-enforcer/SKILL.md",
    ],
    "mcp": [
        "mcp/sysbio-server/server.py",
        "mcp/biomodels-server/server.py",
        "mcp/clawbio-bridge/bridge.py",
    ],
    "benchmarks": [
        "benchmarks/t2b_parity/scorer.py",
        "benchmarks/t2b_parity/runner.py",
        "benchmarks/t2b_parity/manifest.json",
        "benchmarks/t2b_parity/ground_truth/README.md",
        "benchmarks/orchestrator_routing/manifest.json",
        "benchmarks/simulation_accuracy/manifest.json",
        "benchmarks/repro_bundle/manifest.json",
    ],
    "demo_data": [
        "demo_data/README.md",
        "demo_data/bundled_slices/search_glycolysis.json",
        "demo_data/bundles/glycolysis_demo/commands.sh",
        "demo_data/bundles/glycolysis_demo/checksums.sha256",
        "demo_data/sbml/README.md",
    ],
    "praisonai_template": [
        ".praisonai/config.yaml",
        ".praisonai/agents/biomodels-scout.md",
        ".praisonai/agents/sysbio-orchestrator.md",
    ],
    "scripts": [
        "scripts/generate_catalog.py",
        "scripts/download_demo_sbml.py",
        "scripts/validate_repo.py",
    ],
    "tests": [
        "tests/unit/test_biomodels_adapter.py",
        "tests/unit/test_gaps.py",
        "tests/integration/test_biomodels_live.py",
        "tests/agentic/test_discovery_agent.py",
    ],
    "docs": [
        "docs/README.md",
        "docs/get-started.md",
        "docs/quick-tasks.md",
        "docs/for-researchers.md",
        "docs/tools-at-a-glance.md",
        "docs/concepts/vs-clawbio.md",
        "docs/concepts/vs-t2b.md",
        "docs/concepts/workflows.md",
        "docs/concepts/mcp.md",
    ],
    "examples": [
        "examples/README.md",
        "examples/small/01_search.py",
        "examples/big/04_glycolysis_demo.py",
    ],
    "docs_hub": [
        "docs/index.md",
        "docs/get-started.md",
        "docs/install.md",
        "docs/quick-tasks.md",
        "docs/for-researchers.md",
        "docs/tools-at-a-glance.md",
        "docs/examples.md",
        "docs/toolsets.md",
        "docs/recipes.md",
        "docs/cli.md",
        "docs/faq.md",
        "docs/development.md",
    ],
    "mkdocs": ["mkdocs.yml", "docs/requirements.txt"],
}

T2B_TOOLS = [
    "search_models", "get_modelinfo", "load_biomodel", "simulate_model", "ask_question",
    "steady_state", "parameter_scan", "custom_plotter", "get_annotation", "query_article", "save_model",
]

DISCOVERY_TOOL_NAMES = [
    "rank_models", "trust_scorecard", "compare_models", "preview_outcomes", "sbml_summarise",
    "sbml_validate", "sedml_parse", "simulate_perturbation", "compare_simulations", "repro_export",
]

REQUIRED_TOOLSETS = [
    "biomodels-readonly", "sbml_analysis", "sysbio-core", "simulation",
    "reporting", "sysbio-full", "sysbio-orchestrator", "repro", "sysbio-safe", "genomics-bridge",
]

PHASE2_DEFERRED = [
    "src/praisonai-bio/praisonai_bio/adapters/ols_adapter.py",
    "mcp/sysbio-server/Dockerfile",
]


@dataclass
class Result:
    ok: bool
    missing: list[str]
    sections: dict[str, tuple[int, int]]


def check_paths() -> Result:
    missing: list[str] = []
    sections: dict[str, tuple[int, int]] = {}
    for section, paths in PLAN_PATHS.items():
        found = sum(1 for p in paths if (ROOT / p).exists())
        sections[section] = (found, len(paths))
        for p in paths:
            if not (ROOT / p).exists():
                missing.append(p)
    return Result(ok=not missing, missing=missing, sections=sections)


def check_tools_and_toolsets() -> tuple[list[str], list[str]]:
    sys.path.insert(0, str(ROOT / "src" / "praisonai-bio"))
    import praisonai_bio  # noqa: F401
    from praisonaiagents.toolsets import list_toolsets, resolve_toolset

    issues: list[str] = []
    registered = set(list_toolsets())
    for ts in REQUIRED_TOOLSETS:
        if ts not in registered:
            issues.append(f"toolset missing: {ts}")
    full = resolve_toolset("sysbio-full")
    for t in T2B_TOOLS + DISCOVERY_TOOL_NAMES:
        if t not in full:
            issues.append(f"tool not in sysbio-full: {t}")
    cases = len(list((ROOT / "benchmarks/t2b_parity/cases").glob("[0-9]*.json")))
    if cases < 10:
        issues.append(f"benchmark cases: {cases}/10")
    return issues, list(registered)


def main() -> int:
    path_result = check_paths()
    tool_issues, toolsets = check_tools_and_toolsets()

    print("=" * 60)
    print("PraisonAIBio Plan Compliance Report")
    print("=" * 60)
    for section, (found, total) in sorted(path_result.sections.items()):
        status = "OK" if found == total else f"PARTIAL {found}/{total}"
        print(f"  [{status:12}] {section}")
    print("-" * 60)
    if path_result.missing:
        print(f"MISSING ({len(path_result.missing)} files):")
        for p in path_result.missing:
            print(f"  - {p}")
    if tool_issues:
        print(f"TOOL/TOOLSET ISSUES ({len(tool_issues)}):")
        for i in tool_issues:
            print(f"  - {i}")
    print("-" * 60)
    print(f"Phase 2 deferred (not required now): {len(PHASE2_DEFERRED)} items")
    for p in PHASE2_DEFERRED:
        print(f"  ~ {p}")
    print("-" * 60)
    if path_result.ok and not tool_issues:
        print("RESULT: PASS — all planned Phase 0/1 scaffold items present")
        return 0
    print("RESULT: FAIL — gaps remain (see above)")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
