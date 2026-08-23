# Source Inventory

Everything ingested for pstack-bower, with provenance, how it was extracted, and how far
each source can be trusted. Read this before quoting any reference file: a few sources have
OCR damage, and two are secondary paraphrases rather than primary doctrine.

## A. Primary literature (`Refs/consulting_material/`)

| # | Slug | Work | Author / Year | Extraction | Fidelity |
|---|---|---|---|---|---|
| 1 | `minto-pyramid-principle` | *The Minto Pyramid Principle: Logic in Writing, Thinking and Problem Solving*, 3rd ed. | Barbara Minto, 2010 | `pdftotext -layout` | **Moderate.** Heavy OCR damage on ligatures (`n1`→m, `vv`→w, `rathe1~`→rather, `1nust`→must). Meaning recoverable; never quote verbatim without cleaning. |
| 2 | `minto-self-study-workbook` | *The Minto Pyramid Principle — Self-Study Course Workbook* | Barbara Minto, 1998 | `pdftotext -layout` | Moderate. Exercise-heavy; layout columns interleave. Useful for worked examples. |
| 3 | `stanley-so-what-strategy` | *The So What Strategy*, Revised ed. | Davina Stanley & Gerard Castles, 2017 | EPUB → XHTML → text | **High.** Clean prose. The single best source for storyline *patterns*. |
| 4 | `mckinsey-approach-problem-solving` | *The McKinsey Approach to Problem Solving*, Staff Paper No. 66 | Davis, Keeling, Schreier, Williams (McKinsey), Jul 2007 | `pdftotext -layout` | **High.** 27pp, clean. Authoritative internal doctrine — SCR, pyramid tests, dot-dash storylines. |
| 5 | `mckinsey-dave-strategic-storytelling` | *Strategic Storytelling: How to Create Persuasive Business Presentations* | Dave McKinsey, 2014 | `pdftotext -layout` | **High.** 69 numbered tips built on teardowns of the *real* McKinsey, BCG and Accenture USPS decks. Note: the author's surname is a coincidence — no firm affiliation. |
| 6 | `zelazny-say-it-with-charts` | *The Say It With Charts Complete Toolkit* | Gene Zelazny, 2006 | EPUB → XHTML → text | **High** for text. Figures are lost — the chart-form matrix is described in prose, not shown. Zelazny was McKinsey's Director of Visual Communications. |
| 7 | `zelazny-say-it-with-presentations` | *Say It with Presentations*, 2nd ed. rev. | Gene Zelazny, 2011 | `pdftotext -layout` | High. Deck-level structure, storyboarding, delivery. |
| 8 | `knaflic-storytelling-with-data` | *Storytelling with Data* | Cole Nussbaumer Knaflic, 2015 | `pdftotext -layout` | High. Gestalt, decluttering, preattentive attributes. Not MBB doctrine — general dataviz craft that MBB practice is consistent with. |
| 9 | `bcg-format-guide` | *PowerPoint Format Guide* v2.3, Sept 14 2018 | Boston Consulting Group | `pdftotext -layout` | **High and unusually valuable.** 202pp of an actual MBB firm's internal slide standard. The only genuine first-party design doctrine in the corpus. |
| 10 | `boettinger-moving-mountains-1969` | *Moving Mountains, or The Art and Craft of Letting Others See Things Your Way* | Henry M. Boettinger, 1969 | `pdftotext -layout` | Good. Older scan, readable. Persuasion, attention, audience. |
| 11 | `boettinger-moving-mountains-collier` | Same work, Collier paperback ed. | Boettinger | `pdftotext -layout` | **Poor — do not use.** OCR badly garbled (`areno`, `observ'ations`, stray glyph noise). Superseded by #10, same content. |

### Reading the fidelity column
Sources 1, 2 and 11 carry OCR damage. Where this library quotes them, the quote has been
hand-repaired and is marked *(OCR-repaired)*. Sources 3–10 can be quoted directly.

## B. Prior-art repositories (cloned from GitHub)

| Repo | What it is | Why it matters here |
|---|---|---|
| `phthomas/pstack` | The user's own 11-skill product-build toolkit (`ps-` prefix) | **The ergonomics to inherit.** dump → start → build/dormammu → review → close. Design principles in `PSTACK.md` and `WHY.md` are the house style for how a pstack-family toolkit should feel. |
| `phthomas/pstack-loki` | The user's own 8-skill deck toolkit | **The thing being replaced.** Its README already diagnoses the same three failures the user reports; the postmortem is in `06-prior-art/pstack-loki-postmortem.md`. |
| `alextimmer/claude-skills` → `plugins/mbb-deck-plugin` | MBB deck plugin: SKILL.md, 5 reference files, 7 subagents, 3 Python scripts | **Strongest external source on MBB conventions.** Ten core principles, slide patterns, visual style, deterministic linting. |
| `likaku/Mck-ppt-design-skill` | Python `python-pptx` engine + 72-layout catalog | Real McKinsey palette (`#051C2C` navy), strict type scale, 72-entry layout catalog, hard-won `experiences/` notes on overflow and CJK. |
| `kgraph57/mckinsey-style-visualization-skill` | SVG renderer + design-token system | The most rigorous *token* system: emphasis-rung ladder, type ratios, ink discipline, a 24-point quality rubric. |

## C. Extraction method (reproducible)

```bash
# PDFs
pdftotext -layout <in.pdf> <out.txt>

# EPUBs (no pandoc/ebook-convert available in this environment)
# python3 stdlib: zipfile → sort XHTML entries → strip script/style →
# <br>,</p>,</div>,</h1-6>,</li>,</tr> → newline → strip tags → html.unescape
```

Staging directory used for this pass:
`/tmp/claude-1000/-home-philip-Projects-pstackbower/<session>/scratchpad/{raw,repos}`

Raw text is **not** committed — it is copyrighted book content. This library holds
distilled doctrine, rules and short illustrative quotes only.

## D. Coverage map — which source answers which question

| Question | Go to |
|---|---|
| How do I structure the whole argument? | Minto (1,2), McKinsey staff paper (4) |
| Which storyline shape fits this situation? | Stanley & Castles (3) — the seven patterns |
| How do I write a title that lands? | Minto ch.7 (1), Dave McKinsey tips 8/9/17/51 (5), Zelazny message titles (6) |
| What goes on the page, physically? | BCG Format Guide (9), likaku, kgraph57 |
| Which chart form? | Zelazny (6) |
| How do I clean up a chart? | Knaflic (8), BCG ch. Charts (9) |
| How should the toolkit *feel* to drive? | pstack (`PSTACK.md`, `WHY.md`) |
| What went wrong last time? | pstack-loki + `06-prior-art/pstack-loki-postmortem.md` |
