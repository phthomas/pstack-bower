# MBB Slide Design Standards

Primary source: **BCG PowerPoint Format Guide v2.3 (14 Sept 2018)** — 202 pages of an actual
MBB firm's internal standard, and the only first-party design doctrine in the corpus.
Supplemented by likaku (McKinsey-styled `python-pptx` engine), kgraph57 (token system), and
mbb-deck-plugin.

---

## 1. The single most important distinction: Key Message vs Detail Slides

No prior-art skill in the survey captures this, and it explains most confusion about whether
"MBB style" means sparse or dense. **It means both, deliberately, for different jobs.**

BCG's framing:

> "Until now, we've been creating the same slides for many different outputs. The BCG Grid
> methodology is to reconsider the content for each output and design it appropriately."

PowerPoint is used for three distinct jobs: an internal problem-solving tool, a client
deliverable/report, and a projected presentation. One density does not serve all three.

| | **Key Message Slide** | **Detail Slide** |
|---|---|---|
| **Purpose** | Visual aid — glanced at, not studied | Read on paper or a device |
| **Projected?** | Yes — this is the only type that should go on a projector | **No** |
| **Density** | Minimal text | Purposeful, carefully laid out, dense |
| **Background** | Gray | White |
| **Subtitle** | No | Yes |
| **Default body** | 20pt | 12pt |
| **Default heading** | 24pt | 16pt |
| **Absolute floor** | 14pt (chart/label/caption only); 16pt everything else | 8pt (secondary text only) |
| **Y-axis on charts** | Default to **no** y-axis; add if needed for context | Default to **including** a y-axis; remove if not needed |
| **Use for** | Live presentation | Deep-dive, backup, appendix, leave-behind, standalone |

> "The two slide styles can be mixed in one file, but **only the Key Message Slides should be
> presented on an overhead projector.**"

The reasoning is cognitive, not aesthetic:

> "The audible narration of a presentation competes for mental processing with visual reading
> of material, and thus reduces comprehension of the material if the audience is presented with
> dense slides."
>
> "People can't read while listening and can't listen while reading. Too much information on a
> single slide divides their attention."

**Implication for a deck-building toolkit:** density is a *parameter set by the delivery mode*,
not a house style. Ask "projected, or read?" before choosing type sizes. mbb-deck's `dense`
profile is the same idea under a different name.

---

## 2. Critical slide attributes — BCG's six

> "A great slide celebrates and showcases the insight from your analysis."

| Attribute | Definition |
|---|---|
| **Clear** | The reader understands the point you are trying to make |
| **Simple** | **One concept per slide.** Everything on the slide serves the main point — nothing is distracting |
| **Powerful** | Communicates insight — has an "a-ha"; clearly explains implications; **not just a data dump** |
| **Coherent** | Information uses transparent logic that makes obvious and consistent connections between data and conclusions |
| **Honest** | Content accurately and honestly reflects the facts |
| **Maintains perspective** | Subject matter focuses on your audience and what they need or want to know. **Great slide authors eliminate extraneous information the audience doesn't need** |

## 3. The five design principles

> "The most important design principles to achieve information clarity are: **Contrast,
> Whitespace, Hierarchy, Eye flow, Unity.**"

- **Contrast** — each group of content organized by a distinguishing treatment
- **Whitespace** — structure content to the base gridline so each column gets proper breathing
  room. *"Whitespace pushes attention to content, and creates proximity — content goes with
  content within the whitespace. This negates the need for 'boxing' and color coding."*
- **Hierarchy** — font size, font color, and organization create consistent visual hierarchy
- **Eye flow** — left to right for primary points, then top to bottom for secondary detail
- **Unity** — consistent brand colors and elements across the deck

### Focal points
> "Create slide focal points by making key messages or visuals the most dominant or centrally
> focused elements on your slide. Use whitespace — margins, gutters, and spaces between
> paragraphs — to visually set apart key ideas. When there is insufficient visual weight and
> lack of whitespace, ideas can be obscured."

### Conversion best practices (BCG's own checklist for fixing a bad slide)
- Remove unnecessary items
- **Break content into one message per slide**
- Create and preserve whitespace
- Create visuals or visual entry points
- Use brand elements consistently
- Highlight the story in the data

---

## 4. Typography

### BCG's type system

Font: **Trebuchet MS** — chosen because it's readable on screen and in print, available on old
and new Macs and PCs, and shares typographic characteristics with **Henderson**, BCG's actual
brand font. *(The pattern generalizes: firms substitute a widely-available face for their
licensed brand serif in distributable templates.)*

**Key Message Slide scale:**
| Size | Use |
|---|---|
| 24 | Default heading |
| 20 | Default body |
| 18 | Alternate body |
| 16 | Minimum secondary; default chart/label/caption |
| 14 | **Absolute minimum** — chart, label, caption only |
| 28 / 32 / 44 / 54 / 66 / 88 | Special text: key ideas, big statements, big data |

**Detail Slide scale:**
| Size | Use |
|---|---|
| 16 | Default heading |
| 12 | Default body |
| 10 | Minimum secondary; default chart/label/caption |
| 8 | **Absolute minimum** — secondary text only |
| 18–88 | Special text |

> "In all situations, make the font size as large as possible **to help limit word count**."

That clause is the point. The type floor is a *content* constraint disguised as a formatting
rule: if it doesn't fit at the minimum size, cut content — never shrink type.

Detail Slide minimums apply to 16:9, US Letter and A4. They do **not** apply to A3, 11×17 or
larger.

### Comparison across sources

| | BCG (Grid) | likaku (McKinsey-style) | kgraph57 | mbb-deck |
|---|---|---|---|---|
| Title font | Trebuchet, bold | **Georgia** (serif), bold, 22pt | Georgia, bold, 40px | Sans, bold, ~24pt |
| Body font | Trebuchet | Arial, 14pt | Helvetica Neue, 22px | Sans, 14–18pt |
| Footnote | — | 9pt | 13px | ~9pt |
| Cover title | — | 44pt | 54px | — |

**The serif-title convention.** likaku and kgraph57 both set titles in Georgia. kgraph57 is
explicit about why: *"distributable strategy-consulting templates substitute Georgia for their
licensed brand serifs, so Georgia is the accurate portable equivalent."* McKinsey's own brand
typeface is **Bower** — worth noting given this project's codename.

### Type ratios (kgraph57)
Sizes should form a *ratio*, not a grab-bag. Headline : body : chrome ≈ **4 : 1.6 : 1**.
- `T_HEADLINE / T_BODY` ≥ 1.7
- `T_BODY / T_CHROME` ≥ 1.6
- Deck span (cover title / chrome) ≈ 4.2

> "A change that breaks either ratio is wrong, whatever it does for a single slide in isolation."

Reading text has a **hard floor** so it survives projection and screen-share; chrome (sources,
footnotes, page numbers, classification) stays deliberately smallest — *never raise it to
"balance" a slide.*

---

## 5. Text emphasis — BCG's rules are unusually strict

> "**Size, color, and bold are the only approved emphasis styles.**"

| Treatment | Verdict |
|---|---|
| Sentence case | **Use everywhere** except the title slide layout |
| Bold | Only as a label or subheading; only at the beginning and/or end of a sentence or text block |
| Color | Only if it provides meaningful emphasis — a key data point or idea |
| Italics | **Never** |
| ALL CAPS | **Never** |
| Underline | **Only** for active hyperlinks — a functional component, not an emphasis style |

### The title rule, stated three times in the guide
> "**Never highlight words within titles or subtitles.**"
> "It is never permitted to emphasize text in the title or subtitle."
> "Never color highlight words in the title."

No bold, no colour, no italic, no underline, no caps inside an action title. Ever.

### Common mistakes BCG calls out as off-brand
- Any emphasis in the title or subtitle
- Bolding or emphasizing words *within* sentences, or sentences within text blocks
- Too much bold text
- Color highlighting on *every* bullet
- Color highlighting words within sentences
- Color coding on slides that also use highlighted text

> "If your message can be carried by gray text only, it does not need added emphasis."

### The emphasis strength ladder (kgraph57)
Where BCG says *what* is allowed, kgraph57 supplies a *rank order*. Memorize as **fill > line >
text**.

| Rung | Technique | Use for |
|---|---|---|
| 1 (strongest) | Solid fill, reversed text | The one box that states the conclusion |
| 2 | Tinted fill, accent text | A secondary highlighted block |
| 3 | Outline only | A called-out item that shouldn't dominate |
| 4 | Accent-colored text | Keywords and key numbers inline |
| 5 | Bold text | Sub-labels and minor headings |
| Baseline | Body | Everything else |

Discipline: **cap rungs 1–2 at one element per visual** (two only if the message genuinely has
two anchors). **Never stack rungs** — a solid fill already wins; adding coloured bold text on
top is noise. Keep each rung's meaning constant across the deck so the reader learns the code.

---

## 6. Color

### BCG's governing rule
> "**Start with gray and highlight with green.**"
>
> "Always start with medium gray as the 'base' color for fills and outlines. Use bright green
> as the highlight and emphasis on your slides."

> "Do not use many different colors on a slide. Practice restraint so your **message** stands
> out — not the colors."

> "**Do not use color-filled textboxes to visually organize content.** Instead, use whitespace,
> colored text, size, outlines, and dividing lines."

### BCG palette (RGB)
| Color | RGB | Role |
|---|---|---|
| Medium gray | 110, 111, 115 | **Base fill and outline**; primary chart fill |
| Bright green | 41, 186, 116 | **Primary highlight**; chart highlight fill; button fill; headings |
| Soft gray | 154, 154, 154 | Alternative light fill; secondary neutral; leader lines |
| Mint green | 62, 173, 146 | Secondary highlight; secondary chart fill (monochromatic) |
| True blue | 41, 94, 126 | Secondary highlight 2; secondary chart fill; tertiary outline |
| Secondary text gray | 127, 127, 127 | Chart structural elements; small text — labels, captions, footnotes, page numbers |
| Primary text gray | 87, 87, 87 | **Default body text** |
| Yellow | 212, 223, 51 | Highlight — **only over green**, minimum 18pt text |
| Jade green | 25, 122, 86 | Tertiary shape fill; secondary chart fill (monochromatic) |
| Cranberry | 103, 15, 49 | Secondary shape fill (**negative**); tertiary chart fill |
| Forest green | 3, 82, 45 | Tertiary shape/chart fill |
| Dark yellow | 168, 178, 28 | Secondary highlight 1 |
| Bright blue | 48, 193, 215 | Secondary |
| Magenta | 231, 28, 87 | **Negative connotation** |
| Midnight blue | 46, 53, 88 | Secondary |
| Background gray | 242, 242, 242 | Key Message Slide background |
| Table gray / yellow / green / red | 200,200,200 / 238,232,154 / 201,231,202 / 235,197,208 | Table shading: neutral / highlight / positive / negative |

**Note the semantic assignments:** magenta and cranberry carry negative meaning; green is
positive and is the highlight; yellow is restricted to highlighting *over* green and only at
18pt+. Colour is a code, not decoration.

### McKinsey-style palette (likaku)
| Name | Hex | Use |
|---|---|---|
| NAVY | `#051C2C` | Primary — titles, circles, section headers, TOC highlights |
| BLACK | `#000000` | Separator lines, title underlines |
| WHITE | `#FFFFFF` | Backgrounds, text on navy |
| DARK_GRAY | `#333333` | Body text |
| MED_GRAY | `#666666` | Secondary text, labels, source notes |
| LINE_GRAY | `#CCCCCC` | Table row separators |
| BG_GRAY | `#F2F2F2` | Background panels, takeaway areas |

Accent set, used **only when a slide has 3+ parallel items**: `#006BA6` blue, `#007A53` green,
`#D46A00` orange, `#C62828` red/warning. Card body text always stays DARK_GRAY.

likaku's design philosophy, verbatim: *"极简 — 无阴影、无3D、无渐变、无装饰性色块"* (minimalist —
no shadows, no 3D, no gradients, no decorative color blocks); *一致* (consistent); *层级*
(hierarchical); *平面* (flat — pure solid fills, no effects).

### Accent-color families across the corpus
| Firm style | Accent |
|---|---|
| McKinsey | Navy `#003A70` / `#051C2C` |
| Bain | Red `#CC0000` |
| BCG | Green `#00543D` (mbb-deck) / `41,186,116` bright green (actual guide) |

### Colour-blindness and greyscale (kgraph57)
- **Meaning must never depend on hue alone.** Every coloured mark carries a direct label, sign,
  or position that says the same thing.
- The accent and dark grey must stay separable in **greyscale print** — test any replacement.
- In waterfalls, positive and negative bars also differ by **sign prefix on the value label**,
  so monochrome copies still read correctly.

---

## 7. Effects — banned

BCG: *"Do not use shadows, outlines (except as defined), [or other effects]. Effects seem to
enhance shapes, images, and text, [but distract]."*

Universally banned across every source:
- 3D
- Gradient fills (BCG permits six approved gradients on specific Grid graphic elements only)
- Drop shadows
- Bevels
- Chart backgrounds / plot-area shading
- Decorative color blocks behind body text

### Ink discipline (kgraph57 — the strictest formulation)
> "Every mark must carry information (data-ink rule) — with no exceptions. **There is no
> sanctioned decorative motif.**"

Specifically rules out: any decorative bar, horizontal or vertical (a "kicker" stroke above a
headline; a coloured left-edge accent bar on a card); a vertical divider between multi-column
layouts where whitespace would do; and a grey border paired with a grey fill on the same shape
(the fill alone marks the distinction — the border is a redundant second signal).

---

## 8. Layout geometry

### likaku (16:9, `python-pptx`, inches)
```
Slide            13.333 × 7.5
Left margin      0.8"      Right margin  0.8"
Content width    11.733"
Action title     top 0.15", height 0.9"
Title rule       1.05"
Content area     1.3" – 6.5"
Source line      7.05"
Page number      bottom right, 9pt MED_GRAY, "n/total"
```

### kgraph57 (1280×720 px)
```
Grid unit             8 px  (margins and fixed anchors on multiples of 8)
Margins               80 px left and right
Headline baseline     y = 96
Chart band            y = 208 → 560
Annotation baseline   y = 630
Source baseline       y = 692
```

### Mandatory elements on every content slide
From likaku, and consistent with BCG and mbb-deck:
1. **Action title** (top)
2. **Title separator rule**
3. **Content area**
4. **Source line** — `Source: [origin, year]`, bottom-left, ~9pt grey
5. **Page number** — bottom-right, just the number

Title slides are the exception: no page number, no source line.

### Whitespace (mbb-deck)
- Margins at least 0.5", more if possible
- Clear gap between action title and body
- Don't extend content to the edges
- **"If the slide feels full, you have too much on it — split it."**

---

## 9. Density budgets

| Rule | Source |
|---|---|
| **One concept per slide** | BCG (universal) |
| Max 3–5 bullets per text box | mbb-deck |
| Bullets in groups of **at least 2** — a single bullet is not a list, write it as plain text | mbb-deck |
| One idea per bullet: one line ideally, **two lines maximum** | mbb-deck |
| At most one level of sub-bullets | mbb-deck |
| **No clotheslines** — 5+ parallel items get grouped into labelled groups (3 groups of 2 beat 1 list of 6) | mbb-deck |
| 1–6 top-level bullets; a 7th means the slide should split — **7+ is a spec error, never smaller type** | kgraph57 |
| **90-second rule** — if a slide takes >90s to read, it's too dense | mbb-deck |
| ~1 minute per slide of speaking time | likaku |
| Standard report 10–12 slides; short 6–8; minimum 8 for a substantive topic | likaku |
| Appendix slides may be denser — reference material, not presentation material | mbb-deck |

### Word budget (kgraph57)
> "Slides carry claims; prose belongs in the report mode. **When text does not fit, the fix is
> fewer words or another slide — never smaller type** (the type tokens are floors, not
> suggestions)."

---

## 10. "Every slide is a table" — the generating principle

mbb-deck's most useful layout heuristic:

> "Before picking a named pattern, think of the layout as **rows and columns**: rows = items
> (measures, options, phases), columns = dimensions (rationale, impact, timing, owner). This
> single principle produces clean, structured pages and prevents scattered elements."

Three archetypes cover almost everything:
- **Qualitative slide** — a text table: items in rows, columns like measure / rationale /
  impact / timing. Also process steps and timelines.
- **Quantitative slide** — one chart as the main element, with a column for methodology and/or
  implications beside it.
- **Integrated slide** — a table combining text rows with a data column.

*"It is a rule of thumb, not a law — adjust when a framework (2x2, value chain) demands its own
shape."*

---

## 11. Photography, icons, animation

**Icons** — BCG: use when they can be large enough to read; **bugs** when space is limited.
*"Too many icons can quickly [overwhelm]."* mbb-deck: monochrome, one style, accent or grey
only; only when they aid comprehension. kgraph57: no decorative icons that don't encode meaning.

**Photography** — BCG (which does permit it, unlike the other sources) requires considering
tone, subject matter, design aesthetics and composition; find *"true-to-life, clean-looking
photos"*; avoid abstract. **Never near a chart:** *"Refrain from using photography on or near a
chart."* mbb-deck bans stock photography outright.

**Animation** — BCG: *"Animations should only be created by Visual Services."* mbb-deck: **none**
— *"MBB decks are designed to be read on paper or PDF. Any reliance on animation makes the deck
weaker as a standalone document."* Zelazny's storyboard method notes animations should be marked
at storyboard time if used at all.

**Logos** — only when essential; real brand assets only; never generated, never stretched.

---

## 12. File-level conventions

- **16:9** aspect ratio (13.333" × 7.5")
- One master template applied consistently
- File name: `[Client]_[Topic]_[YYYY-MM-DD]_v[N].pptx` (mbb-deck)
- Confidentiality marking centre-footer where needed
- **Status stickers** — PRELIMINARY, INDICATIVE, FOR DISCUSSION, ILLUSTRATIVE — whenever numbers
  are not final. *"Use them honestly: they manage expectations and protect credibility."*

## Cross-references
- Layout catalogue → `03-slide-design/slide-archetypes.md`
- Deck-level shape → `03-slide-design/deck-architecture.md`
- Chart rules → `04-data-visualization/chart-craft-and-decluttering.md`
- Where sources disagree → `05-conventions/contested-points.md`
