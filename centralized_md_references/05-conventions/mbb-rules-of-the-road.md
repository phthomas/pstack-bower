# MBB Rules of the Road

The non-negotiables. Where a rule appears in three or more independent sources it is stated
flatly; where sources differ it is flagged and cross-referenced to
`05-conventions/contested-points.md`.

---

## The ten core principles

Adapted from mbb-deck-plugin's formulation, which is the tightest in the corpus, and reconciled
with the primary literature.

### 1. Answer first
State the recommendation up front, then the supporting arguments, then the evidence. The reader
should know your conclusion from the executive summary. *(Minto; Zelazny's Shirley letter;
McKinsey SP66.)*

### 2. Action titles, not topic titles
Every slide title is a complete declarative sentence stating the takeaway. The title alone
should convey the insight. *(Universal.)*

### 3. One idea per slide
> "If you can't summarize the slide in a single sentence, split it into two slides. If content
> does not support that one message: **if in doubt, leave it out.**"

BCG's version: *"Simple: **One concept per slide.** Everything on the slide serves the main
point — nothing is distracting."* And in its slide-conversion checklist: *"Break content into
one message per slide."*

This is the rule the user specifically flagged as missing from prior work. It has three
mechanically checkable consequences:
- The slide can be summarized in one sentence — which is its title.
- Every element on the slide serves that sentence.
- A slide needing two messages is two slides, or the storyline needs a split — **route it
  upstream, don't cram.**

### 4. MECE structure
Every breakdown is Mutually Exclusive and Collectively Exhaustive. No overlap, no gaps. Stanley
& Castles' alternative mnemonic: **NONG** — no overlaps, no gaps.

Common MECE breakdowns: geography · customer type · function · time period · driver (Volume ×
Price × Mix) · 2×2 axis.

> "When something doesn't fit MECE, **redesign the framework rather than forcing the data** —
> the framework is wrong, not the data."

### 5. Source everything
Cite sources in a small footnote (~9pt, grey) at the bottom-left of any data slide. BCG makes it
a mandatory chart element: *"Include a data source in the footnote."* likaku makes it mandatory
on **every** content slide.

### 6. Action title + framing line
Beneath the action title, a short subtitle (~10–15 words) stating the logic, methodology, or
sample size. **Title says what's true; framing line says how we know.** Examples: "Based on
n=240 customer interviews", "Acme analysis vs. industry benchmark", "Excludes one-time charges".

### 7. Data slides must narrate themselves
The McCandless five-step read: name the chart → answer the obvious questions (axes, units,
period, n) → the action title states the insight → the proving data points are visually
highlighted → the takeaway sets up the next slide. *"If a slide can't be talked through this
way, the slide isn't done."*

### 8. Every slide is a table
Think of any layout as rows and columns — rows = items, columns = dimensions (measure,
rationale, impact, timing). Prevents scattered elements. A rule of thumb; adjust when a chart or
framework demands otherwise.

### 9. Horizontal and vertical logic
- **Horizontal:** read all action titles in sequence — they must tell the storyline by
  themselves.
- **Vertical:** on each slide, the content must fully support its title.

Both are tested explicitly at review. *(Minto's two substructures, applied to a deck.)*

### 10. Synthesize, do not summarize
Slides state implications (the "So what"), not organized facts. *(Minto ch.7; Stanley & Castles
rule 3 for groupings.)*

---

## The flow rules

Three formulations of the same requirement, in increasing order of usefulness:

**a) The "so what?" chain.** For every slide, ask "so what?" The next slide's title should
answer it.

**b) The connective test.** Between every pair of consecutive titles you must be able to insert
**"therefore"** or **"but"** — never **"and then"**. "And then" means the slides are adjacent,
not connected.

**c) The question chain (strongest).** *"To 'own the flow,' each slide should trigger a question
answered by the title of the next slide."* — Dave McKinsey tip 17.

(c) is best because it's diagnostic: it tells you *what the missing slide should say*, not just
that something is missing.

Corollary — **Minto's vertical Q&A**: each box, when stated, raises a question that the boxes
beneath it answer. Horizontal flow is the same mechanism laid on its side.

---

## Hard bans

### Content
| Banned | Because |
|---|---|
| **Topic titles** | The reader has to do the work, and may reach the wrong conclusion |
| **Multiple ideas per slide** | Splits attention; breaks the one-message rule |
| **Bullet dumps** | Bullets must be parallel and ladder to the title |
| **Recommendation buried at the end** | It belongs at the front |
| **Vague action titles** | "Revenue is doing well" — be specific |
| **Action titles longer than two lines** | The claim is compound; split or sharpen |
| **Numbers in titles that don't match the body** | Instant credibility loss |
| **Passive/vague recommendations** | "It might be worth considering" is not a recommendation |
| **General truths and absolute claims** | Says nothing / leaves no room for outliers |
| **Process narration** | "We conducted 15 interviews and learned a lot" — say what they revealed |
| **Clotheslines** | 5+ parallel items unlabelled and ungrouped |
| **Single bullets and paragraph bullets** | A single bullet isn't a list; write it as plain text |
| **Inconsistent footnote markers, units, number formats** | Pick one and hold it deck-wide |

### Visual
| Banned | Source |
|---|---|
| 3D, gradients, drop shadows, bevels | Universal |
| Chart backgrounds and plot-area shading | BCG, Knaflic |
| Uncurated or decorative imagery near content | mbb-deck, kgraph57. **House policy (decision #4): photography IS permitted under BCG's curation convention** — tone, subject, composition considered — **but never on or near a chart.** This row bans decorative use, not curated photography. |
| **Coloured boxes behind standard text** | BCG: *"Do not use color-filled textboxes to visually organize content."* Exception: hierarchically superior text (column and section headers), applied consistently across that level |
| Italics, ALL CAPS, underline as emphasis | BCG (underline reserved for hyperlinks) |
| **Any emphasis inside a title or subtitle** | BCG, stated three times |
| Dual y-axes | mbb-deck, Dave McKinsey tip 64 |
| Rainbow palettes | Universal |
| Undisclosed axis truncation | Universal |
| Screenshots of charts | mbb-deck |
| Animation | mbb-deck (BCG: Visual Services only) |
| Decorative bars with no data | kgraph57 |
| Faux affiliation with named consulting firms | kgraph57 |

---

## The mandatory furniture

Every content slide (not title, not divider):
1. Action title
2. Title separator rule
3. Content area
4. **Source line** — bottom-left, ~9pt grey, `Source: <origin>, as of <date>`
5. **Page number** — bottom-right, just the number, no "Page" or "Slide" prefix
6. *(optional)* Confidentiality marking, centre footer
7. *(when numbers aren't final)* A status sticker: PRELIMINARY / INDICATIVE / FOR DISCUSSION /
   ILLUSTRATIVE

---

## The density decision — ask before you build

**"Will this be projected, or read?"** This single question sets type sizes, word counts, axis
defaults and background colour. See `03-slide-design/mbb-slide-standards.md` §1.

- **Projected → Key Message Slide.** Minimal text, 20pt body, 14pt absolute floor, grey
  background, no y-axis by default.
- **Read → Detail Slide.** Dense but purposeful, 12pt body, 8pt absolute floor, white
  background, y-axis by default.

The two can be mixed in one file. Only Key Message Slides go on the projector.

---

## Integrity rules

These are the ones that cost credibility rather than polish.

1. **Every number on a slide traces to a source.** A cell in a data file or a cited document.
2. **Title numbers and body numbers match exactly.**
3. **Epistemic honesty.** Distinguish fact from estimate from judgement. A hypothesis is not a
   finding. Estimates disclose their method. Judgements are disclosed as judgements. *(pstack-
   loki's FACT / EST / BELIEF tagging is a good mechanism for this.)*
4. **Status stickers used honestly.** They manage expectations and protect credibility.
5. **The neutrality test.** Would someone who disagreed with your conclusion call the exhibit
   fair?
6. **Steelman rejected options.** A strawman option is a lie the audience will smell. Ruled-out
   options belong in the appendix *"to show they have been considered but ruled out"* — silence
   is a hole a sceptic will find.
7. **Disclose what would change your mind.** Optional but powerful on a recommendation slide.
8. **State decision criteria before revealing the recommendation** — pre-commitment discipline.
9. **Honest scaling.** Zelazny's whole scaling section. The picture is the argument.
10. **No fabricated data.** Ever, including as a placeholder that might survive to the client.

---

## When to break the rules

The corpus is unanimous that these are guidelines with a purpose, and Zelazny is explicit:

> "Choosing, and especially using, charts is not an exact science. And so you'll note a liberal
> sprinkling of qualifiers, such as generally, occasionally, most of the time, some of the time,
> all of which imply that **your judgment must play a role**."

And Stanley & Castles, quoting Picasso: *"learn the rules like a pro so we can break them like
an artist. We can only use rules if we know what they are."*

The distinction worth holding: **structural rules** (one message per slide, answer first, MECE,
every number sourced) are close to absolute, because breaking them costs comprehension or
credibility. **Style rules** (pie charts, exec summary placement, whether photography is
allowed) are house policy, and a good toolkit should let the house set them.

## Cross-references
- Where sources disagree → `05-conventions/contested-points.md`
- Checkable versions of these → `05-conventions/quality-rubrics-and-checklists.md`
- The design detail behind each → `03-slide-design/mbb-slide-standards.md`
