# Web QA Playwright section hotspot repair

Use this note when strict-plus replay metadata shows one or more blocked sections as the current hotspot.

## Goal

Repair the hottest blocked section first without widening scope too early.

## Deterministic loop

1. Freeze the same profile/preset, URL, account, viewport, and artifact naming before rerunning.
2. Read the hotspot keys from JSON (`effective_replay_readiness_hotspot_primary_blocker`, `effective_replay_readiness_hotspot_primary_blocker_by_section`).
3. Pick exactly one section (`functional`, `visual`, or `off_happy`) and one blocker class to repair first.
4. Restore stable target refs before artifact/evidence cleanup when both are missing.
5. Rerun only the affected section lane and confirm the blocker count moves down.
6. Re-run the canonical PASS fixture before updating docs or merge guidance.

## Repair order by blocker

- `missing_target_refs` -> restore stable refs and keep them unique.
- `incomplete_evidence_refs` -> attach screenshot/log/trace paths on the same checkpoint line.
- `missing_timestamps` -> restore ISO-8601 timestamps before checking chronology.
- `status_inconsistency` -> align checklist and execution-log PASS/FAIL tokens.

## Operator handoff sentence

Use a copyable handoff like:

> Repair `visual` / `missing_target_refs` first, rerun only that lane, then confirm the hotspot blocker summary changes before widening replay scope.
