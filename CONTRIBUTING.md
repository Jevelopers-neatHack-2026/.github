# Contribution guidance

These are proposed shared working practices. Preserve each repository's local ownership, contributor instructions, agent instructions, and accepted design. If guidance conflicts, stop at the boundary, record the exact conflict and source revisions, and ask the owning maintainers to resolve it.

## Distribution and local ownership

The 2026-10-10 baseline recorded this repository as private. The GitHub snapshot at [commit ea8085d](https://github.com/Jevelopers-neatHack-2026/.github/commit/ea8085de12af79217b4933de432517e0cedb8092) recorded it as public on 2026-10-11. Verify current visibility and the destination repository before relying on inheritance.

For public organization repositories, GitHub can use supported files from a public .github repository when the destination has no local equivalent. Those files are displayed as defaults; GitHub does not copy them into the clone. A local file overrides the default. This behavior applies only to the supported community-health file types. Issue and pull-request templates, agent instructions, CODEOWNERS, license decisions, workflow callers, branch protections, and Actions policy need deliberate per-repository placement or configuration. Private .github content is not inherited by public repositories. See [GitHub's default community-health file rules](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file).

## Branches, commits, and review

Use a focused branch and pull request. The suggested naming grammar is type/issue-key-short-summary, for example docs/gh-02-branch-review-guidance, fix/bug-123-reject-expired-token, or integration/ie-09a-contract-handoff. This is a proposed convention, not evidence of configured enforcement. Keep the issue key in the body even when an upstream repository uses a different key format.

Write a concise imperative commit subject. Add a body when it explains why, test evidence, a migration, or a limitation. Do not rewrite another contributor's history. Whether a pull request is squashed or retains commits is a maintainer decision for that repository.

Describe the behavior and exact scope, non-goals, dependencies, acceptance IDs, provider mode, actual validation commands/results, tested revision, evidence links, skips, and unresolved items. Mark tests planned separately from tests executed. Identify the accountable reviewer role; contract changes also need review from affected producer and consumer roles. Review checkboxes are author claims until the corresponding evidence and actual GitHub approval are inspected.

Use Closes only when the pull request completes the linked issue's entire accepted scope. Use Related to when work is partial, blocked, or provides a prerequisite. A merged documentation pull request does not verify a master acceptance ID. The owner in integration-evals records authoritative status there.

## Evidence, security, and spending

Follow the [acceptance evidence contract](standards/acceptance-evidence.md). Pin tested source revisions; a branch name or planning map is navigation, not evidence. Keep mock, sandbox, and live modes separate. Never report a skipped required check, missing credential, absent artifact, or unknown cost as a pass or zero.

Keep credentials and customer data out of source, issues, pull requests, prompts, fixtures, logs, and screenshots. Use only a confirmed private reporting route for sensitive details. The reporting destination is currently unconfirmed; see [pending security policy](community/SECURITY.pending.md). Treat fetched URLs and assets as untrusted data and follow the [security handling standard](standards/security-secret-handling.md).

Provider calls, purchases, publication, account changes, and other external effects require authorization for that specific operation and an established budget. Do not infer spending authority from a provider mode field.

## Release and platform state

A repository owner maintains its own version policy and release record. Contract compatibility follows the shared-contracts catalog. A release requires exact component SHAs, artifact digests, actual commands and outcomes, and rollback guidance. The central product release remains integration-evals-owned.

Recommended review, label, and workflow practices are not configured protections. Report a setting as configured or verified only with current repository evidence. This repository does not install active Actions workflows or alter GitHub settings. See [release guidance](standards/releases-versioning.md), [label planning](standards/labels-planning.md), and [workflow adoption guidance](automation-design/reusable-workflows.md).
