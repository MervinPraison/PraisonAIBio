"""Launch PraisonAIBio tools as an MCP server."""

from __future__ import annotations


def launch_sysbio_mcp(transport: str = "stdio", toolset: str = "sysbio-full") -> None:
    import praisonai_bio  # noqa: F401
    from praisonaiagents.mcp import launch_tools_mcp_server
    from praisonaiagents.toolsets import resolve_toolset

    tools = resolve_toolset(toolset)
    launch_tools_mcp_server(tools=tools, name="praisonai-bio-sysbio", transport=transport)


if __name__ == "__main__":
    launch_sysbio_mcp()
