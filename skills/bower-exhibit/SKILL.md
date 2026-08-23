---
name: bower-exhibit
description: Write an exhibit spec for every data visual BEFORE any chart renders — message, house-resolved chart form, native/image render flag, data contract, element checklist. Use when called by bower-triage, when the user says "spec the exhibits" or "what charts do we need", or when a storyline exists and slides will need charts, tables, or diagrams. Never lets a chart be built without a spec; refuses numbers that have no provenance home.
---

# bower-exhibit

Every data visual gets a spec before it gets pixels: what it must PROVE, which form, which
numbers, which elements. Build gets a blueprint; QA gets assertions.

Load `references/chart-matrix.md` — the canonical, house-resolved matrix and element checklist.

## Per exhibit, in order

1. **One message.** Usually the slide's action title restated at exhibit scope. Two messages =
   two exhibits, or the ladder needs a split — **route upstream, never cram.**
2. **Form from the message** — trigger words → comparison → form, per the matrix. House rules
   already applied there: **no pie, no doughnut** (component → sorted bar / stacked column;
   when one is requested, cite house policy, note the sources aren't unanimous, build the
   alternative). Numbers the audience must *read*, not compare (<~5) → big number or table.
3. **Chart title = the exhibit's so-what** — narrower than the action title; **omit if
   word-for-word identical.**
4. **`render: native | image`.** Native wherever PowerPoint has the chart type — the client
   must be able to edit the deck. Waterfall counts as native (invisible-base recipe in
   `../bower-build/references/engine-notes.md`). Marimekko and other non-native forms:
   `image`, or re-form the message. Every `image` flag is surfaced in the triage packet.
5. **Data contract.** `data/E##.csv` — curated from `data/src/`, provenance preserved — holds
   the ONLY numbers allowed on that slide. **Refuse any number with no home** (no [D#], no
   src cell): that's an intake gap, name it.
6. **Emphasis + mechanics (BCG):** grey monochrome base, accent on the one message carrier,
   callout on the key datum where pointing is needed, manual leader lines, never backfill.
7. **Fill the element checklist** from chart-matrix.md — QA pass 4 asserts every line against
   the render.
8. **Neutrality test.** Would someone who rejects the conclusion call the chart fair — scale,
   baseline, series inclusion, colour? Honest scaling: cover the scale values; the message must
   still read from the picture alone.

Spec file: `exhibits/E##.spec.md`, exactly the shape given in chart-matrix.md.

## Routing

Message unclear → storyline defect, upstream. Number homeless → intake. Form impossible at
acceptable quality → flag in the packet with the proposed re-form. Never silently substitute a
different claim than the ladder makes.
