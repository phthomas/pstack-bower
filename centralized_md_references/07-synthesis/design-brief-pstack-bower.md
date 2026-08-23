# Design Brief — pstack-bower

What the reference library implies for the skill, gathered so the build phase starts from a
position rather than from a pile. **This is a brief, not a spec** — it states findings and
recommendations; the actual design decisions are the user's.

---

## 1. The three stated defects, traced to causes

| Defect | Root cause | Where the fix lives |
|---|---|---|
| **Action titles not good enough** | Rules without calibration; no theory of *why* titles go blank; no end-product test | `02-action-titles/` (both files) |
| **Not following MBB conventions (one slide one message)** | Design doctrine fell into the gap between "what content" and "how to write XML"; the one-message rule was scoped to exhibits only | `03-slide-design/`, `05-conventions/mbb-rules-of-the-road.md` |
| **Storyline not good enough** | A borrowed dramatic arc displaced the pyramid; one fixed shape for all situations; the answer arrives ~55% in | `01-storyline/` (all four files) |

All three share one meta-cause: **doctrine depth**. loki has good architecture and thin doctrine.
The engine was never the problem.

---

## 2. Five findings that should shape the design

### Finding 1 — SCQA is an introduction, not an architecture
The most consequential correction. Minto's SCQA frames the question and delivers the answer in a
paragraph; the pyramid carries the body. Expanding SCQA into a five-act deck structure defers
the answer, which contradicts the one thing every source agrees on.

**Implication:** the deck's top-level shape is `governing thought → Key Line → support`. SCQA
occupies at most the first two slides.

### Finding 2 — there are seven storyline shapes, not one
Stanley & Castles' pattern library is the largest single gap in all prior art. An update, a
business case, a risk warning and an action plan have genuinely different structures, and the
choice is decided by one question: *does the audience need to know why, or how, or both?*

**Implication:** pattern selection is a step in the pipeline, with an explicit decision and an
explicit fit check. `01-storyline/seven-storyline-patterns.md` is the reference.

### Finding 3 — craft needs calibration, not more rules
pstack's own principle: *"advice-in-context is the weakest tool in the box."* loki uses
advice-in-context for exactly the two outputs the user rates worst. Rules constrain; exemplars
locate.

**Implication:** ship a large, real, cited example bank and put it in the composer's context —
not just the rules. Where a rule can become a machine check or an independent verdict, make it one.

### Finding 4 — density is a parameter, not a style
BCG's Key Message vs Detail Slide distinction resolves the persistent confusion about whether
MBB decks are sparse or dense. **They are both, chosen by delivery mode.** Same file, both types,
only Key Message Slides on the projector.

**Implication:** ask "projected or read?" before building. It sets type sizes, word budgets,
axis defaults and background.

### Finding 5 — the blank assertion is a thinking defect, not a wording defect
Minto's central diagnosis. "There are three options" is a symptom of incomplete thinking. A
rewriter given that title produces a more elaborate blank assertion.

**Implication:** the review must *classify* title defects, and blank assertions route upstream
for more thinking rather than to a wordsmith. See the diagnostic vocabulary in
`02-action-titles/action-title-craft.md` §8.

---

## 3. The pipeline the corpus implies

Mapped onto pstack's ergonomics (dump → triage → autonomous run → results):

```
dump.md                       Audience · ask · data · constraints · stakes · budget
   │                          Gate it. Refuse rather than invent.
   ▼
DEFINE                        SMART question · success criteria · scope · constraints
   │                          · stakeholders · sources        [Problem Statement Worksheet]
   ▼
COMPOSE  ──────────────────►  Purpose statement
   │                          CTQ / SCQA introduction
   │                          The "So what" (5 tests)
   │                          Pattern selection (1 of 7) + honest fit check
   │                          Pyramid: Key Line (2–5), MECE, grouping or deductive
   │                          Dot-dash storyline — the artifact a human reads aloud
   │                          Title ladder — every title, in order
   │                          Exhibit specs — message → Zelazny form → data → checklist
   ▼
GATE  ─────────────────────►  ONE attended sitting
   │                          Read the ladder as a skeptic. Object in plain language.
   │                          Pre-commit the disposition policy. Say "closed".
   ▼
BUILD                         Conductor + fresh workers, full storyline each
   │                          Titles immutable. Archetype per slide. Density per mode.
   ▼
REVIEW                        8 passes, cost-ordered — mechanical first (lint, grounding),
   │                          then ladder · title craft · vertical logic & one message ·
   │                          exhibits · style/positioning on renders · cold read (notes off)
   │                          [settled list: skill-architecture.md §3.6]
   ▼
SHIPPED  or  BLOCKED (one decision needed)
```

**The gate is the product.** Everything upstream exists to make the gate meaningful; everything
downstream exists to render a signed-off blueprint faithfully.

---

## 4. What to keep from loki, unchanged

The storyline is the compiler · titles freeze at the gate · claims vs renders · every number has
a home · fixes route upstream · exhibit specs before charts · one human gate then autonomy ·
cold read with notes off · overflow is an error not a formatting choice · semantic shape names ·
accent only on message carriers · image models never draw charts.

## What to keep from pstack

`dump.md` as the front door · a gate that refuses rather than invents · small-batch interviews
with a recommended default and its tradeoff each · autonomy as a dial with hardstops ·
measurement over exhortation · conductor with fresh-context workers · compose through files, no
hidden state · capabilities named once and degraded visibly · facts stored by rate of change ·
plain-intent triggers · no skill where a sentence works · the morning report.

---

## 5. Open questions for the user

~~These are decisions the library cannot make.~~ **All settled on 2026-08-23.** The resulting
skill design is in [`07-synthesis/skill-architecture.md`](skill-architecture.md); the ten house
policies are in [`05-conventions/contested-points.md`](../05-conventions/contested-points.md).
Kept below for the record.

1. ~~**Skill count and boundaries.**~~ **RESOLVED — eight, functional names** (seven at v1;
   `bower-intake` added at v2 per Fable 5 rec 1, triggerable from grillme): `bower-grillme` ·
   `bower-intake` · `bower-triage` · `bower-storyline` · `bower-exhibit` · `bower-build` ·
   `bower-qa` · `bower-run`. Style resolution, revision and dump-writing are steps, not skills.

2. ~~**The storyline artifact's form.**~~ **RESOLVED — dot-dash.** A plain-text memo is the
   primary artifact and the thing read at the gate; machine-readable forms are derived from it,
   never authored alongside it. See `05-conventions/contested-points.md` §9.

3. ~~**Output medium.**~~ **RESOLVED — `.pptx` only for v1.** Other media (one-pager, memo,
   verbal storyline) are deferred, not designed out: the dot-dash storyline is medium-agnostic,
   so adding them later is a rendering question rather than a re-architecture.

4. ~~**House style.**~~ **RESOLVED — house style first, likaku as fallback.** Yes, the toolkit
   should read a supplied template or brand guide and derive tokens; when none exists it falls
   back to likaku's McKinsey-style system (Georgia/Arial, navy `#051C2C`, the documented
   geometry). See `05-conventions/contested-points.md` §5.

5. ~~**The contested defaults.**~~ **RESOLVED 2026-08-23** — all ten decided; see the decision
   summary at the top of `05-conventions/contested-points.md`. Headlines: exec summary on slide 2
   · chart titles always state the so-what · **pie charts banned** · BCG photography convention ·
   house style else likaku (Georgia/Arial, navy `#051C2C`) · story sets the slide count · pyramid
   structure with narrative framing · BCG chart-annotation mechanics · dot-dash storyline ·
   **no generated imagery** (deferred out of v1).

6. ~~**Naming.**~~ **RESOLVED — `bower-*`, named for function, not lore.** No Marvel-style
   codenames; a reader should be able to guess what a skill does from its name.

7. ~~**How much of the review runs unattended.**~~ **RESOLVED — three-severity disposition
   adopted** (SEV-1 fix · SEV-2 fix · SEV-3 accept), pre-committed at the triage gate. **And the
   QA scope is everything, not just design** — argument, title craft, vertical logic, exhibit
   correctness, grounding, style, geometry, cold read. Eight passes; see
   [`skill-architecture.md`](skill-architecture.md) §3.6.

### New work the decisions create

Three of the ten answers add scope rather than just closing a question:

- **A house-style ingest step.** "House style if one exists, else likaku" means the toolkit must
  detect and read a supplied template or brand guide and derive tokens from it — not just carry a
  hardcoded palette. Likaku's system is the documented fallback.
- **A chart-title de-duplication rule.** "Chart titles always state the so-what" collides with the
  action title on single-chart slides. The rule to implement: the action title carries the
  slide-level claim, the chart title states what that exhibit shows; if identical, drop the chart
  title rather than duplicate it.
- **Pie-chart refusal that explains itself.** A ban enforced in the linter, plus the ability to
  say *why* it is house policy and that the sources are not unanimous — rather than presenting it
  as universal doctrine.

---

## 6. What would make this measurably better than loki

Concrete, checkable targets:

- **A pattern is chosen and named** in every storyline, with a stated reason it fits.
- **The governing thought appears on slide 2**, and the Key Line points on slide 2 are the same
  sentences as the section titles.
- **Every title passes the classifier** — no topic labels, no blank assertions, no blank verbs,
  no compound claims — and the classifier names the defect when it fails.
- **The question chain holds** at every junction, not just the connective test.
- **One message per slide is linted**, not just advised.
- **Density is chosen**, and type sizes come from the chosen scale with no off-scale values.
- **The storyline is readable aloud in two minutes** by a human at the gate.
- **The example bank is in the composer's context** when titles are written.

---

## 7. A note on the name

Marvin Bower ran McKinsey from 1950 to 1967 and is generally credited with inventing management
consulting as a profession — the values, the client-first framing, the insistence on
professional standards. **Bower** is also the name of McKinsey's brand typeface.

The codename fits the intent well: the toolkit is not meant to generate slides, it is meant to
sit beside the user and hold a standard. That framing has a practical consequence worth keeping
— the gate should feel like a **review sitting with a demanding colleague**, not a validation
step. Every source that discusses review says the same thing: someone else must read it.

## Cross-references
- Full postmortem → `06-prior-art/pstack-loki-postmortem.md`
- Ergonomics to inherit → `06-prior-art/pstack-ergonomics.md`
- Decisions to make explicit → `05-conventions/contested-points.md`
- Gate ordering → `05-conventions/quality-rubrics-and-checklists.md` §9
