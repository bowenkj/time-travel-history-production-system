# Self-Learning Loop

## Objective

Turn feedback and performance evidence into auditable production improvements that
survive across episodes and agents.

## Automatic triggers

Record a learning whenever one of these occurs:

- the user explains why a creative choice fails;
- a QA review finds a repeatable defect;
- a reference channel reveals a reusable pattern;
- an asset or model repeatedly fails in the same way;
- title, thumbnail, retention or traffic data contradicts an assumption;
- a source check exposes a recurring research error;
- a workflow step prevents or causes meaningful rework.

Do not wait for the user to say “update the workflow.”

## Atomic learning record

Use `scripts/record_learning.py`. One record contains one observation and one proposed
behavior change. Attach a file, URL, timestamp, metric window, commit or user-feedback
summary as evidence.

Scopes:

- `episode`: relevant only to one event or artifact;
- `channel`: default across this channel;
- `system_candidate`: likely reusable, awaiting repetition or stronger evidence;
- `system_rule`: promoted canonical behavior.

Signal types:

- `user_feedback`;
- `metric`;
- `qa_failure`;
- `reference_pattern`;
- `research_correction`;
- `production_discovery`.

## Promotion rule

Promote a candidate when at least one condition is true:

1. the user explicitly declares a reusable preference;
2. the same issue appears in two independent episodes;
3. a deterministic defect can be prevented by validation;
4. reliable performance evidence supports the behavior;
5. the failure has severe factual, legal, safety or publishing consequences.

Promotion requires:

- update the canonical reference or template;
- add or strengthen a regression check;
- append a promotion event rather than deleting history;
- rebuild `knowledge/LEARNING_REPORT.md`;
- commit with the behavior change in the message.

## Contradictions and retirement

Never silently overwrite a prior rule. Add a new event with `supersedes` pointing to
the old learning ID and explain the new evidence. Mark the old rule `retired` in the
generated report.

## Metrics discipline

Do not infer packaging failure from tiny samples. Record the observation window,
impressions, CTR, views, average view duration, average percentage viewed and traffic
source when available. Compare like-for-like topics and channel age.

## Per-turn behavior

When a reusable learning appears during production:

1. fix the current artifact;
2. record the learning;
3. update the system if promotion criteria are met;
4. run validation;
5. tell the user what behavior will change next time.
