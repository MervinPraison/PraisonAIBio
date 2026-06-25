"""
PraisonAIBio — AI agents for systems biology via BioModels.org.

Import this package before using YAML/CLI toolsets:
    import praisonai_bio
"""

from praisonaiagents.tools import register_tool
from praisonaiagents.tools.retry import RetryPolicy

_DEFAULT_RETRY = RetryPolicy()

# Import tools so entry points resolve; register for in-process use
from praisonai_bio.tools.search_models import search_models
from praisonai_bio.tools.get_modelinfo import get_modelinfo
from praisonai_bio.tools.load_biomodel import load_biomodel
from praisonai_bio.tools.simulate_model import simulate_model
from praisonai_bio.tools.ask_question import ask_question
from praisonai_bio.tools.steady_state import steady_state
from praisonai_bio.tools.parameter_scan import parameter_scan
from praisonai_bio.tools.custom_plotter import custom_plotter
from praisonai_bio.tools.get_annotation import get_annotation
from praisonai_bio.tools.query_article import query_article
from praisonai_bio.tools.save_model import save_model
from praisonai_bio.tools.rank_models import rank_models
from praisonai_bio.tools.trust_scorecard import trust_scorecard
from praisonai_bio.tools.compare_models import compare_models
from praisonai_bio.tools.preview_outcomes import preview_outcomes
from praisonai_bio.tools.sbml_summarise import sbml_summarise
from praisonai_bio.tools.sbml_validate import sbml_validate
from praisonai_bio.tools.sedml_parse import sedml_parse
from praisonai_bio.tools.simulate_perturbation import simulate_perturbation
from praisonai_bio.tools.compare_simulations import compare_simulations
from praisonai_bio.tools.repro_export import repro_export

_ALL_TOOLS = [
    search_models,
    get_modelinfo,
    load_biomodel,
    simulate_model,
    ask_question,
    steady_state,
    parameter_scan,
    custom_plotter,
    get_annotation,
    query_article,
    save_model,
    rank_models,
    trust_scorecard,
    compare_models,
    preview_outcomes,
    sbml_summarise,
    sbml_validate,
    sedml_parse,
    simulate_perturbation,
    compare_simulations,
    repro_export,
]

for _tool in _ALL_TOOLS:
    if getattr(_tool, "retry_policy", None) is None:
        _tool.retry_policy = _DEFAULT_RETRY
    register_tool(_tool)

# Toolsets (import-time registration)
from praisonai_bio.toolsets import prebuilt  # noqa: F401, E402

__all__ = [
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
]

__version__ = "0.1.0"
