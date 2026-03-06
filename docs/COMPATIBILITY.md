# Compatibility Notes

## Works well

- File-based skill formats (`SKILL.md`-style)
- Prompt recipes and framework checklists
- Structured workflow templates

## Requires adaptation

- Assistant-specific slash command engines
- Marketplace/plugin metadata tied to one vendor
- Runtime-specific APIs not available in OpenClaw

## Guideline

Treat this repo as a **portability layer**:
- preserve framework intent,
- adapt execution model,
- document differences clearly.
