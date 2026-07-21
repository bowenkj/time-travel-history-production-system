---
name: time-travel-history-producer
description: Build, revise, or QA retention-driven immersive time-travel history and future YouTube episodes from research through publication. Use when Codex needs to select a historical event, study a reference channel such as Chloe VS History, separate raw chronology from an edited storyline, write a host-led script, plan AI reconstruction shots and character continuity, review pacing and factual grounding, package titles/thumbnails/descriptions, analyze YouTube results, or promote reusable feedback into a self-learning production workflow.
---

# Time-Travel History Producer

## Principle

Make the viewer experience a concrete mission inside another time. Story comes before
spectacle. Historical context enters only when a decision makes it necessary.

## Start every task

1. Locate the production-system repository and the episode workspace.
2. Read `references/WORKFLOW.md` completely.
3. Read the current generated learning report at `knowledge/LEARNING_REPORT.md` when it
   exists. Treat promoted rules as defaults, not immutable truth.
4. Load only the additional reference required:
   - storyline, hook, script or edit: `references/RETENTION_QA.md`;
   - feedback, metrics or a reusable discovery: `references/SELF_LEARNING.md`;
   - upload, title, thumbnail, description or SEO: `references/PUBLICATION.md`;
   - filenames, templates or record fields: `references/SCHEMAS.md`.
5. Preserve evidence and intermediate decisions. Do not jump from a topic directly to
   a full script or generated footage.

## Production sequence

Use this order unless the user explicitly narrows the task:

1. **Reference and demand check** — verify the topic promise and competitive angle.
2. **Source gate** — gather authoritative sources, distinguish facts from recollection,
   and record contradictions and rights restrictions.
3. **Raw story** — write the unedited chronology and character roles.
4. **Edited storyline** — design question ladders, conflict waves, false victories,
   state changes and a late grand payoff.
5. **Script** — write for speech and action; keep context attached to objects, rules or
   decisions.
6. **Continuity and shot plan** — lock identities, wardrobe, geography, props and time;
   then plan visuals and audio.
7. **Production and QA** — generate or edit in small reviewable units; verify factual,
   visual, audio, caption and retention quality before the master render.
8. **Packaging and publication** — align title, thumbnail and opening payoff; complete
   description, chapters, disclosure and restrictions checks.
9. **Performance and learning** — collect feedback and metrics, record an atomic
   learning, and promote it into workflow/templates when warranted.

Copy the matching file from `assets/templates/` at each stage. Do not overwrite a
previous approved version; increment the version.

## Non-negotiable gates

- Do not generate production footage before `RAW_STORY` and `EDITED_STORYLINE` pass.
- The first five seconds must contain a legible problem, consequence or anomaly.
- The main mission must be clear by approximately 30–40 seconds.
- A camera cut alone is not story movement. Change knowledge, goal, obstacle, choice,
  relationship, location or proof.
- Introduce historical figures through action, not consecutive biography cards.
- Do not create a standalone portal/countdown/travel montage. End the mission briefing
  with a spoken launch and cut directly to historical action.
- Let real people retain agency. The recurring host guides and experiences; the host
  must not steal a documented person's decision or achievement.
- Label realistic synthetic historical reconstruction according to current platform
  policy. Keep a visual distinction between documented fact and dramatized connective
  action.
- Never fabricate a quote, atrocity, pursuit, relationship or outcome to manufacture
  tension. Use uncertainty, constraints and documented consequences.

## Self-learning trigger

When user feedback, QA failure, new reference evidence or performance metrics reveal a
reusable lesson, update the system without waiting for a separate request:

1. Apply the episode-level correction.
2. Run `scripts/record_learning.py` with evidence and scope.
3. Decide whether the signal stays episode-specific, becomes a candidate, or is strong
   enough to promote.
4. If promoted, update the canonical reference, QA rule or template and add a
   regression check.
5. Run `scripts/build_learning_report.py` and `scripts/validate_repo.py`.
6. Summarize the promoted behavior change in the commit.

Do not treat “self-learning” as silent background activity. It is an explicit,
auditable feedback loop stored in Git.

## Delivery standard

Report the artifact paths, the current gate, the highest remaining risk and the next
production action. Separate observed evidence from inference and creative choice.
