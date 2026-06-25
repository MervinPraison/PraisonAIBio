# Example — Model metadata

**Category:** Small (no AI) · **Script:** [`examples/small/02_model_info.py`](https://github.com/MervinPraison/PraisonAIBio/blob/main/examples/small/02_model_info.py)

Fetch full metadata for demo model **BIOMD0000000206** (Teusink yeast glycolysis).

---

## How to run

```bash
pip install -e "src/praisonai-bio"
python -c "import praisonai_bio"
python examples/small/02_model_info.py
```

---

## Sample output

JSON metadata including name, submitter, publication links, and MIRIAM annotations:

```json
{
  "id": "BIOMD0000000206",
  "name": "Wolf2000_Glycolytic_Oscillations",
  "submitter": "Nicolas Le Novère",
  "description": "Model reproducing glycolytic oscillations in yeast..."
}
```

The live response includes `publication`, `authors`, `curationStatus`, and `qualifiers` arrays.

??? "Full captured output"
    [`output.txt`](02-model-info/output.txt) (~12 KB JSON)

    ```bash
    python examples/small/02_model_info.py | head -40
    ```

---

[← All examples](../index.md)
