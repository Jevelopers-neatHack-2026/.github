# Proposed label taxonomy and adoption

The names below are a proposed vocabulary for review. The live label set can differ by repository. Labels help people filter issues; they do not prove acceptance, ownership, verification, or dependency completion.

## Dimensions and cardinality

| Dimension | Proposed values | Rule |
|---|---|---|
| Priority | priority:P0, priority:P1, priority:P2, or Production | One priority value. P0 is demonstration/financial integrity, P1 is next useful expansion, and Production means required before live commerce. Production is a gate class, not a lower urgency value. Preserve the central checklist's meaning. |
| Type | type:feature, type:bug, type:integration, type:decision, type:security, type:audit, type:docs, type:epic, type:gate | One primary type. A security decision is type:security if disclosure/safety is the subject; explain its decision work in the body. Do not add duplicate primary types. |
| Area | area:<repository-or-subsystem>, including area:governance | One or more only when multiple owners genuinely need to act. Use repository names or an agreed subsystem vocabulary. |
| Dependency state | state:blocked or state:ready | At most one. Ready means no recorded prerequisite blocks the scoped work; it does not mean tests passed. |
| Required-for-v1 | required:v1 or not required / unknown in the issue body | This dimension is independent of priority and readiness. Only apply a label after the repository's agreed vocabulary exists. |

If a required label is unavailable, keep the equivalent value in issue-body metadata. Do not use a state label to imply verified. Keep a concrete dependency URL, expected artifact, unblock condition, owner role, and status date in the body.

## Existing .github label mapping

The captured target set had ten existing labels. Preserve their current meanings; do not rename or delete them as part of this proposal.

| Existing label | Relationship to proposal |
|---|---|
| accessibility | Keep as an independent accessibility flag; it is not a priority/type/area value. |
| bug | Existing type alias. If a reviewed destination adopts type:bug, map bug to it without renaming or automatically duplicating. |
| documentation | Existing type alias for type:docs; retain existing usage while the destination decides whether to add a new name. |
| enhancement | Existing type alias for type:feature; retain existing usage while the destination decides whether to add a new name. |
| duplicate | Disposition label; preserve. |
| good first issue | Contributor invitation; preserve. |
| help wanted | Contributor invitation; preserve. |
| invalid | Disposition label; preserve. |
| question | Discussion/request-for-information label; preserve. |
| wontfix | Disposition label; preserve. |

Do not create a second label merely to make templates look consistent. The five active issue forms intentionally omit automatic labels; their bodies remain useful without permission or a label rollout.

Examples, with names still proposed:

- A blocked P0 integration: priority:P0, type:integration, area:shared-contracts, state:blocked, required:v1. The body names the producer, consumer, expected fixture/version, owner roles, and unblock condition.
- A P1 required-v1 documentation leaf: priority:P1, type:docs, area:governance, state:ready, required:v1. Required-for-v1 stays separate from readiness.
- A security reporting-route decision: priority:P0, type:security, area:governance, state:blocked, required:v1. The body states that the private route and owner are unconfirmed; no public contact is fabricated.

## Per-repository application

1. Inventory labels and permissions in the destination repository. Record the repository URL, date, current labels, and who can manage them.
2. Compare desired names to existing aliases and meanings. Preview the proposed change as a table; do not rename/delete unrelated labels or infer organization-wide state.
3. If authorized and permitted, create only missing approved names. If a name exists with different meaning, stop and ask its maintainer. If permission is missing, record desired/not applied and request the local owner.
4. Verify the resulting set in that repository and record desired/applied/verified separately with the observation date and evidence. Repeat per destination; one successful repository operation proves nothing about another.
5. Use issue-body metadata when labels are absent. Templates reference labels only after the destination owner confirms they exist.

The source label snapshot was captured at the historical baseline. Recheck live labels before any adoption; this document does not apply them.
