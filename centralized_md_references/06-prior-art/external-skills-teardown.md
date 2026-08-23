# External Skills Teardown

The three repositories from `skills_ref.txt`, assessed for what to borrow and what to avoid.

---

## 1. `alextimmer/claude-skills` → `plugins/mbb-deck-plugin`

**Shape:** a Claude Code plugin. One `SKILL.md`, 5 reference files, 7 subagents, 2 slash
commands, 3 Python scripts, JSON schema, palettes, a validation hook.

```
skills/mbb-deck/
  SKILL.md
  references/  storyline.md · slide-patterns.md · visual-style.md
               output-formats.md · marp-rendering.md
  scripts/     build_deck.py · validate_storyline.py · lint_deck.py
  assets/      storyline_schema.json · palettes.json · style_config.json · example_deck.pptx
  examples/    sample-storyline.md · sample-storyline.json
agents/        storyline-reviewer · qa-reviewer · chart-presenter
               data-diagnostic · forecast-modeler · cohort-analyzer · market-basket-analyzer
commands/      /storyline · /critique-deck
hooks/         validate-storyline.sh
```

### Verdict: the strongest external source. Borrow heavily.

**Borrow:**

| Item | Why |
|---|---|
| **The ten core principles** | The tightest statement of MBB convention in the corpus. Reproduced in `05-conventions/mbb-rules-of-the-road.md`. |
| **"Every slide is a table"** | Excellent generating heuristic — rows = items, columns = dimensions. Prevents scattered layouts. |
| **Action title + framing line** | *Title says what's true; framing line says how we know.* Lets the title stay one clean proposition while methodology still appears. Genuinely useful and rare. |
| **The McCandless five-step read** | The best available build-and-present rule for data slides. |
| **The improvement ladder** (topic → generic → wordy → concise quantified) | The single most useful title calibration device found anywhere. |
| **Build order: message → layout → visual → text → polish** | *"never start with the visual or the text."* |
| **Deterministic lint as a mandatory step after any native render** | *"Native renderers improvise typography and color; the lint is what makes the style contract enforceable rather than hoped-for."* Exactly the measurement-over-exhortation principle. |
| **The measured/judged split in `qa-reviewer`** | Lint first (fonts, sizes, colors, bounds, jitter measured), then walk the judgement half. |
| **Format-agnostic storyline → four render targets** | Markdown outline · Marp · native pptx capability · bundled Python. Sound: the methodology is identical, only the renderer differs. |
| **Anti-patterns list** | Comprehensive and specific — clotheslines, colored boxes behind standard text, single bullets, process narration, general truths. |
| **Structuring techniques for navigation** | Structure pages, tracking elements, chapter trackers, double-click logic, leading references. |
| **Status stickers** | PRELIMINARY / INDICATIVE / FOR DISCUSSION / ILLUSTRATIVE, *used honestly*. |
| **Explicit guard against inventing data** | *"Do not invent or estimate values to fill gaps."* |
| **Density profiles** (`default` vs `dense`) | An independent rediscovery of BCG's Key Message / Detail split. |

**Avoid / reconsider:**

| Item | Concern |
|---|---|
| **Pie charts banned outright, "no exceptions"** | Contradicts Zelazny (who defines the comparison framework everyone else quotes) and BCG's own guide. A defensible house policy, but it's presented as doctrine. Make it a flag. See `05-conventions/contested-points.md` §3. |
| **SCQA drafted but no pattern library** | Its `storyline.md` has the Pyramid, SCQA, governing thought and MECE — all correct — but no situational patterns. Same gap as loki. |
| **JSON as the storyline artifact** | Validates well, reads badly. McKinsey's *"PowerPoint is not a good tool for synthesis"* objection applies to JSON too. Prefer a dot-dash memo with JSON derived from it. |
| **Seven subagents, four of them analytics** | `data-diagnostic`, `forecast-modeler`, `cohort-analyzer`, `market-basket-analyzer` are a different product bolted on. Fine, but out of scope for a deck toolkit. |
| **"Do not include an Executive Summary" is not considered** | It asserts slide 2 without engaging Dave McKinsey's tip 33. Minor, but it's an unstated choice. |

**Its own storyline reference is good but thin** — three pyramid rules, SCQA, the improvement
ladder, governing thought examples, MECE, four tests. Roughly 5KB. Compare the depth available
in Minto and Stanley & Castles. This is where pstack-bower can be substantially better.

---

## 2. `likaku/Mck-ppt-design-skill`

**Shape:** a Python `python-pptx` engine (`mck_ppt/`) plus a 72-layout catalogue and team
convention docs. Partly in Chinese.

```
mck_ppt/      engine.py · deck_builder.py · core.py · qa.py · review.py · constants.py
references/   layout-catalog.md (72 layouts) · color-palette.md · INDEX.md
              team/presentation-convention.md · team/brand-guide.md
              framework/engine-api.md · guard-rails.md · planning-guide.md
experiences/  overflow.md · layout-pitfalls.md · cjk-issues.md · chart-limits.md
```

### Verdict: borrow the design specifics and the `experiences/` idea.

**Borrow:**

| Item | Why |
|---|---|
| **The McKinsey palette** | `NAVY #051C2C`, `DARK_GRAY #333333`, `MED_GRAY #666666`, `LINE_GRAY #CCCCCC`, `BG_GRAY #F2F2F2`. Real, specific, usable. |
| **Strict type scale** | 44 cover / 28 section / 22 action title / 18 sub-header / 14 body / 9 footnote. *"不得使用其他字号"* — no other sizes permitted. Enforceable. |
| **Exact geometry** | 13.333×7.5", 0.8" margins, title at 0.15" height 0.9", rule at 1.05", content 1.3–6.5", source at 7.05". Directly implementable. |
| **Mandatory element list** | Every content slide: action title, separator rule, content, source, page number. |
| **The 72-layout catalogue** | A menu. Condensed into `03-slide-design/slide-archetypes.md` Tier 3. |
| **Accent colours only when 3+ parallel items** | A precise rule for when the palette may expand. |
| **`experiences/` as a first-class directory** | Accumulated hard-won notes on overflow, layout pitfalls, CJK issues, chart limits. **This is a pattern worth copying** — a place for what was learned the hard way, distinct from doctrine. |
| **Design philosophy, stated in four words** | 极简 (minimalist) · 一致 (consistent) · 层级 (hierarchical) · 平面 (flat). No shadows, no 3D, no gradients, no decorative colour blocks. |
| **Retired layouts marked, not deleted** | `~~14~~ Three-Pillar Framework → use #71 Table+Insight`. Honest about what didn't work. |

**Avoid / note:**

| Item | Concern |
|---|---|
| **Georgia for titles** | Fine, but it's a choice — see `contested-points.md` §5. |
| **Hardcoded install path** (`~/.workbuddy/skills/mck-ppt-design`) | Environment-coupled. |
| **Bilingual docs** | Some conventions are only in Chinese; easy to miss. |
| **No storyline layer at all** | This is a *design* skill. It assumes you already know what to say. Complements rather than competes. |

---

## 3. `kgraph57/mckinsey-style-visualization-skill`

**Shape:** an SVG renderer plus a rigorous design-token system, extensive docs, a test suite,
and a lot of go-to-market material (`MARKETPLACE.md`, `COMMERCIALIZATION.md`, `TRACTION.md`,
`GROWTH.md`…).

```
scripts/      render_slide_spec.py · review_slide_spec.py · scaffold_deck.py
              build_html_{deck,report,article} · build_speaker_script.py · validate_skill.py
references/   style-system.md (23KB) · visualization-patterns.md · quality-rubric.md
              document-type-profiles.md · persona-playbook.md · prompt-templates.md
              input-triage.md · iterative-review-loop.md · expert-review-loop.md
tests/        11 test files
```

### Verdict: the best *token system* in the corpus. Borrow the rigor, ignore the marketing.

**Borrow:**

| Item | Why |
|---|---|
| **The emphasis strength ladder** | Fill > line > text, five ranked rungs, with discipline rules: cap rungs 1–2 at one element; never stack rungs; keep meanings constant deck-wide. **The best emphasis guidance found anywhere**, and it makes "highlight the important thing" mechanically checkable. |
| **Type ratios, not just sizes** | headline:body:chrome ≈ 4:1.6:1, with minimum ratios asserted. *"A change that breaks either ratio is wrong, whatever it does for a single slide in isolation."* |
| **Hard reading floor** | 18px for anything the reader must read; chrome deliberately smallest — *"never raise it to 'balance' a slide."* |
| **Word budget as a design token** | *"When text does not fit, the fix is fewer words or another slide — never smaller type."* |
| **Ink discipline, absolutist form** | *"There is no sanctioned decorative motif."* Includes the story of removing its own navy kicker bar because it carried no information. |
| **Greyscale and colour-vision survival** | Accent and dark grey must stay separable in greyscale — *asserted in the test suite*. Waterfall bars carry a sign prefix so monochrome copies still read. |
| **The 24-point quality rubric with blocking gates** | Reproduced in `05-conventions/quality-rubrics-and-checklists.md` §6. |
| **The deck-level check** | *"Single-slide scores do not guarantee a coherent deck."* Read only the headlines; three yes/no questions. |
| **Tokens shared between docs and renderer** | *"If a value changes, change it in both places in the same commit — a spec that cannot be reproduced from this document is a bug."* |
| **Spec-only vs renderer-supported, stated honestly** | *"the skill delivers a spec or image-generation prompt; say so explicitly in the deliverable."* No pretending. |
| **CJK typography handling** | Looser leading (1.75–1.8× vs Latin 1.5×), kinsoku line-breaking, system faces before Noto — *"a partial Noto install (commonly Black weight only) listed first would set body text ultra-bold."* Real-world detail. |
| **Anti-affiliation rule** | *"Faux affiliation language with named consulting firms"* is banned. Worth adopting — the corpus material describes MBB *practice*; a skill should not imply endorsement. |

**Avoid:**

| Item | Concern |
|---|---|
| **Extreme layout specificity in prose** | Its `style-system.md` contains a ~500-word paragraph about `band_start` anchoring, recounting three regression rounds. Valuable as an engineering changelog; misplaced in a style reference. **Keep the rule, move the history to an `experiences/` file** (likaku's pattern). |
| **Marketing docs in the repo** | TRACTION, GROWTH, COMMERCIALIZATION, BUYER_BRIEF, MARKETPLACE_TARGETS, LAUNCH, DISTRIBUTION. Noise for a reference read. |
| **No storyline layer** | Like likaku, this is visualization-first. Headline discipline is present; storyline construction is not. |
| **SVG-only rendering** | 16:9 only; other canvases are spec-only. Fine, but not a `.pptx` path. |

---

## 4. Comparative summary

| Dimension | mbb-deck | likaku | kgraph57 | pstack-loki |
|---|---|---|---|---|
| Storyline theory | **Good** (Minto + SCQA) | None | Minimal | Partial (arc, not pyramid) |
| Storyline patterns | ✗ | ✗ | ✗ | One (fixed) |
| Action title craft | **Good** (ladder, examples) | ✗ | Headline rules | Rules only |
| One slide one message | **Stated** | Implicit | Implicit | Exhibits only |
| Slide design doctrine | **Good** | **Very specific** | **Most rigorous tokens** | ✗ (delegated) |
| Layout catalogue | 9 patterns | **72 layouts** | ~30 patterns | 4 types |
| Chart selection | Zelazny table | Chart types | Comparison-first | **Zelazny table** |
| Deterministic linting | **Yes, 3 scripts** | QA module | Test suite | Geometry lint |
| Quality rubric | Checklists | Gate checks | **24-pt scored** | Six passes |
| Process / ergonomics | 8-step workflow | Planning guide | Review loops | **Best** (one gate, autonomy) |
| Rendering | 4 targets | python-pptx | SVG + HTML | Delegated |

**The composite that doesn't exist yet:** loki's process + mbb-deck's conventions + likaku's and
kgraph57's design specificity + **a real storyline pattern library and title calibration corpus,
which none of them have.** That gap is precisely what pstack-bower is for.

---

## 5. Structural lessons about skill design

Independent of content, three things these repos demonstrate:

1. **Reference files beat a fat SKILL.md.** All three split doctrine into `references/` loaded on
   demand. mbb-deck's SKILL.md points at five; kgraph57 at ten.
2. **Scripts make rules enforceable.** mbb-deck's three-script arrangement — build, validate,
   lint — is the clearest realization of measurement-over-exhortation in the survey. The lint
   runs on *any* pptx, including ones produced by other tools.
3. **An `experiences/` directory is worth having.** likaku's four files (overflow, layout
   pitfalls, CJK, chart limits) capture what was learned the hard way. It keeps doctrine clean
   while preserving the scar tissue — and kgraph57's style doc shows what happens without one.

## Cross-references
- What each contributed → `00-source-inventory.md` §B
- Where they disagree → `05-conventions/contested-points.md`
- The gap they share → `06-prior-art/pstack-loki-postmortem.md` §3
