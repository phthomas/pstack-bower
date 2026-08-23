---
name: bower-qa
description: Full-spectrum review of a built deck — lint, storyline ladder, title craft, vertical logic, exhibit correctness, grounding, style and positioning on rendered pixels, and a cold read. Use when the user says "qa" (scoped mode), "final qa" or "ship qa" (all eight passes), "review the deck", "check the slides", or before any deck ships; also works standalone on any .pptx someone sends, in a degraded mode. Findings carry severities and route upstream to the stage that owns them.
---

# bower-qa

Decks have no compiler; this manufactures one. Render to pixels, assert against the specs,
read the argument end to end. **Findings route upstream** — a flow problem is a storyline bug,
never a slide patch.

Load: `../bower-storyline/references/title-craft.md` (classifier) ·
`../bower-storyline/references/title-bank.md` (pass 2 judges AGAINST it) ·
`../bower-exhibit/references/chart-matrix.md` (pass 4 asserts its checklist) ·
`../bower-build/references/style-schema.md` (pass 0/6 tokens).

## Modes

- **Scoped** (`/bower-qa`, bare) — revision cadence: pass 0 + the full ladder read (cheap, global) + judged
  passes on **dirty slides only** (from the revision delta; else slides changed since last QA).
- **Ship** (`/bower-qa ship`; also "final qa"; used by bower-run before SHIPPED) — all eight passes, whole deck.
- **Standalone/degraded** (an external .pptx, no blueprint): passes 0, 2, 3, 6, 7 run in full;
  passes 1, 4, 5 report "no blueprint — skipped", never guessed.

## Step 0 — render

`scripts/bower_render.py deck.pptx slides/` → one PNG per slide (keeps the intermediate PDF for
`pdffonts`). **QA never reads the pptx XML**: it judges rendered pixels, blueprint artifacts,
and the JSON fragments — the same three things the client's eyes, the argument, and the data
actually touch.

## The eight passes (cost-ordered: 0 and mechanical-5 first)

| # | Pass | Asserts |
|---|---|---|
| 0 | **Lint** (`scripts/bower_lint.py`, stdlib-only) | Fragments: schema · forbidden style keys (by-construction guard) · banned exhibit types · CSV references exist · title slop lexicon · ALL-CAPS · **title-number grounding vs CSV/[D#]** · chartTitle≠title dedup. PDF: embedded font families ⊆ STYLE fonts (`pdffonts`) |
| 1 | **Storyline & ladder** | Memo read · connective test · question chain · Key Line MECE · orphans · repeated/contradictory titles · exec summary on slide 2 = governing thought + Key Line verbatim · divider promises = Key Line sentences |
| 2 | **Title craft** | Every title through the defect classifier, **then judged against the bank**: "does this ladder read like the [REAL] titles or like the anti-pattern gallery?" The classifier catches defects; only the bank catches calibrated-but-bland |
| 3 | **Vertical logic & one message** | Body *unambiguously proves* its title · exactly one message per slide · framing line says how-we-know, not a second claim |
| 4 | **Exhibit correctness** | Form matches comparison type · every element-checklist line against the render · chart so-what present (or deliberately deduped) · emphasis on the right carrier · BCG mechanics |
| 5 | **Grounding** | On fragments, pre-assembly: every exhibit number ↔ `data/E##.csv` cell · every non-exhibit number ↔ [D#] inventory entry · title numbers = body numbers exactly · UNVERIFIED [D#]s under load-bearing claims · renders spot-checked for transcription (pass 6 catches display faults) |
| 6 | **Style & positioning** (renders) | Theme conformance — **judged against the rendered template pages (`slides-template/`) when a template exists: like-for-like, pixels vs pixels** · emphasis-rung discipline (≤1–2 strong, no stacking, meanings constant) · hierarchy and eye flow · whitespace · collisions/clipping/overflow · squint test |
| 7 | **Cold read** (renders) | The whole deck, front to back, **speaker notes off** — it circulates as a pre-read and must argue with its author absent. Would a skeptical exec who reads only this say yes? |

## Findings — `qa.md`

```
SEV-n | S## | pass | finding | route: storyline | exhibit | build | intake | CLAIM(escalate)
```

| SEV | Meaning | Default disposition (pre-committed at triage) |
|---|---|---|
| 1 | Wrong, misleading, unsupportable | Fix |
| 2 | Breaks a convention; costs credibility | Fix |
| 3 | Polish | Accept |

**Routing:** flow → storyline · missing chart element → exhibit · number transcribed wrong →
build (auto-fix to source) · homeless number → intake · **title claiming more than the source
supports → CLAIM: escalate to the human, never auto-fix** (weaken the title or strengthen the
evidence is the user's call). A revision that touched any claim re-runs pass 1 on the whole
ladder — flow is a global property.
