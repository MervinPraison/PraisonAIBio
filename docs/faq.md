# FAQ

## Do I need to code?

No for **small examples** and **YAML workflows**. Agent examples need an API key but not writing code.

---

## What is BIOMD0000000206?

The demo model — Teusink yeast glycolysis. Used in cookbooks and docs.

---

## Why `import praisonai_bio`?

Toolsets register at import time. YAML/CLI will not find `sysbio-full` without it.

---

## Simulation fails / BASICO missing

```bash
pip install "praisonai-bio[simulation]"
```

Discovery and search work without BASICO.

---

## BioModels vs EBI URLs?

PraisonAIBio uses **https://www.biomodels.org** by default. Override with `BIOMODELS_BASE_URL`.

---

## How is this different from Talk2BioModels?

T2B focuses on simulation after you pick a model. PraisonAIBio adds **discovery, ranking, workflows, and multi-agent orchestration**.

[Compare →](concepts/vs-t2b.md)

---

## How is this different from ClawBio?

ClawBio is genomics skills. PraisonAIBio is **BioModels / SBML simulation**.

[Compare →](concepts/vs-clawbio.md)
