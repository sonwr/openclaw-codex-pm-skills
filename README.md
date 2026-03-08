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
- `web-qa-playwright` (now includes QA inventory + failure-recovery references for interactive browser testing)

Current docs:

- `docs/INSTALL_OPENCLAW.md`
- `docs/COMPATIBILITY.md`
- `docs/MAPPING_PM_SKILLS.md`

Current examples:

- discovery prompt example
- strategy prompt example
- PRD prompt example
- prioritization prompt example
- web QA Playwright sample interactive run (`examples/web_qa_playwright_sample_run.md`)
- web QA Playwright strict-fail fixture for duplicate checkpoints (`examples/web_qa_playwright_strict_fail_duplicate_checkpoint.md`)
- web QA Playwright strict-fail fixture for missing failure evidence (`examples/web_qa_playwright_strict_fail_missing_evidence.md`)
- web QA Playwright strict-fail fixture for missing failure classification (`examples/web_qa_playwright_strict_fail_missing_classification.md`)
- web QA Playwright strict-fail fixture for malformed failure breakdown summary (`examples/web_qa_playwright_strict_fail_malformed_failure_breakdown.md`)
- web QA Playwright strict-fail fixture for missing `## 3) Execution log` header (`examples/web_qa_playwright_strict_fail_missing_execution_log_header.md`)
- web QA Playwright strict-plus combined fail fixture (duplicate checkpoints + missing failure metadata in one report) (`examples/web_qa_playwright_strict_plus_combined_fail.md`)
- web QA Playwright strict-plus pass fixture (deterministic replay gates all satisfied) (`examples/web_qa_playwright_strict_plus_pass.md`)
- web QA Playwright strict-plus isolated artifact-ref reuse fail fixture for CI triage (`examples/web_qa_playwright_strict_fail_artifact_ref_reuse_only.md`)
- web QA Playwright strict-plus isolated monotonic-timestamp fail fixture for replay-order triage (`examples/web_qa_playwright_strict_fail_monotonic_timestamp_only.md`)
- web QA Playwright strict-plus isolated status-consistency fail fixture for checkpoint/check drift triage (`examples/web_qa_playwright_strict_fail_status_inconsistency_only.md`)
- web QA Playwright strict-plus isolated missing-artifact-path fail fixture for evidence-capture triage (`examples/web_qa_playwright_strict_fail_missing_artifact_paths_only.md`)

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
│  ├─ install_local.sh          # Local installation helper
│  └─ validate_web_qa_report.py # Fixed-count QA report validator (5/3/2)
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

### 5) Browser QA signoff discipline
Use `web-qa-playwright` and validate the final markdown run artifact:

```bash
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_sample_run.md --strict
```

For machine-readable CI output, add `--json` (stdout) or `--json-out <path>` (artifact file).

`--strict` adds reproducibility gates aligned with Playwright-interactive principles:

- deterministic preconditions (URL, viewport, test account)
- deterministic check labeling (F1..F5 / V1..V3 / O1..O2)
- screenshot evidence density for visual checks (at least one inline shot per V-check)
- normalized status tokens on every check row (`PASS`/`FAIL`)
- explicit signoff fields (regression count + merge recommendation)
- signoff-check consistency (reported regression count must equal checklist `FAIL` line count)
- section summary ratio consistency (`x/y pass`) vs detailed PASS/FAIL lines
- step-by-step execution log checkpoints for all fixed check ids (F1..F5, V1..V3, O1..O2) in deterministic order
- failure recovery traceability for failed checks (`Expected`/`Observed`/`First failure timestamp`/`Retry`)

Optional hardening flags:

- `--strict-plus`: enable `--strict` and all hardening flags below as a single CI preset for deterministic replay and failure recovery.
- `--playwright-interactive-profile`: apply a Playwright-interactive reliability preset (strict-plus equivalent) to prioritize stability, reproducibility, step verification, and failure recovery in one flag.

Playwright-interactive operating principles reflected in this preset and fixture set:

1. **Stability first** — require explicit checkpoint timestamps/status tokens/target refs so repeated runs stay comparable.
2. **Reproducibility first** — keep deterministic replay artifacts (`--json-out`, isolated fail fixtures, PASS fixture) available for CI and triage.
3. **Step-by-step verification** — enforce execution-log shape plus QA inventory/checkpoint accounting instead of trusting free-form prose.
4. **Failure recovery** — require artifact paths, failure classification, and recovery owner/plan metadata so broken runs remain actionable.
- `--deterministic-replay-profile`: alias for `--playwright-interactive-profile` for teams that prefer deterministic replay wording in CI policies.
- `--strict-replay-profile`: alias for `--playwright-interactive-profile` for teams that want explicit strict replay wording in CI presets.
- `--ci-replay-profile`: alias for `--playwright-interactive-profile` for teams that prefer shorter replay-policy naming in CI jobs.
- `--enforce-checkpoint-format`: require each checkpoint line to use `action -> verification` format for clearer step-level reproducibility.
- `--require-checkpoint-timestamps`: require each checkpoint line to include an ISO-8601 UTC timestamp (`YYYY-MM-DDTHH:MM:SSZ`) for deterministic replay timelines.
- `--enforce-monotonic-checkpoint-timestamps`: require checkpoint timestamps to be monotonic in execution-log order, making replay order drift visible in CI.
- `--enforce-checkpoint-status-tokens`: require each checkpoint line to include explicit `PASS`/`FAIL` token for parser-safe replay traces.
- `--require-visual-checkpoint-evidence`: require each visual checkpoint line (`V1..V3`) to include an inline screenshot path for reproducible visual proof.
- `--require-checkpoint-artifact-paths`: require every checkpoint line to include at least one inline artifact path (screenshot/video/log/trace) for post-failure replay and evidence auditing.
- `--require-checkpoint-target-refs`: require every checkpoint line to include a stable target reference token (`ref=<id>`) so interactive replay can bind actions to deterministic UI targets.
- `--enforce-checkpoint-artifact-ref-uniqueness`: require each inline artifact path to appear in only one checkpoint line, reducing ambiguous replay evidence mapping.
- `--require-failure-evidence-artifact-paths`: require failed checks to include an inline artifact path on the `Evidence:` line, so triage links are machine-verifiable.
- `--require-failure-recovery-plan`: require failed checks to include a `Recovery plan:` line with deterministic next-step recovery instructions.
- `--require-failure-recovery-owner`: require failed checks to include a `Recovery owner:` line so ownership is explicit for follow-up recovery.
- `--enforce-failure-timestamp-order`: require failed-check `First failure timestamp` values to be monotonic in checklist order, preventing chronology drift in failure triage.
- `--enforce-checkpoint-to-check-status-consistency`: require each checkpoint line to include `PASS`/`FAIL` and match the checklist status for that same check id (prevents replay-log/checklist drift).
- `--require-failure-classification-summary`: require a signoff line in the form `Failure breakdown: selector=<n>, runtime=<n>, product=<n>` and validate it against failed-check classifications.
- `--require-execution-log-step-count-match`: require the execution log to contain only checkpoint bullets and exactly 10 checkpoint lines (F1..F5, V1..V3, O1..O2), which tightens deterministic replay step accounting.
- `--require-qa-inventory-section`: require the report to include a `## QA inventory` section with explicit environment/tool metadata for replayable incident audits.

The validator always enforces the fixed structure rule (5 functional / 3 visual / 2 off-happy-path checks).

Troubleshooting fixture commands:

```bash
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_duplicate_checkpoint.md --strict
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_missing_evidence.md --strict
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_missing_classification.md --strict
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_missing_execution_log_header.md --strict
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_malformed_failure_breakdown.md --strict --require-failure-classification-summary
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_monotonic_timestamp_only.md --strict-plus
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_missing_artifact_paths_only.md --strict-plus
```

Expected outcomes:
- duplicate-checkpoint fixture: `FAIL` with `duplicate checkpoint ids` error.
- missing-evidence fixture: `FAIL` with `failed check ... must include an Evidence: line` error.
- missing-classification fixture: `FAIL` with `failed check ... must include a Failure classification: line` error.
- malformed-failure-breakdown fixture: `FAIL` with failure-classification-summary mismatch when `--require-failure-classification-summary` is enabled.
- missing-execution-log-header fixture: `FAIL` with strict-mode `Execution log` section-header error.
- missing-artifact-paths-only fixture: `FAIL` with exactly one strict-plus `checkpoint artifact paths` error for evidence-capture triage.
- monotonic-timestamp-only fixture: `FAIL` with exactly one `checkpoint timestamp order` error under `--strict-plus`.

### Strict-plus isolated triage matrix

Use these deterministic fixtures to isolate one replay drift at a time:

- `web_qa_playwright_strict_fail_artifact_ref_reuse_only.md` → artifact mapping drift (`checkpoint artifact refs`)
- `web_qa_playwright_strict_fail_monotonic_timestamp_only.md` → replay-order drift (`checkpoint timestamp order`)
- `web_qa_playwright_strict_fail_status_inconsistency_only.md` → checklist/log state drift (`status consistency`)
- `web_qa_playwright_strict_fail_missing_target_refs.md` → selector-target traceability drift (`checkpoint target refs`)
- `web_qa_playwright_strict_fail_missing_artifact_paths_only.md` → evidence-capture drift (`checkpoint artifact paths`)

Copy-paste recovery commands:

```bash
# Artifact mapping drift
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_artifact_ref_reuse_only.md --strict-plus --json-out .tmp/web-qa-artifact-ref-reuse.json

# Replay-order drift
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_monotonic_timestamp_only.md --strict-plus --json-out .tmp/web-qa-monotonic-only.json

# Checklist/log status drift
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_status_inconsistency_only.md --strict-plus --json-out .tmp/web-qa-status-inconsistency.json

# Selector traceability drift
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_missing_target_refs.md --strict-plus --json-out .tmp/web-qa-missing-target-refs.json

# Evidence capture drift
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_strict_fail_missing_artifact_paths_only.md --strict-plus --json-out .tmp/web-qa-missing-artifact-paths.json
```

This mirrors Playwright-interactive-style recovery: isolate a single failing invariant, verify it deterministically, then fix only that layer before broad reruns.

CI now includes a negative-fixture guard: each strict-fail fixture must fail validation so policy regressions are caught early.
CI also snapshots a strict-plus PASS fixture to JSON and asserts the downstream parser-facing payload shape (`status`, enabled gates, and fixed `counts`).
- JSON payloads now include `validation_schema_version` so CI parsers can detect contract changes explicitly.

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
