# Web QA Playwright Signoff Rerun-Ready Signal

Use this note after validation already passes but the artifact still points to a focused rerun.

Call the artifact **rerun-ready** only when all of the following are true:

1. the blocked lane or section is named explicitly,
2. the next action says what to rerun,
3. the proof target or artifact is named,
4. the owner or routing path is obvious from the handoff,
5. the wording stays lane-scoped instead of implying whole-run readiness.

If one of those signals is missing, keep the wording at **validator-clean** or **inspection-ready** instead of **rerun-ready**.

## Compact status line

- **Rerun-ready:** validation passed, the blocked lane is named, the rerun target is explicit, and the owner can execute the next step without reopening the whole report.
- **Not rerun-ready:** validation passed, but the rerun target, proof artifact, or owner routing is still ambiguous.
