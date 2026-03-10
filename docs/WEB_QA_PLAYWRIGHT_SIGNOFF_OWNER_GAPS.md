# WEB_QA_PLAYWRIGHT_SIGNOFF_OWNER_GAPS

Use this note when a strict-plus report is validation-clean but still weak for handoff because owner coverage is incomplete.

## Quick read order

1. Check `missing_signoff_fields` and `signoff_field_coverage_rate`.
2. Check `next_action_failed_check_gap_count` and `next_action_failed_check_gap_rate_by_classification`.
3. Check `unresolved_failed_check_recovery_owners` and `failed_check_ids_by_recovery_owner`.
4. If ownership is still partial, keep the run as inspection-ready instead of handoff-ready.

## Copy-ready handoff question

- Which failed checks still lack a clear owner?
- Is the gap concentrated in one classification (`selector`, `runtime`, `product`)?
- Can the next rerun be assigned without reopening the full markdown report?

## Decision rule

If signoff fields are present but failed-check ownership is still missing, treat the report as replayable but not fully handoff-ready.
