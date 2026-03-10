# Web QA Playwright signoff scope quickcheck

Use this card right after validation passes and before you describe the artifact as handoff-ready.

## Four checks

1. **Lane named** — the signoff sentence says whether the scope is checkpoint, lane, section, or full run.
2. **Blocker still visible** — unresolved failed checks or replay blockers stay explicit.
3. **Owner routing visible** — the next owner or owner gap is still named.
4. **Proof target visible** — the rerun artifact, checkpoint ids, or target path is still present.

## Pass / hold rule

- **Pass** when all four checks are visible in one compact handoff.
- **Hold** when any check is missing; keep the artifact validator-clean but not signoff-ready.

## Example

- **Good:** `PASS, lane-scoped rerun only: functional remains the blocker, owner is QA automation, rerun F1-F5 with refreshed checkpoint artifacts before signoff.`
- **Too broad:** `PASS and ready for handoff.`
