import json, praisonai_bio
b = json.dumps({"result_preview": {"ATP": [1.0, 0.9, 0.8]}})
v = json.dumps({"result_preview": {"ATP": [1.0, 0.85, 0.75]}})
print(praisonai_bio.compare_simulations.run(baseline_json=b, perturbation_json=v))
