# Governance sandbox web-demo proof loop

Use this when a governance rehearsal repo adds a lightweight web demo and needs a short, reproducible proof cycle.

## Why this exists

Governance demos often look finished before the proof path is stable. This loop keeps the first web demo honest:

- input flow is explicit,
- UI state is checkable,
- report output is reproducible,
- failure recovery is documented before handoff.

## Proof loop

1. **Load a fixed scenario file first** so the same proposal and stakeholder mix can be replayed.
2. **Confirm the first-screen promise**: the form should explain what to paste, what presets exist, and what output file/report the user gets.
3. **Run one deterministic interaction path**: scenario import → optional edit → simulate → report card/result download.
4. **Capture both UI proof and artifact proof**:
   - browser screenshot or HTML report path
   - generated markdown/json report path
5. **Write the next-run cue** whenever the demo blocks on styling, flaky selectors, or missing report fields.

## Playwright-interactive guardrails

- Prefer stable labels and role-based selectors over brittle DOM position checks.
- Reuse the same scenario fixture during repair loops.
- Verify one step at a time: load -> input -> submit -> result -> artifact.
- If a step fails, record the failing state and the smallest retry scope before expanding the run.

## Good first proof claim

"Web demo loads a scenario fixture, renders stakeholder result cards, and exports a matching report artifact with a reproducible replay path."
