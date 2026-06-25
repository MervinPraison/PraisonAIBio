# MCP servers

Expose PraisonAIBio tools to Cursor, Claude Desktop, and other MCP clients.

---

## Servers

| Server | Path | Scope |
|--------|------|-------|
| **sysbio** | `mcp/sysbio-server/server.py` | 11 T2B simulation tools |
| **biomodels** | `mcp/biomodels-server/server.py` | Read-only search and metadata |
| **Package** | `praisonai-bio-mcp` | Same as sysbio (console entry point) |
| **ClawBio bridge** | `mcp/clawbio-bridge/bridge.py` | v2 — connect genomics context to pathway tools |

!!! note "Discovery tools"
    MCP servers expose the **11 Talk2BioModels tools**. The extra 10 discovery tools (`rank_models`, `sbml_validate`, `repro_export`, etc.) are available via Python toolsets and YAML workflows, not MCP yet.

---

## Run locally

```bash
pip install -e "src/praisonai-bio[simulation]"
python -c "import praisonai_bio"
python mcp/sysbio-server/server.py
```

Read-only (no BASICO):

```bash
python mcp/biomodels-server/server.py
```

Health check:

```bash
praisonai-bio doctor mcp
```

---

## PraisonAI integration

```bash
praisonai mcp add   # register server in config
praisonai serve mcp
```

Workflow stub: `workflows/platform/mcp_sysbio_server.yaml`

---

## Resources and prompts

| File | Purpose |
|------|---------|
| `mcp/sysbio-server/resources.md` | `biomodel://{id}`, `demo://glycolysis` URIs |
| `mcp/sysbio-server/prompts.md` | Pre-built MCP prompts |

---

## Cursor config example

```json
{
  "mcpServers": {
    "praisonai-sysbio": {
      "command": "python",
      "args": ["/path/to/PraisonAIBio/mcp/sysbio-server/server.py"]
    }
  }
}
```

Run from repo root after `pip install -e "src/praisonai-bio[simulation]"`.

See [Tools reference](../tools-reference.md) for all 21 Python tools.
