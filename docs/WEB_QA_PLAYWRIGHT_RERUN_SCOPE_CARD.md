# WEB_QA_PLAYWRIGHT_RERUN_SCOPE_CARD

Use this card when strict-plus validation already passed, but you still need to decide whether the next rerun should stay lane-scoped or section-scoped.

## 30-second decision loop

1. Start with the hottest blocked section from the validator JSON.
2. If one blocker key dominates the hotspot, keep the rerun scope narrow.
3. If multiple blocker keys share the hotspot, rerun at section scope.
4. If the next action names a stable target and proof artifact, keep the rerun lane-specific.
5. If the next action still reads like a summary instead of an instruction, rewrite it before rerun.

## Keep the rerun lane-scoped when

- one blocker key clearly dominates,
- checkpoint ids already point to one lane,
- target refs are stable,
- artifact refs already show what must be refreshed.

## Expand to section scope when

- hotspot sections tie,
- blocker classes are split,
- checkpoint ownership is unclear,
- evidence gaps make a lane-only rerun misleading.

## Copy-ready handoff line

`Rerun scope: <lane|section> because <blocker summary>; refresh <artifact> after verifying <target>.`
