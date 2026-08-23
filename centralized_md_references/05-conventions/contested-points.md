# Contested Points — and the Decisions Made

Where the sources genuinely disagree. Each was a decision only Philip could make; **all ten are
now resolved** (decided 2026-08-23). The research is kept below so the reasoning stays visible —
a default whose origin is forgotten becomes doctrine by accident.

## Decision summary

| # | Question | **Decision** |
|---|---|---|
| 1 | Executive summary at the front? | **Yes — slide 2**, always |
| 2 | Chart titles: "what" or "so what"? | **Always "so what"** |
| 3 | Pie charts | **Banned** |
| 4 | Photography | **BCG convention** — curated, permitted, never on or near a chart |
| 5 | Serif or sans titles | **House style if one exists; otherwise likaku** (Georgia title / Arial body, McKinsey navy) |
| 6 | Slide count budgets | **Budget ideas, not slides** — the story sets the count |
| 7 | Narrative depth | **Pyramid structure, narrative framing**; SCQA where it fits best |
| 8 | Chart "so what" placement | **BCG style** |
| 9 | Storyline artifact | **Dot-dash** |
| 10 | Generated imagery | **Off by default**; user-driven opt-in only, deferred |

Two of these are *stricter* than the library recommended (3 and 2), one is *looser* (4). Those
divergences are marked in place below.

---

## 1. Executive summary at the front?

> ### ✅ DECIDED — exec summary on slide 2, always
> Matches the library recommendation. Governing thought as the title; the Key Line points as the
> body, in the same words used as the section titles later. Deliver it in one sentence out loud,
> never bullet-by-bullet — that is the mitigation for tip 33's real concern.

| Position | Source | Argument |
|---|---|---|
| **Yes, slide 2** | mbb-deck, likaku, kgraph57, Minto (answer first) | The whole deck on one page. *"If the audience reads only one slide, this is the one."* Decks circulate as pre-reads. |
| **No, not in a presented deck** | Dave McKinsey tip 33 | Executive summaries are dense bulleted slides, tedious to deliver, *"raise more questions than can be answered in detail"*, and *"once you deliver an executive summary you might as well end the meeting."* He allows two exceptions: a deck **designed for reading**, and **as the last slide** as a recap. |

**Both are right about different artifacts.** The disagreement is really about whether the deck
is a document or a script.

**Recommended default: include it at slide 2.** Reasons: (a) most business decks circulate
without their author, so the document case dominates; (b) Minto's answer-first principle is the
deeper rule and tip 33 is an argument about *delivery mechanics*, not structure; (c) the deck
title already carries the answer under the SMART convention, so nothing is being spoiled.

**Mitigation for tip 33's real concern:** the exec summary should not be read aloud bullet by
bullet. Deliver it in one sentence — Zelazny's *"if I had only one minute…"* — then move.

---

## 2. Chart titles: "what" or "so what"?

> ### ✅ DECIDED — chart titles always state the "so what"
> **Stricter than the library's recommendation**, which resolved by slide composition. Simpler
> and more consistent: every exhibit carries its insight, everywhere, with no per-slide judgement
> call. Sides with Zelazny, BCG and mbb-deck against Dave McKinsey's tip 55.
>
> **Implementation wrinkle to handle:** on a single-chart slide the action title and the chart
> title can collapse into the same sentence. Rule to apply — the **action title carries the
> slide-level claim; the chart title states what this exhibit specifically shows**, which is
> normally narrower. If the two would be word-for-word identical, the chart title is dropped
> rather than duplicated. Duplication is not "consistent", it is noise.

| Position | Source | Argument |
|---|---|---|
| **"What"** — describe the function | Dave McKinsey tip 55 | *"Graph titles should merely explain the function of the graph because it is the visual representation that matters."* Best practice: describe the y-axis then the x-axis — "y over time", "Comparison of y across x". The slide title already carries the so-what; a second one is redundant. |
| **"So what"** — state the insight | mbb-deck, BCG (implicitly), Zelazny | *"Chart headers state the insight, not the metric — 'EBIT margin declines despite growth' beats 'EBIT margin, %'."* Zelazny's whole message-title argument: *"Don't keep it a secret; let your message head the chart."* |

Note that Zelazny himself hedges: *"In actual practice, you might want to delete them from the
charts. For example, when producing onscreen visuals where space is limited, you might decide to
include the message title **only in your written script** and not show it on the visual."* His
non-negotiable is doing the *step*, not printing the result.

**Recommended default, resolving by slide composition:**
- **One chart on the slide** → the action title carries the so-what; the chart gets at most a
  units/scope descriptor ("Net revenue, USD mm, FY22–FY25"). A second so-what is redundant and
  competes with the title.
- **Two or more exhibits on the slide** → each gets its own short message line, because the
  action title can only carry one proposition and the reader needs to know what each panel says.
- **Detail / appendix slide read without narration** → message line on the chart, because the
  reader may be looking at the exhibit out of context.

---

## 3. Pie charts

> ### ✅ DECIDED — pie charts banned
> **Stricter than the library's recommendation** (which was "discouraged, not banned", on the
> grounds that Zelazny and BCG both permit them). Adopting mbb-deck's hard line as house policy.
>
> Share-of-whole messages render as a **sorted bar** or **stacked column**. Doughnuts are covered
> by the same ban. Enforce mechanically in the linter, and when a pie is requested, say the ban
> exists and offer the alternative rather than silently substituting.

| Position | Source |
|---|---|
| **Correct form for a component comparison** — but should be ~5% of charts | Zelazny (the originator of the comparison framework) |
| **Acceptable up to five categories** for composition snapshots | Dave McKinsey tips 67–69 |
| **Permitted** — doughnuts explicitly useful for highlighting | BCG Format Guide; likaku (layout #64) |
| **≤3 slices, and you must defend it** | pstack-loki |
| **Banned outright, no exceptions, mechanically enforced** | mbb-deck |

**Recommended default: discouraged, not banned.** Prefer a sorted bar or stacked column for
share-of-whole. Permit a pie when the message is genuinely "these are the parts of one whole",
slices are ≤5, and the reader needs the whole-ness to register.

Rationale for not banning: Zelazny — the source everyone else is quoting — assigns the pie a
specific correct job, and BCG (an actual MBB firm) permits it. A hard ban is a defensible house
policy but should be *chosen*, not inherited silently. Make it a config flag.

---

## 4. Photography

> ### ✅ DECIDED — follow the BCG convention
> **Looser than the library's default**, and the better call: BCG is the only genuine firm source
> here and it is the most permissive. Its actual rules apply in full —
> - Consider **tone, subject matter, design aesthetics and composition** when choosing.
> - Find *"true-to-life, clean-looking photos"*; avoid abstract.
> - **Never on or near a chart** — BCG's own hard line.
> - Portrait/bio conventions: circular colour photography, consistent size and text treatment,
>   gradient outline; split across slides rather than crowding.
> - Protect image quality — discard editing data before compressing.
>
> This governs *sourced* photography. Generated imagery is a separate question — see #10.

| Position | Source |
|---|---|
| **Permitted, with a whole curation section** — tone, subject matter, composition, aesthetics; a partnership with a stock provider; portrait/bio conventions | **BCG Format Guide** |
| **No stock photography, no clip art** | mbb-deck |
| **No decorative icons that do not encode meaning**; no decorative motif at all | kgraph57 |
| **Generated imagery as a first-class deck element** | pstack-loki (Seedream figures) |

**Recommended default: permitted for dividers, covers and human/qualitative content; banned
near data.** BCG's own hard line is the useful one: *"Refrain from using photography on or near
a chart."*

Note that BCG — the only genuine firm source here — is the *most* permissive. The "no images
ever" position is a skill-author preference, not MBB doctrine. But an agent generating decorative
imagery unprompted is a real failure mode, so the default should be off with an explicit opt-in.

---

## 5. Serif or sans for titles?

> ### ✅ DECIDED — house style first, likaku as the fallback
> Matches the library recommendation, with the fallback pinned. When the engagement has a client
> template or brand guide, follow it. Otherwise **likaku's McKinsey-style system**:
>
> | Element | Value |
> |---|---|
> | Title | **Georgia**, bold, 22pt |
> | Body | **Arial**, 14pt (primary size) |
> | Cover title | Georgia, 44pt · Section 28pt · Sub-header 18pt · Footnote 9pt |
> | Primary | NAVY `#051C2C` |
> | Text | DARK_GRAY `#333333` · MED_GRAY `#666666` |
> | Rules / panels | LINE_GRAY `#CCCCCC` · BG_GRAY `#F2F2F2` |
> | Accents (only when 3+ parallel items) | `#006BA6` · `#007A53` · `#D46A00` · `#C62828` |
>
> Geometry likewise: 13.333×7.5", 0.8" margins, title at 0.15" (height 0.9"), rule at 1.05",
> content 1.3–6.5", source at 7.05", page number bottom-right.
>
> Implication: the toolkit needs a **house-style detection/ingest step** — read a supplied
> template or brand guide and derive tokens, falling back to likaku when none is given.

| Position | Source |
|---|---|
| **Sans throughout** (Trebuchet) | BCG Format Guide |
| **Serif titles** (Georgia), sans body (Arial) | likaku |
| **Serif headline** (Georgia), sans body (Helvetica Neue) | kgraph57 |
| **One font family for the entire deck**, sans | mbb-deck |

kgraph57's justification for Georgia: *"distributable strategy-consulting templates substitute
Georgia for their licensed brand serifs, so Georgia is the accurate portable equivalent."*

**Recommended default: follow the house style if one exists; otherwise serif title + sans body.**
The serif/sans pairing is the more recognizably "consulting" register, and McKinsey's own brand
face (**Bower**) is a serif. But a single sans family is a perfectly professional choice and
BCG's actual guide takes it — so this is taste, not correctness.

---

## 6. Slide count budgets

> ### ✅ DECIDED — the story determines the count
> Matches the library recommendation; Zelazny wins. A slide budget is a constraint on **scope**,
> not on density: if the storyline needs 22 slides and the slot allows 12, **cut arguments, never
> cram slides**. A stated budget becomes an input to storyline scoping, not a post-hoc squeeze.

| Position | Source |
|---|---|
| 10–15 slides for a standard deck | mbb-deck |
| Standard 10–12; short 6–8; minimum 8 for a substantive topic; ~1 min/slide | likaku |
| **Don't budget by time at all** | Zelazny |

Zelazny's argument:
> "Don't worry about showing too many visuals. Some speakers equate the number of visuals with
> the length of a presentation. Someone even quoted a ratio of 2 minutes of presentation for
> every visual. **It doesn't work that way.** Two minutes is too long to look at the same image.
> It's the number of ideas being presented and the complexity of the ideas that dictate length…
> **it takes the same amount of time to present one idea on each of five visuals as it does to
> present five ideas on one visual.**"

**Recommended default: budget ideas, not slides.** Zelazny is right and the conflict matters: a
slide-count ceiling that forces two messages onto one slide breaks the one-message rule to save
nothing. Take the slide budget as an *input constraint on scope* — if the storyline needs 22
slides and you have 12, cut arguments, don't cram slides.

---

## 7. How much drama should the structure carry?

> ### ✅ DECIDED — pyramid structure, narrative framing; SCQA where it fits
> Matches the library recommendation. Concretely:
> - **Structure is always the pyramid** — governing thought → Key Line → support. Never an act
>   structure, never a beat sheet, never anything that defers the answer.
> - **The body takes one of the seven patterns**, chosen to fit the situation.
> - **SCQA/CTQ is the introduction** where it fits and is possible — one slide, at most two. Not
>   every communication needs a full CTQ (a routine update may not), so it is applied on fit
>   rather than mandated.
> - **Narrative technique informs wording and framing**, not order: the audience is the hero and
>   you are the mentor; articulate "what is" versus "what could be" and the gap between them.

| Position | Source |
|---|---|
| **SCQA is the introduction; the pyramid is the body** | Minto |
| **S/C/R as the deck's three top-level acts** | Dave McKinsey (describing real firm decks) |
| **Five-beat dramatic arc** (Cold Open → Stranger Rides In → Raising the Stakes → High Noon → The New Order) | pstack-loki |
| **Seven named patterns, none of them dramatic arcs** | Stanley & Castles |
| **Story path: "what is" vs "what could be", the gap, toggle to build tension; audience is the hero, you are the mentor** | **BCG Format Guide** |

Interesting: BCG's own guide *does* use narrative framing (hero/mentor, what-is/what-could-be,
"toggle back and forth… to increase tension"). So narrative thinking is not un-MBB. But BCG
applies it to **audience framing and slide content**, not as a replacement for the pyramid.

**Recommended default: pyramid structure, narrative framing.** Use SCQA/CTQ as the introduction,
one of the seven patterns as the body, and narrative technique (the gap, the audience as hero,
tension) to *inform how each element is worded* — not to reorganize the deck into acts.

The specific failure to avoid: a dramatic skin that delays the answer. Any structure that makes
the reader wait for the recommendation has broken the one rule every source agrees on. See
`06-prior-art/pstack-loki-postmortem.md`.

---

## 8. Where does the "So what" for a chart go?

> ### ✅ DECIDED — BCG style
> Applies BCG's chart-annotation mechanics:
> - **Highlight colour indicates the main idea.** Start the chart grey monochrome; the message
>   carrier takes the accent. This is BCG's primary so-what mechanism, before any text.
> - **Callouts draw attention to a specific data point** — *"their strongest function is to
>   visually define a key idea."* Circle callouts where several points are marked; square
>   callouts for blocks.
> - **Grey data labels are secondary — context for the highlighted ones**, not clutter.
> - **Leader lines drawn manually**, never PowerPoint defaults.
> - **Never backfill a label.** If it isn't clearly connected, enlarge the chart instead.
> - **Takeaway boxes** for a slide-level conclusion the title can't carry.
>
> Read with #2: the chart's title states the insight; BCG's mechanics show *where on the chart*
> the reader should look to see it.

Related to #2 but distinct: annotation placement.

| Position | Source |
|---|---|
| Annotation **on the key datum**, ≤8 words | pstack-loki |
| Footer takeaway/annotation line at a fixed baseline | kgraph57 |
| Callouts and bubbles for remarks on specific chart elements; takeaway boxes for the slide's overall conclusion | BCG, mbb-deck |
| Bottom-of-slide annotations should **only** be used to transition to the next slide | Dave McKinsey tip 34 |

**Recommended default:** annotate *on* the datum when calling out a specific point; use a
takeaway box for a slide-level conclusion that the title can't carry; reserve the bottom line
for the transition. Tip 34's restriction is worth respecting — a bottom-of-slide annotation that
duplicates the title wastes the one place a transition could live.

---

## 9. Is the storyline artifact a document, an outline, or structured data?

> ### ✅ DECIDED — dot-dash
> Matches the library recommendation, and sides with McKinsey's own doctrine: *"PowerPoint is not
> a good tool for synthesis."* The primary artifact is a **plain-text dot-dash memo** — nested
> dots and dashes, every line a full declarative sentence, indentation carrying the pyramid, the
> whole thing on a page.
>
> Three consequences worth designing around:
> 1. **It grows.** The Day 1 guess and the final storyline are one document at different
>    maturities — no handoff, no re-derivation.
> 2. **It is what the human reads at the gate.** Readable aloud in about two minutes.
> 3. **Machine forms are derived, never authored.** Whatever the builder and linter need is
>    generated from the dot-dash, so there is exactly one source of truth.

| Position | Source |
|---|---|
| **Dot-dash memo** — plain text, grows from Day 1 answer to final storyline | McKinsey SP66 (*"We strongly recommend this technique"*) |
| **One-page visual storyline** — boxes, projected and clicked through | Stanley & Castles |
| **Storyboard** — visuals plus narration plus transitions | Zelazny |
| **JSON conforming to a schema**, validated by a script | mbb-deck |
| **Markdown table: one row per slide** (`S## \| Act \| TITLE \| detail \| evidence \| visual \| status \| transition`) | pstack-loki |

McKinsey's position is the strongest stated: *"PowerPoint is not a good tool for synthesis: It is
poor at highlighting logical connections."* The same objection applies, with less force, to JSON.

**Recommended default: a human-readable dot-dash storyline as the primary artifact**, because it
is the one form the user can read aloud, argue with, and hand to a colleague — which is what
every source says the review step requires. A machine-readable projection of it can be generated
for the builder and the linter, but it should be *derived*, not authored.

---

## 10. Should the toolkit generate imagery?

> ### ✅ DECIDED — off by default; opt-in only, and deferred
> No generated imagery unless explicitly requested, and Philip will drive that himself when the
> time comes. **Whether it belongs in the skill set at all is deferred** — treat it as out of
> scope for v1 rather than as a disabled feature.
>
> Two rules to carry regardless, whenever it does arrive:
> - **Image models never draw charts.** *"They are good enough at fake infographics to be
>   dangerous."*
> - Confine any generated imagery to **dividers and covers** — never content, never near data.
>
> Note this is about *generated* imagery. Sourced photography is permitted under BCG's convention
> — see #4.

pstack-loki invests heavily here (a whole skill, an external image API, reference-chaining). No
other source in the corpus contemplates generated imagery, and its own rule is instructive:

> "Charts prove, figures evoke. Data visuals come only from specs with real CSVs. **Image models
> never draw charts — they are good enough at fake infographics to be dangerous.**"

**Recommended default: off.** MBB decks are austere; the corpus's design sources ban decorative
imagery near content; and the failure mode (a plausible-looking fake chart) is severe. If
included, it should be an explicit opt-in confined to dividers and covers, with the never-draw-
charts rule enforced.

---

## How to use this file

All ten are resolved, so this file now serves two jobs:

1. **The authoritative record of house policy.** When the skill applies one of these rules, this
   is where the rule lives and why.
2. **A guard against silent drift.** Each decision records whether it matched, tightened or
   loosened the library's recommendation, so a future change is a visible reversal rather than an
   accident.

Where a decision diverges from what the sources collectively suggest (#2 and #3 tighten, #4
loosens), the skill should still be able to *say so* if asked — "pie charts are banned as house
policy, though Zelazny and BCG both permit them for component comparisons" is a better answer
than presenting the ban as universal doctrine.

The original problem this file exists to solve: prior work was *"not aligned with what I want"*
partly because opinions were baked in without being surfaced as opinions. These ten are now
surfaced, chosen, and attributed.
