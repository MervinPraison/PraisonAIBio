# MCP servers

Expose PraisonAIBio tools to Cursor, Claude Desktop, and other MCP clients.

---

## Servers

| Server | Path | Scope |
|--------|------|-------|
| **sysbio** | `mcp/sysbio-server/server.py` | All 11 T2B tools |
| **biomodels** | `mcp/biomodels-server/server.py` | Read-only search/metadata |
| **Package** | `praisonai-bio-mcp` | Same as sysbio (entry point) |

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

---

## PraisonAI integration

```bash
praisonai mcp add   # register server in config
praisonai serve mcp
```

Workflow stub: `workflows/platform/mcp_sysbio_server.yaml`

---

## Resources (scaffold)

- `biomodel://{id}` — BioModels model
- `demo://glycolysis` — BIOMD0000000206 bundle

See `mcp/sysbio-server/resources.md` in the repo.
