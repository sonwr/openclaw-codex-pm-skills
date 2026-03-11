# Governance Sandbox report-title handoff

Use scenario metadata to keep governance rehearsal outputs easier to review and easier to demo.

## When to use

- when a scenario memo needs a reviewer-ready title that differs from the raw scenario name
- when markdown/html reports are shared outside the CLI terminal output
- when the demo bundle should keep the memo label stable across repeated scenario inputs

## Minimal rule

Add `report_title` (or `report_heading`) to the scenario file when the output should read like a memo instead of a fixture name.

## Example

```yaml
scenario:
  name: Treasury confidence rehearsal
  report_title: Delegate-ready treasury rehearsal memo
inputs:
  proposal: Add milestone checkpoints before growth spending.
  stakeholders:
    - name: Delegate circle
      preset: delegates
```

## Why it helps

- keeps the scenario fixture name stable for replay
- gives markdown/html artifacts a cleaner headline for review
- reduces last-mile renaming in public demo bundles
