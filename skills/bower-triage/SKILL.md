---
name: bower-triage
description: Turn a reviewed dump.md into a frozen deck blueprint and hold the one human gate. Use when the user types /bower-triage (with no argument), says "triage", "spec it out", "turn the dump into a plan", or when dump.md exists and no frozen storyline does. Invoked WITH an objection as argument ("/bower-triage S07 overclaims — data says 32"), it is the revision front door: classify the objection's magnitude and run the matching delta. Also handles delta-gates during revision (re-printing only a changed storyline leg or slideplan segment for a quick "closed"). Orchestrates bower-intake, bower-storyline and bower-exhibit; emits STYLE.md; runs the environment preflight; freezes on "closed".
---

# bower-triage

Orchestrator and gate-holder. Everything judged happens here or upstream; after "closed",
execution never negotiates with the blueprint.

## Steps, in order

1. **Dump gate.** Check the canonical fields in `dump.md`: Audience · Ask · **Delivery mode
   (projected/read/both)** · Data · Constraints · Stakes. Budget is *optional* — a scope input,
   never a gate field. Anything missing → **STOP: list exactly what's missing as questions to
   answer in dump.md. Never invent the missing content — that defeats the gate.**
   No `## Storyline v0` section → say so and offer bower-grillme; derive from prose only if the
   user insists, and say the ladder will be lower-confidence for it.
2. **Intake step 0.** Run bower-intake if `refs/` changed since it last ran, or it never ran.
3. **Environment preflight.** Check: the STYLE fonts installed · LibreOffice (`soffice`) ·
   `pdftoppm` + `pdffonts` · Node + pptxgenjs. Failures don't block composing but appear in the packet
   in red — **degradation is visible, never silent** (a substituted font means visual QA
   inspects a different deck than the client will open).
4. **Style resolution → `STYLE.md`.** If intake flagged a template, derive it two ways:
   - **Exact tokens** — `scripts/bower_theme.py template.pptx` (stdlib zip read): palette
     hexes, major/minor fonts, slide size.
   - **The visual read** — render the template (`../bower-qa/scripts/bower_render.py`) and
     derive from the pixels what the theme XML cannot say: which colour is the ACCENT vs
     decoration, title treatment and geometry, footer conventions, density register. Usage is
     visual; the rendered pages are the truth. Keep `slides-template/` — QA pass 6 anchors to
     these renders.
   Else: the likaku fallback. Either way fill BOTH scales per
   `../bower-build/references/style-schema.md`; floors always hold — a client template does
   not license 12pt body on a projector. Template fonts not installed → preflight red. Say
   which path was taken.
5. **Delegate:** bower-storyline (harden v0 → v1), then bower-exhibit (spec every visual).
6. **Evidence audit.** Every FACT-tagged claim cites a [D#] or a `data/src/` cell. Anything
   unsupported gets one of three fates — find the data, demote to EST/JUDG with disclosure, or
   cut the slide. UNVERIFIED transcriptions supporting load-bearing claims get named in the
   packet.
7. **The triage packet** — print for the human sitting:
   1. The slide ladder, connectives inline, read as a skeptic would.
   2. **Unresolved objections from dump.md, verbatim — each with how it was resolved or why it
      still stands.** Never silently dropped.
   3. One-line exhibit digests; full spec + data reachable underneath.
   4. STYLE.md summary + its source; preflight results.
   5. Any `render: image` exhibits (non-native forms), named.
   6. The disposition policy for QA findings — defaults: SEV-1 fix · SEV-2 fix · SEV-3 accept.
   7. The ask, verbatim.
8. **Hold the gate.** The user objects in plain language ("S07 overclaims — the data says 32");
   re-lint, re-print the affected part. On **"closed"**: mark `storyline.md` `v1 FROZEN <date>`,
   log to `TIMELINE.md`. Titles are now immutable within the version.

## Delta-gate mode (revision protocol)

**Invocation:** `/bower-triage <objection in plain words>` — classify the magnitude first:
**render** (a pixel/wording-of-render fault) → hand to bower-build, no gate · **sequence**
(slide existence/order) → slideplan delta below · **claim** (a title, number-as-claimed, or the
So-what) → storyline delta below · **frame** (audience/ask) → bower-grillme. Say which class
you chose and why before acting.

For **sequence** deltas (slideplan changes) and **claim** deltas (storyline changes): print
ONLY the changed artifact section — the affected ladder leg with its connectives re-run, or the
new slideplan segment — plus the derived dirty set (slides/exhibits it touches). The user says
"closed"; one message, not a sitting. Claim deltas always bump the storyline version and append
to its `## Changelog`. **Frame** deltas (audience/ask changed) go back to bower-grillme and a
full gate.

## Two minutes of real reading

Tell the user plainly: the ladder read at this gate is the best-spent time in the pipeline — a
flow problem costs one objection here and a rebuild cycle after the build.
