# CLI

## praisonai-bio

```bash
pip install -e "src/praisonai-bio"
praisonai-bio init              # scaffold .praisonai/config.yaml + agents
praisonai-bio validate check    # package + toolsets OK
praisonai-bio validate repo     # full plan compliance (scripts/validate_repo.py)
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
praisonai workflow run workflows/platform/policy_guarded_simulation.yaml
```

Requires `pip install praisonai` and `python -c "import praisonai_bio"`.

---

## MCP servers

```bash
python mcp/sysbio-server/server.py       # 11 T2B tools
python mcp/biomodels-server/server.py    # read-only BioModels
praisonai-bio-mcp                        # console entry (if installed)
```

See [MCP](concepts/mcp.md).

---

## Docs site

```bash
pip install -r docs/requirements.txt
mkdocs serve    # http://127.0.0.1:8000
mkdocs build    # output in site/
```

Live site: [https://bio.praison.ai](https://bio.praison.ai)
