# Action Title Craft

Sources: Minto ch.7 (the underlying theory); Gene Zelazny, *Say It With Charts* ("message
titles"); Dave McKinsey tips 8, 9, 17, 36, 37, 40, 51, 55; Stanley & Castles (the "So what");
mbb-deck-plugin; kgraph57.

**This is the reference the whole toolkit turns on.** Rules alone don't produce good titles —
every prior-art skill already has the rules and still produces bland output. What's missing is
(a) understanding *why* titles go bland, and (b) a calibration corpus. This file covers the
first; `action-title-examples-bank.md` covers the second.

---

## 1. Why agent-written titles go bland — the actual mechanism

Not "the model doesn't know the rules". Four specific causes, each with a different fix:

### Cause 1 — the title is written from the slide, not from the argument
A title summarizing *what is on this slide* produces "Q2 Revenue by Segment". A title
summarizing *what this slide proves in the argument* produces "Enterprise carried the entire
Q2 beat; SMB shrank for a third quarter". You cannot write the second without knowing the
whole ladder. **Fix: titles are written at storyline time, top-down, before any slide exists —
and never re-derived per-slide.**

### Cause 2 — the intellectually blank assertion
Minto's central diagnosis. The writer groups ideas but doesn't complete the thinking, then
labels the group instead of summarizing it:

> "The company should have three objectives." / "There are two problems in the organization."
> / "We recommend five changes."
>
> "I call these statements intellectually blank because they do not in fact summarize the
> essence of the ideas grouped below them, they simply state the kind of idea that will be
> discussed. As such, **they are deadly for both the reader and the writer.**" *(OCR-repaired)*

Deadly for the *reader* because it anchors nothing — Minto's radio anecdote: a speaker says
"for three reasons", the listener latches onto the first sub-point, and the two proceed to talk
past each other entirely. Deadly for the *writer* because it **hides incomplete thinking**.

Her worked case: someone wrote "The company has two organization problems". Pressed to say what
the two had in common and in what order they belonged, he discovered he wasn't describing
organization problems at all — he was describing *areas where greater delegation is needed*,
there were four of them, and the real insight was that **the company's major organizational
problem was its inability to delegate authority.** The blank assertion had been concealing the
finding.

**Fix: treat every "there are N…" / "key considerations" / "overview of…" title as a signal
that the thinking isn't finished — route it back to the storyline, don't reword it.**

### Cause 3 — vague verbs with no end product
Minto's second diagnosis, for action statements. All actions look alike in isolation — they
all read "we should [verb]". You can only tell whether they belong together by reference to
the effect they jointly produce, so the effect must be stated concretely enough to be checkable.

**The end-product test:** *visualize a real person actually taking the action, and ask what
they are holding when they've finished.* If the answer is "nothing", the wording is empty.

Her translation table:

| What was said | What was meant |
|---|---|
| Strengthen regional effectiveness | Assign planning responsibility to the regions |
| Reduce accounts receivable | Establish a system for following up overdue accounts |
| Review management processes | Determine whether management processes need to be revised |
| Improve financial reporting | Install a system that gives early notice of change |
| Tackle strategic issues | Define a clear long-term strategy |
| Redeploy manpower resources | Place people in positions of comparable responsibility |

And the specificity threshold: *"you can't say 'I do these three things so that I can improve
profits', because a 10 percent improvement and a 2 percent improvement are both an improvement
in profits, but the steps you would need to take to achieve each would differ."* Say **"to
improve profits by 10 percent by January 15."**

### Cause 4 — describing the subject instead of what's important about it
Zelazny's diagnosis, from the chart side:

> "COMPANY SALES TREND / PRODUCTIVITY BY REGION / PERCENTAGE OF ASSETS BY DIVISION…
> These titles describe the subject of the chart, but they don't say what's important about it.
> What about sales performance? … **Don't keep it a secret; let your message head the chart.**"

His demonstration of the cost: a pie chart of profits by region titled "PROFITS BY REGION".
Most readers focus on the West and conclude "West accounts for almost half of profits". But the
designer wanted to stress that "**North generates the smallest share of profits**". With a topic
title, *you run the risk of being misunderstood.* The message title eliminates the risk.

His four-way demonstration on a single trend line — all true, only one is the message:
1. The number of contracts has increased
2. The number of contracts has been fluctuating
3. In August, the number of contracts reached its highest point
4. The number of contracts declined in two of the eight months

> "A message title is similar to a headline in your newspaper or magazine; it is brief and to
> the point and summarizes what you're about to read."

---

## 2. The rules

### Hard rules

| # | Rule | Check |
|---|---|---|
| 1 | **Complete declarative sentence with a finite verb** | Parse: subject + verb. "Q2 Performance" fails. |
| 2 | **One proposition** | No two claims joined by "and". Split or sharpen. |
| 3 | **Falsifiable** | Someone could disagree. If no one could, it's decoration. |
| 4 | **Specific — contains the number or the proper noun** | "Significant pressure" fails; "NIM compressed 35bps" passes. |
| 5 | **Fits the title bar in ≤2 lines; 1 line preferred** | BCG allows 2, recommends 1 for Detail Slides. |
| 6 | **Present tense, active voice** | "Price drives growth" beats "growth was driven by price". |
| 7 | **Sentence case; no emphasis inside the title** | BCG: *never* bold, colour, italicise, underline or ALL-CAPS within a title. |
| 8 | **Every number in the title appears identically in the body** | Title says 35, body must say 35. |
| 9 | **No slop lexicon** | unlock, leverage, journey, robust, holistic, empower, transformative, landscape, delve, synergy, seamless, best-in-class… |
| 10 | **No general truths, no absolutes** | "Managing risk is important for success" says nothing. "All divisions fail to follow best practices" leaves no room for outliers. |
| 11 | **Results, not process** | Never "we conducted 15 interviews and learned a lot" — always what they revealed. |

**Lintable vs judged.** Rules 1, 4, 5, 7, 8 and 9 (plus the compound check in 2) are
mechanically lintable. Rules 3, 6, 10 and 11 need judgement. **Rule 6 is a default register,
not a lint**: the calibration bank's own [REAL] titles include past-tense constructions —
"Losses **have been driven** by volume declines…" is verbatim McKinsey. Never auto-flag tense
or voice; raise it only when the passive hides the actor.

### Judgement rules

- **Carries the "so what", not the "what".** Data + implication.
- **Synthesise, don't summarise.** "We win 40% of negotiations" is a fact. "Negotiation
  conversion declined from 55% to 40%, likely driven by recent scaling of the sales team" is an
  insight.
- **Points toward action or decision.** McKinsey SP66's test for a governing thought applies
  down the tree: if the reader's first reaction is "…so what should we do?", it's incomplete.
- **Not obvious.** *"If you shared your hypothesis with the CEO, would it sound naive?"*
- **Independent.** Dave McKinsey tip 37: each slide gets its own title; don't repeat a title
  with "(I)" and "(II)". If two slides genuinely continue one thought, use the ellipsis form.

### On questions as titles
> "In general, I do not recommend using questions as slide titles since they make the audience
> do the work. … One reasonable exception is asking a question in the title of one slide and
> then answering it in the title of the next one, but **use this technique sparingly**."
> — Dave McKinsey, tip 51

### The ellipsis technique (tip 36 / tip 51)
Span one thought across two slides:

> "USPS should pursue volume boosting initiatives…"
> "…by taking critical actions leading to ~$2 billion of incremental net income in 2020."

Use where the second slide genuinely completes the first. Accenture's USPS deck also uses "… as"
to signal an *additional independent factor* rather than a consequence — a subtler variant.

---

## 3. The improvement ladder

The single most useful calibration device found. Climb every title to rung 4.

| Rung | Kind | Example |
|---|---|---|
| **1** | A topic label | "Market dynamics" |
| **2** | A generic claim | "Focus on expansion to attractive geographies" |
| **3** | A specific but wordy sentence | "We should prioritise Asia Pacific and North America because they have better margins and growth and are large markets" |
| **4** | A concise, quantified insight | "Asia Pacific and North America prioritized due to margins, growth and 100+ EUR mn market size" |

Stanley & Castles' parallel ladder for the "So what", weakest to strongest:
1. *"We should be concerned about meeting the new standards."* — obvious
2. *"We should take steps to meet the new standards."* — still obvious
3. *"It's possible to change our manufacturing processes to meet the new standards."* — implies
   something unflattering and says nothing useful
4. *"SurfCo should offer $500,000 for 51% of the Swell Boards start-up to regain market share
   from competitors within the next two years."*

---

## 4. Title grammar — reusable sentence shapes

Titles fail partly because the writer has no *form* to pour the claim into. These are the shapes
that recur across the real decks in the corpus.

| Shape | Template | Example |
|---|---|---|
| **Driver attribution** | *[Outcome] was driven by [driver], not [plausible alternative]* | "The Q3 margin decline is caused by raw material costs, not pricing" |
| **Decomposition** | *[Total] is concentrated in [subset]* | "Two of our four segments generate 85% of profit" |
| **Trend + implication** | *[Metric] [moved] [amount] over [period], [consequence]* | "Deposit growth stalled at 2% while funding costs rose 60bps" |
| **Gap** | *[Required] but [actual], leaving a [size] gap* | "Closing the 2027 target needs $42M of cost-out; three identified opportunities cover it" |
| **Comparative verdict** | *[Option] is [verdict] because [criterion]* | "Outsourcing to Black Inc. meets all criteria" |
| **Threshold breach** | *[Metric] will [breach] by [date] unless [condition]* | "NIM compresses ~35bps by Q4 unless the mix shifts" |
| **Falsified assumption** | *[Widely held belief] does not hold: [evidence]* | "CEO compensation does not vary with company size" |
| **Recommendation** | *[Actor] should [verb] [object] by [date] to [effect]* | "Acme should exit Segment C in Q3 and reinvest in Enterprise within 12 months" |
| **Consolidation / structural** | *[Market] is [structural change], [evidence]* | "The market is consolidating around three players, who now hold 71% share" |
| **Counter-intuitive** | *Despite [expected], [actual]* | "EBIT margin declines despite growth" |

Note the **"X, not Y"** construction. It appears repeatedly in strong titles and rarely in weak
ones, because naming the rejected alternative is what makes a claim falsifiable and non-obvious.

---

## 5. Where titles live in the hierarchy — three levels, three registers

A frequent source of confusion. They are not the same job.

| Level | Register | Rule | Source |
|---|---|---|---|
| **Presentation title** | "So what", SMART, present participle | *"Restoring the USPS to Profitability by 2020"* | Dave McKinsey 8–9 |
| **Slide title (action title)** | "So what" | The claim this slide proves | Everyone |
| **Chart / graph title** | **"So what"** | States what this exhibit specifically shows — narrower than the slide-level claim | House decision #2 |

**The chart-title rule was contested and is now settled** (house decision #2, 2026-08-23):
**chart titles always state the "so what"** — siding with Zelazny, BCG and mbb-deck against Dave
McKinsey's tip 55. Division of labour: the **action title carries the slide-level claim**; the
**chart title states what this exhibit specifically shows**, which is normally narrower. If the
two would be word-for-word identical, **drop the chart title** rather than duplicate it —
duplication is noise, not consistency. Full reasoning: `05-conventions/contested-points.md` §2.

### The framing line / subtitle
mbb-deck adds a useful third element beneath the action title:

> **Title says what's true; framing line says how we know.**
> ~10–15 words, neutral grey, under the title. Examples: "Based on n=240 customer interviews",
> "Acme analysis vs. industry benchmark", "Excludes one-time charges".

This is a good pressure valve: it lets the title stay a clean single proposition while the
methodology qualifier still appears above the fold.

---

## 6. Length

| Source | Guidance |
|---|---|
| BCG Format Guide | Both slide types allow up to 2 lines. **"Wherever possible, it is recommended that Detail Slide titles be kept to one line."** One-line titles let audiences grasp meaning at a glance and keep attention on the speaker. |
| mbb-deck | Two lines max; "if you can't fit it in two lines, the claim is too compound — split the slide or sharpen the title." |
| pstack-loki | ≤ ~14 words |
| kgraph57 | Target ≤40 half-width units (~20 Japanese characters); **never two claims joined by a conjunction** |

Practical synthesis: **aim for one line; two is the ceiling; over two means the claim is
compound, not that the font is too big.** Never shrink type to fit a title.

---

## 7. Writing procedure

1. **Have the storyline first.** The pyramid, the pattern, the Key Line. A title is a leaf of a
   structure; you cannot write it well without the structure.
2. **State the claim in plain speech, out loud.** "OK so the thing here is that basically all
   the growth came from enterprise and SMB actually shrank." Overlong and informal is fine.
3. **Cut to one proposition.** If there are two, you have two slides — or one is the framing line.
4. **Insert the number or the proper noun.** If neither exists, ask whether the slide has
   evidence at all.
5. **Apply the end-product test** if it's an action title: what's in their hand when it's done?
6. **Run the hard rules** (§2).
7. **Read it in the ladder.** Does the previous title's question get answered? Does this one
   raise the next? Can you insert "therefore" or "but"?
8. **Re-check against the governing thought.** Does this title ladder up? If it supports
   nothing, cut the slide.

---

## 8. Diagnostic vocabulary — name the defect, don't just say "weak"

Useful for review output; each maps to a distinct fix.

| Defect | Signature | Fix |
|---|---|---|
| **Topic label** | Noun phrase, no verb | Ask "what about it?" |
| **Intellectually blank assertion** | "There are N…", "Key considerations", "Overview of…" | Complete the thinking upstream — do not reword |
| **Blank verb** | strengthen, improve, review, tackle, redeploy, optimise, enhance | Apply the end-product test |
| **Unquantified claim** | "significant", "substantial", "strong" | Insert the number |
| **Compound claim** | Contains "and" joining two propositions | Split the slide |
| **Process narration** | "We analysed…", "We conducted…" | State what was found |
| **General truth** | True of any company, any year | Delete the slide or find the real claim |
| **Absolute** | "all", "every", "no" without qualification | Bound it |
| **Overclaim** | Title asserts more than the exhibit proves | Weaken the title or strengthen the evidence |
| **Slop** | leverage, unlock, journey, robust, holistic | Say the thing plainly |
| **Orphan** | Supports no Key Line point | Cut it or fix the pyramid |
| **Non-sequitur** | Only "and then" connects it to its neighbour | Storyline defect — route upstream |

## Cross-references
- Calibration corpus → `02-action-titles/action-title-examples-bank.md`
- Theory of summarizing → `01-storyline/minto-pyramid-principle.md`
- Ladder-level tests → `01-storyline/storyline-quality-tests.md`
- The chart-title disagreement → `05-conventions/contested-points.md`
