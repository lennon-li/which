# Plan: use Hermes + Jev to build and validate Which

Status: proposed
Source: adapted from the existing Obsidian Jev delegation testing plan
Primary execution environment: Hermes using the existing Obsidian Jev advisor
Target repository: `lennon-li/which`

## Objective

Use the already-working Jev delegation advisor inside Obsidian as the **live experimental harness**
for building Which.

This deliberately serves two goals at once:

1. collect prospective Jev routing/calibration data from real Hermes work;
2. use that same real work to build Which into the portable engine-neutral replacement.

Once Which reaches parity and has been validated independently, Obsidian should stop owning the Jev
implementation. Obsidian should consume Which as an external decision framework or remove Jev entirely
if the integration no longer needs a local copy.

The migration rule is:

> Obsidian is the incubator and live test harness. Which becomes the reusable product.

## What already exists in Obsidian

The current Obsidian Jev work already provides the important experimental machinery:

- a versioned task-classification rubric;
- a pure deterministic mapper separate from the classifier;
- an advisory-only `agent-route` command;
- bounded retry and validated typed responses;
- a mandatory blind parent label before the Jev answer is seen;
- privacy-preserving append-only decision logging;
- deterministic routing policy;
- a dispatch lifecycle that records proposal, approval, actual route, and outcome;
- an extractor for historical dispatch packets;
- a plan to use `jevcal` once enough prospective labels exist.

The retrospective historical corpus is explicitly **not** sufficient for calibration. The current
Obsidian analysis found only 23 resolved worker labels from 37 packets, with 19 of 23 going to Jax and
only four weak outcome signals. Treat it as a smoke/regression set only.

Prospective collection is therefore mandatory.

## Core strategy

Every substantial Which task performed through Hermes should become a structured routing experiment.

For each task:

```text
user/Hermes task
      |
      +--> parent blind label              (before Jev)
      |
      +--> Jev classification
      |
      +--> deterministic Obsidian route
      |
      +--> confirmed/overridden route
      |
      +--> worker executes Which task
      |
      +--> independent verification
      |
      +--> outcome/rework/escalation record
      |
      +--> reusable calibration row
```

The resulting dataset should then be exported into Which's engine-neutral benchmark format.

## Important experimental rule: blind labels stay blind

Do not change the current Obsidian rule.

Before Jev returns its answer, Hermes records its own classification of the task. This avoids a
retrospective label being contaminated by Jev's prediction.

At minimum capture:

- complexity;
- task shape;
- implementation intensity;
- objective verifiability;
- expected route/profile if Hermes can state it independently.

The parent label is not assumed to be truth. It is a pre-decision reference point.

## Outcome-informed label review

The named or parent-selected route is also not automatically the gold label.

For each completed task retain:

```text
blind_parent_label
jev_classification
jev_probabilities
jev_recommended_route
confirmed_route
actual_route
outcome
reviewed_label
label_status
review_evidence
```

`label_status` should remain:

- `confirmed`
- `corrected`
- `uncertain`

A label may move to `corrected` only when there is real outcome evidence, such as:

- escalation after capability failure;
- repeated rework;
- independent reviewer rejection;
- revert;
- explicit note that the chosen worker/model was too weak or inappropriate;
- successful cheaper substitute demonstrating over-routing;
- a route failure caused by capability rather than quota/transport.

Do not correct labels merely because a later reviewer prefers a different model.

Quota exhaustion, authentication failure, unavailable worker, and transport failure are **not**
capability evidence and must remain separate.

## Which development work should intentionally generate useful routing cases

Do not manufacture artificial tasks just to collect Jev labels. Use real Which development, but
choose work that naturally covers the routing taxonomy.

### Implementation cases

Examples:

- add a new engine adapter;
- implement CLI options;
- add calibration artifact loading;
- add benchmark import/export;
- implement a Laya runtime adapter;
- add DataGangeR-specific example integration.

### Planning/design cases

Examples:

- design the calibration API;
- define an engine capability contract;
- decide how local model serving should be represented;
- design plugin/optional dependency boundaries.

### Debug/diagnosis cases

Examples:

- Jev/Laya normalization mismatch;
- malformed probability distributions;
- CI failures;
- Laya local endpoint incompatibility;
- calibration regression.

### Independent review cases

Every non-trivial implementation should receive a provider/model-family-independent review.

These cases are especially valuable because they test whether Jev distinguishes implementation from
review reliably.

### Audit / read-only survey cases

Examples:

- audit Which against Obsidian's extracted principles;
- audit external routing frameworks for overlap;
- audit calibration data leakage;
- audit package boundaries and dependency creep.

### Orchestration-decision cases

Examples:

- decide whether a task should remain in Obsidian or move to Which;
- decide whether a new capability belongs in core vs application layer;
- decide whether a failure is a classifier problem, policy problem, or runtime problem.

## First experiment: fix and retest the weakest axis

The Obsidian Jev audit identified `complexity` as the weakest surviving axis and recommends rewriting
its levels as observable symptoms rather than adjectives.

Do this work in Which, not as another Obsidian-specific evolution.

### Current conceptual levels

- Easy
- Medium
- Hard
- Frontier

### Rewrite principle

Describe evidence that can be observed from the task/state, for example:

- bounded single-step change with obvious acceptance test;
- several coordinated files/components with known design;
- cross-cutting change with interacting invariants or tradeoffs;
- task whose goal, architecture, or acceptance criterion itself must be discovered.

Counts and other deterministic quantities must be passed as state, not inferred by the decision
engine.

### Test

Port the existing eight-case probe into Which as an engine-neutral fixture.

Run:

1. current Obsidian/Jev rubric;
2. rewritten Which rubric through Jev;
3. later the same rewritten rubric through Laya.

Compare:

- predicted class;
- probability distribution;
- confidence;
- disagreement with blind parent label;
- downstream route difference.

This becomes Which's first engine-comparison regression test.

## Build sequence

### Phase A — make Which capable of ingesting Obsidian experiments

- [ ] add an import schema for Obsidian Jev decision records;
- [ ] preserve blind label, classifier output, proposal, approval, actual route, and outcome;
- [ ] map Obsidian-specific worker/model names into generic delegation profiles;
- [ ] retain raw Obsidian metadata under a namespaced field rather than polluting Which core;
- [ ] add a converter from Obsidian logs/corpus JSONL to Which benchmark JSONL.

Target:

```text
Obsidian decision log
       -> which import
       -> engine-neutral benchmark row
```

### Phase B — port the delegation rubric into Which

- [ ] move the generic task axes into Which;
- [ ] rewrite complexity with observable criteria;
- [ ] keep deterministic fields out of the classifier;
- [ ] version the rubric independently from Jev;
- [ ] add the eight-case regression set;
- [ ] verify the same spec can be sent to Jev and Laya.

Obsidian should keep its existing classifier untouched during this comparison so there is a stable
reference.

### Phase C — Hermes live collection while building Which

For every suitable Which development task:

- [ ] Hermes records blind parent label;
- [ ] call existing Obsidian Jev advisor;
- [ ] record probabilities and recommendation;
- [ ] confirm or override route;
- [ ] execute through normal AgentPorter/dispatch path;
- [ ] independently verify coding work;
- [ ] record outcome and any escalation/rework;
- [ ] export the completed record into Which.

Do not optimize Jev prompts after every disagreement. Accumulate enough cases to see patterns first.

### Phase D — first prospective checkpoint

At approximately 25-30 real Which tasks:

- inspect class balance;
- inspect route balance;
- inspect confidence distributions;
- inspect confusion between audit/read-only and implementation/review;
- check whether the rewritten complexity axis improved the eight-case probe;
- identify missing task shapes or state fields.

This is diagnostic only, not final calibration.

### Phase E — calibration checkpoint

At roughly 100 labelled cases **per question where feasible**, try `jevcal` or equivalent Which
calibration tooling.

Measure:

- raw accuracy;
- Brier score;
- ECE;
- confidence/coverage curves;
- accepted-case accuracy at candidate thresholds;
- abstention rate;
- disagreement rate with blind parent label;
- disagreement rate between named route and outcome-reviewed route.

Keep a fixed held-out set.

Do not choose thresholds on the held-out set.

### Phase F — add Laya as the second engine

Once the Jev path is working in Which:

- [ ] run the same benchmark through stock Laya;
- [ ] normalize Laya into the same decision schema;
- [ ] compare raw probabilities and hard labels;
- [ ] calibrate Laya separately;
- [ ] compare accepted-case accuracy at equal coverage;
- [ ] compare latency and cost;
- [ ] identify systematic disagreement classes;
- [ ] optionally fine-tune Laya only after a stable gold set exists.

The gold labels and held-out set must remain engine-neutral.

## Do not train Laya on Jev outputs

Jev predictions are experimental measurements, not ground truth.

Laya training data should come from:

- reviewed human labels;
- outcome-informed corrections;
- explicit synthetic/public training data;
- stable annotation guidelines.

Jev can be used as:

- a baseline;
- a disagreement detector;
- an active-learning signal;
- a route to prioritize human review.

It must not become the teacher label automatically.

## Data model for Which

A useful benchmark record should look approximately like:

```json
{
  "id": "which-000123",
  "state": {
    "task": "...",
    "material_breadth": 8,
    "requires_execution": true,
    "requires_repo_artifact": true
  },
  "labels": {
    "complexity": "medium",
    "task_shape": "implementation",
    "implementation_intensity": "medium",
    "objective_verifiability": "high"
  },
  "label_status": "confirmed",
  "predictions": {
    "jev": {
      "model": "typesafe/jev-...",
      "spec_version": "...",
      "answers": {}
    }
  },
  "routing": {
    "recommended_profile": "economy",
    "confirmed_profile": "economy",
    "actual_profile": "economy"
  },
  "outcome": {
    "status": "success",
    "rework": false,
    "escalated": false,
    "independent_review": "pass"
  },
  "provenance": {
    "source": "obsidian-hermes-live",
    "run_id": "...",
    "decision_id": "..."
  }
}
```

Raw prompts should not be duplicated into durable telemetry unless deliberately approved. Hash or
reference sensitive task text where appropriate.

## Separate classifier quality from routing-policy quality

A routing miss can happen in two places:

```text
task
  -> classification wrong
  -> policy receives bad state

or

task
  -> classification right
  -> policy maps it to the wrong profile
```

Which should record both boundaries.

Therefore evaluate:

1. **classification metrics** against human/reviewed labels;
2. **policy metrics** against the final reviewed route/outcome.

Do not collapse these into one 'routing accuracy' number.

This distinction is one of the most important lessons to preserve from Obsidian.

## Hermes should exercise Which itself as soon as possible

Migration should be progressive:

### Stage 1

```text
Hermes -> Obsidian agent-route/Jev -> build Which
```

### Stage 2

```text
Hermes -> Obsidian Jev
        -> Which shadow evaluation
```

Which receives the same task state but does not control routing.

### Stage 3

```text
Hermes -> Which/Jev
        -> Obsidian compares result only
```

Which becomes the primary Jev client and classifier normalization layer. Obsidian retains its policy
and dispatch machinery.

### Stage 4

```text
Hermes -> Which -> Jev or Laya -> normalized decision
                         |
                         v
                 Obsidian routing policy
```

At this point Obsidian no longer owns Jev-specific transport, response parsing, calibration, or
benchmark logic.

### Stage 5

Remove the duplicated Jev implementation from Obsidian after parity tests pass.

Keep only:

- a small Which integration/client;
- Obsidian-specific routing policy;
- Obsidian-specific model inventory/quota/permissions;
- migration documentation and historical logs.

## Parity criteria before removing Jev from Obsidian

Do not remove the working implementation merely because Which can make one successful call.

Require:

- [ ] identical parsing on the existing Jev fixtures;
- [ ] same hard labels on the eight-case regression probe unless intentionally changed;
- [ ] same or explicitly versioned confidence/abstention behavior;
- [ ] bounded retry and provider-failure behavior;
- [ ] no loss of blind-label logging;
- [ ] no loss of privacy-preserving telemetry;
- [ ] same deterministic policy inputs;
- [ ] successful live Hermes shadow run;
- [ ] successful confirmed-route/outcome reconciliation;
- [ ] clean CI in both repos;
- [ ] independent review of the migration.

## What should remain in Obsidian permanently

Do **not** move these into Which:

- agent roster;
- model inventory;
- machine placement;
- quota pools;
- provider/account entitlements;
- access permissions;
- protected-pool rules;
- exact delegation ladder;
- operational dispatch/SSH/runtime authority.

Those are application policy and environment state.

Which should only provide the reusable typed-decision, calibration, evaluation, and normalized
decision interface.

## What should move out of Obsidian

Once parity is reached, move/remove:

- Jev endpoint-specific HTTP code;
- Jev response normalization;
- generic typed-decision schemas;
- generic confidence/abstention logic;
- gold benchmark format;
- calibration tooling;
- engine comparison tooling;
- generic Jev/Laya adapters.

## Success criteria

This plan succeeds if:

1. building Which naturally produces a prospective Jev benchmark;
2. the benchmark contains real, outcome-backed delegation cases rather than synthetic routing demos;
3. Which can reproduce the current Jev classification contract;
4. Laya can be swapped in against exactly the same specification and gold cases;
5. Obsidian retains only its domain-specific routing policy and operational machinery;
6. Jev-specific code can be deleted from Obsidian without losing functionality;
7. Hermes can use Which as the common decision layer for future delegation experiments.

## Immediate next tasks

1. add an Obsidian decision-log importer to Which;
2. port the eight-case Jev probe into Which;
3. rewrite the complexity rubric in Which using observable criteria;
4. have Hermes use the existing Obsidian Jev path for the next real Which implementation task;
5. record the blind label, Jev result, actual route, independent review, and outcome;
6. repeat until the prospective corpus is large enough for calibration.
