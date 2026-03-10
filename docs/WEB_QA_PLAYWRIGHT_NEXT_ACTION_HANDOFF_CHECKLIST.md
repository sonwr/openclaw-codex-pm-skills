# Web QA Playwright next-action handoff checklist

Use this quick checklist before sharing a `next_action` recommendation from a strict or strict-plus report.

## Checklist

- Confirm the reported blocker is still the highest-priority unresolved issue.
- Reuse the exact check refs and artifact paths already present in the report.
- Name the owner who should take the next action.
- State whether the next step is rerun, repair, evidence collection, or escalation.
- Keep the handoff scoped to one concrete move that can be executed immediately.
- Avoid suggesting replay when the report already marks replay blockers as active.
- Include the shortest proof line a reviewer can use to verify completion.

## Good handoff shape

```text
next_action: Repair checkout form locator in section checkout, then rerun only failed refs c14 and c15 with the same trace bundle.
```

## Avoid

- vague wording such as "investigate further"
- owner-free action items
- replay suggestions without replay readiness
- multi-step plans hidden inside a single handoff line
