# Next action coverage for every failed check

Use this guide when a Playwright Web QA report has more than one failed check and the signoff block needs a single replay-ready `Next action:` line.

## What good looks like

A handoff-ready next action should:

- name every failed check id exactly once when possible,
- describe the shortest useful repair or rerun step,
- keep target refs and artifact refs visible when they already exist,
- avoid vague phrases like `investigate issue` without naming the blocked checks.

## Fast authoring loop

1. Read the failed check ids from the checklist summary.
2. Confirm the same ids appear in the execution log checkpoints.
3. Draft one sentence that references every failed id.
4. Add target refs like `ref=e42` when the rerun depends on a known locator.
5. Add artifact refs like `artifacts/f2-timeout.png` when the next reviewer will need proof.

## Example

```text
- Next action: Re-run F2 and F3 on the login form, verify ref=e42 still resolves after submit, compare `artifacts/f2-timeout.png` with a fresh dashboard screenshot, and capture replacement evidence before signoff.
```

## Anti-patterns

- Mentioning only the loudest failure when two or more checks are blocked
- Referring to `the failing flow` without the check ids
- Asking for a rerun without any target or artifact context when that context already exists
