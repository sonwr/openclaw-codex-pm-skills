# Web QA Playwright rerun exit note

Use this note when you need a short, human-readable reason for why a rerun should stop instead of looping again.

## Exit note template

- **Current blocker:** name the failed checkpoint or shared blocker.
- **Why rerun stops:** explain the evidence gap, owner dependency, or environment constraint.
- **What changed since last attempt:** note whether the latest pass produced any new signal.
- **Next owner:** identify the team or person who can unblock progress.
- **Next proof to collect:** describe the single most useful follow-up artifact.

## Good exit note traits

1. It is specific to the current rerun.
2. It does not hide behind generic wording like `still failing`.
3. It points to one next action instead of a broad backlog.
4. It helps a reviewer decide whether to retry, repair, or escalate.

## Example

```text
Current blocker: checkout-submit remains blocked by the payment sandbox timeout.
Why rerun stops: two retries produced the same timeout and no new DOM signal.
What changed since last attempt: screenshot timestamps changed, but failure signature did not.
Next owner: payment sandbox maintainer.
Next proof to collect: timeout trace plus sandbox health check result.
```
