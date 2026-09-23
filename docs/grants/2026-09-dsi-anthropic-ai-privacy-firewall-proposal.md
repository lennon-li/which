# Measure Before You Share
## Calibration, Uncertainty, and Dual-Gate Safety for AI Access to Medical and Public-Health Data

**Target program:** University of Toronto Data Sciences Institute — Claude API Credit Award, Claude Research tier  
**Status:** Faculty-review draft  
**Date:** 2026-09-22  
**Requested support:** CAD $75,000 in Claude API credits over 12 months  
**Project type:** Claude Research  
**Primary software:** [DataGangeR](https://github.com/lennon-li/dataganger) and [Which](https://github.com/lennon-li/which)

---

## Executive summary

AI agents can increasingly perform statistical analysis, programming, data cleaning, visualization, and research workflows. Researchers are therefore beginning to use cloud AI not only for writing but for **prototyping analyses and applications against data**. In medical and public-health research, those data may include **personal information (PI), personal health information (PHI), sensitive clinical or sociodemographic attributes, free text, dates, geography, or identifying combinations of variables**. That creates a decision point before the first prompt or tool call: should the agent see the original data, a de-identified extract, synthetic data, summaries, or nothing at all?

> **Is the representation we are about to share appropriate for this AI service and this task, and what evidence should justify that decision?**

This question matters because “synthetic” or “de-identified” does not automatically mean safe for cloud exposure. NIST notes that non-differentially-private synthetic data generally provide only informal privacy guarantees and may remain vulnerable to privacy attacks, while empirical work has shown that synthetic data can have unpredictable privacy–utility trade-offs (NIST SP 800-226, 2025; Stadler, Oprisanu & Troncoso, 2022). The problem is therefore not simply whether a dataset has been transformed, but whether a particular representation is appropriate for a particular AI task and access boundary.

Existing privacy controls answer related but narrower questions. They can detect identifiers, measure uniqueness, estimate disclosure risk, synthesize data, or enforce access rules. They do not generally provide a calibrated decision about whether a particular AI agent should see a particular representation of a dataset for a particular purpose.

This project will develop and evaluate an auditable **AI privacy firewall** for research data. The firewall will combine three distinct sources of evidence:

1. **Deterministic privacy safeguards** that identify facts that should not be guessed by a model.
2. **An interpretable statistical access-decision model** based on measurable properties of the data and proposed use.
3. **A compact local semantic model**, such as Laya, that can interpret natural-language descriptions, data dictionaries, and access requests without sending raw data to an external service.

Claude will be used as a frontier semantic comparator, a controlled research instrument for benchmark construction and robustness experiments, and a downstream example of the class of capable external agents whose access must be mediated.

The central scientific question is:

> **Does semantic information contained in natural-language descriptions of research data and proposed AI use provide incremental, calibrated information about privacy risk beyond conventional statistical and structural predictors?**

A second question is:

> **Can a compact locally deployable semantic decision model recover enough of that contextual information to serve as a practical pre-access firewall on ordinary research hardware?**

The project builds on two pieces of existing work. **DataGangeR** is an open-source R package for privacy-aware synthetic data and human-gated agent workflows. **Which** is a new engine-neutral framework for typed decisions, calibration, abstention, and comparison across models such as Jev and Laya. Together they provide both the domain testbed and the reusable methodological infrastructure needed for this study.

The project will deliver an **open-source, policy-controlled orchestration layer** that governs how deterministic privacy checks, statistical models, compact local models, frontier models, and human reviewers work together. The orchestrator will enforce minimum-necessary context, structured outputs, explicit escalation, and auditable human gating rather than allowing an unconstrained agent team to decide its own access.

It will also deliver a reusable **human-governed evidence-collection and model-improvement framework**. The framework will prospectively collect labelled decisions, preserve human adjudication, maintain versioned train/calibration/test splits, support periodic Laya tuning when justified, calibrate/evaluate hosted models such as Jev, and gate releases through regression testing. Claude can support candidate-case generation, provisional labelling, hard-case discovery, experiment design, error analysis, and independent evaluation without being treated as ground truth.

Privacy-aware AI access is the primary 12-month application. A central reusable output will be a **classifier-evaluation framework** in Which that standardizes calibration, uncertainty, selective prediction, dual-gate error analysis, model/version drift, and regression release criteria across statistical and AI decision models. The underlying infrastructure will be designed for later reuse in other public-health tasks, such as aberration triage and escalation, but those secondary applications are not required deliverables of this project.

A supervised cohort of approximately **3–5 Biostatistics/data-science trainees** will participate in benchmark construction, blinded annotation/review, classifier evaluation, calibration/uncertainty analysis, application building, robustness experiments, replication, and release validation. The educational objective is to train statisticians to use AI efficiently while preserving statistical validation, reproducibility, and human oversight. If organizational approvals and timing permit, we will conduct a **small public-health implementation pilot**, potentially with Public Health Ontario (PHO), using approved/public/synthetic representations. The pilot is an external-validity and knowledge-translation activity and is not required for completion of the primary scientific aims.

---

# 1. Project rationale

## 1.1 AI prototyping creates a new data-release decision

A growing practical use of AI in research is **rapid prototyping**: asking an agent to write analysis code, inspect data structures, debug pipelines, generate visualizations, or build a Shiny/web application. These tasks often become more effective when the agent can inspect realistic examples.

That creates a new kind of release decision. Traditional governance asks whether data may be released to another person, repository, or environment. Agentic AI makes the decision **interactive and repeated**: the system may request a schema, then sample rows, then a distribution, then free text, accumulating context over multiple turns or tool calls.

The question is therefore not simply “may AI see this dataset?” It is:

> **What is the minimum representation this AI needs for this task, and is that representation acceptable to expose across this access boundary?**

Possible representations include schema only, aggregate summaries, bounded examples, transformed/de-identified data, synthetic data, or original row-level data.

## 1.2 Synthetic data can reduce exposure, but does not establish safety

Synthetic data are especially attractive for AI prototyping because they can preserve enough structure to build and test code without routinely exposing original medical or public-health records containing PI/PHI. This is a central motivation for DataGangeR.

However, synthetic data are not automatically anonymous or safe for unrestricted cloud use. NIST SP 800-226 notes that synthetic-data methods without differential privacy generally offer informal rather than robust privacy guarantees and may remain susceptible to privacy attacks. Stadler, Oprisanu and Troncoso (USENIX Security 2022) empirically demonstrated that synthetic data can retain privacy-relevant signals and that the privacy–utility trade-off may be difficult to predict.

In practice, risk can also arise from rare combinations, free text, high-fidelity relationships, or source-like records. The appropriate decision therefore depends not only on whether the data are synthetic, but on **what was preserved, what the AI is being asked to do, where the model runs, and what safeguards are in place**.

Deterministic safeguards remain essential because some facts should not be delegated to a classifier. If a field contains a known direct identifier, a synthetic record exactly reproduces a source record, or a predefined disclosure-control constraint is violated, a favorable semantic-model score should not override that evidence.

## 1.3 Why semantic AI alone is also insufficient

Large language models can interpret context but are not automatically calibrated privacy judges. Their predictions can be sensitive to wording, they may express unwarranted certainty, and a remote model may itself create a new exposure surface if detailed data are transmitted for classification.

For privacy-sensitive applications, a semantically capable model should therefore provide **evidence**, not policy authority.

## 1.4 Why compact decision models are technically interesting

A central hypothesis of this project is that typed decision models can occupy a useful middle layer between hard privacy rules and powerful generative AI systems.

Traditional generative LLMs are autoregressive: they repeatedly predict the next token and produce an open-ended sequence that must then be interpreted, parsed, or constrained for software use. **Jev** is architecturally different at the interface and training objective: TypeSafe describes it as a non-generative System One model with a parallel sampler and Reinforcement Learning for Calibrated Decisions (RLCD), returning typed choices, scores, or binary probabilities instead of prose. Its internal weights and detailed model architecture are not public, so we will evaluate the observable decision interface rather than assume vendor claims about internals.

**Laya** provides an open, inspectable implementation of the same broad decision-model idea. Its published English checkpoint uses a bidirectional ModernBERT-large encoder plus a small decision head; candidate options are scored directly and normalized into probabilities in a single forward pass. Unlike a conventional task-specific classifier with a permanently fixed label set, its answer options are supplied at inference time. Unlike a generative LLM, it does not need to produce and then re-parse a natural-language answer. Laya's open weights also make local deployment and domain-specific adaptation experimentally testable.

These systems therefore combine features of semantic language models and classifiers: they can interpret unstructured context, while producing a finite, machine-readable probability distribution. That distinction matters statistically. A fixed answer space reduces interpretation variability, and numerical probabilities can be calibrated, scored, thresholded, compared, and audited. The numbers are not assumed to be correct merely because they are numeric; **their calibration is itself a primary object of study**.

The proposed architecture treats a compact local model as a **local AI privacy firewall**: a semantic gate that interprets bounded metadata, data dictionaries, column summaries, and requested agent actions before deciding whether information should be exposed, transformed, or escalated for human review.

The firewall is not a guarantee of anonymity or regulatory compliance. It is a calibrated decision layer designed to reduce unnecessary exposure.

## 1.5 Significance beyond the privacy use case

We view decision-native models as an **emerging development direction**, not yet a settled industry standard. The appearance of a hosted decision model (Jev), an open local implementation (Laya), and early framework integrations suggests growing interest in separating fast, bounded decisions from expensive open-ended generation. The attraction is practical: specialized decision models can be smaller, cheaper to invoke, easier to self-host when open weights are available, and easier to connect safely to ordinary software control flow.

They may also be easier for people to evaluate. Free-form language can be persuasive while remaining difficult to score reproducibly; typed decisions force the model into a standardized answer space and expose quantitative uncertainty that statisticians can test. This creates a need for two pieces of infrastructure that are currently immature: **(1) reproducible tools to train or adapt decision models for domain tasks, and (2) statistical tools to evaluate calibration, uncertainty, failure dependence, abstention, drift, and consequence-weighted error.**

Privacy-aware medical/public-health data access is the primary scientific application and validation testbed in this grant. We do **not** propose to solve every decision-model use case. The broader significance is that the training and evaluation framework developed here can remain useful if decision-native models become a common component of future AI systems.

## 1.6 Motivating workflow

A biostatistics trainee is building a prototype application from medical or public-health data with a cloud coding agent. The agent can work from variable names alone, but development is faster if it can see realistic distributions, edge cases, and example records. The researcher generates a synthetic dataset and is tempted to upload it.

The proposed system asks a different question from a PII detector:

1. Are there deterministic blockers such as direct identifiers, free text, exact reproduction, or high-risk combinations?
2. What does the structured statistical evidence imply about access risk?
3. Does the semantic description of the dataset and intended task add information?
4. How uncertain are those predictions, and do independent gates agree?
5. Can the task be completed with a less revealing representation?
6. If uncertainty or disagreement remains, should a human reviewer decide?

The output is not a declaration that PI/PHI or a dataset is “safe,” nor a determination of legal compliance. It is an auditable recommendation to **allow a minimum necessary view, transform first, request human review, or do not expose**.

---

# 2. Conceptual architecture

~~~mermaid
flowchart TB
    A["Sensitive research data"] --> B["Local deterministic privacy checks"]
    A --> C["Bounded local summary / data dictionary"]
    B --> D["Structured privacy features"]
    C --> E["Compact local semantic model<br/>(e.g. Laya)"]
    D --> F["Interpretable statistical access-decision model<br/>(multinomial / one-vs-rest / GAM)"]
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

**Figure 1. Proposed AI privacy firewall.** Deterministic safeguards, statistical access-decision modelling, and compact semantic inference are kept separate until the policy layer. A favorable model score cannot override a deterministic hard blocker.

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

**RQ6.** Can calibrated abstention and a dual-gate authorization strategy reduce inappropriate authorization relative to either classifier alone while keeping human-review burden acceptable?

**Hypothesis 3.** Gates with intentionally diversified evidence and error mechanisms will have lower joint inappropriate-authorization rates than either gate alone, although at the cost of reduced automatic coverage.

**RQ7.** Do severity-aware measures of potential disclosure harm change model or threshold choices relative to unweighted error rates?

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

## 5.2 Candidate sources and data partnerships

The benchmark is designed so that the primary study **does not depend on access to confidential institutional records**.

### Tier 1 — public and immediately available sources

Candidate scenarios will be constructed from:

- Tri-Agency research-data-management policies, data-management-plan requirements, and publicly posted institutional RDM strategies;
- public research-data repository descriptions and data dictionaries;
- the public ICES Data Dictionary and other health-data documentation;
- Public Health Ontario public data products, data-access documentation, and published request criteria;
- public clinical/public-health dataset documentation;
- public/synthetic PII corpora;
- synthetic counterfactual and adversarial scenarios created from these materials.

These sources provide realistic variation in sensitivity, identifiability, access purpose, and governance without requiring restricted participant records.

### Tier 2 — partner-derived decision cases, if approved

We will seek collaboration with research funders and organizations that routinely make privacy/data-access decisions—potentially including DSI, Tri-Agency programs, ICES, DLSPH units, PHO, or comparable partners. The useful research object is **not their confidential source data**, but the decision process: de-identified or abstracted historical scenarios, decision criteria, privacy-review questions, data-management-plan examples, or prospective expert adjudication.

No organization is assumed to participate, and no confidential grant, privacy, or project-review material will be used without explicit authorization. Partner-derived cases will supplement rather than enable the primary benchmark.

### Tier 3 — implementation/pilot cases

If approvals permit, a partner pilot will test the released framework on approved/public/synthetic or otherwise authorized representations. This phase evaluates workflow fit and external validity rather than supplying the primary training set.

## 5.3 Proposed target size

The project will generate approximately **2,000–5,000 candidate scenarios** from public documentation, synthetic cases, and controlled counterfactuals. From these, the core benchmark will contain **at least 600 independent, human-adjudicated scenario families**, split at the family/source level into 360 development, 120 calibration, and 120 locked test families (60/20/20). At least 40 locked-test families will be pre-designated high risk. A family includes all paraphrases, counterfactuals, and controlled variants of one source case; its variants stay in one split. The larger candidate pool supports development and stress tests but is not counted as 2,000–5,000 independent gold-standard observations.

The benchmark will intentionally oversample difficult boundaries, including direct versus non-person identifiers; sensitive versus merely technical fields; individual identifiers versus combination risks; free text with and without sensitive content; fine versus coarse geography; fine versus coarse dates; local versus external agent execution; schema-only versus row-level access; and original versus transformed/synthetic data.

## 5.4 Outcome

The primary outcome will not be labelled simply "safe."

The primary reference target will be a **multiclass recommended action**, rather than assuming these actions lie on a single ordinal severity scale:

1. **bounded access acceptable;**
2. **transform, redact, aggregate, or synthesize first;**
3. **human review required;**
4. **direct exposure inappropriate under the stated conditions.**

For safety-oriented evaluation, we will also pre-specify derived binary endpoints, including **inappropriate authorization**: a model permits direct/bounded access when the reference action requires transformation, human review, or no direct exposure. This provides a clear interpretation for privacy-relevant false-negative rates and selective-risk analyses.

## 5.5 Annotation

Each case will include case identifier, **source tier/provenance**, natural-language scenario, structured feature representation, expert action label, annotator certainty, brief rationale, difficulty/adversarial flag, and split assignment. Adjudicators will also record an **exposure-impact profile** covering identifiability/linkability, sensitivity, scale, vulnerability, exploitability, and persistence/irreversibility.

Two independent reviewers will label **every locked-test case** and a stratified **20% of development cases**, including high-risk and ambiguous strata, before an adjudicator resolves disagreements. Calibration cases receive human adjudication under the same rubric; the team will pre-specify any additional double review. For one case per 600-family core, this means at least 792 initial review assignments: 600 first reviews plus 120 test and 72 development second reviews. Variant reviews and disagreement adjudication add work. We will report initial agreement, disagreement, and adjudication decisions. Reviewer effort and the proposed trainee/practicum contribution will be confirmed before work begins and supervised by the project team; Claude credits pay for API use, **not reviewer or trainee salaries**. Split assignment occurs at the **scenario-family/source level**. The locked test remains unseen for model fitting, threshold selection, prompt revision, and gate selection until the final comparison. Inference is to the sampled public/synthetic, deliberately enriched scenario-family distribution and specified perturbations, not to all clinical deployments. Even with 40 high-risk test families, very rare failure rates cannot be estimated precisely; we will report family-clustered intervals and counts rather than claim proof of safety.

---

# 6. Comparator 1 — deterministic baseline

The first baseline is the existing deterministic privacy logic in DataGangeR.

Relevant components already implemented include direct identifier detection, structured/high-cardinality identifier detection, sensitive-field heuristics, free-text detection, date and geographic handling, exact source-to-synthetic record matching, k-anonymity-related assessment and enforcement, rare-category and disclosure diagnostics, role-aware privacy checks, and human review gates.

These are not treated as obsolete once models are introduced. They remain an explicit baseline and, where appropriate, a safety floor.

---

# 7. Comparator 2 — interpretable statistical model

A conventional statistical model will be developed as a first-class comparator, not merely as a weak baseline.

Candidate predictors include record count, number of variables, direct/quasi/sensitive counts, maximum uniqueness ratio, minimum equivalence-class size, rare-category prevalence, free-text presence, temporal precision, geographic precision, combination uniqueness, missingness summaries, entropy/cardinality summaries, original versus transformed status, requested operation, local versus external access boundary, and deterministic privacy flags.

Because the four reference actions are **not assumed to form a single ordinal scale**, the primary structured model will use multinomial or one-versus-rest formulations, with generalized additive terms where justified. For action (j),

$$
P(Y_i=j\mid X_i)=
\frac{\exp\{\alpha_j+f_j(X_i)\}}
{\sum_{\ell=1}^{4}\exp\{\alpha_\ell+f_\ell(X_i)\}}.
$$

A separate binary safety endpoint will model inappropriate authorization directly. More flexible machine-learning comparators will be added only if they improve pre-specified held-out criteria.

This comparator asks how far carefully engineered structural evidence can take us without semantic AI.

---

# 8. Comparator 3 — semantic decision models

## 8.1 Claude

Claude will serve as a frontier semantic comparator. It will receive the same versioned natural-language representation as other semantic models and return structured decisions under a fixed rubric.

Claude will not define ground truth.

Its role is to establish how much signal a capable frontier model can extract from the semantic representation and to provide a high-capability comparison point for smaller local models.

## 8.2 Laya and compact local decision models

Laya is particularly relevant because it represents the deployment direction of interest: a compact, open, locally executable decision model.

The study will evaluate stock Laya, calibrated stock Laya, domain-adapted Laya only if the calibrated stock model adds residual value, and a frontier Claude comparator on the same cases. Jev will be treated as a hosted typed-decision comparator that can be calibrated and evaluated through the same interface, not as a locally fine-tuned model.

For the local English Laya baseline, each case supplies a **versioned semantic capsule of at most 512 tokens**: a bounded description of dataset meaning, intended task, access environment, and transformation state. Structured variables used by the statistical gate remain separate and are not silently appended to Laya's text. Semantic comparators receive equivalent case information under the same rubric, with their formatting and token accounting recorded. A longer Laya input may be tested only in a separately pre-specified evaluation if the selected checkpoint and runtime support it; it is not assumed in the baseline.

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

- inappropriate-authorization rate and false-negative rate among high-risk cases;
- high-severity miss rate and harm-weighted inappropriate authorization;
- Brier score and log loss;
- calibration;
- selective risk at pre-specified coverage;
- coverage at pre-specified abstention thresholds;
- joint unsafe-authorization rate for the dual-gate system.

## Secondary metrics

- sensitivity and specificity;
- balanced accuracy;
- multiclass log loss;
- expected calibration error;
- human-review burden;
- inter-rater agreement;
- incremental predictive value;
- performance by dataset domain and access type.

A particularly relevant operational quantity is:

> **Among cases for which the system chooses not to defer to a human, how often is its decision correct?**

Risk-coverage curves will therefore be central to evaluation. A privacy gate should be allowed to say "uncertain." For a confidence threshold $\tau$,

$$
R(\tau)=E\{L(Y,\hat Y)\mid C\ge\tau\},
\qquad
\mathrm{Coverage}(\tau)=P(C\ge\tau)
$$

so safety can be evaluated explicitly against the fraction of cases handled automatically.

## 11.1 Uncertainty, calibration, and dual-gate safety

Jev and Laya can return class probabilities or confidence-like outputs, but these values will be treated as **uncalibrated model scores until empirically validated**. Modern neural-network confidence is often miscalibrated, motivating held-out probability calibration rather than direct use of raw confidence (Guo et al., 2017).

For each semantic classifier we will evaluate:

- reliability/calibration curves;
- Brier score and log loss;
- expected calibration error;
- entropy and top-two probability margin;
- class-specific sensitivity/specificity;
- selective risk as uncertain cases are abstained;
- coverage at pre-specified risk targets;
- performance under distribution shift and controlled perturbations.

Calibration methods may include temperature scaling, logistic/Platt-style calibration, or isotonic regression, selected using calibration data rather than the final test set.

We will also evaluate a **dual-gate authorization strategy**. Gate A will emphasize structured/statistical evidence and Gate B semantic/contextual evidence. Bounded access is eligible only when both gates authorize it and no deterministic hard blocker applies. Disagreement or uncertainty triggers human review or a more restrictive representation. We will compare this with deterministic-only and each single-gate policy under the same hard blockers, using calibration data to pre-specify thresholds. Success requires a lower inappropriate-authorization rate, including high-risk misses, at **comparable automatic coverage and human-review burden**; risk-coverage curves and matched-coverage comparisons will show whether any apparent gain is simply due to sending more cases to people. The locked test is opened only once for the final pre-specified comparison, with family-clustered uncertainty intervals.

The key safety quantity is not just each classifier's error rate but the **joint inappropriate-authorization probability**:

$$
J=P(E_A\cap E_B\mid Y=\text{unsafe})
$$

We will also estimate excess joint failure beyond the independence benchmark,

$$
\Delta
=J-
P(E_A\mid Y=\text{unsafe})
P(E_B\mid Y=\text{unsafe})
$$

so correlated failure is measured rather than assumed away. We will test whether intentionally diversified gates reduce joint unsafe authorization relative to either gate alone and quantify the corresponding increase in abstention and human-review burden. Independence will be encouraged through distinct feature representations, model classes, and development samples; it will **not** be inferred merely because two bootstrap samples were used.

This follows the selective-classification literature, which explicitly trades coverage for lower prediction risk (Geifman & El-Yaniv, 2017; 2019). Where sample size and exchangeability assumptions are adequate, we will also explore conformal or other distribution-free risk-control methods for statistically principled abstention/coverage targets (Angelopoulos & Bates, 2021). Ensemble-style disagreement will be examined as an additional uncertainty signal, motivated by work showing that diversified predictive models can improve uncertainty estimation and sensitivity to distribution shift (Lakshminarayanan et al., 2017).

The statistical objective is therefore broader than building a classifier: **we will estimate, calibrate, compare, and stress-test the full decision system, including uncertainty, error dependence, abstention, and human-review cost.**

We will also distinguish **error frequency from error consequence**. Human adjudicators will assign the structured exposure-impact profile defined in the benchmark. A primary severity endpoint will be

$$
P(\text{authorize}\mid Y=\text{unsafe},\ H=\text{high})
$$

with a transparent, pre-specified harm-weighted analysis as a sensitivity measure,

$$
\mathrm{HWFA}
=
\frac{\sum_i h_i I(\hat A_i=\text{allow},Y_i=\text{unsafe})}
{\sum_i h_i I(Y_i=\text{unsafe})}
$$

Component harm ratings will remain visible rather than being hidden inside a single opaque score. For dual gates, we will examine not only how often both gates fail, but whether they prevent the most consequential failures.


---

# 12. Robustness experiments

Semantic models will be evaluated under controlled perturbations, including paraphrasing the same access request; renaming variables while preserving meaning; changing irrelevant wording; altering agent location from local to external; changing row-level access to schema-only access; changing geographic or temporal precision; adding or removing free text; changing original data to synthetic data; and adding combinations of individually innocuous quasi-identifiers.

Claude API credits make systematic repeated experiments at this scale feasible.

---

# 13. Existing work and investigator preparation

**Team roles.** Laura C. Rosella will serve as Principal Investigator, providing scientific oversight and public-health/implementation leadership. Lennon Li will serve as project lead and software/methods lead, with responsibility for DataGangeR/Which development, statistical evaluation, experiment orchestration, and reproducibility infrastructure. We will seek to involve approximately **3–5 Biostatistics/data-science trainees**, potentially through practicum or supervised research-project mechanisms subject to program approval. Trainees will work in a shared protocol with distinct responsibilities for benchmark curation, classifier evaluation, replication, software validation, and implementation testing.

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

## 13.6 Training the next generation of statisticians

Many current AI workflows teach students how to prompt a model, generate code, or accelerate analysis. We want to add the complementary skill that statisticians are particularly well equipped to provide: **how to evaluate an AI decision quantitatively**.

Open-ended LLM outputs are often difficult to validate with conventional statistical tools because the response space is unconstrained natural language. In this project, important AI judgments will be expressed as typed outcomes with probabilities, abstention, and explicit reference actions. That makes questions such as calibration, discrimination, uncertainty, selective risk, error dependence, subgroup performance, and reproducibility directly estimable.

The trainee program will therefore teach a two-part workflow:

1. **Use AI effectively** for statistical programming, analysis prototyping, and application development.
2. **Evaluate AI statistically** by defining outcomes, constructing held-out tests, calibrating probabilities, quantifying uncertainty and error, testing robustness, and specifying when a human should intervene.

The goal is to train statisticians who can both exploit frontier AI capability and independently assess whether its outputs deserve trust in a given context—including the statistical principle that **classification errors should be weighted by their consequences, not merely counted**.

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
- reusable training/adaptation interfaces for open decision models where weights are available, with human-governed data/version manifests;
- a reusable classifier-evaluation framework covering calibration, uncertainty, selective prediction, dual-gate/joint-error analysis, subgroup robustness, model/version drift, and regression release gates;
- evaluation metrics and confidence intervals;
- engine comparison;
- model/spec/calibration/evaluation manifests.

## DataGangeR owns

- privacy threat model;
- deterministic privacy and disclosure checks;
- bounded column/dataset summary construction;
- privacy annotation taxonomy;
- definition of agent_exposure_risk;
- statistical access-decision model;
- DataGangeR benchmark case construction;
- reconciliation of deterministic/statistical/semantic evidence;
- transformation/synthesis policy;
- human review;
- eventual ai_safe() interface.

**Which never decides what "safe data" means. DataGangeR never reimplements generic decision-engine infrastructure.**

---

# 15. Work packages

## WP1 — Decision and classifier-evaluation infrastructure

Complete Which, migrate the working Jev decision path, add Laya parity, and establish reusable **training/adaptation interfaces for open decision models** plus a classifier-evaluation layer for probability calibration, uncertainty, abstention/risk-coverage, dual-gate joint-error analysis, model/version comparison, confidence intervals, and regression release criteria. Jev will remain a hosted comparator; trainable local models such as Laya can use the adaptation pipeline when justified. Validate the infrastructure prospectively using real typed-decision tasks.

## WP2 — Privacy benchmark

Formalize the agent-access outcome and exposure-impact profile; construct scenarios from public RDM/privacy guidance, health-data dictionaries, public repositories, and synthetic counterfactuals; add approved partner-derived abstracted cases if available; establish annotation guidance; double-review every locked-test case and a stratified 20% of development cases; adjudicate disagreements; and freeze family-level development/calibration/test splits.

## WP3 — Statistical comparator

Engineer interpretable privacy features, fit conventional statistical models, evaluate calibration and selective risk, estimate uncertainty, and establish the structured-information baseline.

## WP4 — Semantic models

Evaluate Claude under a fixed rubric, evaluate stock/calibrated Laya and hosted Jev, fine-tune Laya only if justified, quantify calibration and uncertainty, and conduct robustness experiments.

## WP5 — Orchestration, model improvement, and open-source package

Test incremental semantic value, evaluate transparent fusion and dual-gate authorization, estimate joint error dependence and risk-coverage trade-offs, and build a policy-controlled orchestration layer governing when deterministic rules, statistical models, Laya, hosted comparators such as Jev/Claude, and human reviewers are invoked. Add a human-governed framework for prospective labelled-data collection, adjudication, Laya tuning when justified, hosted-model calibration/evaluation, model/version manifests, and regression-gated releases.

## WP6 — Trainee research, dissemination, and implementation pilot

Recruit and supervise approximately 3–5 Biostatistics/data-science trainees, potentially through practicum or supervised project mechanisms. The cohort will be trained in a paired workflow: **use AI to build, then use statistics to evaluate what AI produced**. Trainees will contribute to benchmark curation, typed classifier evaluation, calibration/uncertainty analysis, open-source application development, independent replication, robustness testing, and release validation.

The project will not stop at a manuscript. We will release the software, benchmark/evaluation assets, and implementation guidance. If approvals and timing permit, we will conduct a small public-health implementation pilot, potentially with PHO, using approved/public/synthetic representations. The pilot will assess usability, workflow fit, failure modes, and external validity, and may support a subsequent implementation/public-health methods publication. The pilot remains approval-dependent and is not required to complete the primary statistical aims.

---

# 16. Phased, gated research plan

The project is structured so that **later complexity is earned by evidence**. It does not require every model or partnership to succeed in order to produce useful outputs.

### Phase 1 — benchmark and evaluation infrastructure

Build the public/synthetic benchmark, annotation protocol, Which evaluation framework, and deterministic/statistical baselines.

**Gate 1:** proceed only after acceptable annotation agreement, split integrity, and reproducible baseline evaluation are demonstrated.

**Minimum deliverable if stopped here:** open benchmark protocol, classifier-evaluation software, deterministic/statistical baseline paper or report, and trainee training materials.

### Phase 2 — semantic-model evaluation

Evaluate Claude, Jev, and local Laya on the frozen benchmark; calibrate probabilities; quantify uncertainty, robustness, and incremental value.

**Gate 2:** local semantic adaptation proceeds only if semantic evidence adds pre-specified held-out value beyond simpler baselines.

**If the gate fails:** publish the negative result and retain the simpler rule/statistical system.

### Phase 3 — dual-gate integration

Evaluate structured + semantic dual gating, joint-error dependence, severity-weighted errors, abstention, and human-review burden.

**Gate 3:** retain the dual gate only if it improves safety-relevant held-out metrics enough to justify added complexity and review burden.

**If the gate fails:** deploy the best simpler calibrated architecture.

### Phase 4 — partner external validation and implementation

Seek approved partner-derived decision cases and, if feasible, a small public-health pilot.

**Gate 4:** pilot only after the software, calibration, privacy safeguards, and organizational approvals are in place.

Partner participation is therefore an **external-validation accelerator, not a dependency**. Failure to secure a partner does not prevent completion of the primary scientific aims.

~~~mermaid
flowchart LR
    P1["Phase 1<br/>Public/synthetic benchmark<br/>+ evaluation framework"] --> G1{"Gate 1<br/>reproducible + adjudicable?"}
    G1 -->|No| O1["Release benchmark methods<br/>and simpler baselines"]
    G1 -->|Yes| P2["Phase 2<br/>Claude / Jev / Laya"]
    P2 --> G2{"Gate 2<br/>incremental semantic value?"}
    G2 -->|No| O2["Retain rules/statistics<br/>publish negative result"]
    G2 -->|Yes| P3["Phase 3<br/>dual-gate safety"]
    P3 --> G3{"Gate 3<br/>safety gain justifies burden?"}
    G3 -->|No| O3["Use best simpler<br/>calibrated architecture"]
    G3 -->|Yes| P4["Phase 4<br/>partner validation / pilot"]
~~~

**Figure 4. Gated research roadmap.** Every phase produces a useful artifact; failure at a gate narrows the system rather than causing project failure.

---

# 17. Timeline

~~~mermaid
gantt
    title 12-month research plan
    dateFormat  YYYY-MM-DD
    axisFormat  %b %Y

    section Foundations
    Which/Jev migration and protocol freeze     :a1, 2026-11-01, 60d
    Laya adapter and calibration                :a2, 2026-12-01, 60d

    section Benchmark
    Outcome/annotation guide                    :b1, 2026-11-15, 45d
    Candidate scenario construction             :b2, 2026-12-01, 120d
    Core adjudication and family-level split    :b3, 2027-02-01, 90d

    section Models
    Statistical access-decision comparator      :c1, 2027-03-01, 75d
    Claude/Laya/Jev evaluation                  :c2, 2027-03-15, 90d
    Robustness and calibration                  :c3, 2027-05-15, 75d

    section Training and translation
    Trainee onboarding / protocol training      :e1, 2026-11-15, 60d
    Trainee research / independent replication  :e2, 2027-01-15, 210d
    Pilot planning / partner approvals          :e3, 2027-03-01, 120d
    Optional implementation pilot               :e4, 2027-07-01, 75d

    section Integration
    Incremental-value analysis                  :d1, 2027-06-15, 60d
    Open-source integration/regression suite    :d2, 2027-07-01, 75d
    Replication, manuscript, release            :d3, 2027-08-15, 60d
~~~

The primary scientific aims and open-source release are scheduled to complete within 12 months. Work packages intentionally overlap. The gated design protects feasibility: Phase 1 can be completed entirely from public/synthetic sources; semantic adaptation, dual-gate integration, and the partner pilot proceed only after pre-specified gates are met. A public-health implementation pilot, if feasible, will not delay the primary deliverables.

---

# 18. Purpose of Claude API credits
## Application-field draft — maximum 500 words

Claude API credits will support five connected research functions.

**First, Claude will serve as a frontier semantic comparator.** Benchmark cases will contain versioned descriptions of datasets, intended uses, proposed AI-agent operations, and access conditions. Claude will return structured decisions under a fixed rubric for comparison with deterministic safeguards, interpretable statistical models, and compact local models.

**Second, Claude will support labelled-data development and training supervision.** Claude will help transform public research/privacy documentation into candidate scenarios, generate counterfactuals and hard cases, propose provisional labels and rationales for human adjudication, identify blind spots, and assist with experiment design and error analysis. Claude-generated material will not automatically become ground truth. Human reviewers will approve benchmark cases, gold labels, training-set additions, and release decisions. The primary untouched test set will be independently curated and will not use Claude-generated labels as its reference standard.

**Third, Claude will support systematic robustness experiments.** We will vary wording, identifiability, sensitivity, requested operation, access environment, and transformation status while preserving scenario-family-level split integrity.

**Fourth, Claude will support validation of the open-source orchestration and model-improvement framework.** End-to-end workflows will be exercised under normal, ambiguous, adversarial, disagreement, and failure conditions. Claude can independently review selected local-model outputs and help diagnose failure patterns. Local Laya checkpoints may be tuned using local or separately funded compute; hosted Jev will be calibrated/evaluated rather than fine-tuned. Both will use the same versioned decision and evaluation framework.

**Fifth, Claude will support a supervised cohort of approximately 3–5 Biostatistics/data-science trainees and, if feasible, a small public-health implementation pilot.** Trainees will use versioned workflows for benchmark development, classifier evaluation, calibration/uncertainty analysis, blinded review, application building, reproducibility exercises, adversarial testing, and release validation. The training objective is to prepare the next generation of statisticians to do more than prompt AI: they will learn to build with it and then evaluate its classifications, probabilities, uncertainty, failure modes, and need for human review using statistical methods. Any pilot, potentially with PHO, will be contingent on organizational approval and will use approved/public/synthetic representations rather than transmitting restricted source records.

All experiments will record model, rubric, package, orchestration-policy, dataset, and split versions. Claude will provide research evidence, not policy authority. Claude-derived probabilities will be treated as predictions requiring calibration and uncertainty evaluation; they will be compared using proper scoring rules, selective prediction, disagreement/joint-error analysis, and human-review burden rather than simple accuracy alone. Sonnet will carry most high-volume experimentation; Opus 5.5 will be used selectively for complex coding, independent review, and model/version re-evaluation; Fable 5.1, or an officially released successor with a verified API identifier and price, will be reserved for selected high-stakes planning and risk-evaluation tasks where added capability justifies the higher cost.

---

# 19. Budget justification
## Application-field draft — maximum 500 words

We request **CAD $75,000 in Claude API credits over 12 months**.

A bottom-up planning model supports this request using the current Claude lineup. As of September 22, 2026, **Claude Opus 5.5** was released at US$4/M input and US$20/M output tokens. **Claude Fable 5.1**, the documented public Fable model, is US$10/M input and US$50/M output and will be reserved for selected high-stakes planning, risk review, and difficult-case adjudication. Only an officially released successor with a verified API identifier and published price would be evaluated prospectively under the frozen protocol.

Illustrative annual usage:

| Workload | Scale | Model | Approx. USD |
|---|---:|---|---:|
| Candidate-case / labelled-data workflows | 5,000 long-context runs | Sonnet 5 | $2,250 |
| High-stakes planning/risk adjudication | 2,000 runs | Fable 5.1 / successor | $6,000 |
| Bulk benchmark / robustness scoring | 200,000 evaluations | Sonnet 5 Batch | $7,000 |
| Orchestration / regression validation | 10,000 agentic runs | Sonnet 5 | $9,000 |
| 3–5 trainee research program | ~9,500 supervised runs | Sonnet 5 | $7,125 |
| Open-source coding / validation | ~4,000 long-context runs | Opus 5.5 | $12,000 |
| Conditional public-health pilot | ~3,000 runs | Sonnet 5 | $3,000 |
| Model/version re-evaluation | ~4,000 runs | Opus 5.5 | $6,000 |
| **Planned total** |  |  | **~$52,375 USD (~$73,660 CAD)** |

The remaining margin accommodates exchange-rate movement and workload variation. These are planning assumptions, not quotas. The trainee workload assumes a supervised cohort of approximately 3–5 students using versioned AI workflows for both application development and statistical evaluation; credits support API use, not compensation. API use will be logged by experiment, model, user/workstream, token count, and purpose.

In this budget a run is a workload unit at the row's average input/output token totals. The 200,000 bulk evaluations are one API call apiece, illustrated by 2,500 candidate cases × 4 controlled variants × 4 repeats × 5 pre-specified model/rubric-version conditions. This is a usage calculation, not a claim of 200,000 independent cases or statistical power. Other rows are multi-call aggregate sessions with tokens summed across tool turns, retries, and context. The bulk row alone assumes published Batch pricing; other rows use standard uncached rates, so no caching discount is budgeted. At 1 USD = 1.4064 CAD, US$52,375 is CAD $73,660.20, rounded to approximately CAD $73,660. The detailed row arithmetic is in the budget model.

The project is explicitly designed for classification errors. A semantic classifier cannot independently authorize sensitive-data access. Deterministic hard blockers remain authoritative; low-confidence predictions abstain; disagreement between statistical and semantic evidence escalates to human review; and consequential releases require human approval. Post-release regression tests, audit logs, and versioned rollback points allow a model or policy change to be withdrawn if error rates worsen.

Local Laya tuning will use local/separately funded compute; Jev will be calibrated/evaluated as a hosted comparator. Claude credits fund labelled-data development, training supervision, frontier comparison, adversarial testing, independent evaluation, orchestration validation, and reproducible release testing.

---

# 20. AI safety
## Application-field draft — maximum 500 words

Safety and privacy are the central research questions of this project rather than ancillary considerations.

The initial benchmark will be constructed from public documentation, public datasets, synthetic examples, and expert-authored scenarios. Confidential research records, personal health information, credentials, and other restricted source data will not be submitted to the Claude API for benchmark construction or model comparison.

We will maintain a strict separation between **model evidence and policy authority**. Claude and other semantic models will return predictions under a versioned rubric; they will not independently authorize access to research data. Deterministic privacy safeguards and human review will remain authoritative for consequential decisions.

Claude-generated scenarios or proposed labels will not automatically become ground truth. Benchmark labels will be human reviewed, provenance will be recorded, and development/calibration/test partitions will be frozen before final model comparison. Scenario families—including paraphrases and counterfactual variants derived from the same source case—will remain within a single partition to reduce information leakage. We will explicitly report semantic-model disagreement, calibration, abstention, wording sensitivity, and privacy-relevant false negatives.

DataGangeR's existing default no-network workflow will be preserved. Future semantic integration will remain optional, with local inference preferred for sensitive applications. Raw records will not be transmitted to remote decision models. Any future model-assisted production workflow will operate on bounded and versioned summaries whose disclosure properties must be evaluated separately.

The proposed local-firewall architecture is designed specifically to reduce unnecessary exposure: deterministic checks, an interpretable statistical model, and a compact local semantic model operate inside the trusted boundary before a larger external agent receives a minimum-necessary representation. A policy-controlled orchestrator will enforce component permissions, minimum-necessary context, structured outputs, disagreement escalation, and human gating; individual agents will not be free to expand their own data access.

All public software, benchmark-generation procedures, model specifications, calibration artifacts, and evaluation code will be version controlled to support reproducibility and independent audit. We will avoid claims that any model score guarantees anonymity, regulatory compliance, or universal safety.

**Classification-error fallback.** Model classifications are advisory evidence, not autonomous authorization. The operational fallback is conservative and layered:

1. deterministic hard blockers cannot be overridden by a favorable model prediction;
2. calibrated confidence below a pre-specified threshold produces **abstention**, not access;
3. material disagreement among deterministic, statistical, and semantic evidence triggers **human review**;
4. ambiguous or out-of-distribution cases default to the more restrictive representation or no direct exposure;
5. every decision records model/version, inputs, outputs, confidence, policy version, and human override;
6. regression monitoring can suspend or roll back a model/checkpoint/policy if predefined error or calibration limits are exceeded.

The primary safety endpoint will include **inappropriate authorization**—allowing direct/bounded access when the reference action requires transformation, human review, or no direct exposure. We will also report **harm-weighted inappropriate authorization** and high-severity miss rates so that errors with potentially serious PI/PHI consequences count more than low-impact mistakes.

---

# 21. Abstract
## Application-field draft — maximum 200 words

Researchers increasingly use cloud AI to prototype analyses, write code, and build research applications. In medical and public-health research, those workflows may involve data containing **personal information (PI), personal health information (PHI), sensitive attributes, or identifying combinations of variables**. This creates a privacy question before the first prompt: **is the representation we are about to share—original, de-identified, synthetic, or summarized—appropriate for this AI service and this task?**

Synthetic data can reduce unnecessary exposure, but it is not automatically safe. Privacy depends on what information is preserved, how the data were generated, what the agent is asked to do, and where the computation occurs.

We will develop and statistically evaluate calibrated decision methods for AI data access, comparing deterministic privacy safeguards, an interpretable access-decision model, and semantic classifiers. We will study calibration, uncertainty, abstention, dual-gate authorization, joint error, and human-review burden rather than relying on raw model confidence.

Claude will support labelled-data development, robustness testing, independent evaluation, and supervised trainee workflows. The project will deliver an open-source privacy-gating and classifier-evaluation framework in DataGangeR/Which, together with a provenance-tracked benchmark and a path to real-world public-health implementation.

# 22. Keywords

**privacy-preserving AI; statistical calibration; selective prediction; data access; AI agents; semantic decision models; local AI; synthetic data; disclosure risk; biostatistics; interpretable models; responsible AI**

---

# 23. Expected contributions

## Methodological

- a formalized agent-exposure decision problem;
- comparison of structural/statistical versus semantic evidence;
- calibration and selective-prediction methodology for AI access gates;
- incremental-value analysis for semantic decision models;
- transparent ensemble/dual-gate methodology if justified;
- calibration and uncertainty analysis for typed semantic decision models;
- statistical analysis of joint unsafe-error probability, error dependence, abstention, human-review burden, and severity-weighted consequences of false authorization.

## Data

- an open, provenance-tracked benchmark of AI data-access scenarios;
- expert annotation guidance;
- controlled robustness and adversarial subsets.

## Software and evaluation infrastructure

- an open-source, human-gated AI privacy-firewall framework spanning DataGangeR and Which;
- reusable training/adaptation tooling for open typed-decision models, with human-governed labelled-data and version manifests;
- a reusable classifier-evaluation framework in Which for calibration, uncertainty, selective prediction, dual-gate/joint-error analysis, subgroup robustness, model/version drift, and regression release gates;
- a policy-controlled orchestration layer for deterministic tools, statistical models, Laya/Jev, Claude, and human review;
- a reusable, human-governed prospective labelled-data and model-improvement framework, with Laya tuning and hosted-model calibration/evaluation exposed through open-source interfaces where useful;
- engine-neutral decision/calibration infrastructure in Which;
- Jev and Laya adapters;
- statistical and semantic evaluation tooling;
- reusable adversarial and regression-validation suites;
- reproducible model/spec/calibration/orchestration manifests.

## Training and translational impact

- a supervised 3–5 trainee program in **AI application development plus statistical evaluation of AI classifications, probabilities, uncertainty, and failure modes**;
- a practical reference architecture for local AI privacy firewalls;
- guidance on when compact local models are sufficient;
- evidence for when human review remains necessary;
- supervised trainee experience in privacy-aware AI evaluation and reproducible model testing;
- a potential public-health pilot, subject to organizational approval;
- reusable decision infrastructure designed for later public-health applications such as aberration triage and escalation;
- a path for institutions to reduce unnecessary disclosure while retaining AI utility.

---

# 24. Publication, open-source, and translation pathway

The project is designed to produce **research evidence, reusable infrastructure, and real-world implementation experience** rather than ending with a manuscript.

### Core outputs within the 12-month award

1. **Primary methods manuscript:** calibration, uncertainty, selective prediction, dual-gate safety, and consequence-aware evaluation for AI data-access decisions, including joint-error dependence and human-review burden.
2. **Open-source release:** DataGangeR/Which privacy-gating workflow plus the reusable classifier-evaluation framework, regression tests, versioned evaluation manifests, and implementation documentation.
3. **Open benchmark/evaluation assets:** provenance-tracked scenarios, annotation guidance, frozen evaluation splits where licensing permits, and reproducible statistical analysis code.
4. **Trainee outputs:** supervised student analyses, reproducibility reports, presentations/posters, and documented contributions to software/evaluation modules, with a reusable training workflow for statistically evaluating AI classifiers and their uncertainty.

### Follow-on publication opportunities

If the software/evaluation framework reaches sufficient maturity, we will target a second software/methodology paper describing the reusable classifier-evaluation and model-improvement infrastructure. If a partner implementation pilot proceeds and produces sufficient evidence, we will develop an implementation/public-health methods report or manuscript focused on workflow fit, failure modes, human oversight, and external validity.

These follow-on papers are **opportunities rather than dependencies**: failure to secure a partner approval or a second publication does not compromise the primary study.

### Partner translation

A public-health pilot is important because the project is intended for use, not only publication. Subject to organizational approval, a partner such as PHO would test the released framework on realistic approved/public/synthetic workflows. Pilot feedback will be treated as implementation evidence, used to identify usability and safety failures, and fed back into regression tests and documentation before broader dissemination.

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
| Candidate benchmark is too large for expert review | Maintain a large candidate pool but rigorously adjudicate a smaller core benchmark |
| Counterfactual variants leak across data splits | Split by source/scenario family, not individual generated case |
| Laya/Jev capabilities differ from assumptions | Treat Laya tuning and Jev calibration/evaluation separately; retain engine-neutral interfaces |
| Partner-derived cases are unavailable | Complete the primary benchmark from public/synthetic sources; partner cases are external validation, not a dependency |
| Pilot approvals/timing are unavailable | Pilot remains optional and does not affect completion of primary aims |
| A later modelling phase does not meet its gate | Stop escalation, release the simpler validated architecture, and publish the negative/neutral result |
| Dual gates make correlated mistakes | Measure joint error and dependence explicitly; diversify evidence/model families; do not assume independence |
| Raw model confidence is overconfident | Recalibrate on held-out data; use abstention, risk-coverage analysis, and human review |
| Error counts hide consequence | Annotate exposure impact and report harm-weighted false authorization and high-severity miss rates |

---

# 26. Why this project is timely

AI agents are moving from text generation toward direct participation in scientific workflows. Data access is therefore becoming an active decision rather than a static permission.

At the same time, capable semantic models and compact local decision models now make it possible to ask whether contextual privacy reasoning can be operationalized without placing all decision authority in a large external model.

The methodological opportunity is to turn consequential AI judgments from difficult-to-evaluate free-form language into typed predictions with explicit reference outcomes, then bring conventional statistical principles—calibration, held-out validation, uncertainty, proper scoring, selective prediction, and incremental-value analysis—to their evaluation. This is also an educational opportunity: statisticians already possess much of the methodological vocabulary needed to evaluate classifiers rigorously, but need training to apply it to AI systems.

The practical opportunity is to create a local decision boundary that lets researchers benefit from increasingly capable AI while minimizing unnecessary exposure of research participants' information. More broadly, if typed decision models become a common complement to generative LLMs, reproducible training/adaptation and statistical evaluation infrastructure will become increasingly important.

---

# 27. Program alignment

The University of Toronto Data Sciences Institute Claude API Credit Award provides up to CAD $100,000 in Claude API credits for research projects over a maximum of 12 months. The proposed project uses Claude as a research instrument and frontier comparator while directly addressing responsible AI deployment, privacy, statistical methodology, reproducibility, open research software, and hands-on training of 3–5 Biostatistics/data-science trainees to both build with AI and evaluate its outputs and uncertainties using statistical methods.

Anthropic's Canadian research initiative emphasizes beneficial and responsible applications of AI, including trust and safety and health/science research. This project connects those themes through a concrete methodological problem: determining the minimum information an AI system should receive to contribute productively to scientific work.

---

# 28. References and relevant resources

- University of Toronto Data Sciences Institute. **Claude API Credit Award.**  
  https://datasciences.utoronto.ca/claude-api-credit/

- Anthropic. **Anthropic commits $10 million to Canadian AI research.** 2026.  
  https://www.anthropic.com/news/canadian-ai-research

- Anthropic. **Claude Platform pricing.** Accessed 2026-09-22.  
  https://platform.claude.com/docs/en/about-claude/pricing

- Bank of Canada. **Daily Digest — exchange rates.** 2026-09-22.  
  https://www.bankofcanada.ca/rates/daily-digest/

- DataGangeR source repository.  
  https://github.com/lennon-li/dataganger

- Which source repository.  
  https://github.com/lennon-li/which

- Tri-Agency. **Research Data Management Policy.**  
  https://science.gc.ca/site/science/en/interagency-research-funding/policies-and-guidelines/research-data-management/tri-agency-research-data-management-policy

- ICES. **Data Dictionary.**  
  https://www.ices.on.ca/use-ices-data/data-dictionary/

- Public Health Ontario. **Data Requests.**  
  https://www.publichealthontario.ca/en/Data-and-Analysis/Using-Data/Data-Requests

- NIST. **Guidelines for Evaluating Differential Privacy Guarantees (SP 800-226).** 2025.  
  https://csrc.nist.gov/pubs/sp/800/226/final

- Stadler, T., Oprisanu, B., & Troncoso, C. (2022). **Synthetic Data – Anonymisation Groundhog Day.** 31st USENIX Security Symposium, 1451–1468.  
  https://www.usenix.org/conference/usenixsecurity22/presentation/stadler

- Microsoft Presidio.  
  https://github.com/microsoft/presidio

- TypeSafe AI. **Introducing System One Models & Jev.** 2026.  
  https://typesafe.ai/blog/introducing-system-one-models-and-jev

- Laya. **Model card and architecture.**  
  https://huggingface.co/convaiinnovations/laya

- RouteLLM.  
  https://github.com/lm-sys/RouteLLM

- Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). **On Calibration of Modern Neural Networks.** ICML, PMLR 70:1321–1330.  
  https://proceedings.mlr.press/v70/guo17a.html

- Geifman, Y., & El-Yaniv, R. (2017). **Selective Classification for Deep Neural Networks.** NeurIPS 30.  
  https://papers.neurips.cc/paper_files/paper/2017/hash/4a8423d5e91fda00bb7e46540e2b0cf1-Abstract.html

- Geifman, Y., & El-Yaniv, R. (2019). **SelectiveNet: A Deep Neural Network with an Integrated Reject Option.** ICML, PMLR 97:2151–2159.  
  https://proceedings.mlr.press/v97/geifman19a.html

- Angelopoulos, A. N., & Bates, S. (2021). **A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification.** arXiv:2107.07511.  
  https://arxiv.org/abs/2107.07511

- Lakshminarayanan, B., Pritzel, A., & Blundell, C. (2017). **Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles.** NeurIPS 30.  
  https://papers.neurips.cc/paper_files/paper/2017/hash/9ef2ed4b7fd2c810847ffa5fa85bce38-Abstract.html


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

> **Can calibrated statistical and semantic evidence determine whether an original, transformed, synthetic, or summarized representation of medical or public-health data—including data derived from PI/PHI—is appropriate to expose to a cloud AI agent for a specific research task?**

# Appendix C. One-sentence translational vision

> **A small local model should be able to guard the door to a much larger AI model without requiring PI/PHI or other sensitive research data to leave the trusted environment merely to decide whether an appropriate representation may leave it.**
