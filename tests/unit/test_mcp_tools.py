"""MCP server exposes sysbio-full toolset."""

from __future__ import annotations


def test_mcp_resolves_full_toolset():
    import praisonai_bio  # noqa: F401
    from praisonaiagents.toolsets import resolve_toolset

    tools = resolve_toolset("sysbio-full")
    assert len(tools) >= 28
    if isinstance(tools[0], str):
        names = set(tools)
    else:
        names = {getattr(t, "name", getattr(t, "__name__", str(t))) for t in tools}
    assert "sbml_to_graph" in names
    assert "sedml_simulate" in names
