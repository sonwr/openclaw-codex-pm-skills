# Mapping: phuryn/pm-skills → openclaw-codex-pm-skills

This document explains how concepts from `phuryn/pm-skills` are adapted into this repository.

## Mapping Principles

1. Preserve framework intent.
2. Replace assistant-specific command engines with portable skill instructions.
3. Keep outputs deterministic and auditable.
4. Prioritize small, composable workflows.

## Current Mapping (v0)

| Upstream concept | This repo equivalent | Status |
|---|---|---|
| Discovery workflow | `skills/pm-discovery-foundations/SKILL.md` | ✅ Initial |
| Strategy canvas workflow | `skills/pm-strategy-canvas/SKILL.md` | ✅ Initial |
| Slash command orchestration | `examples/*.md` prompt recipes | ✅ Adapted |
| Plugin metadata/runtime hooks | Not ported (tool-specific) | ⚠️ Out of scope |

## Planned Mapping

- PRD drafting workflow
- Prioritization framework helper
- Interview synthesis template
- Metrics dashboard template

## Non-goals

- 1:1 replication of upstream plugin runtime behavior
- Vendor-locked command execution semantics
