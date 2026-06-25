# Example — Search BioModels

**Category:** Small (no AI) · **Script:** [`examples/small/01_search.py`](https://github.com/MervinPraison/PraisonAIBio/blob/main/examples/small/01_search.py)

Search curated glycolysis models on BioModels.org.

---

## How to run

```bash
pip install -e "src/praisonai-bio"
python -c "import praisonai_bio"
python examples/small/01_search.py
```

No API key required. Needs network access to [BioModels.org](https://www.biomodels.org).

---

## Sample output

Returns JSON with a curated search query and matching models:

```json
{
  "query": "glycolysis AND curationstatus:\"Manually curated\"",
  "count": 10,
  "models": [
    {
      "id": "BIOMD0000000471",
      "name": "Smallbone2013 - Yeast metabolic model with linlog rate law",
      "url": "https://www.biomodels.org/BIOMD0000000471"
    },
    {
      "id": "BIOMD0000000472",
      "name": "Smallbone2013 - Yeast metabolic model with modular rate law",
      "url": "https://www.biomodels.org/BIOMD0000000472"
    }
  ]
}
```

??? "Full captured output"
    Full JSON is saved in the repo: [`output.txt`](01-search/output.txt)

    ```bash
    cat docs/examples/small/01-search/output.txt
    ```

---

[← All examples](../index.md)
