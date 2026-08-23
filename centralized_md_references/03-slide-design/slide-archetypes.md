# Slide Archetypes

A catalogue of slide layouts, merged from mbb-deck-plugin (9 patterns, well-specified),
likaku (72-entry layout catalogue), kgraph57 (renderer patterns), and BCG's graphics section.

**Choosing rule:** pick the archetype that fits the *action title*, never the one that fits the
data shape. The title states the claim; the archetype is the apparatus for proving it.

---

## Tier 1 — the ones that carry most decks

### A. Executive summary
**The most important slide in the deck.** The entire deck on one page.

```
Action title  = the governing thought
Body          = 3–5 sub-points, each one sentence, each corresponding to a
                major section of the deck  (these ARE the Key Line)
No chart, no decoration
```
> "If the audience reads only one slide, this is the one." — mbb-deck

Placement is contested — see `05-conventions/contested-points.md`.

### B. Single-chart slide
Action title on top; one chart as the body; takeaway labelled **directly on the chart**, never
via a legend the reader must cross-reference.

Must satisfy the McCandless five-step read (see §Tier 4 below).

### C. Bullet-supported insight slide
Action title; 3–4 supporting bullets, parallel in structure, each expanding one piece of the
title's claim.

**Bullet rules:** same part of speech across bullets; complete thoughts, not fragments; groups
of ≥2; 3–5 max; one idea per bullet, ≤2 lines; no nested sub-bullets (one level if unavoidable).
No clotheslines.

### D. Comparison table
Options as **columns**, criteria as **rows**. Cells hold ratings (High/Med/Low, Harvey balls,
check/cross).
- The recommended option is highlighted (bold border, accent, or a "Recommended" badge)
- Criteria listed **in order of importance**
- **Don't include a criterion if all options score the same on it**

The natural body for a *To B or Not to B* storyline.

### E. 2×2 matrix
- Label **both axes** with what increases in each direction
- Label quadrants, or leave blank if the items tell the story
- Items as dots, logos, or short labels
- Action title states the conclusion the matrix supports, e.g. *"Three of our five products fall
  in the low-growth, low-margin quadrant"*

### F. MECE bucket list
3–5 boxes representing the breakdown. Each: category name, short description, key metric or
finding. Often the slide right after the executive summary — it introduces the framework that
organizes the rest.

### G. Value chain / horizontal flow
Steps left-to-right with arrows or chevrons; short label plus one-line description below each.
Process, customer journey, or sequential framework.

### H. Roadmap / Gantt
Phases as columns or rows with milestones, owners, dates.
- 2–4 phases (Now / Next / Later, or quarters)
- 2–4 milestones per phase max
- Mark dependencies
- Owner or function on each milestone
- BCG: *"Keep the Gantt chart clear of unnecessary gridlines"*

### I. Quote slide
One direct quote, large, centred; attribution below in smaller text. **Use sparingly — at most
one or two per deck.** Dave McKinsey tip 53: use real quotes you obtained directly.

kgraph57's spec: one oversized opening quotation mark, tinted; **never a matching closing
mark**; quote text ≤4 lines; attribution prefixed with an em-dash.

---

## Tier 2 — structure and navigation

| Pattern | Notes |
|---|---|
| **Cover / title slide** | Deck title, client/department, sub-headline, date, team, internal-vs-external positioning. No page number, no source line. |
| **Agenda / table of contents** | ≤5 short items (Dave McKinsey tip 12). Titles deliberately visually ignorable (tip 11). Start items with **action verbs** to signal mental mode (tip 14). Apply contrast to highlight the current section (tip 15). kgraph57: 1–8 rows on hairlines; >6 splits into two columns; >8 is a spec error, not smaller rows. |
| **Section divider** | Section name plus a one-line promise of the section. kgraph57's navy chromeless family: small-caps `SECTION 02` kicker, large serif title, optional section rail showing progress. **House rule:** the divider's one-line promise IS the section's Key Line sentence, verbatim; the short section name is only the label. The ladder test reads the Key Line sentence, so "Key Line points = section titles" and the divider archetype stop conflicting. |
| **Appendix separator** | Back-matter boundary. |
| **Closing / key takeaways / next steps** | kgraph57: two columns — `KEY TAKEAWAYS` (1–4 numbered) and `NEXT STEPS` (action + "Owner · Timing"). |
| **End cover** | Mirrors the cover; contact lines. |

### Navigation aids for decks >10 slides (mbb-deck)
- **Structure pages** — introduce a framework before a section so upcoming pages have a home
- **Tracking elements** — repeat the framework marker on each following page
- **Chapter trackers** — small section labels in a slide corner
- **Double-click logic** — a detail page is structured as a virtual double-click into an element
  of the prior page
- **Leading references** — start action titles with words introduced on the structure page, so
  slides visibly attach to the framework

Stanley & Castles agree: *"in a presentation pack you can include 'tracker' pages so the
audience knows where they are up to, and possibly mini versions of the tracker image in the top
right corner of each page in longer packs."*

---

## Tier 3 — the fuller catalogue (likaku's 72 layouts, condensed)

Useful as a *menu* when you know the message but not the form.

**Data & statistics:** Big Number / Factoid · Two-Stat Comparison · Three-Stat Dashboard · Data
Table · Metric Cards Row · Traffic Light / RAG · Scorecard

**Frameworks & matrices:** 2×2 Matrix · Staircase Evolution · Process Chevron (3–5 steps) ·
Venn Diagram · Temple / House Framework (roof-pillar-foundation)

**Comparison & evaluation:** Side-by-Side · Before / After · Pros and Cons · Traffic Light Status

**Content & narrative:** Executive Summary · Key Takeaway with Detail · Quote / Insight ·
Two-Column Text · Four-Column Overview

**Timeline & process:** Timeline / Roadmap · Vertical Steps · Cycle / Loop (PDCA) · Funnel

**Charts:** Grouped Bar · Stacked Bar · Horizontal Bar · ~~Donut~~ · Waterfall · Line / Trend ·
Pareto · Progress Bars / KPI Tracker · Bubble / Scatter · Risk / Heat Matrix · Gauge · Harvey
Ball Status Table · Stacked Area · ~~Pie~~

*(Pie and Donut struck — banned by house decision #3. Share-of-whole renders as a sorted bar or
stacked column.)*

**Dashboards:** KPIs + Chart + Takeaways · Table + Chart + Factoids

**Storytelling & special:** Stakeholder Map (influence × interest) · Issue / Decision Tree ·
Checklist / Status · Metric Comparison Row with delta badges · Icon Grid · SWOT · Value Chain ·
Numbered List with Side Panel · Table + Insight Panel · Multi-Bar Panel Chart · Meet the Team ·
Case Study (SAR) · Action Items · Closing

*Note: likaku retired its "Three-Pillar Framework" layout in favour of "Table + Insight Panel" —
a small signal that generic framework boxes tend to lose to structured tables.*

---

## Tier 4 — the chart-slide build method

### The McCandless Method (mbb-deck)
Any data slide must support five questions **in order**. If it can't answer them by itself, it
isn't done.

1. **What is this chart?** A title or label so the viewer can name it. ("FY24 revenue by region.")
2. **What are the obvious questions?** Axes labelled, units stated, time period given, sample
   size or scope noted.
3. **What is the insight?** The action title states it. *The chart is evidence; the title is the
   claim.*
4. **Which data points prove it?** Highlighted — accent on the bars/lines that matter, neutral
   grey on the rest. **Don't make the audience hunt.**
5. **What's the takeaway, and what comes next?** The slide ends in a position the next slide's
   action title naturally picks up.

> "This is both a build rule and a presentation rule. A slide built this way can be talked
> through live without notes; a slide built badly cannot be rescued by a good presenter."

### Build order (mbb-deck) — never start with the visual
1. **Message** — the one message, written as the action title. *If the message is not clear, the
   slide is not ready to be built.*
2. **Layout** — pick the archetype; think rows and columns.
3. **Main visual** — chart type from the *message's comparison type*, not the data shape.
4. **Supporting text** — parallel grammar, groups of ≥2, max 5 per box.
5. **Polish** — alignment, consistency, no jitter.

---

## Useful slide elements (BCG + mbb-deck)

| Element | Use |
|---|---|
| **Callouts / bubbles** | Remarks on specific chart elements. BCG: circle callouts when there are several points to mark; square callouts for blocks. |
| **Buttons** | Visually relate two ideas. BCG: *"Buttons should not be used as bullets."* Directional buttons for flow. |
| **Lollipops** | Differentiate information similarly to a callout. |
| **Takeaway boxes** | The slide's overall conclusion. |
| **Harvey balls** | Multi-criteria qualitative evaluation in a table. |
| **Status stickers** | PRELIMINARY / INDICATIVE / FOR DISCUSSION / ILLUSTRATIVE whenever numbers aren't final. |
| **Leader lines** | Only when necessary, and **drawn manually** — never PowerPoint's defaults, which arrange at random and add noise. |

---

## Choosing an archetype from the action title

| If the title claims… | Reach for |
|---|---|
| One number is the whole story | Big Number / Factoid |
| X is bigger/smaller than Y | Horizontal bar, sorted |
| X changed over time | Line (many points) or column (few) |
| We got from A to B because of… | **Waterfall** |
| X is __% of the whole | Stacked column or sorted bar |
| Option B is best | Comparison table (criteria × options) |
| These three things must happen | MECE bucket list, or numbered list with side panel |
| This is where each item sits on two dimensions | 2×2 matrix or scatter |
| Here's the sequence | Process chevron, value chain, or timeline |
| Here's the status of N workstreams | Traffic light / RAG table |
| Someone said something that matters | Quote slide |
| Here's how the whole argument hangs together | Executive summary |

## Cross-references
- Chart form selection in depth → `04-data-visualization/zelazny-chart-selection.md`
- Type, colour, spacing → `03-slide-design/mbb-slide-standards.md`
- Where each archetype sits in the deck → `03-slide-design/deck-architecture.md`
