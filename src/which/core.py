from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Protocol


class WhichError(RuntimeError):
    pass


class EngineUnavailable(WhichError):
    pass


@dataclass(frozen=True)
class QuestionSpec:
    type: str
    instructions: str
    criteria: Any


@dataclass(frozen=True)
class DecisionSpec:
    questions: Mapping[str, QuestionSpec]
    confidence_floor: float = 0.75
    version: str = "unversioned"


@dataclass(frozen=True)
class AxisDecision:
    value: Any
    confidence: float | None
    probabilities: Mapping[str, float] = field(default_factory=dict)
    raw: Mapping[str, Any] = field(default_factory=dict)

    @property
    def uncertain(self) -> bool:
        return self.confidence is None


@dataclass(frozen=True)
class DecisionResult:
    engine: str
    model: str | None
    spec_version: str
    answers: Mapping[str, AxisDecision]
    raw: Mapping[str, Any] = field(default_factory=dict)

    def uncertain_axes(self, floor: float) -> tuple[str, ...]:
        return tuple(
            name
            for name, answer in self.answers.items()
            if answer.confidence is None or answer.confidence < floor
        )


class DecisionEngine(Protocol):
    name: str

    def decide(self, state: Mapping[str, Any], spec: DecisionSpec) -> DecisionResult:
        ...


def _clean_probabilities(value: Any) -> dict[str, float]:
    if value is None:
        return {}
    if not isinstance(value, Mapping):
        raise WhichError("probabilities must be a mapping")
    out = {str(key): float(prob) for key, prob in value.items()}
    if any(prob < 0.0 or prob > 1.0 for prob in out.values()):
        raise WhichError("probabilities must be between 0 and 1")
    if out and abs(sum(out.values()) - 1.0) > 0.02:
        raise WhichError("probabilities must sum to approximately 1")
    return out


def _criterion_label(text: str) -> str:
    return text.split(":", 1)[0].strip().lower().replace(" ", "_")


def _confidence(answer: Mapping[str, Any], probabilities: Mapping[str, float]) -> float | None:
    raw = answer.get("confidence")
    if raw is not None:
        value = float(raw)
        if not 0 <= value <= 1:
            raise WhichError("confidence must be between 0 and 1")
        return value
    if probabilities:
        return max(probabilities.values())
    return None


def normalize_system_one_response(
    response: Mapping[str, Any],
    spec: DecisionSpec,
    *,
    engine: str,
    model: str | None = None,
) -> DecisionResult:
    """Normalize Jev/Laya-style typed answers into an engine-neutral contract."""

    raw_answers = response.get("answers")
    if not isinstance(raw_answers, Mapping):
        raise WhichError("engine response must contain an 'answers' mapping")

    normalized: dict[str, AxisDecision] = {}
    for name, question in spec.questions.items():
        answer = raw_answers.get(name)
        if not isinstance(answer, Mapping):
            raise WhichError(f"missing answer for {name!r}")

        probabilities = _clean_probabilities(answer.get("probabilities"))
        qtype = question.type.lower()

        if qtype == "choice":
            value = answer.get("choice")
            if value is None and probabilities:
                value = max(probabilities, key=probabilities.get)
            if value is None:
                raise WhichError(f"choice answer {name!r} has no value")
            value = str(value).lower()

        elif qtype == "score":
            if not isinstance(question.criteria, list) or not question.criteria:
                raise WhichError(f"score question {name!r} needs ordered criteria")
            if probabilities:
                index = int(max(probabilities, key=probabilities.get))
            elif answer.get("score") is not None:
                index = int(round(float(answer["score"])))
            else:
                raise WhichError(f"score answer {name!r} has no distribution or score")
            if index < 0 or index >= len(question.criteria):
                raise WhichError(f"score answer {name!r} is outside its rubric")
            value = _criterion_label(str(question.criteria[index]))

        elif qtype == "noul":
            # Different System-One implementations expose this primitive slightly
            # differently. Preserve the raw value and only claim confidence when
            # the engine supplies a distribution or confidence explicitly.
            if "noul" in answer:
                value = answer["noul"]
            elif "value" in answer:
                value = answer["value"]
            else:
                raise WhichError(f"noul answer {name!r} has no value")

        else:
            raise WhichError(f"unsupported question type: {question.type!r}")

        normalized[name] = AxisDecision(
            value=value,
            confidence=_confidence(answer, probabilities),
            probabilities=probabilities,
            raw=dict(answer),
        )

    return DecisionResult(
        engine=engine,
        model=model,
        spec_version=spec.version,
        answers=normalized,
        raw=dict(response),
    )


def spec_from_mapping(value: Mapping[str, Any]) -> DecisionSpec:
    questions = value.get("questions")
    if not isinstance(questions, Mapping) or not questions:
        raise WhichError("decision spec requires questions")
    parsed = {
        name: QuestionSpec(
            type=str(question["type"]),
            instructions=str(question.get("instructions", "")),
            criteria=question.get("criteria"),
        )
        for name, question in questions.items()
    }
    floor = float(value.get("confidence_floor", 0.75))
    if not 0 <= floor <= 1:
        raise WhichError("confidence_floor must be between 0 and 1")
    return DecisionSpec(
        questions=parsed,
        confidence_floor=floor,
        version=str(value.get("schema_version", value.get("version", "unversioned"))),
    )
