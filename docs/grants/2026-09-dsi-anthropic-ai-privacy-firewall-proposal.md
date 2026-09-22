# Who Should See the Data?
## Calibrated Statistical and Semantic Gates for Privacy-Preserving AI Access to Research Data

**Target program:** University of Toronto Data Sciences Institute — Claude API Credit Award, Claude Research tier  
**Status:** Draft full proposal  
**Date:** 2026-09-22  
**Requested support:** CAD $75,000 in Claude API credits over 12 months  
**Project type:** Claude Research  
**Primary software:** [DataGangeR](https://github.com/lennon-li/dataganger) and [Which](https://github.com/lennon-li/which)

---

## Executive summary

AI agents can increasingly perform statistical analysis, programming, data cleaning, visualization, and research workflows. Their usefulness creates a practical privacy problem that is still poorly formalized:

> **What information does an AI agent need to see to perform a task, and when should that information first be transformed, restricted, or reviewed by a human?**

Existing privacy controls answer related but narrower questions. They can detect identifiers, measure uniqueness, estimate disclosure risk, synthesize data, or enforce access rules. They do not generally provide a calibrated decision about whether a particular AI agent should see a particular representation of a dataset for a particular purpose.

This project will develop and evaluate an auditable **AI privacy firewall** for research data. The firewall will combine three distinct sources of evidence:

1. **Deterministic privacy safeguards** that identify facts that should not be guessed by a model.
2. **An interpretable statistical risk model** based on measurable properties of the data and proposed use.
3. **A compact local semantic model**, such as Laya, that can interpret natural-language descriptions, data dictionaries, and access requests without sending raw data to an external service.

Claude will be used as a frontier semantic comparator, a controlled research instrument for benchmark construction and robustness experiments, and a downstream example of the class of capable external agents whose access must be mediated.

The central scientific question is:

> **Does semantic information contained in natural-language descriptions of research data and proposed AI use provide incremental, calibrated information about privacy risk beyond conventional statistical and structural predictors?**

A second question is:

> **Can a compact locally deployable semantic decision model recover enough of that contextual information to serve as a practical pre-access firewall on ordinary research hardware?**

The project builds on two pieces of existing work. **DataGangeR** is an open-source R package for privacy-aware synthetic data and human-gated agent workflows. **Which** is a new engine-neutral framework for typed decisions, calibration, abstention, and comparison across models such as Jev and Laya. Together they provide both the domain testbed and the reusable methodological infrastructure needed for this study.

---

# 1. Project rationale

## 1.1 The problem is not simply "private data versus AI"

Research data access decisions are contextual.

The same dataset may be reasonable for one operation and inappropriate for another. For example, an agent may be able to inspect schema and summary statistics without needing row-level values. A locally running agent may present a different exposure boundary from an external API. A synthetic derivative may be suitable for application development while the original data remain restricted. Free-text clinical notes can carry semantic risks that are difficult to capture using uniqueness metrics alone.

A useful access decision therefore depends on at least four components:

- **what the data contain;**
- **what the agent is being asked to do;**
- **where and how the agent operates;**
- **what transformations and safeguards are already in place.**

This is not naturally solved by a single yes/no privacy rule.

## 1.2 Why deterministic rules are necessary but insufficient

Deterministic safeguards are valuable because some privacy facts should not be delegated to an AI model. If a field is known to contain a direct identifier, if a synthetic record exactly reproduces a source record, or if a specific disclosure-control constraint is violated, the system should not ask a language model to reinterpret that fact.

However, rule-based systems are weakest where meaning depends on context. The string "ID" may refer to a participant identifier, a product identifier, or an internal non-person record key. A geographic field may be harmless in one aggregate dataset but highly identifying when combined with age and a rare occupation. A variable description may reveal health or financial sensitivity even when the column name does not.

## 1.3 Why semantic AI alone is also insufficient

Large language models can interpret context but are not automatically calibrated privacy judges. Their predictions can be sensitive to wording, they may express unwarranted certainty, and a remote model may itself create a new exposure surface if detailed data are transmitted for classification.

For privacy-sensitive applications, a semantically capable model should therefore provide **evidence**, not policy authority.

## 1.4 Why compact local models are particularly promising

A central hypothesis of this project is that small typed-decision models can occupy a useful middle layer between hard privacy rules and powerful external AI systems.

Compact open models such as **Laya** can be deployed locally, calibrated or fine-tuned for a narrow task, versioned as a model artifact, and run without continuous access to expensive GPU infrastructure. This makes them attractive for research settings where the privacy control itself should not require sending sensitive material to a remote service.

The proposed architecture treats such a model as a **local AI privacy firewall**: a semantic gate that interprets bounded metadata, data dictionaries, column summaries, and requested agent actions before deciding whether information should be exposed, transformed, or escalated for human review.

The firewall is not a guarantee of anonymity or regulatory compliance. It is a calibrated decision layer designed to reduce unnecessary exposure.

---

# 2. Conceptual architecture

~~~mermaid
flowchart TB
    A["Sensitive research data"] --> B["Local deterministic privacy checks"]
    A --> C["Bounded local summary / data dictionary"]
    B --> D["Structured privacy features"]
    C --> E["Compact local semantic model<br/>(e.g. Laya)"]
    D --> F["Interpretable statistical risk model<br/>(logistic / ordinal / GAM)"]
    E --> G["Calibrated semantic evidence"]
    F --> H["Calibrated statistical evidence"]
    B --> I["Hard blockers / known facts"]
    G --> J["Transparent evidence fusion"]
    H --> J
    I --> J
    J --> K{"Access policy"}
    K -->|Low risk, bounded| L["Agent receives minimum necessary view"]
    K -->|Transform first| M["Redact / synthesize / aggregate"]
    K -->|Uncertain| N["Human review"]
    K -->|High risk| O["Do not expose"]
    M --> L
~~~

**Figure 1. Proposed AI privacy firewall.** Deterministic safeguards, statistical risk modelling, and compact semantic inference are kept separate until the policy layer. A favorable model score cannot override a deterministic hard blocker.

---

# 3. Research questions and hypotheses

## Primary research question

**RQ1.** Does semantic information in natural-language descriptions of research data and proposed AI use provide incremental predictive value for privacy-relevant access decisions beyond conventional statistical and structural predictors?

**Hypothesis 1.** A calibrated semantic model will improve discrimination and selective prediction beyond a structured statistical model alone for cases in which privacy relevance depends on semantic context.

## Secondary research question

**RQ2.** Can a compact, locally deployable semantic model provide useful contextual privacy information with sufficient calibration and efficiency to serve as a practical pre-access firewall?

**Hypothesis 2.** A compact local decision model will recover a meaningful fraction of the semantic signal available to frontier models while being feasible to deploy on ordinary researcher hardware and without external transmission of raw records.

## Additional research questions

**RQ3.** When semantic and statistical models disagree, can calibrated abstention reduce high-risk false negatives without imposing an unacceptable human-review burden?

**RQ4.** Does a transparent hybrid model provide measurable incremental value over either semantic or statistical evidence alone?

**RQ5.** How robust are semantic decisions to paraphrase, irrelevant wording, altered variable names, and controlled changes in the stated access environment?

---

# 4. Research design

~~~mermaid
flowchart LR
    A["Public documentation,<br/>data dictionaries,<br/>synthetic scenarios"] --> B["Expert-reviewed<br/>access benchmark"]
    B --> C["Frozen train split"]
    B --> D["Frozen calibration split"]
    B --> E["Untouched test split"]
    C --> F["Statistical model"]
    C --> G["Compact semantic model"]
    C --> H["Frontier semantic comparator<br/>(Claude)"]
    D --> I["Probability calibration<br/>and abstention thresholds"]
    F --> I
    G --> I
    H --> I
    I --> J["Pre-specified evaluation"]
    E --> J
    J --> K["Incremental-value analysis"]
    K --> L["Transparent hybrid<br/>only if justified"]
    L --> M["DataGangeR validation"]
~~~

**Figure 2. Study design.** The benchmark is split before model development. Calibration and threshold selection are separated from the untouched final test set.

---

# 5. Benchmark construction

## 5.1 Unit of analysis

The study will not require thousands of confidential source datasets.

The primary unit will be a **data-access scenario** containing:

- a natural-language dataset description;
- selected data-dictionary or variable descriptions;
- structured characteristics of the dataset;
- intended research purpose;
- proposed AI-agent operation;
- access environment;
- privacy transformations already applied;
- an expert-reviewed recommended action.

This design permits extensive use of public and synthetic information while directly studying the decision boundary relevant to AI access.

## 5.2 Candidate sources

Cases may be derived from public research-data repository descriptions, public data dictionaries, controlled-access dataset documentation, public data-management and data-sharing plans, funding-agency data governance examples, institutional privacy guidance, public health and clinical dataset descriptions, public/synthetic PII corpora, synthetic counterfactual cases, and deliberately designed hard negatives and adversarial examples.

No confidential research records are required for the initial benchmark.

## 5.3 Proposed target size

The initial benchmark will target approximately **2,000–5,000 curated scenarios**, with a smaller high-quality subset receiving independent double annotation.

The benchmark will intentionally oversample difficult boundaries, including direct versus non-person identifiers; sensitive versus merely technical fields; individual identifiers versus combination risks; free text with and without sensitive content; fine versus coarse geography; fine versus coarse dates; local versus external agent execution; schema-only versus row-level access; and original versus transformed/synthetic data.

## 5.4 Outcome

The primary outcome will not be labelled simply "safe."

A more defensible ordinal action target is:

1. **bounded access acceptable;**
2. **transform, redact, aggregate, or synthesize first;**
3. **human review required;**
4. **direct exposure inappropriate under the stated conditions.**

## 5.5 Annotation

Each case will include case identifier, source/provenance, natural-language scenario, structured feature representation, expert action label, annotator certainty, brief rationale, difficulty/adversarial flag, and split assignment.

For a subset, two independent reviewers will label the case before reconciliation. Human disagreement will be reported rather than hidden.

---

# 6. Comparator 1 — deterministic baseline

The first baseline is the existing deterministic privacy logic in DataGangeR.

Relevant components already implemented include direct identifier detection, structured/high-cardinality identifier detection, sensitive-field heuristics, free-text detection, date and geographic handling, exact source-to-synthetic record matching, k-anonymity-related assessment and enforcement, rare-category and disclosure diagnostics, role-aware privacy checks, and human review gates.

These are not treated as obsolete once models are introduced. They remain an explicit baseline and, where appropriate, a safety floor.

---

# 7. Comparator 2 — interpretable statistical model

A conventional statistical model will be developed as a first-class comparator, not merely as a weak baseline.

Candidate predictors include record count, number of variables, direct/quasi/sensitive counts, maximum uniqueness ratio, minimum equivalence-class size, rare-category prevalence, free-text presence, temporal precision, geographic precision, combination uniqueness, missingness summaries, entropy/cardinality summaries, original versus transformed status, requested operation, local versus external access boundary, and deterministic privacy flags.

Initial models will prioritize interpretability:

1. penalized logistic or ordinal regression;
2. generalized additive models;
3. more flexible machine-learning comparators only if justified.

A representative formulation is:

[
operatorname{logit} P(Y ge k)
=
alpha_k +
f_1(	ext{uniqueness}) +
f_2(	ext{record count}) +
eta_1 I(	ext{free text}) +
eta_2 I(	ext{sensitive}) +
eta_3 I(	ext{external agent}) + cdots
]

This model asks how far carefully engineered structural evidence can take us without semantic AI.

---

# 8. Comparator 3 — semantic decision models

## 8.1 Claude

Claude will serve as a frontier semantic comparator. It will receive the same versioned natural-language representation as other semantic models and return structured decisions under a fixed rubric.

Claude will not define ground truth.

Its role is to establish how much signal a capable frontier model can extract from the semantic representation and to provide a high-capability comparison point for smaller local models.

## 8.2 Laya and compact local decision models

Laya is particularly relevant because it represents the deployment direction of interest: a compact, open, locally executable decision model.

The study will evaluate stock Laya, calibrated stock Laya, domain-adapted Laya only if the calibrated stock model adds residual value, and a frontier Claude comparator on the same cases.

The final goal is not to prove that one named model is universally best. It is to determine whether the **compact local decision-model class** is useful as a privacy boundary.

---

# 9. The local AI firewall hypothesis

~~~mermaid
flowchart LR
    A["Raw / sensitive data"] --> B["Local AI privacy firewall"]
    B --> C{"Decision"}
    C -->|Minimum necessary view| D["Powerful external or local AI agent"]
    C -->|Transform| E["DataGangeR synthetic / redacted view"]
    C -->|Uncertain| F["Human reviewer"]
    C -->|Block| G["No exposure"]
    E --> D
~~~

**Figure 3. Local firewall deployment concept.** The compact model operates inside the trusted boundary. The potentially more capable external agent receives only the representation authorized by the local gate.

This architecture has several potential advantages: sensitive inference can stay local; the semantic model can be task-specifically calibrated or fine-tuned; a model checkpoint and calibration artifact can be versioned and audited; deployment does not depend on continuous cloud access; inference can be feasible without dedicated high-end GPU infrastructure; and the downstream frontier model is separated from the original data by an explicit decision boundary.

The project will measure, rather than assume, whether these advantages can be obtained without unacceptable loss of predictive performance.

---

# 10. Model comparison and incremental value

| Model | Deterministic | Statistical | Semantic | Purpose |
|---|---:|---:|---:|---|
| A | Yes | No | No | Existing baseline |
| B | No | Yes | No | Statistical model alone |
| C | No | No | Laya | Local semantic model |
| D | No | No | Claude | Frontier semantic comparator |
| E | Yes | Yes | No | Rules + statistics |
| F | Yes | No | Laya | Rules + local semantics |
| G | Yes | Yes | Laya | Candidate local firewall |
| H | Yes | Yes | Claude | Upper semantic comparator |

The hybrid is **not** assumed to win. It will be retained only if it materially improves pre-specified metrics over simpler alternatives on the untouched test set.

---

# 11. Evaluation

Overall accuracy will not be the primary measure.

## Primary metrics

- false-negative rate among high-risk cases;
- Brier score or other proper probabilistic loss;
- calibration;
- selective risk at pre-specified coverage;
- coverage at pre-specified abstention thresholds.

## Secondary metrics

- sensitivity and specificity;
- balanced accuracy;
- ordinal/log loss;
- expected calibration error;
- human-review burden;
- inter-rater agreement;
- incremental predictive value;
- performance by dataset domain and access type.

A particularly relevant operational quantity is:

> **Among cases for which the system chooses not to defer to a human, how often is its decision correct?**

Risk-coverage curves will therefore be central to evaluation. A privacy gate should be allowed to say "uncertain."

---

# 12. Robustness experiments

Semantic models will be evaluated under controlled perturbations, including paraphrasing the same access request; renaming variables while preserving meaning; changing irrelevant wording; altering agent location from local to external; changing row-level access to schema-only access; changing geographic or temporal precision; adding or removing free text; changing original data to synthetic data; and adding combinations of individually innocuous quasi-identifiers.

Claude API credits make systematic repeated experiments at this scale feasible.

---

# 13. Existing work and investigator preparation

## 13.1 DataGangeR

I developed **DataGangeR**, an open-source R package for creating reviewable synthetic stand-ins for research data so coding agents, collaborators, and application developers can work without unnecessary access to original records.

DataGangeR is available through CRAN and implements a human-gated privacy workflow rather than an automatic anonymization claim.

Existing work includes column-role and disclosure classification; direct and structured identifier detection; free-text detection; sensitive-field handling; date and postal/geographic handling; exact synthetic-to-original record detection; k-anonymity-related controls; disclosure diagnostics using synthpop; validation against sdcMicro; propensity-based synthetic-data utility diagnostics; reusable frozen synthesis generators; bounded generation policies; approval/revocation lifecycle; audit receipts; local/no-network test gates; and reproducible agent-ready export bundles.

This work supplies the privacy domain, deterministic comparators, measurable predictors, and eventual implementation environment for the proposed project.

## 13.2 Why DataGangeR led to this proposal

While developing DataGangeR, an unresolved boundary repeatedly emerged.

We can identify direct identifiers. We can quantify uniqueness. We can synthesize data and assess exact reproduction. We can apply disclosure controls. But these mechanisms do not directly answer:

> **What representation of the data, if any, should this AI agent be allowed to see for this specific task?**

That question is partly statistical and partly semantic.

The proposal is therefore a direct methodological extension of an already encountered research problem rather than an attempt to add AI to an unrelated software package.

## 13.3 Which

I have begun development of **Which**, an engine-neutral framework for calibrated typed decisions.

Its core architecture separates decision specification, decision engine, normalized probabilities, calibration/abstention, and application policy.

Current target engines include Jev and Laya.

This separation is important scientifically: gold labels and evaluation criteria belong to the decision problem, not to one vendor or model.

## 13.4 Prospective Jev work

Before creating Which, I built a Jev-backed model-delegation classifier into my agent workflow. That work already separates learned task classification from deterministic routing policy, supports confidence-aware abstention, and records prospective blind labels before seeing the model prediction.

The existing Jev implementation will be used as the live harness while Which is developed. Real Which development tasks will therefore simultaneously generate prospective calibration data for the generic decision framework.

## 13.5 Statistical methodology perspective

My work in biostatistics and prediction emphasizes out-of-sample validation, calibration, reproducibility, and separation of model development from held-out evaluation.

That perspective motivates a central principle:

> **A semantically persuasive AI output should be treated as a statistical prediction to be calibrated and validated, not as ground truth because it sounds reasonable.**

---

# 14. Which versus DataGangeR

## Which owns

- generic typed-decision schemas;
- Jev/Laya/future engine adapters;
- normalized probabilities and labels;
- calibration tooling;
- abstention and threshold utilities;
- train/calibration/test split support;
- benchmark formats;
- evaluation metrics;
- engine comparison;
- model/spec/calibration manifests.

## DataGangeR owns

- privacy threat model;
- deterministic privacy and disclosure checks;
- bounded column/dataset summary construction;
- privacy annotation taxonomy;
- definition of agent_exposure_risk;
- statistical privacy model;
- DataGangeR benchmark case construction;
- reconciliation of deterministic/statistical/semantic evidence;
- transformation/synthesis policy;
- human review;
- eventual ai_safe() interface.

**Which never decides what "safe data" means. DataGangeR never reimplements generic decision-engine infrastructure.**

---

# 15. Work packages

## WP1 — Decision infrastructure and prospective validation

Complete Which, migrate the working Jev decision path, add Laya parity, establish calibration/abstention/benchmark tooling, and validate prospectively using real model-delegation decisions.

## WP2 — Privacy benchmark

Formalize the agent-access outcome, construct public/synthetic scenarios, establish annotation guidance, double-annotate a high-value subset, and freeze development/calibration/test splits.

## WP3 — Statistical comparator

Engineer interpretable privacy features, fit conventional statistical models, evaluate calibration and selective risk, and establish the structured-information baseline.

## WP4 — Semantic models

Evaluate Claude under a fixed rubric, evaluate stock/calibrated Laya, fine-tune Laya only if justified, and conduct robustness experiments.

## WP5 — Evidence fusion and DataGangeR prototype

Test incremental semantic value, evaluate transparent fusion, compare risk/coverage against simpler alternatives, and integrate a research-only optional gate into DataGangeR if evidence supports it.

---

# 16. Gated roadmap

~~~mermaid
flowchart TB
    G1["Gate 1<br/>Which + Hermes/Jev<br/>prospective testing"] --> G2["Gate 2<br/>Jev/Laya parity<br/>same gold cases"]
    G2 --> G3["Gate 3<br/>DataGangeR semantic benchmark"]
    G3 --> Q1{"Does calibrated Laya add<br/>value beyond deterministic rules?"}
    Q1 -->|No| S1["Stop semantic adaptation<br/>retain simpler system"]
    Q1 -->|Yes| G4["Gate 4<br/>Optional Laya fine-tuning"]
    G3 --> G5["Gate 5<br/>Define and fit interpretable<br/>statistical exposure-risk model"]
    G4 --> Q2{"Do both semantic and statistical<br/>models independently add value?"}
    G5 --> Q2
    Q2 -->|No| S2["Use best simpler model"]
    Q2 -->|Yes| G6["Gate 6<br/>Transparent ensemble"]
    G6 --> G7["Gate 7<br/>Prospective DataGangeR validation"]
~~~

**Figure 4. Gated research roadmap.** More complex modelling is permitted only after simpler components demonstrate independent value.

---

# 17. Timeline

~~~mermaid
gantt
    title 12-month research plan
    dateFormat  YYYY-MM-DD
    axisFormat  %b %Y

    section Which
    Jev migration and prospective testing :a1, 2026-11-01, 60d
    Laya parity and calibration            :a2, after a1, 45d

    section Benchmark
    Outcome definition and annotation guide :b1, 2026-11-15, 45d
    Public/synthetic case construction       :b2, after b1, 90d
    Double annotation and split freeze       :b3, after b2, 45d

    section Models
    Statistical comparator                 :c1, after b3, 60d
    Claude and Laya semantic evaluation    :c2, after b3, 60d
    Robustness experiments                 :c3, after c2, 45d

    section Integration
    Incremental-value and ensemble analysis :d1, after c3, 45d
    DataGangeR research prototype           :d2, after d1, 45d
    Manuscript and open release             :d3, after d2, 45d
~~~

---

# 18. Purpose of Claude API credits
## Application-field draft — maximum 500 words

Claude API credits will support three complementary research functions.

**First, Claude will serve as a frontier semantic-model comparator.** Each benchmark case will contain a versioned natural-language description of a dataset, intended use, proposed AI-agent operation, and access conditions. Claude will return structured decisions under a fixed rubric. Its predictions and uncertainty behavior will be compared with an interpretable statistical model and with compact open decision models such as Laya operating on the same cases. Claude will not define ground truth.

**Second, Claude will support benchmark construction and stress testing.** We will use Claude to help transform public privacy, research-data, and access documentation into candidate scenarios; generate controlled counterfactual variations; identify ambiguous wording; and propose difficult cases for expert review. Claude-generated cases and labels will remain candidate material. Human reviewers will approve benchmark content and gold labels, and provenance will be retained.

**Third, Claude will support systematic robustness experiments.** We will vary access purpose, identifiability, sensitivity, wording, agent location, requested operation, and transformations while holding other factors fixed. These repeated experiments will quantify whether semantic decisions respond to relevant privacy evidence or to superficial phrasing.

The project specifically contrasts frontier cloud models with compact local decision models. Claude will therefore provide a high-capability semantic reference point while we test whether smaller models can recover sufficient contextual information to operate locally as a privacy firewall. This distinction is central to the proposed impact: a production privacy gate should not necessarily require sending detailed metadata or records to the same external model whose access it is supposed to govern.

All experiments will record model, rubric, and dataset versions. Training, calibration, and final held-out evaluation will remain separated. Claude predictions will never be used automatically as gold labels for Laya or the statistical model.

---

# 19. Budget justification
## Application-field draft — maximum 500 words

We request **CAD $75,000 in Claude API credits for 12 months**.

The project requires repeated structured inference over thousands of benchmark and robustness scenarios rather than one-off interactive use. The requested amount is intended to permit sufficiently broad replication across model versions, prompt/rubric variants, and controlled scenario perturbations while preserving an untouched final evaluation set.

| Activity | Share | Approx. value |
|---|---:|---:|
| Benchmark construction and controlled augmentation | 20% | $15,000 |
| Frontier semantic-model evaluation | 25% | $18,750 |
| Counterfactual and robustness experiments | 25% | $18,750 |
| Calibration, replication, and sensitivity analyses | 15% | $11,250 |
| Research/software workflow support | 10% | $7,500 |
| Replication contingency | 5% | $3,750 |

The largest component is systematic experimental inference: thousands of scenarios may each be evaluated under multiple access conditions, semantic formulations, model configurations, and replication runs. This is necessary to estimate calibration, selective risk, wording sensitivity, and domain-specific failure modes rather than reporting a single accuracy estimate.

Local open models and conventional statistical models do not consume Claude credits; this is deliberate. Claude usage is concentrated where a frontier semantic comparator materially improves the scientific design.

---

# 20. AI safety
## Application-field draft — maximum 500 words

Safety and privacy are the central research questions of this project rather than ancillary considerations.

The initial benchmark will be constructed from public documentation, public datasets, synthetic examples, and expert-authored scenarios. Confidential research records, personal health information, credentials, and other restricted source data will not be submitted to the Claude API for benchmark construction or model comparison.

We will maintain a strict separation between **model evidence and policy authority**. Claude and other semantic models will return predictions under a versioned rubric; they will not independently authorize access to research data. Deterministic privacy safeguards and human review will remain authoritative for consequential decisions.

Claude-generated scenarios or proposed labels will not automatically become ground truth. Benchmark labels will be human reviewed, provenance will be recorded, and development/calibration/test partitions will be frozen before final model comparison. We will explicitly report semantic-model disagreement, calibration, abstention, wording sensitivity, and privacy-relevant false negatives.

DataGangeR's existing default no-network workflow will be preserved. Future semantic integration will remain optional, with local inference preferred for sensitive applications. Raw records will not be transmitted to remote decision models. Any future model-assisted production workflow will operate on bounded and versioned summaries whose disclosure properties must be evaluated separately.

The proposed local-firewall architecture is designed specifically to reduce unnecessary exposure: deterministic checks, an interpretable statistical model, and a compact local semantic model operate inside the trusted boundary before a larger external agent receives a minimum-necessary representation.

All public software, benchmark-generation procedures, model specifications, calibration artifacts, and evaluation code will be version controlled to support reproducibility and independent audit. We will avoid claims that any model score guarantees anonymity, regulatory compliance, or universal safety.

---

# 21. Abstract
## Application-field draft — maximum 200 words

AI agents can increasingly perform statistical analysis, programming, and research workflows, but their usefulness creates a practical privacy question that remains poorly formalized: **when should an AI agent be allowed to see research data, and when should those data first be transformed, restricted, or reviewed by a human?**

We propose to develop and evaluate calibrated decision methods for AI data access. Rather than treating "safe" as a binary model-generated judgment, we will compare three complementary approaches: deterministic privacy safeguards; an interpretable statistical risk model based on measurable characteristics of a dataset and proposed use; and semantic decision models that interpret natural-language data descriptions and access requests.

A distinctive focus is whether compact open models such as Laya can operate locally as an **AI privacy firewall**, providing contextual semantic assessment without transmitting raw records to external services. Claude will provide a frontier semantic comparator and support large-scale controlled robustness experiments.

We will create an expert-reviewed benchmark from public documentation, data dictionaries, and synthetic scenarios, with held-out evaluation of calibration, privacy-relevant false negatives, abstention, and incremental predictive value. The project builds on our existing DataGangeR privacy framework and the new engine-neutral Which decision framework.

---

# 22. Keywords

**privacy-preserving AI; statistical calibration; selective prediction; data access; AI agents; semantic decision models; local AI; synthetic data; disclosure risk; biostatistics; interpretable models; responsible AI**

---

# 23. Expected contributions

## Methodological

- a formalized agent-exposure decision problem;
- comparison of structural/statistical versus semantic evidence;
- calibration and selective-prediction methodology for AI access gates;
- incremental-value analysis for semantic decision models;
- transparent ensemble methodology if justified.

## Data

- an open, provenance-tracked benchmark of AI data-access scenarios;
- expert annotation guidance;
- controlled robustness and adversarial subsets.

## Software

- engine-neutral decision/calibration infrastructure in Which;
- Jev and Laya adapters;
- statistical and semantic evaluation tooling;
- an optional research prototype in DataGangeR;
- reproducible model/spec/calibration manifests.

## Translational

- a practical reference architecture for local AI privacy firewalls;
- guidance on when compact local models are sufficient;
- evidence for when human review remains necessary;
- a path for institutions to reduce unnecessary disclosure while retaining AI utility.

---

# 24. Expected publications and outputs

Potential manuscripts include:

1. **Semantic versus statistical evidence for AI data-access decisions: a calibrated benchmark study.**
2. **Selective prediction and abstention for privacy-preserving AI access gates.**
3. **Compact local decision models as privacy firewalls for research AI workflows.**
4. **DataGangeR + Which: an open reference architecture for privacy-aware agent access.**

Additional outputs include conference/poster presentations, the open benchmark, software releases, and documentation suitable for reuse by other research groups.

---

# 25. Risks and mitigation

| Risk | Mitigation |
|---|---|
| Expert labels are subjective | Double annotation, certainty ratings, disagreement reporting |
| Public cases are too easy | Hard negatives, counterfactuals, adversarial combinations |
| Semantic model appears accurate but is poorly calibrated | Proper scoring rules, reliability analysis, held-out calibration |
| Laya adds no value | Stop at the gate; retain simpler statistical/deterministic system |
| Statistical model misses semantic context | Explicit incremental semantic comparison |
| Ensemble adds complexity without benefit | Retain only if it beats simpler components on pre-specified metrics |
| Remote inference creates privacy exposure | Public/synthetic research phase; local model for eventual sensitive deployment |
| Model/version drift | Versioned manifests, frozen test sets, regression evaluation |
| "Safe" is overinterpreted | Use action/risk terminology, explicit threat model, no compliance/anonymity claims |

---

# 26. Why this project is timely

AI agents are moving from text generation toward direct participation in scientific workflows. Data access is therefore becoming an active decision rather than a static permission.

At the same time, capable semantic models and compact local decision models now make it possible to ask whether contextual privacy reasoning can be operationalized without placing all decision authority in a large external model.

The methodological opportunity is to bring conventional statistical principles—explicit outcomes, calibration, held-out validation, uncertainty, proper scoring, and incremental-value analysis—to a problem that is often handled through informal prompting.

The practical opportunity is to create a local decision boundary that lets researchers benefit from increasingly capable AI while minimizing unnecessary exposure of research participants' information.

---

# 27. Program alignment

The University of Toronto Data Sciences Institute Claude API Credit Award provides up to CAD $100,000 in Claude API credits for research projects over a maximum of 12 months. The proposed project uses Claude as a research instrument and frontier comparator while directly addressing responsible AI deployment, privacy, statistical methodology, reproducibility, and open research software.

Anthropic's Canadian research initiative emphasizes beneficial and responsible applications of AI, including trust and safety and health/science research. This project connects those themes through a concrete methodological problem: determining the minimum information an AI system should receive to contribute productively to scientific work.

---

# 28. References and relevant resources

- University of Toronto Data Sciences Institute. **Claude API Credit Award.**  
  https://datasciences.utoronto.ca/claude-api-credit/

- Anthropic. **Anthropic commits $10 million to Canadian AI research.** 2026.  
  https://www.anthropic.com/news/canadian-ai-research

- DataGangeR source repository.  
  https://github.com/lennon-li/dataganger

- Which source repository.  
  https://github.com/lennon-li/which

- Microsoft Presidio.  
  https://github.com/microsoft/presidio

- Laya.  
  https://github.com/NandhaKishorM/laya

- RouteLLM.  
  https://github.com/lm-sys/RouteLLM

---

# Appendix A. Research logic in one figure

~~~mermaid
flowchart TB
    P["Problem:<br/>Should this AI agent see this data?"] --> R["Deterministic facts"]
    P --> S["Structured measurable risk"]
    P --> T["Semantic/contextual meaning"]
    R --> R1["DataGangeR rules"]
    S --> S1["Interpretable statistical model"]
    T --> T1["Local Laya"]
    T --> T2["Claude comparator"]
    R1 --> E["Calibrated evidence"]
    S1 --> E
    T1 --> E
    T2 --> X["Research benchmark only"]
    X --> E
    E --> A{"Explicit access policy"}
    A --> A1["Allow minimum necessary view"]
    A --> A2["Transform / synthesize"]
    A --> A3["Human review"]
    A --> A4["Block"]
~~~

# Appendix B. One-sentence project framing

> **Can compact semantic decision models and interpretable statistical models provide independent, calibrated evidence for deciding when research data require transformation or human review before exposure to an AI agent?**

# Appendix C. One-sentence translational vision

> **A small local model should be able to guard the door to a much larger AI model without requiring the sensitive data to leave the trusted environment merely to decide whether they may leave it.**
