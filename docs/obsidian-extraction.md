# What Which extracts from Obsidian

Which intentionally extracts the reusable decision architecture, not Obsidian's
machine names, quota pools, credentials, or personal routing preferences.

## Patterns retained

1. **Classifier != router.** A decision engine classifies fuzzy properties. Deterministic
   application policy decides what action follows.
2. **Compute facts in code.** Counts, release state, sensitive-data flags, deployment
   reach, quota state, and other knowable facts should not be guessed by a language model.
3. **Confidence is part of the answer.** Low-confidence axes abstain rather than silently
   turning a weak classification into an expensive or risky action.
4. **Capability floors are policy.** Planning, diagnosis, audit, and independent review
   can require a minimum capability even when a classifier calls the task easy.
5. **Failure type matters.** Quota exhaustion is not evidence of capability failure.
6. **Review independence is deterministic.** A reviewer should not silently reuse the
   same provider/model family when independence is required.
7. **Telemetry should be replayable without leaking raw task text.** Log engine/model,
   spec version, probabilities, chosen policy profile, and hashes/IDs rather than copying
   sensitive prompts by default.
8. **Calibration data is an asset separate from the engine.** The same gold cases should
   evaluate Jev, Laya, future engines, and deterministic baselines.

## Deliberately not copied

Obsidian's worker roster, model inventory, quota pools, provider priorities, cost
assumptions, and permission system remain Obsidian-specific. Which exposes policy
hooks so an application can supply those facts without embedding them in the core.
