---
name: bower-build
description: Assemble deck.pptx from a FROZEN storyline, slideplan, STYLE.md and exhibit specs, using per-slide worker fragments applied by a single assembler. Use when called by bower-run, when the user says "build the deck", "rebuild S07", "assemble the pptx", or when frozen artifacts exist and slides don't. Refuses to run without a frozen storyline. Renders titles verbatim; fixes renders, never claims; overflow is a build error.
---

# bower-build

The deliberately dumb stage: all thinking happened upstream, so build's job is fidelity —
render exactly what the blueprint says, flag anything that resists, invent nothing.

Load: `references/style-schema.md` · `references/archetypes.md` · `references/engine-notes.md`.

## Preconditions (hard)

`storyline.md` marked FROZEN · `slideplan.md` · `STYLE.md` · every S##/X## row's exhibit has a
spec + CSV. Missing → refuse and name the gap (route: triage). Preflight failures (fonts,
soffice, pdftoppm, Node + pptxgenjs) → refuse loudly; a silently substituted font ships a different
deck than QA inspected.

## Scope

Invoked bare: build everything in `slideplan.md`. Invoked with slide ids
(`/bower-build S07 S12`): rebuild only those rows, then reassemble and re-render just them.

## Conductor plan

- Waves of fresh-context workers; **every worker receives the full storyline** — late slides
  get the same clear head as early ones.
- **Workers emit per-slide JSON fragments** (`fragments/S##.json`, contract in
  engine-notes.md — content only; style/geometry keys are forbidden and linted). Workers never
  open the deck file. **One assembler** (Node + pptxgenjs) dispatches each fragment to its
  archetype builder — builders apply STYLE tokens, so off-scale sizes, off-palette colours and
  banned chart types are impossible by construction — names every shape semantically, saves
  once.
- Per wave: assemble → `../bower-qa/scripts/bower_render.py` → fast visual loop (overflow bbox,
  collisions, clipping, squint). Render faults fixed in-wave; spec or claim faults FLAG to the
  conductor — **never patched locally.**

## Rules

- **Titles verbatim from slideplan.** Slide says 35 but CSV says 32 → transcription fault,
  auto-fix to the CSV. Title claims 35 but CSV says 32 → **claim fault: STOP and flag** — build
  never edits claims.
- Archetype per row (archetypes.md); build order per slide: message → layout → visual → text →
  polish. One concept per slide.
- Density: deck mode from STYLE; **X## rows always scale.read**. No off-scale sizes; floors
  hard. **Overflow = error** → split content or FLAG the spec; never shrink below floors,
  never autofit.
- Charts native-first per the exhibit `render` flag; data from `data/E##.csv` only; grey base,
  accent only on message carriers (and the recommendation column, and the ask).
- No emphasis inside titles. No colour-filled boxes behind body text. Effects banned.
- Photography: `refs/` files only, never fetched or generated, never on or near a chart;
  real logos from brand assets only, never stretched.
- **Speaker notes** (projected decks), per content slide: how to read the visual → its so-what
  → the oral transition from the slideplan `connective-out`.
- Mandatory furniture per content slide: title · rule · source (bottom-left) · page number
  (bottom-right); none on cover/dividers.

## Output

`deck.pptx` · `slides/*.png` (wave renders) · a buildlog: waves, flags raised, transcription
fixes applied, any spec deviations with reasons.
