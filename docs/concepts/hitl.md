# Human-in-the-loop (HITL)

PraisonAIBio uses the **PraisonAI backbone** for approvals — not a custom gate.

## YAML workflows

```yaml
- name: assumption_hitl
  approve:
    description: Approve SBML assumptions before simulation
    risk_level: medium
    auto_approve: false
```

Examples:

- `workflows/cookbooks/full_platform_pipeline.yaml`
- `workflows/platform/approval_assumption_gate.yaml`
- `workflows/discovery/biomodels_assumption_review.yaml`

## When to use HITL

| Step | Risk | Gate |
|------|------|------|
| Assumption review | Medium | Before simulation |
| Parameter scan | Medium | Before execution |
| Export to lab paths | High | Under `bio-lab` policy |

Run platform gates manually when inline `approve` is unavailable:

```bash
praisonai workflow run workflows/platform/approval_assumption_gate.yaml
```

See [Workflows](workflows.md) and [Policy](policy.md).
