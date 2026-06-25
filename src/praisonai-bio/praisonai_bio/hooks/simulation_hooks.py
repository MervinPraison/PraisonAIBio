"""Simulation lifecycle hooks."""

from __future__ import annotations

import logging

logger = logging.getLogger("praisonai_bio.hooks.simulation")


def before_simulation(event: dict) -> None:
    logger.info("Starting simulation: model=%s", event.get("model_id"))


def after_simulation(event: dict) -> None:
    logger.info("Simulation finished: model=%s", event.get("model_id"))


def approval_gate(event: dict) -> bool:
    return bool(event.get("approved", False))
