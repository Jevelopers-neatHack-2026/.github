# Documentation index

This index routes maintainers and contributors to the source that owns each question. It does not replace repository-specific instructions or the authoritative source linked below.

## Cross-repository architecture and status

- This audit’s [dated findings](AUDIT-2026-10-12.md) explain scope, source authority, outcomes, validation, limitations, and unresolved owner decisions. The companion [per-file inventory](inventory.json) is version 1.1 and supersedes the v1 candidate metadata while preserving v1 in Git history. The frozen inventory covers 16 repositories in 550 rows (547 individual and 3 grouped) across 1,185 classified paths, with zero missing paths. Aggregate navigation checked 389 non-README documents and 1,628 links with no findings; all 6 Mermaid diagrams parsed. The audit records the remaining structured-data, schema/reference, source-pin, scope, and repository-local results. PR #29, archived landing-page PR #37, and marketing-material PR #32 remain open for their stated reviewer, access, and package-owner blockers.
- [Current architecture and integration state](https://github.com/Jevelopers-neatHack-2026/getticketstub.com/blob/main/docs/architecture/CURRENT-STATE.md) is the maintained source for observed architecture and cross-repository connections. It was published by getticketstub.com PR [#117](https://github.com/Jevelopers-neatHack-2026/getticketstub.com/pull/117) and verified on main at `aec83af65ee75be80246d88782c8f8ce00a10c31`; its canonical file blob is `31d199072287b80237a9b7c65deed2c434a188de` (SHA-256 `e7d05bc9827b0a7aa9daeee1a2021692b2c683550b9000e070f5234876f11f29`). The page records source-state observations and does not establish product acceptance or deployment.
- [Architecture kit v1.0](https://github.com/Jevelopers-neatHack-2026/getticketstub.com/blob/7f59d33922a0585205547d490b288b49eed32419/docs/architecture-kit/v1.0/docs/architecture.md) is the dated design-intent snapshot. It is not a current implementation inventory.
- The [maintained contract catalog](https://github.com/Jevelopers-neatHack-2026/shared-contracts/blob/main/docs/contract-catalog.md) owns cross-repository contract definitions and version decisions.
- The [master acceptance checklist](https://github.com/Jevelopers-neatHack-2026/integration-evals/blob/main/planning/acceptance-checklist.md), JSON tracker, and evidence index in integration-evals own cross-repository acceptance state and evidence records. The audited main revision `13bde39399a09d4a14cc97d72cd769b51da83e00` contains 47 criteria (44 planned; SPN-01, SPN-02, SPN-03 verified); use the current master tracker for later decisions.
- The current product work sequence is in the [getticketstub.com implementation plan](https://github.com/Jevelopers-neatHack-2026/getticketstub.com/blob/main/docs/planning/implementation-plan.md). Planning links are not tested component pins.

## `.github` governance source

- [Ownership and scope](../architecture/OWNERSHIP.md) describes this repository’s responsibilities, the shared-default boundaries, and the separate destination-owner decisions.
- [Local acceptance view](../architecture/ACCEPTANCE.md) selects relevant master IDs without changing their owner or state.
- [Current and historical governance status](../status.md) distinguishes the pre-PR-28 adoption snapshot from the current root workflow source and its recorded main run.
- The [2026-10-12 governance status addendum](../../adoption/observations/governance-status-addendum-2026-10-12.md) and [machine-readable adoption observation](../../adoption/observations/organization-adoption-2026-10-12.json) retain their dated, pinned evidence; the observation predates PR #28 and does not establish later consumer adoption.
- The [governance lifecycle](../../standards/governance-lifecycle.md) defines proposed, published, available, adopted, enforced, and retired states without configuring controls for a destination.
- [Architecture and evidence links](../../standards/architecture-linking.md) explains source precedence, SHA pins, and cross-repository handoffs.

## Working guidance and records

| Task | Start here | Supporting sources |
|---|---|---|
| Review a documentation change | [Documentation guidance](../../standards/documentation.md) | [Contribution workflow](../../standards/contribution-workflow.md), [pull-request template](../../.github/pull_request_template.md) |
| Record a test or acceptance result | [Acceptance and evidence](../../standards/acceptance-evidence.md) | [Evidence-record template](../../templates/evidence-record.md), [backlog-audit template](../../templates/backlog-audit.md) |
| Change an API or shared contract | [Architecture and evidence links](../../standards/architecture-linking.md) | Contract catalog and owner instructions linked above |
| Set up a destination repository | [Bootstrap guidance](../../adoption/repository-bootstrap.md) | [Adoption-record template](../../templates/adoption-record.md) and its [new-repository example](../../templates/examples/adoption-new-repository.md) or [existing-private example](../../templates/examples/adoption-existing-private.md) |
| Handle agent instructions | [Agent guidance](../../standards/agent-contributors.md) | Destination repository’s own AGENTS.md remains authoritative |
| Prepare a release record | [Release and version guidance](../../standards/releases-versioning.md) | [Release-record template](../../templates/release-record.md) |
| Review labels | [Label planning](../../standards/labels-planning.md) | Labels are configured per repository; this page does not create them |
| Handle secrets or an unsafe URL/asset | [Security handling guidance](../../standards/security-secret-handling.md) | The security contact/form remain pending in [the retained draft](../../community/SECURITY.pending.md) |
| Review workflow source or adoption | [Reusable workflow guidance](../../automation-design/reusable-workflows.md) | Root source is in `.github/workflows/`; [starter](../../workflow-templates/docs-check.yml), [caller example](../../automation-design/examples/caller/.github/workflows/docs-check.yml), and [local fixture](../../automation-design/fixtures/reusable-workflow/docs/reference.md) are separate |

## Publication and adoption boundaries

Five issue forms and the pull-request template are published source material in this public repository. The security form remains inactive because the private reporting route and responsible owner are unconfirmed. PR #28 added the root reusable workflow and caller; its post-merge receipt records a successful run on `.github` main. That run does not establish required-check enforcement, downstream adoption, or destination-specific permissions. Workflow examples and templates remain distinct from installed callers. See [reusable workflow guidance](../../automation-design/reusable-workflows.md), [issue-form guidance](../../templates/issue-forms.md), and the [dated adoption observation](../../adoption/observations/organization-adoption-2026-10-12.json) before describing their status.
