import hashlib
import io
import json
import zipfile
from pathlib import Path

from praisonaiagents import tool

from praisonai_bio.tools._helpers import as_json, get_client, normalise_model_id
from praisonai_bio.state.session import run_dir, save_json


def _write_optional_files(client, model_id: str, out: Path, written: list[str]) -> None:
    """Download SED-ML, COMBINE archive, and curation artefacts when available."""
    try:
        combine = client.download_combine_archive(model_id)
        combine_path = out / f"{model_id}_combine.zip"
        combine_path.write_bytes(combine)
        written.append(combine_path.name)
        with zipfile.ZipFile(io.BytesIO(combine)) as zf:
            manifest = {"archive_files": zf.namelist()}
            (out / "combine_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
            written.append("combine_manifest.json")
    except Exception:
        pass

    try:
        files = client.list_files(model_id)
        candidates = files if isinstance(files, list) else files.get("files", [])
        for item in candidates:
            name = item.get("filename") or item.get("name") or ""
            lower = name.lower()
            if lower.endswith(".sedml") or lower.endswith(".sedml.xml"):
                content = client.download_file(model_id, name)
                dest = out / Path(name).name
                dest.write_bytes(content)
                written.append(dest.name)
            if "curation" in lower or lower.endswith(".png") or lower.endswith(".svg"):
                content = client.download_file(model_id, name)
                dest = out / Path(name).name
                dest.write_bytes(content)
                written.append(dest.name)
    except Exception:
        pass


@tool
def repro_export(model_id: str, output_dir: str, run_id: str | None = None) -> str:
    """Export a reproducibility bundle (SBML, metadata, COMBINE, SED-ML, commands, checksums)."""
    try:
        client = get_client()
        model_id = normalise_model_id(model_id)
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        written: list[str] = []
        sbml = client.download_sbml(model_id)
        sbml_path = out / "model.sbml"
        sbml_path.write_bytes(sbml)
        written.append(sbml_path.name)
        meta = client.get_model_info(model_id)
        meta_path = out / "metadata.json"
        meta_path.write_text(json.dumps(meta, indent=2, default=str), encoding="utf-8")
        written.append(meta_path.name)
        _write_optional_files(client, model_id, out, written)
        commands = out / "commands.sh"
        commands.write_text(
            f"#!/usr/bin/env bash\n# Repro bundle for {model_id}\n"
            f"python -c \"import praisonai_bio; from praisonai_bio.tools.sedml_simulate import sedml_simulate; "
            f"print(sedml_simulate.run(model_id='{model_id}'))\"\n",
            encoding="utf-8",
        )
        written.append(commands.name)
        checksums = []
        for p in sorted(out.iterdir()):
            if p.is_file() and p.name != "checksums.sha256":
                digest = hashlib.sha256(p.read_bytes()).hexdigest()
                checksums.append(f"{digest}  {p.name}")
        (out / "checksums.sha256").write_text("\n".join(checksums) + "\n", encoding="utf-8")
        written.append("checksums.sha256")
        readme = out / "README.md"
        readme.write_text(
            f"# Reproducibility bundle\n\nModel: `{model_id}`\nRun: `{run_id or 'manual'}`\n",
            encoding="utf-8",
        )
        written.append(readme.name)
        result = {"model_id": model_id, "bundle_dir": str(out.resolve()), "files": sorted(set(written))}
        if run_id:
            save_json(run_id, "repro_manifest.json", result)
            result["session_dir"] = str(run_dir(run_id))
        return as_json(result)
    except Exception as exc:
        return as_json({"error": str(exc)})
