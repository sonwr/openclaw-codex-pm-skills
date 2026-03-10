# WEB QA Playwright signoff owner-ready brief

Use this quick brief when validation already passes but you still need to confirm the artifact is safe to hand off to an owner.

## 30-second check

1. Name the blocked lane, section, or checkpoint explicitly.
2. Confirm the failed refs still visible in the report are covered by the proposed owner or clearly marked unresolved.
3. Keep the next action narrow enough that a human can rerun or repair without reopening the full report.
4. Do not call the report fully signoff-ready if owner coverage is partial or alias-only.

## Copy-ready status line

`Validator PASS; owner-ready only for <lane/section> after confirming failed-ref coverage, named proof target, and a rerun-safe next action.`

## When to avoid this brief

Skip this shortcut and use the broader handoff docs when:

- multiple blocked lanes still compete for priority,
- owner assignment is missing or ambiguous,
- the next action does not yet name a proof artifact,
- or the report still sounds whole-run ready instead of lane-scoped.
