# Time-Travel History Production System

An open production system for building source-grounded, retention-driven YouTube
episodes that place a recurring host inside the past or future.

The system was created from hands-on analysis of immersive history channels and the
production of a first episode about the four prisoners who escaped Auschwitz in a
stolen SS staff car. It separates factual chronology from edited storytelling, then
connects script, visual continuity, sound, QA, packaging and performance learning.

## Core format

```text
consequence hook
→ short brand ident
→ direct-to-camera mission briefing
→ spoken launch + hard cut into historical action
→ escalating mission with real people and constraints
→ climax
→ documented consequence/aftershock
→ concise debrief and CTA
```

There is no standalone portal or time-travel montage. Historical figures retain agency;
the host guides the viewer without replacing their decisions.

## Start here

Use the bundled [`time-travel-history-producer`](skills/time-travel-history-producer/SKILL.md)
skill. Its canonical workflow, QA rules and self-learning loop live in:

- [Production workflow](skills/time-travel-history-producer/references/WORKFLOW.md)
- [Retention QA](skills/time-travel-history-producer/references/RETENTION_QA.md)
- [Self-learning loop](skills/time-travel-history-producer/references/SELF_LEARNING.md)
- [Publication system](skills/time-travel-history-producer/references/PUBLICATION.md)
- [Schemas](skills/time-travel-history-producer/references/SCHEMAS.md)

## Repository layout

```text
skills/       reusable Codex skill, references, scripts and templates
knowledge/    append-only learning events and generated learning report
examples/     reviewed, text-only golden examples
.github/      validation workflow
```

Large source videos, generated media, API keys and production masters do not belong in
this repository.

## Self-learning

Self-learning is an auditable workflow, not an invisible claim. Whenever feedback,
metrics, QA or new evidence reveals a reusable lesson:

```bash
python3 skills/time-travel-history-producer/scripts/record_learning.py \
  --signal-type user_feedback \
  --scope system_candidate \
  --stage storyline \
  --episode ep01-auschwitz-escape \
  --observation "Background explanation delayed the next action." \
  --decision "Cap context-only passages at 15 seconds and attach context to a decision." \
  --evidence "User review of storyline v1"

python3 skills/time-travel-history-producer/scripts/build_learning_report.py
python3 skills/time-travel-history-producer/scripts/validate_repo.py
```

Promoted rules update the canonical workflow/template and receive a regression check.
History remains append-only so later evidence can retire or supersede earlier rules.

## Validation

```bash
python3 skills/time-travel-history-producer/scripts/validate_repo.py
```

## License

MIT. Historical source materials and third-party media retain their own rights.
