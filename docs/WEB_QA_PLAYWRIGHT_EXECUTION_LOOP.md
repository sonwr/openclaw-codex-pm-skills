# Web QA Playwright execution loop

This note turns the `web-qa-playwright` skill into a repeatable signoff loop for OpenClaw/Codex workflows.

## Why this exists

Interactive browser QA often fails for boring reasons: a missing precondition, a stale selector, or screenshots captured in the wrong state. The goal of this document is to keep the loop stable, reviewable, and easy to rerun.

## Core loop

1. **Write the QA inventory first**
   - List requested behaviors, user-visible controls, and the claims you expect to make in the final signoff.
   - Map each item to at least one functional check, one visual checkpoint where needed, and an evidence artifact.
2. **Lock reproducible preconditions**
   - Record URL, viewport, account/seed data, and any required flags.
   - Prefer explicit, copyable preconditions over implied environment knowledge.
3. **Run the interaction in small verified steps**
   - After each meaningful action, confirm the resulting state before moving on.
   - Keep checkpoints deterministic (`F1..F5`, `V1..V3`, `O1..O2`) so reruns stay comparable.
4. **Capture evidence in the state you are signing off**
   - Functional evidence should prove the claim.
   - Visual evidence should show the exact UI state being evaluated, not a nearby screen.
5. **Classify failures before proposing fixes**
   - Use a small failure taxonomy: `selector`, `runtime`, `product`.
   - A good handoff says what broke, who owns it, and what should be rerun first.
6. **Recover deliberately**
   - Renderer-only change: reload and rerun the affected checks.
   - Startup/main-process change: relaunch and rerun the affected checks.
   - Do not "continue anyway" after a broken precondition.

## Minimal reviewer checklist

- Is the QA inventory complete enough to cover every signed-off claim?
- Are URL/viewport/account details explicit?
- Does every failed check include classification, evidence, owner, and next action?
- Do checkpoint refs and artifact refs make the rerun path obvious?

## Recommended command pattern

```bash
python3 scripts/validate_web_qa_report.py   --file examples/web_qa_playwright_strict_plus_with_check_refs_pass.md   --strict-plus   --require-qa-inventory-check-refs   --json-out artifacts/validation.json
```

This command gives both human-readable review output and machine-readable replay metadata for CI triage.
