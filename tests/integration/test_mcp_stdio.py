"""MCP server exposes full sysbio toolset."""

from __future__ import annotations


def test_sysbio_full_tool_count():
    import praisonai_bio  # noqa: F401
    from praisonaiagents.toolsets import resolve_toolset

    tools = resolve_toolset("sysbio-full")
    assert len(tools) >= 28


def test_mcp_launcher_import():
    from praisonai_bio.mcp.server import launch_sysbio_mcp

    assert callable(launch_sysbio_mcp)
