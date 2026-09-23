# DSI Claude Credit Budget — Bottom-Up Planning Model

**Date:** 2026-09-22  
**Working request:** CAD $75,000 / 12 months  
**Purpose:** Internal planning support for the DSI Claude API Credit Award application.

## Current planning rates

Claude API prices are in USD.

| Model / mode | Input | Output | Planned role |
|---|---:|---:|---|
| Claude Sonnet 5 | US$2 / 1M | US$10 / 1M | high-volume experiments, trainee workflows |
| Claude Opus 5.5 | US$4 / 1M | US$20 / 1M | complex coding, independent review, version re-evaluation |
| Claude Fable 5.1 | US$10 / 1M | US$50 / 1M | selected high-stakes planning/risk adjudication |
| Claude Sonnet 5 Batch | US$1 / 1M | US$5 / 1M | bulk benchmark and robustness scoring |

**Freshness note.** Opus 5.5 was released on September 22, 2026. Fable 5.1 remains Anthropic's documented public Fable release. The budget uses that released model and its published price. Any officially released successor would require a verified API identifier, price, and prospective protocol amendment before substitution; no future-model rate is assumed.

Bank of Canada daily rate used for planning: **1 USD = 1.4064 CAD**.

## Planned workload assumptions

| Workload | Runs/evals | Avg input/run | Avg output/run | Model/mode | Estimated USD |
|---|---:|---:|---:|---|---:|
| Candidate-case / labelled-data research | 5,000 | 150k | 15k | Sonnet 5 | $2,250 |
| High-stakes planning/risk adjudication | 2,000 | 200k | 20k | Fable 5.1 | $6,000 |
| Bulk benchmark / robustness scoring | 200,000 | 20k | 3k | Sonnet 5 Batch | $7,000 |
| Orchestration / regression validation | 10,000 | 300k | 30k | Sonnet 5 | $9,000 |
| Trainee research | 9,500 | 250k | 25k | Sonnet 5 | $7,125 |
| Open-source coding / validation | 4,000 | 500k | 50k | Opus 5.5 | $12,000 |
| Conditional public-health implementation pilot | 3,000 | 350k | 30k | Sonnet 5 | $3,000 |
| Model/version re-evaluation | 4,000 | 250k | 25k | Opus 5.5 | $6,000 |
| **Total** |  |  |  |  | **$52,375 USD** |

Here a **run** is one budgeted workload unit with the row's average input and output tokens. The 200,000 **bulk evaluations** are one Claude API call each, planned as approximately 2,500 candidate cases × 4 controlled variants × 4 repeats × 5 pre-specified model/rubric-version conditions. These factors describe usage and robustness work, **not 200,000 independent cases or statistical power**. Family-level inference uses the separately human-adjudicated benchmark. The other rows are **aggregate sessions**: their token totals represent all calls, tool turns, retries, and accumulated context within a session, not a single API request. Log actual calls and tokens within each session so the budget can be reconciled with invoices.

Each row is calculated as runs × (average input tokens × listed input price + average output tokens × listed output price) / 1,000,000, rounded to the nearest USD dollar. The averages are planning totals, not per-request context-window claims. Only the bulk row assumes the listed 50% Batch price. Other rows use uncached standard rates; caching may reduce actual cost, but no cache-hit discount is counted and cache writes, retries, or non-Batch runs must be logged at their actual rates. At 1.4064 CAD/USD, US$52,375 × 1.4064 = CAD $73,660.20, reported as approximately **CAD $73,660** to the nearest $10. The CAD $75,000 request leaves approximately CAD $1,340 for exchange-rate and workload variation. Recheck published rates and exchange conversion before submission.

## Classification-error fallback and risk control

The package must assume that classifiers will sometimes be wrong. A model prediction is therefore **evidence, not authorization**.

Operational fallback:
1. **Hard blockers dominate.** Known direct identifiers, prohibited exposures, and other deterministic constraints cannot be overridden by a model.
2. **Abstain on uncertainty.** Calibrated confidence below a pre-specified threshold routes to human review.
3. **Escalate disagreement.** Material disagreement between deterministic rules, the interpretable statistical model, and semantic models triggers review.
4. **Fail conservatively.** Out-of-distribution or malformed cases default to a more restrictive representation, transformation, or no direct exposure.
5. **Human release gate.** Consequential policy/model releases require explicit human approval.
6. **Audit and rollback.** Every decision records versions, scores, evidence, and overrides. Regression monitoring can suspend or roll back a model/checkpoint/policy.
7. **Measure the failure mode.** The primary safety endpoint includes inappropriate authorization, so the fallback is empirically evaluated.

## Why use multiple Claude tiers

- **Sonnet 5:** economical high-volume experimental work.
- **Opus 5.5:** newly released frontier model for complex coding, independent review, and version-drift evaluation.
- **Fable 5.1 / verified officially released successor:** selected planning, risk evaluation, and difficult-case review where the higher cost is justified.
- **Local Laya:** privacy-preserving local decision model; tuning uses local/separately funded compute.
- **Jev:** hosted typed-decision comparator; calibrated/evaluated rather than treated as a local trainable checkpoint.

This portfolio lets the study test whether expensive frontier reasoning is actually necessary, and where compact/local models are sufficient.

## Sources

- DSI Claude API Credit Award: https://datasciences.utoronto.ca/claude-api-credit/
- Anthropic Opus 5.5 announcement: https://www.anthropic.com/claude-opus-5-5
- Anthropic Claude Platform pricing: https://platform.claude.com/docs/en/about-claude/pricing
- Anthropic Fable 5.1 docs: https://platform.claude.com/docs/en/models/fable-5-1/overview
- Bank of Canada Daily Digest: https://www.bankofcanada.ca/rates/daily-digest/
