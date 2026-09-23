# DSI Claude API Credit Award — Application Packet

## Executive summary

This packet guides **Laura C. Rosella, the sole PI and Good Grants submitter**, through the DSI Claude API Credit Award application. The project requests CAD $75,000 in Claude API credits over 12 months to develop and evaluate a statistically calibrated privacy firewall that helps determine what representations of medical and public-health data may be shared with cloud AI systems, for which tasks, and under what safeguards.

The packet follows the form’s sections, provides draft application answers, identifies PI decisions and required materials, and ends with a submission checklist. **Ye Lennon Li is a project lead/collaborator and is not eligible to be PI; do not list him as PI.** His contact and affiliation details are listed below for Laura to enter if the portal allows a collaborator/project-lead role.

**Open the Good Grants application:** [Start or continue the application](https://apply.datasciences.utoronto.ca/).

### How Laura should use this document

1. **Read the bold questions and action items first.** They identify decisions, confirmations, and materials needed from you as PI.
2. Review the draft answers in portal order and revise any wording that does not reflect your plans or commitments. Use the [portal-ready application](2026-09-dsi-claude-portal-ready.md) as the canonical copy/paste text; this packet is the walkthrough and checklist.
3. Follow the links to the proposal, budget, and review-memo PDFs when you want the detailed rationale or assumptions behind a draft answer. Keep those PDFs alongside this HTML file so its links work.
4. Open the [Good Grants application](https://apply.datasciences.utoronto.ca/), enter the approved content and your PI information, complete required declarations, then proofread and submit the application yourself.

### Questions to consider while reviewing

- **Eligibility and external-grant evidence:** Are you eligible and willing to serve as PI, and what exact grant record best verifies the required lead-applicant criterion?
- **Request and scope:** Is CAD $75,000 appropriate? Would you change the priorities if DSI awards less? Does the 12-month plan and its phased scope feel feasible?
- **Scientific framing:** Are the research question, benchmark/adjudication plan, safeguards, and success criteria convincing? See the full proposal PDF for methodological detail.
- **People and training:** Is the proposed 3–5 trainee cohort realistic, and what practicum or supervision route should we describe? Which collaborator role, if any, does Good Grants permit for Lennon?
- **Partners and implementation:** Should PHO remain a conditional potential pilot partner? Are there privacy/data-governance experts or partners you would recommend for review or external validation?
- **Portal and submission:** Does the live form offer an optional full-proposal attachment? Which CV should be uploaded, and are your terms acceptance and demographic-survey response current?

Please answer or annotate the bold items as you go. Lennon can revise the narrative and provide his team details; **Laura makes the PI-level decisions and submits the form.**

**Project:** Measure Before You Share: Calibration, Uncertainty, and Dual-Gate Safety for AI Access to Medical and Public-Health Data  
**Program:** University of Toronto Data Sciences Institute — Claude API Credit Award  
**Tier:** Claude Research  
**Deadline:** September 25, 2026, 23:59 ET  
**Working request:** CAD $75,000 in Claude API credits over 12 months  
**PI and submitter:** Laura C. Rosella, PhD, MHSc

**Project lead / collaborator (not PI; not PI-eligible):** Ye Lennon Li, PhD, P.Stat.

**Status:** Scientific narrative and workload model prepared. Laura is the PI and Good Grants submitter; Lennon’s team details are listed below. Submission still needs the PI confirmations below. Canonical copy-paste text: [portal-ready application](2026-09-dsi-claude-portal-ready.md); detailed background is in the linked PDFs.

---

## Laura’s walkthrough: decisions and actions

**Laura is the PI and should complete and submit the Good Grants application.** The narrative answers are drafted below. Lennon’s proposed team/contact details are included here; he can support revisions but is not the PI or submitter.

### Laura: please confirm or provide

1. **PI eligibility:** confirm you are eligible to apply as PI and are not PI on another proposal in this competition round.
2. **External-grant evidence:** confirm the exact agency/program, project title, funding status/date, and your lead-applicant role for a qualifying grant within the past three years. A publicly documented candidate is listed below, but please verify it against your grant record.
3. **Request and budget:** approve or revise the CAD $75,000 request and its reduced-award priority order. See the [budget model PDF](2026-09-dsi-claude-budget-model.pdf) for the token assumptions, model rates, arithmetic, and fallback plan.
4. **Project framing:** approve or revise the scientific narrative, 3–5 trainee plan, privacy-review approach, and whether PHO should remain a conditional potential pilot partner. See the [full proposal PDF](2026-09-dsi-anthropic-ai-privacy-firewall-proposal.pdf) for detailed methods and milestones.
5. **PI materials:** provide your PI CV as a PDF and confirm whether your required DSI demographic survey is already current.
6. **Portal-specific items:** confirm the PI role terminology, review the available team-role options for Lennon, and check whether the live form has an optional full-proposal attachment field.
7. **Final submission:** review and accept the Claude/Anthropic terms, enter the application in Good Grants, proofread the portal-rendered fields, and submit it.

### Suggested collaborator entry for Lennon

- **Name:** Ye Lennon Li, PhD, P.Stat.
- **Proposed role/description:** Project Lead / Technical Lead — AI Privacy-Firewall Architecture and Software Methods. If the portal uses a fixed role list, Laura should select the closest permitted collaborator/project-lead option.
- **Email:** ye.li@utoronto.ca
- **Institution/affiliations:** Public Health Ontario; University of Toronto
- **Division:** Dalla Lana School of Public Health, University of Toronto
- **Unit:** Division of Biostatistics, Dalla Lana School of Public Health
- **Professional titles:** Biostatistical Specialist, Public Health Ontario; Adjunct Professor, University of Toronto

**Lennon is not PI-eligible and must not be listed as PI.** Laura should enter these details only if the portal supports a collaborator/project-lead entry; if it only accepts PIs and trainees, describe Lennon in the project narrative or ask DSI how to record him.

### Reference files

- [Laura review memo PDF](2026-09-dsi-laura-review-memo.pdf) — concise decision questions and review priorities.
- [Portal-ready application PDF](2026-09-dsi-claude-portal-ready.pdf) — clean copy for reviewing the proposed form text. Use the linked Markdown version above as the copy/paste source.
- [Lennon Li CV PDF](Lennon_Li_DSI_AI_CV_2026.pdf) — background on the collaborator’s qualifications; this is not a PI CV and does not replace Laura’s required CV.
- [Full technical proposal PDF](2026-09-dsi-anthropic-ai-privacy-firewall-proposal.pdf) — detailed rationale, methods, benchmark design, and milestones.
- [Budget model PDF](2026-09-dsi-claude-budget-model.pdf) — detailed workload and cost assumptions.

Keep these PDFs alongside this HTML file so the links below open when the packet is shared. No separate long-form proposal upload is listed in the call; Laura should check the live portal for an optional attachment field.

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

**LAURA: confirm this grant qualifies and verify the exact wording against your records.**
- Agency/program: CIHR / Diabetes Canada — Embracing Diversity to Achieve Precision & Health Equity Team Grant
- Proposal: *Developing a Precision Participatory and Multi-Level Approach for Population-Based Diabetes Risk Assessment to Address Inequities in Type 2 Diabetes*
- Status: Funded, 2025
- Lead role: Principal Investigator

### Terms and Conditions

**LAURA: verify and accept Claude/Anthropic terms in the portal.**

---

## Tab 3 — Team Information

The portal asks for role, name, email, institution, division, and unit for all PIs and trainees.

### PI

- **Role:** NPI / PI — **LAURA: confirm the portal’s exact PI terminology.**
- **Name:** Laura C. Rosella
- **Email:** laura.rosella@utoronto.ca
- **Institution:** University of Toronto
- **Division:** Dalla Lana School of Public Health
- **Unit:** Epidemiology Division

### Project lead / collaborator

- **Name:** Ye Lennon Li, PhD, P.Stat.
- **Proposed role/description:** Project Lead / Technical Lead — AI Privacy-Firewall Architecture and Software Methods. If the form uses a fixed role list, **Laura: select the closest permitted collaborator/project-lead option; Lennon is not PI-eligible and must not be listed as PI.**
- **Email:** ye.li@utoronto.ca
- **Institution/affiliations:** Public Health Ontario; University of Toronto
- **Division:** Dalla Lana School of Public Health, University of Toronto
- **Unit:** Division of Biostatistics, Dalla Lana School of Public Health
- **Professional titles:** Biostatistical Specialist, Public Health Ontario; Adjunct Professor, University of Toronto

**Laura: if the portal only records PIs and trainees and has no collaborator category, check with DSI whether Lennon should be entered here or described only in the project narrative.**

### Planned trainee cohort

We propose to involve **3–5 Biostatistics/data-science trainees** in supervised project work, potentially through existing practicum or research-project mechanisms subject to program approval. The training objective is not only to teach students how to use AI to analyze data and prototype applications, but how to **evaluate AI statistically**: define reference outcomes, quantify error, calibrate probabilities, assess uncertainty, study abstention and correlated failures, and decide when human review is required. Trainees will contribute to benchmark construction, classifier evaluation, adversarial testing, reproducibility, open-source application development, and independent replication. Claude API credits will support their research workflows; the credit award will **not** be represented as trainee salary support.

- **Names/roles:** to be added if required by the portal once trainees are identified.
- **Laura: confirm whether the proposed practicum/supervised-project mechanism is realistic; add trainee names only if the portal requires them.**

---

## Tab 4 — Proposal

The form-ready narrative is included below. For the study design, benchmark rules, evaluation criteria, and phased milestones in full, see the [full technical proposal PDF](2026-09-dsi-anthropic-ai-privacy-firewall-proposal.pdf).

### A. Project Type

**Claude Research**

### B. Project Description — maximum 500 words

Researchers increasingly use cloud AI systems to prototype statistical analyses, write R/Python code, debug pipelines, and build applications. In medical and public-health settings, the underlying data may contain **PI, PHI, sensitive health characteristics, free text, dates, geography, or combinations of quasi-identifiers**. These workflows may require example rows, distributions, free text, or realistic synthetic data. The question arises **before upload**: is this representation appropriate for this AI system and task?

Synthetic data can reduce direct exposure of PI/PHI, but “synthetic” is not a privacy certificate. A generated dataset may preserve rare combinations, sensitive relationships, or source-like records, while an agentic workflow may repeatedly request additional context.

We will formalize this as a calibrated statistical decision problem and compare deterministic privacy safeguards, an interpretable access-decision model, and semantic classifiers. Raw probabilities will be recalibrated on held-out data; entropy, probability margin, disagreement, abstention, and risk-coverage will be studied. We will test **dual-gate authorization** against simpler gates at comparable automatic coverage and human-review burden, with thresholds chosen on calibration data and the test locked until final comparison. The local English Laya baseline will use a versioned semantic capsule of at most 512 tokens, equivalent case information for semantic comparators, and structured variables kept separate. Longer Laya input requires a separate pre-specified supported evaluation.

A central methodological idea is to convert an otherwise difficult-to-evaluate natural-language AI judgment into a **typed classification problem with explicit outcomes and probabilities**. This creates a natural role for biostatistics: proper scoring rules, calibration, uncertainty quantification, selective prediction, confidence intervals, subgroup analysis, and reproducible held-out validation.

Specialized decision models return standardized choices and probabilities that can be calibrated and audited. Privacy is our primary testbed; the evaluation tools are reusable.

We will generate approximately **2,000–5,000 candidate scenarios** from public RDM/privacy guidance, public data dictionaries and repositories, and synthetic counterfactuals. A core of at least **600 independent human-adjudicated scenario families** will be split 360/120/120 for development/calibration/locked test, with at least 40 high-risk test families. Every test case and a stratified 20% of development cases will be double reviewed; disagreements will be adjudicated. Expert annotation will record **potential harm if exposure occurs**. Inference covers sampled public/synthetic families and planned perturbations; very rare failure rates remain imprecise.

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

All experiments will record model, rubric, package, orchestration-policy, dataset, and split versions. Claude will provide research evidence, not policy authority. Claude-derived probabilities will be treated as predictions requiring calibration and uncertainty evaluation; they will be compared using proper scoring rules, selective prediction, disagreement/joint-error analysis, and human-review burden rather than simple accuracy alone. Sonnet will carry most high-volume experimentation; Opus 5.5 will be used selectively for complex coding and review; Fable 5.1, or an officially released successor with verified identifier and price, will be reserved for selected high-stakes planning and risk-evaluation tasks.

### D. Amount Requested

**CAD $75,000 — WORKING REQUEST**

**LAURA: approve or revise the CAD $75,000 request before submission.** The quantitative workload and token-cost calculation is complete in the [budget model PDF](2026-09-dsi-claude-budget-model.pdf) and [editable source](2026-09-dsi-claude-budget-model.md). Its rates, exchange conversion, Batch assumption, and projected usage remain planning assumptions to verify before submission; the request is a ceiling, not a commitment to exhaust credits.

### E. Budget Justification — maximum 500 words

We request CAD $75,000 in Claude API credits over 12 months. The bottom-up workload model estimates US$52,375, or CAD $73,660.20 at 1 USD = 1.4064 CAD, rounded to approximately CAD $73,660, leaving a modest margin for variation.

Building and benchmark development. Approximately US$14,250 supports candidate-case generation, labelled-data workflows, open-source coding, and implementation of the DataGangeR/Which privacy-gating and classifier-evaluation framework. This includes constructing 2,000–5,000 candidate scenarios, generating controlled counterfactuals and hard cases, building model adapters, implementing calibration and abstention workflows, and packaging reproducible software.

Testing and statistical evaluation. Approximately US$22,000 supports bulk scoring, robustness and adversarial experiments, orchestration/regression validation, and model/version re-evaluation. The 200,000 one-call bulk evaluations reflect 2,500 candidate cases × four variants × four repeats × five model/rubric-version conditions; they are usage units, not independent observations or a power calculation. Other budgeted runs are multi-call sessions with aggregate token totals.

Scientific planning and difficult-case adjudication. Approximately US$6,000 is reserved for selected high-capability review of ambiguous or high-consequence cases, experiment design, risk analysis, and independent methodological critique.

Education and supervised research. Approximately US$7,125 supports 3–5 Biostatistics/data-science trainees using versioned Claude workflows for benchmark construction, statistical classifier evaluation, reproducibility exercises, robustness testing, software validation, and independent replication. Credits support research use, not trainee compensation.

Pilot and translation. Approximately US$3,000 is reserved for a small approval-dependent public-health implementation pilot using approved/public/synthetic representations. If a pilot is not feasible within the award period, these credits will instead support additional external validation, replication, or adjudicated benchmark cases.

Sonnet will carry most high-volume work; Opus 5.5 and Fable 5.1 have selective roles. Any successor must be officially released with verified identifier and price. Only bulk scoring assumes Batch pricing; other rows use uncached rates without a cache discount. Actual calls, tokens, Batch and cache use will be logged. Later stages proceed only if earlier gates demonstrate value.

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

Required: **Laura: provide/upload your PDF CV. A PDF CV is required for every PI.**

- Laura C. Rosella — **LAURA: provide/upload your CV.**
- If another eligible Co-PI is added, that person's PDF CV is also required.
- Lennon does not need a PI CV unless the portal/application instructions separately request collaborator CVs.

---

## Demographic Survey

**Laura: mandatory for all PI applicants; complete/update it if DSI does not already have a current response on file.**

- Laura — **complete/update if DSI does not already have a current response on file.**

---

# Final submission checklist

- [ ] **Laura confirms PI eligibility and that she is not PI on another proposal in this round.**
- [ ] **Laura reviews and approves the title, abstract, project description, Claude-credit purpose, budget, and AI-safety text.** See the [review memo PDF](2026-09-dsi-laura-review-memo.pdf) for decision prompts.
- [ ] **Laura confirms exact external-grant agency/program/title, status/date, and lead-applicant wording.**
- [ ] **Laura provides and uploads her PDF CV.**
- [ ] **Laura enters Lennon’s listed name, contact, and affiliation details if the portal supports a collaborator/project-lead role; select the closest permitted role, never PI.**
- [x] Quantitative token/cost model prepared in `2026-09-dsi-claude-budget-model.md`; verify live prices and exchange conversion before submission.
- [ ] **Laura confirms the 3–5 trainee framing, recruitment/practicum mechanism, and whether names are required at submission.**
- [ ] **Laura decides whether to name PHO as a potential pilot site or use generic “public-health pilot” wording** until organizational approval is obtained.
- [ ] Identify 1–3 potential privacy/data-access partners for abstracted external-validation cases; do not imply participation before approval.
- [ ] Pre-specify the four stop/go gates and minimum deliverable at each phase.
- [ ] Confirm open-source deliverables: DataGangeR/Which integration, orchestration layer, prospective labelled-data/model-improvement framework, benchmark, and regression-validation suite.
- [ ] Keep secondary public-health uses as future extensibility only; primary 12-month study remains privacy-focused.
- [ ] If PHO is named, retain conditional wording unless organizational approval is obtained.
- [ ] Confirm dissemination/translation plan: primary methods manuscript + open software/benchmark + implementation guidance, with software/evaluation and pilot publications pursued when mature.
- [ ] **Laura verifies and accepts Anthropic terms and conditions.**
- [ ] **Laura completes the demographic survey if required/current response is not on file.**
- [ ] **Laura enters the finalized fields in Good Grants, checks the rendered form and word/character limits, and submits before September 25, 2026, 23:59 ET.**

---

# Publicly verifiable PI details for cross-checking

Laura's current DLSPH profile lists her as Professor, Epidemiology Division, tenured, Division Head, PhD Epidemiology Program Director, and DSI Associate Director of Education. The profile also lists AI/public health among her research interests.

A 2025 DLSPH announcement reports that a team led by Laura received $2 million for diabetes-risk research, and Diabetes Canada identifies her as the lead on the project named above. This appears suitable for the DSI external-grant eligibility field, subject to Laura confirming the exact grant record.

---

# Links

- DSI call: https://datasciences.utoronto.ca/claude-api-credit/
- Application portal: https://apply.datasciences.utoronto.ca/
- Full working proposal: ./2026-09-dsi-anthropic-ai-privacy-firewall-proposal.md
- [Full technical proposal PDF](2026-09-dsi-anthropic-ai-privacy-firewall-proposal.pdf)
- [Budget model PDF](2026-09-dsi-claude-budget-model.pdf)
- [Laura review memo PDF](2026-09-dsi-laura-review-memo.pdf)
- [Portal-ready application PDF](2026-09-dsi-claude-portal-ready.pdf)
