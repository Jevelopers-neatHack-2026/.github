# Shared governance guidance

This repository holds shared contribution guidance, policy drafts, and starter sources for the Jevelopers repositories. The documents describe practices; they do not themselves change a repository's settings or prove that a product requirement passed.

## Status and adoption

The reviewed starting point for this package is policy pack 1.1.0. The shared governance repository had public visibility and default branch main in the captured GitHub snapshot at commit [ea8085d](https://github.com/Jevelopers-neatHack-2026/.github/commit/ea8085de12af79217b4933de432517e0cedb8092), observed 2026-10-11. A prior 2026-10-10 baseline described it as private. Recheck live visibility and each destination before relying on GitHub defaults.

Files here affect this repository only when present on its default branch. Other repositories must deliberately install or adapt guidance. The five active issue forms and pull request template in this package are source artifacts, not proof that every repository adopted them. The security reporting draft is intentionally pending a confirmed private route. Workflow sources are examples and starters; this repository has no root .github/workflows. No branch protections, required checks, labels, licenses, CODEOWNERS assignments, or Actions settings are configured by these files.

The master acceptance IDs and evidence status remain owned by integration-evals. Merged guidance, this branch, local fixture results, and mock checks do not verify a master acceptance ID or complete a product release.

## Start here

- [Contribution guidance](CONTRIBUTING.md) and the [branch-to-review procedure](standards/contribution-workflow.md)
- [Acceptance and evidence rules](standards/acceptance-evidence.md), [evidence record](templates/evidence-record.md), and [backlog audit](templates/backlog-audit.md)
- [Source-of-truth and cross-repository links](standards/architecture-linking.md)
- [Release and version guidance](standards/releases-versioning.md) and [release record](templates/release-record.md)
- [Label planning](standards/labels-planning.md)
- [Agent contributor guidance](standards/agent-contributors.md) and this repository's [AGENTS.md](AGENTS.md)
- [Security and secret handling](standards/security-secret-handling.md); the proposed public reporting policy remains at [SECURITY.pending.md](community/SECURITY.pending.md)
- [Reusable workflow design](automation-design/reusable-workflows.md) and the deliberate [repository bootstrap checklist](adoption/repository-bootstrap.md)

## Architecture and evidence ownership

The [local ownership view](docs/architecture/OWNERSHIP.md) defines this repository's documentation responsibility. The [local acceptance view](docs/architecture/ACCEPTANCE.md) selects criteria but is not the master tracker.

Canonical architecture and the implementation plan live in getticketstub.com. Canonical schemas live in shared-contracts. Master acceptance state and evidence records live in integration-evals. Each repository owns its local implementation instructions, checks, and adoption record. See the [source registry](standards/architecture-linking.md) for immutable inspected references and link rules.

## Installation boundaries

A public organization .github repository may provide supported default community-health files when a repository has no local equivalent. GitHub displays those defaults; it does not copy them into clones. Local files take precedence. Agent instructions, CODEOWNERS, licenses, workflow callers, and repository settings need deliberate local decisions. A private .github repository is not a supported source for public organization community-health defaults.

Use the [bootstrap record](templates/adoption-record.md) to capture source revision, destination revision, applicability, verification evidence, deviations, and blockers. Do not report organization-wide adoption from a single repository's result.

## Current unresolved acceptance

- GH-07 security reporting remains blocked until a maintainer confirms the private destination and responsible role. No contact or response time is supplied here.
- GH-06 platform evidence remains pending: the local fixture exercises the same helper and workflow inputs/outputs, but it is not a GitHub-hosted run and proves neither platform execution nor private-workflow secret isolation.
- GH-03-I security-form chooser/routing preview remains pending with the reporting route.
- UI chooser/preview review, independent review, default-branch installation, and any per-repository adoption remain for their authorized owners.
