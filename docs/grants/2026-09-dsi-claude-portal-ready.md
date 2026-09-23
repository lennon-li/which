# DSI Claude API Credit Award — Portal-Ready Copy

Canonical copy-paste version for the Good Grants application.

Project: Measure Before You Share: Calibration, Uncertainty, and Dual-Gate Safety for AI Access to Medical and Public-Health Data

Working request: CAD $75,000 over 12 months

PI: Laura C. Rosella

Project lead/collaborator: Lennon Li

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

## Project Description — 390/500 words

Researchers increasingly use cloud AI systems to prototype statistical analyses, write R/Python code, debug pipelines, and build applications. In medical and public-health settings, the underlying data may contain PI, PHI, sensitive health characteristics, free text, dates, geography, or identifying combinations. The decision arises before upload: what representation should an AI system receive for this task, if any?

Synthetic data can reduce direct exposure, but “synthetic” is not a privacy certificate. Risk depends on what information is preserved, what the AI is asked to do, where computation occurs, and what safeguards are in place.

We will formalize this as a calibrated statistical decision problem. We will compare deterministic privacy safeguards, an interpretable statistical access-decision model, and semantic classifiers. Model probabilities will be calibrated on held-out data; uncertainty, abstention, risk-coverage, subgroup performance, correlated failures, and human-review burden will be evaluated. We will test a dual-gate strategy in which structured/statistical and semantic evidence must concur before bounded access is eligible. We will also distinguish error frequency from error consequence by recording potential exposure harm and reporting high-severity and harm-weighted authorization errors.

A central methodological idea is to convert difficult-to-evaluate natural-language AI judgments into typed classifications with explicit options and probabilities. Unlike autoregressive LLMs that generate open-ended token sequences, Laya uses a bidirectional language encoder with a decision head to score candidate options directly; Jev exposes a hosted non-generative typed-decision interface. These systems retain semantic input while returning standardized, machine-readable decisions that can be calibrated, scored, thresholded, compared, and audited. Their probabilities are not assumed correct merely because they are numeric; calibration is itself a study outcome.

We will generate 2,000–5,000 candidate scenarios from public research-data-management and privacy guidance, public data dictionaries and repositories, synthetic counterfactuals, and, if agreements permit, de-identified or abstracted decision cases from privacy/data-access partners. Initial public sources can include Tri-Agency RDM guidance and public documentation from organizations such as ICES and PHO. A smaller rigorously adjudicated core benchmark will use scenario-family-level train/calibration/test separation.

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

## Budget Justification — 224/500 words

We request CAD $75,000 in Claude API credits over 12 months.

A bottom-up annual planning model using current API pricing allocates approximately US$52,375 (about CAD $73,650 at the exchange rate used for planning) across eight workloads: candidate-case and labelled-data workflows, about US$2,250; high-stakes planning and difficult-case adjudication, US$6,000; bulk benchmark and robustness scoring, US$7,000; orchestration and regression validation, US$9,000; supervised trainee research, US$7,125; open-source coding and validation, US$12,000; a conditional public-health pilot, US$3,000; and model/version re-evaluation, US$6,000.

Sonnet will carry most high-volume experimentation and trainee workflows. Opus 5.5 will be used selectively for complex coding, independent review, and model/version re-evaluation. Fable 5.1, or a formally released successor if available during the award, will be reserved for selected high-stakes planning, risk review, and difficult-case adjudication. Batch processing and caching will be used where appropriate.

These are planning assumptions, not usage quotas. API use will be logged by experiment, model, workstream, token count, and purpose. Savings from batching, caching, or price changes will be redirected to independent replication, robustness/adversarial testing, model/version re-evaluation, regression validation, or additional human-adjudicated cases rather than manufactured usage.

Claude credits fund frontier comparison, candidate-case development, robustness testing, independent evaluation, trainee supervision, orchestration validation, and reproducible release testing. Local Laya training/adaptation will use local or separately funded compute; hosted Jev will be calibrated/evaluated rather than fine-tuned. Credits support API use, not trainee compensation.

## AI Safety — 312/500 words

Safety and privacy are the central research questions rather than ancillary considerations.

The initial benchmark will be built from public documentation, public datasets, synthetic examples, and expert-authored scenarios. Confidential research records, PHI, credentials, and other restricted source data will not be submitted to Claude for benchmark construction or model comparison.

We will maintain a strict separation between model evidence and policy authority. Claude and other semantic models will return predictions under a versioned rubric; they will not independently authorize research-data access. Deterministic privacy safeguards and human review remain authoritative for consequential decisions.

Claude-generated scenarios or proposed labels will not automatically become ground truth. Benchmark labels will be human reviewed, provenance recorded, and development/calibration/test partitions frozen before final model comparison. Scenario families, including paraphrases and counterfactual variants from the same source case, will remain within one partition. We will report calibration, abstention, disagreement, wording sensitivity, subgroup behavior, privacy-relevant false negatives, high-severity misses, and harm-weighted inappropriate authorization.

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

Project lead / collaborator

Lennon Li
Role: TO CONFIRM from portal choices
Institution / unit / email: TO COMPLETE

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
- Confirm Lennon collaborator role and contact fields allowed by the portal.
- Add trainee names only if the portal requires named trainees at submission.
- Review and accept Claude/Anthropic terms.
- Final PI review and submission before the deadline.

## Internal note

The long-form technical proposal remains the methodological source of truth. It contains equations, detailed architecture, references, data-source tiers, statistical estimands, phased gates, software design, publication plan, and pilot strategy. Do not try to paste the long proposal into portal fields unless DSI explicitly provides an additional attachment or narrative field.
