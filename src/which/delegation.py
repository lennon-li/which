from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from .core import DecisionResult, WhichError


@dataclass(frozen=True)
class DelegationAdvice:
    status: str
    reason: str | None
    profile: Mapping[str, Any] | None
    classification: Mapping[str, Any]
    uncertain_axes: tuple[str, ...] = ()


def consequence(state: Mapping[str, Any]) -> str:
    """Keep factual risk inputs deterministic rather than asking a classifier."""
    sensitive = bool(state.get("touches_sensitive_data", False))
    released = bool(state.get("is_released", False))
    reaches_main = bool(state.get("reaches_main_or_deploy", False))
    if sensitive or (released and reaches_main):
        return "high"
    if released or reaches_main:
        return "medium"
    return "low"


def _value(result: DecisionResult, key: str) -> str:
    try:
        return str(result.answers[key].value).lower()
    except KeyError as exc:
        raise WhichError(f"delegation result is missing {key!r}") from exc


def route_delegation(
    result: DecisionResult,
    state: Mapping[str, Any],
    policy: Mapping[str, Any],
    *,
    confidence_floor: float,
) -> DelegationAdvice:
    """Turn engine-neutral classification into deterministic delegation advice."""

    uncertain = result.uncertain_axes(confidence_floor)
    classification = {name: answer.value for name, answer in result.answers.items()}
    if uncertain:
        return DelegationAdvice(
            "abstain", "low_confidence", None, classification, uncertain
        )

    if not bool(state.get("parent_understands_task", True)):
        return DelegationAdvice(
            "abstain", "finish_line_unclear", None, classification
        )

    complexity = _value(result, "complexity")
    shape = _value(result, "task_shape")
    intensity = _value(result, "implementation_intensity")

    if complexity == "frontier":
        return DelegationAdvice("abstain", "frontier_complexity", None, classification)

    if (
        shape == "orchestration_decision"
        and intensity == "low"
        and consequence(state) != "high"
    ):
        return DelegationAdvice(
            "self_execute",
            "bounded_orchestration_decision",
            None,
            classification,
        )

    profiles = policy.get("profiles", {})
    if not isinstance(profiles, Mapping):
        raise WhichError("delegation policy requires profiles")

    large_context_shapes = set(
        policy.get("large_context_shapes", ["audit", "read_only_survey"])
    )
    breadth = int(state.get("material_breadth", 0) or 0)
    threshold = int(policy.get("large_context_threshold", 15))

    profile_name: str
    if shape in large_context_shapes and breadth >= threshold:
        profile_name = str(policy.get("large_context_profile", "large_context"))
    else:
        shape_profiles = policy.get("shape_profiles", {})
        complexity_profiles = policy.get("complexity_profiles", {})
        if shape in shape_profiles:
            profile_name = str(shape_profiles[shape])
        elif complexity in complexity_profiles:
            profile_name = str(complexity_profiles[complexity])
        else:
            profile_name = str(policy.get("default_profile", "economy"))

    profile = profiles.get(profile_name)
    if not isinstance(profile, Mapping):
        raise WhichError(f"unknown delegation profile {profile_name!r}")

    previous_provider = str(state.get("previous_provider", "")).lower().strip()
    target_provider = str(profile.get("provider", "")).lower().strip()
    if (
        shape in {"independent_review", "audit"}
        and previous_provider
        and target_provider
        and previous_provider == target_provider
    ):
        return DelegationAdvice(
            "abstain", "review_provider_not_independent", None, classification
        )

    return DelegationAdvice(
        "advise",
        None,
        {"name": profile_name, **dict(profile)},
        classification,
    )
