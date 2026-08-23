---
name: bower-storyline
description: Harden the draft dot-dash storyline from dump.md into storyline.md (the frozen argument) and slideplan.md (the slide ladder), enforcing pyramid structure, the seven-pattern rules, and action-title craft. Use when called by bower-triage, when the user says "harden the storyline", "compile the storyline", "the flow is broken", "recompile", or when a storyline exists and its argument needs re-testing. Never builds slides; never re-derives an agreed argument from prose.
---

# bower-storyline

The compiler. Input: `dump.md` (brief + Storyline v0). Output: `storyline.md` + `slideplan.md`,
gate-clean. **Harden, never re-derive**: run the gates, sharpen every sentence, fix wording —
the v0 tree the user agreed to is the tree. Cold case (no v0): say so, offer bower-grillme;
derive only on explicit insistence.

Load before composing: `references/patterns.md` · `references/title-craft.md` ·
`references/title-bank.md` (the calibration corpus — in context WHILE writing titles, not
after) · `references/storyline-tests.md`.

## storyline.md — the argument

Plain-text dot-dash, readable aloud in ~2 minutes. Every line a complete declarative sentence;
indentation is the pyramid; evidence tags inline.

```
v1 FROZEN <date>
CONTEXT   …
TRIGGER   …
QUESTION  …

SO WHAT   <governing thought — one sentence, rung 4>
  • <Key Line 1>                       [D3]
      – <support>                      [D3]
      – <support>                      [E04]
  • <Key Line 2> …

## Changelog
(appended by revision deltas — what changed, why, which slides touched)
```

## slideplan.md — the sequence

One row per slide; three row types:

```
S## | node | ACTION TITLE (verbatim, immutable) | archetype | exhibit | FACT/EST/JUDG | connective-out
G## | —    | cover / agenda / divider:<section> / closing    | —
X## | appendix | title | archetype | exhibit | tag           | —
```

- **S##** — every row tied to a storyline node. No orphans.
- **G##** — sequence, not argument. A divider's one-line promise IS its section's Key Line
  sentence, verbatim. Exec summary is always slide 2: title = the governing thought, body = the
  Key Line sentences.
- **X##** — appendix: ladder-exempt, always read-density, still linted. Receives ruled-out
  options, methodology, detail twins of projected charts.
- `connective-out` is written explicitly (therefore/but + the next question raised) — it later
  becomes the speaker-note transition.

## Composing titles — the discipline

1. Titles are written top-down from the hardened tree, whole-ladder at once — never per-slide.
2. **Compose 2–3 candidate ladders and pick** (judging drafts beats first-drafting to
   register). Judge against the bank: does this read like the [REAL] titles, or like the
   anti-pattern gallery?
3. House register: plain, specific, complete; long is fine; no sparkle.
4. Every title through the defect classifier. **A blank assertion routes upstream for more
   thinking — never to a rewriter.**

## Gates — all must pass before returning (see storyline-tests.md)

Purpose stated · CTQ six checks · So-what five rules · pattern named with fit reason ·
grouping-5 or deductive-4 · pyramid down/across/up · **memo read** (titles alone argue) ·
**connective test** (therefore/but, never and-then) · **question chain** (each title's implied
question answered by the next — when it fails, it names the missing slide) · per-slide checks.

Failures are fixed and re-run here. Failures that reveal *thinking* gaps (blank assertion, no
plural noun, orphan legs) go back to the user via triage — with the specific question, not a
guess.

## Never

Invent evidence · reorder the agreed Key Line without flagging it as a delta · exceed one
message per slide (a second message = a new slide or a ladder split) · let a structural slide
carry argument · touch STYLE, exhibits, or pptx.
