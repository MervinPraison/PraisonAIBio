import hashlib
import json
from pathlib import Path

from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id


@tool
def repro_export(model_id: str, output_dir: str, run_id: str | None = None) -> str:
    """Export a reproducibility bundle (SBML, metadata, commands.sh, checksums)."""
    try:
        client = get_client()
        model_id = normalise_model_id(model_id)
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        sbml = client.download_sbml(model_id)
        sbml_path = out / "model.sbml"
        sbml_path.write_bytes(sbml)
        meta = client.get_model_info(model_id)
        meta_path = out / "metadata.json"
        meta_path.write_text(json.dumps(meta, indent=2, default=str), encoding="utf-8")
        commands = out / "commands.sh"
        commands.write_text(
            f"#!/usr/bin/env bash\n# Repro bundle for {model_id}\n"
            f"python -c \"import praisonai_bio; from praisonai_bio.tools.simulate_model import simulate_model; "
            f"print(simulate_model.run(model_id='{model_id}'))\"\n",
            encoding="utf-8",
        )
        checksums = []
        for p in sorted(out.iterdir()):
            if p.is_file() and p.name != "checksums.sha256":
                digest = hashlib.sha256(p.read_bytes()).hexdigest()
                checksums.append(f"{digest}  {p.name}")
        (out / "checksums.sha256").write_text("\n".join(checksums) + "\n", encoding="utf-8")
        readme = out / "README.md"
        readme.write_text(
            f"# Reproducibility bundle\n\nModel: `{model_id}`\nRun: `{run_id or 'manual'}`\n",
            encoding="utf-8",
        )
        return as_json({"model_id": model_id, "bundle_dir": str(out.resolve()), "files": [p.name for p in out.iterdir()]})
    except Exception as exc:
        return as_json({"error": str(exc)})
