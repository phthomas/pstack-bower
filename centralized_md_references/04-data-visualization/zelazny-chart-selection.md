# Chart Selection — The Zelazny Method

Source: Gene Zelazny, *The Say It With Charts Complete Toolkit* (2006). Zelazny was McKinsey's
Director of Visual Communications; this is the canonical MBB chart-choice framework and every
other source in the corpus cites or paraphrases it.

---

## The three steps

```
   DATA  ──[A]──►  MESSAGE  ──[B]──►  COMPARISON  ──[C]──►  CHART FORM
```

> "Choosing a chart form without a message in mind is like trying to color coordinate your
> wardrobe while blindfolded."

> "**It is not the data** — be they dollars, percentages, liters, yen — **that determine the
> chart. It is not the measure** — be it profits, return on investment, compensation —
> **that determines the chart. Rather, it is your message,** what you want to show, the specific
> point you want to make."

This is the whole method. Skipping step A and choosing from the data shape is the single most
common charting error, and it is why so many decks contain technically correct charts that prove
nothing.

---

## Step A — Determine your message

The same data supports many messages. Zelazny's demonstration with one table of sales by region
for two companies — six different charts, six different claims:

| Chart choice | Message it makes |
|---|---|
| Two pies / two 100% columns | The **mix** of sales is different for Companies A and B |
| Two bar sets, source order | The percentage of sales for both companies **varies by region** |
| Bars ranked descending | Company A is **highest in the South**; Company B is highest in the North |
| Bars mirrored around regions | Company A's share is **highest in the South where B's is weakest** |
| Bars grouped on a common base | In the South, A **leads B by a wide margin**; East and West competitive; North A lags |

And on a single sales table, three legitimate messages depending on which aspect you highlight:
- Reading down the time column → *"Sales have risen steadily since January."*
- Reading across May → *"In May, sales of Product A exceeded those of B and C by a wide margin."*
- Reading May as shares → *"In May, Product A accounted for the largest share of total company sales."*

> "The decision to emphasize ranking or share is up to you, and that decision will give you your
> message."

**Then make the message the title.** See `02-action-titles/action-title-craft.md` §1 — Zelazny's
"message title vs topic title" argument is one of the four root causes of bland titles.

---

## Step B — Identify the comparison

**Every message implies exactly one of five comparisons.** Zelazny gives trigger words for each.

| # | Comparison | Definition | Trigger words |
|---|---|---|---|
| 1 | **Component** | Size of each part as a percentage of the total | *share, percentage of total, accounted for X percent* |
| 2 | **Item** | How things rank — same, more, less | *larger than, smaller than, equal, exceeds, ranks* |
| 3 | **Time series** | How things change over time | *change, grow, rise, decline, increase, decrease, fluctuate* |
| 4 | **Frequency distribution** | How many items fall into progressive numerical ranges | *x to y range, concentration, frequency, distribution* |
| 5 | **Correlation** | Whether two variables follow the pattern you'd expect | *related to, increases with, decreases with, varies with,* and negations |

Stated compactly:
- **Component:** percentage of a total
- **Item:** ranking of items
- **Time series:** changes over time
- **Frequency distribution:** items within ranges
- **Correlation:** relationship between variables

### Dual comparisons
Some messages imply two. *"Sales are forecast to increase over the next 10 years, but profits
may not keep pace"* is time series (primary) **and** item (secondary).

> "You must determine which comparison is **primary** and which is secondary… the primary
> emphasis remains on changes over time, and we would therefore use the basic chart form most
> appropriate to a time series comparison."

Rule: **the primary comparison picks the chart form; the secondary is expressed within it** (in
this case, a line chart with a separate line per item).

---

## Step C — Select the chart form

Five basic quantitative forms: **pie, bar, column, line, dot.**

### The matrix

| Comparison | Primary form | When |
|---|---|---|
| **Component** | **Pie** | The only job a pie does — *"a circle gives such a clear impression of being a total"* |
| **Item** | **Bar** (horizontal) | Ranking; long category labels |
| **Time series** | **Column** | Few data points (say 6–7) |
| **Time series** | **Line** | Many data points |
| **Frequency distribution** | **Column** | Few ranges |
| **Frequency distribution** | **Line** | Many ranges |
| **Correlation** | **Bar** (paired/deviation) | Few data points |
| **Correlation** | **Dot** (scatter) | Many data points |

The two-choice rows resolve on **data volume**, not on preference.

> **House policy override (decision #3, 2026-08-23): pie and doughnut charts are banned in
> pstack-bower.** Zelazny's row is kept above for source fidelity, but a component message
> renders as a **sorted bar or stacked column**. When a pie is requested, say the ban is house
> policy and note the sources are not unanimous — see `05-conventions/contested-points.md` §3.
> Any skill-facing distillate of this matrix must carry the resolved row, not Zelazny's.

### Zelazny's usage budget
His own estimate of a healthy chart mix:

| Form | Share | His comment |
|---|---|---|
| Pie | **~5%** | *"the most popular. It shouldn't be; it's the least practical"* |
| Bar | **~25%** | *"the least appreciated… the most versatile"* |
| Column + Line | **~50%** | *"good old reliable"* and *"the workhorse"* |
| Dot | **~10%** | *"possibly intimidating at first glance… has its place"* |
| Combinations | ~10% | Line-with-column, pie-with-bar, etc. |

If a deck's chart mix is 40% pie and 5% bar, that's diagnostic on its own.

### Scaling — the honesty section

> "**A chart is a picture of relationships, and only the picture counts.** Everything else —
> titles, labels, scale values — merely identifies and explains. The most important feature of
> the picture is the impression you receive. **Scaling has an important controlling effect on
> that impression.**"

Zelazny's four-fault example (a chart making rising profits look like falling profits):
1. Years shown in reverse — most recent at left
2. The bottom 20 units of profit lopped off
3. Columns in three dimensions — measure from the front or the rear?
4. Scale lines drawn in perspective

The two factors that control the picture:
- **The shape of the chart** — short-and-wide through tall-and-narrow
- **The scale range** — 0 to 5, 0 to 10, 0 to 25

And the judgement call, which cannot be automated:
> "A $1,000 change in a multimillion contract may be insignificant while a one-cent change in
> the price of a floor tile may be [significant]. You would therefore select a scale to reflect
> your understanding of the importance of the changes."

Zelazny's test for your own charts: **omit the scale values and see whether the message still
comes across.** If the picture alone doesn't say it, the chart form or the scaling is wrong.

---

## Extending the matrix

Zelazny's five forms predate several now-standard consulting charts. The corpus's combined
extension:

| Message says… | Comparison | Form |
|---|---|---|
| "We got from A to B because of…" | Bridge / decomposition | **Waterfall** |
| "Market splits by segment × share" | Two-dimensional composition | **Marimekko** |
| "Rank shifted between two points" | Rank change | **Slope / dumbbell** |
| "Same pattern across many groups" | Multiples | **Small multiples**, shared axes |
| "This is 80/20" | Concentration | **Pareto** (bars + cumulative line) |
| Qualitative comparison | Judgement | **Harvey balls / 2×2** |
| Two variables plus magnitude | Correlation + size | **Bubble** |
| Risk assessment | Two-dimensional judgement | **Heat matrix** |
| Flow between states | Allocation | **Sankey-style** |

**On the waterfall specifically** (mbb-deck): *"Reach for a waterfall whenever the message is
'how did this number change' or 'which drivers compose it'… It is the workhorse chart of
professional services; when in doubt between a waterfall and a plain bar for a change-or-drivers
message, take the waterfall."*

The real McKinsey USPS deck uses exactly this: the title *"Losses have been driven by volume
declines, RHB pre-funding requirements, and limitations on cost savings"* is proved by a
waterfall decomposing the net-income decline from 2006 to 2009.

### When a chart is the wrong answer entirely
pstack-loki's rule, consistent with Zelazny's minimalism: *"When numbers beat charts: fewer than
~5 values the audience must **read**, not compare → big-number layout or a clean table. A chart
of three numbers is decoration wearing a lab coat."*

mbb-deck's table rule: *"Use a data table **only when the audience needs to look up specific
values**; if the point is a trend or comparison, use a chart."*

---

## Non-quantitative messages — concepts and metaphors

Zelazny's Section III addresses what the five forms can't: *"images for ideas such as
interaction, leverage, obstacles, and interrelationships, as well as images that convey
structure, sequence, and process."*

Two families:
- **Concept visuals** — abstract geometric shapes: arrows, circles, triangles
- **Visual metaphors** — everyday objects: puzzles, mazes, ladders

His framing is worth keeping: they are **"solutions in search of a problem."**

> "In isolation, none is right or wrong, good or bad. **The appropriateness of any visual
> depends on its fit with the message that you're trying to visualize** — and that's for you to
> determine."

Method:
1. Browse the portfolio as **thought starters** — look at images from different orientations.
2. Simplify, expand, multiply, or otherwise modify them.
3. **Once you've selected a diagram, add the words** — around or inside it — that bring your
   message home.
4. **Don't settle for the first idea that grabs you.** His worked example shows *nine* different
   diagrams for the same five-step project-phase list.
5. **Test the visual with colleagues** — *"like other visual images, these diagrams will have
   different meanings for different people."*

Point 4 is the one that matters for an agent: the first plausible diagram is rarely the best
fit, and the discipline is to generate several and choose.

---

## The full selection procedure

1. State the message as a **complete sentence** — this is the action title or the exhibit's
   message line.
2. Find the **trigger words**. Which of the five comparisons?
3. If two, decide **which is primary**.
4. Read off the **chart form** from the matrix (data volume resolves the two-choice rows).
5. Check the extension table for a modern form that fits better (waterfall, slope, marimekko…).
6. Check whether a **number or table** beats a chart here.
7. Choose **scale and shape** to reflect your honest understanding of how significant the
   changes are.
8. **Omit the scale values and check the message still reads.**
9. Put the message in the title. *(For where — see the chart-title question in
   `05-conventions/contested-points.md`.)*

## Cross-references
- Cleaning up the chosen chart → `04-data-visualization/chart-craft-and-decluttering.md`
- Turning the message into the title → `02-action-titles/action-title-craft.md`
- Slide layouts that host charts → `03-slide-design/slide-archetypes.md`
