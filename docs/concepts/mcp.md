# MCP Servers

| Server | Path | Scope |
|--------|------|-------|
| sysbio-server | `mcp/sysbio-server/server.py` | All 11 T2B tools |
| biomodels-server | `mcp/biomodels-server/server.py` | Read-only BioModels |
| Package MCP | `praisonai_bio.mcp.server` | `praisonai-bio-mcp` CLI |

```bash
python mcp/sysbio-server/server.py
python mcp/biomodels-server/server.py
```

Resources (Phase 1): `biomodel://{id}`, `demo://glycolysis`

Prompts: `sysbio_analyse_model`, `sysbio_precision_medicine` (Phase 2)
