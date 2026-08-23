# pstack-loki — Postmortem

Source: `github.com/phthomas/pstack-loki` — eight skills, read in full.

The user's report: the resulting presentations are *"not aligned with what I want"*, with three
named defects — weak action titles, MBB conventions not followed (specifically one-slide-one-
message), and a weaker storyline.

**The striking finding: loki's own README names the same three failure modes as its reason for
existing.** So the diagnosis was right and the implementation didn't close the gap. That makes
this a more useful postmortem than a simple "it was bad" — the question is *why correct
intentions produced insufficient output.*

---

## 1. What loki gets right — keep these

loki is not a weak toolkit. Carrying these forward is most of the win.

| Idea | Why it's right |
|---|---|
| **"The storyline is the compiler"** — nothing builds until the title ladder reads as a persuasive memo | The correct architecture. Matches McKinsey's *"PowerPoint is not a good tool for synthesis"* |
| **Titles freeze at triage** — workers render titles verbatim | Prevents drift; makes the gate meaningful |
| **Claims vs renders** | *Slide says 35, CSV says 32 → transcription fault, auto-fix. Title claims 35, CSV says 32 → BLOCKED.* The best single idea in the toolkit |
| **Every number has a home** — traces to a CSV cell or dump reference | The integrity rule that matters most |
| **Fixes route upstream** — a flow problem is a storyline bug | Correct, and rare |
| **Exhibit specs before any chart renders**, with a 10-point element checklist | Matches the corpus's exhibit doctrine closely |
| **Zelazny comparison→form table** in loki-exhibit | Faithful to the source |
| **One human gate, then autonomous** | The ergonomic the user likes |
| **Cold read with speaker notes off** | *"decks circulate as pre-reads and must argue with their author absent"* — correct and often skipped |
| **Overflow is a build error, not a formatting choice** | Matches BCG's "cut content, don't shrink type" |
| **Semantic shape names** so geometry lint can work | Real engineering insight |
| **Accent only on message carriers** | Matches BCG's grey-then-highlight rule |
| **Image models never draw charts** | *"they are good enough at fake infographics to be dangerous"* — exactly right |

---

## 2. Defect 1 — weak action titles

### What loki has
`loki-storyline` Step 3 lists seven title rules: complete sentence with a verb · falsifiable ·
carries the so-what · specific (number or noun) · ≤14 words · no slop lexicon · tagged
FACT/EST/BELIEF. Plus one passing and one failing ladder example.

These rules are correct. They are also roughly what mbb-deck has, and roughly what this library
now has in `02-action-titles/action-title-craft.md` §2.

### Why it isn't enough

**(a) Rules without calibration.** Seven bullet points do not locate a target. The model can
satisfy every rule and still produce a title that a partner would rewrite. What's missing is a
*corpus* — dozens of before/after pairs, real firm titles, full ladders — so the model has
something to match against rather than merely comply with. That is why this library ships
`action-title-examples-bank.md` as a separate, deliberately large file.

**(b) No theory of the failure.** loki says "don't write topic titles". It does not contain
Minto's **intellectually blank assertion** — the observation that "There are three options" is a
symptom of *incomplete thinking*, not of poor wording. That distinction changes the fix: a blank
title must be routed back for more thinking, not reworded. An agent told to "make this title
better" will produce a more elaborate blank assertion.

**(c) No end-product test.** Minto's action-statement machinery — *visualize a real person doing
this; what are they holding?* — is absent. It is the sharpest available tool against
"Strengthen regional effectiveness" and its family, and those are exactly the titles that read
as bland.

**(d) One example ladder.** Two ladders (one pass, one fail) in the entire toolkit. Compare the
real USPS deck titles: they are plainer, longer, and more specific than anything loki's rules
would encourage — several run well past 14 words. loki's ≤14-word cap may actively push titles
toward the terse-but-empty register.

**(e) Titles carry a theme tax.** See defect 3.

### The fix
Theory (why titles go blank) + a large calibration corpus + the end-product test + a routing
rule that sends blank assertions upstream rather than to a rewriter.

---

## 3. Defect 2 — MBB conventions, especially one-slide-one-message

### The finding
**"One slide, one message" does not appear as a rule anywhere in loki-storyline or loki-build.**

It appears once, in `loki-exhibit` Step 1, scoped to *exhibits*:
> "One message per exhibit… If a chart seems to need two messages, it's two exhibits or the
> ladder needs a split."

That's the right rule applied to the wrong object. A slide can hold one exhibit and still carry
three messages in its kicker, bullets and takeaway box. The universal MBB rule — BCG's *"Simple:
One concept per slide. Everything on the slide serves the main point"* — is not stated, not
gated, and not linted.

### The broader gap: no design doctrine at all
`loki-build` explicitly delegates: *"Delegate the *how* to whatever pptx engine the environment
provides… Loki-build governs *what* is on each slide; the engine skill governs *how* XML gets
written. Don't duplicate engine documentation here."*

Separating *what* from *how* is good engineering. But **MBB slide design is not engine
documentation** — it is doctrine, and it went missing in the gap:

| Present in the corpus | In loki? |
|---|---|
| Key Message vs Detail Slides (the density decision) | ✗ |
| Type scales with hard floors per slide type | Partial — STYLE.md has "min sizes" but no scale |
| Grey-first, highlight-with-accent | ✓ (accent rule only) |
| No emphasis inside titles, ever | ✗ |
| No colour-filled text boxes | ✗ |
| Bullet discipline: groups of ≥2, max 3–5, ≤2 lines, no clotheslines | ✗ |
| "Every slide is a table" | ✗ |
| Slide archetype catalogue | Partial — 4 slide types |
| Mandatory furniture (source line, page number) | Partial — source + tracker |
| BCG's five design principles | ✗ |
| McCandless five-step read | ✗ |
| Emphasis strength ladder | ✗ |
| 90-second / 10-second / squint tests | Squint only |

`STYLE.md` is a handful of tokens the model invents per project. That is a template, not a
standard. When the design contract is generated fresh each run, output cannot be consistent.

### The fix
A real design reference (now `03-slide-design/`), the one-message rule stated at slide level and
enforced at both the storyline gate and the lint, and a slide archetype catalogue so the builder
picks from a menu rather than improvising.

---

## 4. Defect 3 — the storyline

This is the deepest problem, and it is structural rather than a matter of missing detail.

### The Western beat sheet

loki-storyline Step 2 mandates a five-beat structure:

| Beat | Mapped to | Share of deck |
|---|---|---|
| Cold Open | Situation | ~5–10% |
| The Stranger Rides In | Complication | ~15–20% |
| Raising the Stakes | (implied Question) | ~25–30% |
| High Noon | Answer | ~25–30% |
| The New Order | Resolution | ~15–20% |

loki argues the structure is universal and only the *skin* is dialable (`theme intensity: 0–3`).
Three problems with that:

**(a) It misreads Minto.** SCQA is an **introduction** — a paragraph, a slide, at most two. loki
expands it into the deck's entire top-level architecture, giving Situation ~10% and Complication
~20% of the slides. In Minto, the deck body is the *pyramid*: governing thought → Key Line →
support, ordered by one of four logical orders. loki has no pyramid, no Key Line, no MECE check
against the governing thought except a single line ("Acts II–III must be MECE").

**(b) The answer arrives 50–60% of the way in.** "High Noon" — the decision moment — starts after
Cold Open, Stranger, and Raising the Stakes. That is *the exact structure Zelazny's J.J. Ltd.
example is written to condemn*: it took the board until the summary of conclusions to know the
recommendation, "at least 45 minutes, and maybe a lot longer." Every source in the corpus says
answer first. A five-act arc cannot answer first — withholding is what makes it an arc.

To be fair, loki does mandate a frame with a controlling idea at the top of `storyline.md`. But
the *deck* is beat-ordered, and the beat order defers the answer. There is no executive summary
slide anywhere in loki's slide grammar.

**(c) Only one shape.** *"Structure is non-negotiable."* Every deck gets the same five beats.
But an update is not a business case is not a risk warning is not an action plan. Stanley &
Castles identified **seven** patterns precisely because forcing one shape onto all situations
produces exactly the "storyline isn't as good" complaint — a Traffic Light update crammed into
a High Noon showdown will feel wrong, and no amount of title polish fixes it.

Notice also that four of the seven patterns are *deductive* (statement → comment → therefore) and
three are *groupings*. loki's beats are neither; they're a dramatic arc that resembles SCQA
without being it.

### What's missing beyond the beat sheet
- **No pattern library.** The single biggest gap.
- **No pyramid.** No Key Line, no plural-noun test, no summarize-the-group discipline, no
  grouping-vs-deduction choice.
- **No "So what" rules.** The frame has "controlling idea: ONE falsifiable sentence, ≤25 words",
  which is good, but not Stanley & Castles' five tests or Minto's synthesis machinery.
- **No question-chain test.** loki has the connective test (therefore/but, never and-then),
  which is good but weaker than *"each slide should trigger a question answered by the title of
  the next slide"* — the connective test says something's wrong; the question chain says what's
  missing.
- **No purpose statement.** Stanley & Castles' *"As a result of receiving my communication, I
  want my audience to…"* — subtly but importantly different from loki's "the ask".
- **No medium decision.** loki always builds a `.pptx`. Sometimes a one-page storyline, a memo,
  or five slides is the right answer.

### The theme intensity dial doesn't solve it
loki's defence is that theme intensity 0 gives a *"pure McKinsey surface"*. But intensity
controls the **skin** (imagery, act dividers, speaker-note metaphors), not the **structure** —
which the skill states is non-negotiable. So at intensity 0 you still get a five-act arc with the
recommendation at 60%, just without the tumbleweeds. **The structural problem survives the dial.**

---

## 5. Root cause

Three, in order of importance:

1. **A borrowed structure displaced the domain structure.** The Western arc is a genuinely good
   idea for holding attention, and BCG's own guide uses narrative framing (hero/mentor, the gap,
   toggling to build tension). But loki applied it at the *architecture* layer, where the pyramid
   belongs, rather than at the *wording and framing* layer, where narrative helps. Narrative
   should inform how each element is worded; it should not decide the order of the deck.

2. **Rules were treated as sufficient.** loki states good rules and expects compliance to produce
   craft. But craft is calibration — the model needs exemplars, not just constraints. This is
   pstack's own principle turned against loki: *"advice-in-context is the weakest tool in the
   box."* loki uses advice-in-context for exactly the two things the user says came out worst.

3. **Design doctrine fell into the what/how gap.** Sound separation of concerns, but MBB slide
   convention is neither "what content" nor "how to write XML" — it's a third thing, and it had
   no home.

---

## 6. What to change in pstack-bower

| Change | From | To |
|---|---|---|
| **Storyline architecture** | Five-beat Western arc, mandatory | Pyramid + a pattern library (the seven patterns), pattern chosen to fit the situation |
| **Answer position** | ~50–60% in (High Noon) | Slide 2, executive summary = governing thought + Key Line |
| **SCQA scope** | The whole deck | The introduction — one slide, maybe two |
| **Title guidance** | 7 rules | Rules + failure theory + a large calibration corpus + end-product test |
| **Blank assertions** | Not identified | Named defect that routes upstream, never gets reworded |
| **One message per slide** | Only for exhibits | Stated at slide level, gated at storyline, linted at build |
| **Design doctrine** | Delegated to the engine; STYLE.md invented per run | A real standard, versioned, with archetypes and a type/colour system |
| **Flow test** | Connective test | Connective **+** question chain (diagnostic) |
| **Theme** | Structural (beats) + skin dial | Register/wording only; structure is always the pyramid |
| **Output medium** | Always .pptx | ~~Chosen per engagement~~ **Superseded 2026-08-23: v1 is .pptx-only by decision; other media deferred, not designed out** |
| **Generated imagery** | First-class, its own skill | Off by default; opt-in for dividers/covers only |

## What to keep, unchanged
The storyline-is-the-compiler architecture · titles freeze at the gate · claims vs renders ·
every number has a home · fixes route upstream · exhibit specs before charts · one human gate
then autonomy · cold read with notes off · overflow is an error · semantic shape names · accent
only on message carriers · image models never draw charts.

That is a lot of good machinery. **The problem was never the engine — it was the doctrine loaded
into it.**

## Cross-references
- The pattern library loki lacks → `01-storyline/seven-storyline-patterns.md`
- The calibration corpus → `02-action-titles/action-title-examples-bank.md`
- The design doctrine → `03-slide-design/mbb-slide-standards.md`
- The narrative-vs-pyramid question → `05-conventions/contested-points.md` §7
