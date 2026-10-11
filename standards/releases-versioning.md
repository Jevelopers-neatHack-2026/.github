# Release and version guidance

This standard separates the revision of shared governance documents, each repository's own package/release version, shared contract versions, and an assembled product release. It does not publish a release, set tags, select a license, or make a version decision for another repository.

## Ownership and naming

Each repository's maintainers own its release cadence, versioning policy, publication authority, licensing decision, tags, and rollback. Record the actual decision in that repository. The shared-contracts catalog owns schema compatibility: each contract has an explicit schema version, and incompatible changes require a new supported version plus producer/consumer review. Do not assign one product-wide version to every component.

Where a repository has not selected a version policy, SemVer-style vMAJOR.MINOR.PATCH and prerelease identifiers such as -rc.1 are a proposal for owner review, not an existing rule. The repository owner must record whether tags/releases are used and who may publish. No current release or tested manifest is implied here.

Keep these identities separate:

- Governance policy pack 1.1.0 labels this documentation package; it is not a product release or an installed workflow version.
- A repository commit identifies source content. A full SHA is immutable; main and tags can move unless the tag is protected and verified.
- A contract version is owned by shared-contracts and recorded by each producer/consumer.
- An assembled product release is owned by integration-evals and its release owner, and records every selected component.

## Release record and gates

Use templates/release-record.md. Before declaring a release ready, confirm:

- exact component and repository SHAs, contract versions, runtime and dependency lockfile revisions;
- artifact names and digests, migration set, feature flags, environment and provider mode per component;
- commands/procedures, expected and actual results, evidence links/hashes, reviewer roles and dates;
- compatibility and affected-consumer acknowledgment, known limitations, and recovery/rollback steps tied to a validated artifact;
- authorization for publication and current release/tag/workflow settings.

A planning repository map, moving branch, missing artifact/command record, skipped mandatory test, or mock-only result for a live-required criterion blocks the corresponding release claim. Unknown cost or billing remains unknown. A release record template is not a tested manifest.

When a relevant contract, component, runtime, configuration, or fixture changes, mark prior evidence stale and rerun the affected gate. Preserve the old record as superseded. Roll back only to an artifact and data-recovery procedure that were actually validated; describe irreversible migration recovery explicitly.

## Clearly hypothetical examples

These examples illustrate shape only; they are not tested releases.

- Governance revision example: source commit 28f67d2 is the fixed implementation starting revision for policy pack 1.1.0. The final governance document commit is not known until the work is committed. This identifies the starting source only; it does not claim a release or merge.
- Hypothetical multi-repository product manifest: component SHAs = UNKNOWN until pinned; shared contract version = UNKNOWN until the catalog owner confirms it; artifact digest = UNKNOWN until built; integrated command/result = NOT RUN; provider mode = mock/sandbox/live per component after inspection; rollback target = UNKNOWN until a specific validated artifact exists. The product release remains blocked.

The source catalog and central plan are linked from standards/architecture-linking.md. Do not duplicate their records in this repository.
