# Web QA Playwright signoff next-action status line

Use this when validation already passes and you need a single-line handoff that keeps the blocked lane, owner, and next proof target visible.

## Format

```text
Status: validator PASS; next action is <owner> repairing <blocked-lane/check-ref> and attaching <artifact/proof target> before rerun.
```

## Keep the line honest

- Name the real blocked lane or failed check reference.
- Name the owner only if the report already carries owner coverage.
- Name the next artifact or proof target so the rerun stays reviewable.
- Do not call the report signoff-ready if the next action is still vague.

## Example

```text
Status: validator PASS; next action is QA repairing checkout-payment evidence and attaching a refreshed trace bundle before rerun.
```
