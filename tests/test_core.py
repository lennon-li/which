from which.core import DecisionSpec, QuestionSpec, normalize_system_one_response
from which.delegation import route_delegation


SPEC = DecisionSpec(
    version="test",
    confidence_floor=0.75,
    questions={
        "complexity": QuestionSpec(
            "score", "", ["Easy: x", "Medium: x", "Hard: x", "Frontier: x"]
        ),
        "task_shape": QuestionSpec(
            "choice", "", {"implementation": "x", "audit": "x", "orchestration_decision": "x"}
        ),
        "implementation_intensity": QuestionSpec(
            "score", "", ["Low: x", "Medium: x", "High: x"]
        ),
        "objective_verifiability": QuestionSpec(
            "score", "", ["Low: x", "Medium: x", "High: x"]
        ),
    },
)


def response(confidence=0.9):
    return {
        "answers": {
            "complexity": {
                "type": "score",
                "probabilities": {"0": 0.05, "1": 0.85, "2": 0.1, "3": 0.0},
                "confidence": confidence,
            },
            "task_shape": {
                "type": "choice",
                "choice": "implementation",
                "probabilities": {"implementation": 0.9, "audit": 0.05, "orchestration_decision": 0.05},
                "confidence": confidence,
            },
            "implementation_intensity": {
                "type": "score",
                "probabilities": {"0": 0.1, "1": 0.8, "2": 0.1},
                "confidence": confidence,
            },
            "objective_verifiability": {
                "type": "score",
                "probabilities": {"0": 0.0, "1": 0.1, "2": 0.9},
                "confidence": confidence,
            },
        }
    }


def test_system_one_normalization_is_engine_neutral():
    jev = normalize_system_one_response(response(), SPEC, engine="jev", model="x")
    laya = normalize_system_one_response(response(), SPEC, engine="laya", model="y")
    assert jev.answers["complexity"].value == "medium"
    assert jev.answers["task_shape"].value == "implementation"
    assert {
        k: v.value for k, v in jev.answers.items()
    } == {
        k: v.value for k, v in laya.answers.items()
    }


def test_low_confidence_abstains_before_policy():
    result = normalize_system_one_response(response(0.6), SPEC, engine="jev")
    advice = route_delegation(
        result,
        {},
        {"profiles": {"economy": {}}, "default_profile": "economy"},
        confidence_floor=0.75,
    )
    assert advice.status == "abstain"
    assert advice.reason == "low_confidence"


def test_policy_is_separate_from_engine():
    result = normalize_system_one_response(response(), SPEC, engine="laya")
    policy = {
        "default_profile": "economy",
        "complexity_profiles": {"medium": "economy"},
        "profiles": {"economy": {"capability": "economy"}},
    }
    advice = route_delegation(result, {}, policy, confidence_floor=0.75)
    assert advice.status == "advise"
    assert advice.profile["name"] == "economy"
