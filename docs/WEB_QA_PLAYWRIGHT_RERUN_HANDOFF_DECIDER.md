# Web QA Playwright rerun handoff decider

Use this note when the report already identifies a hotspot but the next owner still needs a quick rerun-versus-repair answer.

## Ask these questions in order

1. **Did the failing checkpoint already capture enough evidence?**
   - Yes: prefer repair handoff.
   - No: prefer rerun handoff with the missing artifact or timestamp called out.
2. **Is the failure scoped to one section or spreading across multiple sections?**
   - One section: keep the rerun scope narrow.
   - Multiple sections: escalate to repair/owner triage before asking for a broad rerun.
3. **Does the current report already name the recovery owner?**
   - Yes: keep the owner in the status line.
   - No: treat owner assignment as part of the handoff before requesting another execution loop.

## Recommended status line

`next_action: rerun <section/checkpoint set> only after missing evidence or owner routing is explicit`

## When not to rerun

Do not request a rerun just to restate an already-proven blocker. If the blocker is stable, route to repair with the existing evidence instead.
