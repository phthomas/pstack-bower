# Chart Craft and Decluttering

Once the form is chosen (see `zelazny-chart-selection.md`), this is how the chart gets built.
Sources: BCG Format Guide (Charts, Tables, Diagrams sections); Cole Nussbaumer Knaflic,
*Storytelling with Data*; mbb-deck; kgraph57; pstack-loki.

---

## 1. Anatomy of a chart — BCG's element list

> "No matter from where the chart originates, it should follow these guidelines:
> - Data generate all work to allow for easy updates
> - Clearly label everything in the datasheet
> - Remove all data not related to the chart from the datasheet
> - **Include a data source in the footnote**
> - Refrain from outlining or shading the chart area unless absolutely necessary
> - Include a legend if different colors are used or if data is not labeled in the body"

And the governing tip:
> "**Remove any chart element that does not improve visual translation.** This includes
> gridlines, plot area boundaries, tick marks, and axis lines. Conversely, if the chart needs
> these elements to be more easily understood, include them."

That last clause matters — decluttering is not stripping. Knaflic agrees: *"reducing clutter
doesn't mean the removal of everything but one key point."*

---

## 2. Structural elements

### Axes
- Most charts need an **x-axis line**; a y-axis often isn't necessary.
- **Key Message Slides: default to no y-axis** — add one only if it gives needed context.
- **Detail Slides: default to including a y-axis** — remove if not needed.
- Reverse both defaults for horizontal bar charts.
- Axis line weight: **0.75pt**.
- Axis titles aligned to the outside boundaries of the chart.
- Keep x-axis unit labels **horizontal**. If space is tight, use fewer labels — never shrink
  below the minimum font size.
- Keep axis unit labels **separate from axis titles**.
- The percent sign goes in the axis unit label **in parentheses**, never as part of a number
  scale.
- When a y-axis is included, use **as few units as required**. A chart with data labels may only
  need the lowest, mid-point and highest values.

### Gridlines
- **0.75pt**, light.
- **No minor gridlines** except on a very wide chart or where genuinely required.
- **No gridlines on a dense line chart.**
- Include a minimum of major gridlines if no data points are labelled, or if the chart is very
  wide.
- *"If it is important to understand every data point value, consider using labels instead of
  gridlines."*
- Knaflic: if you keep them, make them **thin and light grey** — *"do not let them compete
  visually with your data."*

### Tick marks
- **Avoid them.** If required, use them only to denote **major** units.
- *"Sometimes the visual relationships (e.g., the shape of the graph) tell the story, and the
  unit-axis can be greatly simplified or removed to reduce chart clutter."*
- Adjust the interval of tick-mark labels to reduce noise — include only what's needed to
  understand the scale.

### Data labels
- Format numbers and decimal points **consistently** across the slide and the deck. *"If a tenth
  of a point is used, use it consistently across the data set."*
- Place labels **over the chart fills** or next to their graphical place.
- **Never backfill a data label.** If it isn't clearly connected to its element, make the chart
  larger, don't add a white box behind the text.
- **No default leader lines** — *"these tend to look messy and haphazard."* Draw them manually
  when needed.
- Use labels **strategically** — too many and they become unreadable. *"If they don't offer
  context, avoid them."*
- Labels can replace a y-axis or a legend entirely to reduce clutter.

### Legends
- **Direct labels beat legends, always.** Never force the reader to cross-reference.
- If used, keep them consistently styled and positioned **per chart type** (not per individual
  chart).
- **Orient and order the legend the same way the data series are oriented** (Dave McKinsey tip
  62; BCG's "read left to right, the same as the chart categories").
- *"Keep in mind how far the eye needs to travel to visually link the legend and its associated
  data. This distance can make comparisons challenging."*
- kgraph57: direct labels on the first instance replace legend swatches.

---

## 3. Colour in charts

BCG's rule, again:
> "**Always start a chart with gray monochrome. Use bright green to highlight as necessary.**"

> "Colors guide the viewer's eye to the main point in your charts."

Universal across sources:
- **The message carrier gets the accent; everything else goes grey.**
- kgraph57: *"Use blue for the main argument and grey for context. Use red only for negative
  variance, risk, or loss."*
- mbb-deck: *"If a bar is in the accent color, it's the one the audience should look at. Don't
  color things just because."*
- Signed data (variance, YoY, deviation) in heatmaps uses a **diverging ramp anchored at zero**,
  never a single-hue ramp.
- BCG's semantic assignments: **magenta / cranberry = negative**; green = positive and highlight;
  yellow only over green, minimum 18pt.

BCG on gray secondary labels: *"The gray data labels are secondary — included to give specific
context to the green data labels' meaning."* Grey isn't just "not important"; it's *context for*
the highlighted thing.

---

## 4. Reducing visual noise — BCG

> "Showing everything on the chart just to 'cover all the bases' can be detrimental to the
> chart's core message. Conversely, reducing clutter doesn't mean the removal of everything but
> one key point. Instead, **remove anything that isn't required for validity and quantification**
> of the chart."

- Keep the area around the chart free of embellishment.
- **No photography on or near a chart.**
- No bevels, shadows, or other graphic emphasis.
- Icons, bugs and logos may accompany a chart for at-a-glance clarity, but *"their size and
  quantity should not be the most noticeable graphic on the slide; **let the data speak,
  first**."*
- **No gratuitous logos or icons** in the chart area.

### The glance test
> "Your audience should understand your charts at-a-glance. Consider different charts and tables
> when deciding the best way to communicate your data's main point. **Which will help your
> audience understand your main point at a single glance?**"

> "Make sure your data is visually accurate and honest. **Don't use effects to mislead your
> audience.** Always provide data source references."

### Essential vs supporting data
BCG makes this a Key Message / Detail decision, not a taste call:
> "When projecting a chart in a presentation, it is best to **remove all but the most essential
> information** required to convey a key idea. Charts should support — not distract — the
> audience."
>
> "More chart details may be necessary to add support to a key idea. Such charts belong as
> **Detail Slides**, which are ideal for higher density information that the reader can digest
> apart from in-person interaction."

**The same chart legitimately exists in two versions.** Build the dense one for the appendix and
the distilled one for the projection.

---

## 5. Knaflic — the Gestalt principles

Six principles that explain *why* an element is or isn't clutter. Each is a lever, not just a
description.

| Principle | Statement | Chart application |
|---|---|---|
| **Proximity** | Objects physically close together are perceived as a group | Table row/column spacing alone directs the eye down columns or across rows — no borders needed |
| **Similarity** | Objects of similar colour, shape, size or orientation are perceived as related | Colour similarity makes the eye read across rows, eliminating the need for borders |
| **Enclosure** | Objects physically enclosed together are perceived as a group; *"it doesn't take a very strong enclosure — light background shading is often enough"* | Shade the forecast region to separate it from actuals |
| **Closure** | People perceive individual elements as a single recognizable shape; the eye fills gaps | **Chart borders and background shading are unnecessary** — remove them and the graph still reads as a cohesive whole, and the data stands out more |
| **Continuity** | The eye seeks the smoothest path and creates continuity where none is drawn | The y-axis line can be removed; the aligned bar starts imply it |
| **Connection** | Physically connected objects are perceived as a group | A line connecting points groups them more strongly than colour does |

> "There is a simple reason we should aim to reduce clutter: because it [adds cognitive load]."

---

## 6. Knaflic — decluttering, step by step

Her six-step worked example (an IT ticket-volume chart):

1. **Remove chart border.** *"Chart borders are usually unnecessary… Instead, think about using
   white space to differentiate the visual from other elements on the page."*
2. **Remove gridlines.** *"When you can, get rid of them altogether: this allows for greater
   contrast, and your data will stand out more."*
3. **Remove data markers.** *"Use them on purpose and with a purpose, rather than because their
   inclusion is your graphing application's default."*
4. **Clean up axis labels.** Kill trailing zeros — *"they carry no informative value, and yet
   make the numbers look more complicated than they are."* Abbreviate months so they fit
   horizontally, eliminating diagonal text.
5. **Label data directly.** Removes the back-and-forth to the legend.
6. **Leverage consistent colour** between the data and its label.

The general rule underneath: **every single element adds cognitive load.** Defaults are not
decisions.

### Preattentive attributes
Knaflic's ch.4. Attributes the visual system processes *before* conscious attention — size,
colour, position on page, intensity, enclosure, orientation. Her demonstration: counting the 3s
in a block of digits is slow; the same block with the 3s in a different colour is instant.

Consequence: **you get to choose where the reader looks first, and you exercise that choice
whether or not you know it.** If nothing is emphasized, the eye lands somewhere arbitrary.

---

## 7. Charting rules, consolidated

### Banned outright (across sources)
- 3D
- Gradient fills
- Drop shadows / bevels
- Chart backgrounds and plot-area shading
- Rainbow palettes
- Dual y-axes *(Dave McKinsey tip 64: "Stick to one set of axes per graph")*
- Undisclosed axis truncation
- Smoothing that hides reversals
- **Screenshots of charts** — mbb-deck: *"rebuild natively: screenshots can't highlight your
  message, clash with the document's look, and bring resolution problems"*
- Distorted proportions *(tip 66: "Do not distort graphs")*

### Constraints
| Rule | Source |
|---|---|
| Max 4 series on a line chart; max 5 on a stacked bar | mbb-deck |
| Y-axis usually starts at zero; disclose any truncation on the axis | mbb-deck, kgraph57 |
| Mark the zero baseline with an explicit "0" tick so the reader can verify it | kgraph57 |
| Floating bars (waterfall middles) carry explicit value labels | kgraph57 |
| Lie Factor ≈ 1.0 — visual proportions match data proportions within 5% | kgraph57 |
| Sort the data (largest first) — sorting is part of the craft | mbb-deck |
| Anchor time series with CAGR labels to state the growth story | mbb-deck |
| Use a more subtle treatment for forecast data | Dave McKinsey tip 59 |
| Maintain design consistency across similar graphs in a presentation | tip 65 |
| For a series of charts on sequential slides, keep the axis aligned | BCG |
| Truncated text shows an ellipsis and keeps the full string accessible; nothing is cut silently | kgraph57 |
| Bars, cards and boxes are **flat fill, never fill-plus-border** | kgraph57 |
| Chart annotations explain critical inflections | Dave McKinsey tip 57 |
| Footnote sources, critical assumptions, and details too granular for the body | tip 60 |
| Disclose n= / sample basis for surveys or subsets | pstack-loki |
| Label the time basis (YoY/QoQ/YTD; fiscal vs calendar) | pstack-loki |
| Axis labels carry **units** — never ambiguous between IDR bn, USD mm, % | pstack-loki |

### The pie-chart question — genuinely contested
| Source | Position |
|---|---|
| Zelazny | Pie is the *right* form for a component comparison, but should be ~5% of charts |
| Dave McKinsey (tip 67) | Acceptable for composition snapshots of up to five categories; consider treemaps (68); rely on bar charts for composition (69) |
| BCG | Includes doughnut charts as useful for highlighting; no ban |
| likaku | Pie is layout #64 in the catalogue — permitted |
| **mbb-deck** | **Banned outright**, no exceptions, enforced by two linters |
| pstack-loki | Pie only if ≤3 slices and you can defend it |

See `05-conventions/contested-points.md`. The defensible synthesis: pie is legitimate for a
genuine component message with few slices, and is over-used everywhere; a sorted bar or stacked
column is nearly always at least as good. A hard ban is a *policy*, not a finding.

---

## 8. Tables

BCG's table section:

- **Alignment.** *"Horizontally align column headers the same as the [data]."* Universal rule
  from mbb-deck: **numbers right-aligned, text left-aligned — always.**
- **Whitespace within and around** the table does the organizing work.
- **Gridlines sparingly.** Add vertical gridlines only when the whitespace between columns
  isn't enough.
- **Avoid shading.** *"Shading can easily affect contrast and [readability]."* When shading is
  required, use the four designated table colours: **table gray** (highlight, neutral), **table
  yellow** (highlight, neutral), **table green** (positive), **table red/magenta** (negative).
- **Strategically define visual flow.**
- Column headers short — one or two words.
- Highlight the one cell or row that carries the message.
- kgraph57: hairline rules only; no boxes.

**Candy striping** is called out by BCG as a technique for filling text boxes in tables — apply
it deliberately, not by default.

---

## 9. Diagrams

BCG:
> "Diagrams should match your content needs while still [following the guidelines]. Diagrams
> should be simple and appropriately colored. Diagram text can be placed over the diagram
> [where legible]. **Refrain from color coding content to match** [across unrelated elements]."

Zelazny's concept/metaphor guidance applies here — see
`04-data-visualization/zelazny-chart-selection.md` §Non-quantitative messages.

---

## 10. The exhibit checklist

A mergeable checklist for a review gate, drawn from pstack-loki's element list and cross-checked
against BCG, Knaflic and mbb-deck. Each line is assertable against a rendered chart:

- [ ] Chart form matches the message's comparison type
- [ ] Kicker or chart label states what the reader is looking at
- [ ] Axis labels carry **units** (IDR bn vs USD mm vs % — never ambiguous)
- [ ] Time basis labelled (YoY / QoQ / YTD; fiscal vs calendar)
- [ ] Source line, bottom-left, ~9pt: `Source: <origin>, as of <date>`
- [ ] Annotation on the key datum stating the so-what (≤8 words)
- [ ] Emphasis: message-carrier in accent; **all other series muted grey**
- [ ] Reference line present if the claim is vs. a benchmark, target or peer
- [ ] Direct series labels (legend only if direct labelling is impossible)
- [ ] n= / sample basis disclosed if survey or subset
- [ ] Axis starts at zero for bars; any truncation disclosed on the axis
- [ ] Zero baseline explicitly ticked
- [ ] Data sorted (largest first) unless the order carries meaning
- [ ] Number formats consistent within the chart and across the deck
- [ ] No border, no background shading, no gridline competing with the data
- [ ] Nothing from the banned list present
- [ ] Passes the glance test and the squint test
- [ ] Every number traces to a source cell

### The neutrality test
pstack-loki adds a check worth keeping: after building the chart, ask whether a reader who
disagreed with your conclusion would call the chart fair. Scale choice, baseline, series
inclusion and colour are all places where advocacy can quietly become distortion. Zelazny's
scaling section is the same warning from the other direction.

## Cross-references
- Which chart form → `04-data-visualization/zelazny-chart-selection.md`
- Colour tokens and type floors → `03-slide-design/mbb-slide-standards.md`
- Full QA rubrics → `05-conventions/quality-rubrics-and-checklists.md`
