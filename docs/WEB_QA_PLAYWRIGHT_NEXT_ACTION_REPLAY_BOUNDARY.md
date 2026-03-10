# Web QA Playwright next-action replay boundary

Use this note when the validator already passes but the next step still feels too broad for a safe rerun.

## Goal

Turn a vague replay request into a narrow, artifact-backed boundary.

## Ask these three questions

1. **Which failed lane is being replayed?**
   - Name the section or checkpoint group.
   - Reuse the failed check ids when possible.
2. **What proof artifact anchors the rerun?**
   - Call out the screenshot, trace, DOM capture, or execution log that explains the boundary.
3. **What is intentionally out of scope?**
   - Say which sections, owners, or follow-up fixes are *not* part of the immediate rerun.

## Copy-ready handoff pattern

```text
Next action: replay <failed lane> using <artifact/proof anchor> and keep <out-of-scope lane> out of this rerun until the current blocker is cleared.
```

## Good boundary signals

- The rerun target can be understood in one sentence.
- A reviewer can tell what evidence to open first.
- The handoff does not silently expand into a full-suite retry.

## Escalate instead of narrowing when

- the same blocker spans multiple sections with shared evidence gaps,
- owner routing is still unknown,
- or the next action cannot name a stable proof artifact.
