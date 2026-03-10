# Web QA Playwright signoff owner alias check

Use this quick check when a report passes validation but the owner wording still feels ambiguous.

## Goal

Make the signoff line name the same repair owner across:

- `failed_checks[].recovery_owner`
- any hotspot owner summary
- the final signoff or handoff sentence

## Quick check

1. Pick the owner label that appears most directly in failed-check metadata.
2. Reuse that exact owner label in the signoff line.
3. Avoid switching between role synonyms such as `qa`, `test-owner`, and `frontend-owner` unless the artifact truly distinguishes them.
4. If multiple labels exist, call that out as an owner-routing gap instead of flattening them into one owner.

## Good signoff wording

- `Validation passed, but checkout lane failures still route to frontend-owner for selector repair before rerun.`
- `Validation passed; owner coverage is split between qa and backend-owner, so keep the handoff blocked until routing is normalized.`

## Bad signoff wording

- `Validation passed, hand off to the team.`
- `Validation passed, QA should probably look.`

## Use this when

Use this note after `docs/WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_HANDOFF.md` when the artifact is clean enough to hand off, but the owner wording still risks drift between JSON metadata and the final sentence.
