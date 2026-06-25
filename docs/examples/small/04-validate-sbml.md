# Example — Validate SBML

**Category:** Small (no AI) · **Script:** [`examples/small/04_validate_sbml.py`](https://github.com/MervinPraison/PraisonAIBio/blob/main/examples/small/04_validate_sbml.py)

Download SBML from BioModels and check structure (species, reactions, basic validity). No simulation required.

---

## How to run

```bash
pip install -e "src/praisonai-bio"
python -c "import praisonai_bio"
python examples/small/04_validate_sbml.py
```

---

## Sample output

```json
{
  "valid": true,
  "species_count": 9,
  "reaction_count": 11,
  "issues": []
}
```

If validation fails, `valid` is `false` and `issues` lists problems found.

??? "Full captured output"
    [`output.txt`](04-validate-sbml/output.txt)

---

[← All examples](../index.md)
