#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

export PYTHONPATH=.

echo '[ci] check required docs'
test -f README.md
test -f docs/INSTALL_OPENCLAW.md
test -f docs/COMPATIBILITY.md

echo '[ci] check skill files'
find skills -name 'SKILL.md' | grep -q .

echo '[ci] check helper scripts'
test -x scripts/install_local.sh
test -x scripts/validate_web_qa_report.py

echo '[ci] validate sample web QA report shape'
python3 scripts/validate_web_qa_report.py --file examples/web_qa_playwright_sample_run.md --strict

echo '[ci] run validator unit tests'
python3 -m unittest discover -s tests -p 'test_*.py' -v

echo '[ci] run replay-profile smoke script'
chmod +x scripts/smoke_replay_profile_examples.sh
./scripts/smoke_replay_profile_examples.sh

echo '[ci] local CI entrypoint: PASS'
