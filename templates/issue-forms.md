# Issue forms

Six program issue forms plus a chooser configuration, tracked by
[GH-03-I](https://github.com/Jevelopers-neatHack-2026/.github/issues/13).
They live in [`.github/ISSUE_TEMPLATE/`](../.github/ISSUE_TEMPLATE/).

| Form | File | Labels applied on submit | Type-specific fields |
| --- | --- | --- | --- |
| Feature | `feature.yml` | `type:implementation`, `enhancement` | user outcome |
| Bug | `bug.yml` | `type:bug`, `bug` | sanitized repro, expected vs actual, environment/revision, regression scope |
| Integration | `integration.yml` | `type:implementation`, `cross-repo` | producer, consumers, contract/version, handoff tests |
| Research / decision | `research-decision.yml` | `type:docs`, `question` | question, alternatives, bounded experiment/budget, decision owner/output, follow-on |
| Security (non-sensitive) | `security.yml` | `type:bug` | private-routing warning, sensitive-details location, no-secrets confirmation |
| Backlog / acceptance audit | `backlog-audit.yml` | `type:chore` | criterion-to-evidence coverage, gaps, release impact |

## Fields every form asks for

Issue key, owner role, priority with rationale, required-for-v1, context/current evidence, exact gap,
scope/non-goals, acceptance criteria (checkbox list), master acceptance IDs or `N/A - reason`,
dependencies as full `owner/repo#N` links, test/validation plan, provider mode
(`N/A`, `mock`, `sandbox`, `live`, `mixed`, `unknown`) and evidence required for closure.

Every free-text field is required, except optional context such as regression scope and follow-on work.
Contributors write `unknown` or `N/A - <reason>` rather than inventing a value. A required field only
forces *something* to be typed; it does not check that the answer is true. Triage still reviews it.

## Labels

Forms apply only `type:*` and GitHub default labels. These labels exist in all fourteen repositories
(checked 2026-10-10 with `gh label list`). Triage adds exactly one `priority:*` and one `state:*`, the
repository's `area:*`, `required-for-v1` and `cross-repo` where they apply, and the `v1` milestone.
The dropdown answers for priority and required-for-v1 do not set labels; GitHub issue forms cannot map
a dropdown answer to a label.

## Security routing

The security form is public and collects coordination metadata only. A confirmed private reporting
route does **not** exist yet; it is owned by
[GH-07](https://github.com/Jevelopers-neatHack-2026/.github/issues/11). Until GH-07 confirms one, the
form and `config.yml` tell reporters to contact a known maintainer privately and never to post details.
GitHub private vulnerability reporting is not claimed to be enabled. Update both files when GH-07 lands.

## How the forms reach a repository

This `.github` repository is public, so its `.github/ISSUE_TEMPLATE/` folder is the organization default
for every repository that has **no** `ISSUE_TEMPLATE` folder of its own. On 2026-10-10 none of the fourteen
repositories had one. A repository that adds any local issue template replaces the whole default set,
including `config.yml`. Inherited forms do not appear in clones.
