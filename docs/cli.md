# CLI

## praisonai-bio

```bash
pip install -e "src/praisonai-bio"
praisonai-bio init              # scaffold .praisonai
praisonai-bio validate check    # package + toolsets OK
praisonai-bio tools validate    # 21 entry points
praisonai-bio doctor mcp        # MCP + BASICO check
```

---

## PraisonAI wrapper

Correct patterns (not `praisonai agent run`):

```bash
praisonai run --agent biomodels-scout "Find glycolysis models"
praisonai workflow run workflows/cookbooks/glycolysis_demo.yaml
praisonai workflow run workflows/discovery/biomodels_discovery_pipeline.yaml
```

---

## MCP servers

```bash
python mcp/sysbio-server/server.py       # 11 T2B tools
python mcp/biomodels-server/server.py    # read-only BioModels
praisonai-bio-mcp                        # console entry (if installed)
```

See [MCP](concepts/mcp.md).
