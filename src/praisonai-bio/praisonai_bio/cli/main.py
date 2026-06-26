"""PraisonAIBio CLI (Phase 0 + validation)."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[4]


def cmd_init() -> int:
    root = _repo_root()
    praisonai_dir = root / ".praisonai"
    praisonai_dir.mkdir(exist_ok=True)
    agents_dir = praisonai_dir / "agents"
    agents_dir.mkdir(exist_ok=True)
    for name in ("biomodels-scout.md", "sysbio-orchestrator.md"):
        src = root / ".praisonai" / "agents" / name
        if src.exists():
            shutil.copy2(src, agents_dir / name)
    config = praisonai_dir / "config.yaml"
    if not config.exists():
        config.write_text(
            "llm: gpt-4o-mini\ntoolsets:\n  - sysbio-core\n"
            "biomodels:\n  base_url: https://www.biomodels.org\n  curated_only: true\n",
            encoding="utf-8",
        )
    print(f"Initialised {praisonai_dir}")
    print("Next: pip install -e 'src/praisonai-bio[simulation]' && python -c \"import praisonai_bio\"")
    return 0


def cmd_validate_check() -> int:
    try:
        import praisonai_bio  # noqa: F401
        from praisonaiagents.toolsets import list_toolsets, resolve_toolset

        names = sorted(t for t in list_toolsets() if "sysbio" in t or "biomodels" in t or t == "repro")
        full = resolve_toolset("sysbio-full")
        print(f"OK — praisonai_bio {praisonai_bio.__version__}")
        print(f"Toolsets: {names}")
        print(f"sysbio-full tools: {len(full)}")
        return 0
    except Exception as exc:
        print(f"FAIL — {exc}", file=sys.stderr)
        return 1


def cmd_tools_validate() -> int:
    import praisonai_bio  # noqa: F401
    from importlib.metadata import entry_points

    eps = entry_points(group="praisonaiagents.tools")
    bio_tools = [e.name for e in eps if e.module.startswith("praisonai_bio")]
    print(f"Entry points: {len(bio_tools)} — {', '.join(sorted(bio_tools))}")
    return 0 if len(bio_tools) >= 16 else 1


def cmd_doctor_mcp() -> int:
    from praisonai_bio.adapters.basico_adapter import check_basico_available
    from praisonaiagents.toolsets import resolve_toolset

    ok, msg = check_basico_available()
    print(f"BASICO: {'OK' if ok else 'MISSING — ' + msg}")
    full = resolve_toolset("sysbio-full")
    print(f"MCP sysbio-full: {len(full)} tools via praisonai-bio-mcp")
    return 0


def cmd_bench_run() -> int:
    root = _repo_root()
    import subprocess

    return subprocess.call([sys.executable, str(root / "benchmarks/run_all.py")])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="praisonai-bio", description="PraisonAIBio utilities")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("init", help="Scaffold .praisonai bio template")
    validate = sub.add_parser("validate", help="Validate installation")
    validate.add_argument("target", nargs="?", default="check", choices=["check", "repo"])
    tools = sub.add_parser("tools", help="Tool utilities")
    tools_sub = tools.add_subparsers(dest="tools_cmd")
    tools_sub.add_parser("validate", help="Verify pip entry points")
    doctor = sub.add_parser("doctor", help="Health checks")
    doctor.add_argument("target", nargs="?", default="mcp", choices=["mcp"])
    bench = sub.add_parser("bench", help="Run deterministic benchmarks")
    bench_sub = bench.add_subparsers(dest="bench_cmd")
    bench_sub.add_parser("run", help="Run benchmarks/run_all.py")

    args = parser.parse_args(argv)
    if args.command == "init":
        return cmd_init()
    if args.command == "validate" and args.target == "check":
        return cmd_validate_check()
    if args.command == "validate" and args.target == "repo":
        root = _repo_root()
        import subprocess
        return subprocess.call([sys.executable, str(root / "scripts" / "validate_repo.py")])
    if args.command == "tools" and args.tools_cmd == "validate":
        return cmd_tools_validate()
    if args.command == "doctor":
        return cmd_doctor_mcp()
    if args.command == "bench" and args.bench_cmd == "run":
        return cmd_bench_run()
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
