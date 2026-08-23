# Chart Matrix and Exhibit Checklist — house-resolved

The **canonical copy** of the chart-selection matrix and the exhibit element checklist.
House policy is already applied (pie/doughnut banned, chart titles carry the so-what).

## Message → comparison → form

Never pick from the data shape. State the message, find the trigger words, read off the form.

| Comparison | The message says… | Trigger words | Form |
|---|---|---|---|
| **Component** | X is __% of the whole | share, percentage of total, accounted for | **Sorted bar or stacked column** (house: pie/doughnut banned) |
| **Item** | X ranks above/below Y | larger, smaller, equal, exceeds, ranks | Horizontal bar, sorted |
| **Time series** | X changed over time | grow, rise, decline, fluctuate | Column (≤6–7 points) · line (more) |
| **Frequency** | Items concentrate in ranges | x-to-y range, concentration, distribution | Column (few ranges) · line (many) |
| **Correlation** | X varies with Y (or fails to) | related to, increases with, varies with | Paired bar (few) · scatter (many) |

**Dual comparison:** the primary comparison picks the form; the secondary is expressed within
it (e.g., time-series-plus-item → one line per item).

## Extensions — the consulting workhorses

| Message | Form |
|---|---|
| We got from A to B because of… / which drivers compose it | **Waterfall** — when in doubt vs a plain bar for a change-or-drivers message, take the waterfall |
| Market splits by segment × share | Marimekko (`render: image` — not native; or re-form: often two messages anyway) |
| Rank shifted between two points | Slope / dumbbell |
| Same pattern across many groups | Small multiples, shared axes |
| This is 80/20 | Pareto (bars + cumulative line) |
| Two variables + magnitude | Bubble |
| Qualitative comparison | Harvey balls / 2×2 |
| Risk positioning | Heat matrix (diverging ramp anchored at zero for signed data) |

## When a chart is the wrong answer

- Fewer than ~5 values the audience must *read*, not compare → **big number or a clean table.**
  A chart of three numbers is decoration.
- The audience needs to look up specific values → table. Trend or comparison → chart.
- Non-quantitative idea (structure, sequence, interaction) → concept visual; generate several
  candidates and choose — never settle for the first diagram that fits.

## The exhibit spec — `exhibits/E##.spec.md`

```markdown
# E## — <slide S##>
action_title_verbatim: "<from slideplan — immutable within the storyline version>"
message: <the one sentence this exhibit proves>
chart_title: "<so-what for THIS exhibit — narrower than the action title;
              omit if word-for-word identical>"
form: <from the matrix> because <comparison type>
render: native | image        # native wherever PowerPoint has the type (house §8)
emphasis: <the one series/bar/point that carries the message>

## data
source: [D#] <origin, as-of, basis>     # every number needs a home: data/src cell or [D#]
file: data/E##.csv                       # the only numbers allowed on the slide
```

## The element checklist — QA asserts each line against the render

- [ ] Form matches the message's comparison type
- [ ] Chart title states the exhibit's so-what (or is deliberately omitted as a duplicate)
- [ ] Axis labels carry UNITS (IDR bn vs USD mm vs % — never ambiguous)
- [ ] Time basis labelled (YoY/QoQ/YTD; fiscal vs calendar)
- [ ] Source line bottom-left: "Source: <origin>, as of <date>"
- [ ] Grey monochrome base; **accent only on the message carrier** (BCG mechanics)
- [ ] Callout on the key datum where the message needs pointing (≤8 words)
- [ ] Reference line if the claim is vs. a benchmark/target/peer
- [ ] Direct labels; legend only if direct labelling is impossible; legend ordered like the data
- [ ] Leader lines manual, never defaults; labels never backfilled — enlarge the chart instead
- [ ] n= / sample basis disclosed for surveys or subsets
- [ ] Bars start at zero; any truncation disclosed on the axis; zero baseline ticked
- [ ] Data sorted (largest first) unless order carries meaning
- [ ] Number formats and decimals consistent within chart and across deck
- [ ] No border, no plot-area shading, no gridline competing with the data

## Banned (linted)

Pie · doughnut · 3D · gradients · shadows · dual y-axes · rainbow palettes · undisclosed
truncation · smoothing that hides reversals · screenshots of charts (rebuild natively) ·
photography on or near a chart.

**When a pie is requested:** say the ban is house policy (decision #3), note the sources are
not unanimous (Zelazny and BCG permit them), and build the sorted bar / stacked column.

## Integrity

One message per exhibit — two messages = two exhibits, or the ladder needs a split: **route
upstream, don't cram.** The neutrality test before shipping a spec: would someone who disagrees
with the conclusion call this chart fair (scale, baseline, series inclusion, colour)? Honest
scaling: the picture is the argument — chart shape and scale range reflect your honest view of
the change's significance; check the message still reads with scale values covered.
