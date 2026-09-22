# Who Should See the Data?
## Calibrated Statistical and Semantic Gates for Privacy-Preserving AI Access to Research Data

**Faculty discussion draft — September 2026**  
**Target:** University of Toronto Data Sciences Institute Claude API Credit Award — Research tier  
**Requested support:** CAD $75,000 in Claude API credits over 12 months

---

## Project summary

AI agents are becoming useful participants in statistical programming, data cleaning, analysis, visualization, and research software development. This creates a practical privacy question that current tools do not directly answer:

> **When should an AI agent be allowed to see research data, and when should those data first be transformed, restricted, or reviewed by a human?**

Existing privacy tools can detect identifiers, estimate disclosure risk, synthesize data, and enforce access rules. What is missing is a **calibrated, task-aware decision layer** that considers what the data contain, what the AI agent is being asked to do, where the agent operates, and what representation of the data is actually necessary.

The proposed research compares three complementary sources of evidence:

1. **Deterministic privacy safeguards** for facts that should not be delegated to a model.
2. **Interpretable statistical risk models** based on measurable properties of the data, intended use, and access environment.
3. **Semantic decision models** that can interpret natural-language dataset descriptions, data dictionaries, and proposed AI tasks.

A key recent development makes the project newly practical. The release of compact open decision models such as **Laya** fills a missing piece: the semantic privacy gate itself can run locally, inside the trusted environment, rather than sending potentially sensitive context to another external model merely to decide whether the data may leave.

Claude will be used as a **frontier semantic comparator and research instrument**, not as ground truth or as the authority deciding whether data are safe.

### Central research question

> **Does semantic information in natural-language descriptions of research data and proposed AI use provide incremental, calibrated information about privacy risk beyond conventional statistical and structural predictors?**

A second question is whether a compact local model can recover enough of that semantic signal to serve as a practical privacy gate in front of a more capable AI agent.

---

## Why this matters

The same dataset can present very different risks depending on the task. An AI coding agent may need only a schema or realistic synthetic data rather than participant-level records. A locally hosted model presents a different exposure boundary from a cloud API. Fine-grained dates, geography, or free text may be acceptable in one context but highly identifying in another.

The goal is therefore not to label a dataset universally “safe.” The system instead recommends an action under a specified use case:

- bounded access is acceptable;
- transform, redact, aggregate, or synthesize first;
- human review is required;
- direct exposure is inappropriate under the stated conditions.

A favorable model prediction would never override a deterministic privacy blocker.

---

## Proposed architecture

~~~mermaid
flowchart TB
    A["Research data"] --> B["Local deterministic privacy checks"]
    A --> C["Bounded local summary / data dictionary"]
    B --> D["Structured privacy features"]
    D --> E["Interpretable statistical risk model"]
    C --> F["Compact local semantic model<br/>(e.g. Laya)"]
    E --> G["Calibrated statistical evidence"]
    F --> H["Calibrated semantic evidence"]
    B --> I["Hard blockers / known facts"]
    G --> J["Transparent evidence fusion"]
    H --> J
    I --> J
    J --> K{"Access policy"}
    K -->|Bounded access| L["Minimum necessary view"]
    K -->|Transform first| M["Redact / aggregate / synthesize"]
    K -->|Uncertain| N["Human review"]
    K -->|High risk| O["Do not expose"]
~~~

The statistical and semantic components provide evidence; the policy and human-review layer retains authority.

---

## Study design

The primary unit will be a **data-access scenario** containing a dataset description, selected variable descriptions, measurable structural characteristics, intended research purpose, proposed AI task, execution environment, transformations already applied, and an expert-reviewed recommended action.

The initial benchmark will target approximately **2,000–5,000 curated scenarios**, drawing primarily from public research documentation, public data dictionaries, governance guidance, public/synthetic privacy examples, and controlled counterfactual cases. A high-value subset will receive independent double annotation.

Development, calibration, and final test sets will be frozen before final model comparison.

### Comparators

- existing deterministic privacy logic;
- penalized logistic/ordinal regression and generalized additive models;
- compact local semantic models such as Laya;
- Claude as a frontier semantic comparator;
- transparent combinations only if each component demonstrates incremental value.

### Primary evaluation

The emphasis will be on consequential error and calibration rather than raw accuracy:

- false-negative rate for high-risk cases;
- Brier score / proper probabilistic loss;
- calibration;
- selective risk at pre-specified coverage;
- coverage under abstention thresholds;
- human-review burden.

A central operational measure is:

> **Among cases the system chooses not to defer to a human, how often is its decision correct?**

The project will also test robustness to paraphrasing, variable renaming, irrelevant wording, local versus external execution, schema-only versus row-level access, changes in temporal/geographic precision, free text, synthetic transformation, and combinations of quasi-identifiers.

---

## Existing foundation

### DataGangeR

**DataGangeR** is an existing R package for privacy-aware synthetic data and human-gated research/AI workflows. It grew from a practical question: if an AI coding or research agent only needs data with the right structure and statistical behavior, why expose original participant-level data unnecessarily?

Its current workflow includes deterministic privacy checks, identifier and free-text detection, sensitive-field handling, exact source-to-synthetic record checks, k-anonymity-related diagnostics, synthetic-data disclosure assessment, utility assessment, reproducible synthesis, explicit human approval, and local/no-network safeguards.

This project extends DataGangeR from privacy diagnostics and transformation to the broader question of **what representation an AI agent should receive for a particular task**.

### Which

**Which** is a small engine-neutral framework for typed decisions, normalized probabilities, calibration, abstention, and model comparison.

The boundary is intentional:

- **Which** owns generic decision/evaluation infrastructure.
- **DataGangeR** owns the privacy threat model, statistical predictors, transformation rules, and human-review policy.

This keeps the scientific question independent of any one model.

### Why now

Until recently, the semantic component presented a circular problem: using a powerful remote model to decide whether data were safe to transmit could expose the same information the gate was intended to protect.

Compact local decision models such as **Laya** change that design space. They can produce typed probabilistic decisions locally. This project will test—not assume—whether that capability is sufficient and sufficiently calibratable for privacy gating.

---

## Role of Claude

Claude API credits will support three functions.

**Frontier semantic comparator.** Claude will receive the same versioned scenario representation as local semantic models and return structured decisions under a fixed rubric. It provides a high-capability reference point; it does not define ground truth.

**Benchmark construction and stress testing.** Claude will help turn public privacy and research-data documentation into candidate scenarios, generate controlled counterfactuals, identify ambiguous cases, and propose difficult examples. Human reviewers will approve benchmark content and labels.

**Systematic robustness experiments.** Repeated Claude inference will allow controlled variation of access purpose, identifiability, sensitivity, wording, execution environment, requested operation, and transformations.

Claude predictions will never automatically become gold labels for the local or statistical models.

---

## Expected outcomes

The research is useful even if the most complex approach does not win.

Possible findings include that structural/statistical predictors are sufficient for most cases; that semantic context adds value only in a defined gray zone; that a compact local model captures enough semantic information for local gating; or that semantic models add too little value and should not be deployed.

Expected outputs include:

- an open, provenance-tracked benchmark of AI data-access scenarios;
- an interpretable statistical model of agent-exposure risk;
- calibrated comparison of local and frontier semantic models;
- selective-prediction and abstention methods for access decisions;
- reproducible open evaluation infrastructure;
- a DataGangeR research prototype if supported by evidence;
- manuscripts on calibrated AI access decisions and local privacy gating.

---

## Proposed 12-month plan

| Period | Milestone |
|---|---|
| Months 1–2 | Finalize decision specification, annotation protocol, and evaluation infrastructure |
| Months 2–5 | Construct and review public/synthetic benchmark; freeze splits |
| Months 4–7 | Fit statistical baseline and evaluate Claude/local semantic models |
| Months 7–9 | Calibration, abstention, counterfactual and robustness experiments |
| Months 9–10 | Incremental-value analysis and transparent evidence fusion |
| Months 10–12 | DataGangeR prototype if justified; manuscript and open benchmark/software release |

---

## Budget

**Requested: CAD $75,000 in Claude API credits over 12 months.**

| Activity | Share | Approx. value |
|---|---:|---:|
| Benchmark construction and controlled augmentation | 20% | $15,000 |
| Frontier semantic-model evaluation | 25% | $18,750 |
| Counterfactual and robustness experiments | 25% | $18,750 |
| Calibration, replication, and sensitivity analyses | 15% | $11,250 |
| Research/software workflow support | 10% | $7,500 |
| Replication contingency | 5% | $3,750 |

Local open models and conventional statistical models do not consume Claude credits. Claude usage is concentrated where a frontier semantic comparator materially strengthens the study.

---

## Safety and privacy

The initial benchmark will use public documentation, public datasets, synthetic examples, and expert-authored scenarios. Confidential research records and personal health information will not be submitted to the Claude API for benchmark construction or model comparison.

Model evidence will remain separate from policy authority. Deterministic safeguards and human review remain authoritative for consequential decisions. Development, calibration, and test sets will be separated, model/rubric versions retained, and privacy-relevant false negatives and disagreement explicitly reported.

DataGangeR's local/no-network workflow will remain the default. The project will not claim that a model score guarantees anonymity, regulatory compliance, or universal safety.

---

## One-sentence framing

> **Can compact semantic decision models and interpretable statistical models provide independent, calibrated evidence for deciding when research data require transformation or human review before exposure to an AI agent?**

## Translational vision

> **A small local model should be able to guard the door to a much larger AI model without requiring sensitive data to leave the trusted environment merely to decide whether they may leave it.**

---

## Relevant links

- DataGangeR: https://github.com/lennon-li/dataganger
- Which: https://github.com/lennon-li/which
- Laya model: https://huggingface.co/convaiinnovations/laya
- Microsoft Presidio: https://github.com/microsoft/presidio
