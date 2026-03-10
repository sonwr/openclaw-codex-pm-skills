# Playwright signoff exit criteria

Use this when a strict-plus report already passes, but you still need to decide whether the artifact is safe to hand off.

A report is signoff-ready when all of the following are true:

1. every failed check id appears in either the repair plan or the rerun explanation,
2. each failed check has a named owner or explicit owner gap note,
3. the next action sentence names the immediate lane to execute,
4. replay blockers and evidence gaps agree on the highest-risk hotspot,
5. no unresolved ambiguity remains about whether the artifact needs repair, rerun, or signoff.

If one of those conditions is missing, treat the report as validator-clean but not signoff-ready.
