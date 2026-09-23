# DSI Claude API Credit Award — Application Packet

**Project:** Who Should See the Data? Calibrated Statistical and Semantic Gates for Privacy-Preserving AI Access to Research Data  
**Program:** University of Toronto Data Sciences Institute — Claude API Credit Award  
**Tier:** Claude Research  
**Deadline:** September 25, 2026, 23:59 ET  
**Working request:** CAD $75,000 in Claude API credits over 12 months  
**PI:** Laura C. Rosella, PhD, MHSc  
**Project lead / collaborator:** Lennon Li  
**Status:** Application-ready draft; PI-specific items marked **LAURA TO CONFIRM**

---

## What Laura needs to provide

The scientific/application text is prepared below. The remaining PI-specific items are intentionally limited:

1. **Review and approve the scientific framing and final application text.**
2. **Provide/upload a PDF CV.**
3. **Confirm one external grant on which Laura was lead applicant within the past three years.**
   - Publicly documented candidate: *Developing a Precision Participatory and Multi-Level Approach for Population-Based Diabetes Risk Assessment to Address Inequities in Type 2 Diabetes* — CIHR / Diabetes Canada, 2025, $2M team grant. **LAURA TO CONFIRM exact agency/program/title as submitted.**
4. **Complete the mandatory DSI demographic survey** if a current response is not already on file.
5. **Confirm team roles in the Good Grants portal** and submit/approve the application.

The project team will prepare the scientific text, quantitative API-usage model, open-source deliverables, trainee workflow, and pilot plan. Laura's expected commitment is PI oversight, scientific review, eligibility documentation, and final approval/submission rather than preparing the application from scratch.

No separate long-form proposal upload is listed in the call; the application is entered into portal fields. CV PDFs are required for each PI.

---

# Portal fields

## Tab 1 — Start Here

### Project Title

**Who Should See the Data? Calibrated Statistical and Semantic Gates for Privacy-Preserving AI Access to Research Data**

---

## Tab 2 — Administrative Information

### Abstract — maximum 200 words

AI agents can increasingly perform statistical analysis, programming, and research workflows, but their usefulness creates a practical privacy question that remains poorly formalized: **when should an AI agent be allowed to see research data, and when should those data first be transformed, restricted, or reviewed by a human?**

We will develop and evaluate calibrated decision methods for AI data access. Rather than treating “safe” as a binary model-generated judgment, we will compare three complementary approaches: deterministic privacy safeguards; an interpretable statistical risk model based on measurable characteristics of a dataset and proposed use; and semantic decision models that interpret natural-language data descriptions and access requests.

A distinctive focus is whether compact local models such as Laya can operate as an **AI privacy firewall**, providing contextual semantic assessment without transmitting raw records to external services. Claude will provide a frontier semantic comparator and support controlled robustness experiments.

We will construct an expert-reviewed benchmark from public documentation, data dictionaries, and synthetic scenarios, with held-out evaluation of calibration, privacy-relevant false negatives, abstention, and incremental predictive value. The project builds on the existing DataGangeR privacy framework and the engine-neutral Which decision framework.

### Keywords

privacy-preserving AI; statistical calibration; selective prediction; data access; AI agents; semantic decision models; local AI; synthetic data; disclosure risk; biostatistics; interpretable models; responsible AI

### Tri-Agency and External Grants

For each PI, DSI requires evidence of at least one external grant **secured or applied for as lead applicant within the past three years**.

**Laura C. Rosella — LAURA TO CONFIRM exact wording**
- Agency/program: CIHR / Diabetes Canada — Embracing Diversity to Achieve Precision & Health Equity Team Grant
- Proposal: *Developing a Precision Participatory and Multi-Level Approach for Population-Based Diabetes Risk Assessment to Address Inequities in Type 2 Diabetes*
- Status: Funded, 2025
- Lead role: Principal Investigator

### Terms and Conditions

**LAURA:** verify and accept Claude/Anthropic terms in the portal.

---

## Tab 3 — Team Information

The portal asks for role, name, email, institution, division, and unit for all PIs and trainees.

### PI

- **Role:** NPI / PI — **LAURA TO CONFIRM portal terminology**
- **Name:** Laura C. Rosella
- **Email:** laura.rosella@utoronto.ca
- **Institution:** University of Toronto
- **Division:** Dalla Lana School of Public Health
- **Unit:** Epidemiology Division

### Project lead / collaborator

- **Name:** Lennon Li
- **Role:** **TO CONFIRM from portal choices; do not list as PI because the budgetary-appointment criterion is not met**
- **Institution / unit / email:** **Lennon to complete**

If the portal only records PIs and trainees and has no collaborator category, confirm with DSI whether Lennon should be entered in this tab or described only in the project narrative.

---

## Tab 4 — Proposal

### A. Project Type

**Claude Research**

### B. Project Description — maximum 500 words

AI agents are increasingly capable of performing statistical analysis, programming, data cleaning, visualization, and other research tasks. Their usefulness creates a practical privacy problem: **what information does an AI agent actually need to see, and when should that information first be transformed, restricted, or reviewed by a human?**

Existing privacy controls address related but narrower questions. They can detect identifiers, quantify uniqueness, estimate disclosure risk, synthesize data, or enforce access rules, but they do not generally provide a calibrated decision about whether a particular AI agent should receive a particular representation of a dataset for a particular purpose.

We propose to formalize this as a statistical decision problem and evaluate three distinct sources of evidence:

1. **Deterministic privacy safeguards**, including direct identifiers, quasi-identifiers, free text, exact-match checks, and other facts that should not be overridden by a model.
2. **An interpretable statistical risk model** based on measurable properties of the data, proposed task, access boundary, and existing transformations.
3. **A semantic decision model** that interprets natural-language dataset descriptions, data dictionaries, intended uses, and requested AI operations.

The primary research question is whether semantic information provides **incremental, calibrated predictive value** beyond conventional structural and statistical predictors for privacy-relevant access decisions.

A second objective is to determine whether compact, locally deployable models such as Laya can provide enough contextual information to operate as an **AI privacy firewall**. The local model would operate inside the trusted environment, allowing sensitive access decisions to be made without transmitting raw records to an external service merely to determine whether they may be exposed.

We will construct an expert-reviewed benchmark of approximately 2,000–5,000 data-access scenarios using public documentation, public data dictionaries, synthetic examples, and controlled counterfactual cases. Outcomes will distinguish bounded access, transformation/redaction/synthesis, human review, and inappropriate direct exposure. Development, calibration, and final test sets will be separated prospectively.

Models will be evaluated using privacy-relevant false-negative rates, proper probabilistic scores, calibration, selective risk, abstention/coverage, robustness to wording changes, and human-review burden. Hybrid approaches will be retained only if they demonstrate incremental value over simpler alternatives on held-out data.

The project builds directly on DataGangeR, an open-source R framework for privacy-aware synthetic data and human-gated agent workflows, and Which, an engine-neutral framework for typed decisions, calibration, abstention, and model comparison.

A major deliverable will be an **open-source, human-gated AI privacy-firewall framework** that can orchestrate deterministic privacy checks, statistical risk models, compact local models such as Laya/Jev, frontier-model comparison, and human review under an explicit policy. The orchestration layer will control which component is invoked, what information it can see, when disagreement triggers escalation, and how the complete decision trail is logged.

The project will also create an open benchmark and regression-validation suite so that new model versions and software releases can be re-evaluated as AI technology changes. Students and trainees will participate in benchmark construction, blinded review, robustness testing, replication, and software validation.

Subject to organizational approval, we will seek a **real-world public-health pilot**, potentially with Public Health Ontario (PHO), to test the framework on realistic research workflows without requiring confidential records to be sent to Claude.

### C. Purpose of Claude Credits — maximum 500 words

Claude API credits will support five complementary research functions.

**First, Claude will serve as a frontier semantic-model comparator.** Each benchmark case will contain a versioned description of a dataset, intended use, proposed AI-agent operation, and access conditions. Claude will return structured decisions under a fixed rubric. Its predictions and uncertainty behavior will be compared with an interpretable statistical model and with compact local models such as Laya operating on the same cases. Claude will not define ground truth.

**Second, Claude will support benchmark construction and stress testing.** We will use Claude to help transform public privacy, research-data, and access documentation into candidate scenarios; generate controlled counterfactual variations; identify ambiguous wording; and propose difficult cases for expert review. Claude-generated material will remain candidate material: human reviewers will approve benchmark cases and gold labels, and provenance will be retained.

**Third, Claude will support systematic robustness experiments.** We will vary access purpose, identifiability, sensitivity, wording, agent location, requested operation, and transformations while holding other factors fixed. These repeated experiments will quantify whether semantic decisions respond to relevant privacy evidence or superficial phrasing.

**Fourth, Claude will support development and validation of the open-source orchestration layer.** We will test end-to-end agent-team workflows in which deterministic checks, statistical models, compact local models such as Laya/Jev, Claude, and human reviewers have explicitly bounded roles. Claude will be used to exercise normal, ambiguous, adversarial, disagreement, and model-failure scenarios; to independently review selected local-model decisions; and to support regression testing after changes to models, policies, or package code.

**Fifth, Claude credits will support trainee-led replication and a potential public-health pilot.** Students and trainees will use the API within versioned research workflows for benchmark development, blinded replication, error analysis, robustness experiments, and package validation. Subject to PHO approval, a pilot will evaluate the framework on realistic public-health research workflows using approved/public/synthetic representations rather than transmitting restricted source records.

The scientific design deliberately contrasts frontier cloud models with compact local decision models. Claude provides a high-capability semantic reference point while we test whether smaller models can recover sufficient contextual information to operate locally as a privacy firewall. Training or fine-tuning Laya/Jev itself will use local or separately funded compute; Claude credits will instead support benchmark generation, independent comparison, stress testing, calibration research, and validation around those models.

All experiments will record model, rubric, package, orchestration-policy, and dataset versions. Training, calibration, and final held-out evaluation will remain separate. Claude predictions will never be used automatically as gold labels for the local model or statistical comparator.

### D. Amount Requested

**CAD $75,000 — WORKING REQUEST**

**Budget note:** This amount should be finalized only after a quantitative token-usage calculation. Current Claude pricing makes $75,000 a substantial research allocation; the application should demonstrate enough replicated inference, benchmark augmentation, long-context testing, robustness runs, and model/version sensitivity analyses to credibly exhaust the credits within 12 months.

### E. Budget Justification — maximum 500 words

We request **CAD $75,000 in Claude API credits over 12 months** to support a replicated research, training, open-source validation, and pilot program rather than one-off interactive use.

The core benchmark will contain approximately 2,000–5,000 expert-reviewed data-access scenarios. Each scenario will be evaluated under multiple controlled variants, including changes in access environment, requested operation, data sensitivity, transformation status, semantic wording, and model configuration. Selected cases will be repeated across model versions and orchestration policies, so the total number of API evaluations will be much larger than the base benchmark.

Planned credit use is organized around five workloads:

- **25% — benchmark and frontier-model experiments:** structured Claude inference across benchmark cases, counterfactual variants, and selected model/configuration comparisons;
- **20% — open-source package and orchestration validation:** adversarial tests, disagreement handling, agent-team workflow testing, independent review, and regression suites after package/model/policy changes;
- **20% — robustness, calibration, and replication:** paraphrase/context perturbations, selective-prediction experiments, repeated runs, and independent frozen-set replication;
- **15% — trainee research and training:** supervised student use for benchmark construction, blinded review, error analysis, reproducibility exercises, and validation of successive releases;
- **10% — potential public-health pilot:** realistic workflow testing, implementation evaluation, and post-pilot regression testing, subject to organizational approval;
- **10% — model/version and pricing contingency:** re-evaluation when Claude models, local models, context windows, or API prices change during the award period.

The project will deliver reusable open-source software, not a one-time model comparison. Because the software may mediate consequential decisions about AI access to research data, meaningful changes to models, package code, or orchestration policy will trigger human-gated validation cycles and regression testing.

Local training/fine-tuning of Laya/Jev will not consume Claude credits directly. Claude credits will support the surrounding scientific workload: benchmark construction, frontier comparison, adversarial testing, calibration research, independent review, and end-to-end validation.

AI capabilities and inference economics are changing rapidly. We will therefore maintain a frozen benchmark and reproducible validation protocol while allowing newly released model versions to be prospectively evaluated. API use will be logged by experiment, model, user/workstream, input/output tokens, and purpose, and spend will be reviewed monthly.

**Before submission:** add a bottom-up quantitative usage table using current Claude API prices, estimated input/output tokens per evaluation, number of benchmark variants, repetitions, trainee workflows, and pilot/regression runs.

### F. AI Safety — maximum 500 words

Safety and privacy are the central research questions of this project rather than ancillary considerations.

The initial benchmark will be constructed from public documentation, public datasets, synthetic examples, and expert-authored scenarios. Confidential research records, personal health information, credentials, and other restricted source data will not be submitted to the Claude API for benchmark construction or model comparison.

We will maintain a strict separation between **model evidence and policy authority**. Claude and other semantic models will return predictions under a versioned rubric; they will not independently authorize access to research data. Deterministic privacy safeguards and human review will remain authoritative for consequential decisions.

Claude-generated scenarios or proposed labels will not automatically become ground truth. Benchmark labels will be human reviewed, provenance will be recorded, and development/calibration/test partitions will be frozen before final model comparison. We will explicitly report semantic-model disagreement, calibration, abstention, wording sensitivity, and privacy-relevant false negatives.

DataGangeR's existing default no-network workflow will be preserved. Future semantic integration will remain optional, with local inference preferred for sensitive applications. Raw records will not be transmitted to remote decision models. Any future model-assisted production workflow will operate on bounded and versioned summaries whose disclosure properties must be evaluated separately.

The proposed local-firewall architecture is designed specifically to reduce unnecessary exposure: deterministic checks, an interpretable statistical model, and a compact local semantic model operate inside the trusted boundary before a larger external agent receives a minimum-necessary representation. A policy-controlled orchestrator will enforce component permissions, minimum-necessary context, structured outputs, disagreement escalation, and human gating; individual agents will not be free to expand their own data access.

All public software, benchmark-generation procedures, model specifications, calibration artifacts, and evaluation code will be version controlled to support reproducibility and independent audit. We will avoid claims that any model score guarantees anonymity, regulatory compliance, or universal safety.

---

## Tab 5 — CVs

Required: **PDF CV for every PI.**

- Laura C. Rosella — **LAURA TO PROVIDE/UPLOAD**
- If another eligible Co-PI is added, that person's PDF CV is also required.
- Lennon does not need a PI CV unless the portal/application instructions separately request collaborator CVs.

---

## Demographic Survey

Mandatory for all PI applicants.

- Laura — **complete/update if DSI does not already have a current response on file.**

---

# Final submission checklist

- [ ] Laura confirms willingness to be NPI/PI and is not PI on another proposal in this round.
- [ ] Laura reviews title, abstract, project description, Claude-credit purpose, budget, and AI-safety text.
- [ ] Laura confirms exact external grant agency/program/title and lead-applicant status.
- [ ] Laura provides PDF CV.
- [ ] Confirm Lennon's correct team role in Good Grants.
- [ ] Add a quantitative token/cost model supporting the requested CAD $75,000.
- [ ] Confirm expected trainee count and trainee roles.
- [ ] Decide whether to name PHO as a **potential** pilot site or use generic "public-health pilot" wording until organizational approval is obtained.
- [ ] Confirm open-source deliverables: DataGangeR/Which integration, orchestration layer, benchmark, and regression-validation suite.
- [ ] Laura verifies Anthropic terms and conditions.
- [ ] Laura completes demographic survey if required.
- [ ] Enter all fields in Good Grants.
- [ ] Final proofread against portal character/word counts.
- [ ] Submit before **September 25, 2026, 23:59 ET**.

---

# Publicly verifiable PI details for cross-checking

Laura's current DLSPH profile lists her as Professor, Epidemiology Division, tenured, Division Head, PhD Epidemiology Program Director, and DSI Associate Director of Education. The profile also lists AI/public health among her research interests.

A 2025 DLSPH announcement reports that a team led by Laura received $2 million for diabetes-risk research, and Diabetes Canada identifies her as the lead on the project named above. This appears suitable for the DSI external-grant eligibility field, subject to Laura confirming the exact grant record.

---

# Links

- DSI call: https://datasciences.utoronto.ca/claude-api-credit/
- Application portal: https://apply.datasciences.utoronto.ca/
- Full working proposal: ./2026-09-dsi-anthropic-ai-privacy-firewall-proposal.md
