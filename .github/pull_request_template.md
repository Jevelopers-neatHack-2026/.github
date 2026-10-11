<!--
Jevelopers neatHack 2026 program pull request template (GH-03-P).
Guidance: https://github.com/Jevelopers-neatHack-2026/.github/blob/main/templates/README.md
Replace every <placeholder>. Write "None" or "N/A — <reason>" instead of deleting a section.
Checkboxes are author claims for the reviewer to check. They do not prove that reviews,
branch protection, required checks or provider calls are configured or happened.
Never paste secrets, tokens, signed URLs, customer data or exploit details here.
-->

## Summary
<2–4 sentences: what changed and why.>

## Linked issues
<!-- Use "Closes owner/repo#N" only for issues this PR fully completes (all acceptance criteria met).
     Use "Refs owner/repo#M" for partial work, parents/epics and release gates. Release gates never close from a PR. -->
Closes <owner/repo#N> · Refs <owner/repo#M>

## Scope / Non-goals
- **In scope:** <what this PR does>
- **Non-goals:** <what it deliberately does not do>

## Changes
- <grouped, file/area-level bullets>

## Acceptance criteria → evidence
<!-- One line per criterion from the linked issue. Tick only criteria with evidence attached.
     Leave unmet criteria unticked and say why. Include master acceptance IDs (e.g. CON-01) or "N/A — <reason>". -->
- [ ] <criterion from issue> — <test name / command output / screenshot path>
- **Acceptance IDs:** <IDs from integration-evals/planning/acceptance-checklist.md, or N/A — reason>

## Verification
<!-- Separate what was actually run from what is only planned. Include the tested commit SHA. -->
- **Tested revision:** <full commit SHA>
- **Executed:** <exact commands and their result; CI run link>
- **Planned / not run:** <checks not executed and why, or "None">
- **Provider mode:** <mock | sandbox | live | N/A — reason> (list each component separately when mixed)

## Dependencies / blockers
- **Blocked by:** <owner/repo#N, or None>
- **Blocks:** <owner/repo#N, or None>

## Cross-repo impact
<!-- Contracts/versions consumed or published, affected producers/consumers and their acknowledgement; "None" if none. -->
<None | details>

## Security & provenance
- [ ] No secrets, tokens, credentials, signed URLs or customer data in the diff, fixtures, logs or screenshots.
- [ ] New dependencies and assets are pinned and their license/provenance is recorded (or N/A).
- [ ] Paid or live provider use was authorized with a stated budget, or none occurred.

## Risk & rollback
<Risk level, what could break, how to revert.>
