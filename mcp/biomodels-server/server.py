#!/usr/bin/env python3
"""Run read-only BioModels MCP server (no BASICO)."""

import praisonai_bio  # noqa: F401
from praisonaiagents.mcp import launch_tools_mcp_server

from praisonai_bio.tools.search_models import search_models
from praisonai_bio.tools.get_modelinfo import get_modelinfo
from praisonai_bio.tools.get_annotation import get_annotation
from praisonai_bio.tools.query_article import query_article
from praisonai_bio.tools.rank_models import rank_models
from praisonai_bio.tools.trust_scorecard import trust_scorecard
from praisonai_bio.tools.sbml_summarise import sbml_summarise

if __name__ == "__main__":
    launch_tools_mcp_server(
        tools=[search_models, get_modelinfo, get_annotation, query_article, rank_models, trust_scorecard, sbml_summarise],
        name="praisonai-bio-biomodels",
    )
