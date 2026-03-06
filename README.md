# openclaw-codex-pm-skills

Practical PM skill pack and migration guide for **OpenClaw + Codex-style agents**.

This repository helps teams adapt PM-oriented skill systems (e.g., marketplace-style skill collections) into an OpenClaw-compatible workflow that is easy to install, audit, and extend.

## Origin and Scope

This project is a practical adaptation layer for teams who want to use ideas and frameworks from [`phuryn/pm-skills`](https://github.com/phuryn/pm-skills) in **OpenClaw + Codex-style** environments.

- It focuses on portability, reproducibility, and OpenClaw-friendly structure.
- It does **not** attempt to replicate assistant-specific plugin runtime behavior one-to-one.
- It is an independent community adaptation, not an official fork or affiliated release.


## Why this exists

Most PM skill repositories are built around assistant-specific plugin systems.
OpenClaw users often need:

- a portable skill structure,
- clear installation steps,
- reproducible examples,
- and safe defaults for shared environments.

This repo provides that bridge.

---

## What you get

- **OpenClaw-oriented PM skill templates**
- **Migration playbook** from plugin-centric skills to file-based skills
- **Command recipes** for discovery, strategy, and PRD workflows
- **Safety notes** for multi-user/chat deployments
- **Contribution structure** for community extensions

---

## Quick Start

1. Clone this repository.
2. Copy `skills/*` into your OpenClaw skill directory (or your workspace skill directory).
3. Register/allow those skills for your target agent.
4. Use the prompts in `examples/` to run workflows.

> Note: OpenClaw setup can vary by deployment. See [`docs/INSTALL_OPENCLAW.md`](docs/INSTALL_OPENCLAW.md).

---

## Repository Layout

- `skills/` — skill packs in portable format
- `examples/` — runnable prompt examples
- `docs/` — install, architecture, compatibility
- `scripts/` — helper scripts for local setup

---

## Initial Skill Packs (v0)

- Discovery foundations
- Strategy foundations
- PRD drafting workflow
- Prioritization helper

These are intentionally minimal and auditable.

---

## Philosophy

1. **Portable over platform-locked**
2. **Deterministic over magical**
3. **Safe defaults over broad power**
4. **Composability over monoliths**

---

## Roadmap

- v0.1: basic templates + docs
- v0.2: richer example library + quality checklist
- v0.3: validation tooling and compatibility matrix automation
- v1.0: stable community PM skill pack for OpenClaw ecosystems

---

## License

MIT
