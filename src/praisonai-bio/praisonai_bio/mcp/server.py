"""Launch PraisonAIBio tools as an MCP server."""

from __future__ import annotations


def launch_sysbio_mcp(transport: str = "stdio") -> None:
    import praisonai_bio  # noqa: F401
    from praisonaiagents.mcp import launch_tools_mcp_server

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

    tools = [
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
    ]
    launch_tools_mcp_server(tools=tools, name="praisonai-bio-sysbio", transport=transport)


if __name__ == "__main__":
    launch_sysbio_mcp()
