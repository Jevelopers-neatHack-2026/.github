# Documentation index

This index routes maintainers and contributors to the source that owns each question. It does not replace repository-specific instructions or the authoritative source linked below.

## Cross-repository architecture and status

- This audit’s [dated findings](AUDIT-2026-10-12.md) explain scope, validation, limitations, and the independent-review routing blocker. The companion [per-file inventory](inventory.json) carries source revisions, accuracy, completeness, risk priority, exclusions, and remediation.

- [Current architecture and integration state](https://github.com/Jevelopers-neatHack-2026/getticketstub.com/blob/main/docs/architecture/CURRENT-STATE.md) is the maintained source for observed architecture and cross-repository connections. It depends on getticketstub.com PR [#117](https://github.com/Jevelopers-neatHack-2026/getticketstub.com/pull/117) merging first; until then, treat the target as an announced companion, not a published main-branch source.
- [Architecture kit v1.0](https://github.com/Jevelopers-neatHack-2026/getticketstub.com/blob/7f59d33922a0585205547d490b288b49eed32419/docs/architecture-kit/v1.0/docs/architecture.md) is the dated design-intent snapshot. It is not a current implementation inventory.
- The [maintained contract catalog](https://github.com/Jevelopers-neatHack-2026/shared-contracts/blob/main/docs/contract-catalog.md) owns cross-repository contract definitions and version decisions.
- The [master acceptance checklist](https://github.com/Jevelopers-neatHack-2026/integration-evals/blob/main/planning/acceptance-checklist.md), JSON tracker, and evidence index in integration-evals own cross-repository acceptance state and evidence records.
- The current product work sequence is in the [getticketstub.com implementation plan](https://github.com/Jevelopers-neatHack-2026/getticketstub.com/blob/main/docs/planning/implementation-plan.md). Planning links are not tested component pins.

## .github governance source

- [Ownership and scope](../architecture/OWNERSHIP.md) describes what this repository maintains and what GitHub defaults or workflow examples do not install.
- [Local acceptance view](../architecture/ACCEPTANCE.md) selects relevant master IDs without changing their owner or state.
- [Current and historical governance status](../status.md) carries dated scope decisions and implementation/installation limits.
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
| Review the reusable workflow starter | [Reusable workflow guidance](../../automation-design/reusable-workflows.md) | [Starter](../../workflow-templates/docs-check.yml), [caller example](../../automation-design/examples/caller/.github/workflows/docs-check.yml), and [local fixture](../../automation-design/fixtures/reusable-workflow/docs/reference.md) |

## Publication boundaries

The five issue forms and pull-request template are published source material in this public repository; destination overrides and adoption remain destination-specific. The security form is inactive and the private reporting route is unconfirmed. Workflow examples and templates are not installed callers. See [reusable workflow guidance](../../automation-design/reusable-workflows.md) and [issue-form guidance](../../templates/issue-forms.md) before describing their status.
