#!/usr/bin/env bash
set -euo pipefail

TARGET_ROOT="${1:-$HOME/.openclaw/skills}"
TARGET_DIR="${TARGET_ROOT%/}/openclaw-codex-pm-skills"

mkdir -p "$TARGET_ROOT"
rm -rf "$TARGET_DIR"
cp -R "$(cd "$(dirname "$0")/.." && pwd)" "$TARGET_DIR"

echo "Installed skills into: $TARGET_DIR"
echo "Tip: ensure your OpenClaw agent allowlist includes this path."
