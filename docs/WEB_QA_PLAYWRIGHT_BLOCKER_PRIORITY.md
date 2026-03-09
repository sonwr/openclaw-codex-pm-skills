# Web QA Playwright blocker priority

Use this note when a strict-plus replay run is blocked and you need one deterministic repair order.

## Repair order

1. **Target reference blockers first**
   - Missing `ref=<id>`
   - Reused checkpoint target refs
   - Why first: replay cannot bind actions reliably without stable targets.

2. **Artifact evidence blockers second**
   - Missing checkpoint artifact paths
   - Reused artifact refs
   - Why second: you can replay the step, but signoff stays weak without evidence.

3. **Chronology blockers third**
   - Missing timestamps
   - Non-monotonic checkpoint timestamps
   - Why third: ordering drift matters after selector/evidence stability exists.

4. **State consistency blockers fourth**
   - Checklist/log PASS-FAIL mismatch
   - Failure breakdown summary drift
   - Why fourth: these are interpretation-layer blockers after the run is structurally replayable.

5. **Owner/handoff blockers last**
   - Missing recovery owner
   - Missing next-action failed-check refs
   - Why last: fix the runnable artifact first, then polish the recovery lane.

## Quick operator rule

Repair exactly one blocker class at a time, rerun the isolated fixture that proves the class, then rerun the canonical PASS fixture before updating docs or CI expectations.

## Related docs

- `docs/WEB_QA_PLAYWRIGHT_REPAIR_SEQUENCE_CARD.md`
- `docs/PLAYWRIGHT_INTERACTIVE_EXECUTION_PRINCIPLES.md`
- `docs/WEB_QA_PLAYWRIGHT_STABILITY_CHECKLIST.md`
- `docs/WEB_QA_PLAYWRIGHT_FAILURE_HANDOFF.md`
- `docs/WEB_QA_PLAYWRIGHT_SECTION_HOTSPOT_REPAIR.md`
