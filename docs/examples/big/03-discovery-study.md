# Example — Discovery study (MAPK)

**Category:** Big (AI agent) · **Script:** [`examples/big/03_discovery_study.py`](https://github.com/MervinPraison/PraisonAIBio/blob/main/examples/big/03_discovery_study.py)

Search, rank, and recommend the best curated model for a research question.

---

## How to run

```bash
pip install -e "src/praisonai-bio"
export OPENAI_API_KEY=sk-...
python -c "import praisonai_bio"
python examples/big/03_discovery_study.py
```

Uses toolset `sysbio-orchestrator` (`search_models`, `rank_models`, `trust_scorecard`, …).

---

## Sample output

```
The best curated MAPK model for cell signaling studies is:

### Sarma2012 - Oscillations in MAPK cascade (S2), inclusion of external signaling module
- ID: BIOMD0000000442
- Submitter: Uddipan Sarma
- Submission Date: 2011-12-19
- Relevance Score: 3

This model provides a comprehensive framework for studying MAPK behavior
in a signaling context.
```

??? "Full captured output"
    [`output.txt`](03-discovery-study/output.txt)

---

[← All examples](../index.md)
