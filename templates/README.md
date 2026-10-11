# Templates

Contributor templates for the fourteen Jevelopers neatHack 2026 repositories. Each one is a
documented convention; none of them configures reviews, branch protection or required checks.

| Template | Source | Issue |
| --- | --- | --- |
| Pull request template | [`.github/pull_request_template.md`](../.github/pull_request_template.md) | [GH-03-P](https://github.com/Jevelopers-neatHack-2026/.github/issues/14) |

## How the pull request template reaches a repository

- This `.github` repository is **public**, so GitHub uses its `.github/pull_request_template.md` as the
  organization default for any repository that has **no pull request template of its own**
  ([GitHub docs](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)).
- A repository that adds its own `pull_request_template.md` (in the root, `docs/` or `.github/`) overrides
  the default completely. Copy this file there and edit it if a repository needs extra sections.
- The default only pre-fills the description of **new** pull requests opened in the browser. It does not
  rewrite existing pull requests, and `gh pr create --body ...` skips it.
- Inherited files do not appear in a clone. Coding agents must read this template from this repository,
  or from the local copy, before writing a description.

Record adoption per repository (inherited default, local copy, or not applicable) in the adoption record
planned under [GH-10](https://github.com/Jevelopers-neatHack-2026/.github/issues/15).

## Filling in the template

- **Linked issues.** `Closes owner/repo#N` is only for issues whose acceptance criteria this PR fully
  meets. Use `Refs` for partial work, epics and release gates. A merged PR never verifies a master
  acceptance ID in [integration-evals](https://github.com/Jevelopers-neatHack-2026/integration-evals/blob/main/planning/acceptance-checklist.md);
  that status changes there, with evidence.
- **Acceptance criteria → evidence.** Tick a box only when the evidence next to it exists. Leave a
  criterion unticked and explain it when it is unmet, skipped or blocked.
- **Verification.** Keep *Executed* (commands that ran, with results) apart from *Planned / not run*.
  Name the tested commit SHA. A mock pass is not evidence for a live-required outcome.
- **Provider mode.** `mock`, `sandbox`, `live`, or `N/A — reason`. List components separately when a run
  mixes modes.
- **Security & provenance.** These boxes are the author's claims. A reviewer checks them; they do not
  prove that any scanner or rule ran.

## Examples

The three examples below are **samples**. Their issue numbers, SHAs and outputs are placeholders, not
program evidence.

### 1. Documentation-only change

```markdown
## Summary
Adds the branching and commit conventions to CONTRIBUTING.md so contributors and agents name branches consistently.

## Linked issues
Refs Jevelopers-neatHack-2026/.github#7

## Scope / Non-goals
- **In scope:** branch and commit naming guidance with examples.
- **Non-goals:** configuring branch protection or rulesets.

## Changes
- CONTRIBUTING.md: new "Branches and commits" section.

## Acceptance criteria → evidence
- [x] Branch and commit examples cover feature, bug, docs and cross-repo work — CONTRIBUTING.md#branches-and-commits
- [ ] A contributor can follow one example end to end — walkthrough not yet reviewed
- **Acceptance IDs:** N/A — governance documentation; verifies no master criterion.

## Verification
- **Tested revision:** <sample SHA>
- **Executed:** `npx markdown-link-check CONTRIBUTING.md` → 0 dead links (sample output)
- **Planned / not run:** reviewer walkthrough
- **Provider mode:** N/A — documentation only

## Dependencies / blockers
- **Blocked by:** None
- **Blocks:** Jevelopers-neatHack-2026/.github#10

## Cross-repo impact
None.

## Security & provenance
- [x] No secrets, tokens, credentials, signed URLs or customer data in the diff.
- [x] No new dependencies or assets (N/A).
- [x] No paid or live provider use.

## Risk & rollback
Low. Revert the commit.
```

### 2. Bug fix

```markdown
## Summary
Fixes the build failure caused by a missing root package.json; the workspace scripts now resolve from the repository root.

## Linked issues
Closes Jevelopers-neatHack-2026/<repo>#<n>

## Acceptance criteria → evidence
- [x] `npm ci && npm run build` succeeds from a clean clone — CI run <link>
- [x] Regression test added — `test/root-workspace.test.ts`
- **Acceptance IDs:** N/A — build defect

## Verification
- **Tested revision:** <sample SHA>
- **Executed:** `npm ci && npm run build && npm test` → pass (CI run <link>)
- **Planned / not run:** None
- **Provider mode:** mock — no provider calls in the build

## Risk & rollback
Medium: changes dependency resolution. Revert the PR; the previous state did not build either.
```

### 3. Cross-repo contract change

```markdown
## Summary
Adds an optional `edition` field to the order contract (minor version bump) so print-production can select a stub style.

## Linked issues
Refs Jevelopers-neatHack-2026/shared-contracts#<n> · Refs Jevelopers-neatHack-2026/print-production#<m>

## Acceptance criteria → evidence
- [x] Schema validates old and new fixtures — `npm test -- contracts/order` (CI run <link>)
- [ ] Consumer acknowledgement from print-production — requested, not yet given
- **Acceptance IDs:** CON-01 (not verified by this PR; status changes in integration-evals only)

## Verification
- **Executed:** contract fixture tests against <sample SHA> → pass
- **Planned / not run:** consumer integration test in print-production after the version is pinned
- **Provider mode:** mock

## Dependencies / blockers
- **Blocked by:** None
- **Blocks:** Jevelopers-neatHack-2026/print-production#<m>

## Cross-repo impact
Publishes contract `order` v1.1.0 (additive). Producer: shared-contracts. Consumers: print-production,
fulfillment-connectors. Both must pin v1.1.0 before using the field.

## Risk & rollback
Low: additive and optional. Roll back by re-pinning consumers to v1.0.x; do not delete the published tag.
```
