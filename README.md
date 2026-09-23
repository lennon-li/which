# Which

**Which is planned as an open-source decision and evaluation layer for safer AI
access to research data.** The goal is to help researchers decide what an AI
agent may see for a specific task: a schema, aggregate summaries, transformed or
synthetic data, or no data at all.

> **Project status:** This is the planned direction, not a claim that the full
> system or proposed research has been completed or funded. Which is an early
> scaffold; the privacy-firewall evaluation and integrations described here are
> proposed work.

## What we aim to build

An auditable AI privacy firewall that evaluates a proposed data-access request
and recommends one of four actions:

- allow a bounded, minimum-necessary view;
- transform, redact, aggregate, or synthesize the data first;
- defer to a human reviewer; or
- block exposure under the stated conditions.

The decision should combine evidence without letting a model set policy:

1. **Deterministic safeguards** catch known risks such as direct identifiers or
   prohibited disclosure conditions.
2. **Statistical models** assess measurable properties such as uniqueness,
   sensitivity, and data granularity.
3. **Semantic decision models** interpret bounded descriptions of the data,
   task, and access environment. The research will test compact local models;
   hosted models such as Claude may serve as comparators.
4. **Explicit policy and human review** handle hard blockers, uncertainty, and
   disagreement. The system should abstain when evidence is insufficient.

The firewall is a decision aid—not a guarantee of anonymity, a legal or
regulatory-compliance determination, or permission to expose data by itself.

## What Which contributes

Which is intended to provide the model-neutral decision infrastructure:
typed decision specifications, model adapters, normalized probabilities,
calibration, abstention, and reusable evaluation. Its purpose is to measure
whether a model's scores are reliable and useful—not to define what data are
safe.

[DataGangeR](https://github.com/lennon-li/dataganger) supplies the privacy
domain and data-handling context: deterministic disclosure checks, safer
synthetic-data workflows, and potential integration points for applying an
access decision. DataGangeR defines the privacy problem; Which provides reusable
decision and evaluation tools.

## Planned research

The proposed study will build a human-reviewed benchmark from public and
synthetic scenarios, then compare deterministic safeguards, interpretable
statistical models, compact local semantic models, and frontier-model
comparators. It will measure calibration, high-risk errors, uncertainty,
abstention, robustness, and human-review burden. A combined or dual-gate system
will be kept only if held-out results justify its added complexity. Any partner
pilot is conditional on approvals and is not required for the core research.

The intended outputs are reusable evaluation software, a documented benchmark
and protocol, an evaluated access-decision approach, and implementation
guidance. The project is deliberately gated: if semantic models do not add
reliable value, the simpler rules/statistical approach remains the result.

Read the [full technical proposal](docs/grants/2026-09-dsi-anthropic-ai-privacy-firewall-proposal.md)
for the detailed questions, methods, work packages, and timeline.
