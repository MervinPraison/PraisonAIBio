# Agent examples

:material-robot: **AI agent** · Uses `gpt-4o-mini` · Needs `OPENAI_API_KEY`

PraisonAI agents call BioModels tools on your behalf.

---

## Setup

```bash
pip install -e "src/praisonai-bio"
export OPENAI_API_KEY=sk-...
```

---

## Examples

| # | What it does | Docs |
|---|--------------|------|
| 01 | Find glycolysis models | [01 — Find models](01-find-models.md) |
| 02 | Summarise one model | [02 — Summarise](02-summarise-model.md) |
| 03 | Mini discovery study | [03 — Discovery](03-discovery-study.md) |
| 04 | Glycolysis walkthrough | [04 — Glycolysis](04-glycolysis-demo.md) |
| 05 | Perturb + compare | [05 — Perturb compare](05-perturb-compare.md) |
| 06 | Full repro export | [06 — Full repro](06-full-repro-study.md) |
| 07 | Presets + skills | [07 — Agent configs](07-agent-with-configs.md) |

!!! note "Output varies"
    LLM text differs each run. Saved output on each page is a real capture.

---

[← All examples](../index.md) · [Small examples](../small/index.md)
