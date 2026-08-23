# Engine Notes — pptxgenjs, settled decisions

*(Amended 2026-08-23: writer switched from python-pptx to pptxgenjs. Rationale: QA reviews
rendered pixels + fragments, so the writer's XML is never read back; compliance is by
construction in the assembler; the writer is chosen purely as a generation substrate, and
pptxgenjs's declarative API is the better one.)*

## The decisions

| Question | Decision |
|---|---|
| Writer | **pptxgenjs** (Node), single assembler |
| Fragments | **Declarative JSON** (schema below) — content only, style forbidden |
| Charts | **Native-first** — `addChart` wherever PowerPoint has the type (BAR, LINE, AREA, SCATTER, BUBBLE, RADAR…); the client must be able to edit the deck. `render: image` only where no native form exists, per the exhibit spec flag |
| Waterfall | Native: stacked bar (`barGrouping: 'stacked'`) with an invisible base series — base = running total, coloured to the background; floating bars carry explicit value labels |
| Marimekko / non-native | `render: image`, or re-form the message |
| Overflow | Character-budget pre-check in builders; **verdict by render-and-inspect** (soffice → PNG → bbox vs the content band). Never PowerPoint autofit (`fit: shrink` etc. banned — autofit hides overflow) |
| Concurrency | Workers emit fragments; **one assembler** writes deck.pptx once |
| Templates | **Visual-match v1** (no master/layout inheritance — the deck looks like the template; it does not embed the client's masters). Two channels: theme XML via `bower-triage/scripts/bower_theme.py` (stdlib — exact palette/fonts/slide size) + the rendered template pages (accent usage, geometry, register). Fallback when no template: likaku |

## The fragment contract — `fragments/S##.json`

Workers never touch the deck file. Each emits one JSON fragment; the assembler (Node +
pptxgenjs) walks `slideplan.md` order, dispatches each fragment to its **archetype builder**,
and saves once.

```json
{
  "id": "S07",
  "archetype": "single-chart",
  "title": "Repricing the top decile via RBPE protects ~20bps at low attrition risk",
  "framing": "Acme analysis vs FY25 repricing cohorts; excludes one-off recoveries",
  "blocks": [ {"kind": "bullets", "items": ["…", "…"]} ],
  "exhibit": {
    "spec": "E04",
    "type": "bar",
    "csv": "data/E04.csv",
    "chartTitle": "NIM protection by repricing decile, bps",
    "emphasis": "series:Top decile",
    "render": "native"
  },
  "callouts": [ {"anchor": "Top decile", "text": "~20bps protected"} ],
  "notes": "How to read → so-what → transition (from connective-out)",
  "tracker": "III"
}
```

**Forbidden keys, anywhere in a fragment** (linted, SEV-1): `font`, `fontFace`, `fontSize`,
`size`, `color`, `colour`, `fill`, `bold`, `italic`, `x`, `y`, `w`, `h`, `align`. Style and
geometry belong to STYLE.md + the archetype builders — **compliance by construction**. A
fragment that wants styling is a worker trying to make a design decision; refuse it.

## The assembler + builders (Node)

- One builder per archetype (see `archetypes.md`); builders read STYLE tokens once and apply
  them everywhere — there is no path to an off-scale size or an off-palette colour.
- **There is no pie or doughnut builder.** The ban is structural, not advisory.
- Titles placed verbatim from the fragment (which carries them verbatim from slideplan).
- Every shape gets its semantic name via `objectName`: `title`, `framing`, `exhibit`,
  `chart-title`, `callout-*`, `takeaway`, `source`, `page`, `tracker`.
- Speaker notes from `notes` (projected decks).
- Furniture (source, page number) added by the builder for every content slide — impossible to
  forget, no lint needed.
- pptxgenjs gotchas: define the layout BEFORE adding slides; hex colours WITHOUT `#`; use
  native `addChart` for anything PowerPoint can chart.

## QA reading — no XML, ever

- Passes 1–4, 6, 7: rendered PNGs + blueprint artifacts (storyline, slideplan, specs).
- Pass 5 grounding: **fragments vs `data/E##.csv` + `refs/inventory.md`** — exact, pre-assembly.
- Font verification: `pdffonts deck.pdf` — embedded families must ⊆ STYLE fonts. Exact, no XML.
- `bower_lint.py` runs on `fragments/` + the rendered PDF (python3 stdlib only — no
  python-pptx dependency).

## Study, don't adopt

likaku's `mck_ppt` engine still informs the overflow heuristics and geometry constants — but
its 40-char title gate stays out (our house register runs far longer), and its python-pptx
mechanics no longer apply to the writer.
