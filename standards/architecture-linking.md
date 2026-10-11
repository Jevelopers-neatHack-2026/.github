# Architecture, ownership, and evidence links

This registry keeps one authoritative source for each kind of decision. It is a navigation aid, not a lockfile and not evidence that a linked behavior exists.

## Source-of-truth registry

| Subject | Canonical owner and source | Local view | Update rule |
|---|---|---|---|
| Product architecture and repository boundaries | [getticketstub.com architecture kit v1.0 at inspected commit 7f59d33](https://github.com/Jevelopers-neatHack-2026/getticketstub.com/blob/7f59d33922a0585205547d490b288b49eed32419/docs/architecture-kit/v1.0/docs/architecture.md) | Each repository's OWNERSHIP.md | Product architecture owner approves decisions; preserve versioned snapshots and record rationale |
| Implementation work packages | [Central implementation plan at inspected source commit 5a29864](https://github.com/Jevelopers-neatHack-2026/getticketstub.com/blob/5a2986454297dd6df97088a8fbde69adc771f7a0/docs/planning/implementation-plan.md) | Repository issues and local plans | Product owner maintains cross-repo sequence; the plan map is not tested component metadata |
| Shared schemas and compatibility | [shared-contracts catalog at inspected commit c4caacc](https://github.com/Jevelopers-neatHack-2026/shared-contracts/blob/c4caaccc2ea63b273eeac17ed89af8ac64f6bbde/docs/contract-catalog.md) | Consumer/provider links to a catalog entry and version | shared-contracts owns definitions; affected producer and consumer roles review changes |
| Acceptance IDs, evidence, and integrated status | [integration-evals checklist at inspected commit ff1f6d2](https://github.com/Jevelopers-neatHack-2026/integration-evals/blob/ff1f6d2df816ebbff34742f51be728fcb5c28cb5/planning/acceptance-checklist.md), its [JSON tracker](https://github.com/Jevelopers-neatHack-2026/integration-evals/blob/ff1f6d2df816ebbff34742f51be728fcb5c28cb5/planning/acceptance-checklist.json), and [evidence index](https://github.com/Jevelopers-neatHack-2026/integration-evals/blob/ff1f6d2df816ebbff34742f51be728fcb5c28cb5/evidence/README.md) | This repository's docs/architecture/ACCEPTANCE.md selects relevant IDs | integration-evals owner changes authoritative state after evidence review |
| Shared governance guidance | this .github repository | Local copies/adaptations in destination repositories | Shared source maintains proposed guidance; each destination owner approves local use |
| Implementation, local settings, and agent instructions | The repository that owns the behavior or setting | Its local AGENTS.md, README, OWNERSHIP.md, tests, and settings | Owning maintainers decide and verify locally; links do not transfer ownership |

These commit references identify inspected source revisions, not promises that they remain the latest. Use branch links for navigation only. Use full immutable commit links for evidence. Recheck current sources before a new decision.

## Link conventions

- Within one repository, use relative Markdown links and stable headings. If a heading changes, update inbound links in the same change.
- Across repositories, link to the exact owner/repository/path and, for evidence, a full commit SHA. A main-branch URL is a convenience link and can move.
- A tested source revision belongs in the evidence or release record. Do not describe the central planning repository map as a tested lockfile.
- A repository may record its own release revision in release metadata; do not put a self-referential SHA into the manifest whose commit is being measured.
- Private repository links may be inaccessible to some readers. Record access as restricted or unavailable to that reader; do not call an inaccessible link broken or verified.

## Cross-repository handoff

Before marking a dependency ready, record the exact producer and consumer issue URLs, owner roles, expected artifact and version, tested source revision if one exists, unblock condition, current status date, and evidence needed for consumer acknowledgment. If the issue or revision is unknown, write unknown and assign the resolution to an owner role. Do not manufacture an issue number, contract version, commit, or reviewer.

Example source chain: repository ownership → implementation issue → shared-contracts entry/version → master acceptance ID → immutable evidence → local gate → integrated gate. The actual [shared-contracts gate issue #3](https://github.com/Jevelopers-neatHack-2026/shared-contracts/issues/3) and [integration-evals report issue #8](https://github.com/Jevelopers-neatHack-2026/integration-evals/issues/8) are inspected coordination references. Their links alone establish no completion or current status.

| Handoff field | Example record |
|---|---|
| Producer issue | Actual source link: shared-contracts issue #3 |
| Consumer/report issue | Actual source link: integration-evals issue #8 |
| Producer role / consumer role | Agent and research / Finance and reliability; confirm current assignments |
| Expected artifact/version | Catalog entry and explicit contract version; exact version remains to be confirmed by the owners |
| Producer revision and executed checks | Unknown until recorded against the producer's immutable revision |
| Consumer fixture and acknowledgment | Unknown until the consumer runs and reviews it |
| Unblock condition and date | Both owner roles record the accepted condition and date |
| Acceptance status | Remains with integration-evals; no status follows from this sample |

This example uses real inspected issue links and deliberately leaves unobserved values unknown. It is not a new issue or a completed handoff.

## Architecture and contract changes

For a behavior or schema change, write a decision record in the owning repository with context, options, tradeoffs, decision owner, affected producer/consumer roles, source revisions, compatibility, migration, and rollback. Update the maintained source first, then reverse links and local ownership/acceptance views. Retain immutable versioned snapshots when the architecture kit changes. Do not create a second canonical catalog or move state into this repository.

When guidance disagrees with an accepted local decision, preserve both source links, stop changes at the conflict boundary, and ask the owner of that decision. A code review may resolve a scoped implementation detail only when the authorized owner is clear.
