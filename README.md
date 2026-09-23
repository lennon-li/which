# Which

**Which** is a pluggable typed-decision framework. Its first application is **model
and agent delegation**: classify a task with a fast decision engine, normalize the
result, then apply explicit deterministic policy to decide what should happen.

The core rule is simple:

> The engine classifies. The application owns the standard and the action.

That keeps Jev, Laya, future learned routers, and deterministic baselines
interchangeable.

## Why this exists

Typed-decision models make impressive demos, but they do not know your standards by
default. Real deployment still needs:

- explicit labels and rubrics;
- representative gold cases;
- held-out evaluation;
- confidence/coverage thresholds;
- drift checks;
- deterministic policy for facts the model should not guess.

Which makes those pieces first-class and keeps the calibration dataset independent of
the engine.

## Architecture

```text
state
  |
decision specification
  |
DecisionEngine
  |-- Jev (hosted)
  |-- Laya (local/remote)
  |-- future engines
  |
normalized labels + probabilities
  |
confidence / abstention
  |
application policy
  |
delegation advice or another domain action
```

The initial delegation specification classifies four fuzzy axes:

- complexity;
- task shape;
- implementation intensity;
- objective verifiability.

Knowable facts such as file counts, release state, data sensitivity, quota state, and
deployment reach stay outside the learned classifier.

## Jev and Laya

Both adapters target a common System-One style contract: state + typed questions in,
typed answers/probabilities out.

Jev is configured as a hosted OpenRouter engine. Laya is configured with a local or
remote Jev-compatible HTTP endpoint, so the same decision specification and gold
dataset can be used for both.

```bash
pip install -e ".[dev]"

# Jev
export OPENROUTER_API_KEY=...
which \
  --engine jev \
  --state examples/state.json \
  --spec configs/delegation-spec.yaml \
  --policy configs/delegation-policy.yaml

# Laya
which \
  --engine laya \
  --laya-endpoint http://127.0.0.1:8000/v1/system-one \
  --state examples/state.json \
  --spec configs/delegation-spec.yaml \
  --policy configs/delegation-policy.yaml
```

The Laya URL is deliberately configurable; Which does not own Laya serving.

## Calibration and evaluation

Use one gold dataset for every engine:

```json
{"id":"case-001","state":{"task":"Review this patch"},"labels":{"complexity":"medium","task_shape":"independent_review"}}
```

`which.evaluation` reads this simple JSONL shape and reports accuracy, handled
coverage, accepted accuracy, and Brier score where probabilities are available.

For threshold fitting and drift checks, do not reinvent existing work. The repository
[jevcal](https://github.com/abhixhek/jevcal) already implements a strong calibration
workflow and uses the same basic `id/state/labels` dataset shape. Which should
interoperate with it rather than clone it.

## What came from Obsidian

The reusable routing work in Obsidian was distilled into generic principles rather
than copied with its private machine/account assumptions:

- classifier and deterministic router are separate;
- countable/known facts are computed, not inferred;
- low-confidence classifications abstain;
- capability floors belong to policy;
- quota failure is not capability failure;
- consequential review can require provider/model-family independence;
- calibration data belongs to the decision problem, not to Jev.

See [docs/obsidian-extraction.md](docs/obsidian-extraction.md).

## Existing work we should reuse

Before building more infrastructure, see [docs/prior-art.md](docs/prior-art.md).
The important neighboring projects include:

- [RouteLLM](https://github.com/lm-sys/RouteLLM) for learned strong/weak model routing
  and router benchmarking;
- [vLLM Semantic Router](https://github.com/vllm-project/semantic-router) for
  programmable production model routing;
- [Aurelio Semantic Router](https://github.com/aurelio-labs/semantic-router) for
  low-latency embedding/intent routing;
- [LiteLLM](https://github.com/BerriAI/litellm) for provider transport, load balancing,
  retry, fallback, and usage infrastructure;
- [Laya](https://github.com/NandhaKishorM/laya) and
  [@receptron/laya](https://github.com/receptron/laya) for open/local System-One
  inference;
- [jevcal](https://github.com/abhixhek/jevcal) for calibration and drift checking.

Which should sit **above decision engines and below application policy**. It should not
become another inference gateway.

## Status

Early scaffold. The current code establishes the engine-neutral contract, Jev/Laya HTTP
adapters, delegation policy boundary, and evaluation data format. Next work should be
driven by comparative Jev/Laya calibration experiments rather than adding framework
surface area speculatively.
