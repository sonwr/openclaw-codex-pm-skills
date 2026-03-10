# WEB_QA_PLAYWRIGHT_OWNER_GAP_EXIT_CHECK

Use this card after strict-plus validation passes but before calling a report owner-complete for handoff.

## 30-second check

1. Open `unresolved_failed_check_recovery_owners`.
2. Confirm whether every failed check id appears under a recovery owner or an explicit escalation bucket.
3. Check whether `next_action` still names the same owner lane that the unresolved gaps suggest.
4. If unresolved owner coverage still exists, stop at inspection-ready instead of handoff-ready.

## Pass / hold rule

- **Pass** — every failed check is routed to a recovery owner or an explicit escalation lane, and the `next_action` sentence follows that routing.
- **Hold** — one or more failed checks still sit outside owner coverage, or the `next_action` sentence points at a different lane than the unresolved owner gaps.

## Copy-ready note

`Owner gap exit check: only call this report handoff-ready when every failed check is already routed to a named recovery owner or escalation lane.`
