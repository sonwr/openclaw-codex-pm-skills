# Web QA Playwright repair sequence card

Use this compact card when a strict-plus report fails and you need one reproducible next move.

## Step-by-step order

1. **Lock selectors first**
   - Repair missing or reused `ref=<id>` values.
   - Why: interactive replay is unstable until the target binding is deterministic.

2. **Restore evidence second**
   - Repair missing checkpoint artifact paths or reused artifact refs.
   - Why: the run may execute, but signoff still stays weak without durable evidence.

3. **Fix chronology third**
   - Repair missing timestamps and non-monotonic checkpoint time order.
   - Why: replay and evidence should be stable before you normalize execution order.

4. **Align report state fourth**
   - Repair PASS/FAIL mismatches between logs, checklists, and failure summaries.
   - Why: interpretation drift matters after the raw replay artifact is structurally sound.

5. **Finish owner handoff last**
   - Add missing recovery owner, next-action check refs, and replay follow-up notes.
   - Why: owner routing is only useful once the failure is reproducible.

## Recovery rule

Repair one blocker class, rerun the smallest proving fixture, then rerun the canonical PASS fixture before updating docs or CI expectations.

## Related docs

- `docs/WEB_QA_PLAYWRIGHT_BLOCKER_PRIORITY.md`
- `docs/WEB_QA_PLAYWRIGHT_PRECHECK.md`
- `docs/PLAYWRIGHT_INTERACTIVE_EXECUTION_PRINCIPLES.md`
- `docs/WEB_QA_PLAYWRIGHT_SECTION_RERUN_CHECKLIST.md`
