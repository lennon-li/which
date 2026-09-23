# DSI Claude API Credit Award — Portal-Ready Copy

Canonical copy-paste version for the Good Grants application.

Project: Measure Before You Share: Calibration, Uncertainty, and Dual-Gate Safety for AI Access to Medical and Public-Health Data

Working request: CAD $75,000 over 12 months

PI: Laura C. Rosella

Project lead/collaborator (not PI; not PI-eligible): Ye Lennon Li, PhD, P.Stat.

Important: the text below intentionally contains no equations, tables, citations, or Markdown-dependent formatting inside portal fields. Word counts use whitespace tokenization and leave substantial margin below the published limits.

## Project Title

Measure Before You Share: Calibration, Uncertainty, and Dual-Gate Safety for AI Access to Medical and Public-Health Data

## Abstract — 156/200 words

Researchers increasingly use cloud AI to prototype analyses, write code, and build research applications. In medical and public-health research, these workflows may involve personal information (PI), personal health information (PHI), sensitive attributes, or identifying combinations of variables. This creates a privacy question before the first prompt: is the representation we are about to share—original, de-identified, synthetic, or summarized—appropriate for this AI service and task?

We will develop and statistically evaluate calibrated decision methods for AI data access, comparing deterministic privacy safeguards, an interpretable access-decision model, and semantic classifiers. We will study calibration, uncertainty, abstention, dual-gate authorization, correlated errors, harm-weighted mistakes, and human-review burden rather than relying on raw model confidence.

Claude will support candidate-case development, robustness testing, independent evaluation, and supervised trainee workflows. The project will deliver an open-source privacy-gating and classifier-evaluation framework in DataGangeR/Which, a provenance-tracked benchmark, training for the next generation of statisticians to evaluate AI outputs statistically, and a path to public-health implementation.

## Keywords

privacy-preserving AI; statistical calibration; selective prediction; data access; AI agents; semantic decision models; local AI; synthetic data; disclosure risk; biostatistics; interpretable models; responsible AI

## Project Type

Claude Research

## Project Description — 418/500 words

Researchers increasingly use cloud AI systems to prototype statistical analyses, write R/Python code, debug pipelines, and build applications. In medical and public-health settings, the underlying data may contain PI, PHI, sensitive health characteristics, free text, dates, geography, or identifying combinations. The decision arises before upload: what representation should an AI system receive for this task, if any?

Synthetic data can reduce direct exposure, but “synthetic” is not a privacy certificate. Risk depends on what information is preserved, what the AI is asked to do, where computation occurs, and what safeguards are in place.

We will formalize this as a calibrated statistical decision problem. We will compare deterministic privacy safeguards, an interpretable statistical access-decision model, and semantic classifiers. Model probabilities will be calibrated on held-out data; uncertainty, abstention, risk-coverage, subgroup performance, correlated failures, and human-review burden will be evaluated. We will test a dual-gate strategy in which structured/statistical and semantic evidence must concur before bounded access is eligible. Success requires fewer inappropriate authorizations than simpler gates at comparable automatic coverage and human-review burden, using thresholds set before the locked final test. We will also record exposure harm and report high-severity and harm-weighted authorization errors.

A central methodological idea is to convert natural-language AI judgments into typed classifications with explicit options and probabilities. Laya scores candidate options with a local encoder; Jev exposes a hosted typed-decision interface. The local English Laya baseline receives a versioned semantic capsule of at most 512 tokens; structured variables stay separate, and semantic comparators receive equivalent information. Longer Laya input is a separate pre-specified evaluation only if supported. These machine-readable decisions can be calibrated, scored, thresholded, compared, and audited; numeric probabilities are not assumed calibrated.

We will generate 2,000–5,000 candidate scenarios from public guidance, data dictionaries, and synthetic counterfactuals. At least 600 independent human-adjudicated families will form the core benchmark, split 360/120/120 for development/calibration/locked test; at least 40 test families will be high risk. Every test case and a stratified 20% of development cases will receive independent double review, with disagreements adjudicated. Inference applies to sampled public/synthetic families and planned perturbations; very rare failures cannot be estimated precisely.

The project will deliver an open-source human-gated privacy firewall spanning DataGangeR and Which; reusable training/adaptation and classifier-evaluation tools; and a supervised 3–5 trainee cohort learning to use AI and evaluate its outputs statistically.

The study is phased: benchmark and baselines; semantic-model evaluation; dual-gate integration; then optional partner validation/pilot. Each phase has a stop/go gate, so a negative result still yields reusable software, benchmark assets, and publishable evidence.

## Purpose of Claude Credits — 311/500 words

Claude API credits will support five connected research functions.

First, Claude will serve as a frontier semantic comparator. Benchmark cases will contain versioned descriptions of datasets, intended uses, proposed AI-agent operations, and access conditions. Claude will return structured decisions under a fixed rubric for comparison with deterministic safeguards, interpretable statistical models, and compact decision models.

Second, Claude will support candidate-case and labelled-data development. It will help transform public research/privacy documentation into scenarios, generate counterfactuals and hard cases, propose provisional labels and rationales for human adjudication, identify blind spots, and assist with experiment design and error analysis. Claude-generated labels will not become ground truth automatically. Human reviewers will approve benchmark cases, gold labels, training additions, and release decisions. The primary test set will be independently curated.

Third, Claude will support robustness experiments varying wording, identifiability, sensitivity, requested operation, access environment, and transformation status while preserving scenario-family split integrity.

Fourth, Claude will support development and validation of the open-source orchestration, training/adaptation, and evaluation framework. End-to-end workflows will be exercised under normal, ambiguous, adversarial, disagreement, and failure conditions. Local Laya checkpoints may be adapted using local or separately funded compute; hosted Jev will be calibrated/evaluated rather than fine-tuned. Both will use the same versioned decision and evaluation framework.

Fifth, Claude will support approximately 3–5 Biostatistics/data-science trainees and, if feasible, a small public-health implementation pilot. Trainees will use versioned workflows for benchmark development, classifier evaluation, calibration/uncertainty analysis, blinded review, application building, reproducibility, adversarial testing, and release validation. The training objective is to prepare statisticians to do more than use AI: they will learn to evaluate AI classifications, probabilities, uncertainty, failure modes, and the need for human review using statistical methods. Any pilot will require organizational approval and will use approved/public/synthetic representations rather than restricted source records.

All experiments will record model, rubric, package, orchestration-policy, dataset, and split versions. Claude provides research evidence, not policy authority.

## Amount Requested

CAD $75,000

## Budget Justification — 319/500 words

We request CAD $75,000 in Claude API credits over 12 months. The bottom-up workload model estimates US$52,375, or CAD $73,660.20 at 1 USD = 1.4064 CAD, rounded to approximately CAD $73,660. The difference from the request allows modest workload and exchange-rate variation.

Building and benchmark development. Approximately US$14,250 supports candidate-case generation, labelled-data workflows, open-source coding, and implementation of the DataGangeR/Which privacy-gating and classifier-evaluation framework. This includes constructing 2,000–5,000 candidate scenarios, generating controlled counterfactuals and hard cases, building model adapters, implementing calibration and abstention workflows, and packaging reproducible software.

Testing and statistical evaluation. Approximately US$22,000 supports bulk benchmark scoring, robustness and adversarial experiments, orchestration/regression validation, and model/version re-evaluation. The 200,000 bulk evaluations are one-call usage units: 2,500 candidate cases by four controlled variants, four repeats, and five model/rubric-version conditions. They do not represent independent cases or statistical power. Other budgeted runs are multi-call sessions whose token estimates aggregate tool turns, retries, and context.

Scientific planning and difficult-case adjudication. Approximately US$6,000 is reserved for selected high-capability review of ambiguous or high-consequence cases, experiment design, risk analysis, and independent methodological critique.

Education and supervised research. Approximately US$7,125 supports 3–5 Biostatistics/data-science trainees using versioned Claude workflows for benchmark construction, statistical classifier evaluation, reproducibility exercises, robustness testing, software validation, and independent replication. Credits support research use, not trainee compensation.

Pilot and translation. Approximately US$3,000 is reserved for a small approval-dependent public-health implementation pilot using approved/public/synthetic representations. If a pilot is not feasible within the award period, these credits will instead support additional external validation, replication, or adjudicated benchmark cases.

Sonnet will carry most high-volume work; Opus 5.5 and Fable 5.1 have selective roles. Any successor must be officially released with a verified identifier and price. Only bulk scoring assumes Batch pricing; other rows use uncached rates, with no cache discount budgeted. API calls, tokens, and actual Batch/cache use will be logged by model and workstream. Later stages proceed only if earlier gates demonstrate value.

## AI Safety — 308/500 words

Safety and privacy are the central research questions rather than ancillary considerations.

The initial benchmark will be built from public documentation, public datasets, synthetic examples, and expert-authored scenarios. Confidential research records, PHI, credentials, and other restricted source data will not be submitted to Claude for benchmark construction or model comparison.

We will maintain a strict separation between model evidence and policy authority. Claude and other semantic models will return predictions under a versioned rubric; they will not independently authorize research-data access. Deterministic privacy safeguards and human review remain authoritative for consequential decisions.

Claude-generated scenarios or proposed labels will not automatically become ground truth. Benchmark labels will be human adjudicated, provenance recorded, and family-level development/calibration/test partitions frozen before final comparison. The locked test remains untouched during fitting, prompt revision, and threshold selection. We will report calibration, abstention, disagreement, subgroup behavior, privacy-relevant false negatives, high-severity misses, and harm-weighted inappropriate authorization with family-level uncertainty.

DataGangeR's default no-network workflow will be preserved. Local inference is preferred for sensitive applications. Raw records will not be sent to remote decision models. Any future model-assisted production workflow will operate on bounded, versioned representations whose disclosure properties are evaluated separately.

The local-firewall architecture uses deterministic checks, an interpretable statistical model, and a compact local semantic model inside the trusted boundary before a larger external agent receives a minimum-necessary representation. A policy-controlled orchestrator will enforce permissions, structured outputs, disagreement escalation, and human gating.

Operational fallback is conservative: hard blockers cannot be overridden; low-confidence predictions abstain; material disagreement triggers human review; ambiguous or out-of-distribution cases default to a more restrictive representation or no direct exposure; decisions are logged; and regression monitoring can suspend or roll back a model or policy if predefined error or calibration limits worsen.

The primary safety endpoint is inappropriate authorization: allowing access when the reference action requires transformation, human review, or no direct exposure.

## Team Information

Principal Investigator

Laura C. Rosella, PhD, MHSc
University of Toronto
Dalla Lana School of Public Health
Epidemiology Division

Project lead / collaborator (not PI; not PI-eligible)

Ye Lennon Li, PhD, P.Stat.
Proposed role/description: Project Lead / Technical Lead — AI Privacy-Firewall Architecture and Software Methods. If the portal uses a fixed role list, select the closest permitted collaborator/project-lead option; do not list as PI.
Email: ye.li@utoronto.ca
Institution/affiliations: Public Health Ontario; University of Toronto
Division: Dalla Lana School of Public Health, University of Toronto
Unit: Division of Biostatistics, Dalla Lana School of Public Health
Professional titles: Biostatistical Specialist, Public Health Ontario; Adjunct Professor, University of Toronto

Planned trainee cohort

Approximately 3–5 Biostatistics/data-science trainees, potentially through practicum or supervised research-project mechanisms subject to program approval. Trainees will contribute to benchmark construction, classifier evaluation, calibration and uncertainty analysis, robustness testing, reproducibility, open-source application development, independent replication, and release validation. The training objective is to prepare the next generation of statisticians to both use AI and evaluate its outputs statistically. Claude API credits support research workflows, not trainee compensation.

## External Grant Evidence — Laura to confirm exact portal wording

Agency/program: CIHR / Diabetes Canada — Embracing Diversity to Achieve Precision & Health Equity Team Grant

Proposal: Developing a Precision Participatory and Multi-Level Approach for Population-Based Diabetes Risk Assessment to Address Inequities in Type 2 Diabetes

Status: Funded, 2025

Lead role: Principal Investigator

Laura should confirm the exact agency/program/title/lead-applicant wording against her grant record before submission.

## Required attachments / actions

- Laura PDF CV.
- Laura confirmation of external grant wording.
- Complete DSI demographic survey if required/current response is not on file.
- Laura to select the closest permitted collaborator/project-lead role for Lennon and enter his listed contact/affiliation details; do not list Lennon as PI.
- Add trainee names only if the portal requires named trainees at submission.
- Review and accept Claude/Anthropic terms.
- Final PI review and submission before the deadline.

## Internal note

The long-form Markdown proposal remains the methodological source of truth. The HTML and PDF are supplemental exports; use the portal-ready fields above for Good Grants unless DSI provides an additional attachment or narrative field.
