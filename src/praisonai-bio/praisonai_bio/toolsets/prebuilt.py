"""Prebuilt toolsets for PraisonAIBio."""

from __future__ import annotations

from praisonaiagents.toolsets import register_toolset

# Read-only BioModels discovery
register_toolset(
    "biomodels-readonly",
    [
        "search_models",
        "get_modelinfo",
        "get_annotation",
        "query_article",
        "rank_models",
        "trust_scorecard",
        "compare_models",
        "sbml_summarise",
    ],
    description="Read-only BioModels.org discovery and metadata tools",
)

register_toolset(
    "sbml_analysis",
    [
        "load_biomodel",
        "sbml_summarise",
        "sbml_validate",
        "sbml_to_graph",
        "list_model_files",
        "download_model_file",
        "get_annotation",
        "ask_question",
        "sedml_parse",
        "advanced_search",
    ],
    description="SBML loading and structural analysis",
)

register_toolset(
    "sysbio-core",
    [
        "search_models",
        "get_modelinfo",
        "load_biomodel",
        "simulate_model",
        "ask_question",
        "rank_models",
        "preview_outcomes",
    ],
    description="Core systems biology workflow (Phase 0 demo)",
)

register_toolset(
    "simulation",
    [
        "load_biomodel",
        "simulate_model",
        "simulate_perturbation",
        "steady_state",
        "parameter_scan",
        "preview_outcomes",
        "custom_plotter",
        "sedml_parse",
    ],
    description="SBML simulation and plotting via BASICO",
)

register_toolset(
    "reporting",
    [
        "compare_models",
        "compare_simulations",
        "trust_scorecard",
        "query_article",
        "get_annotation",
        "custom_plotter",
        "preview_outcomes",
    ],
    description="Comparison, trust scoring, and reporting",
)

register_toolset(
    "sysbio-full",
    [
        "search_models",
        "get_modelinfo",
        "load_biomodel",
        "simulate_model",
        "ask_question",
        "steady_state",
        "parameter_scan",
        "custom_plotter",
        "get_annotation",
        "query_article",
        "save_model",
        "rank_models",
        "trust_scorecard",
        "compare_models",
        "preview_outcomes",
        "sbml_summarise",
        "sbml_validate",
        "sedml_parse",
        "simulate_perturbation",
        "compare_simulations",
        "repro_export",
        "sbml_to_graph",
        "list_model_files",
        "download_model_file",
        "advanced_search",
        "sedml_simulate",
        "search_parameters",
        "get_reaction_graph",
    ],
    description="Full T2B parity plus discovery tools",
)

register_toolset(
    "sysbio-orchestrator",
    [
        "search_models",
        "rank_models",
        "trust_scorecard",
        "get_modelinfo",
        "sbml_summarise",
        "ask_question",
        "simulate_model",
        "preview_outcomes",
        "compare_models",
        "advanced_search",
        "list_model_files",
    ],
    description="Multi-agent discovery pipeline orchestrator tools",
)

try:
    from praisonaiagents.tools import register_tool as _register_tool
    from praisonaiagents.tools.schedule_tools import schedule_add, schedule_list, schedule_remove

    for _sched in (schedule_add, schedule_list, schedule_remove):
        _register_tool(_sched)
    register_toolset(
        "sysbio-orchestrator-scheduled",
        [
            "search_models",
            "rank_models",
            "simulate_model",
            "schedule_add",
            "schedule_list",
            "schedule_remove",
        ],
        description="Orchestrator with PraisonAI scheduler tools",
    )
except ImportError:
    pass

register_toolset(
    "repro",
    ["repro_export", "save_model", "load_biomodel", "get_modelinfo", "query_article"],
    description="Reproducibility bundle helpers",
)

register_toolset(
    "sysbio-safe",
    [
        "search_models",
        "get_modelinfo",
        "get_annotation",
        "query_article",
        "rank_models",
        "trust_scorecard",
        "compare_models",
        "sbml_summarise",
        "ask_question",
    ],
    description="Safe read-only toolset (no simulation or file writes)",
)

register_toolset(
    "genomics-bridge",
    [],
    description="v2: ClawBio genomics bridge (stub — register external tools at runtime)",
)
