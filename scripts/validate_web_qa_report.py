#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path


VALIDATION_SCHEMA_VERSION = 1

SECTION_TITLES = {
    "functional": r"Functional checks",
    "visual": r"Visual checks",
    "off_happy": r"Off-happy-path checks",
}


def _section_block(text: str, title_pattern: str) -> str:
    pattern = rf"(?ms)^\s*-\s*{title_pattern}.*?$\n(?P<body>.*?)(?=^\s*-\s*[A-Z][^\n]*checks|^##\s|\Z)"
    match = re.search(pattern, text)
    return match.group("body") if match else ""


def _count(pattern: str, text: str) -> int:
    return len(re.findall(pattern, text, flags=re.MULTILINE))


def _extract_check_ids(prefix: str, text: str) -> list[int]:
    matches = re.findall(rf"^\s*-\s*{prefix}(\d+):", text, flags=re.MULTILINE)
    return [int(m) for m in matches]


def _extract_status_counts(prefix: str, text: str) -> tuple[int, int]:
    lines = re.findall(rf"(?mi)^\s*-\s*{prefix}\d+:\s*(.+)$", text)
    pass_count = 0
    fail_count = 0
    for tail in lines:
        if re.search(r"\bPASS\b", tail):
            pass_count += 1
        if re.search(r"\bFAIL\b", tail):
            fail_count += 1
    return pass_count, fail_count


def _extract_section_reported_ratio(text: str, title_pattern: str) -> tuple[int, int] | None:
    match = re.search(
        rf"(?mi)^\s*-\s*{title_pattern}\s*\((\d+)\s*/\s*(\d+)\s*pass\)",
        text,
    )
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def _failed_check_blocks(text: str) -> list[tuple[str, str]]:
    """Return (check_id, block_body) tuples for each failed check line."""
    pattern = r"(?ms)^\s*-\s*([FVO]\d+):\s*FAIL\b.*?$\n(?P<body>.*?)(?=^\s*-\s*[FVO]\d+:|^\s*-\s*[A-Z][^\n]*checks|^##\s|\Z)"
    blocks: list[tuple[str, str]] = []
    for match in re.finditer(pattern, text):
        blocks.append((match.group(1), match.group("body")))
    return blocks


def _extract_checkpoint_order(text: str) -> list[str]:
    return re.findall(r"(?mi)^\s*-\s*([A-Z]\d+)\s+checkpoint:\s*.+$", text)


def _extract_checkpoint_tails(text: str) -> list[tuple[str, str]]:
    return re.findall(r"(?mi)^\s*-\s*([FVO]\d+)\s+checkpoint:\s*(.+)$", text)


def _extract_checkpoint_timestamps_by_id(text: str) -> dict[str, str]:
    timestamps: dict[str, str] = {}
    for checkpoint_id, tail in _extract_checkpoint_tails(text):
        match = re.search(r"\b(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\b", tail)
        if match is not None:
            timestamps[checkpoint_id] = match.group(1)
    return timestamps


def _extract_checkpoint_target_refs(tail: str) -> list[str]:
    return re.findall(r"\bref=([A-Za-z0-9_.:-]+)\b", tail)


def _extract_checkpoint_artifact_refs(tail: str) -> list[str]:
    return re.findall(
        r"`([^`]+\.(?:png|jpg|jpeg|webp|mp4|log|txt|json|zip|har|trace))`",
        tail,
        flags=re.IGNORECASE,
    )


def _extract_check_status_map(text: str) -> dict[str, str]:
    pairs = re.findall(r"(?mi)^\s*-\s*([FVO]\d+):\s*.*\b(PASS|FAIL)\b", text)
    return {check_id: status.upper() for check_id, status in pairs}


def _extract_checkpoint_status_map(text: str) -> dict[str, str]:
    pairs = re.findall(r"(?mi)^\s*-\s*([FVO]\d+)\s+checkpoint:\s*.*\b(PASS|FAIL)\b", text)
    return {check_id: status.upper() for check_id, status in pairs}


def _extract_iso_utc_timestamp(value: str) -> datetime | None:
    match = re.search(r"\b(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\b", value)
    if not match:
        return None
    return datetime.strptime(match.group(1), "%Y-%m-%dT%H:%M:%SZ")


def _extract_reported_regressions(text: str) -> int | None:
    match = re.search(r"(?mi)^\s*-\s*Regressions:\s*(\d+)\s*$", text)
    if not match:
        return None
    return int(match.group(1))


def _extract_merge_recommendation(text: str) -> str | None:
    match = re.search(
        r"(?mi)^\s*-\s*Merge recommendation:\s*(?:\*\*)?(APPROVE|BLOCK)(?:\*\*)?\s*$",
        text,
    )
    if not match:
        return None
    return match.group(1).upper()


def _extract_replay_readiness(text: str) -> str | None:
    match = re.search(
        r"(?mi)^\s*-\s*Replay readiness:\s*(?:\*\*)?(READY|BLOCKED)(?:\*\*)?\s*$",
        text,
    )
    if not match:
        return None
    return match.group(1).upper()


def _extract_next_action(text: str) -> str | None:
    match = re.search(r"(?mi)^\s*-\s*Next action:\s*(.+)$", text)
    if not match:
        return None
    return match.group(1).strip()


def _has_signoff_section(text: str) -> bool:
    return re.search(r"(?mi)^##\s*4\)\s*Signoff\s*$", text) is not None


def _extract_failed_check_ids(text: str) -> list[str]:
    return [check_id for check_id, _ in _failed_check_blocks(text)]


def _extract_failed_check_classifications(text: str) -> list[str]:
    failed_blocks = _failed_check_blocks(text)
    classifications: list[str] = []
    for _, block in failed_blocks:
        match = re.search(
            r"(?mi)^\s*-\s*Failure classification:\s*(selector|runtime|product)\b",
            block,
        )
        if match is not None:
            classifications.append(match.group(1).lower())
    return classifications


def _extract_failed_check_classifications_by_id(text: str) -> dict[str, str]:
    classifications: dict[str, str] = {}
    for check_id, block in _failed_check_blocks(text):
        match = re.search(
            r"(?mi)^\s*-\s*Failure classification:\s*(selector|runtime|product)\b",
            block,
        )
        if match is not None:
            classifications[check_id] = match.group(1).lower()
    return classifications


def _extract_failed_check_recovery_owners(text: str) -> dict[str, str]:
    owners: dict[str, str] = {}
    for check_id, block in _failed_check_blocks(text):
        match = re.search(r"(?mi)^\s*-\s*Recovery owner:\s*(.+)$", block)
        if match is not None:
            owners[check_id] = match.group(1).strip()
    return owners


def _extract_next_action_failed_check_refs(text: str) -> list[str]:
    next_action = _extract_next_action(text)
    if next_action is None:
        return []
    refs: list[str] = []
    seen: set[str] = set()
    for ref in re.findall(r"\b([FVO]\d+)\b", next_action):
        if ref in seen:
            continue
        seen.add(ref)
        refs.append(ref)
    return refs


def _extract_next_action_target_refs(text: str) -> list[str]:
    next_action = _extract_next_action(text)
    if next_action is None:
        return []
    refs: list[str] = []
    seen: set[str] = set()
    for ref in _extract_checkpoint_target_refs(next_action):
        if ref in seen:
            continue
        seen.add(ref)
        refs.append(ref)
    return refs


def _extract_next_action_artifact_refs(text: str) -> list[str]:
    next_action = _extract_next_action(text)
    if next_action is None:
        return []
    refs: list[str] = []
    seen: set[str] = set()
    for ref in _extract_checkpoint_artifact_refs(next_action):
        if ref in seen:
            continue
        seen.add(ref)
        refs.append(ref)
    return refs


def _next_action_mentions_rerun(text: str) -> bool:
    next_action = _extract_next_action(text)
    if next_action is None:
        return False
    return re.search(r"\b(rerun|re-run|replay|re-test|retest|retry)\b", next_action, flags=re.IGNORECASE) is not None


def _summarize_checkpoint_sections(checkpoint_order: list[str]) -> dict[str, int]:
    counts = {"functional": 0, "visual": 0, "off_happy": 0}
    for checkpoint_id in checkpoint_order:
        if checkpoint_id.startswith("F"):
            counts["functional"] += 1
        elif checkpoint_id.startswith("V"):
            counts["visual"] += 1
        elif checkpoint_id.startswith("O"):
            counts["off_happy"] += 1
    return counts


def _build_report_metadata(text: str) -> dict[str, object]:
    failed_check_ids = _extract_failed_check_ids(text)
    checkpoint_order = _extract_checkpoint_order(text)
    expected_checkpoint_order = [
        "F1", "F2", "F3", "F4", "F5",
        "V1", "V2", "V3",
        "O1", "O2",
    ]
    missing_checkpoint_ids = [checkpoint_id for checkpoint_id in expected_checkpoint_order if checkpoint_id not in checkpoint_order]
    unexpected_checkpoint_ids = [checkpoint_id for checkpoint_id in checkpoint_order if checkpoint_id not in expected_checkpoint_order]
    checkpoint_section_counts = _summarize_checkpoint_sections(checkpoint_order)
    checkpoint_count = len(checkpoint_order)
    checkpoint_timestamps_by_id = _extract_checkpoint_timestamps_by_id(text)
    missing_checkpoint_timestamp_ids = [
        checkpoint_id for checkpoint_id in checkpoint_order if checkpoint_id not in checkpoint_timestamps_by_id
    ]
    checkpoint_timestamp_count = len(checkpoint_timestamps_by_id)
    checkpoint_timestamp_coverage_rate = round(
        checkpoint_timestamp_count / checkpoint_count, 4
    ) if checkpoint_count else 0.0
    missing_checkpoint_timestamp_ids_by_section = {
        "functional": [checkpoint_id for checkpoint_id in missing_checkpoint_timestamp_ids if checkpoint_id.startswith("F")],
        "visual": [checkpoint_id for checkpoint_id in missing_checkpoint_timestamp_ids if checkpoint_id.startswith("V")],
        "off_happy": [checkpoint_id for checkpoint_id in missing_checkpoint_timestamp_ids if checkpoint_id.startswith("O")],
    }
    checkpoint_timestamp_count_by_section = {
        "functional": sum(1 for checkpoint_id in checkpoint_timestamps_by_id if checkpoint_id.startswith("F")),
        "visual": sum(1 for checkpoint_id in checkpoint_timestamps_by_id if checkpoint_id.startswith("V")),
        "off_happy": sum(1 for checkpoint_id in checkpoint_timestamps_by_id if checkpoint_id.startswith("O")),
    }
    checkpoint_timestamp_coverage_rate_by_section = {
        section: round(
            checkpoint_timestamp_count_by_section[section] / checkpoint_section_counts[section],
            4,
        ) if checkpoint_section_counts[section] else 0.0
        for section in checkpoint_section_counts
    }
    checkpoint_target_refs: list[str] = []
    checkpoint_artifact_refs: list[str] = []
    checkpoint_target_refs_by_id: dict[str, list[str]] = {}
    checkpoint_artifact_refs_by_id: dict[str, list[str]] = {}
    checkpoint_reused_target_refs: list[str] = []
    checkpoint_reused_artifact_refs: list[str] = []
    checkpoint_reused_target_refs_by_id: dict[str, list[str]] = {}
    checkpoint_reused_artifact_refs_by_id: dict[str, list[str]] = {}
    seen_target_refs: set[str] = set()
    seen_artifact_refs: set[str] = set()
    for checkpoint_id, tail in _extract_checkpoint_tails(text):
        target_refs = _extract_checkpoint_target_refs(tail)
        artifact_refs = _extract_checkpoint_artifact_refs(tail)
        if target_refs:
            checkpoint_target_refs_by_id[checkpoint_id] = target_refs
        if artifact_refs:
            checkpoint_artifact_refs_by_id[checkpoint_id] = artifact_refs
        for target_ref in target_refs:
            if target_ref in seen_target_refs:
                if target_ref not in checkpoint_reused_target_refs:
                    checkpoint_reused_target_refs.append(target_ref)
                checkpoint_reused_target_refs_by_id.setdefault(checkpoint_id, [])
                if target_ref not in checkpoint_reused_target_refs_by_id[checkpoint_id]:
                    checkpoint_reused_target_refs_by_id[checkpoint_id].append(target_ref)
                continue
            seen_target_refs.add(target_ref)
            checkpoint_target_refs.append(target_ref)
        for artifact_ref in artifact_refs:
            if artifact_ref in seen_artifact_refs:
                if artifact_ref not in checkpoint_reused_artifact_refs:
                    checkpoint_reused_artifact_refs.append(artifact_ref)
                checkpoint_reused_artifact_refs_by_id.setdefault(checkpoint_id, [])
                if artifact_ref not in checkpoint_reused_artifact_refs_by_id[checkpoint_id]:
                    checkpoint_reused_artifact_refs_by_id[checkpoint_id].append(artifact_ref)
                continue
            seen_artifact_refs.add(artifact_ref)
            checkpoint_artifact_refs.append(artifact_ref)
    checkpoint_target_ref_id_count = len(checkpoint_target_refs_by_id)
    checkpoint_target_ref_id_count_by_section = {
        "functional": sum(1 for checkpoint_id in checkpoint_target_refs_by_id if checkpoint_id.startswith("F")),
        "visual": sum(1 for checkpoint_id in checkpoint_target_refs_by_id if checkpoint_id.startswith("V")),
        "off_happy": sum(1 for checkpoint_id in checkpoint_target_refs_by_id if checkpoint_id.startswith("O")),
    }
    checkpoint_target_ref_coverage_rate = (checkpoint_target_ref_id_count / checkpoint_count) if checkpoint_count else 0.0
    checkpoint_artifact_ref_id_count = len(checkpoint_artifact_refs_by_id)
    checkpoint_artifact_ref_id_count_by_section = {
        "functional": sum(1 for checkpoint_id in checkpoint_artifact_refs_by_id if checkpoint_id.startswith("F")),
        "visual": sum(1 for checkpoint_id in checkpoint_artifact_refs_by_id if checkpoint_id.startswith("V")),
        "off_happy": sum(1 for checkpoint_id in checkpoint_artifact_refs_by_id if checkpoint_id.startswith("O")),
    }
    checkpoint_artifact_ref_coverage_rate = (checkpoint_artifact_ref_id_count / checkpoint_count) if checkpoint_count else 0.0
    checkpoint_evidence_ref_ids = [
        checkpoint_id
        for checkpoint_id in checkpoint_order
        if checkpoint_id in checkpoint_target_refs_by_id and checkpoint_id in checkpoint_artifact_refs_by_id
    ]
    checkpoint_evidence_ref_ids_by_section = {
        "functional": [checkpoint_id for checkpoint_id in checkpoint_evidence_ref_ids if checkpoint_id.startswith("F")],
        "visual": [checkpoint_id for checkpoint_id in checkpoint_evidence_ref_ids if checkpoint_id.startswith("V")],
        "off_happy": [checkpoint_id for checkpoint_id in checkpoint_evidence_ref_ids if checkpoint_id.startswith("O")],
    }
    checkpoint_evidence_ref_count_by_section = {
        section: len(checkpoint_evidence_ref_ids_by_section[section])
        for section in checkpoint_evidence_ref_ids_by_section
    }
    checkpoint_evidence_ref_coverage_rate = (len(checkpoint_evidence_ref_ids) / checkpoint_count) if checkpoint_count else 0.0
    checkpoint_evidence_ref_coverage_rate_by_section = {
        section: round(
            checkpoint_evidence_ref_count_by_section[section] / checkpoint_section_counts[section],
            4,
        ) if checkpoint_section_counts[section] else 0.0
        for section in checkpoint_section_counts
    }
    missing_checkpoint_evidence_ref_ids = [
        checkpoint_id for checkpoint_id in checkpoint_order if checkpoint_id not in checkpoint_evidence_ref_ids
    ]
    missing_checkpoint_evidence_dimensions_by_id = {
        checkpoint_id: [
            dimension
            for dimension, present in (
                ("target_ref", checkpoint_id in checkpoint_target_refs_by_id),
                ("artifact_ref", checkpoint_id in checkpoint_artifact_refs_by_id),
                ("timestamp", checkpoint_id in checkpoint_timestamps_by_id),
            )
            if not present
        ]
        for checkpoint_id in checkpoint_order
    }
    missing_checkpoint_evidence_dimensions_count_by_id = {
        checkpoint_id: len(dimensions)
        for checkpoint_id, dimensions in missing_checkpoint_evidence_dimensions_by_id.items()
    }
    missing_checkpoint_evidence_dimensions_by_section = {
        "functional": {
            checkpoint_id: missing_checkpoint_evidence_dimensions_by_id[checkpoint_id]
            for checkpoint_id in checkpoint_order
            if checkpoint_id.startswith("F") and missing_checkpoint_evidence_dimensions_by_id[checkpoint_id]
        },
        "visual": {
            checkpoint_id: missing_checkpoint_evidence_dimensions_by_id[checkpoint_id]
            for checkpoint_id in checkpoint_order
            if checkpoint_id.startswith("V") and missing_checkpoint_evidence_dimensions_by_id[checkpoint_id]
        },
        "off_happy": {
            checkpoint_id: missing_checkpoint_evidence_dimensions_by_id[checkpoint_id]
            for checkpoint_id in checkpoint_order
            if checkpoint_id.startswith("O") and missing_checkpoint_evidence_dimensions_by_id[checkpoint_id]
        },
    }
    missing_checkpoint_evidence_dimension_counts = {
        "target_ref": sum(1 for dimensions in missing_checkpoint_evidence_dimensions_by_id.values() if "target_ref" in dimensions),
        "artifact_ref": sum(1 for dimensions in missing_checkpoint_evidence_dimensions_by_id.values() if "artifact_ref" in dimensions),
        "timestamp": sum(1 for dimensions in missing_checkpoint_evidence_dimensions_by_id.values() if "timestamp" in dimensions),
    }
    missing_checkpoint_evidence_ref_ids_by_section = {
        "functional": [checkpoint_id for checkpoint_id in missing_checkpoint_evidence_ref_ids if checkpoint_id.startswith("F")],
        "visual": [checkpoint_id for checkpoint_id in missing_checkpoint_evidence_ref_ids if checkpoint_id.startswith("V")],
        "off_happy": [checkpoint_id for checkpoint_id in missing_checkpoint_evidence_ref_ids if checkpoint_id.startswith("O")],
    }
    missing_checkpoint_evidence_ref_count_by_section = {
        section: len(missing_checkpoint_evidence_ref_ids_by_section[section])
        for section in missing_checkpoint_evidence_ref_ids_by_section
    }
    missing_checkpoint_evidence_ref_coverage_rate_by_section = {
        section: round(
            missing_checkpoint_evidence_ref_count_by_section[section] / checkpoint_section_counts[section],
            4,
        ) if checkpoint_section_counts[section] else 0.0
        for section in checkpoint_section_counts
    }
    checkpoint_reused_target_ref_count_by_section = {
        "functional": sum(1 for checkpoint_id in checkpoint_reused_target_refs_by_id if checkpoint_id.startswith("F")),
        "visual": sum(1 for checkpoint_id in checkpoint_reused_target_refs_by_id if checkpoint_id.startswith("V")),
        "off_happy": sum(1 for checkpoint_id in checkpoint_reused_target_refs_by_id if checkpoint_id.startswith("O")),
    }
    checkpoint_reused_target_ref_coverage_rate = (len(checkpoint_reused_target_refs_by_id) / checkpoint_count) if checkpoint_count else 0.0
    checkpoint_reused_target_ref_coverage_rate_by_section = {
        section: round(
            checkpoint_reused_target_ref_count_by_section[section] / checkpoint_section_counts[section],
            4,
        ) if checkpoint_section_counts[section] else 0.0
        for section in checkpoint_section_counts
    }
    checkpoint_reused_artifact_ref_count_by_section = {
        "functional": sum(1 for checkpoint_id in checkpoint_reused_artifact_refs_by_id if checkpoint_id.startswith("F")),
        "visual": sum(1 for checkpoint_id in checkpoint_reused_artifact_refs_by_id if checkpoint_id.startswith("V")),
        "off_happy": sum(1 for checkpoint_id in checkpoint_reused_artifact_refs_by_id if checkpoint_id.startswith("O")),
    }
    checkpoint_reused_artifact_ref_coverage_rate = (len(checkpoint_reused_artifact_refs_by_id) / checkpoint_count) if checkpoint_count else 0.0
    checkpoint_reused_artifact_ref_coverage_rate_by_section = {
        section: round(
            checkpoint_reused_artifact_ref_count_by_section[section] / checkpoint_section_counts[section],
            4,
        ) if checkpoint_section_counts[section] else 0.0
        for section in checkpoint_section_counts
    }
    missing_checkpoint_target_ref_ids = [
        checkpoint_id for checkpoint_id in checkpoint_order if checkpoint_id not in checkpoint_target_refs_by_id
    ]
    missing_checkpoint_target_ref_count_by_section = {
        "functional": sum(1 for checkpoint_id in missing_checkpoint_target_ref_ids if checkpoint_id.startswith("F")),
        "visual": sum(1 for checkpoint_id in missing_checkpoint_target_ref_ids if checkpoint_id.startswith("V")),
        "off_happy": sum(1 for checkpoint_id in missing_checkpoint_target_ref_ids if checkpoint_id.startswith("O")),
    }
    missing_checkpoint_target_ref_coverage_rate_by_section = {
        section: round(
            missing_checkpoint_target_ref_count_by_section[section] / checkpoint_section_counts[section],
            4,
        ) if checkpoint_section_counts[section] else 0.0
        for section in checkpoint_section_counts
    }
    missing_checkpoint_artifact_ref_ids = [
        checkpoint_id for checkpoint_id in checkpoint_order if checkpoint_id not in checkpoint_artifact_refs_by_id
    ]
    missing_checkpoint_artifact_ref_count_by_section = {
        "functional": sum(1 for checkpoint_id in missing_checkpoint_artifact_ref_ids if checkpoint_id.startswith("F")),
        "visual": sum(1 for checkpoint_id in missing_checkpoint_artifact_ref_ids if checkpoint_id.startswith("V")),
        "off_happy": sum(1 for checkpoint_id in missing_checkpoint_artifact_ref_ids if checkpoint_id.startswith("O")),
    }
    missing_checkpoint_artifact_ref_coverage_rate_by_section = {
        section: round(
            missing_checkpoint_artifact_ref_count_by_section[section] / checkpoint_section_counts[section],
            4,
        ) if checkpoint_section_counts[section] else 0.0
        for section in checkpoint_section_counts
    }
    failed_check_classifications = _extract_failed_check_classifications(text)
    failed_check_classifications_by_id = _extract_failed_check_classifications_by_id(text)
    failed_check_classification_counts = {"selector": 0, "runtime": 0, "product": 0}
    for classification in failed_check_classifications:
        failed_check_classification_counts[classification] += 1
    failed_check_recovery_owners = _extract_failed_check_recovery_owners(text)
    next_action_failed_check_recovery_owners: dict[str, str] = {}
    unresolved_failed_check_recovery_owners: dict[str, str] = {}
    next_action_failed_check_classification_counts = {"selector": 0, "runtime": 0, "product": 0}
    next_action_failed_check_ids_by_classification = {"selector": [], "runtime": [], "product": []}
    unresolved_failed_check_classification_counts = {"selector": 0, "runtime": 0, "product": 0}
    unresolved_failed_check_ids_by_classification = {"selector": [], "runtime": [], "product": []}
    missing_failed_check_classification_ids = [
        check_id for check_id in failed_check_ids if check_id not in _extract_failed_check_classifications_by_id(text)
    ]
    missing_failed_check_recovery_owner_ids = [
        check_id for check_id in failed_check_ids if check_id not in failed_check_recovery_owners
    ]
    reported_regressions = _extract_reported_regressions(text)
    merge_recommendation = _extract_merge_recommendation(text)
    replay_readiness = _extract_replay_readiness(text)
    next_action = _extract_next_action(text)
    next_action_failed_check_refs = _extract_next_action_failed_check_refs(text)
    next_action_target_refs = _extract_next_action_target_refs(text)
    next_action_artifact_refs = _extract_next_action_artifact_refs(text)
    next_action_mentions_rerun = _next_action_mentions_rerun(text)
    for check_id in next_action_failed_check_refs:
        classification = failed_check_classifications_by_id.get(check_id)
        owner = failed_check_recovery_owners.get(check_id)
        if owner is not None:
            next_action_failed_check_recovery_owners[check_id] = owner
        if classification is not None:
            next_action_failed_check_classification_counts[classification] += 1
            next_action_failed_check_ids_by_classification[classification].append(check_id)
    unresolved_failed_check_ids = [
        check_id for check_id in failed_check_ids if check_id not in next_action_failed_check_refs
    ]
    next_action_references_all_failed_checks = not unresolved_failed_check_ids
    for check_id in unresolved_failed_check_ids:
        classification = failed_check_classifications_by_id.get(check_id)
        owner = failed_check_recovery_owners.get(check_id)
        if owner is not None:
            unresolved_failed_check_recovery_owners[check_id] = owner
        if classification is not None:
            unresolved_failed_check_classification_counts[classification] += 1
            unresolved_failed_check_ids_by_classification[classification].append(check_id)
    qa_inventory_check_refs = _extract_qa_inventory_check_refs(text)
    expected_check_ids = [
        "F1", "F2", "F3", "F4", "F5",
        "V1", "V2", "V3",
        "O1", "O2",
    ]
    qa_inventory_missing_check_refs = [
        check_id for check_id in expected_check_ids if check_id not in qa_inventory_check_refs
    ]
    failed_check_count = len(failed_check_ids)
    qa_inventory_check_ref_coverage_rate = round(
        ((len(expected_check_ids) - len(qa_inventory_missing_check_refs)) / len(expected_check_ids)), 4
    ) if expected_check_ids else 0.0
    failed_check_classification_coverage_rate = round(
        len(failed_check_classifications_by_id) / failed_check_count, 4
    ) if failed_check_count else 1.0
    failed_check_recovery_owner_coverage_rate = round(
        len(failed_check_recovery_owners) / failed_check_count, 4
    ) if failed_check_count else 1.0
    next_action_failed_check_coverage_rate = round(
        len(next_action_failed_check_refs) / failed_check_count, 4
    ) if failed_check_count else 1.0
    next_action_failed_check_coverage_rate_by_classification = {
        classification: round(
            (
                next_action_failed_check_classification_counts[classification]
                / failed_check_classification_counts[classification]
            ),
            4,
        )
        if failed_check_classification_counts[classification]
        else 1.0
        for classification in next_action_failed_check_classification_counts
    }
    unresolved_failed_check_coverage_rate_by_classification = {
        classification: round(
            (
                unresolved_failed_check_classification_counts[classification]
                / failed_check_classification_counts[classification]
            ),
            4,
        )
        if failed_check_classification_counts[classification]
        else 0.0
        for classification in unresolved_failed_check_classification_counts
    }
    replay_readiness_reference_regressions = (
        reported_regressions if reported_regressions is not None else failed_check_count
    )
    signoff_field_values = {
        "regressions": reported_regressions,
        "merge_recommendation": merge_recommendation,
        "replay_readiness": replay_readiness,
        "next_action": next_action,
    }
    missing_signoff_fields = [field for field, value in signoff_field_values.items() if value is None]
    present_signoff_fields = [field for field, value in signoff_field_values.items() if value is not None]
    signoff_field_status = {
        field: ("present" if value is not None else "missing")
        for field, value in signoff_field_values.items()
    }
    signoff_field_coverage_rate = round(
        (len(signoff_field_values) - len(missing_signoff_fields)) / len(signoff_field_values), 4
    ) if signoff_field_values else 1.0
    replay_readiness_consistent_with_failed_checks = (
        replay_readiness is None
        or (replay_readiness_reference_regressions == 0 and replay_readiness == "READY")
        or (replay_readiness_reference_regressions > 0 and replay_readiness == "BLOCKED")
    )
    replay_readiness_blockers: list[str] = []
    replay_readiness_blocker_keys: list[str] = []
    if replay_readiness_reference_regressions == 0 and replay_readiness == "BLOCKED":
        replay_readiness_blockers.append("regressions=0 but replay_readiness=BLOCKED")
        replay_readiness_blocker_keys.append("blocked_without_regressions")
    if replay_readiness_reference_regressions > 0 and replay_readiness == "READY":
        replay_readiness_blockers.append(
            f"regressions={replay_readiness_reference_regressions} but replay_readiness=READY"
        )
        replay_readiness_blocker_keys.append("ready_with_regressions")
    if replay_readiness == "READY" and missing_checkpoint_target_ref_ids:
        replay_readiness_blockers.append(
            "replay_readiness=READY but checkpoint target refs are missing for "
            + ", ".join(missing_checkpoint_target_ref_ids)
        )
        replay_readiness_blocker_keys.append("missing_target_refs")
    if replay_readiness == "READY" and missing_checkpoint_artifact_ref_ids:
        replay_readiness_blockers.append(
            "replay_readiness=READY but checkpoint artifact refs are missing for "
            + ", ".join(missing_checkpoint_artifact_ref_ids)
        )
        replay_readiness_blocker_keys.append("missing_artifact_refs")
    if replay_readiness == "READY" and missing_checkpoint_evidence_ref_ids:
        replay_readiness_blockers.append(
            "replay_readiness=READY but checkpoint evidence refs are incomplete for "
            + ", ".join(missing_checkpoint_evidence_ref_ids)
        )
        replay_readiness_blocker_keys.append("incomplete_evidence_refs")
    if replay_readiness == "READY" and missing_checkpoint_timestamp_ids:
        replay_readiness_blockers.append(
            "replay_readiness=READY but checkpoint timestamps are missing for "
            + ", ".join(missing_checkpoint_timestamp_ids)
        )
        replay_readiness_blocker_keys.append("missing_timestamps")
    replay_readiness_blocker_counts = {
        blocker_key: replay_readiness_blocker_keys.count(blocker_key)
        for blocker_key in [
            "blocked_without_regressions",
            "ready_with_regressions",
            "missing_target_refs",
            "missing_artifact_refs",
            "incomplete_evidence_refs",
            "missing_timestamps",
        ]
    }
    replay_readiness_blocker_count_by_section = {
        section: 0 for section in checkpoint_section_counts
    }
    replay_readiness_blocker_keys_by_section = {
        section: [] for section in checkpoint_section_counts
    }
    if replay_readiness == "READY":
        for section, count in missing_checkpoint_target_ref_count_by_section.items():
            replay_readiness_blocker_count_by_section[section] += count
            if count:
                replay_readiness_blocker_keys_by_section[section].append("missing_target_refs")
        for section, count in missing_checkpoint_artifact_ref_count_by_section.items():
            replay_readiness_blocker_count_by_section[section] += count
            if count:
                replay_readiness_blocker_keys_by_section[section].append("missing_artifact_refs")
        for section, count in missing_checkpoint_timestamp_ids_by_section.items():
            replay_readiness_blocker_count_by_section[section] += len(count)
            if count:
                replay_readiness_blocker_keys_by_section[section].append("missing_timestamps")
        for section, count in missing_checkpoint_evidence_ref_count_by_section.items():
            replay_readiness_blocker_count_by_section[section] += count
            if count:
                replay_readiness_blocker_keys_by_section[section].append("incomplete_evidence_refs")
    replay_readiness_blocker_coverage_rate_by_section = {
        section: round(
            replay_readiness_blocker_count_by_section[section] / checkpoint_section_counts[section],
            4,
        ) if checkpoint_section_counts[section] else 0.0
        for section in checkpoint_section_counts
    }
    effective_replay_readiness_blocker_keys_by_section = {
        section: list(keys) for section, keys in replay_readiness_blocker_keys_by_section.items()
    }
    effective_replay_readiness_blocker_count_by_section = {
        section: replay_readiness_blocker_count_by_section[section]
        for section in checkpoint_section_counts
    }
    if replay_readiness == "READY" and replay_readiness_reference_regressions > 0:
        for section, count in checkpoint_section_counts.items():
            if count and "ready_with_regressions" not in effective_replay_readiness_blocker_keys_by_section[section]:
                effective_replay_readiness_blocker_keys_by_section[section].insert(0, "ready_with_regressions")
                effective_replay_readiness_blocker_count_by_section[section] += count
    effective_replay_readiness_blocker_coverage_rate_by_section = {
        section: round(
            effective_replay_readiness_blocker_count_by_section[section] / checkpoint_section_counts[section],
            4,
        ) if checkpoint_section_counts[section] else 0.0
        for section in checkpoint_section_counts
    }
    effective_replay_readiness_added_blocker_keys_by_section = {
        section: [
            key
            for key in effective_replay_readiness_blocker_keys_by_section[section]
            if key not in replay_readiness_blocker_keys_by_section[section]
        ]
        for section in checkpoint_section_counts
    }
    effective_replay_readiness_blocker_delta_by_section = {
        section: (
            effective_replay_readiness_blocker_count_by_section[section]
            - replay_readiness_blocker_count_by_section[section]
        )
        for section in checkpoint_section_counts
    }
    hotspot_sections = [
        section
        for section, count in effective_replay_readiness_blocker_count_by_section.items()
        if count == max(effective_replay_readiness_blocker_count_by_section.values(), default=0) and count > 0
    ]
    effective_replay_readiness_hotspot_section = hotspot_sections[0] if hotspot_sections else None
    effective_replay_readiness_hotspot_sections = hotspot_sections
    effective_replay_readiness_hotspot_count = (
        effective_replay_readiness_blocker_count_by_section[effective_replay_readiness_hotspot_section]
        if effective_replay_readiness_hotspot_section is not None
        else 0
    )
    effective_replay_readiness_hotspot_blocker_keys = (
        list(effective_replay_readiness_blocker_keys_by_section[effective_replay_readiness_hotspot_section])
        if effective_replay_readiness_hotspot_section is not None
        else []
    )
    checkpoint_ids_by_section = {
        "functional": [checkpoint_id for checkpoint_id in checkpoint_order if checkpoint_id.startswith("F")],
        "visual": [checkpoint_id for checkpoint_id in checkpoint_order if checkpoint_id.startswith("V")],
        "off_happy": [checkpoint_id for checkpoint_id in checkpoint_order if checkpoint_id.startswith("O")],
    }
    effective_replay_readiness_hotspot_checkpoint_ids_by_section = {
        section: list(checkpoint_ids_by_section[section])
        for section in hotspot_sections
    }
    effective_replay_readiness_hotspot_checkpoint_count_by_section = {
        section: len(checkpoint_ids_by_section[section])
        for section in hotspot_sections
    }
    effective_replay_readiness_hotspot_checkpoint_share_by_section = {
        section: round(
            len(checkpoint_ids_by_section[section]) / checkpoint_section_counts[section],
            4,
        )
        if checkpoint_section_counts[section]
        else 0.0
        for section in hotspot_sections
    }
    effective_replay_readiness_hotspot_summaries = [
        {
            "section": section,
            "count": effective_replay_readiness_blocker_count_by_section[section],
            "coverage_rate": effective_replay_readiness_blocker_coverage_rate_by_section[section],
            "blocker_keys": list(effective_replay_readiness_blocker_keys_by_section[section]),
            "checkpoint_ids": list(checkpoint_ids_by_section[section]),
        }
        for section in hotspot_sections
    ]
    effective_replay_readiness_blocker_keys = list(replay_readiness_blocker_keys)
    effective_replay_readiness_blocker_counts = dict(replay_readiness_blocker_counts)
    if replay_readiness == "READY" and replay_readiness_reference_regressions > 0:
        if "ready_with_regressions" not in effective_replay_readiness_blocker_keys:
            effective_replay_readiness_blocker_keys.insert(0, "ready_with_regressions")
        effective_replay_readiness_blocker_counts["ready_with_regressions"] = 1
    effective_replay_readiness_blocker_count = len(effective_replay_readiness_blocker_keys)
    effective_replay_readiness = replay_readiness
    if replay_readiness == "READY" and replay_readiness_blockers:
        effective_replay_readiness = "BLOCKED"
    replay_readiness_effective_changed = effective_replay_readiness != replay_readiness
    return {
        "has_signoff_section": _has_signoff_section(text),
        "reported_regressions": reported_regressions,
        "merge_recommendation": merge_recommendation,
        "replay_readiness": replay_readiness,
        "effective_replay_readiness": effective_replay_readiness,
        "replay_readiness_effective_changed": replay_readiness_effective_changed,
        "replay_readiness_reference_regressions": replay_readiness_reference_regressions,
        "replay_readiness_consistent_with_failed_checks": replay_readiness_consistent_with_failed_checks,
        "replay_readiness_blockers": replay_readiness_blockers,
        "replay_readiness_blocker_keys": replay_readiness_blocker_keys,
        "replay_readiness_blocker_counts": replay_readiness_blocker_counts,
        "replay_readiness_blocker_count_by_section": replay_readiness_blocker_count_by_section,
        "replay_readiness_blocker_keys_by_section": replay_readiness_blocker_keys_by_section,
        "replay_readiness_blocker_coverage_rate_by_section": replay_readiness_blocker_coverage_rate_by_section,
        "effective_replay_readiness_blocker_keys": effective_replay_readiness_blocker_keys,
        "effective_replay_readiness_blocker_counts": effective_replay_readiness_blocker_counts,
        "effective_replay_readiness_blocker_count": effective_replay_readiness_blocker_count,
        "effective_replay_readiness_blocker_keys_by_section": effective_replay_readiness_blocker_keys_by_section,
        "effective_replay_readiness_blocker_count_by_section": effective_replay_readiness_blocker_count_by_section,
        "effective_replay_readiness_blocker_coverage_rate_by_section": effective_replay_readiness_blocker_coverage_rate_by_section,
        "effective_replay_readiness_added_blocker_keys_by_section": effective_replay_readiness_added_blocker_keys_by_section,
        "effective_replay_readiness_blocker_delta_by_section": effective_replay_readiness_blocker_delta_by_section,
        "effective_replay_readiness_hotspot_section": effective_replay_readiness_hotspot_section,
        "effective_replay_readiness_hotspot_sections": effective_replay_readiness_hotspot_sections,
        "effective_replay_readiness_hotspot_count": effective_replay_readiness_hotspot_count,
        "effective_replay_readiness_hotspot_blocker_keys": effective_replay_readiness_hotspot_blocker_keys,
        "effective_replay_readiness_hotspot_checkpoint_ids_by_section": effective_replay_readiness_hotspot_checkpoint_ids_by_section,
        "effective_replay_readiness_hotspot_checkpoint_count_by_section": effective_replay_readiness_hotspot_checkpoint_count_by_section,
        "effective_replay_readiness_hotspot_checkpoint_share_by_section": effective_replay_readiness_hotspot_checkpoint_share_by_section,
        "effective_replay_readiness_hotspot_summaries": effective_replay_readiness_hotspot_summaries,
        "replay_readiness_blocker_count": len(replay_readiness_blockers),
        "signoff_field_values": signoff_field_values,
        "signoff_field_status": signoff_field_status,
        "present_signoff_fields": present_signoff_fields,
        "present_signoff_field_count": len(present_signoff_fields),
        "missing_signoff_fields": missing_signoff_fields,
        "missing_signoff_field_count": len(missing_signoff_fields),
        "signoff_field_coverage_rate": signoff_field_coverage_rate,
        "has_next_action": next_action is not None,
        "next_action_text": next_action,
        "failed_check_ids": failed_check_ids,
        "failed_check_count": failed_check_count,
        "failed_check_classifications": failed_check_classifications,
        "failed_check_classifications_by_id": failed_check_classifications_by_id,
        "failed_check_classification_counts": failed_check_classification_counts,
        "failed_check_classification_coverage_rate": failed_check_classification_coverage_rate,
        "missing_failed_check_classification_ids": missing_failed_check_classification_ids,
        "missing_failed_check_classification_count": len(missing_failed_check_classification_ids),
        "failed_check_recovery_owners": failed_check_recovery_owners,
        "failed_check_recovery_owner_count": len(failed_check_recovery_owners),
        "failed_check_recovery_owner_coverage_rate": failed_check_recovery_owner_coverage_rate,
        "missing_failed_check_recovery_owner_ids": missing_failed_check_recovery_owner_ids,
        "missing_failed_check_recovery_owner_count": len(missing_failed_check_recovery_owner_ids),
        "next_action": next_action,
        "next_action_failed_check_refs": next_action_failed_check_refs,
        "next_action_failed_check_ref_count": len(next_action_failed_check_refs),
        "next_action_failed_check_coverage_rate": next_action_failed_check_coverage_rate,
        "next_action_target_refs": next_action_target_refs,
        "next_action_target_ref_count": len(next_action_target_refs),
        "next_action_artifact_refs": next_action_artifact_refs,
        "next_action_artifact_ref_count": len(next_action_artifact_refs),
        "next_action_mentions_rerun": next_action_mentions_rerun,
        "next_action_failed_check_classification_counts": next_action_failed_check_classification_counts,
        "next_action_failed_check_ids_by_classification": next_action_failed_check_ids_by_classification,
        "next_action_failed_check_classifications_by_id": {
            check_id: failed_check_classifications_by_id[check_id]
            for check_id in next_action_failed_check_refs
            if check_id in failed_check_classifications_by_id
        },
        "next_action_failed_check_coverage_rate_by_classification": next_action_failed_check_coverage_rate_by_classification,
        "next_action_failed_check_recovery_owners": next_action_failed_check_recovery_owners,
        "next_action_failed_check_recovery_owner_count": len(next_action_failed_check_recovery_owners),
        "unresolved_failed_check_ids": unresolved_failed_check_ids,
        "unresolved_failed_check_count": len(unresolved_failed_check_ids),
        "next_action_references_all_failed_checks": next_action_references_all_failed_checks,
        "unresolved_failed_check_classification_counts": unresolved_failed_check_classification_counts,
        "unresolved_failed_check_ids_by_classification": unresolved_failed_check_ids_by_classification,
        "unresolved_failed_check_classifications_by_id": {
            check_id: failed_check_classifications_by_id[check_id]
            for check_id in unresolved_failed_check_ids
            if check_id in failed_check_classifications_by_id
        },
        "unresolved_failed_check_coverage_rate_by_classification": unresolved_failed_check_coverage_rate_by_classification,
        "unresolved_failed_check_recovery_owners": unresolved_failed_check_recovery_owners,
        "unresolved_failed_check_recovery_owner_count": len(unresolved_failed_check_recovery_owners),
        "qa_inventory_check_refs": qa_inventory_check_refs,
        "qa_inventory_check_ref_count": len(qa_inventory_check_refs),
        "qa_inventory_check_ref_coverage_rate": qa_inventory_check_ref_coverage_rate,
        "qa_inventory_missing_check_refs": qa_inventory_missing_check_refs,
        "qa_inventory_missing_check_ref_count": len(qa_inventory_missing_check_refs),
        "checkpoint_order": checkpoint_order,
        "checkpoint_count": checkpoint_count,
        "checkpoint_timestamps_by_id": checkpoint_timestamps_by_id,
        "checkpoint_timestamp_count": checkpoint_timestamp_count,
        "checkpoint_timestamp_count_by_section": checkpoint_timestamp_count_by_section,
        "missing_checkpoint_timestamp_ids": missing_checkpoint_timestamp_ids,
        "missing_checkpoint_timestamp_count": len(missing_checkpoint_timestamp_ids),
        "missing_checkpoint_timestamp_ids_by_section": missing_checkpoint_timestamp_ids_by_section,
        "missing_checkpoint_timestamp_count_by_section": {
            section: len(missing_checkpoint_timestamp_ids_by_section[section])
            for section in missing_checkpoint_timestamp_ids_by_section
        },
        "checkpoint_timestamp_coverage_rate": checkpoint_timestamp_coverage_rate,
        "checkpoint_timestamp_coverage_rate_by_section": checkpoint_timestamp_coverage_rate_by_section,
        "missing_checkpoint_timestamp_coverage_rate_by_section": {
            section: round(
                (
                    len(missing_checkpoint_timestamp_ids_by_section[section]) / checkpoint_section_counts[section]
                    if checkpoint_section_counts[section]
                    else 0.0
                ),
                4,
            )
            for section in missing_checkpoint_timestamp_ids_by_section
        },
        "checkpoint_section_counts": checkpoint_section_counts,
        "missing_checkpoint_ids": missing_checkpoint_ids,
        "missing_checkpoint_count": len(missing_checkpoint_ids),
        "unexpected_checkpoint_ids": unexpected_checkpoint_ids,
        "unexpected_checkpoint_count": len(unexpected_checkpoint_ids),
        "checkpoint_target_refs": checkpoint_target_refs,
        "checkpoint_target_ref_count": len(checkpoint_target_refs),
        "checkpoint_target_ref_id_count": checkpoint_target_ref_id_count,
        "checkpoint_target_ref_id_count_by_section": checkpoint_target_ref_id_count_by_section,
        "checkpoint_target_ref_coverage_rate": checkpoint_target_ref_coverage_rate,
        "checkpoint_target_refs_by_id": checkpoint_target_refs_by_id,
        "missing_checkpoint_target_ref_ids": missing_checkpoint_target_ref_ids,
        "missing_checkpoint_target_ref_count": len(missing_checkpoint_target_ref_ids),
        "missing_checkpoint_target_ref_count_by_section": missing_checkpoint_target_ref_count_by_section,
        "missing_checkpoint_target_ref_coverage_rate_by_section": missing_checkpoint_target_ref_coverage_rate_by_section,
        "checkpoint_reused_target_refs": checkpoint_reused_target_refs,
        "checkpoint_reused_target_ref_count": len(checkpoint_reused_target_refs),
        "checkpoint_reused_target_ref_id_count": len(checkpoint_reused_target_refs_by_id),
        "checkpoint_reused_target_ref_count_by_section": checkpoint_reused_target_ref_count_by_section,
        "checkpoint_reused_target_ref_coverage_rate": checkpoint_reused_target_ref_coverage_rate,
        "checkpoint_reused_target_ref_coverage_rate_by_section": checkpoint_reused_target_ref_coverage_rate_by_section,
        "checkpoint_reused_target_refs_by_id": checkpoint_reused_target_refs_by_id,
        "checkpoint_artifact_refs": checkpoint_artifact_refs,
        "checkpoint_artifact_ref_count": len(checkpoint_artifact_refs),
        "checkpoint_artifact_ref_id_count": checkpoint_artifact_ref_id_count,
        "checkpoint_artifact_ref_id_count_by_section": checkpoint_artifact_ref_id_count_by_section,
        "checkpoint_artifact_ref_coverage_rate": checkpoint_artifact_ref_coverage_rate,
        "checkpoint_evidence_ref_ids": checkpoint_evidence_ref_ids,
        "checkpoint_evidence_ref_ids_by_section": checkpoint_evidence_ref_ids_by_section,
        "checkpoint_evidence_ref_count": len(checkpoint_evidence_ref_ids),
        "checkpoint_evidence_ref_count_by_section": checkpoint_evidence_ref_count_by_section,
        "checkpoint_evidence_ref_coverage_rate": checkpoint_evidence_ref_coverage_rate,
        "checkpoint_evidence_ref_coverage_rate_by_section": checkpoint_evidence_ref_coverage_rate_by_section,
        "missing_checkpoint_evidence_ref_ids": missing_checkpoint_evidence_ref_ids,
        "missing_checkpoint_evidence_ref_count": len(missing_checkpoint_evidence_ref_ids),
        "missing_checkpoint_evidence_ref_ids_by_section": missing_checkpoint_evidence_ref_ids_by_section,
        "missing_checkpoint_evidence_ref_count_by_section": missing_checkpoint_evidence_ref_count_by_section,
        "missing_checkpoint_evidence_ref_coverage_rate_by_section": missing_checkpoint_evidence_ref_coverage_rate_by_section,
        "missing_checkpoint_evidence_dimensions_by_id": missing_checkpoint_evidence_dimensions_by_id,
        "missing_checkpoint_evidence_dimensions_count_by_id": missing_checkpoint_evidence_dimensions_count_by_id,
        "missing_checkpoint_evidence_dimensions_by_section": missing_checkpoint_evidence_dimensions_by_section,
        "missing_checkpoint_evidence_dimension_counts": missing_checkpoint_evidence_dimension_counts,
        "checkpoint_artifact_refs_by_id": checkpoint_artifact_refs_by_id,
        "missing_checkpoint_artifact_ref_ids": missing_checkpoint_artifact_ref_ids,
        "missing_checkpoint_artifact_ref_count": len(missing_checkpoint_artifact_ref_ids),
        "missing_checkpoint_artifact_ref_count_by_section": missing_checkpoint_artifact_ref_count_by_section,
        "missing_checkpoint_artifact_ref_coverage_rate_by_section": missing_checkpoint_artifact_ref_coverage_rate_by_section,
        "checkpoint_reused_artifact_refs": checkpoint_reused_artifact_refs,
        "checkpoint_reused_artifact_ref_count": len(checkpoint_reused_artifact_refs),
        "checkpoint_reused_artifact_ref_id_count": len(checkpoint_reused_artifact_refs_by_id),
        "checkpoint_reused_artifact_ref_count_by_section": checkpoint_reused_artifact_ref_count_by_section,
        "checkpoint_reused_artifact_ref_coverage_rate": checkpoint_reused_artifact_ref_coverage_rate,
        "checkpoint_reused_artifact_ref_coverage_rate_by_section": checkpoint_reused_artifact_ref_coverage_rate_by_section,
        "checkpoint_reused_artifact_refs_by_id": checkpoint_reused_artifact_refs_by_id,
    }



def _extract_failure_breakdown_summary(text: str) -> dict[str, int] | None:
    match = re.search(
        r"(?mi)^\s*-\s*Failure breakdown:\s*selector\s*=\s*(\d+)\s*,\s*runtime\s*=\s*(\d+)\s*,\s*product\s*=\s*(\d+)\s*$",
        text,
    )
    if match is None:
        return None
    return {
        "selector": int(match.group(1)),
        "runtime": int(match.group(2)),
        "product": int(match.group(3)),
    }


def _extract_execution_log_body(text: str) -> str:
    match = re.search(r"(?ms)^##\s*3\)\s*Execution log\s*$\n(?P<body>.*?)(?=^##\s|\Z)", text)
    if match is None:
        return ""
    return match.group("body")


def _extract_qa_inventory_body(text: str) -> str:
    match = re.search(r"(?ms)^##\s*1\)\s*QA inventory\s*$\n(?P<body>.*?)(?=^##\s|\Z)", text)
    if match is None:
        return ""
    return match.group("body")


def _extract_qa_inventory_check_refs(text: str) -> list[str]:
    inventory_body = _extract_qa_inventory_body(text)
    refs: list[str] = []
    seen: set[str] = set()
    for line in re.findall(r"(?mi)^\s*-\s+.+$", inventory_body):
        match = re.search(r"Checks:\s*([A-Z0-9, ]+)", line)
        if match is None:
            continue
        for ref in re.findall(r"\b([FVO]\d+)\b", match.group(1)):
            if ref in seen:
                continue
            seen.add(ref)
            refs.append(ref)
    return refs


def validate_report_text(
    text: str,
    strict: bool = False,
    enforce_checkpoint_format: bool = False,
    require_checkpoint_timestamps: bool = False,
    enforce_monotonic_checkpoint_timestamps: bool = False,
    enforce_checkpoint_status_tokens: bool = False,
    require_visual_checkpoint_evidence: bool = False,
    require_checkpoint_artifact_paths: bool = False,
    require_checkpoint_target_refs: bool = False,
    enforce_checkpoint_target_ref_uniqueness: bool = False,
    enforce_checkpoint_artifact_ref_uniqueness: bool = False,
    require_failure_checkpoint_artifact_paths: bool = False,
    require_failure_evidence_artifact_paths: bool = False,
    require_failure_recovery_plan: bool = False,
    require_failure_recovery_owner: bool = False,
    enforce_failure_timestamp_order: bool = False,
    enforce_checkpoint_to_check_status_consistency: bool = False,
    require_failure_classification_summary: bool = False,
    require_execution_log_step_count_match: bool = False,
    require_qa_inventory_section: bool = False,
    require_qa_inventory_check_refs: bool = False,
    require_qa_inventory_full_coverage: bool = False,
    require_signoff_section: bool = False,
    require_replay_readiness: bool = False,
    require_next_action: bool = False,
    require_next_action_failed_check_ref: bool = False,
    require_next_action_all_failed_check_refs: bool = False,
) -> list[str]:
    functional_block = _section_block(text, SECTION_TITLES["functional"])
    visual_block = _section_block(text, SECTION_TITLES["visual"])
    off_happy_block = _section_block(text, SECTION_TITLES["off_happy"])

    functional = _count(r"^\s*-\s*F\d+:", functional_block)
    visual = _count(r"^\s*-\s*V\d+:", visual_block)
    off_happy = _count(r"^\s*-\s*O\d+:", off_happy_block)

    functional_ids = _extract_check_ids("F", functional_block)
    visual_ids = _extract_check_ids("V", visual_block)
    off_happy_ids = _extract_check_ids("O", off_happy_block)

    errors: list[str] = []
    if functional != 5:
        errors.append(f"functional checks must be exactly 5, found {functional}")
    if visual != 3:
        errors.append(f"visual checks must be exactly 3, found {visual}")
    if off_happy != 2:
        errors.append(f"off-happy checks must be exactly 2, found {off_happy}")

    if functional_ids and functional_ids != [1, 2, 3, 4, 5]:
        errors.append("functional checks must be labeled sequentially as F1..F5")
    if visual_ids and visual_ids != [1, 2, 3]:
        errors.append("visual checks must be labeled sequentially as V1..V3")
    if off_happy_ids and off_happy_ids != [1, 2]:
        errors.append("off-happy checks must be labeled sequentially as O1..O2")

    if strict:
        reported_functional_ratio = _extract_section_reported_ratio(text, SECTION_TITLES["functional"])
        reported_visual_ratio = _extract_section_reported_ratio(text, SECTION_TITLES["visual"])
        reported_off_happy_ratio = _extract_section_reported_ratio(text, SECTION_TITLES["off_happy"])

        for section_name, reported_ratio in [
            ("Functional checks", reported_functional_ratio),
            ("Visual checks", reported_visual_ratio),
            ("Off-happy-path checks", reported_off_happy_ratio),
        ]:
            if reported_ratio is None:
                errors.append(
                    f"strict mode: {section_name} header must include explicit pass ratio '(x/y pass)'"
                )

        if reported_functional_ratio is not None:
            functional_passes, functional_fails = _extract_status_counts("F", functional_block)
            if reported_functional_ratio[1] != 5:
                errors.append("strict mode: Functional checks header denominator must be 5")
            if functional_passes + functional_fails != 5:
                errors.append("strict mode: Functional checks must declare PASS/FAIL on all 5 lines")
            if reported_functional_ratio[0] != functional_passes:
                errors.append(
                    "strict mode: Functional checks header pass count must match detailed PASS lines"
                )

        if reported_visual_ratio is not None:
            visual_passes, visual_fails = _extract_status_counts("V", visual_block)
            if reported_visual_ratio[1] != 3:
                errors.append("strict mode: Visual checks header denominator must be 3")
            if visual_passes + visual_fails != 3:
                errors.append("strict mode: Visual checks must declare PASS/FAIL on all 3 lines")
            if reported_visual_ratio[0] != visual_passes:
                errors.append(
                    "strict mode: Visual checks header pass count must match detailed PASS lines"
                )

        if reported_off_happy_ratio is not None:
            off_happy_passes, off_happy_fails = _extract_status_counts("O", off_happy_block)
            if reported_off_happy_ratio[1] != 2:
                errors.append("strict mode: Off-happy-path checks header denominator must be 2")
            if off_happy_passes + off_happy_fails != 2:
                errors.append("strict mode: Off-happy-path checks must declare PASS/FAIL on all 2 lines")
            if reported_off_happy_ratio[0] != off_happy_passes:
                errors.append(
                    "strict mode: Off-happy-path checks header pass count must match detailed PASS lines"
                )

        if not re.search(r"(?mi)^-\s*URL:\s*`?https?://", text):
            errors.append("strict mode: scope must include a concrete URL")
        if not re.search(r"(?mi)^-\s*Viewport:\s*`?\d{3,4}x\d{3,4}`?", text):
            errors.append("strict mode: scope must include a deterministic viewport (e.g. 1366x768)")
        if not re.search(r"(?mi)^-\s*Test account:\s*`?.+`?", text):
            errors.append("strict mode: scope must include a test account")

        visual_shot_refs = _count(r"`[^`]+\.(png|jpg|jpeg|webp)`", visual_block)
        if visual_shot_refs < 3:
            errors.append(
                "strict mode: visual checks must include at least 3 screenshot references"
            )

        visual_lines = re.findall(r"(?mi)^\s*-\s*V\d+:.*$", visual_block)
        missing_visual_evidence = [
            line.strip()
            for line in visual_lines
            if re.search(r"`[^`]+\.(png|jpg|jpeg|webp)`", line) is None
        ]
        if missing_visual_evidence:
            errors.append(
                "strict mode: every visual check line must include inline screenshot evidence"
            )

        checklist_body = "\n".join([functional_block, visual_block, off_happy_block])
        all_check_lines = re.findall(r"(?mi)^\s*-\s*([FVO]\d+):\s*(.+)$", checklist_body)
        invalid_status_lines = [
            check_id
            for check_id, tail in all_check_lines
            if re.search(r"\b(PASS|FAIL)\b", tail) is None
        ]
        if invalid_status_lines:
            errors.append(
                "strict mode: every check line must include normalized status token PASS/FAIL "
                f"(invalid: {', '.join(invalid_status_lines)})"
            )

        reported_regressions = _extract_reported_regressions(text)
        if reported_regressions is None:
            errors.append("strict mode: signoff must include explicit regression count")

        merge_recommendation = _extract_merge_recommendation(text)
        if merge_recommendation is None:
            errors.append("strict mode: signoff must include merge recommendation (APPROVE/BLOCK)")

        replay_readiness = _extract_replay_readiness(text)
        if replay_readiness is None:
            errors.append("strict mode: signoff must include replay readiness (READY/BLOCKED)")

        checklist_body = "\n".join([functional_block, visual_block, off_happy_block])
        failed_check_count = len(
            re.findall(r"(?mi)^\s*-\s*[FVO]\d+:\s*.*\bFAIL\b", checklist_body)
        )
        if reported_regressions is not None and reported_regressions != failed_check_count:
            errors.append(
                "strict mode: signoff regressions count must match checklist FAIL count "
                f"(reported {reported_regressions}, found {failed_check_count})"
            )

        if reported_regressions is not None and merge_recommendation is not None:
            if reported_regressions == 0 and merge_recommendation != "APPROVE":
                errors.append(
                    "strict mode: merge recommendation must be APPROVE when regressions are 0"
                )
            if reported_regressions > 0 and merge_recommendation != "BLOCK":
                errors.append(
                    "strict mode: merge recommendation must be BLOCK when regressions are present"
                )

        if reported_regressions is not None and replay_readiness is not None:
            if reported_regressions == 0 and replay_readiness != "READY":
                errors.append(
                    "strict mode: replay readiness must be READY when regressions are 0"
                )
            if reported_regressions > 0 and replay_readiness != "BLOCKED":
                errors.append(
                    "strict mode: replay readiness must be BLOCKED when regressions are present"
                )

        if not re.search(r"(?mi)^##\s*3\)\s*Execution log\s*$", text):
            errors.append(
                "strict mode: report must include an explicit '## 3) Execution log' section header"
            )

        expected_checkpoints = [
            "F1", "F2", "F3", "F4", "F5", "V1", "V2", "V3", "O1", "O2"
        ]
        missing_checkpoints = [
            check_id
            for check_id in expected_checkpoints
            if re.search(rf"(?mi)^\s*-\s*{check_id}\s+checkpoint:\s*.+", text) is None
        ]
        if missing_checkpoints:
            errors.append(
                "strict mode: execution log must include checkpoint lines for all checks "
                f"({', '.join(missing_checkpoints)} missing)"
            )

        checkpoint_lines = _extract_checkpoint_order(text)
        checkpoint_id_counts: dict[str, int] = {}
        for checkpoint_id in checkpoint_lines:
            checkpoint_id_counts[checkpoint_id] = checkpoint_id_counts.get(checkpoint_id, 0) + 1

        duplicate_checkpoint_ids = [
            checkpoint_id
            for checkpoint_id, count in checkpoint_id_counts.items()
            if count > 1
        ]
        if duplicate_checkpoint_ids:
            errors.append(
                "strict mode: execution log must not contain duplicate checkpoint ids "
                f"({', '.join(sorted(duplicate_checkpoint_ids))})"
            )

        unknown_checkpoint_ids = [
            checkpoint_id
            for checkpoint_id in checkpoint_id_counts
            if checkpoint_id not in expected_checkpoints
        ]
        if unknown_checkpoint_ids:
            errors.append(
                "strict mode: execution log includes unknown checkpoint ids "
                f"({', '.join(sorted(unknown_checkpoint_ids))})"
            )

        expected_order_index = {check_id: idx for idx, check_id in enumerate(expected_checkpoints)}
        ordered_known_checkpoints = [
            checkpoint_id for checkpoint_id in checkpoint_lines if checkpoint_id in expected_order_index
        ]
        if ordered_known_checkpoints:
            if ordered_known_checkpoints != sorted(
                ordered_known_checkpoints, key=lambda checkpoint_id: expected_order_index[checkpoint_id]
            ):
                errors.append(
                    "strict mode: execution log checkpoint ids must follow deterministic order "
                    "F1..F5, V1..V3, O1..O2"
                )

        failed_blocks = _failed_check_blocks(text)
        if failed_blocks:
            checkpoint_status_map = _extract_checkpoint_status_map(text)
            failed_timestamps: list[tuple[str, datetime]] = []
            for check_id, block in failed_blocks:
                checkpoint_status = checkpoint_status_map.get(check_id)
                if checkpoint_status != "FAIL":
                    errors.append(
                        "strict mode: failed checks must map to execution-log checkpoints marked FAIL "
                        f"(invalid: {check_id})"
                    )
                if not re.search(r"(?mi)^\s*-\s*Expected:\s*.+", block):
                    errors.append(
                        f"strict mode: failed check {check_id} must include an Expected: line"
                    )
                if not re.search(r"(?mi)^\s*-\s*Observed:\s*.+", block):
                    errors.append(
                        f"strict mode: failed check {check_id} must include an Observed: line"
                    )
                timestamp_match = re.search(
                    r"(?mi)^\s*-\s*First failure timestamp:\s*(.+)$", block
                )
                if not timestamp_match:
                    errors.append(
                        "strict mode: failed check "
                        f"{check_id} must include a First failure timestamp: line"
                    )
                else:
                    timestamp_value = timestamp_match.group(1).strip()
                    if re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", timestamp_value) is None:
                        errors.append(
                            "strict mode: failed check "
                            f"{check_id} must use ISO-8601 UTC timestamp format YYYY-MM-DDTHH:MM:SSZ"
                        )
                    else:
                        failed_timestamps.append(
                            (check_id, datetime.strptime(timestamp_value, "%Y-%m-%dT%H:%M:%SZ"))
                        )
                if not re.search(r"(?mi)^\s*-\s*Retry:\s*(PASS|FAIL)\b", block):
                    errors.append(
                        f"strict mode: failed check {check_id} must include Retry: PASS/FAIL"
                    )
                classification_match = re.search(
                    r"(?mi)^\s*-\s*Failure classification:\s*(selector|runtime|product)\b",
                    block,
                )
                if classification_match is None:
                    errors.append(
                        "strict mode: failed check "
                        f"{check_id} must include Failure classification: selector|runtime|product"
                    )
                if not re.search(r"(?mi)^\s*-\s*Evidence:\s*.+", block):
                    errors.append(
                        f"strict mode: failed check {check_id} must include an Evidence: line"
                    )

            if enforce_failure_timestamp_order and len(failed_timestamps) > 1:
                for idx in range(1, len(failed_timestamps)):
                    prev_id, prev_ts = failed_timestamps[idx - 1]
                    cur_id, cur_ts = failed_timestamps[idx]
                    if cur_ts < prev_ts:
                        errors.append(
                            "strict mode: failed-check First failure timestamp values must be monotonic "
                            f"in checklist order ({prev_id}={prev_ts.strftime('%Y-%m-%dT%H:%M:%SZ')} > "
                            f"{cur_id}={cur_ts.strftime('%Y-%m-%dT%H:%M:%SZ')})"
                        )
                        break

    if require_qa_inventory_section:
        if not re.search(r"(?mi)^##\s*1\)\s*QA inventory\s*$", text):
            errors.append(
                "qa inventory: report must include an explicit '## 1) QA inventory' section header"
            )

    if require_qa_inventory_check_refs:
        inventory_body = _extract_qa_inventory_body(text)
        inventory_lines = re.findall(r"(?mi)^\s*-\s+.+$", inventory_body)
        if not inventory_body.strip():
            errors.append(
                "qa inventory check refs: report must include a non-empty '## 1) QA inventory' section"
            )
        else:
            missing_checks_lines = [line.strip() for line in inventory_lines if "Checks:" not in line]
            if missing_checks_lines:
                errors.append(
                    "qa inventory check refs: every QA inventory bullet must include 'Checks:' mapping"
                )
            inventory_refs = _extract_qa_inventory_check_refs(text)
            unknown_refs = sorted({ref for ref in inventory_refs if ref not in {"F1","F2","F3","F4","F5","V1","V2","V3","O1","O2"}})
            if unknown_refs:
                errors.append(
                    "qa inventory check refs: inventory must reference only known check ids F1..F5, V1..V3, O1..O2 "
                    f"(unknown: {', '.join(unknown_refs)})"
                )
            if not inventory_refs:
                errors.append(
                    "qa inventory check refs: inventory must map claims to at least one checklist id via 'Checks:'"
                )
            if require_qa_inventory_full_coverage and inventory_refs:
                expected_inventory_refs = {"F1", "F2", "F3", "F4", "F5", "V1", "V2", "V3", "O1", "O2"}
                missing_inventory_refs = sorted(expected_inventory_refs - set(inventory_refs))
                if missing_inventory_refs:
                    errors.append(
                        "qa inventory full coverage: inventory must reference every checklist id at least once "
                        f"(missing: {', '.join(missing_inventory_refs)})"
                    )

    if require_signoff_section:
        if not re.search(r"(?mi)^##\s*4\)\s*Signoff\s*$", text):
            errors.append(
                "signoff section: report must include an explicit '## 4) Signoff' section header"
            )

    if require_replay_readiness and _extract_replay_readiness(text) is None:
        errors.append(
            "replay readiness: signoff must include 'Replay readiness: READY' or 'Replay readiness: BLOCKED'"
        )

    next_action = _extract_next_action(text)
    if require_next_action:
        if next_action is None:
            errors.append(
                "next action: signoff must include 'Next action: ...' for explicit handoff"
            )
        elif len(next_action) < 8:
            errors.append(
                "next action: signoff Next action line must be specific enough for the next run (>=8 chars)"
            )

    if require_next_action_failed_check_ref:
        failed_check_ids = _extract_failed_check_ids(text)
        if failed_check_ids and next_action is None:
            errors.append(
                "next action failed-check ref: signoff must include 'Next action: ...' when failed checks need a deterministic owner handoff"
            )
        elif failed_check_ids and not any(re.search(rf"\b{re.escape(check_id)}\b", next_action) for check_id in failed_check_ids):
            errors.append(
                "next action failed-check ref: Next action must reference at least one failed check id "
                f"({', '.join(failed_check_ids)}) so recovery work stays traceable"
            )

    if require_next_action_all_failed_check_refs:
        failed_check_ids = _extract_failed_check_ids(text)
        if failed_check_ids and next_action is None:
            errors.append(
                "next action all failed-check refs: signoff must include 'Next action: ...' when failed checks need a deterministic full handoff"
            )
        elif failed_check_ids:
            unresolved_failed_check_ids = [
                check_id
                for check_id in failed_check_ids
                if re.search(rf"\b{re.escape(check_id)}\b", next_action) is None
            ]
            if unresolved_failed_check_ids:
                errors.append(
                    "next action all failed-check refs: Next action must reference every failed check id "
                    f"({', '.join(failed_check_ids)}; missing: {', '.join(unresolved_failed_check_ids)}) "
                    "so replay recovery keeps a complete deterministic handoff"
                )

    checkpoint_pairs = _extract_checkpoint_tails(text)

    if require_execution_log_step_count_match:
        execution_log_body = _extract_execution_log_body(text)
        if not execution_log_body.strip():
            errors.append(
                "execution log step count: report must include a non-empty '## 3) Execution log' section"
            )
        else:
            execution_log_bullets = re.findall(r"(?mi)^\s*-\s+.+$", execution_log_body)
            checkpoint_lines = re.findall(r"(?mi)^\s*-\s*[FVO]\d+\s+checkpoint:\s*.+$", execution_log_body)
            if len(execution_log_bullets) != len(checkpoint_lines):
                errors.append(
                    "execution log step count: every execution log bullet must be a check checkpoint line "
                    "for deterministic replay"
                )
            expected_checkpoints = ["F1", "F2", "F3", "F4", "F5", "V1", "V2", "V3", "O1", "O2"]
            expected_total_checkpoints = len(expected_checkpoints)
            if len(checkpoint_lines) != expected_total_checkpoints:
                errors.append(
                    "execution log step count: execution log must include exactly 10 checkpoint lines "
                    "(F1..F5, V1..V3, O1..O2)"
                )

            checkpoint_ids = _extract_checkpoint_order(execution_log_body)
            if checkpoint_ids:
                if checkpoint_ids != expected_checkpoints:
                    errors.append(
                        "execution log step count: checkpoint ids must exactly match deterministic order "
                        "F1..F5, V1..V3, O1..O2"
                    )

    if enforce_checkpoint_format:
        malformed_ids = [
            checkpoint_id
            for checkpoint_id, tail in checkpoint_pairs
            if re.fullmatch(r"\s*[^-\s].*\s->\s[^-\s].*\s*", tail) is None
        ]
        if malformed_ids:
            errors.append(
                "checkpoint format: every checkpoint line must use non-empty "
                "'action -> verification' format "
                f"(invalid: {', '.join(malformed_ids)})"
            )

    if require_checkpoint_timestamps:
        missing_timestamp_ids = [
            checkpoint_id
            for checkpoint_id, tail in checkpoint_pairs
            if re.search(r"\b\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z\b", tail) is None
        ]
        if missing_timestamp_ids:
            errors.append(
                "checkpoint timestamps: every checkpoint line must include ISO-8601 UTC timestamp "
                f"YYYY-MM-DDTHH:MM:SSZ (missing: {', '.join(missing_timestamp_ids)})"
            )

    if enforce_monotonic_checkpoint_timestamps:
        missing_timestamp_ids = [
            checkpoint_id
            for checkpoint_id, tail in checkpoint_pairs
            if _extract_iso_utc_timestamp(tail) is None
        ]
        if missing_timestamp_ids:
            errors.append(
                "checkpoint timestamp order: all checkpoint lines must include ISO-8601 UTC timestamp "
                f"before monotonic order can be validated (missing: {', '.join(missing_timestamp_ids)})"
            )
        else:
            ordered_timestamps = [
                (checkpoint_id, _extract_iso_utc_timestamp(tail))
                for checkpoint_id, tail in checkpoint_pairs
            ]
            concrete = [(cid, ts) for cid, ts in ordered_timestamps if ts is not None]
            for idx in range(1, len(concrete)):
                prev_id, prev_ts = concrete[idx - 1]
                cur_id, cur_ts = concrete[idx]
                if cur_ts < prev_ts:
                    errors.append(
                        "checkpoint timestamp order: checkpoint timestamps must be monotonic "
                        f"in execution-log order ({prev_id}={prev_ts.strftime('%Y-%m-%dT%H:%M:%SZ')} > "
                        f"{cur_id}={cur_ts.strftime('%Y-%m-%dT%H:%M:%SZ')})"
                    )
                    break

    if enforce_checkpoint_status_tokens:
        missing_status_ids = [
            checkpoint_id
            for checkpoint_id, tail in checkpoint_pairs
            if re.search(r"\b(PASS|FAIL)\b", tail) is None
        ]
        if missing_status_ids:
            errors.append(
                "checkpoint status tokens: every checkpoint line must include PASS/FAIL "
                f"(missing: {', '.join(missing_status_ids)})"
            )

    if enforce_checkpoint_to_check_status_consistency:
        checklist_status_map = _extract_check_status_map(text)
        checkpoint_status_map = _extract_checkpoint_status_map(text)

        missing_checkpoint_status_ids = sorted(
            check_id
            for check_id in checklist_status_map
            if check_id not in checkpoint_status_map
        )
        if missing_checkpoint_status_ids:
            errors.append(
                "checkpoint/check status consistency: checkpoint lines must include PASS/FAIL status "
                "for every checklist check "
                f"(missing: {', '.join(missing_checkpoint_status_ids)})"
            )

        mismatch_ids = sorted(
            check_id
            for check_id, checklist_status in checklist_status_map.items()
            if checkpoint_status_map.get(check_id) is not None
            and checkpoint_status_map[check_id] != checklist_status
        )
        if mismatch_ids:
            errors.append(
                "checkpoint/check status consistency: checkpoint PASS/FAIL must match checklist PASS/FAIL "
                f"(mismatch: {', '.join(mismatch_ids)})"
            )

    if require_visual_checkpoint_evidence:
        visual_checkpoint_pairs = [
            (checkpoint_id, tail)
            for checkpoint_id, tail in checkpoint_pairs
            if checkpoint_id.startswith("V")
        ]
        missing_visual_evidence_ids = [
            checkpoint_id
            for checkpoint_id, tail in visual_checkpoint_pairs
            if re.search(r"`[^`]+\.(png|jpg|jpeg|webp)`", tail, flags=re.IGNORECASE) is None
        ]
        if missing_visual_evidence_ids:
            errors.append(
                "visual checkpoint evidence: every visual checkpoint line must include inline screenshot evidence "
                f"(missing: {', '.join(missing_visual_evidence_ids)})"
            )

    if require_checkpoint_artifact_paths:
        missing_artifact_path_ids = [
            checkpoint_id
            for checkpoint_id, tail in checkpoint_pairs
            if re.search(
                r"`[^`]+\.(png|jpg|jpeg|webp|mp4|log|txt|json|zip|har|trace)`",
                tail,
                flags=re.IGNORECASE,
            )
            is None
        ]
        if missing_artifact_path_ids:
            errors.append(
                "checkpoint artifact paths: every checkpoint line must include at least one inline artifact path "
                "(screenshot/video/log/trace) for reproducible replay "
                f"(missing: {', '.join(missing_artifact_path_ids)})"
            )

    if require_checkpoint_target_refs:
        missing_target_ref_ids = [
            checkpoint_id
            for checkpoint_id, tail in checkpoint_pairs
            if re.search(r"\bref=[A-Za-z0-9_.:-]+\b", tail) is None
        ]
        if missing_target_ref_ids:
            errors.append(
                "checkpoint target refs: every checkpoint line must include stable target ref token "
                "'(ref=<id>)' for deterministic replay "
                f"(missing: {', '.join(missing_target_ref_ids)})"
            )

    if enforce_checkpoint_target_ref_uniqueness:
        ref_to_checkpoint_ids: dict[str, list[str]] = {}
        for checkpoint_id, tail in checkpoint_pairs:
            for target_ref in _extract_checkpoint_target_refs(tail):
                ref_to_checkpoint_ids.setdefault(target_ref, []).append(checkpoint_id)

        duplicate_refs = sorted(
            ref
            for ref, owners in ref_to_checkpoint_ids.items()
            if len(set(owners)) > 1
        )
        if duplicate_refs:
            errors.append(
                "checkpoint target ref uniqueness: each ref=<id> must map to exactly one checkpoint "
                f"(duplicates: {', '.join(duplicate_refs)})"
            )

    if enforce_checkpoint_artifact_ref_uniqueness:
        artifact_to_checkpoint_ids: dict[str, list[str]] = {}
        for checkpoint_id, tail in checkpoint_pairs:
            for artifact_ref in _extract_checkpoint_artifact_refs(tail):
                artifact_to_checkpoint_ids.setdefault(artifact_ref, []).append(checkpoint_id)

        duplicate_artifacts = sorted(
            artifact
            for artifact, owners in artifact_to_checkpoint_ids.items()
            if len(set(owners)) > 1
        )
        if duplicate_artifacts:
            errors.append(
                "checkpoint artifact ref uniqueness: each inline artifact path must map to exactly one checkpoint "
                f"(duplicates: {', '.join(duplicate_artifacts)})"
            )

    if require_failure_checkpoint_artifact_paths:
        checkpoint_status_map = _extract_checkpoint_status_map(text)
        checkpoint_pairs_map = dict(checkpoint_pairs)
        failed_checkpoint_ids = sorted(
            checkpoint_id
            for checkpoint_id, status in checkpoint_status_map.items()
            if status == "FAIL"
        )
        missing_failure_checkpoint_artifact_ids = [
            checkpoint_id
            for checkpoint_id in failed_checkpoint_ids
            if re.search(
                r"`[^`]+\.(png|jpg|jpeg|webp|mp4|log|txt|json|zip|har|trace)`",
                checkpoint_pairs_map.get(checkpoint_id, ""),
                flags=re.IGNORECASE,
            )
            is None
        ]
        if missing_failure_checkpoint_artifact_ids:
            errors.append(
                "failure checkpoint artifact paths: every failed checkpoint line must include an inline artifact path "
                "(screenshot/video/log/trace) for deterministic failure replay "
                f"(missing: {', '.join(missing_failure_checkpoint_artifact_ids)})"
            )

    if require_failure_evidence_artifact_paths:
        failed_blocks = _failed_check_blocks(text)
        missing_failure_evidence_artifact_ids = []
        for checkpoint_id, block in failed_blocks:
            evidence_match = re.search(r"(?mi)^\s*-\s*Evidence:\s*(.+)$", block)
            evidence_tail = evidence_match.group(1) if evidence_match else ""
            has_artifact_ref = re.search(
                r"`[^`]+\.(png|jpg|jpeg|webp|mp4|log|txt|json|zip|har|trace)`",
                evidence_tail,
                flags=re.IGNORECASE,
            )
            if has_artifact_ref is None:
                missing_failure_evidence_artifact_ids.append(checkpoint_id)

        if missing_failure_evidence_artifact_ids:
            errors.append(
                "failure evidence artifact paths: every failed check must include an inline artifact path in Evidence: "
                f"(missing: {', '.join(missing_failure_evidence_artifact_ids)})"
            )

    if require_failure_recovery_plan:
        failed_blocks = _failed_check_blocks(text)
        missing_failure_recovery_plan_ids = [
            checkpoint_id
            for checkpoint_id, block in failed_blocks
            if re.search(r"(?mi)^\s*-\s*Recovery plan:\s*.+$", block) is None
        ]
        if missing_failure_recovery_plan_ids:
            errors.append(
                "failure recovery plan: every failed check must include a Recovery plan: line "
                f"(missing: {', '.join(missing_failure_recovery_plan_ids)})"
            )

    if require_failure_recovery_owner:
        failed_blocks = _failed_check_blocks(text)
        missing_failure_recovery_owner_ids = [
            checkpoint_id
            for checkpoint_id, block in failed_blocks
            if re.search(r"(?mi)^\s*-\s*Recovery owner:\s*.+$", block) is None
        ]
        if missing_failure_recovery_owner_ids:
            errors.append(
                "failure recovery owner: every failed check must include a Recovery owner: line "
                f"(missing: {', '.join(missing_failure_recovery_owner_ids)})"
            )

    if require_failure_classification_summary:
        breakdown = _extract_failure_breakdown_summary(text)
        if breakdown is None:
            errors.append(
                "failure classification summary: signoff must include 'Failure breakdown: selector=<n>, runtime=<n>, product=<n>'"
            )
        else:
            actual_counts = {"selector": 0, "runtime": 0, "product": 0}
            for classification in _extract_failed_check_classifications(text):
                actual_counts[classification] += 1
            if breakdown != actual_counts:
                errors.append(
                    "failure classification summary: signoff breakdown must match failed-check classifications "
                    f"(reported selector={breakdown['selector']}, runtime={breakdown['runtime']}, product={breakdown['product']}; "
                    f"actual selector={actual_counts['selector']}, runtime={actual_counts['runtime']}, product={actual_counts['product']})"
                )

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate fixed-count sections in a web QA Playwright markdown report"
    )
    parser.add_argument("--file", required=True, help="Path to markdown report")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Enable stricter reproducibility checks (URL/viewport/account/screenshots/checkpoints/signoff/failure recovery)",
    )
    parser.add_argument(
        "--strict-plus",
        action="store_true",
        help=(
            "Enable strict mode plus all reproducibility gates "
            "(checkpoint format + timestamps + monotonic order + status tokens + visual evidence + artifact paths + target refs + failure recovery plan)"
        ),
    )
    parser.add_argument(
        "--playwright-interactive-profile",
        action="store_true",
        help=(
            "Apply the Playwright interactive reliability profile "
            "(equivalent to strict-plus with deterministic recovery gates)."
        ),
    )
    parser.add_argument(
        "--deterministic-replay-profile",
        action="store_true",
        help=(
            "Alias for --playwright-interactive-profile. "
            "Use when you want deterministic replay + recovery requirements in one switch."
        ),
    )
    parser.add_argument(
        "--strict-replay-profile",
        action="store_true",
        help=(
            "Alias for --playwright-interactive-profile. "
            "Use for strict deterministic replay gates in CI presets."
        ),
    )
    parser.add_argument(
        "--ci-replay-profile",
        action="store_true",
        help=(
            "Alias for --playwright-interactive-profile. "
            "Use when CI jobs prefer short replay-policy naming."
        ),
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON output for CI parsers",
    )
    parser.add_argument(
        "--json-out",
        default=None,
        help="Optional path to write machine-readable JSON payload (PASS/FAIL) for CI artifacts",
    )
    parser.add_argument(
        "--enforce-checkpoint-format",
        action="store_true",
        help="Require checkpoint lines to use 'action -> verification' format",
    )
    parser.add_argument(
        "--require-checkpoint-timestamps",
        action="store_true",
        help="Require every checkpoint line to include ISO-8601 UTC timestamp (YYYY-MM-DDTHH:MM:SSZ)",
    )
    parser.add_argument(
        "--enforce-monotonic-checkpoint-timestamps",
        action="store_true",
        help=(
            "Require checkpoint timestamps to be monotonic in execution-log order. "
            "Every checkpoint line must include ISO-8601 UTC timestamp."
        ),
    )
    parser.add_argument(
        "--enforce-checkpoint-status-tokens",
        action="store_true",
        help="Require every checkpoint line to include normalized PASS/FAIL status token",
    )
    parser.add_argument(
        "--require-visual-checkpoint-evidence",
        action="store_true",
        help="Require visual checkpoint lines (V1..V3) to include inline screenshot evidence",
    )
    parser.add_argument(
        "--require-checkpoint-artifact-paths",
        action="store_true",
        help="Require every checkpoint line to include at least one inline artifact path (screenshot/video/log/trace)",
    )
    parser.add_argument(
        "--require-checkpoint-target-refs",
        action="store_true",
        help="Require every checkpoint line to include a stable target ref token (ref=<id>)",
    )
    parser.add_argument(
        "--enforce-checkpoint-target-ref-uniqueness",
        action="store_true",
        help="Require every checkpoint target ref token (ref=<id>) to appear in only one checkpoint line",
    )
    parser.add_argument(
        "--enforce-checkpoint-artifact-ref-uniqueness",
        action="store_true",
        help="Require inline artifact paths (e.g., `artifacts/f1.log`) to appear in only one checkpoint line",
    )
    parser.add_argument(
        "--require-failure-checkpoint-artifact-paths",
        action="store_true",
        help="Require execution-log checkpoint lines marked FAIL to include inline artifact paths",
    )
    parser.add_argument(
        "--require-failure-evidence-artifact-paths",
        action="store_true",
        help="Require failed checks to include an inline artifact path on their Evidence: line",
    )
    parser.add_argument(
        "--require-failure-recovery-plan",
        action="store_true",
        help="Require failed checks to include a Recovery plan: line describing deterministic recovery steps",
    )
    parser.add_argument(
        "--require-failure-recovery-owner",
        action="store_true",
        help="Require failed checks to include a Recovery owner: line for explicit follow-up ownership",
    )
    parser.add_argument(
        "--enforce-failure-timestamp-order",
        action="store_true",
        help=(
            "Require failed-check First failure timestamp values to be monotonic in checklist order. "
            "All failed checks must use ISO-8601 UTC format first."
        ),
    )
    parser.add_argument(
        "--enforce-checkpoint-to-check-status-consistency",
        action="store_true",
        help="Require checkpoint PASS/FAIL status tokens to be present and match checklist PASS/FAIL per check id",
    )
    parser.add_argument(
        "--require-failure-classification-summary",
        action="store_true",
        help="Require signoff Failure breakdown summary and verify selector/runtime/product totals against failed checks",
    )
    parser.add_argument(
        "--require-qa-inventory-section",
        action="store_true",
        help="Require report to include explicit '## 1) QA inventory' section for claim-to-check coverage planning",
    )
    parser.add_argument(
        "--require-qa-inventory-check-refs",
        action="store_true",
        help=(
            "Require every QA inventory bullet to include a Checks: mapping to known check ids "
            "for claim-to-check planning and deterministic replay coverage"
        ),
    )
    parser.add_argument(
        "--require-qa-inventory-full-coverage",
        action="store_true",
        help="Require the QA inventory to reference every checklist id F1..F5, V1..V3, O1..O2 at least once",
    )
    parser.add_argument(
        "--require-execution-log-step-count-match",
        action="store_true",
        help=(
            "Require execution log to contain only checkpoint bullet lines and exactly 10 total check steps "
            "(F1..F5, V1..V3, O1..O2)."
        ),
    )
    parser.add_argument(
        "--require-signoff-section",
        action="store_true",
        help="Require report to include explicit '## 4) Signoff' section header for deterministic review closure",
    )
    parser.add_argument(
        "--require-replay-readiness",
        action="store_true",
        help="Require signoff to include 'Replay readiness: READY/BLOCKED' for deterministic replay handoff",
    )
    parser.add_argument(
        "--require-next-action",
        action="store_true",
        help="Require signoff to include 'Next action: ...' so the next run has an explicit handoff step",
    )
    parser.add_argument(
        "--require-next-action-failed-check-ref",
        action="store_true",
        help="Require signoff Next action to reference at least one failed check id when regressions are present",
    )
    parser.add_argument(
        "--require-next-action-all-failed-check-refs",
        action="store_true",
        help="Require signoff Next action to reference every failed check id for a complete deterministic recovery handoff",
    )
    args = parser.parse_args()

    profile_enabled = (
        args.strict_plus
        or args.playwright_interactive_profile
        or args.deterministic_replay_profile
        or args.strict_replay_profile
        or args.ci_replay_profile
    )
    strict_enabled = args.strict or profile_enabled
    enforce_checkpoint_format = args.enforce_checkpoint_format or profile_enabled
    require_checkpoint_timestamps = args.require_checkpoint_timestamps or profile_enabled
    enforce_monotonic_checkpoint_timestamps = (
        args.enforce_monotonic_checkpoint_timestamps or profile_enabled
    )
    enforce_checkpoint_status_tokens = args.enforce_checkpoint_status_tokens or profile_enabled
    require_visual_checkpoint_evidence = args.require_visual_checkpoint_evidence or profile_enabled
    require_checkpoint_artifact_paths = args.require_checkpoint_artifact_paths or profile_enabled
    require_checkpoint_target_refs = args.require_checkpoint_target_refs or profile_enabled
    enforce_checkpoint_target_ref_uniqueness = (
        args.enforce_checkpoint_target_ref_uniqueness or profile_enabled
    )
    enforce_checkpoint_artifact_ref_uniqueness = (
        args.enforce_checkpoint_artifact_ref_uniqueness or profile_enabled
    )
    require_failure_checkpoint_artifact_paths = (
        args.require_failure_checkpoint_artifact_paths or profile_enabled
    )
    require_failure_evidence_artifact_paths = args.require_failure_evidence_artifact_paths or profile_enabled
    require_failure_recovery_plan = args.require_failure_recovery_plan or profile_enabled
    require_failure_recovery_owner = args.require_failure_recovery_owner or profile_enabled
    enforce_failure_timestamp_order = args.enforce_failure_timestamp_order or profile_enabled
    enforce_checkpoint_to_check_status_consistency = (
        args.enforce_checkpoint_to_check_status_consistency or profile_enabled
    )
    require_failure_classification_summary = (
        args.require_failure_classification_summary or profile_enabled
    )
    require_execution_log_step_count_match = (
        args.require_execution_log_step_count_match or profile_enabled
    )
    require_qa_inventory_section = args.require_qa_inventory_section or profile_enabled
    require_qa_inventory_check_refs = args.require_qa_inventory_check_refs
    require_qa_inventory_full_coverage = args.require_qa_inventory_full_coverage or args.strict_plus
    require_signoff_section = args.require_signoff_section or profile_enabled
    require_replay_readiness = args.require_replay_readiness or profile_enabled
    require_next_action = args.require_next_action
    require_next_action_failed_check_ref = args.require_next_action_failed_check_ref
    require_next_action_all_failed_check_refs = args.require_next_action_all_failed_check_refs

    def resolve_profile_preset() -> str | None:
        if args.playwright_interactive_profile:
            return "playwright-interactive-profile"
        if args.deterministic_replay_profile:
            return "deterministic-replay-profile"
        if args.strict_replay_profile:
            return "strict-replay-profile"
        if args.ci_replay_profile:
            return "ci-replay-profile"
        if args.strict_plus:
            return "strict-plus"
        return None

    active_profile_preset = resolve_profile_preset()

    report_path = Path(args.file)
    if not report_path.exists():
        print(f"error: report not found: {report_path}", file=sys.stderr)
        raise SystemExit(2)

    text = report_path.read_text(encoding="utf-8")
    errors = validate_report_text(
        text,
        strict=strict_enabled,
        enforce_checkpoint_format=enforce_checkpoint_format,
        require_checkpoint_timestamps=require_checkpoint_timestamps,
        enforce_monotonic_checkpoint_timestamps=enforce_monotonic_checkpoint_timestamps,
        enforce_checkpoint_status_tokens=enforce_checkpoint_status_tokens,
        require_visual_checkpoint_evidence=require_visual_checkpoint_evidence,
        require_checkpoint_artifact_paths=require_checkpoint_artifact_paths,
        require_checkpoint_target_refs=require_checkpoint_target_refs,
        enforce_checkpoint_target_ref_uniqueness=enforce_checkpoint_target_ref_uniqueness,
        enforce_checkpoint_artifact_ref_uniqueness=enforce_checkpoint_artifact_ref_uniqueness,
        require_failure_checkpoint_artifact_paths=require_failure_checkpoint_artifact_paths,
        require_failure_evidence_artifact_paths=require_failure_evidence_artifact_paths,
        require_failure_recovery_plan=require_failure_recovery_plan,
        require_failure_recovery_owner=require_failure_recovery_owner,
        enforce_failure_timestamp_order=enforce_failure_timestamp_order,
        enforce_checkpoint_to_check_status_consistency=enforce_checkpoint_to_check_status_consistency,
        require_failure_classification_summary=require_failure_classification_summary,
        require_execution_log_step_count_match=require_execution_log_step_count_match,
        require_qa_inventory_section=require_qa_inventory_section,
        require_qa_inventory_check_refs=require_qa_inventory_check_refs,
        require_qa_inventory_full_coverage=require_qa_inventory_full_coverage,
        require_signoff_section=require_signoff_section,
        require_replay_readiness=require_replay_readiness,
        require_next_action=require_next_action,
        require_next_action_failed_check_ref=require_next_action_failed_check_ref,
        require_next_action_all_failed_check_refs=require_next_action_all_failed_check_refs,
    )
    report_metadata = _build_report_metadata(text)

    def emit_json_payload(payload: dict[str, object]) -> None:
        if args.json:
            print(json.dumps(payload, ensure_ascii=False))
        if args.json_out:
            out_path = Path(args.json_out)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    if errors:
        payload = {
            "status": "FAIL",
            "validation_schema_version": VALIDATION_SCHEMA_VERSION,
            "strict": strict_enabled,
            "strict_plus": args.strict_plus,
            "playwright_interactive_profile": args.playwright_interactive_profile,
            "deterministic_replay_profile": args.deterministic_replay_profile,
            "strict_replay_profile": args.strict_replay_profile,
            "ci_replay_profile": args.ci_replay_profile,
        "active_profile_preset": active_profile_preset,
            "enforce_checkpoint_format": enforce_checkpoint_format,
            "require_checkpoint_timestamps": require_checkpoint_timestamps,
            "enforce_monotonic_checkpoint_timestamps": enforce_monotonic_checkpoint_timestamps,
            "enforce_checkpoint_status_tokens": enforce_checkpoint_status_tokens,
            "require_visual_checkpoint_evidence": require_visual_checkpoint_evidence,
            "require_checkpoint_artifact_paths": require_checkpoint_artifact_paths,
            "require_checkpoint_target_refs": require_checkpoint_target_refs,
            "enforce_checkpoint_target_ref_uniqueness": enforce_checkpoint_target_ref_uniqueness,
            "enforce_checkpoint_artifact_ref_uniqueness": enforce_checkpoint_artifact_ref_uniqueness,
            "require_failure_checkpoint_artifact_paths": require_failure_checkpoint_artifact_paths,
            "require_failure_evidence_artifact_paths": require_failure_evidence_artifact_paths,
            "require_failure_recovery_plan": require_failure_recovery_plan,
            "require_failure_recovery_owner": require_failure_recovery_owner,
            "enforce_failure_timestamp_order": enforce_failure_timestamp_order,
            "enforce_checkpoint_to_check_status_consistency": enforce_checkpoint_to_check_status_consistency,
            "require_failure_classification_summary": require_failure_classification_summary,
            "require_execution_log_step_count_match": require_execution_log_step_count_match,
            "require_qa_inventory_section": require_qa_inventory_section,
            "require_qa_inventory_check_refs": require_qa_inventory_check_refs,
            "require_qa_inventory_full_coverage": require_qa_inventory_full_coverage,
            "require_signoff_section": require_signoff_section,
            "require_replay_readiness": require_replay_readiness,
            "require_next_action": require_next_action,
            "require_next_action_failed_check_ref": require_next_action_failed_check_ref,
            "require_next_action_all_failed_check_refs": require_next_action_all_failed_check_refs,
            "file": str(report_path),
            "errors": errors,
            "error_count": len(errors),
            "report_metadata": report_metadata,
        }
        if args.json or args.json_out:
            emit_json_payload(payload)
        else:
            print("web-qa-playwright report validation: FAIL")
            for err in errors:
                print(f"- {err}")
        raise SystemExit(1)

    payload = {
        "status": "PASS",
        "validation_schema_version": VALIDATION_SCHEMA_VERSION,
        "strict": strict_enabled,
        "strict_plus": args.strict_plus,
        "playwright_interactive_profile": args.playwright_interactive_profile,
        "deterministic_replay_profile": args.deterministic_replay_profile,
        "strict_replay_profile": args.strict_replay_profile,
        "ci_replay_profile": args.ci_replay_profile,
        "active_profile_preset": active_profile_preset,
        "enforce_checkpoint_format": enforce_checkpoint_format,
        "require_checkpoint_timestamps": require_checkpoint_timestamps,
        "enforce_monotonic_checkpoint_timestamps": enforce_monotonic_checkpoint_timestamps,
        "enforce_checkpoint_status_tokens": enforce_checkpoint_status_tokens,
        "require_visual_checkpoint_evidence": require_visual_checkpoint_evidence,
        "require_checkpoint_artifact_paths": require_checkpoint_artifact_paths,
        "require_checkpoint_target_refs": require_checkpoint_target_refs,
        "enforce_checkpoint_target_ref_uniqueness": enforce_checkpoint_target_ref_uniqueness,
        "enforce_checkpoint_artifact_ref_uniqueness": enforce_checkpoint_artifact_ref_uniqueness,
        "require_failure_checkpoint_artifact_paths": require_failure_checkpoint_artifact_paths,
        "require_failure_evidence_artifact_paths": require_failure_evidence_artifact_paths,
        "require_failure_recovery_plan": require_failure_recovery_plan,
        "require_failure_recovery_owner": require_failure_recovery_owner,
        "enforce_failure_timestamp_order": enforce_failure_timestamp_order,
        "enforce_checkpoint_to_check_status_consistency": enforce_checkpoint_to_check_status_consistency,
        "require_failure_classification_summary": require_failure_classification_summary,
        "require_execution_log_step_count_match": require_execution_log_step_count_match,
        "require_qa_inventory_section": require_qa_inventory_section,
        "require_qa_inventory_check_refs": require_qa_inventory_check_refs,
        "require_qa_inventory_full_coverage": require_qa_inventory_full_coverage,
        "require_signoff_section": require_signoff_section,
        "require_replay_readiness": require_replay_readiness,
        "require_next_action": require_next_action,
        "require_next_action_failed_check_ref": require_next_action_failed_check_ref,
        "require_next_action_all_failed_check_refs": require_next_action_all_failed_check_refs,
        "file": str(report_path),
        "report_metadata": report_metadata,
        "counts": {
            "functional": 5,
            "visual": 3,
            "off_happy": 2,
        },
    }

    if args.json or args.json_out:
        emit_json_payload(payload)
    if args.json:
        return

    print("web-qa-playwright report validation: PASS")
    print("- functional checks: 5")
    print("- visual checks: 3")
    print("- off-happy-path checks: 2")
    if strict_enabled:
        print("- strict checks: enabled")
    if args.strict_plus:
        print("- strict-plus preset: enabled")
    if args.playwright_interactive_profile:
        print("- playwright interactive profile: enabled")
    if args.deterministic_replay_profile:
        print("- deterministic replay profile: enabled")
    if args.strict_replay_profile:
        print("- strict replay profile: enabled")
    if args.ci_replay_profile:
        print("- ci replay profile: enabled")
    if enforce_checkpoint_format:
        print("- checkpoint format checks: enabled")
    if require_checkpoint_timestamps:
        print("- checkpoint timestamp checks: enabled")
    if enforce_monotonic_checkpoint_timestamps:
        print("- monotonic checkpoint timestamp checks: enabled")
    if enforce_checkpoint_status_tokens:
        print("- checkpoint status token checks: enabled")
    if require_visual_checkpoint_evidence:
        print("- visual checkpoint evidence checks: enabled")
    if require_checkpoint_artifact_paths:
        print("- checkpoint artifact path checks: enabled")
    if require_checkpoint_target_refs:
        print("- checkpoint target-ref checks: enabled")
    if enforce_checkpoint_target_ref_uniqueness:
        print("- checkpoint target-ref uniqueness checks: enabled")
    if enforce_checkpoint_artifact_ref_uniqueness:
        print("- checkpoint artifact-ref uniqueness checks: enabled")
    if require_failure_checkpoint_artifact_paths:
        print("- failure checkpoint artifact path checks: enabled")
    if require_failure_evidence_artifact_paths:
        print("- failure evidence artifact path checks: enabled")
    if require_failure_recovery_plan:
        print("- failure recovery plan checks: enabled")
    if require_failure_recovery_owner:
        print("- failure recovery owner checks: enabled")
    if enforce_failure_timestamp_order:
        print("- failed-check timestamp monotonicity checks: enabled")
    if enforce_checkpoint_to_check_status_consistency:
        print("- checkpoint/check status consistency checks: enabled")
    if require_failure_classification_summary:
        print("- failure classification summary checks: enabled")
    if require_execution_log_step_count_match:
        print("- execution log step-count checks: enabled")
    if require_qa_inventory_section:
        print("- qa inventory section checks: enabled")
    if require_qa_inventory_check_refs:
        print("- qa inventory check-ref mapping checks: enabled")
    if require_qa_inventory_full_coverage:
        print("- qa inventory full-coverage checks: enabled")
    if require_signoff_section:
        print("- signoff section checks: enabled")
    if require_replay_readiness:
        print("- replay readiness checks: enabled")
    if require_next_action:
        print("- next action handoff checks: enabled")
    if require_next_action_failed_check_ref:
        print("- next action failed-check traceability checks: enabled")
    if require_next_action_all_failed_check_refs:
        print("- next action all-failed-check handoff checks: enabled")
    if report_metadata.get("has_signoff_section"):
        print(
            "- signoff field coverage: "
            f"{report_metadata.get('signoff_field_coverage_rate', 0.0) * 100:.2f}% "
            f"({len(report_metadata.get('missing_signoff_fields', []))} missing field(s))"
        )
    if report_metadata.get("missing_signoff_fields"):
        print(
            "- missing signoff fields: "
            + ", ".join(report_metadata["missing_signoff_fields"])
        )
    if report_metadata.get("failed_check_ids"):
        all_failed_refs = report_metadata.get("next_action_references_all_failed_checks", False)
        print(f"- next action covers all failed checks: {'yes' if all_failed_refs else 'no'}")
    if report_metadata.get("unresolved_failed_check_ids"):
        unresolved = ", ".join(report_metadata["unresolved_failed_check_ids"])
        print(f"- unresolved failed checks: {unresolved}")


if __name__ == "__main__":
    main()
