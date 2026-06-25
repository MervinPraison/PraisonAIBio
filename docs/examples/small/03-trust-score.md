# Example — Trust scorecard

**Category:** Small (no AI) · **Script:** [`examples/small/03_trust_score.py`](https://github.com/MervinPraison/PraisonAIBio/blob/main/examples/small/03_trust_score.py)

Score how trustworthy a BioModels entry is (curation, publication, metadata completeness).

---

## How to run

```bash
pip install -e "src/praisonai-bio"
python -c "import praisonai_bio"
python examples/small/03_trust_score.py
```

Uses model **BIOMD0000000206**.

---

## Sample output

```json
{
  "model_id": "BIOMD0000000206",
  "score": 85,
  "grade": "high",
  "reasons": [
    "Manually curated on BioModels.org",
    "Linked publication metadata present",
    "MIRIAM annotations available"
  ],
  "curation_status": "Manually curated"
}
```

Exact score fields depend on live BioModels metadata.

??? "Full captured output"
    [`output.txt`](03-trust-score/output.txt)

---

[← All examples](../index.md)
