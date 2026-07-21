#!/usr/bin/env python3
"""Validate the production-system repository, skill, templates and learning log."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "skills" / "time-travel-history-producer"

REQUIRED = [
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    SKILL / "SKILL.md",
    SKILL / "agents" / "openai.yaml",
    SKILL / "references" / "WORKFLOW.md",
    SKILL / "references" / "RETENTION_QA.md",
    SKILL / "references" / "SELF_LEARNING.md",
    SKILL / "references" / "PUBLICATION.md",
    SKILL / "references" / "SCHEMAS.md",
    SKILL / "assets" / "templates" / "EPISODE_BRIEF.template.md",
    SKILL / "assets" / "templates" / "RAW_STORY.template.md",
    SKILL / "assets" / "templates" / "EDITED_STORYLINE.template.md",
    SKILL / "assets" / "templates" / "SCRIPT.template.md",
    SKILL / "assets" / "templates" / "CONTINUITY_BIBLE.template.md",
    SKILL / "assets" / "templates" / "SHOT_LIST.template.md",
    SKILL / "assets" / "templates" / "VIDEO_QA.template.md",
    SKILL / "assets" / "templates" / "PACKAGING.template.md",
    SKILL / "assets" / "templates" / "PERFORMANCE_REVIEW.template.md",
    SKILL / "assets" / "templates" / "RETROSPECTIVE.template.md",
    ROOT / "knowledge" / "learnings.jsonl",
    ROOT / "knowledge" / "LEARNING_REPORT.md",
]

REQUIRED_EVENT_FIELDS = {
    "id",
    "recorded_at",
    "event",
    "signal_type",
    "scope",
    "episode",
    "stage",
    "observation",
    "decision",
    "evidence",
    "supersedes",
    "status",
}

MEDIA_SUFFIXES = {
    ".mp4", ".mov", ".mkv", ".avi", ".wav", ".mp3", ".flac", ".aif",
    ".aiff", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".zip", ".tar", ".gz",
}


def error(message: str, errors: list[str]) -> None:
    errors.append(message)


def validate_skill(errors: list[str]) -> None:
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        error("SKILL.md is missing YAML frontmatter", errors)
    if "name: time-travel-history-producer" not in text:
        error("SKILL.md has the wrong name", errors)
    if "description:" not in text or "TODO" in text:
        error("SKILL.md description is missing or contains TODO", errors)
    yaml = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
    if "$time-travel-history-producer" not in yaml:
        error("agents/openai.yaml default_prompt must mention the skill", errors)


def validate_learning_log(errors: list[str]) -> None:
    path = ROOT / "knowledge" / "learnings.jsonl"
    seen: set[str] = set()
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            event = json.loads(raw)
        except json.JSONDecodeError as exc:
            error(f"{path}:{number}: invalid JSON: {exc}", errors)
            continue
        missing = REQUIRED_EVENT_FIELDS - event.keys()
        if missing:
            error(f"{path}:{number}: missing fields {sorted(missing)}", errors)
        event_id = event.get("id")
        if event_id in seen:
            error(f"{path}:{number}: duplicate id {event_id}", errors)
        seen.add(event_id)
        if not isinstance(event.get("evidence"), list):
            error(f"{path}:{number}: evidence must be a list", errors)
        if not isinstance(event.get("supersedes"), list):
            error(f"{path}:{number}: supersedes must be a list", errors)


def validate_files(errors: list[str]) -> None:
    for path in REQUIRED:
        if not path.is_file():
            error(f"missing required file: {path.relative_to(ROOT)}", errors)
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() in MEDIA_SUFFIXES:
            error(f"media/archive file must not be committed: {path.relative_to(ROOT)}", errors)
        if path.stat().st_size > 10 * 1024 * 1024:
            error(f"file exceeds 10 MiB: {path.relative_to(ROOT)}", errors)


def validate_report(errors: list[str]) -> None:
    script = SKILL / "scripts" / "build_learning_report.py"
    result = subprocess.run(
        [sys.executable, str(script), "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        error(result.stderr.strip() or result.stdout.strip(), errors)


def main() -> int:
    errors: list[str] = []
    validate_files(errors)
    if not errors:
        validate_skill(errors)
        validate_learning_log(errors)
        validate_report(errors)
    if errors:
        for item in errors:
            print(f"ERROR: {item}", file=sys.stderr)
        return 1
    print("repository validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
