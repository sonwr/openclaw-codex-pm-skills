# GOVERNANCE_SANDBOX_STRING_PRESET_NOTE

When scenario files already know a preset audience, allow bare string stakeholder entries such as `delegates` or `community` instead of forcing the longer object form.

## Why it helps
- Scenario fixtures stay shorter and easier to review.
- Preset expansion still produces the same normalized stakeholder objects.
- Report and demo flows can share the same compact scenario input.
