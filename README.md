# pstack-bower

> MBB rigor for the argument, pstack ergonomics for the drive.
> Eight skills that turn an agreed storyline into a consulting-grade `.pptx` —
> grill → dump → triage → run.

Named for Marvin Bower, who made consulting a profession. The idea: Bower works alongside you —
a demanding colleague who holds the standard, not a slide generator.

## Why this exists

Its predecessor ([pstack-loki](https://github.com/phthomas/pstack-loki)) had the right
architecture and thin doctrine: titles passed the rules and still read bland, one-slide-one-
message was never enforced, and a fixed five-act arc deferred the answer to slide 12. bower
keeps the machinery and replaces the doctrine:

- **Pyramid structure, always.** Governing thought on slide 2, Key Line as the sections,
  SCQA as a one-slide introduction — never the deck's architecture.
- **Seven storyline patterns** (Stanley & Castles) chosen to fit the situation, not one arc
  forced onto everything.
- **Titles calibrated, not just ruled.** A real-deck example bank sits in context at
  composition AND at judgement; blank assertions route upstream for more thinking, never to a
  rewriter.
- **A real design standard** — BCG's Key Message/Detail density model, hard type floors, the
  emphasis ladder, grey-first colour — resolved into house policy (pie charts banned, chart
  titles always carry the so-what, likaku fallback style).
- **Everything QA'd**: eight passes from mechanical lint to a notes-off cold read of the
  rendered pixels.

## The skills

| Skill | Job |
|---|---|
| `bower-grillme` | Interrogate the thinking until a storyline holds; write `dump.md` |
| `bower-intake` | Sources → provenance-tagged `[D#]` registry (grillme can trigger it mid-conversation) |
| `bower-triage` | Dump gate · style resolution · preflight · orchestrates · holds the ONE human gate |
| `bower-storyline` | Harden the agreed dot-dash into `storyline.md` + `slideplan.md` |
| `bower-exhibit` | One spec per chart before any pixel — form, data contract, checklist |
| `bower-build` | Frozen artifacts → `deck.pptx`; fragments + one assembler; overflow is an error |
| `bower-qa` | Eight passes; findings route upstream; claims escalate, renders auto-fix |
| `bower-run` | Autonomous to SHIPPED or BLOCKED (decisions batched); the morning report |

## The flow

```
/bower-grillme <topic> ──► argument agreed ──► "create dump.md"
   ▲                                                │  you review & edit dump.md
   └── /bower-intake ◄── files land                 ▼
                                             /bower-triage ──► ladder · specs · STYLE · packet
                                                    │  you read 2 minutes, object, say "closed"
                                                    ▼
                                              /bower-run ──► waves → 8-pass QA → SHIPPED / BLOCKED
                                                    │
                                  revision: /bower-triage <objection> — routes by magnitude
```

Slash commands **start** stages (deterministic — no intent-matching). Inside a running stage
you reply in words: answering the grilling, `create dump.md`, objections at the gate, `closed`,
and answers to a BLOCKED report. Plain-intent phrases ("grill me", "qa") still work as a
fallback; the slash is the precise handle.

## Install

```bash
cp -r skills/* ~/.claude/skills/        # install all eight - they cross-reference
```

Requirements (checked by triage's preflight, degradation always visible):
Node + **pptxgenjs** (the writer) · LibreOffice (`soffice`) · poppler (`pdftoppm`, `pdffonts`)
· python3 (stdlib only — the QA and theme scripts) · Georgia + Arial (or your house-template
fonts). Drop a client template in `refs/` and triage derives the style from it automatically:
exact palette and fonts from its theme XML, accent usage and geometry from its rendered pages —
and QA later verifies your deck against those same rendered pages.

```bash
# Arch/CachyOS        sudo pacman -S libreoffice-fresh poppler nodejs npm
# Debian/Ubuntu       sudo apt install libreoffice poppler-utils nodejs npm
npm install -g pptxgenjs        # or per-project
```

## Quick start

```bash
mkdir q3-deck && cd q3-deck
cp ~/materials/*.xlsx refs/       # optional, any time - grillme ingests them live
claude
> /bower-grillme Q3 cost review for the exec committee
  … the argument gets pressure-tested; drop files whenever …
> create dump.md                  # grillme's terminal action — then edit the file yourself
> /bower-triage
  … read the ladder as a skeptic, object in plain words, then:
> closed
> /bower-run
  … SHIPPED: deck.pptx + qa.md + the morning report
```

## Command reference

| Command | Does |
|---|---|
| `/bower-grillme <topic>` | Start the interrogation; drop files any time (it triggers intake) |
| `/bower-intake` | Ingest `refs/` → manifest + `[D#]` registry, standalone |
| `/bower-triage` | Gate a reviewed dump: compose the blueprint, print the packet, freeze on "closed" |
| `/bower-triage <objection>` | **The revision front door** — classifies the magnitude, runs the matching delta |
| `/bower-storyline` | Re-test / re-harden the ladder ("the flow is broken") |
| `/bower-exhibit` | (Re)spec the exhibits |
| `/bower-build` | Full build from frozen artifacts |
| `/bower-build S07 S12` | Scoped rebuild of named slides |
| `/bower-qa` | Scoped review (dirty slides + ladder + lint) |
| `/bower-qa ship` | All eight passes — run before anything leaves the building |
| `/bower-run` | Autonomous to SHIPPED / BLOCKED |

Revision goes through one deterministic door: **`/bower-triage <objection in plain words>`**.
Triage classifies the magnitude and routes it — *"label overlaps on S07"* → rebuild that slide,
no gate · *"move S09 before S07"* → slideplan delta, one-message gate · *"S07 overclaims — the
data says 32"* → storyline version bump, re-gate that leg · *"the audience is actually the
board"* → back to `/bower-grillme`. You never pick the route; stating the problem precisely is
the whole interface.

## House policy (the short version)

Exec summary on slide 2, always · one message per slide, linted · chart titles state the
so-what · **no pie or doughnut charts** · story sets the slide count · answer first, pyramid
always · dot-dash storyline is the source of truth · native charts wherever PowerPoint has the
type (your client can edit their own deck) · no generated imagery · photography per BCG's
curation rules, never near a chart.

Full policy with the reasoning and the sources that disagree:
`centralized_md_references/05-conventions/contested-points.md`.

## Lineage

Barbara Minto (pyramid, SCQA) · Gene Zelazny (charts, storyboards) · Stanley & Castles (the
seven patterns) · the McKinsey problem-solving staff paper (dot-dash) · BCG's format guide
(density, colour) · Knaflic (declutter) · Dave McKinsey's USPS teardowns (the [REAL] title
bank) · pstack (the ergonomics) · pstack-loki (the machinery worth keeping).

Not affiliated with or endorsed by McKinsey, Bain, BCG or Accenture — this encodes published
practice, nothing more.

## License

MIT.
