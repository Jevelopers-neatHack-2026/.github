# Documentation guidance

This page helps maintainers keep shared governance and implementation documentation accurate. It does not add a new acceptance gate, mandatory CI check, organization-wide contributor obligation, or authority to change another repository. A repository’s local instructions, accepted design, and named decision owner take precedence. If sources conflict, preserve the boundary and ask the owner identified by the applicable local guidance.

## Audience, owner, and source

Write for a named reader: for example, a contributor setting up a local checkout, an operator restoring state, an API consumer, a maintainer reviewing a release, or an agent following repository instructions. State the owning repository or owner role when the decision is cross-repository; a role does not establish a named assignee, CODEOWNERS entry, or approval.

Keep one canonical source for each decision. Link to the repository that owns the runtime behavior, schema, contract, setting, acceptance status, or policy. A local summary may explain how to find or use that source, but must not become a competing authority. When two documents serve different purposes, name the boundary instead of copying an unqualified claim.

For product naming and terminology, use the [brand-kit voice guide](https://github.com/Jevelopers-neatHack-2026/brand-kit/blob/main/docs/voice.md) and [source-of-truth index](https://github.com/Jevelopers-neatHack-2026/brand-kit/blob/main/docs/source-of-truth.md) as navigation to their owning decisions. Prefer the product spelling “TicketStub” and exact repository identifiers when naming components. The voice guide labels its examples illustrative and unapproved; do not turn them into product, price, capability, identity, or asset approval. Brand ratification, public claims and asset provenance remain with their recorded brand owners.

Use a default-branch link for current navigation and a full immutable commit SHA for dated evidence. For a verified claim, identify the source revision, relevant file or interface, inspection or test date, actual command/result when applicable, and material limitations. A planning map is not a dependency lock; a link is not a test; a merged guidance change is not implementation acceptance. Use “unknown” when an owner, version, run, cost, approval, or setting was not established.

## Capability language

Choose the description that matches the evidence at the cited source revision. These states describe a capability; they do not replace a repository’s criterion state or authorize its acceptance owner to update a master tracker.

| State | Use when | Keep explicit |
|---|---|---|
| **Implemented and verified** | The owning implementation exists and the relevant check ran successfully on the identified revision. | The exact scope, revision, procedure, result, environment and limits. A fixture proves only the behavior it exercised. |
| **Implemented but not integrated** | A component has the implementation or consumer-facing interface, but the intended application or system does not call, import, deploy, or accept it. | The observed boundary and the missing consumer, deployment, or owner evidence. |
| **Partial** | Only a subset or one mode of the intended capability exists or has been checked. | Which path works, which remains absent, and whether the result is local, mock, sandbox, or live. |
| **Awaiting acceptance or external approval** | Source and possibly test evidence exist, but a required owner decision, external account/access approval, policy choice, or platform observation is pending. | The decision owner role and exact evidence or approval still required. Do not present a technical pass as acceptance. |
| **Planned** | A roadmap, issue, design, or proposed interface describes future work without implementation evidence. | The plan source and any unresolved design, owner, dependency, or approval. |
| **Deprecated or unsupported** | The owner has ended support or states that the capability is not available. | The decision source/date and a replacement or migration path when one exists; do not silently imply compatibility. |

Keep project acceptance state, command outcome, artifact origin, and execution/provider mode separate. Use the owning repository’s acceptance source for authoritative status. A mock or offline check is not a sandbox or live run. A recorded artifact retains its original provenance even when a later replay uses offline mode.

## Risk of a documentation defect

Use P0–P3 here only to describe the risk caused by an inaccurate or missing document. This scale is separate from product priority, acceptance priority, implementation severity, or whether work is required for a release.

| Documentation risk | Typical examples |
|---|---|
| **P0 — Critical** | Instructions could expose credentials/customer data, authorize an unintended payment/provider call, bypass an authority boundary, destroy data, or make a consequential recovery action unsafe. |
| **P1 — High** | A wrong API method, retry/idempotency rule, authentication requirement, deployment prerequisite, restore procedure, or security boundary could cause failed or unsafe operation. Blocking developer setup or missing deployment instructions also belong here. |
| **P2 — Medium** | Incomplete explanations, examples, navigation, configuration, or maintenance information makes a common task less reliable when the gap does not block developer setup or deployment. |
| **P3 — Low** | Wording, layout, or a non-blocking reference makes information harder to find without changing a decision or operation. |

When noting a gap, say whether it is a documentation defect, an implementation gap, an external approval, or an unknown. Improving text does not close an implementation gap.

## API, configuration, and operational instructions

Derive API descriptions from the owning route, exported interface, schema, tests, and versioned contract. Record supported methods, path, authentication/authorization, required inputs, validation, response/error behavior, side effects, and compatibility only where those details are verified. Name the source file and revision. Keep a repository-owned convenience reference clearly subordinate to the canonical contract.

For configuration and setup, verify names, defaults, valid values, required/runtime versions, entry points, filesystem or service assumptions, and whether a key merely enables a path or also triggers an external effect. Distinguish a documented example from a configured deployment. For deployment and recovery instructions, explain prerequisites, data durability, safe stopping points, backup/restore order, failure recovery, and the owner-controlled approval required for destructive or externally visible steps. Never infer production readiness from a local command or a green mock.

For retries and idempotency, cite the actual state transition, deduplication key, timeout/lease behavior, and tests that exercise duplicate, timeout, or partial-failure cases. If a retry could create duplicate money movement, external submission, or customer communication, say exactly what is and is not safe to repeat. If evidence is absent, state that the policy is unknown or unsupported; do not invent a plausible rule.

## Examples, schemas, and generated material

Prefer the canonical schema or contract from its owner. Label examples as synthetic, fixture-derived, sandbox-derived, recorded, or live when known; include the origin revision and avoid real credentials or customer data. Show whether an example is executable and how it was checked. A parsed JSON/YAML file has syntax evidence only. A schema meta-check or resolved reference does not prove semantic validity, fixture behavior, API availability, consumer adoption, or acceptance.

Identify generated files and their source generator. Update the maintained source and regenerate only when that is in scope; do not edit a generated snapshot as if it were the canonical source. For vendored or captured historical material, retain provenance and direct corrections to its owner. Do not use sample paths or placeholder names as if they exist in a repository.

## Links, headings, and diagrams

Use relative Markdown links within one repository. For cross-repository navigation, identify the repository and owning path; use a full SHA link when the text makes a dated evidence claim. Mark a destination that depends on an unmerged source change and state the merge dependency. A private page that cannot be read by every audience is access-restricted, not necessarily broken.

Keep headings stable when referenced. Check local file paths and anchors after changing a page; separately inspect cross-repository links through authorized access where the claim depends on them. Exclude website routes, generated routing, private permissions, and external-service behavior from a local link check unless a specific validator covers them. Validate Mermaid syntax with the available parser and compare the diagram with the described source behavior. Do not treat a diagram as an independent source of truth.

## Historical and maintained records

Date and pin immutable plans, architecture snapshots, incident notes, and evidence records. Label them historical when newer current guidance exists, preserve their original findings, and link the maintained successor. Do not rewrite a dated record to make it appear as if it described later code or decisions. Current indexes should lead to the maintained source and distinguish design intent from observed implementation.

## Validation and maintenance

Record only commands actually run. Include relevant tool/runtime versions, exact source revision, input or fixture identity, expected and actual result, execution/provider mode, date, skips, and limitations. Run the repository’s existing checks that directly cover the edit when practical; do not invent or claim hosted workflow, platform setting, deployment, private-route, provider, or consumer evidence from local tests. Keep test plans distinct from results and preserve failures or skips.

Revisit affected documentation when an API, schema, config default, source pin, security boundary, workflow interface, deployment path, recovery procedure, owner decision, acceptance record, policy pack, or adoption state changes. Update the maintained source first, then its indexes and reverse links. A source pin ages when the relevant source changes; mark it historical and refresh evidence only when the claim still matters. Ask the decision owner when the change would alter acceptance, access, policy, licensing, spending, or another repository’s contract.

This standard describes a careful documentation practice. It does not install automation, make a local file universal, create security reporting access, select an organization policy, or satisfy any acceptance criterion by itself.
