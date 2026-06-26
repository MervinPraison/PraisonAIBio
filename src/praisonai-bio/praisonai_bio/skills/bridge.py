"""Discover bio skill directories for SDK SkillsConfig."""

from __future__ import annotations

from pathlib import Path


def bio_skills_paths() -> list[str]:
    """Return repo skill folders for PraisonAI SkillsConfig."""
    repo = Path(__file__).resolve().parents[4]
    skills = repo / "skills"
    return [str(skills)] if skills.is_dir() else []


def skills_config_kwargs() -> dict:
    """Optional kwargs for Agent(skills=...) when SDK SkillsConfig is available."""
    paths = bio_skills_paths()
    if not paths:
        return {}
    try:
        from praisonaiagents import SkillsConfig

        return {"skills": SkillsConfig(paths=paths)}
    except ImportError:
        return {"skills": paths}
