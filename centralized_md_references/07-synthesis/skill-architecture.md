# Skill Architecture — bower-*

**v2 — 2026-08-23.** Supersedes v1 (same day) after the independent Fable 5 review
([`fable5-review.md`](fable5-review.md)) and Philip's decisions on its four open forks:
`bower-intake` added as the eighth skill (triggerable from grillme) · grillme emits the draft
dot-dash inside `dump.md` · the revision protocol adopted (§5) · engine settled with native-first charts (§8; writer amended
same day to **pptxgenjs** after Philip's render-review argument — QA reviews pixels + fragments,
so compliance is by construction and the writer's XML never needs re-reading). Output medium:
**.pptx only** for v1.

---

## 1. The workflow this serves

Philip's described sequence, and the skill that owns each step:

```
   discuss sources, brainstorm, pressure-test the argument
   └─────────────────────────────────────────────► bower-grillme
                          │                            │ files land mid-discussion?
                          │                            └──► bower-intake  (refs → [D#] registry)
                    (storyline agreed)
                          │
   "create dump.md"  ─────┴───────────────────────► grillme's terminal action
                          │                          (brief + draft dot-dash v0 + objections)
   Philip reviews and edits dump.md            ◄─── HUMAN
                          │
   "triage"  ─────────────┴───────────────────────► bower-triage
                          │                          ├── bower-intake   (step 0, if not current)
                          │                          ├── bower-storyline (hardens v0 → v1)
                          │                          └── bower-exhibit
                          │
   triage packet closed                        ◄─── HUMAN GATE ("closed" → v1 FROZEN)
                          │
   "run"  ────────────────┴───────────────────────► bower-run
                          │                          ├── bower-build
                          │                          └── bower-qa
                          │
   revision until it's good                    ◄─── HUMAN + the revision protocol (§5)
```

### The inversion that matters

In pstack, `dump.md` is the honest mess and `/ps-start` discovers structure from it. **Here the
storyline is agreed before the dump exists.** Consequences:

- `dump.md` is a **considered brief carrying a draft argument**, not a braindump.
- `bower-grillme` carries the heaviest judgement load in the toolkit — the argument is won or
  lost there, in conversation.
- `bower-storyline` **hardens** an agreed argument; it never re-derives one from prose. (It must
  still handle the cold case — a dump written without grilling — and should say so and suggest
  grillme rather than silently guessing.)
- The gate after triage is a **last look** at the ladder and exhibit plan before slides get
  built, not a first look.

---

## 2. The eight skills

| # | Skill | Job | Justification (pstack's five) |
|---|---|---|---|
| 1 | **`bower-grillme`** | Interrogate the thinking until a storyline holds; write `dump.md` | An independent verdict; a gate before capture |
| 2 | **`bower-intake`** | Ingest source materials into a provenance-tagged, citable data inventory | File mechanics; a gate before exhibits |
| 3 | **`bower-triage`** | Orchestrate dump → frozen blueprint; resolve style; preflight; hold the gate | A gate to enforce |
| 4 | **`bower-storyline`** | Harden the dot-dash storyline; produce the slide ladder | Highest-judgement compile; file mechanics |
| 5 | **`bower-exhibit`** | Spec every exhibit before any chart renders | A gate; file mechanics |
| 6 | **`bower-build`** | Assemble `deck.pptx` from frozen artifacts | File mechanics; unattended guardrail |
| 7 | **`bower-qa`** | Full-spectrum review — argument, exhibits, style, geometry | An independent verdict |
| 8 | **`bower-run`** | Autonomous build → QA → fix loop to a terminal state | A guardrail to hold unattended |

### Deliberately not skills
- **Style resolution** — a triage step emitting `STYLE.md` (§7); re-deriving it is a sentence.
- **Revision** — a protocol (§5), not a skill; objections route by magnitude.
- **Dump writing** — grillme's terminal action.
- **Environment doctor** — a preflight step in triage, re-verified by run (§3.3).

---

## 3. Skill-by-skill

### 3.1 `bower-grillme`
**Triggers:** "grill me", "let's work out the storyline", "pressure-test this", "what's the story
here", or handing over source materials with no storyline.

**Job.** Adversarial, Socratic. Not a note-taker — a demanding colleague. Works through:
- **Purpose** — *"As a result of receiving my communication, I want my audience to…"*
- **Audience** — who decides, who influences, who can block; what they believe *today*; what
  keeps each of them up at night
- **Delivery mode** — projected, read, or both (it sets density downstream)
- **The question** — the single question they will ask, framed from *their* side
- **The So what** — climbed to rung 4, tested against the five rules
- **The pattern** — which of the seven, and an honest fit check
- **The Key Line** — 2–5 points, MECE, nameable with one plural noun
- **Evidence** — tested against the **[D#] inventory**, not against vibes
- **Constraints and stakes** — so the dump it writes passes the gate it will face

**Mid-conversation intake.** When Philip hands over files during the discussion, grillme
**triggers `bower-intake`** so the [D#] registry exists while the argument is still being
formed — a Key Line point with no [D#] behind it gets challenged on the spot, not discovered at
exhibit time.

**Behaviour.** Pushes back. Names the blank assertion when it hears one. Keeps asking "so what?"
until it stops getting an answer. Refuses a governing thought that would make a CEO reply
*"…and what should we do?"*

**Terminal action — `dump.md`, three sections:**
1. **The brief** — audience · ask · delivery mode · data inventory pointer · constraints ·
   stakes · (optional) slide/time budget as a scope input. One canonical field list, shared
   verbatim with triage's gate — a dump grillme writes cannot fail the gate it feeds.
2. **The draft storyline (v0)** — the agreed argument as dot-dash, exactly as it stood when the
   conversation closed. bower-storyline hardens this; nothing downstream re-derives it.
3. **Unresolved objections** — pushback that didn't get settled. Triage must surface these at
   the gate; it may never silently drop them. (Without this section, adversarial grilling
   degenerates into a note-taker with attitude — live conversation rewards agreement.)

Then it stops. Philip reviews and edits.

**Model tier:** deep.

---

### 3.2 `bower-intake`  *(new in v2 — the mobius-equivalent)*
**Triggers:** "ingest these files", "read these refs", files appearing in `refs/`, called by
grillme mid-conversation, or by triage as step 0.

**Job.** Turn source materials into citable evidence with provenance.

- **Classify each source by role:** *material* (claims and numbers) · *data* (spreadsheets,
  extracts) · *exemplar* (learn the register) · *template* (style-token source — flagged for
  triage, which derives `STYLE.md` from it).
- **Build `refs/manifest.md`** — one entry per source: role, origin, as-of date, owner.
- **Build `refs/inventory.md`** — the **[D#] registry**: every citable fact or number, with its
  source pointer, as-of date, and epistemic tag (FACT / EST / JUDGEMENT).
- **Extract data:** xlsx/csv → `data/src/<slug>.csv` with sheet/range provenance. Screenshots
  and PDF tables → transcribed, **tagged EST until verified against a real file**.
- **Idempotent:** re-running on an updated `refs/` diffs the registry and reports what changed —
  new [D#]s, changed values, stale as-of dates.

**Gate it enforces:** `bower-exhibit` refuses to spec a number that has no home — a
`data/src/` cell or a [D#] entry.

**Model tier:** standard (extraction mechanics), with judgement on role assignment and
epistemic tagging.

---

### 3.3 `bower-triage`
**Triggers:** "triage", "spec it out", "turn the dump into a plan".

**Job.** Orchestrator and gate-holder. In order:
1. **Dump gate** — the canonical fields present? Audience · ask · **delivery mode (projected /
   read / both)** · data inventory · constraints · stakes. Slide/time budget is *optional* — a
   scope input per decision #6, never a gate field. **Refuse and list what's missing rather
   than invent.** No v0 storyline section → say so and offer grillme.
2. **Intake step 0** — run `bower-intake` if `refs/` changed since it last ran, or it never ran.
3. **Environment preflight** — fonts installed (Georgia/Arial or the house faces), LibreOffice,
   renderer (`pdftoppm` + `pdffonts`), Node + pptxgenjs. Results go in the triage packet; **degradation is
   visible, never silent** (a missing font means pass-6 renders lie about the client's deck).
4. **Style resolution → `STYLE.md`** (§7) — from the template intake flagged, else the likaku
   fallback. Say which path was taken.
5. **Delegate** to `bower-storyline` (harden v0 → v1), then `bower-exhibit`.
6. **Evidence audit** — every FACT-tagged claim cites a [D#] or a `data/src/` cell. Unsupported
   claims get one of three fates: find the data, demote to EST/JUDGEMENT with disclosure, or cut.
7. **The triage packet:**
   - the slide ladder, connectives inline, read as a skeptic would
   - **the unresolved objections from dump.md, verbatim, with how each was resolved or why it
     stands**
   - one-line exhibit digests, specs underneath
   - `STYLE.md` and its source; preflight results
   - the disposition policy (default SEV-1 fix · SEV-2 fix · SEV-3 accept)
   - the ask, verbatim
8. **Freeze** on "closed" — `storyline.md` marked `v1 FROZEN`, titles immutable within the
   version.

**Model tier:** deep.

---

### 3.4 `bower-storyline`
**Triggers:** "harden the storyline", "the flow is broken", "recompile", or called by triage.

**Job.** Take the v0 dot-dash from `dump.md` and **harden** it into `storyline.md` +
`slideplan.md`. Hardening means: run every gate, sharpen every sentence, fix the wording —
**never reconstruct the tree from prose.** Cold case (no v0): say so, offer grillme; derive
only if Philip insists.

**`storyline.md` — the argument.** Plain-text dot-dash, readable aloud in ~2 minutes:

```
v1 FROZEN 2026-08-23
CONTEXT   …
TRIGGER   …
QUESTION  …

SO WHAT   <governing thought — one sentence, rung 4>
  • <Key Line point 1>
      – <support>  [D3]
      – <support>  [D7]
  • <Key Line point 2>
      – <support>  [E04]

## Changelog
(appended by the revision protocol — see §5)
```

**`slideplan.md` — the sequence.** One row per slide, three row types:

```
S## | storyline node | ACTION TITLE | archetype | exhibit | FACT/EST/JUDGEMENT | connective-out
G## | —              | (cover / agenda / divider / closing)                    | —
X## | appendix       | title | archetype | exhibit | tag                       | —
```

- **S## argument rows** — every one tied to a storyline node; no orphans.
- **G## structural rows** — sequence, not argument. A divider's one-line promise **is** its
  section's Key Line sentence, verbatim.
- **X## appendix rows** — ladder-exempt (no connective test, no question chain), always Detail
  density, still linted. Receives: ruled-out options, methodology, detail twins of projected
  charts.

**Hard gates before it returns:** pattern named with a stated fit reason · So what passes the
five rules · structure passes grouping-5 or deductive-4 · pyramid tests down/across/up · every
title through the classifier · **question chain** at every junction · memo read.

**Title over-determination:** compose **2–3 candidate ladders and pick** — models choose
between drafts better than they first-draft to register. The example bank is in context while
composing, with the house-register note: *plain, specific, long-is-fine, no sparkle.*

**Routing rule.** A blank assertion is a *thinking* defect — back upstream, never to a rewriter.

**Model tier:** deep.

---

### 3.5 `bower-exhibit`
**Triggers:** "spec the exhibits", "what charts do we need", or called by triage.

**Job.** One spec per exhibit, before any chart renders: `exhibits/E##.spec.md` + `data/E##.csv`
(curated from `data/src/`, provenance preserved).

Per spec: message → comparison type (Zelazny trigger words, **house-resolved matrix** — the
pie row replaced by sorted bar / stacked column) → chart form → **`render: native | image`**
(§8; native wherever PowerPoint has the type) → emphasis → data source ([D#] / src cell) →
element checklist → banned list.

**House rules applied here:**
- **Chart title states the so-what** (decision #2); dropped only if word-for-word identical to
  the action title.
- **No pie, no doughnut** (decision #3). When requested, cite house policy and note the sources
  aren't unanimous.
- **BCG annotation mechanics** (decision #8) — grey monochrome first, accent on the message
  carrier, callouts on specific data points, manual leader lines, never backfilled labels.
- One message per exhibit; two messages = two exhibits or a ladder split, routed upstream.
- **Refuses numbers with no home** — the intake gate.

**Model tier:** deep for form and message; standard for spec mechanics.

---

### 3.6 `bower-build`
**Triggers:** "build the deck", "rebuild S07", or called by run.

**Job.** The deliberately dumb *policy* — invent nothing — executed with full awareness that
pptx assembly is not dumb work (§8).

- **Refuses** without a frozen storyline.
- **Titles render verbatim.** Build fixes *renders*, never *claims*.
- **Workers emit per-slide fragments; a single assembler writes the file.** Fresh-context
  workers in waves, each holding the full storyline — but they never co-write one `.pptx`.
- Archetype per slide from `slideplan.md`; density per delivery mode; appendix rows always
  Detail density; tokens from `STYLE.md`, no off-scale sizes.
- **Overflow is a build error** — detected by the render-and-inspect loop (§8), resolved by
  splitting content or flagging the spec. Never shrink below floors.
- **Speaker notes** (presented decks): per slide — how to read the visual, its so-what, and the
  oral transition built from `connective-out`. The QA cold read stays notes-off.
- **Photography:** only files present in `refs/`, placed per the BCG convention — never
  fetched, never generated, never on or near a chart.
- Semantic shape names (`title`, `kicker`, `exhibit`, `source`, `page`) so geometry QA works.
- Accent only on message carriers.

**Model tier:** standard.

---

### 3.7 `bower-qa`
**Triggers:** "qa" (scoped), "final qa" / "ship qa" (full), "review the deck", or called by run.
Works standalone on any `.pptx` in a **degraded mode**: without specs and a storyline, passes
0, 2, 3, 6 and 7 run in full; passes 1, 4 and 5 report "no blueprint — skipped" rather than
guessing.

**Two modes:**
- **Scoped (revision cadence):** pass 0 + the ladder read (always full — it's cheap) + judged
  passes on **dirty slides only**.
- **Ship (full):** all eight passes, whole deck. `bower-run` uses ship mode before SHIPPED.

| # | Pass | Inspects | Kind |
|---|---|---|---|
| 0 | **Lint** | Fonts, sizes vs scale, palette, bounds, overflow, jitter, page numbers, source lines, banned elements (incl. pie), number formats | Mechanical |
| 1 | **Storyline & ladder** | Memo read · connective test · **question chain** · Key Line MECE · orphans · repeated/contradictory titles | Judged |
| 2 | **Title craft** | The classifier **plus bank-anchored judgement**: "does this ladder read like the bank's [REAL] titles, or like its anti-pattern gallery?" — the classifier catches defects; only the bank catches blandness | Judged + measured |
| 3 | **Vertical logic & one message** | Body *unambiguously proves* the title; exactly one message | Judged |
| 4 | **Exhibit correctness** | Form matches comparison type · element checklist · chart so-what · BCG mechanics · emphasis right | Judged |
| 5 | **Grounding** | Every number traces — exhibit numbers to `data/E##.csv` cells, **non-exhibit numbers to [D#] inventory entries** · title/body match exactly | Measured + judged |
| 6 | **Style & positioning** | On *rendered images*: theme conformance · emphasis-rung discipline · hierarchy, eye flow, whitespace · collisions, clipping · squint test | Judged, on renders |
| 7 | **Cold read** | The whole rendered deck, front to back, speaker notes off | Judged |

**Execution is cost-ordered:** 0 and the mechanical half of 5 run first — a deck failing lint
never spends deep-model time.

**Findings** carry severity (SEV-1 fix · SEV-2 fix · SEV-3 accept) and **route to the stage
that owns them**: flow → storyline · missing chart element → exhibit · mis-transcribed number →
build (auto-fix) · **title claiming more than the source supports → claim defect, escalate,
never auto-fix.**

**Model tier:** deep for passes 1–4 and 7; mechanical for 0 and 5.

---

### 3.8 `bower-run`
**Triggers:** "run", "take it from here", "build it out".

**Job.** Autonomous from a closed triage to a terminal state, no questions.

```
re-verify preflight → build waves (per-wave fast visual check) → ship-mode bower-qa →
apply the pre-committed disposition → one bounded fix cycle → SHIPPED or BLOCKED
```

- **Cannot ask questions.** It finishes or fails loudly.
- **SHIPPED** — `deck.pptx`, clean `qa.md`, a `TIMELINE.md` entry. The morning report is the
  point.
- **BLOCKED** — **all independent load-bearing questions batched into one report** (never
  serial mornings), each with the exact finding and the decision needed. Answers are revision
  deltas (§5); "run" again rebuilds only the dirty set.
- Stop conditions so it doesn't thrash.

**Model tier:** conductor holds the map only; workers routed by task nature.

---

## 4. Artifacts

```
project/
  dump.md               brief + draft dot-dash v0 + unresolved objections   ← grillme, Philip edits
  refs/                 source materials, client template
    manifest.md         one entry per source: role, provenance, as-of       ← intake
    inventory.md        the [D#] registry: citable facts, tags, pointers    ← intake
  data/src/             extracted tables with provenance                    ← intake
  storyline.md          dot-dash argument, vN FROZEN + Changelog            ← the gate reads this
  slideplan.md          S## / G## / X## rows
  STYLE.md              resolved design tokens (§7)
  exhibits/E##.spec.md  one per exhibit
  data/E##.csv          curated per-exhibit data, derived from data/src/
  deck.pptx             the deliverable
  qa.md                 findings, severity-tagged
  slides/               rendered PNGs for visual QA
  TIMELINE.md           append-only run and revision log
```

One deck per project directory. Skills compose **through files only** — no hidden state.

---

## 5. The revision protocol  *(new in v2)*

The freeze has a thaw. "Revision until it's good" runs on this machinery.

### The route table — match the fix to the magnitude

| You say | Magnitude | Route | Gate |
|---|---|---|---|
| "label overlaps on S07", "typo", "logo is stretched" | **Render** | build delta on the dirty slides | none |
| "move S09 before S07", "add an appendix slide on X", "drop S11" | **Sequence** | slideplan delta | **delta-gate** |
| "S07 overclaims — data says 32", "change this title", "the So-what should carry the date" | **Claim** | storyline delta → **version bump (v2 FROZEN…)** → re-touch of the affected leg | **delta-gate on that leg** |
| "actually the audience is the board", "the ask changed" | **Frame** | back to grillme → dump delta → full triage | full gate |

### The delta-gate
Lighter than a triage sitting, heavier than nothing: triage prints **only the changed artifact
section** — the affected ladder leg with its connectives re-run, or the new slideplan segment —
plus the dirty-set it implies. Philip says "closed". One message, not a sitting.

### Dirty-set propagation
Every slideplan row names its storyline node; every exhibit names its slide. A delta anywhere
derives its dirty set by graph walk:

```
storyline node → slideplan rows on it → exhibits on those rows → slides → scoped QA
```

"Run" after a delta rebuilds **only the dirty set**. The BLOCKED path is the same machinery:
each answered question is a delta, routed by this table.

### Versioning
`storyline.md` carries `vN FROZEN <date>` and an append-only `## Changelog` (what changed, why,
which slides it touched). **Titles are immutable within a version** — a title change is always
a version bump, however small. `TIMELINE.md` logs every delta.

### QA cadence
Revision cycles use **scoped QA**; the full eight passes run at ship. A revision that touched a
claim always re-runs pass 1 on the whole ladder — flow is a global property.

---

## 6. Doctrine packaging  *(new in v2)*

The library (~5,500 lines) is the human-facing source of truth. **Skills load policy-resolved
distillates, not the raw library.** Phase 2 produces, per skill:

| Skill | Distillates to produce | Drawn from |
|---|---|---|
| grillme | So-what rules · pattern selector · purpose/audience checklist · problem-statement fields | 01-storyline (scqa, patterns, hypothesis) |
| intake | role taxonomy · [D#] entry format · epistemic tags | 06 (loki mobius notes), 05 (integrity rules) |
| storyline | **title craft + the full example bank** (~590 lines — fits) · quality tests · house-register paragraph | 02 (both files), 01 (tests) |
| exhibit | **house-resolved chart matrix** (no pie row) · the one canonical exhibit checklist | 04 (both files) |
| build | STYLE schema · archetype catalogue · engine notes | 03 (all three), §7–8 here |
| qa | pass definitions · classifier · **the bank again** (pass 2 judges against it) · canonical checklists | 05 (rubrics), 02 |

**Canonical-copy rule:** the exhibit checklist and the title rules each live in exactly **one**
distillate; other skills reference, never duplicate. (The library's own redundancy is fine for
humans; in skill files it drifts.)

The bank is deliberately in **two** contexts — composition (storyline) and judgement (qa) —
because a judge without the bank can't recognize calibrated-but-bland.

---

## 7. STYLE.md schema  *(new in v2)*

Density is a parameter (BCG's Key Message vs Detail), so the style contract carries **two
scales**, selected by the brief's delivery mode. Appendix (X##) rows always use the read scale.

```
source:  house-template <path>  |  likaku-fallback
mode:    projected | read | both      # from dump.md; "both" = body projected, appendix read

fonts:   title Georgia bold · body Arial          # or derived from the template

[scale.projected]        # honors BCG Key Message floors — hard minimums
  title 28 · kicker 18 · body 20 · secondary 16 · chart labels ≥14 · chrome 12
[scale.read]             # likaku, verbatim
  title 22 · sub-header 18 · body 14 · chart labels ≥10 · chrome/source 9

palette: NAVY #051C2C · DARK_GRAY #333333 · MED_GRAY #666666
         LINE_GRAY #CCCCCC · BG_GRAY #F2F2F2
         accents (3+ parallel items only): #006BA6 · #007A53 · #D46A00 · #C62828
         negative: #C62828

geometry: 13.333×7.5" · margins 0.8" · title 0.15"/h0.9" · rule 1.05"
          content 1.3–6.5" · source 7.05" · page # bottom-right

chart tokens: grey base → accent carries the message · manual leader lines · no backfill
```

This resolves the review's §3.3: likaku's single scale becomes the **read** scale it actually
is; the projected scale is derived to meet BCG's floors (exact values phase-2 tunable, the
floors are not). Template-derived styles fill the same schema — both scales, both floors.

---

## 8. Engine — settled  *(amended 2026-08-23: writer = pptxgenjs)*

The deciding argument (Philip's): QA reviews the **rendered PDF/pixels**, not the .pptx — and
since workers emit **declarative JSON fragments** applied by one assembler, grounding is checked
on the fragments *before* assembly and style compliance is **by construction** (the assembler
only applies STYLE tokens; no pie builder exists, so no pie can exist). The writer's XML never
needs to be read back, so the writer is chosen purely as a generation substrate.

| Question | Decision |
|---|---|
| Writer | **pptxgenjs** (Node) — declarative API; the substrate the Anthropic pptx ecosystem battle-tested for creation |
| Fragments | **Declarative JSON**, schema in `bower-build/references/engine-notes.md`. Fragments carry content only — style/geometry keys (font, size, color, x/y/w/h) are FORBIDDEN and linted; the assembler + archetype builders own all styling from STYLE.md |
| Charts | **Native-first**: pptxgenjs `addChart` wherever PowerPoint has the type — the client must be able to edit their own deck. `render: image` only where no native form exists, flagged per exhibit spec |
| Waterfall | Native: stacked bar with an invisible base series (base = running total, background-coloured), floating bars labelled |
| Overflow | Character-budget pre-check in builders; **verdict by render-and-inspect** (soffice → PNG → bbox) |
| Concurrency | Workers emit fragments; **one assembler** (Node) writes deck.pptx once |
| QA reading | **Pixels + fragments + pdffonts** — passes 1–4/6/7 on renders and blueprint artifacts; grounding (5) on fragments vs CSV/[D#]; font families verified exactly via `pdffonts` on the PDF. No XML reading in the loop |
| Templates | **Visual-match, v1** (Philip: "I don't need exact template — the visuals must match the master"). Two channels: **theme XML** read with stdlib zip (exact palette hexes, font names, slide size — `bower_theme.py`) + **rendered template pages** (accent usage, geometry, footer conventions, register — usage is visual). QA pass 6 then verifies the deck against the same template renders: derive from pixels, verify against pixels. No master/layout embedding |
| python-pptx | **Out of the stack entirely** — theme XML needs only stdlib zip/xml; prior decks read via soffice→pdftotext; everything else is pixels |
| Preflight | Node + pptxgenjs · LibreOffice (`soffice`) · poppler (`pdftoppm`, `pdffonts`) · fonts · python3 (stdlib only, QA scripts) — checked at triage, re-verified by run, degradation always visible |
| likaku's engine | Still study-don't-adopt — its overflow heuristics inform the builders; its 40-char title gate stays out |

---

## 9. Invocation vocabulary

| Say | Runs |
|---|---|
| "grill me" · "let's work out the storyline" | `bower-grillme` |
| "ingest these files" · "read these refs" | `bower-intake` |
| "create dump.md" | grillme's terminal action |
| "triage" · "spec it out" | `bower-triage` |
| "closed" | freezes the blueprint (or closes a delta-gate) |
| "run" · "take it from here" | `bower-run` |
| "rebuild S07" | `bower-build`, scoped |
| "qa" | `bower-qa`, scoped mode |
| "final qa" · "ship qa" | `bower-qa`, all eight passes |
| "the flow is broken" | `bower-storyline` |
| "spec the exhibits" | `bower-exhibit` |
| "S07 overclaims — the data says 32" | a **claim** delta → §5 route table |
| "move S09 before S07" | a **sequence** delta → delta-gate |

---

## 10. Status

All architecture-level decisions are made (ten house policies + the four review forks). What
remains is phase-2 *work*, not open questions: write the eight SKILL.md files, produce the
distillates per §6, build the engine per §8, and tune the projected scale values in §7.

## Cross-references
- The independent review that shaped v2 → [`fable5-review.md`](fable5-review.md)
- House policy behind the rules → `05-conventions/contested-points.md`
- Why this differs from loki → `06-prior-art/pstack-loki-postmortem.md`
- Ergonomics inherited → `06-prior-art/pstack-ergonomics.md`
- QA detail → `05-conventions/quality-rubrics-and-checklists.md`
