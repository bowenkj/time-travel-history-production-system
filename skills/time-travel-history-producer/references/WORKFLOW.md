# Production Workflow

## 0. System startup

- Read `knowledge/LEARNING_REPORT.md` and recent decisions.
- Identify the episode workspace, current approved versions and unresolved feedback.
- Confirm whether the task is research, storyline, script, production, QA, packaging
  or performance analysis.

## 1. Topic gate

### Inputs

- candidate event;
- reference-channel evidence;
- public competition and demand;
- accessible sources and visual feasibility.

### Pass conditions

- one-sentence audience promise;
- a concrete mission, danger, social rule or impossible choice;
- at least five meaningful state changes;
- human interaction or conflict, not only scenery;
- a distinct angle even if the event is already popular;
- sufficient source evidence and a plausible visual strategy.

Reject or redesign topics that are only “visit a famous era” without a goal.

## 2. Source gate

Create `SOURCE_LOG.md` and record:

- primary/official source URL, title, publisher and access date;
- what claim it supports;
- source type: record, contemporary account, survivor recollection, scholarship,
  secondary retelling;
- confidence and contradictions;
- image/audio usage rights;
- whether the source is research-only or production-cleared.

For sensitive history, prefer archives, museums, public institutions and direct
testimony. Never convert a popular retelling into “fact” without tracing it backward.

## 3. Raw story

Use `assets/templates/RAW_STORY.template.md`.

Write chronology before drama:

- world context required to understand the event;
- people, motives, access and constraints;
- preparations;
- event sequence;
- immediate response;
- consequences and later fates;
- high-confidence facts, attributed recollections and unresolved claims;
- safe dialogue and visual proof objects.

### Gate

Every decisive action has a source or is explicitly labeled reconstruction. Conflicting
versions remain visible.

## 4. Edited storyline

Use `assets/templates/EDITED_STORYLINE.template.md` and read `RETENTION_QA.md`.

Convert chronology into a causal story:

- consequence-first cold open;
- short brand ident;
- mission briefing ending in a spoken launch and hard cut;
- 5–7 escalating setup–tension–payoff loops;
- varied conflict types;
- false victories that reveal larger problems;
- strongest testimony or confrontation saved for a late climax;
- consequence/aftershock after the physical climax;
- concise debrief and CTA.

### Gate

The paper edit passes character agency, evidence, retention, visual feasibility and
audio-contour QA before scripting.

## 5. Script

Use `assets/templates/SCRIPT.template.md`.

- Write natural spoken English.
- Attach background to an immediate scene question.
- Keep the host's personality, but avoid modern jokes that trivialize suffering.
- Use dialogue from testimony when available; label translated reconstruction.
- Do not narrate what the image or character already proves.
- End each section by making the next section necessary.

Read aloud and run a cold-reader comprehension pass before TTS or recording.

## 6. Continuity and shot plan

Use `CONTINUITY_BIBLE.template.md` and `SHOT_LIST.template.md`.

Lock before generation:

- face, age, build and hair for recurring people;
- clothing state and changes;
- date, weather and lighting;
- geography and travel direction;
- hero props and their state;
- camera grammar for host, reconstruction and evidence.

For every storyboard sequence, also write explicit **count locks** and **state-polarity
locks**. Count locks cover people, seats, props and repeated objects. State-polarity
locks cover visually opposite conditions whose reversal changes the story: occupied
vs empty, open vs closed, raised vs lowered, moving vs stopped, present vs missing,
inside vs outside and before vs after. Do not approve a semantically reversed panel
just because the composition is attractive.

Every shot must have a story function. Prefer character action, decision and reaction
over empty establishing imagery.

Storyboard the chronological journey before designing or producing cold-open-exclusive
shots. Mark possible hook moments while boarding, but choose the final cold open only
after the complete journey reveals which conflict beats are visually strongest and
actually available.

Keep user-facing review directories canonical: one active artifact per sequence.
After a correction passes QA, merge it into the numbered master and remove correction
sidecars, superseded drafts and obsolete review files from the delivery directory.
Use Git history and the learning log—not duplicate review assets—to preserve process
history.

Before storyboard approval, review every panel without its prompt and ask:

1. Does the visible count match the locked count?
2. Is the visible state the intended side of every polarity pair?
3. Would a viewer infer the correct event within one second?

Regenerate count or polarity failures before promoting the board to production.

## 7. Production

- Generate the approved chronological journey sequences before making footage solely
  for the cold open. The hook should normally be cut from complete conflict beats that
  already belong to the journey.
- Once strong journey material exists, assemble a 45–90 second opening proof containing
  the derived hook, host mode and one historical action before finishing the full
  episode.
- Generate/edit in short sequences with stable handles and version numbers.
- Keep narration over moving, relevant footage when possible; use stills only when the
  evidence itself is a still.
- Design music by tension wave. Do not keep all scenes at maximum intensity.
- Add captions for all narration and important raw dialogue unless an approved style
  rule says otherwise.

## 8. QA and master

Use `VIDEO_QA.template.md`.

Check:

- story and factual continuity;
- character/object consistency;
- shot relevance and legibility;
- audio continuity, missing sound, mix and music fit;
- full caption coverage and safe placement;
- transition motivation;
- disclosure, rights and graphic-content handling;
- final duration against story needs, not a preset quota.

Do not call a render production-ready until the complete master is watched with sound.

## 9. Packaging and release

Read `PUBLICATION.md` and use `PACKAGING.template.md`.

Title, thumbnail and first 30 seconds must promise and deliver the same conflict.
Complete platform checks before public release.

## 10. Performance loop

Use `PERFORMANCE_REVIEW.template.md` at approximately 24 hours, 7 days and 28 days
when analytics are available. Separate low-impression uncertainty from packaging or
retention conclusions. Record reusable signals through the self-learning workflow.
