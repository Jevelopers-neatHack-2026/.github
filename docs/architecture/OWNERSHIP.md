# .github ownership and scope

**Repository status:** Public on GitHub, observed 2026-10-12 through repository metadata.

**Owner role:** Finance and reliability is the accountable role recorded for shared governance; a named ongoing maintainer assignment is not confirmed here.

**Delivery state:** The repository contains maintained guidance, published source templates, adoption records, and a local reusable-workflow fixture. Their presence does not establish destination adoption, product acceptance, configured settings, or hosted workflow execution.

## Responsibility

Maintain shared contribution and issue conventions, agent guidance, acceptance/evidence practices, architecture links, release and label guidance, security handling, workflow examples, and adoption records. Keep each policy tied to its owner and distinguish central guidance from implementation in another repository.

This repository has a real automation-design test suite and a reusable-workflow documentation starter, examples, and local fixture. The fixture executes the workflow's embedded checker locally. The repository has no root .github/workflows installation, and the starter has no verified GitHub-hosted run. A copied starter or example caller becomes configured only after an adopting repository installs it and verifies its own settings and run.

## Publication and adoption boundaries

GitHub currently reports this repository as public. Supported community-health files can serve as organization defaults when a destination lacks a local equivalent; destination-local files take precedence and inherited content is not copied into a clone. This does not install AGENTS.md, CODEOWNERS, a workflow caller, branch protection, or other repository or Actions settings. Adoption and settings must be checked in each destination before describing them as active.

The five active issue forms and pull-request template are published source material. Blank issue submissions are disabled in the published chooser. The sixth security form remains a draft outside that chooser because no private reporting destination and responsible owner are confirmed. The security draft, pending policy, and public issue warning must not be described as a private reporting route. See [issue-form guidance](../../templates/issue-forms.md) and [security handling](../../standards/security-secret-handling.md).

## Architecture and decision ownership

The maintained cross-repository view is the getticketstub.com [current architecture and integration state](https://github.com/Jevelopers-neatHack-2026/getticketstub.com/blob/main/docs/architecture/CURRENT-STATE.md), dependent on companion PR [#117](https://github.com/Jevelopers-neatHack-2026/getticketstub.com/pull/117) merging first. The immutable [architecture kit v1.0](https://github.com/Jevelopers-neatHack-2026/getticketstub.com/blob/7f59d33922a0585205547d490b288b49eed32419/docs/architecture-kit/v1.0/docs/architecture.md) remains design intent, not a current implementation inventory. The [shared-contracts catalog](https://github.com/Jevelopers-neatHack-2026/shared-contracts/blob/main/docs/contract-catalog.md) owns contract definitions. The [integration-evals master checklist](https://github.com/Jevelopers-neatHack-2026/integration-evals/blob/main/planning/acceptance-checklist.md) owns cross-repository acceptance status. Each destination repository owns its own behavior, local instructions, configuration, releases, and acceptance evidence.

Use the [architecture-linking standard](../../standards/architecture-linking.md) for source precedence and immutable evidence. Use the [local acceptance view](ACCEPTANCE.md) only to find criteria relevant to this repository; it cannot change their master status. A guidance update, local fixture pass, or source link does not prove integration or acceptance.

## Maintained records

- [Current status and scope boundaries](../status.md) distinguishes the latest governance disposition from dated historical evidence.
- [Adoption inventory and register](../../adoption/governance-inventory.md) records its dated 2026-10-10, 14-repository snapshot; it is not a current organization-wide count.
- [Governance release assessment](../../adoption/governance-release-record.md) preserves the dated partial/blocked assessment and later scope reconciliation.
- [Documentation index](../documentation/INDEX.md) routes readers to the maintained standards, templates, local views, and canonical external owners.

Master acceptance IDs, criteria, and contributor requirements remain owned by their existing maintainers. This file does not alter them or claim that the .github governance gate has been accepted.
