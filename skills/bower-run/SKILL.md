---
name: bower-run
description: Run the deck pipeline autonomously from a closed triage to a terminal state — build waves, ship-mode QA, pre-committed dispositions, one bounded fix cycle, then SHIPPED or BLOCKED. Use when the user says "run", "take it from here", "build it out", or wants the whole deck produced unattended after the gate. Cannot ask questions mid-run: it finishes or fails loudly with every decision needed batched into one report.
---

# bower-run

The dormammu gear. All judgement was front-loaded at the gate; this executes to a terminal
state with zero interruptions.

## Preconditions

`storyline.md` FROZEN · triage packet closed · disposition policy on file. Not met → refuse,
name the gap, point at bower-triage. Then **re-verify preflight** (fonts, soffice, pdftoppm,
Node + pptxgenjs) — a red preflight is an immediate BLOCKED, not a degraded run.

## The run

```
build waves (bower-build; per-wave fast visual loop)
  → ship-mode bower-qa (all eight passes)
  → apply the pre-committed disposition (SEV-1 fix · SEV-2 fix · SEV-3 accept, as closed)
  → ONE bounded fix cycle: route findings upstream, rebuild the dirty set, scoped re-QA
  → SHIPPED or BLOCKED
```

Rules while unattended:
- Renders may be fixed; **claims may not** — a CLAIM finding is always BLOCKED material.
- Fixes route upstream and rebuild only the dirty set (slideplan/exhibit graph walk).
- Stop conditions: the same finding surviving two fix attempts · the fix cycle growing the
  finding count · anything requiring a human answer. Don't thrash; don't burn the night.

## Terminal states

**SHIPPED** — `deck.pptx` · clean (or accepted-SEV-3-only) `qa.md` · `TIMELINE.md` entry.

**BLOCKED** — **every independent load-bearing question, batched into ONE report** (never
serial mornings). Per item: the exact finding, the slide, the evidence, and the decision
needed. Each answer is a revision delta (route table: render → build · sequence → slideplan +
delta-gate · claim → storyline + version bump + delta-gate · frame → grillme). "run" again
rebuilds only what the answers touched.

## The morning report (this is the point)

Whether SHIPPED or BLOCKED: what was built (slides, exhibits, waves) · what QA found by pass
and severity · what was auto-fixed under the policy · what was accepted · what's parked ·
timings. Append to `TIMELINE.md`: `date | run | vN | SHIPPED/BLOCKED | summary`.
