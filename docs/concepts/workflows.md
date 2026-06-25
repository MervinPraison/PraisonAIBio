# Workflows

| Workflow | Pattern | Path |
|----------|---------|------|
| Discovery pipeline | Parallel | `workflows/discovery/biomodels_discovery_pipeline.yaml` |
| Full research (7 phases) | Route, Parallel, Loop, Repeat | `workflows/discovery/biomodels_full_research_workflow.yaml` |
| Assumption review | Approval HITL | `workflows/discovery/biomodels_assumption_review.yaml` |
| Route by input | Route | `workflows/orchestration/sysbio_route_by_input.yaml` |
| Glycolysis demo | Cookbook | `workflows/cookbooks/glycolysis_demo.yaml` |

```bash
praisonai workflow run workflows/discovery/biomodels_discovery_pipeline.yaml
```

Requires `import praisonai_bio` before running toolset-based workflows.
