# Fable 5 Design Review

Independent fresh-context review, commissioned by Philip on 2026-08-23 before phase 2
(implementation). Reviewer: Claude Fable 5, with no prior involvement in the work. It read all
library files in full and verified claims against the staged prior-art repos (pstack-loki's
SKILL.md, pstack's PSTACK.md, likaku's constants.py and qa.py) — all checked out.

**Disposition (same day):** the four staleness contradictions (§3.1), the dump-gate fields
(§3.2/2.3), the QA-pass drift (§3.4), the divider ambiguity (§3.5) and the hard-rule-6 demotion
(§3.6) were fixed in the library immediately. The structural recommendations were decided by Philip the
same day — bower-intake added (triggerable from grillme) · grillme emits the draft dot-dash ·
revision protocol adopted · native-first engine — and all landed in skill-architecture v2 along
with the accepted note-for-later items. (Engine writer amended later the same day: pptxgenjs
replaced python-pptx after Philip's render-review argument — see architecture §8; QA reviews
pixels + JSON fragments, python-pptx demoted to an optional template-token reader.)

The review follows verbatim.

---

# pstack-bower design review

**Reviewer basis.** I read all 22 files in `/home/philip/Projects/pstackbower/centralized_md_references/` in full, and verified the library's claims against the staged repos where possible. The postmortem's claims about `pstack-loki` check out line-for-line against `loki-storyline/SKILL.md` (five-beat Western sheet with "Structure is non-negotiable", the seven title rules, the 0–3 theme dial, one-message scoped to exhibits only, the README naming the same three failure modes). The pstack quotes are verbatim in `PSTACK.md`. likaku's tokens match its `constants.py` (NAVY `#051C2C`, Georgia 22pt, Arial 14pt), and its `qa.py` really does EMU-level overflow detection. The library is trustworthy as a record.

---

## 1. Verdict on direction

**The shape is right, and the three defects are genuinely addressed at the design level — not just described better.**

- **Titles.** loki had rules; bower has a failure theory (four named mechanisms), a calibration corpus with real firm titles, the end-product test, a defect classifier, and the routing rule that sends blank assertions upstream instead of to a rewriter. That last rule is the single most important fix in the whole design, because it attacks the actual loki failure (rule-compliant blandness) rather than adding an eighth rule.
- **One-slide-one-message.** Now stated at slide level (`mbb-rules-of-the-road.md` §3), gated in the storyline, and given its own QA pass. Fixed.
- **Storyline.** The diagnosis — SCQA-as-architecture displaced the pyramid, answer at 55% — is correct and verified against loki's source. Pyramid + seven patterns + question chain + exec summary on slide 2 is the direct repair, and the pattern library is the one asset no prior art has.

The meta-fix (calibration + measurement over advice-in-context) is applied consistently. **However:** the doctrinal risk is now retired and the *execution* risk is not. Everything that will actually go wrong with the first deck lives in the seams the architecture hasn't specified — data ingestion, the revision loop, doctrine packaging, and the pptx engine. Those are Section 2 and 4. And one honest caveat on titles: the fix is calibration-plus-judgement, which is plausible but unproven until a real deck. A title can pass all eleven hard rules and the classifier and still be the "fancier blank assertion" — the only defense is the judged pass explicitly anchored to the bank, so make that anchoring structural (see rec 10).

---

## 2. What's missing

Ordered by when the first real deck hits it.

**2.1 Data ingestion has no owner — the biggest gap in the pipeline.** loki had `loki-mobius`: reference intake, `refs/manifest.md`, `[D#]` citable fragments, house-style calibration. bower dropped it and absorbed only the style-resolution half (into triage). Nothing ingests the xlsx, the screenshot of a table, the prior deck, the 40-page PDF. Yet the design depends on it three times: triage's evidence audit ("every FACT-tagged claim cites a data reference" — a reference *in what registry?*), bower-exhibit's `data/E##.csv` (extracted from what, verified by whom?), and QA pass 5 ("every number traces to a source cell" — of which source?). Your actual workflow starts with "giving source materials"; the first real deck stalls at exhibit-spec time when someone has to turn `Q3_board_pack_v7.xlsx` into citable numbers with provenance. Needs a mobius-equivalent (a skill or a heavy triage step): refs → inventory with provenance, xlsx/csv extraction, screenshot transcriptions tagged EST until verified against a real file.

**2.2 The revision protocol doesn't exist — and revision is most of your stated workflow.** "Revision until it's good" implies many post-build iterations, and the architecture's only answer is "objecting in plain language and re-running." Undefined: who may unfreeze `storyline.md`; what a v2 freeze looks like; how a storyline delta propagates a dirty-set through slideplan → exhibits → slides; whether a post-build title change requires re-gating (it's a claim change — by the design's own logic it must, but a full triage sitting per objection would be unbearable, so you need a lightweight delta-gate); how a QA SEV-1 escalation ("title overclaims") re-enters the pipeline after you answer it. loki had the germ — `## Changelog` deltas triggering a re-touch list — and bower dropped it. This is the machinery the entire "until it's good" phase runs on. Design it before phase 2, or the first revision session will improvise it badly.

**2.3 The delivery-mode question is never asked.** Finding 4 says density is *the* parameter ("ask 'projected or read?' before building"), the rules-of-the-road has a whole section on it — and it appears in no gate field anywhere. Triage's six dump-gate fields: audience, ask, data inventory, constraints, stakes, slide/time budget. Delivery mode is missing, and slide budget (which decision #6 demoted to an optional scope input) is mandatory instead. This is exactly backwards relative to the settled decisions.

**2.4 Appendix handling is absent.** The doctrine demands one (tip 26: ruled-out options belong in the appendix; BCG: the dense twin of a projected chart belongs there; density budgets explicitly loosen for appendix slides). But `slideplan.md` knows only argument rows and structural rows, and the ladder tests would flag every appendix slide as an orphan. Needs an explicit appendix section: exempt from ladder/connective tests, Detail density, still linted, with a rule for what triage sends there (ruled-out options, methodology, detail twins).

**2.5 Speaker notes are unassigned.** `deck-architecture.md` §7 has the doctrine (voiceover = how-to-read-the-visual + so-what + oral transition; the connective-out column is the raw material) — and no skill writes them. The cold read is correctly notes-off, but a projected deck without notes is half-delivered. One sentence in bower-build's contract fixes this.

**2.6 No environment preflight.** pstack has `/ps-doctor` and the principle "capabilities named once, degrade visibly" — the design brief lists it as inherited, but no bower skill owns it. Concretely: if Georgia/Arial aren't installed on the build host, LibreOffice silently substitutes fonts, so pass 6 inspects renders of a *different deck* than the client will open, and overflow QA measures the wrong text extents. Preflight (fonts, LibreOffice, python-pptx, renderer) belongs in triage or bower-run's pre-flight, with visible degradation.

**2.7 Doctrine packaging is unsolved, and the open item understates it.** "Where does the example bank live" is the small version of the question. The library is ~5,500 lines (~60–75k tokens) — no skill loads it all. There is no mapping of which files feed which skill, and the files are review-oriented prose (provenance, contested tables, verbatim quotes) rather than skill-facing instruction. The numbers are workable — craft + bank ≈ 590 lines (~8k tokens) fits comfortably in bower-storyline and in QA pass 2 — but somebody has to decide the manifest and produce policy-resolved distillates (see 3.1 for why resolution matters, not just selection). Note the bank must be in *two* contexts: composition (bower-storyline) and judgement (QA pass 2), or the judge can't recognize calibrated-but-bland.

**2.8 Grounding for numbers outside exhibits.** `data/E##.csv` holds "the only numbers allowed on that slide" — for exhibit slides. A big-number slide, a text slide claiming "three of seven sites", the exec summary's quantified Key Line: where do those trace? loki's rule was "a CSV cell **or dump reference**"; bower dropped the second half. Restore a home for non-exhibit numbers or pass 5 has holes exactly where overclaim lives.

**2.9 Smaller gaps, noted:** QA's "works standalone on any .pptx" needs a defined degraded mode (passes 1 and 5 need artifacts external decks don't have). Photography in an autonomous run — state that photos come only from `refs/`, never fetched or generated, or run will improvise. Mixed-density decks (present + leave-behind in one file, BCG's actual model) — fine to defer, but say so. One deck per project directory is implied, never stated.

---

## 3. What's wrong or overbuilt

The library's content quality is high and I found no misrepresented doctrine. The problems are **staleness against the settled decisions** — pre-decision text that survives in files a skill will load, which is precisely the "opinions baked in without being surfaced" failure this project exists to prevent.

**3.1 The library contradicts house policy in four places:**

1. **`02-action-titles/action-title-craft.md` §5** still states the *superseded* chart-title rule as current: "Resolution used in this library: when the chart is the whole slide … the chart needs at most a units/axis descriptor." Decision #2 says chart titles **always** state the so-what, dropped only when word-for-word identical. An implementer loading the craft file — the file the whole toolkit turns on — follows the wrong rule.
2. **`05-conventions/mbb-rules-of-the-road.md` hard-ban table** still lists "Decorative imagery / stock photography" as banned. Decision #4 adopted BCG's permissive convention. The parenthetical pointer exists, but a linter built from that table bans what policy permits.
3. **`04-data-visualization/zelazny-chart-selection.md`** hands "pie" to every component message with no ban pointer at all, and `slide-archetypes.md` Tier 3 menu offers Pie, Donut, and Gauge. Source-faithfulness is right for the library — but if bower-exhibit loads these files as its form-picker, the model will propose pies and the linter will bounce them, forever. The skill-facing versions must be house-resolved (component → sorted bar/stacked column; banned rows marked).
4. **`06-prior-art/pstack-loki-postmortem.md` change table** still says output medium "Chosen: one-pager · memo · deck · verbal storyline" — superseded by pptx-only-v1.

**3.2 The dump gate contradicts decision #6.** Slide/time budget as a mandatory refuse-if-missing field, when the settled policy is "the story sets the count" and a budget is only a scope input. Make it optional-with-default; make delivery mode mandatory instead (see 2.3).

**3.3 The STYLE.md fallback can't express the density parameter.** likaku's system is one fixed scale — 22pt Georgia titles, **14pt Arial body**. By BCG's own classification that is a read-density system: a *projected* deck at 14pt body violates the Key Message floor (16pt for everything except chart labels; 20pt default body). So the two settled positions — "density is a parameter" and "fallback = likaku's single scale" — cannot both hold as written. (Also: likaku's 22/14 title:body ratio is 1.57, under kgraph57's asserted 1.7 minimum — the corpus's own token systems disagree.) `STYLE.md` needs a schema with per-mode scales, and nobody has defined that schema at all.

**3.4 Document drift on the QA passes.** Design brief §3 shows seven passes with "slop" as its own pass; rubrics §8 shows a different seven; the architecture (the settled one) has eight with title-craft absorbing slop. Cosmetic, but stale diagrams in the brief will confuse phase 2.

**3.5 Section-title ambiguity.** The measurable target says "the Key Line points on slide 2 are the same sentences as the section titles," while the archetype file exempts section dividers from action titles ("section name and, optionally, a one-line promise"). Both defensible; pick one and state it, or the ladder lint will fight the divider archetype.

**3.6 Hard rule 6 is contradicted by the bank's own real exemplars.** "Present tense, active voice" as a *mechanically checkable hard rule* would flag "Losses **have been driven** by volume declines…" — a verbatim McKinsey title the bank holds up as ground truth. The bank's own note ("real firm titles are plainer and longer… they do not sparkle") is the correct register; rule 6 belongs in the judgement list as a default, not the lint. (Similarly rule 3, falsifiability, is listed under "mechanically checkable" and isn't.)

**3.7 Overbuilt? Very little.** Seven skills all pass pstack's five-justification test; the deliberate redundancy across library files is fine for humans. The one real redundancy risk is at packaging time: the exhibit checklist exists in two files and the title rules in three — pick one canonical copy per rule for the skill-facing versions or they will drift.

---

## 4. Risks in the skill architecture

**4.1 The grillme→dump→triage handoff has a contract mismatch and a lossy round-trip.**

- *Contract mismatch:* grillme interrogates purpose, audience, question, So-what, pattern, Key Line, evidence. Triage gates on audience, ask, data inventory, constraints, stakes, budget. Constraints and budget are in neither grillme's list nor its terminal output spec — so a dump grillme itself wrote can fail triage's gate. One canonical dump.md field list, shared by writer and gate.
- *Lossy round-trip:* the storyline is agreed in conversation, serialized into prose in dump.md, then *re-derived* into dot-dash by bower-storyline. That is exactly the "handoff and re-derivation" contested point #9 forbids ("the Day 1 guess and the final storyline are one document… no handoff, no re-derivation"). Since the argument is already agreed at grillme's terminal moment, grillme should emit the draft dot-dash itself (inside dump.md as a distinct section, or as `storyline.md v0 DRAFT`), and bower-storyline should *harden* it — run the gates, fix the wording, never reconstruct the tree from prose. This also splits dump.md's two conflated jobs: the brief (facts about the engagement — audience, ask, data, constraints, stakes, mode) and the argument (the dot-dash). They change at different rates, which is pstack's own storage principle. Also: grillme should write an "unresolved objections" section — the pushback that didn't get resolved in conversation — and triage should refuse to silently drop it. Otherwise adversarial grilling degenerates into a note-taker with attitude, because live conversation rewards agreement.

**4.2 The one-gate/frozen model serves build #1, not "revision until good."** Covered in 2.2 — this is the architecture's largest hole. The gate-then-autonomy ergonomic is correct and the freeze is correct; what's missing is the *thaw*. Concretely design: a route table by objection magnitude (wording of a render → build delta, no gate; a slide's existence/order → slideplan delta + delta-gate; a claim/title/So-what → storyline delta + scoped re-gate of the affected leg + version bump; audience/ask → back to grillme), with automatic dirty-set derivation so "run" after an answer rebuilds only what the answer touched (the architecture promises this for BLOCKED; extend it to all revision).

**4.3 Eight QA passes are executable but will dominate the loop.** Five judged passes on renders of a 25-slide deck, per revision iteration, is a lot of deep-model time. Fine for the overnight dormammu run; punishing at revision cadence. Add a scoped QA mode (dirty slides + ladder + lint) for revision cycles, full 8-pass reserved for ship. Also: the numbering isn't cost-ordered — grounding (pass 5, cheap-mechanical) runs after four judged passes, against the rubric file's own "run the measurable checks first and cheaply." And BLOCKED's "the *one* decision needed" reads as one-decision-per-run; if QA surfaces three independent load-bearing questions, batch them into one BLOCKED report or you get serial mornings.

**4.4 "Dumb assembly" is the right *policy* and the wrong *estimate of difficulty*.** Build must invent no content — correct. But pptx assembly is not dumb work:

- **Text fitting.** python-pptx cannot measure text. "Overflow is a build error" therefore requires either heuristic character budgets (likaku's approach — hence its whole `experiences/overflow.md` scar-tissue file) or a render-and-inspect loop (LibreOffice → bbox check). Pick one in the build spec; it shapes worker design.
- **Charts.** The doctrine calls the waterfall "the workhorse chart of professional services" — and python-pptx cannot make one natively (it predates the chartex types; the standard workaround is a stacked bar with an invisible base series). Mekko isn't a native PowerPoint chart at all. So the engine decision is not a detail: native XML charts (editable by the client — which a real engagement deck must be) vs rendered images (pixel-faithful, dead to editing) vs hybrid with an editability flag per exhibit spec. Decide before bower-exhibit's spec format is fixed, because the spec must carry the flag.
- **Concurrency.** Fresh workers "in waves" cannot co-write one .pptx. Workers must emit per-slide intermediates (spec/code fragments) that a single assembler applies. Say so in the build contract.
- **likaku's engine: study, don't adopt.** It's real (3,249-line engine, genuine overflow QA) but CJK-calibrated — its S3 gate *rejects action titles over 40 characters*, while bower's own calibration corpus holds up 100+-character real McKinsey titles as ground truth. Wholesale adoption imports a constraint that fights your central doctrine.
- **Template ingest fork.** Tokens-from-template (readable via python-pptx theme/master: palette, fonts, slide size — feasible) is a different engineering path from *building on* the client template (inheriting masters/layouts/placeholders — what a client actually expects when they say "use our template"). v1 should explicitly pick tokens-only-honored and defer true template inheritance, or scope it in — but decide, because the geometry system (likaku-style absolute boxes) is incompatible with placeholder-driven layouts.

**4.5 Residual title risk.** The design's one unproven bet is that calibration-in-context plus a judged pass beats loki's rules-in-context. Two cheap over-determinations: (a) bower-storyline generates 2–3 candidate ladders and picks (Zelazny's "don't settle for the first idea," applied to titles — deep models are much better at choosing between drafts than at first-drafting to register); (b) QA pass 2's judge is *explicitly instructed to compare against the bank* — "does this ladder read like Part 2's [REAL] titles or like Part 7's gallery?" — not merely to apply the classifier, because the classifier catches defects, not blandness.

---

## 5. Prioritized recommendations

**Must fix before phase 2** (these change what phase 2 builds):

1. **Add the reference-intake/data-inventory step** (a mobius-equivalent skill, or a heavyweight triage step 0): refs → provenance-tagged inventory, xlsx/csv extraction, screenshot transcriptions tagged EST until verified; wire triage's evidence audit, `data/E##.csv`, and QA pass 5 to it; restore a grounding home for non-exhibit numbers ("CSV cell or inventory reference"). *Without this the first real deck stops at exhibit spec.*
2. **Design the revision protocol**: storyline versioning (v2 FROZEN…), a delta-gate lighter than triage, dirty-set propagation across slideplan/exhibits/slides, and the objection-magnitude route table. This is what "revision until good" runs on, and it's currently a shrug.
3. **Decide the engine now**: python-pptx (likely) + native-vs-image chart policy with per-exhibit editability flag + the waterfall workaround + single-assembler worker model + tokens-only template handling for v1. Add an environment preflight (fonts, LibreOffice, renderer) with visible degradation to triage or run.
4. **Produce the per-skill doctrine manifest and policy-resolved distillates**, and fix the four stale spots in the library itself (craft §5 chart-title rule; rules-of-the-road photography ban row; a house-resolved chart matrix so Zelazny's pie row can't reach bower-exhibit; postmortem medium row). Keep the library source-faithful; make the skills load resolved doctrine. Ensure the example bank is in both the composer's and the QA judge's context.
5. **Fix the gate contract**: one canonical dump.md field list shared by grillme and triage; add delivery mode (projected/read/both) as a mandatory field; demote slide budget to optional scope input; grillme's terminal action emits the draft dot-dash and an unresolved-objections section, and bower-storyline hardens rather than re-derives.
6. **Define the STYLE.md schema** with per-density scales; reconcile the likaku fallback (14pt body) against BCG's Key Message floors so a projected deck on fallback style isn't born non-compliant.

**Note for later** (won't change phase 2's architecture, will bite within the first few decks):

7. **Appendix as a first-class slideplan section** — ladder-exempt, Detail density, receives ruled-out options and detail twins.
8. **Speaker notes ownership** — build generates them from connective-out + the McCandless script for presented decks; cold read stays notes-off.
9. **QA ergonomics** — scoped/dirty-slide QA mode for revision cycles; cost-order the passes (mechanical before judged); batch BLOCKED decisions; define the degraded standalone mode for external decks; demote title hard-rule 6 (tense/voice) to judgement.
10. **Title over-determination** — candidate ladders in bower-storyline; bank-anchored judging in QA pass 2; a one-paragraph "house register" note (plain, specific, long-is-fine, no sparkle) distilled from the bank's Part 2 commentary.

**Bottom line.** The direction is right, the library is genuinely good and accurate to its sources, and the three named defects would be fixed by this design — the doctrine debt loki carried is paid. The remaining exposure is concentrated in four seams the architecture hasn't specified: getting real data in, getting revisions through, getting doctrine into context in policy-resolved form, and getting pptx out at quality. All four are designable now, and none of them threatens the seven-skill shape.
