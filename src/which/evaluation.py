from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping

from .core import DecisionEngine, DecisionSpec


@dataclass(frozen=True)
class QuestionMetrics:
    question: str
    n: int
    accuracy: float
    handled: float
    accepted_accuracy: float | None
    brier: float | None


def load_jsonl(path: str | Path) -> list[dict[str, Any]]:
    """Load the same simple id/state/labels shape used by jevcal."""
    rows = []
    with Path(path).open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def _brier(probabilities: Mapping[str, float], gold: Any) -> float | None:
    if not probabilities:
        return None
    gold_key = str(gold).lower()
    return sum(
        (prob - (1.0 if key.lower() == gold_key else 0.0)) ** 2
        for key, prob in probabilities.items()
    )


def evaluate(
    engine: DecisionEngine,
    spec: DecisionSpec,
    cases: Iterable[Mapping[str, Any]],
    *,
    threshold: float | None = None,
) -> list[QuestionMetrics]:
    """Evaluate one engine against gold labels without changing the gold standard."""

    threshold = spec.confidence_floor if threshold is None else threshold
    stats = {
        name: {"n": 0, "correct": 0, "handled": 0, "accepted_correct": 0, "brier": []}
        for name in spec.questions
    }

    for row in cases:
        labels = row.get("labels", {})
        result = engine.decide(row["state"], spec)
        for name, gold in labels.items():
            if name not in result.answers:
                continue
            answer = result.answers[name]
            bucket = stats[name]
            bucket["n"] += 1
            correct = str(answer.value).lower() == str(gold).lower()
            bucket["correct"] += int(correct)
            if answer.confidence is not None and answer.confidence >= threshold:
                bucket["handled"] += 1
                bucket["accepted_correct"] += int(correct)
            score = _brier(answer.probabilities, gold)
            if score is not None:
                bucket["brier"].append(score)

    out = []
    for name, bucket in stats.items():
        n = bucket["n"]
        handled = bucket["handled"]
        out.append(
            QuestionMetrics(
                question=name,
                n=n,
                accuracy=(bucket["correct"] / n) if n else 0.0,
                handled=(handled / n) if n else 0.0,
                accepted_accuracy=(
                    bucket["accepted_correct"] / handled if handled else None
                ),
                brier=(
                    sum(bucket["brier"]) / len(bucket["brier"])
                    if bucket["brier"]
                    else None
                ),
            )
        )
    return out
