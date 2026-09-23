# DSI Claude Credit Budget — Bottom-Up Planning Model

**Date:** 2026-09-22  
**Working request:** CAD $75,000 / 12 months  
**Purpose:** Internal planning support for the DSI Claude API Credit Award application.

## Current planning rates

Claude API prices are in USD.

| Model / mode | Input | Output |
|---|---:|---:|
| Claude Sonnet 5, standard | US$2 / 1M tokens | US$10 / 1M tokens |
| Claude Opus 5, standard | US$5 / 1M tokens | US$25 / 1M tokens |
| Claude Sonnet 5, batch | US$1 / 1M tokens | US$5 / 1M tokens |

Batch processing is 50% of standard API pricing.

Bank of Canada daily rate on 2026-09-22: **1 USD = 1.4064 CAD**. Therefore:
- CAD $50,000 ≈ US$35,552
- CAD $75,000 ≈ US$53,328
- CAD $100,000 ≈ US$71,104

## Planned workload assumptions

| Workload | Runs/evals | Avg input/run | Avg output/run | Model/mode | Estimated USD |
|---|---:|---:|---:|---|---:|
| Candidate-case / labelled-data research | 5,000 | 150k | 15k | Sonnet standard | $2,250 |
| High-capability adjudication/error review | 2,000 | 200k | 20k | Opus standard | $3,000 |
| Bulk benchmark / robustness scoring | 200,000 | 20k | 3k | Sonnet batch | $7,000 |
| Orchestration / regression validation | 10,000 | 300k | 30k | Sonnet standard | $9,000 |
| Trainee research | 9,000 | 250k | 25k | Sonnet standard | $6,750 |
| Open-source coding / validation | 7,000 | 500k | 50k | Sonnet standard | $10,500 |
| Conditional public-health implementation pilot | 3,000 | 350k | 30k | Sonnet standard | $3,000 |
| Model/version re-evaluation | 6,000 | 250k | 25k | Opus standard | $11,250 |
| **Total** |  |  |  |  | **$52,750 USD** |

At 1.4064 CAD/USD, this is approximately **CAD $74,180**.

## Formula checks

- Sonnet 150k input + 15k output = 0.15×$2 + 0.015×$10 = **$0.45/run**
- Opus 200k input + 20k output = 0.20×$5 + 0.020×$25 = **$1.50/run**
- Sonnet Batch 20k input + 3k output = 0.020×$1 + 0.003×$5 = **$0.035/evaluation**
- Sonnet 300k input + 30k output = 0.30×$2 + 0.030×$10 = **$0.90/run**
- Sonnet 250k input + 25k output = 0.25×$2 + 0.025×$10 = **$0.75/run**
- Sonnet 500k input + 50k output = 0.50×$2 + 0.050×$10 = **$1.50/run**
- Sonnet 350k input + 30k output = 0.35×$2 + 0.030×$10 = **$1.00/run**
- Opus 250k input + 25k output = 0.25×$5 + 0.025×$25 = **$1.875/run**

## Why these workloads are plausible

The high call count is driven mostly by **200,000 inexpensive batch evaluations**, not by hundreds of thousands of interactive researcher sessions. Agentic runs are long-context, multi-step research/software workflows that may include repository context, data dictionaries, benchmark cases, model outputs, validation traces, tool results, and iterative code/review cycles.

A proposed trainee scale of roughly 4–6 students/research trainees can account for ~9,000 supervised research runs over a year without requiring extreme individual use. For example, 5 trainees × 180 active research days × 10 API workflows/day = 9,000 workflows.

The model-version allocation is intentionally substantial because the project studies calibration and robustness in a fast-changing technology environment. It allows a frozen benchmark to be re-run prospectively when materially different Claude or local-model versions appear.

## Sensitivity / safeguards

This is a **planning model, not a commitment to manufacture usage**.

Factors that may reduce spend:
- prompt caching;
- increased use of batch processing;
- model price reductions;
- shorter-than-assumed contexts;
- a pilot not proceeding.

Factors that may increase spend:
- newly released higher-capability models;
- larger context requirements;
- additional independent replications;
- newly discovered failure modes requiring challenge-set expansion.

If realized costs are lower, capacity should be reassigned in this order:
1. independent held-out replication;
2. robustness/adversarial testing;
3. model/version re-evaluation;
4. regression validation of open-source releases;
5. additional human-adjudicated benchmark cases.

The scientific objectives and benchmark definition should not be expanded merely to consume credits.

## Sources

- DSI Claude API Credit Award: https://datasciences.utoronto.ca/claude-api-credit/
- Anthropic Claude Platform pricing: https://platform.claude.com/docs/en/about-claude/pricing
- Anthropic batch-processing pricing: https://platform.claude.com/docs/en/build-with-claude/batch-processing
- Bank of Canada Daily Digest: https://www.bankofcanada.ca/rates/daily-digest/
