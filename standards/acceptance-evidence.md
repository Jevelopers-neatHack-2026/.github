# Acceptance and evidence

This standard records evidence for a scoped issue while preserving central acceptance ownership. The authoritative IDs and status are in [integration-evals' master checklist](https://github.com/Jevelopers-neatHack-2026/integration-evals/blob/ff1f6d2df816ebbff34742f51be728fcb5c28cb5/planning/acceptance-checklist.md) and its [JSON tracker](https://github.com/Jevelopers-neatHack-2026/integration-evals/blob/ff1f6d2df816ebbff34742f51be728fcb5c28cb5/planning/acceptance-checklist.json). The inspected tracker has planned criteria and empty evidence/tested-revision fields. It remains the source of truth; this repository does not duplicate or update it.

## Evidence record

For each verified claim, record:

- acceptance ID(s), or N/A with a reason; owning repository and issue URL;
- exact tested full commit SHA, or the digest and exact revision of an assembled manifest;
- runtime, configuration, environment, and input/fixture identity or digest;
- command or procedure, expected result, actual result, execution date, and reviewer role;
- evidence URLs and content hashes where available, with access class and redaction status;
- status, execution outcome, provider mode for each component, limitations, blocker owner role, and budget/cost/usage state including unknown values.

Never invent a URL, SHA, date, reviewer, digest, cost, or owner. Restrict evidence references to authorized readers; store sanitized summaries in the central evidence index. Do not put credentials, customer data, exploit details, signed URLs, or raw payment material in ordinary reports.

## Keep state, result, and provider mode separate

| Dimension | Values | Meaning |
|---|---|---|
| Criterion state | planned, in_progress, blocked, verified, deferred | Project decision about the requirement |
| Execution outcome | pass, fail, skipped, error, N/A with rationale | Result of one actual command or procedure |
| Provider mode | mock, sandbox, live, N/A with rationale | Mode for a specific component or procedure |

A passing mock check can be useful local evidence, but cannot verify a live-required criterion. A mixed-mode result lists each component and mode separately. A required skipped check, failed command, missing credential, absent artifact, or unknown result does not pass. Preserve failed and skipped runs.

## Completion terms and transitions

| Term | Required evidence | What it does not mean |
|---|---|---|
| Backlog-ready | Issue is fully actionable with owner role, scope, IDs, dependencies, validation and closure evidence | Code or guidance is implemented |
| Guidance-ready | Reviewed documents/templates exist and remaining plans/blockers are tracked | Repository settings or product behavior are enforced |
| Subsystem-complete | Scoped behavior is implemented and its required checks pass on an exact revision | Other repositories or the product release are complete |
| Integrated/product release | Integration-evals-owned evidence covers the exact assembled revisions and release gates | A merged PR or green mock alone is sufficient |

An issue may move planned → in_progress → verified only after its acceptance evidence is reviewed. Use blocked when a concrete prerequisite is missing. Use deferred only with an explicit scope decision and owner; a deferred P0 is an exception, not a pass. A failed or stale result returns the criterion to in_progress or blocked. Do not delete history: mark old evidence superseded and link the replacement.

## Authority and freshness

The owning role proposes a status change and supplies the record. An accountable reviewer checks scope, exact revisions, test meaning, privacy, and whether the evidence meets the criterion. The integration-evals owner updates the master Markdown/JSON tracker after its evidence review, coordinating the listed criterion owner. A local issue, local acceptance view, or merged governance document cannot change master status.

Evidence becomes stale after a relevant source contract, component, runtime, configuration, fixture, or test procedure changes. Re-run the affected check against the new revision and retain both records. A moving branch link is for navigation only; cite a full SHA for immutable evidence.

The evidence owner selects retention and access according to the actual storage and privacy policy. Until an authorized retention term exists, do not invent a duration. Restrict sensitive evidence to the smallest authorized audience and keep only sanitized metadata in shared indexes.

## Release decision rules

| Observation | Decision |
|---|---|
| Only docs or an issue is merged | Guidance or planning may be ready; master product criterion remains unchanged |
| Mock passes; criterion requires sandbox/live | Record the mock pass and leave required mode pending/blocked |
| Required check failed, skipped, or errored | Do not call the criterion verified |
| Credential, artifact, SHA, digest, reviewer, or result is missing | Keep unknown/pending; do not substitute a plausible value |
| Tested ref is main, a tag, or another moving name | Useful navigation, not immutable evidence |
| Component/contract changed after a pass | Mark old evidence stale and rerun the affected check |
| Local tests pass but integrated evidence is absent | Subsystem evidence only; integrated release remains owned by integration-evals |

## Fictional examples

Every row below is fictional training data and is not Jevelopers program evidence. Example SHAs, dates, and URLs are intentionally omitted.

- Documentation-only: state guidance-ready; execution outcome pass for the cited local documentation commands; provider mode N/A (no provider was called). No master acceptance ID is verified.
- Mock-only component: a hypothetical checker passes a synthetic fixture on a named test revision; provider mode mock; an acceptance criterion requiring live provider evidence stays planned or blocked.
- Failed/skipped live-required check: record the actual failure or skip if one occurs; state blocked while the required credential or environment is unavailable. Do not write pass or zero cost.
- Mixed mode: list a mocked local adapter, sandbox supplier, and a separately live-paid model call as separate components, including actual paid usage or unknown cost. The report cannot flatten them into one provider-mode label.
