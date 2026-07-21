# Files and Schemas

## Episode artifact order

```text
episodes/<episode-id>/
  00_EPISODE_BRIEF.md
  01_SOURCE_LOG.md
  02_RAW_STORY.md
  03_EDITED_STORYLINE_V1.md
  04_SCRIPT_V1.md
  05_CONTINUITY_BIBLE.md
  06_SHOT_LIST_V1.md
  07_VIDEO_QA.md
  08_PACKAGING.md
  09_PERFORMANCE_REVIEW.md
  10_RETROSPECTIVE.md
```

Use explicit versions for changing creative artifacts. Preserve approved history.

## Learning event schema

`knowledge/learnings.jsonl` is append-only UTF-8 JSONL.

Required fields:

```json
{
  "id": "lrn_YYYYMMDDTHHMMSSZ_slug",
  "recorded_at": "ISO-8601 UTC",
  "event": "observe|promote|retire",
  "signal_type": "user_feedback|metric|qa_failure|reference_pattern|research_correction|production_discovery",
  "scope": "episode|channel|system_candidate|system_rule",
  "episode": "episode-id or null",
  "stage": "topic|research|storyline|script|visual|edit|audio|packaging|publication|analytics|workflow",
  "observation": "What happened",
  "decision": "What behavior should change",
  "evidence": ["file, URL, timestamp, metric, feedback summary"],
  "supersedes": [],
  "status": "observed|candidate|promoted|retired"
}
```

## Source confidence

- `high`: archive, official record, contemporary document or directly supported fact;
- `attributed`: direct testimony or recollection that must be attributed;
- `secondary`: credible scholarship or reporting;
- `unresolved`: conflicting or insufficient evidence;
- `creative`: declared reconstruction or presentation choice.
