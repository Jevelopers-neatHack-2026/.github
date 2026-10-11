# Fictional evidence cases

All cases below are training examples, not Jevelopers program proof. They use no invented issue URLs, SHAs, dates, digests, reviewers, costs, or run URLs.

## Documentation-only case

- State: guidance-ready, not verified for a product ID.
- Outcome: pass only for documentation commands actually executed on an exact revision; the final revision is unknown until committed.
- Provider mode: N/A because no provider call occurred.
- Release claim: none.

## Mock-only pass

- State: a hypothetical subsystem check may be verified for that local behavior only after a real command/result and test revision are recorded.
- Outcome: pass on a synthetic fixture.
- Provider mode: mock.
- If the master criterion requires live behavior, that criterion remains planned or blocked; the mock cannot promote it.

## Failed or skipped live-required check

- State: blocked while credentials/environment are missing, or in_progress after a recorded failure.
- Outcome: skipped or fail, with the real reason and exact tested revision.
- Provider mode: live-required but not executed.
- Do not report pass, zero cost, or a fabricated URL.

## Mixed-mode report

List each component separately: a local mock, a sandbox supplier, and a live-paid model call only if each actually ran. Tie each to its own revision, command, environment, expected/actual result, evidence/access class, and cost/usage. Unknown billing remains unknown. A single label such as mixed cannot hide a live-required skipped check.
