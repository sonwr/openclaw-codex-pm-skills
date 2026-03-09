# Playwright Interactive Repair Loop

A compact repair loop for interactive browser QA runs.

This guide adapts the same operating posture used by persistent Playwright-interactive workflows:

- keep runs stable and reproducible,
- verify one meaningful step at a time,
- capture evidence before claiming success,
- and recover by repairing the smallest broken unit first.

---

## When to use this loop

Use this after a blocked or flaky interactive run when the report already tells you **what failed**, but the next rerun still needs an ordered recovery path.

Typical triggers:

- target refs are missing or unstable,
- artifact paths are incomplete,
- timestamps are missing or out of order,
- the next action is too vague for handoff,
- a rerun needs a deterministic first checkpoint instead of a full restart.

---

## Core repair order

Always repair in this order unless a stronger local constraint exists:

1. **Session stability**
   - Confirm the same environment/profile/runtime is still in use.
   - Avoid changing multiple variables before the rerun.
2. **Target refs**
   - Re-establish stable UI references before replaying functional intent.
   - If the target cannot be named, the rerun is not yet reproducible.
3. **Evidence capture**
   - Restore screenshot/log/trace paths before broadening the rerun scope.
   - A fix without evidence is not signoff-ready.
4. **Chronology**
   - Repair missing or non-monotonic timestamps so the recovery log can be audited.
5. **Next-action handoff**
   - Rewrite the next action so it names failed checks, rerun scope, owner, and expected evidence.

---

## Step-by-step rerun pattern

### 1) Freeze the rerun surface

Write down:

- URL / environment
- runtime profile or browser profile
- viewport/device mode
- account or seeded state
- exact failing section (`functional`, `visual`, `off_happy`)

### 2) Reduce to one checkpoint burst

Do not attempt a whole-suite rerun first.

Prefer:

- one failed check,
- one UI state transition,
- one screenshot/log pair,
- one verification sentence.

### 3) Verify immediately after the action

For each checkpoint, capture:

- the action performed,
- the visible result,
- the stable ref used,
- the evidence artifact produced.

If any one of these is missing, stop and repair that field before continuing.

### 4) Recover locally, not globally

Prefer:

- page reload over full environment restart,
- targeted selector repair over broad prompt rewriting,
- replacing one missing artifact path over regenerating the whole report.

Restart the whole flow only when process ownership, profile state, or app bootstrap changed.

### 5) Re-run the same checkpoint once more

After repair, repeat the same checkpoint once to confirm the failure is actually resolved and not merely bypassed.

---

## Failure-to-repair mapping

### Missing target refs

Repair by:

- naming the exact control or state anchor,
- reusing the same ref format across checkpoint and next-action text,
- avoiding vague labels like "the button" or "main card".

### Missing artifact refs

Repair by:

- capturing the missing screenshot/log/trace first,
- storing the exact path in the checkpoint line,
- mirroring that path in the next action if follow-up is still required.

### Missing timestamps

Repair by:

- adding UTC timestamps per checkpoint,
- ensuring order is monotonic,
- avoiding hand-edited sequences that imply impossible chronology.

### Vague next action

Repair by rewriting the handoff to include:

- failed check ids,
- target refs,
- artifact expectations,
- rerun intent,
- recovery owner when known.

---

## Minimal signoff rule

Do not mark the rerun ready unless all of the following are true:

- the repaired checkpoint is reproducible,
- the evidence path exists in the report,
- the chronology is readable,
- the next action is specific enough for a different operator to continue.

---

## Copyable micro-checklist

- Same environment/profile confirmed
- One failed checkpoint selected
- Stable target ref present
- Evidence artifact path present
- Timestamp present and ordered
- Next action references failed check ids
- One rerun confirms the repaired checkpoint
