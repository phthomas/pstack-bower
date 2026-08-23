# Quality Rubrics and Checklists

Everything in the corpus that can be run as a check, organized by what it inspects. Storyline-
level tests live in `01-storyline/storyline-quality-tests.md`; this file covers slide,
production and deck-level QA, plus the scored rubrics.

---

## 1. What can be measured vs what must be judged

The most useful distinction for building gates. mbb-deck's linter draws the line explicitly:
*"fonts, sizes, colors, bounds, jitter, page numbers, banned chart types are **measured**, not
judged."*

| Measurable (deterministic) | Judgeable (needs a model or a human) |
|---|---|
| Font family, size, weight | Whether the title states a so-what |
| Colour values against the palette | Whether the claim is falsifiable |
| Element bounds / overflow / clipping | Whether the grouping is MECE |
| Alignment jitter | Whether the flow works |
| Page numbers present | Whether the exhibit proves the title |
| Source line present | Whether an option set is complete |
| Banned chart types | Whether the emphasis lands on the right thing |
| Title/body number match | Whether the recommendation is the only one that follows |
| Bullet counts, nesting depth | Whether the deck is honest |
| Slop-lexicon hits | Whether it's *good* |
| Title word/line count | |
| Number-format consistency | |

**Design implication:** run the measurable checks first and cheaply, so the expensive judgement
passes aren't spent on formatting.

---

## 2. Slide-level checklist

- [ ] **One message.** Can the slide be summarized in a single sentence? That sentence is the title.
- [ ] **Vertical logic.** Does the body *unambiguously prove* the title? (Dave McKinsey tip 40)
- [ ] **Design matches the message.** Is the treatment in the body suited to the claim in the
      title? (tip 41)
- [ ] **Three-minute rule.** Can the slide be covered in three minutes or less? (tip 42)
- [ ] **90-second rule.** Does it take more than 90 seconds to read? Then it's too dense.
- [ ] **10-second executive test.** Can a senior executive get the point in 10 seconds? Does the
      title tell them what to think? Could any element be removed without losing the message?
      Would you be comfortable if only the titles were read aloud?
- [ ] **Squint test.** Squint — is the most important element still obvious?
- [ ] **Glance test.** Does the reader understand the chart at a single glance?
- [ ] **Eye flow.** Left-to-right for primary, top-to-bottom for secondary. (BCG; tip 44)
- [ ] **Numbers match** between title and body, exactly.
- [ ] **Source line** present, bottom-left.
- [ ] **Page number** present, bottom-right.
- [ ] **Nothing out of bounds**, no overflow, no shrink-to-fit below minimums.
- [ ] **No banned element** present.

---

## 3. First-impressions check (mbb-deck)

What a reviewer registers in the first seconds, before reading anything:
- Grouping and alignment
- Nothing out of bounds
- Consistent font sizes
- Parallel grammar in bullets
- Controlled white space
- Selective bolding of the words that carry the message

> "Reviewers judge these within seconds."

---

## 4. Production QA checklist

Run on a finished file, before it leaves the building.

**Mechanical:**
- [ ] One font family (or the sanctioned title/body pair) throughout
- [ ] All font sizes drawn from the defined scale — no off-scale sizes
- [ ] Nothing below the minimum size for its slide type (14/16pt Key Message, 8pt Detail)
- [ ] All colours drawn from the palette
- [ ] Page numbers on every content slide, none on the title slide
- [ ] Source lines on every data slide
- [ ] No banned chart types
- [ ] Alignment: no jitter between equivalent elements across slides
- [ ] Consistent footnote marker style deck-wide (pick one, e.g. ¹)
- [ ] Consistent number and currency formats deck-wide (e.g. €1,412.84)
- [ ] Consistent decimal precision within each data set
- [ ] Images not compressed by PowerPoint's defaults (BCG: *"Try discarding editing data first,
      before compressing"*)
- [ ] File named per convention

**Judgement:**
- [ ] Cover page complete: title, client, sub-headline, date, team, internal-vs-external
- [ ] Every content slide has a genuine action title
- [ ] Every "So what" is a synthesis, not a summary
- [ ] Footnote conventions applied consistently
- [ ] Confidentiality marking where required
- [ ] Status stickers on any non-final numbers

---

## 5. Deck-level checks

From kgraph57 — the cleanest statement of the deck-level gate:

> Single-slide scores do not guarantee a coherent deck. Before delivering a deck, **read only
> the headlines top to bottom** and answer yes/no:
> - Do the headlines alone form one logical argument (a pyramid: governing thought supported by
>   grouped reasons)?
> - Is each headline a single proposition — one answer or one tension — not multiple claims
>   joined by "and"?
> - Does any slide's headline repeat or contradict another's?
>
> If any answer fails, **fix the storyline before polishing individual slides.**

Plus:
- [ ] Connective test passes at every junction (therefore / but, never and-then)
- [ ] Question chain holds: each title's implied question is answered by the next
- [ ] Every slide ladders to a Key Line point; no orphans
- [ ] The Key Line points are MECE against the governing thought
- [ ] Structural completeness: a `section_divider` has a matching agenda entry; a `closing` has
      a `cover`
- [ ] Consistent chart design across similar charts (tip 65)
- [ ] Axes aligned across a series of charts on sequential slides (BCG)

---

## 6. The 24-point scored rubric (kgraph57)

Useful when you want a number rather than a pass/fail.

| Dimension | Max | 
|---|---|
| **Strategy** | 5 |
| **Data integrity** | 5 |
| **Visual hierarchy** | 4 |
| **Data-ink and graphical integrity** | 4 |
| **Portability** | 3 |
| **Marketplace safety** | 3 |

Anchors worth keeping:

- **Strategy 5:** the headline answers a decision-critical question and the visual supports a
  clear implication. **3:** useful but the implication is partly descriptive. **1:** a chart
  request with no strategic argument. **0:** does not support a decision.
- **Data integrity 5:** values, labels, units, assumptions and sources explicit and internally
  consistent. **0:** invents data or hides uncertainty.
- **Visual hierarchy 4:** the eye lands on headline, key number and implication *in the right
  order*, and emphasis follows the strength ladder with **at most one or two strong-emphasis
  elements**. **2:** emphasis applied on a whim rather than by rank.
- **Data-ink 4:** removing any non-text mark would lose information; proportions match data
  within 5% (Lie Factor ≈ 1.0); zero baselines marked; floating bars labelled; nothing truncated
  without an ellipsis.

**Thresholds:** 20–24 shippable · 17–19 usable draft, revise before publishing · 12–16 internal
draft only · 0–11 **restart from the strategic question.**

### Blocking gates — fail regardless of score
- The visual uses universal or guaranteed language beyond the evidence
- The primary reader or decision is not named
- The recommendation would change under a plausible missing-data scenario that is not disclosed
- **The meaning depends on colour alone**, tiny labels, cultural shorthand, or insider jargon
- The output implies professional verification or an affiliation that does not exist

---

## 7. Severity and routing

pstack-loki's model, which is sound and worth keeping: findings carry a severity, and **findings
route upstream to the stage responsible.**

| Severity | Meaning | Default disposition |
|---|---|---|
| SEV-1 | Wrong, misleading, or unsupportable | Always fix |
| SEV-2 | Breaks a convention; costs credibility | Fix |
| SEV-3 | Polish | Accept unless cheap |

**Routing rules:**
- A *flow* problem is a **storyline** defect, not a slide patch.
- A *chart missing an element* is an **exhibit spec** defect.
- A *number transcribed wrong* is a **build** defect (slide says 35, source says 32 — auto-fix).
- A *title claiming more than the source supports* is a **claim** defect — escalate, never
  auto-fix. (This claims/renders distinction is pstack-loki's best single idea.)

---

## 8. Review passes — a composite

Merging pstack-loki's six passes with mbb-deck's two-reviewer split:

| # | Pass | Inspects | Kind |
|---|---|---|---|
| 1 | **Deterministic lint** | Fonts, sizes, colours, bounds, jitter, page numbers, banned types, number formats | Measured |
| 2 | **Storyline / memo** | Title ladder read; connective and question-chain tests; pyramid tests | Judged |
| 3 | **Vertical logic** | Does each body prove its title? | Judged |
| 4 | **Grounding** | Every number traces to a source; title/body match | Measured + judged |
| 5 | **Visual** | Rendered pixels: hierarchy, emphasis, squint test, collisions, clipping | Judged, on renders |
| 6 | **Slop** | Lexicon, hollow phrasing, process narration, general truths | Measured + judged |
| 7 | **Cold read** | The whole rendered deck, front to back, **speaker notes off** | Judged |

**Pass 7 is the one most easily skipped and most worth keeping.** Decks circulate as pre-reads;
they must argue with their author absent. Reading the rendered deck as a stranger, in sequence,
finds things no per-slide check can.

**Pass 5 must inspect renders, not source.** A `.pptx` that lints clean can still have
overlapping shapes and unreadable contrast. Render to images and look.

---

**Settled composite (2026-08-23):** the eight-pass version adopted for `bower-qa` lives in
`07-synthesis/skill-architecture.md` §3.6 — title-craft absorbs the slop pass, and execution is
cost-ordered (mechanical passes run before judged ones). The table above is the research record.

## 9. Ordering the gates

Cheapest and most structural first — a failure upstream invalidates everything downstream.

```
BEFORE ANY SLIDE EXISTS
  1. Dump gate            — is there enough to work with?
  2. Problem definition   — SMART question, success criteria, stakeholders
  3. Storyline gate       — CTQ, So what, pattern, structure, pyramid tests, title ladder
                            ← THE decisive gate. Everything downstream is cheap by comparison.

BEFORE ANY CHART RENDERS
  4. Exhibit specs        — message, form (Zelazny), data source, element checklist

AFTER THE BUILD
  5. Deterministic lint   — measured
  6. Grounding            — numbers trace
  7. Visual QA on renders — hierarchy, collisions, squint
  8. Cold read            — the whole deck, notes off
```

The economics, stated by every source that discusses process: **a flow problem costs minutes at
the storyline gate and a rebuild cycle after the build.** McKinsey's version — synthesize
continuously, keep the storyline visible, don't synthesize in PowerPoint — is the same claim.

---

## 10. The human in the loop

Every source that discusses review says the same thing: **someone else must read it.**

- Stanley & Castles: *"ask someone else to test your storyline"*; for deductive patterns, *"ask
  a colleague to review your logic at a high level before you prepare your more detailed
  communication"*; and after delivery, ask a few people what they remember about your key
  messages.
- Zelazny: test concept visuals with colleagues — *"these diagrams will have different meanings
  for different people."*
- McKinsey: post the storyline on the team-room wall.
- BCG: *"Rehearse your delivery several times."*

For a toolkit this argues for: (a) a real review sitting at the storyline gate, not a silent
pass; (b) critique from a fresh context rather than the context that authored the thing; and
(c) the storyline artifact being something a human can actually read in two minutes.

## Cross-references
- Storyline tests → `01-storyline/storyline-quality-tests.md`
- Title diagnostics → `02-action-titles/action-title-craft.md` §8
- Exhibit checklist → `04-data-visualization/chart-craft-and-decluttering.md` §10
- The rules being checked → `05-conventions/mbb-rules-of-the-road.md`
