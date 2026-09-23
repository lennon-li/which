# DSI Claude API Credit Award — Application Packet

**Project:** Measure Before You Share: Calibration, Uncertainty, and Dual-Gate Safety for AI Access to Medical and Public-Health Data  
**Program:** University of Toronto Data Sciences Institute — Claude API Credit Award  
**Tier:** Claude Research  
**Deadline:** September 25, 2026, 23:59 ET  
**Working request:** CAD $75,000 in Claude API credits over 12 months  
**PI:** Laura C. Rosella, PhD, MHSc  
**Project lead / collaborator:** Lennon Li  
**Status:** Application-ready. Canonical copy-paste text: `docs/grants/2026-09-dsi-claude-portal-ready.md`. PI-specific items remain marked **LAURA TO CONFIRM**

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

**Measure Before You Share: Calibration, Uncertainty, and Dual-Gate Safety for AI Access to Medical and Public-Health Data**

---

## Tab 2 — Administrative Information

### Abstract — maximum 200 words

Researchers increasingly use cloud AI to prototype analyses, write code, and build research applications. In medical and public-health research, those workflows may involve data containing **personal information (PI), personal health information (PHI), sensitive attributes, or identifying combinations of variables**. This creates a privacy question before the first prompt: **is the representation we are about to share—original, de-identified, synthetic, or summarized—appropriate for this AI service and this task?**

Synthetic data can reduce unnecessary exposure, but it is not automatically safe. Privacy depends on what information is preserved, how the data were generated, what the agent is asked to do, and where the computation occurs.

We will develop and statistically evaluate calibrated decision methods for AI data access, comparing deterministic privacy safeguards, an interpretable access-decision model, and semantic classifiers. We will study calibration, uncertainty, abstention, dual-gate authorization, joint error, and human-review burden rather than relying on raw model confidence.

Claude will support labelled-data development, robustness testing, independent evaluation, and supervised trainee workflows. The project will deliver an open-source privacy-gating and classifier-evaluation framework in DataGangeR/Which, together with a provenance-tracked benchmark and a path to real-world public-health implementation.

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

### Planned trainee cohort

We propose to involve **3–5 Biostatistics/data-science trainees** in supervised project work, potentially through existing practicum or research-project mechanisms subject to program approval. The training objective is not only to teach students how to use AI to analyze data and prototype applications, but how to **evaluate AI statistically**: define reference outcomes, quantify error, calibrate probabilities, assess uncertainty, study abstention and correlated failures, and decide when human review is required. Trainees will contribute to benchmark construction, classifier evaluation, adversarial testing, reproducibility, open-source application development, and independent replication. Claude API credits will support their research workflows; the credit award will **not** be represented as trainee salary support.

- **Names/roles:** to be added if required by the portal once trainees are identified.
- **Practicum mechanism:** to be confirmed with the Biostatistics program.

---

## Tab 4 — Proposal

### A. Project Type

**Claude Research**

### B. Project Description — maximum 500 words

Researchers increasingly use cloud AI systems to prototype statistical analyses, write R/Python code, debug pipelines, and build applications. In medical and public-health settings, the underlying data may contain **PI, PHI, sensitive health characteristics, free text, dates, geography, or combinations of quasi-identifiers**. These workflows may require example rows, distributions, free text, or realistic synthetic data. The question arises **before upload**: is this representation appropriate for this AI system and task?

Synthetic data can reduce direct exposure of PI/PHI, but “synthetic” is not a privacy certificate. A generated dataset may preserve rare combinations, sensitive relationships, or source-like records, while an agentic workflow may repeatedly request additional context.

We will formalize this as a calibrated statistical decision problem and compare deterministic privacy safeguards, an interpretable access-decision model, and semantic classifiers. Raw probabilities will be recalibrated on held-out data; entropy, probability margin, disagreement, abstention, and risk-coverage will be studied. We will also test a **dual-gate authorization strategy** in which independently developed structured and semantic classifiers must concur before bounded access is permitted, estimating individual and joint inappropriate-authorization rates, error dependence, and human-review burden.

A central methodological idea is to convert an otherwise difficult-to-evaluate natural-language AI judgment into a **typed classification problem with explicit outcomes and probabilities**. This creates a natural role for biostatistics: proper scoring rules, calibration, uncertainty quantification, selective prediction, confidence intervals, subgroup analysis, and reproducible held-out validation.

This also targets an emerging AI design direction: specialized decision models that consume semantic context but return standardized choices and probabilities rather than prose. Such outputs are easier to integrate, calibrate, and audit than free-form language. Privacy is our primary testbed; the training and evaluation tools are deliberately reusable.

We will generate approximately **2,000–5,000 candidate scenarios** from public RDM/privacy guidance, public data dictionaries and repositories, synthetic counterfactuals, and—if agreements permit—de-identified or abstracted decision cases contributed by privacy/data-access partners. A smaller rigorously human-adjudicated core benchmark will use scenario-family-level train/calibration/test separation. Expert annotation will also record **potential harm if exposure occurs**, enabling harm-weighted false-authorization and high-severity miss rates.

The project has three reusable outputs: an **open-source human-gated AI privacy firewall** spanning DataGangeR and Which; a **general classifier-evaluation framework** for statistical evaluation of AI decisions; and a supervised **3–5 trainee cohort**. Students will learn not only to use AI for analysis and application building, but to evaluate its outputs and uncertainties using statistical methods.

The study is deliberately phased: public/synthetic benchmark → model evaluation → dual-gate integration → optional partner validation/pilot. Each phase has a stop/go gate, so a negative result still yields a benchmark, evaluation framework, and publishable evidence rather than an unfinished system.

A manuscript is not the endpoint. We will release software, benchmark/evaluation assets, and implementation guidance and, if approvals permit, conduct a small public-health implementation pilot, potentially with PHO.

### C. Purpose of Claude Credits — maximum 500 words

Claude API credits will support five connected research functions.

**First, Claude will serve as a frontier semantic comparator.** Benchmark cases will contain versioned descriptions of datasets, intended uses, proposed AI-agent operations, and access conditions. Claude will return structured decisions under a fixed rubric for comparison with deterministic safeguards, interpretable statistical models, and compact local models.

**Second, Claude will support labelled-data development and training supervision.** Claude will help transform public research/privacy documentation into candidate scenarios, generate counterfactuals and hard cases, propose provisional labels and rationales for human adjudication, identify blind spots, and assist with experiment design and error analysis. Claude-generated material will not automatically become ground truth. Human reviewers will approve benchmark cases, gold labels, training-set additions, and release decisions. The primary untouched test set will be independently curated and will not use Claude-generated labels as its reference standard.

**Third, Claude will support systematic robustness experiments.** We will vary wording, identifiability, sensitivity, requested operation, access environment, and transformation status while preserving scenario-family-level split integrity.

**Fourth, Claude will support validation of the open-source orchestration and model-improvement framework.** End-to-end workflows will be exercised under normal, ambiguous, adversarial, disagreement, and failure conditions. Claude can independently review selected local-model outputs and help diagnose failure patterns. Local Laya checkpoints may be tuned using local or separately funded compute; hosted Jev will be calibrated/evaluated rather than fine-tuned. Both will use the same versioned decision and evaluation framework.

**Fifth, Claude will support a supervised cohort of approximately 3–5 Biostatistics/data-science trainees and, if feasible, a small public-health implementation pilot.** Trainees will use versioned workflows for benchmark development, classifier evaluation, calibration/uncertainty analysis, blinded review, application building, reproducibility exercises, adversarial testing, and release validation. The training objective is to prepare the next generation of statisticians to do more than prompt AI: they will learn to build with it and then evaluate its classifications, probabilities, uncertainty, failure modes, and need for human review using statistical methods. Any pilot, potentially with PHO, will be contingent on organizational approval and will use approved/public/synthetic representations rather than transmitting restricted source records.

All experiments will record model, rubric, package, orchestration-policy, dataset, and split versions. Claude will provide research evidence, not policy authority. Claude-derived probabilities will be treated as predictions requiring calibration and uncertainty evaluation; they will be compared using proper scoring rules, selective prediction, disagreement/joint-error analysis, and human-review burden rather than simple accuracy alone. Sonnet will carry most high-volume experimentation; Opus 5.5 will be used selectively for complex coding, independent review, and model/version re-evaluation; Fable 5.1 (or a formally released successor such as Fable 5.2) will be reserved for selected high-stakes planning and risk-evaluation tasks where added capability justifies the higher cost.

### D. Amount Requested

**CAD $75,000 — WORKING REQUEST**

**Budget note:** This amount should be finalized only after a quantitative token-usage calculation. Current Claude pricing makes $75,000 a substantial research allocation; the application should demonstrate enough replicated inference, benchmark augmentation, long-context testing, robustness runs, and model/version sensitivity analyses to credibly exhaust the credits within 12 months.

### E. Budget Justification — maximum 500 words

We request CAD $75,000 in Claude API credits over 12 months. The request is based on a bottom-up work plan rather than a single large inference estimate. Using the current planning assumptions, expected use is approximately US$52,375, or about CAD $73,650 at the exchange rate used for budgeting, leaving a small margin for workload and exchange-rate variation.

Building and benchmark development. Approximately US$14,250 supports candidate-case generation, labelled-data workflows, open-source coding, and implementation of the DataGangeR/Which privacy-gating and classifier-evaluation framework. This includes constructing 2,000–5,000 candidate scenarios, generating controlled counterfactuals and hard cases, building model adapters, implementing calibration and abstention workflows, and packaging reproducible software.

Testing and statistical evaluation. Approximately US$22,000 supports the largest experimental workload: bulk benchmark scoring, robustness and adversarial experiments, orchestration/regression validation, and model/version re-evaluation. This is where repeated API calls are necessary to estimate calibration, selective risk, subgroup performance, wording sensitivity, joint errors, harm-weighted failures, and stability across model versions. Repeated held-out evaluation and independent replication are essential because the project studies uncertainty and failure rates, not one-off model demonstrations.

Scientific planning and difficult-case adjudication. Approximately US$6,000 is reserved for selected high-capability review of ambiguous or high-consequence cases, experiment design, risk analysis, and independent methodological critique.

Education and supervised research. Approximately US$7,125 supports 3–5 Biostatistics/data-science trainees using versioned Claude workflows for benchmark construction, statistical classifier evaluation, reproducibility exercises, robustness testing, software validation, and independent replication. Credits support research use, not trainee compensation.

Pilot and translation. Approximately US$3,000 is reserved for a small approval-dependent public-health implementation pilot using approved/public/synthetic representations. If a pilot is not feasible within the award period, these credits will instead support additional external validation, replication, or adjudicated benchmark cases.

Sonnet will carry most high-volume work; Opus 5.5 will be used selectively for complex coding, independent review, and model/version re-evaluation; Fable 5.1 or a formally released successor will be reserved for selected high-stakes planning and difficult-case review. Batch processing and caching will be used where appropriate. API use will be logged by model, experiment, workstream, token count, and purpose. The phased stop/go design also limits waste: later modelling stages proceed only if earlier stages demonstrate sufficient value.

### F. AI Safety — maximum 500 words

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
- [ ] Confirm planned **3–5 trainee** cohort, recruitment/practicum mechanism, and whether names are required at submission.
- [ ] Decide whether to name PHO as a **potential** pilot site or use generic "public-health pilot" wording until organizational approval is obtained.
- [ ] Identify 1–3 potential privacy/data-access partners for abstracted external-validation cases; do not imply participation before approval.
- [ ] Pre-specify the four stop/go gates and minimum deliverable at each phase.
- [ ] Confirm open-source deliverables: DataGangeR/Which integration, orchestration layer, prospective labelled-data/model-improvement framework, benchmark, and regression-validation suite.
- [ ] Keep secondary public-health uses as future extensibility only; primary 12-month study remains privacy-focused.
- [ ] If PHO is named, retain conditional wording unless organizational approval is obtained.
- [ ] Confirm dissemination/translation plan: primary methods manuscript + open software/benchmark + implementation guidance, with software/evaluation and pilot publications pursued when mature.
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
