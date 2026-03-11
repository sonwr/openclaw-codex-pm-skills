# WEB_QA_STRICT_SIGNOFF_CHECKLIST

Use this checklist before calling a strict Playwright web QA report review-ready.

- Confirm the report still includes Scope, checklist summary, execution log, and Signoff sections.
- Confirm every failed check carries Expected, Observed, First failure timestamp, Retry, Failure classification, and Evidence fields.
- Confirm execution-log checkpoint IDs stay deterministic and match the checklist order.
- Confirm replay evidence stays actionable: target refs, artifact paths, and next-action references should point to the same failing checks.
- Confirm the merge recommendation and replay readiness still match the observed regression count.

This is meant to be a last-pass signoff card, not a replacement for the validator.
