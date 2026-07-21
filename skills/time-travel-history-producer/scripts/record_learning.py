#!/usr/bin/env python3
"""Append one auditable learning event to knowledge/learnings.jsonl."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


SIGNALS = {
    "user_feedback",
    "metric",
    "qa_failure",
    "reference_pattern",
    "research_correction",
    "production_discovery",
}
SCOPES = {"episode", "channel", "system_candidate", "system_rule"}
EVENTS = {"observe", "promote", "retire"}
STATUSES = {"observed", "candidate", "promoted", "retired"}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return (slug[:48].rstrip("-") or "learning")


def default_status(event: str, scope: str) -> str:
    if event == "retire":
        return "retired"
    if event == "promote" or scope == "system_rule":
        return "promoted"
    if scope == "system_candidate":
        return "candidate"
    return "observed"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--signal-type", required=True, choices=sorted(SIGNALS))
    parser.add_argument("--scope", required=True, choices=sorted(SCOPES))
    parser.add_argument("--stage", required=True)
    parser.add_argument("--observation", required=True)
    parser.add_argument("--decision", required=True)
    parser.add_argument("--episode")
    parser.add_argument("--event", choices=sorted(EVENTS), default="observe")
    parser.add_argument("--status", choices=sorted(STATUSES))
    parser.add_argument("--evidence", action="append", default=[])
    parser.add_argument("--supersedes", action="append", default=[])
    parser.add_argument("--slug")
    parser.add_argument(
        "--store",
        type=Path,
        default=repo_root() / "knowledge" / "learnings.jsonl",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    now = datetime.now(timezone.utc).replace(microsecond=0)
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    learning_id = f"lrn_{stamp}_{slugify(args.slug or args.decision)}"
    record = {
        "id": learning_id,
        "recorded_at": now.isoformat().replace("+00:00", "Z"),
        "event": args.event,
        "signal_type": args.signal_type,
        "scope": args.scope,
        "episode": args.episode,
        "stage": args.stage,
        "observation": args.observation.strip(),
        "decision": args.decision.strip(),
        "evidence": args.evidence,
        "supersedes": args.supersedes,
        "status": args.status or default_status(args.event, args.scope),
    }
    args.store.parent.mkdir(parents=True, exist_ok=True)
    with args.store.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")))
        handle.write("\n")
    print(learning_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
