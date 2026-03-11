# Governance Sandbox Playwright Recovery Note

Use this when the governance-sandbox web demo proof is almost stable but one browser step flakes.

## Keep the recovery loop narrow
- Re-run the smallest scenario-file-backed flow first.
- Keep one stable form action and one visible result-card proof in scope.
- Confirm the same report download evidence remains visible after the retry.

## Recovery checkpoints
1. Reopen the scenario fixture that drives the web demo.
2. Re-run the deterministic browser path from input form to result card.
3. Verify the report artifact link or download target is still visible.
4. Only widen scope after the failing checkpoint is reproducible again.
