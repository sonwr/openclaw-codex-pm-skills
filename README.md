# openclaw-codex-pm-skills

A community-driven adaptation layer for applying PM skill frameworks (inspired by [phuryn/pm-skills](https://github.com/phuryn/pm-skills)) to **OpenClaw + Codex-style** workflows.

This project is designed for teams who want practical, reusable product-management skills that are:

- portable across environments,
- easy to audit,
- safe for collaborative use,
- and realistic to maintain in open source.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Origin and Positioning](#origin-and-positioning)
- [Vision](#vision)
- [Project Direction (2026)](#project-direction-2026)
- [Core Principles](#core-principles)
- [Who This Project Is For](#who-this-project-is-for)
- [What Exists Today](#what-exists-today)
- [What We Are Building Next](#what-we-are-building-next)
- [Architecture and Repository Structure](#architecture-and-repository-structure)
- [How to Install](#how-to-install)
- [How to Use in Real Work](#how-to-use-in-real-work)
- [Quality Standards](#quality-standards)
- [Contributing Guide](#contributing-guide)
- [Governance and Decision-Making](#governance-and-decision-making)
- [Compatibility Notes](#compatibility-notes)
- [Roadmap](#roadmap)
- [References](#references)
- [License](#license)

---

## Project Overview

`openclaw-codex-pm-skills` turns PM workflows into skill assets that can be consistently applied in OpenClaw-based agent operations.

It focuses on practical outcomes:

- better discovery quality,
- clearer strategy artifacts,
- faster PRD drafting,
- more transparent prioritization,
- and repeatable outputs in team environments.

This is **not** a prompt dump.
It is a structured, evolving skill system intended for real delivery workflows.

---

## Origin and Positioning

This repository is inspired by the ideas and workflow style of:

- [phuryn/pm-skills](https://github.com/phuryn/pm-skills)

and adapts those concepts for OpenClaw/Codex usage patterns.

### Important scope statement

- This is an **independent community adaptation**, not an official fork.
- We preserve intent (PM rigor and workflow clarity), not runtime-specific behavior.
- We intentionally avoid vendor-locked orchestration semantics.

---

## Vision

Build the most practical open PM skill pack for agent-assisted product development, where outputs are:

1. **actionable** (usable in real planning and execution),
2. **auditable** (clear rationale and traceable assumptions),
3. **collaborative** (easy for multiple contributors to improve),
4. **portable** (usable across OpenClaw/Codex-style setups).

---

## Project Direction (2026)

### Direction A — Practical PM execution

Prioritize skills that directly improve shipping quality:

- discovery
- strategy
- PRD
- prioritization
- risk/assumption management

### Direction B — Shared team standards

Standardize output formats so multiple contributors can collaborate without style drift.

### Direction C — Safe, transparent automation

Support automation with explicit boundaries and predictable outputs, especially in group/chat contexts.

### Direction D — Open contributor ecosystem

Design the project so contributors can add domain packs (B2B SaaS, Web3, infra tools, etc.) with consistent quality.

---

## Core Principles

1. **Portability over lock-in**
2. **Clarity over magic**
3. **Determinism over ambiguity**
4. **Safety over convenience**
5. **Incremental improvement over giant rewrites**

---

## Who This Project Is For

- Product managers using agent-assisted workflows
- Founders who need PM structure in fast-moving build cycles
- AI-native teams shipping iterative product changes
- OSS contributors who want reusable PM skill assets

---

## What Exists Today

Current initial skill packs:

- `pm-discovery-foundations`
- `pm-strategy-canvas`
- `pm-prd-drafting`
- `pm-prioritization-helper`

Current docs:

- `docs/INSTALL_OPENCLAW.md`
- `docs/COMPATIBILITY.md`
- `docs/MAPPING_PM_SKILLS.md`

Current examples:

- discovery prompt example
- strategy prompt example
- PRD prompt example
- prioritization prompt example

---

## What We Are Building Next

Near-term priorities:

1. stronger skill specifications (inputs/outputs/evaluation criteria),
2. review checklist per skill PR,
3. domain-specific extensions,
4. compatibility matrix across OpenClaw runtime patterns,
5. starter integration recipes for real product teams.

---

## Architecture and Repository Structure

```text
openclaw-codex-pm-skills/
├─ skills/                      # Core and extension skill packs
│  ├─ pm-discovery-foundations/
│  ├─ pm-strategy-canvas/
│  ├─ pm-prd-drafting/
│  └─ pm-prioritization-helper/
├─ docs/
│  ├─ INSTALL_OPENCLAW.md       # Installation and activation guidance
│  ├─ COMPATIBILITY.md          # Runtime compatibility and constraints
│  └─ MAPPING_PM_SKILLS.md      # Upstream concept mapping
├─ examples/                    # Real prompt usage examples
├─ scripts/
│  └─ install_local.sh          # Local installation helper
└─ .github/workflows/ci.yml     # Minimal structural validation
```

---

## How to Install

```bash
git clone https://github.com/sonwr/openclaw-codex-pm-skills.git
cd openclaw-codex-pm-skills
./scripts/install_local.sh
```

By default this installs to `~/.openclaw/skills`.

For custom location:

```bash
./scripts/install_local.sh /path/to/skills
```

Then ensure your OpenClaw configuration allows these skills for your target agent.

---

## How to Use in Real Work

### 1) Discovery sprint
Use `pm-discovery-foundations` to produce:

- problem framing
- assumption ranking
- low-cost experiments
- decision recommendation

### 2) Strategy alignment
Use `pm-strategy-canvas` to produce:

- target segment
- strategic bets
- risk mitigation plan
- measurable checkpoints

### 3) Build planning
Use `pm-prd-drafting` to produce:

- one-page PRD
- scope boundaries
- acceptance criteria

### 4) Prioritization session
Use `pm-prioritization-helper` to produce:

- weighted rankings
- exclusion rationale
- revisit triggers

---

## Quality Standards

A skill should be merged only if it is:

- **Clear**: purpose and when-to-use are explicit.
- **Structured**: includes deterministic output sections.
- **Testable**: has at least one realistic usage example.
- **Safe**: no hidden destructive instructions.
- **Maintainable**: concise, readable, and versionable.

---

## Contributing Guide

We welcome contributors.

### Contribution flow

1. Fork and create a branch
2. Add or improve one focused skill/doc change
3. Include an example in `examples/` if behavior changed
4. Open a PR with:
   - purpose,
   - before/after behavior,
   - sample output format,
   - compatibility notes

### Commit style

- `feat:` new capability
- `fix:` correctness/safety improvement
- `docs:` documentation improvements
- `chore:` maintenance tasks

### PR review checklist (required)

- [ ] Scope is clear and narrow
- [ ] Output format is explicit
- [ ] Example is included/updated
- [ ] No vendor-locked assumptions hidden in skill text
- [ ] Compatibility implications are documented

---

## Governance and Decision-Making

This repository currently follows a maintainer-driven model with transparent rationale in PRs.

As contributor volume grows, governance will evolve to:

- lightweight RFCs for major changes,
- domain maintainers for extension packs,
- release notes with migration guidance.

---

## Compatibility Notes

- Works well for file-based skill execution patterns.
- Requires adaptation for assistant-specific slash-command engines.
- This repository intentionally avoids hard dependencies on a single vendor runtime.

See full details in `docs/COMPATIBILITY.md`.

---

## Roadmap

### v0.2

- richer skill specs
- contributor checklist hardening
- additional examples

### v0.3

- domain extension packs
- stronger compatibility documentation
- quality scoring for skill submissions

### v0.4

- reusable "skill test scenarios" for regression checks
- release process for community contributions

### v1.0

Stable, community-supported PM skill framework for OpenClaw/Codex-style teams.

---

## References

- Upstream inspiration: [phuryn/pm-skills](https://github.com/phuryn/pm-skills)
- This project: adaptation for OpenClaw + Codex-style workflows

---

## License

MIT
