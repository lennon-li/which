# Plan: optional Laya domain adaptation for DataGangeR

Status: proposed
Owner repo for generic decision/calibration machinery: **Which**
First downstream application: **DataGangeR**

## Goal

Use Laya as an optional, local semantic decision engine inside DataGangeR without
weakening DataGangeR's deterministic privacy rules or human review gate.

The central design rule is:

> deterministic rules establish hard facts and safety floors; Laya adds semantic
> evidence; explicit policy reconciles the two; a human still owns ambiguous or
> consequential release decisions.

This should remain engine-neutral at the Which layer so the same gold data and
decision specification can later be evaluated with Jev or other engines.

## Why DataGangeR is a strong first domain-adaptation target

DataGangeR already separates fuzzy semantic judgment from deterministic checks:

- direct identifier / combination identifier / non-identifier;
- sensitive vs non-sensitive;
- semantic column role;
- deterministic checks for dates, cardinality, structured IDs, exact-row matches,
  disclosure flags, and k-anonymity-related logic;
- explicit human review when confidence is insufficient.

That is a good match for a small typed decision model. Laya should improve uncertain
semantic classification, not replace deterministic checks.

## Scope

Initial Laya decisions should be column-level and bounded. Do not pass entire datasets.

Candidate typed outputs:

1. `identifies`
   - none
   - combination
   - direct

2. `sensitive`
   - false
   - true

3. `semantic_role`
   - identifier
   - demographic
   - geography
   - health
   - financial
   - credential
   - free_text
   - measurement
   - coded_category
   - other

Optional later outputs:

- confidence that the deterministic detector is wrong;
- requires_human_review;
- likely quasi-identifier combination risk.

## Input representation

Construct a compact local summary per column. Candidate fields:

- column name;
- R/storage type;
- number of rows;
- number and proportion distinct;
- missingness;
- median/min/max string length;
- representative public/synthetic sample values;
- detected regex/pattern families;
- date-like / postal-like / structured-ID flags;
- current deterministic recommendation;
- dataset-level context that is safe and useful, such as neighboring column names.

Do not include full sensitive columns by default.

The representation should be deterministic and versioned so calibration runs are
reproducible.

## Safety policy

Laya must not silently downgrade a deterministic privacy warning.

Examples:

- deterministic `direct` + Laya `none` -> keep `direct`, record disagreement;
- deterministic unknown + high-confidence Laya `direct` -> escalate to direct/review;
- deterministic non-sensitive + high-confidence Laya sensitive -> flag for review;
- low-confidence Laya result -> no automatic change;
- any consequential conflict -> human review.

The first release should allow Laya to make the system more conservative, not less
conservative.

## Architecture

```text
DataGangeR column
      |
      +--> deterministic role detector
      |
      +--> compact semantic summary
                |
                v
            Which spec
                |
                v
          DecisionEngine
             |     |
            Jev   Laya
                   |
                   v
       normalized probabilities
                |
                v
        reconciliation policy
                |
                v
          human review gate
```

Which owns:

- decision specification;
- engine adapter contract;
- normalized probability/label output;
- calibration/evaluation tooling;
- benchmark data schema.

DataGangeR owns:

- feature/summary construction;
- privacy taxonomy;
- deterministic safety rules;
- reconciliation policy;
- user-facing review workflow.

## Dependency model

Laya must be optional.

DataGangeR default behavior remains network-free and dependency-light:

```r
roles <- detect_roles(dat)
```

Optional semantic augmentation:

```r
roles <- detect_roles(
  dat,
  semantic_engine = "laya"
)
```

Prefer a local service or local runtime installed separately. Do not bundle large model
weights inside the CRAN tarball.

A possible configuration API:

```r
configure_semantic_engine(
  engine = "laya",
  endpoint = "http://127.0.0.1:8000/v1/system-one",
  model = "dataganger-laya-v1"
)
```

## Phase 1: baseline benchmark before training

Do not fine-tune first.

Build an engine-neutral benchmark and compare:

1. current DataGangeR deterministic heuristics;
2. stock Laya zero-shot;
3. stock Laya + probability calibration;
4. deterministic + Laya hybrid;
5. Jev on the same decision spec, where practical.

Primary metrics should reflect asymmetric privacy costs:

- sensitivity/recall for direct identifiers;
- sensitivity/recall for sensitive columns;
- false-negative rate for direct/sensitive labels;
- specificity / false-positive burden;
- balanced accuracy;
- Brier score;
- calibration error;
- coverage at each abstention threshold;
- accepted-case accuracy after abstention.

Do not optimize on overall accuracy alone.

## Phase 2: build a public/synthetic gold corpus

Target initial benchmark: roughly 1,000-2,000 well-curated cases.

Use public or synthetic sources only for the initial open benchmark.

### Candidate sources

- AI4Privacy OpenPII synthetic PII corpus;
- Microsoft Presidio examples/evaluation data;
- public tabular datasets with documented semantic columns;
- synthetic columns generated from known entity classes;
- hand-built hard-negative and ambiguity cases.

### Convert entity examples into column-level cases

PII corpora are usually entity-level. DataGangeR needs column-level judgments.

Generate examples such as:

- patient_id;
- study_subject_number;
- postal_code;
- visit_date;
- diagnosis_code;
- free_text_notes;
- annual_income;
- race_ethnicity;
- lab_value;
- temperature;
- product_id;
- order_number;
- random UUID;
- city;
- age;
- occupation.

Include realistic value distributions and misleading column names.

### Combination-risk cases

Create cases where no single variable is a direct identifier but combinations can be:

- age + sex + postal code;
- date of birth + rare diagnosis;
- city + occupation;
- geographic unit + age band + event date.

These are needed to learn DataGangeR's `combination` concept rather than generic PII
recognition.

### Hard negatives

Explicitly include:

- numeric high-cardinality measurements;
- product/order IDs that do not identify people;
- date columns with no person-level linkage;
- columns named `id` that are not person identifiers;
- disease-like words in non-sensitive contexts;
- synthetic/fake names;
- coded categories that resemble identifiers.

Hard negatives are essential to prevent a conservative model from becoming useless.

## Annotation contract

Create a versioned annotation guide before collecting large numbers of labels.

Each benchmark row should include at least:

```json
{
  "id": "case-0001",
  "state": {
    "column_name": "patient_id",
    "storage_type": "character",
    "n_rows": 500,
    "distinct_ratio": 1.0,
    "sample_values": ["P001", "P002", "P003"]
  },
  "labels": {
    "identifies": "direct",
    "sensitive": true,
    "semantic_role": "identifier"
  },
  "metadata": {
    "source": "synthetic",
    "annotator": "expert",
    "certainty": "high"
  }
}
```

Recommended metadata:

- source dataset/corpus;
- public/synthetic provenance;
- annotation version;
- annotator;
- certainty;
- rationale;
- split assignment;
- difficulty / hard-negative flag.

Keep train/calibration/test separation fixed once the first benchmark is frozen.

## Phase 3: calibration

Before changing weights, calibrate stock Laya probabilities against the DataGangeR gold
set.

Candidate methods:

- temperature scaling;
- per-question thresholds;
- class-specific abstention thresholds;
- conservative thresholding for direct/sensitive labels.

Use a separate calibration split.

Example policy:

```text
P(direct) >= 0.90       -> flag direct
0.50 <= P(direct) < .90 -> human review
P(direct) < 0.50        -> do not downgrade deterministic result
```

Thresholds must be selected against target error rates, not chosen ad hoc.

Store calibration artifacts separately from model weights:

```text
artifacts/
  dataganger/
    spec-v1.yaml
    calibration-v1.json
    benchmark-manifest.json
```

## Phase 4: fine-tune Laya

Only fine-tune after:

- taxonomy is stable;
- annotation guide is stable;
- baseline and calibrated stock Laya are measured;
- residual error patterns justify domain adaptation.

Training data can combine:

- public/synthetic gold cases;
- augmented variants;
- hard negatives;
- combination-risk cases;
- later, opt-in de-identified real-world annotations if governance permits.

Keep the held-out test set untouched.

Track:

- base Laya checkpoint;
- training corpus version/hash;
- training code/parameters;
- random seed;
- calibration artifact;
- benchmark metrics;
- license/provenance of every training source.

Publish model weights separately from the R package.

Possible model naming:

- `dataganger-laya-v1`
- `which-laya-dataganger-v1`

## Phase 5: hybrid integration in DataGangeR

Add a semantic augmentation layer around existing `detect_roles()`.

Proposed internal flow:

```text
detect_roles()
  -> deterministic roles
  -> summarize_columns_for_semantic_engine()
  -> semantic_role_engine()
  -> reconcile_role_evidence()
  -> dataganger_roles + provenance/confidence
```

Potential additional columns:

- `semantic_engine`;
- `semantic_model`;
- `semantic_identifies`;
- `semantic_sensitive`;
- `semantic_role`;
- `semantic_confidence`;
- `semantic_probabilities`;
- `semantic_disagreement`;
- `semantic_requires_review`.

Do not overwrite original deterministic evidence; retain both for auditability.

## Phase 6: prospective evaluation

After integration, prospectively collect:

- human overrides;
- deterministic/Laya disagreements;
- confidence;
- final human decision;
- downstream privacy flags.

Use these only as a future learning corpus after explicit governance/provenance checks.

Avoid silent online training. Model updates should be versioned offline releases.

## Relationship to Which

Which should remain more general than DataGangeR.

Reusable pieces to add to Which over time:

- benchmark schema;
- calibration split support;
- threshold fitting;
- reliability/calibration plots;
- class-specific abstention rules;
- engine comparison reports;
- model artifact manifests;
- adapter for local Laya inference;
- optional jevcal interoperability.

Do not put DataGangeR privacy policy into Which core.

A future package structure could be:

```text
which/
  core/
  engines/
    jev
    laya
  evaluation/
  calibration/
  applications/
    delegation/
    examples/
      dataganger/
```

DataGangeR itself remains the authoritative implementation of the privacy application.

## Deliverables

### Milestone A — benchmark design

- [ ] freeze DataGangeR semantic taxonomy v1;
- [ ] write annotation guide;
- [ ] define engine-neutral JSONL schema;
- [ ] assemble first 200 hand-reviewed cases;
- [ ] add deterministic baseline evaluator.

### Milestone B — public benchmark

- [ ] ingest/transform approved public PII resources;
- [ ] generate hard negatives and combination-risk cases;
- [ ] reach 1,000-2,000 curated cases;
- [ ] freeze train/calibration/test splits;
- [ ] document data licenses and provenance.

### Milestone C — Laya baseline

- [ ] run stock Laya;
- [ ] measure privacy-weighted metrics;
- [ ] fit calibration/abstention thresholds;
- [ ] compare stock vs calibrated vs deterministic hybrid;
- [ ] run Jev on the same benchmark where useful.

### Milestone D — fine-tuning experiment

- [ ] fine-tune Laya on training split;
- [ ] calibrate on calibration split;
- [ ] evaluate once on untouched test split;
- [ ] compare against stock Laya and hybrid baseline;
- [ ] publish reproducible training manifest.

### Milestone E — optional DataGangeR integration

- [ ] add optional semantic-engine interface;
- [ ] add local Laya adapter;
- [ ] add reconciliation policy;
- [ ] preserve deterministic safety floors;
- [ ] expose disagreement/confidence in Configure UI;
- [ ] add no-network regression tests proving default behavior is unchanged;
- [ ] add documentation and opt-in setup instructions.

## Non-goals

- Laya does not replace DataGangeR's privacy checks.
- Laya does not autonomously approve public release.
- Which does not become a model-serving gateway.
- The CRAN package does not bundle large model weights.
- User data is not silently collected for training.
- Online/self-modifying training is out of scope.

## Success criteria

The integration is worthwhile if the hybrid system:

1. reduces unresolved/manual classifications;
2. does not materially increase false negatives for direct identifiers or sensitive
   columns;
3. is better calibrated than stock Laya;
4. preserves DataGangeR's default local/no-network behavior;
5. remains auditable and reproducible by model/spec/calibration version;
6. shows measurable improvement on an untouched public/synthetic test set.
