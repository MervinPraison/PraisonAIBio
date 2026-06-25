# Ground truth

Populate reference trajectories here for simulation accuracy benchmarks.

Run `scripts/download_demo_sbml.py` then generate COPASI/BASICO reference with:

```bash
pip install "praisonai-bio[simulation]"
python -c "import praisonai_bio; ..."
```

Expected file: `BIOMD0000000206_trajectory.csv` (coordinate with BioModels/T2B benchmark sets).
