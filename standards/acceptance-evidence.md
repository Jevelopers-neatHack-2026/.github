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

## Fictional examples with supporting records

These four complete schema demonstrations are fictional training cases, not Jevelopers program evidence. Their illustrative outcomes explain how a record would read if the scenario occurred; the actual outcome in each record is N/A because no command ran. UNKNOWN and N/A fields are intentional and are not evidence. No fictional SHA, URL, date, reviewer, artifact digest, or cost is supplied.

### Sample A — documentation-only

| Required field | Fictional supporting record |
|---|---|
| Acceptance IDs; owning repository/issue | N/A — this standalone fictional documentation example is not linked to a product criterion or issue. |
| Exact tested SHA or manifest digest | UNKNOWN — no execution occurred. |
| Runtime, configuration, environment, input/fixture identity and digest | Documentation-only local checkout and a link-check fixture are hypothetical; exact runtime, configuration, revision, and digest are UNKNOWN. |
| Command; expected and actual result | Example command to record after execution: the destination's documented Markdown/link check. Illustrative expectation: links pass. Actual command and result: N/A — not run. |
| Execution date and reviewer role | N/A — no run or review occurred. |
| Evidence URL/hash, access class, redaction | None — no run artifact exists. |
| Criterion state; actual execution outcome; provider mode | Planned; N/A (no command ran); N/A (no provider call). The illustrative label guidance-ready is not a verified criterion. |
| Limitations; blocker owner | No product behavior is tested. Destination owner role is unassigned in this standalone sample; a real destination owner must record evidence. |
| Budget/cost/usage | N/A for the imagined documentation-only process because no provider call is proposed; this is not a claim of zero product cost. |

### Sample B — hypothetical passing mock case

| Required field | Fictional supporting record |
|---|---|
| Acceptance IDs; owning repository/issue | N/A — no real product criterion or issue is identified. |
| Exact tested SHA or manifest digest | UNKNOWN — no execution occurred. |
| Runtime, configuration, environment, input/fixture identity and digest | A hypothetical isolated local checker and synthetic fixture; exact runtime, configuration, revision, and fixture digest are UNKNOWN. |
| Command; expected and actual result | Example command to record after execution: the checker test against the synthetic fixture. Illustrative scenario outcome: the mock check passes. Actual command and result: N/A — not run. |
| Execution date and reviewer role | N/A — no run or review occurred. |
| Evidence URL/hash, access class, redaction | None — no output, URL, hash, or reviewer evidence exists. |
| Criterion state; actual execution outcome; provider mode | Planned; N/A (no command ran); actual mode N/A. The fictional mode for the hypothetical check is mock, with illustrative outcome pass. |
| Limitations; blocker owner | A mock cannot verify any sandbox/live-required criterion. The actual criterion and owner are UNKNOWN; the master acceptance owner must decide whether live evidence is required. |
| Budget/cost/usage | UNKNOWN because no run occurred and no usage source was observed; no zero-cost claim is made. |

### Sample C — failed or skipped live-required case

| Required field | Fictional supporting record |
|---|---|
| Acceptance IDs; owning repository/issue | N/A — no real product criterion or issue is identified. |
| Exact tested SHA or manifest digest | UNKNOWN — no execution occurred. |
| Runtime, configuration, environment, input/fixture identity and digest | A hypothetical live-required integration test with a missing authorized credential or environment; exact runtime, configuration, revision, and fixture digest are UNKNOWN. |
| Command; expected and actual result | Example command to record after an authorized run: the named integration test. Illustrative result: skipped because a required prerequisite is absent. Actual command and result: N/A — not run. |
| Execution date and reviewer role | N/A — no run or review occurred. |
| Evidence URL/hash, access class, redaction | None — no run artifact exists; a real record must use an authorized, sanitized evidence location. |
| Criterion state; actual execution outcome; provider mode | Blocked; N/A (no command ran); actual mode N/A. The hypothetical required mode is live; the illustrated skip cannot pass it. |
| Limitations; blocker owner | The credential/environment and responsible owner are UNKNOWN. The actual credential owner and test owner must resolve them before execution. |
| Budget/cost/usage | UNKNOWN — no provider call occurred and no usage record was observed. Do not report pass or zero cost. |

### Sample D — hypothetical mixed-mode report

| Required field | Fictional supporting record |
|---|---|
| Acceptance IDs; owning repository/issue | N/A — no real product criterion or issue is identified. |
| Exact tested SHA or manifest digest | UNKNOWN — no component revision or assembled manifest exists in this example. |
| Runtime, configuration, environment, input/fixture identity and digest | Hypothetical local mock, sandbox supplier, and live provider components; each runtime, configuration, fixture identity, and digest is UNKNOWN. |
| Command; expected and actual result | Mock: illustrative pass, actual N/A. Sandbox: illustrative skipped for missing authorization, actual N/A. Live provider: not authorized and not run, actual N/A. Commands/results must be recorded per component if they later execute. |
| Execution date and reviewer role | N/A — no component ran and no review occurred. |
| Evidence URL/hash, access class, redaction | None — no component output or release evidence exists. |
| Criterion state; actual execution outcome; provider mode | Blocked; actual outcome N/A for every component. Illustrative modes are mock, sandbox, and live, each kept on a separate row; no aggregate pass is allowed. |
| Limitations; blocker owner | The sandbox credential/environment, live-call authority, component owners, and integration acceptance are UNKNOWN. The relevant authorized owners must resolve each blocker. |
| Budget/cost/usage | UNKNOWN — no call occurred and no billing/usage source was observed. A live cost cannot be inferred from the mock or sandbox scenario. |

| Component | Fictional mode and illustrative outcome | Actual execution/outcome | Evidence and cost |
|---|---|---|---|
| Local adapter | mock; illustrative pass | N/A — not run | No artifact; cost UNKNOWN because no usage source was observed |
| Supplier test | sandbox; illustrative skipped for missing authorization | N/A — not run | No artifact; cost UNKNOWN because no usage source was observed |
| Product provider | live; not authorized or attempted | N/A — not run | No artifact; cost UNKNOWN because no usage source was observed |

The three component rows are independent supporting records; the hypothetical mock result cannot be aggregated into a sandbox/live pass.

### Decision drills for missing or stale evidence

Each row is a fictional decision example and contains no run claim.

| Scenario | Recorded state and outcome | Release decision |
|---|---|---|
| Expected artifact or command record is missing | Blocked; skipped or N/A with the actual reason once observed; owner and source revision UNKNOWN until recorded | Do not claim verified or release-ready; obtain the missing record |
| Evidence points only to a moving branch or tag | In progress; moving ref is navigation only; immutable tested SHA UNKNOWN | Do not reuse it as immutable evidence; rerun or record the full SHA |
| Mandatory check was skipped | Blocked; outcome skipped, never pass | Do not promote or publish; satisfy the gate and record a fresh result |

The local automation fixture in this repository is separately measured documentation evidence for its own checker only. It does not replace these fictional product examples or update any master acceptance state.
