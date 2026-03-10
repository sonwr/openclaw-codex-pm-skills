# Next-action owner sequence

Use this quick sequence when the validator passes but the handoff still feels vague.

## Goal

Turn a passing report into an owner-routable next action in under one minute.

## Sequence

1. Name the hottest failed check or blocked lane first.
2. Name the owner or owner role second.
3. Name the target ref or artifact path third.
4. End with the smallest rerun or repair action that can verify the fix.

## Good pattern

```text
Next action: Frontend owner reruns F2 on ref e12 using artifacts/f2-inline-error.png after fixing the alert focus regression.
```

## Weak pattern

```text
Next action: Investigate the issue and rerun later.
```

## Quick check

If the sentence does not make the owner, proof target, and smallest next move obvious, it is not handoff-ready yet.
