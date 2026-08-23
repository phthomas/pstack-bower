# pstack-bower — Centralized References

Distilled doctrine for building MBB-style business presentations, extracted from 10 books and
papers and 5 skill repositories. This is the reference base the pstack-bower skills will be
built on.

**Named for Marvin Bower** — who invented management consulting as a profession, and whose name
McKinsey also gave to its brand typeface.

---

## Start here

| If you want to… | Read |
|---|---|
| Understand what was ingested and how far to trust it | [`00-source-inventory.md`](00-source-inventory.md) |
| See the skill design | [`07-synthesis/skill-architecture.md`](07-synthesis/skill-architecture.md) |
| See the settled house policy | [`05-conventions/contested-points.md`](05-conventions/contested-points.md) |
| Know what this all implies for the skill | [`07-synthesis/design-brief-pstack-bower.md`](07-synthesis/design-brief-pstack-bower.md) |
| Understand why the last attempt fell short | [`06-prior-art/pstack-loki-postmortem.md`](06-prior-art/pstack-loki-postmortem.md) |
| Write a better action title *right now* | [`02-action-titles/action-title-examples-bank.md`](02-action-titles/action-title-examples-bank.md) |
| Pick a storyline shape | [`01-storyline/seven-storyline-patterns.md`](01-storyline/seven-storyline-patterns.md) |

---

## The library

### `01-storyline/` — how the argument is built
| File | Covers |
|---|---|
| [`minto-pyramid-principle.md`](01-storyline/minto-pyramid-principle.md) | The three rules · vertical Q&A · deduction vs induction · the Key Line · summarizing groups · the end-product test |
| [`scqa-and-introductions.md`](01-storyline/scqa-and-introductions.md) | SCQA / SCR / CTQ · writing each element · Minto's four introduction patterns · **why SCQA is the introduction, not the deck** |
| [`seven-storyline-patterns.md`](01-storyline/seven-storyline-patterns.md) | **Action Jackson · The Pitch · Traffic Light · Close the Gap · Houston · To B or Not to B · Watch Out** — with selection logic, rules and traps |
| [`hypothesis-driven-problem-solving.md`](01-storyline/hypothesis-driven-problem-solving.md) | Problem Statement Worksheet · issue and hypothesis trees · **the dot-dash storyline** · distinctiveness practices · ghost decks |
| [`storyline-quality-tests.md`](01-storyline/storyline-quality-tests.md) | Every runnable storyline test in the corpus, in the order to run them |

### `02-action-titles/` — the hardest craft
| File | Covers |
|---|---|
| [`action-title-craft.md`](02-action-titles/action-title-craft.md) | **Why titles go bland — four specific mechanisms** · 11 hard rules · the improvement ladder · ten title grammars · three title registers · a diagnostic vocabulary |
| [`action-title-examples-bank.md`](02-action-titles/action-title-examples-bank.md) | The calibration corpus — before/after pairs · **real McKinsey/BCG/Accenture titles** · governing thoughts · six complete title ladders · anti-pattern gallery |

### `03-slide-design/` — what goes on the page
| File | Covers |
|---|---|
| [`mbb-slide-standards.md`](03-slide-design/mbb-slide-standards.md) | **Key Message vs Detail Slides** · BCG's six slide attributes and five design principles · type scales · emphasis rules · palettes · geometry · density budgets |
| [`slide-archetypes.md`](03-slide-design/slide-archetypes.md) | 9 core patterns · structure/navigation slides · likaku's 72-layout menu · the McCandless build method · choosing an archetype from the title |
| [`deck-architecture.md`](03-slide-design/deck-architecture.md) | **Zelazny's answer-first demonstration** · the message test · the standard deck shape · storyboarding in six steps · packaging and delivery |

### `04-data-visualization/` — exhibits
| File | Covers |
|---|---|
| [`zelazny-chart-selection.md`](04-data-visualization/zelazny-chart-selection.md) | **Message → comparison → chart form** · five comparisons with trigger words · the matrix · usage budget · honest scaling · concepts and metaphors |
| [`chart-craft-and-decluttering.md`](04-data-visualization/chart-craft-and-decluttering.md) | BCG chart anatomy · axes, gridlines, labels, legends · Knaflic's Gestalt principles and six decluttering steps · the banned list · tables · the exhibit checklist |

### `05-conventions/` — the rules
| File | Covers |
|---|---|
| [`mbb-rules-of-the-road.md`](05-conventions/mbb-rules-of-the-road.md) | The ten core principles · the three flow rules · hard bans · mandatory furniture · integrity rules · when to break them |
| [`quality-rubrics-and-checklists.md`](05-conventions/quality-rubrics-and-checklists.md) | **Measured vs judged** · slide/production/deck checklists · the 24-point scored rubric · severity and routing · seven review passes · gate ordering |
| [`contested-points.md`](05-conventions/contested-points.md) | **Nine places the sources genuinely disagree**, each with a recommended default and a reason |

### `06-prior-art/` — what already exists
| File | Covers |
|---|---|
| [`pstack-ergonomics.md`](06-prior-art/pstack-ergonomics.md) | The loop to inherit · pstack's design principles verbatim · the dump gate · the autonomy dial · artifact discipline |
| [`pstack-loki-postmortem.md`](06-prior-art/pstack-loki-postmortem.md) | What loki gets right · each of the three defects traced to a cause · root causes · a change table |
| [`external-skills-teardown.md`](06-prior-art/external-skills-teardown.md) | mbb-deck · likaku · kgraph57 — borrow/avoid for each, plus a comparative matrix |

### `07-synthesis/`
| File | Covers |
|---|---|
| [`design-brief-pstack-bower.md`](07-synthesis/design-brief-pstack-bower.md) | Five findings · the implied pipeline · what to keep · measurable success criteria · the seven open questions (**all now resolved**) |
| [`skill-architecture.md`](07-synthesis/skill-architecture.md) | **v2 — the eight `bower-*` skills**, the revision protocol, STYLE.md schema, engine decisions, doctrine packaging |
| [`fable5-review.md`](07-synthesis/fable5-review.md) | **Independent Fable 5 review** (2026-08-23) — direction endorsed; four unspecified seams flagged: data intake, revision protocol, engine, doctrine packaging |

---

## Conventions used in these files

- **Quotes are verbatim** unless marked *(OCR-repaired)*, which indicates a source with scan
  damage where ligatures were reconstructed. See `00-source-inventory.md` for which sources.
- **Examples are tagged** `[REAL]` (from an actual firm deck), `[BOOK]`, `[SKILL]`, or
  `[DERIVED]` (constructed here to fill a gap).
- **Disagreements are flagged**, never silently resolved. Anywhere sources conflict, the file
  says so and points at `05-conventions/contested-points.md`.
- Cross-references sit at the foot of each file.

## What is deliberately not here

- **Raw extracted book text.** Copyrighted. The staging directory holds it for this session
  only; the library holds distilled doctrine and short illustrative quotes.
- **Implementation.** No SKILL.md, no scripts, no templates. That's the next phase.
- **Firm affiliation.** These references describe published *practice*. Nothing here implies
  endorsement by McKinsey, Bain, BCG or Accenture, and the skill should not either.

---

## The one-paragraph summary

Every source agrees on a small core: **answer first, one message per slide, titles that state
the so-what, MECE groupings, every number sourced.** Where prior skills fall short is not in
knowing these rules but in *depth* — no library of storyline shapes, no calibration corpus for
titles, and no real design standard. This library supplies those three, keeps the good
architecture from `pstack-loki` and the ergonomics from `pstack`, and flags the nine places
where the sources genuinely disagree so those become explicit choices rather than inherited
opinions.
