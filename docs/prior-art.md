# Prior art and what Which should reuse

Which is not intended to become another inference gateway. The useful boundary is
a small engine-neutral typed-decision and evaluation layer, with model delegation
as the first application.

## RouteLLM

https://github.com/lm-sys/RouteLLM

Useful: router interface, benchmark-first development, learned routing from preference
data, and explicit cost/quality tradeoffs.

Do not duplicate: serving infrastructure or strong-vs-weak learned routing. Which can
eventually expose RouteLLM as another delegation engine.

## vLLM Semantic Router

https://github.com/vllm-project/semantic-router

Useful: separate request signals, application policy, and model/compute pools; treat
privacy, latency, cost, and capability as explicit routing dimensions.

Do not duplicate: production inference infrastructure, Kubernetes integration, model
serving, or signal processors.

## Aurelio Semantic Router

https://github.com/aurelio-labs/semantic-router

Useful: embedding-based semantic intent routing is a valid low-latency decision engine.
It is complementary to Jev/Laya rather than something Which should reimplement.

## LiteLLM

https://github.com/BerriAI/litellm

Useful: provider abstraction, retries, fallbacks, rate limits, cost tracking, and
load-balancing are mature transport concerns.

Do not duplicate: API provider adapters or production load balancing. A future Which
execution layer should hand a selected model/profile to LiteLLM or another gateway.

## Jev

TypeSafe's System-One API is the original hosted typed-decision engine used by the
Obsidian routing work. Which keeps Jev behind an engine adapter and never lets Jev
own application policy.

## Laya

Reference implementation:
https://github.com/NandhaKishorM/laya

Jev-compatible ONNX/TypeScript runtime:
https://github.com/receptron/laya

Useful: open-weight local System-One decisions with the same choice/score/noul style.
Because the request/response contract is intentionally close to Jev, Which uses one
SystemOne HTTP normalization layer for both.

## jevcal

https://github.com/abhixhek/jevcal

This is the strongest existing calibration resource found. It already implements
threshold fitting, held-out validation, coverage/accuracy tradeoffs, ECE, drift checks,
and a JSONL shape of id/state/labels.

Which should interoperate rather than rebuild all of that. Its evaluation loader uses
the same simple id/state/labels dataset shape. A later integration can import/export
jevcal lock files while keeping the gold dataset engine-neutral.

## Braintrust / Langfuse

https://github.com/braintrustdata
https://github.com/langfuse/langfuse

Useful for general evaluation, tracing, regression analysis, and observability. Which
should emit clean events that these systems can ingest rather than inventing another
observability platform.

## Design conclusion

The missing piece is not another router or gateway. It is a small layer that lets one
decision specification and one gold dataset be run against multiple typed-decision
engines, normalized into a common result, calibrated, and then consumed by explicit
application policy.
