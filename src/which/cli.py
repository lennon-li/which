from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

from .core import spec_from_mapping
from .delegation import route_delegation
from .engines import jev_openrouter, laya_http


def _load(path: str):
    with Path(path).open(encoding="utf-8") as handle:
        if path.endswith((".yaml", ".yml")):
            return yaml.safe_load(handle)
        return json.load(handle)


def main() -> None:
    parser = argparse.ArgumentParser(prog="which")
    parser.add_argument("--engine", choices=["jev", "laya"], required=True)
    parser.add_argument("--state", required=True, help="JSON state file")
    parser.add_argument("--spec", required=True, help="YAML/JSON decision spec")
    parser.add_argument("--policy", help="YAML/JSON delegation policy")
    parser.add_argument("--laya-endpoint")
    parser.add_argument("--model")
    args = parser.parse_args()

    state = _load(args.state)
    spec_mapping = _load(args.spec)
    spec = spec_from_mapping(spec_mapping)

    if args.engine == "jev":
        engine = jev_openrouter(model=args.model or "typesafe/jev-1.13-20260917")
    else:
        if not args.laya_endpoint:
            parser.error("--laya-endpoint is required for the laya engine")
        engine = laya_http(args.laya_endpoint, model=args.model)

    result = engine.decide(state, spec)
    payload = {
        "engine": result.engine,
        "model": result.model,
        "spec_version": result.spec_version,
        "answers": {
            name: {
                "value": answer.value,
                "confidence": answer.confidence,
                "probabilities": dict(answer.probabilities),
            }
            for name, answer in result.answers.items()
        },
    }

    if args.policy:
        policy = _load(args.policy)
        advice = route_delegation(
            result, state, policy, confidence_floor=spec.confidence_floor
        )
        payload["delegation"] = {
            "status": advice.status,
            "reason": advice.reason,
            "profile": advice.profile,
            "classification": advice.classification,
            "uncertain_axes": list(advice.uncertain_axes),
        }

    print(json.dumps(payload, indent=2, sort_keys=True))
