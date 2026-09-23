from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any, Mapping

from .core import (
    DecisionResult,
    DecisionSpec,
    EngineUnavailable,
    WhichError,
    normalize_system_one_response,
)


@dataclass
class SystemOneHTTPEngine:
    """HTTP adapter for Jev/Laya-compatible typed-decision endpoints."""

    name: str
    endpoint: str
    model: str | None = None
    api_key_env: str | None = None
    timeout: float = 15.0
    attempts: int = 3

    def decide(self, state: Mapping[str, Any], spec: DecisionSpec) -> DecisionResult:
        questions = {
            name: {
                "type": q.type,
                "instructions": q.instructions,
                "criteria": q.criteria,
            }
            for name, q in spec.questions.items()
        }
        payload: dict[str, Any] = {"state": dict(state), "questions": questions}
        if self.model:
            payload["model"] = self.model

        headers = {"Content-Type": "application/json"}
        if self.api_key_env:
            key = os.environ.get(self.api_key_env)
            if not key:
                raise EngineUnavailable(f"missing environment variable {self.api_key_env}")
            headers["Authorization"] = f"Bearer {key}"

        request = urllib.request.Request(
            self.endpoint,
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method="POST",
        )
        retryable = {429, 500, 502, 503, 504, 520, 529}

        for attempt in range(self.attempts):
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    result = json.load(response)
                if not isinstance(result, Mapping):
                    raise WhichError("engine returned a non-object response")
                return normalize_system_one_response(
                    result, spec, engine=self.name, model=self.model
                )
            except urllib.error.HTTPError as exc:
                if exc.code not in retryable or attempt + 1 == self.attempts:
                    raise EngineUnavailable(f"{self.name} HTTP {exc.code}") from exc
            except urllib.error.URLError as exc:
                if attempt + 1 == self.attempts:
                    raise EngineUnavailable(
                        f"{self.name} network failure: {exc.reason}"
                    ) from exc
            time.sleep(0.25 * (2**attempt))

        raise AssertionError("retry loop exhausted")


def jev_openrouter(
    *,
    model: str = "typesafe/jev-1.13-20260917",
    endpoint: str = "https://openrouter.ai/api/alpha/decisions",
) -> SystemOneHTTPEngine:
    return SystemOneHTTPEngine(
        name="jev",
        endpoint=endpoint,
        model=model,
        api_key_env="OPENROUTER_API_KEY",
    )


def laya_http(
    endpoint: str,
    *,
    model: str | None = None,
    api_key_env: str | None = None,
) -> SystemOneHTTPEngine:
    """Create a Laya adapter for any Jev-compatible local/remote HTTP server."""

    return SystemOneHTTPEngine(
        name="laya",
        endpoint=endpoint,
        model=model,
        api_key_env=api_key_env,
    )
