# Shared governance guidance

This repository publishes shared contribution standards, governance records, contributor templates, and reusable workflow starters for the Jevelopers repositories. The documentation defines expectations; it does not by itself change repository settings, prove that a product requirement passed, or establish adoption by another repository.

## Current status

At inspected public default-branch revision [4129e71](https://github.com/Jevelopers-neatHack-2026/.github/commit/4129e71f42a51d42803b1020e146f54108cf2f93), observed 2026-10-11 02:48:39 UTC, [PR #19](https://github.com/Jevelopers-neatHack-2026/.github/pull/19) published the pull-request template and adoption guide, and [PR #20](https://github.com/Jevelopers-neatHack-2026/.github/pull/20) published five active issue forms plus a security draft outside the chooser. The PR template contract is `GH-PR-TEMPLATE@1.0.0`; the issue-form contract is `GH-ISSUE-FORMS@1.0.0`. Both interface versions are separate from execution-policy pack 1.1.0, product releases, and destination adoption status. Recheck live repository state before relying on this dated snapshot.

The remaining governance guidance work is still under review. `GH-01` still needs its second-maintainer validation. `GH-07` remains blocked until a maintainer confirms a private security-reporting destination and responsible role. A dated native GitHub client check after the PR20 merge verified the five active chooser entries, editable prompts, empty-text client-side required-field rejection under a per-tab network deny guard, and 46 per-field Markdown previews. It created no issue and did not test server validation or an assembled posted body. The check recorded a small 8 px mobile document overflow as an advisory, not a responsive pass; it was not a full assistive-technology audit. The security form remains outside the chooser, and no sensitive details should be sent through an ordinary public issue while the private route is unresolved. `GH-03-I` remains open.

The central workflow documentation and local fixture can be reviewed independently of a GitHub-hosted workflow run. This repository has no root `.github/workflows` installation; downstream workflow execution, private-workflow access, fork isolation, and secret behavior remain unverified unless separately supported by actual destination evidence.

The master acceptance IDs and their status are owned by integration-evals. A merged documentation change, local fixture result, or mock check does not verify a master acceptance ID or complete a product release.

## Start here

- [Governance inventory](adoption/governance-inventory.md) and [repository gap register](adoption/governance-register.json)
- [Contribution guidance](CONTRIBUTING.md), [branch-to-review procedure](standards/contribution-workflow.md), and [agent guidance](AGENTS.md)
- [Acceptance and evidence rules](standards/acceptance-evidence.md), [evidence record](templates/evidence-record.md), and [backlog audit](templates/backlog-audit.md)
- [Architecture source-of-truth and cross-repository links](standards/architecture-linking.md)
- [Release and version guidance](standards/releases-versioning.md) and [release record](templates/release-record.md)
- [Dated partial governance release assessment](adoption/governance-release-record.md) — 2026-10-11 snapshot; GH-11 remains open.
- [Label planning](standards/labels-planning.md)
- [Security and secret handling](standards/security-secret-handling.md) and the pending [security policy draft](community/SECURITY.pending.md)
- [Reusable workflow design](automation-design/reusable-workflows.md) and the [workflow starter](workflow-templates/docs-check.yml)
- [Repository bootstrap checklist](adoption/repository-bootstrap.md) and [adoption record](templates/adoption-record.md)
- [Contributor templates and adoption guidance](templates/README.md), including the [pull-request template](.github/pull_request_template.md)
- [Issue-form source and adoption guidance](templates/issue-forms.md)
- [Repository profile](profile/README.md)

## Architecture and evidence ownership

The [local ownership view](docs/architecture/OWNERSHIP.md) defines this repository's documentation responsibility. The [local acceptance view](docs/architecture/ACCEPTANCE.md) selects criteria but is not the master tracker.

Canonical architecture and the implementation plan live in getticketstub.com. Canonical schemas live in shared-contracts. Master acceptance state and evidence records live in integration-evals. Each repository owns its local implementation instructions, checks, settings, and adoption record. See the [source registry](standards/architecture-linking.md) for immutable inspected references and link rules.

## Template and installation boundaries

The pull-request template is a published source on this repository's public default branch. GitHub may use organization default community-health files when a destination repository has no local equivalent. Local files take precedence; inherited defaults do not appear in clones. See [template guidance](templates/README.md) for source visibility, local overrides, the versioned template contract, and per-repository adoption records.

Agent instructions, CODEOWNERS, licenses, workflow callers, labels, and repository settings require deliberate local decisions. Public issue forms and pull-request templates may appear as organization defaults when a destination has no local equivalent, but a local template directory overrides them. Consult current, destination-specific evidence before claiming a setting, label, workflow, or template is active. Do not report organization-wide adoption from one repository's result.

Use the [bootstrap record](templates/adoption-record.md) to capture source revision, destination revision, applicability, verification evidence, deviations, and blockers. Public `.github` defaults are not copied into clones, and a private `.github` repository is not a supported source for public organization community-health defaults.

## Open acceptance and adoption questions

- `GH-01` remains open until the required second-maintainer review is recorded.
- `GH-07` security reporting remains blocked until a maintainer confirms the private destination and responsible role; no contact or response time is supplied here.
- `GH-03-I` remains open: post-merge native checks verified empty-text client rejection for the five active forms, but did not test server validation, an assembled issue body, or an unselected required dropdown. The private route and sixth active form remain blocked, and destination-specific adoption is unverified.
- Per-repository settings and adoption, plus any GitHub-hosted workflow execution or secret-isolation evidence, require separate destination-specific observations.
