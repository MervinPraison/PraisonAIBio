"""MCP client example — connect Agent to praisonai-bio-mcp stdio server.

Run the server in another terminal:
  praisonai-bio-mcp

Then (with OPENAI_API_KEY):
  python examples/mcp/sysbio_client.py
"""

from __future__ import annotations

import os
import shutil
import sys


def main() -> int:
    if not os.environ.get("OPENAI_API_KEY"):
        print("Set OPENAI_API_KEY to run the agentic MCP demo.", file=sys.stderr)
        return 1
    if not shutil.which("praisonai-bio-mcp"):
        print("Install package first: pip install -e src/praisonai-bio", file=sys.stderr)
        return 1

    import praisonai_bio  # noqa: F401
    from praisonaiagents import Agent
    from praisonaiagents.mcp import MCP

    mcp = MCP("praisonai-bio-mcp")
    agent = Agent(
        name="mcp-scout",
        instructions="Use search_models to find one curated glycolysis model. Reply with one model ID.",
        model="gpt-4o-mini",
        tools=[mcp],
    )
    result = agent.start("Find a curated yeast glycolysis model")
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
