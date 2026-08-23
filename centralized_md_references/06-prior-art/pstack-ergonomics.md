# pstack Ergonomics — What to Inherit

Source: `github.com/phthomas/pstack` — the user's own toolkit. `PSTACK.md`, `WHY.md`, and the
eleven `ps-*` skills.

The user's brief: *"pstack is because I like the ergonomic of pstack skills. dump → triage →
dormammu → results."* This file extracts the *shape* worth carrying into pstack-bower.

---

## 1. The core loop

```
braindump  ──►  specced product  ──►  built product  ──►  shipping is always yours
```

| Stage | Command | What it does |
|---|---|---|
| Braindump | *(write `dump.md`)* | Three loose headings, no structure required. Messy is the intended input. |
| Front door | `/ps-start` | Gates the dump, interviews on gaps, writes the plan docs and one spec per phase |
| Build (hands-on) | `/ps-build` | One phase, with steering throughout |
| Build (autonomous) | `/ps-dormammu` | Conducts fresh-context workers per phase, in dependency waves |
| Judge | `/ps-review` | Fresh-context panel, weighted by risk |
| Land | `/ps-close` | Verify, review, record, checkpoint, merge — *the merge is yours* |

Session bookends: `/ps-resume` (brief me, propose next action), `/ps-checkpoint` (write the
handoff). Occasional: `/ps-doctor` (probe environment), `/ps-init` (audit docs vs reality after
outside work).

---

## 2. The design principles — verbatim, because they are the actual asset

From `PSTACK.md`:

### Conversation is the primary interface
> "The slash commands are muscle-memory handles; **every skill also triggers on plain intent**
> ('build it', 'ship it', 'run the panel', 'where were we')."

### Clarification is a behavior, not a stage
> "/ps-start asks while drafting; /ps-build asks before coding its phase; /ps-dormammu asks once
> at pre-flight, then assumes-and-records the safe calls and hardstops on the load-bearing ones.
> `[OPEN: ...]` markers in later phases are healthy — **they get answered at the last responsible
> moment, when you know the most.**"

### Tests are not a step
> "Each build gear turns the phase's acceptance criteria into red tests before implementing…
> 'Done' stays executable; you never schedule it."

### Measurement over exhortation
> "Wherever 'write good code' could become a machine check (the gate) or an independent
> fresh-context verdict (the panel), it did. **Advice-in-context is the weakest tool in the
> box**; it's reserved for what can't be measured."

**This is the single most important principle to carry over**, and it maps directly onto the
measured-vs-judged split in `05-conventions/quality-rubrics-and-checklists.md` §1. pstack-loki
already knew it — *"Decks have no compiler, so review manufactures one"* — but under-applied it
to titles and structure, which is exactly where the user reports failure.

### Capabilities live in the environment, never in the core
> "The skills are markdown; reviewers, docs lookup, browser, canvas are providers, named once in
> CLAUDE.md's `## Capabilities` and resolved at runtime. **A missing provider degrades a judge to
> its inline bar — visibly, in the manifest line, never silently.**"

Directly applicable: the pptx engine, the renderer, the image model are all providers. Name them
once; degrade visibly.

### Ceremony scales with risk; models follow task nature
> "The `model-tiers` line in Capabilities routes each spawn by **what the task *is*** (deep =
> judgment, prose craft, security · standard = routine building · mechanical = known fixes and
> re-checks — **never by role name**)."

For a deck toolkit: storyline composition and title craft are *deep* (judgement + prose craft);
slide assembly is *standard*; lint re-checks are *mechanical*.

### No skill where a sentence works
> "A skill exists **only** where there's a gate to enforce, a guardrail to hold unattended, a
> verdict to keep independent, file mechanics to keep consistent, or an environment to make
> visible."

A useful constraint on how many skills pstack-bower should have. pstack-loki has eight; this
principle suggests auditing each against the five justifications.

### Every fact lives where it changes at its own speed
From `WHY.md`:
> "The vision barely moves; the current phase moves constantly. If they share a file, you get
> churn and confusion… **The real point is that I should never have to hold the whole plan in my
> head, because my head will drop it.**"

### Compose through files only
> "The skills compose through files only… **no hidden state.** Stop, inspect, or re-run at any
> point."

### Calibrate
> "Trivial fixes skip the pipeline entirely. The flow is for non-trivial, shippable work."

---

## 3. The `WHY.md` thesis

> "**The agent isn't the bottleneck. The ambiguity is.** An agent told to 'just build it' has to
> guess at a hundred decisions I never made out loud, and it guesses wrong often enough to burn
> the evening. The same agent, handed a clear contract, is startlingly good."
>
> "So the leverage isn't a cleverer prompt. It's **structure — machinery that collapses the
> ambiguity *before* the agent starts typing.**"

For decks, the analogue is exact: an agent told to "make a deck" guesses at the audience, the
ask, the argument, the evidence and the register. Handed a frozen storyline, it's fine. **The
storyline gate is pstack-bower's equivalent of the spec.**

And on the front door:
> "**Start from a brain dump, because that's the honest input.** I don't think in clean specs. I
> think in a messy pile of 'wouldn't it be cool if,' half-remembered constraints, and stack
> preferences. Pretending otherwise just adds a step where I procrastinate."

---

## 4. The dump gate — the pattern to copy

`/ps-start` gates the dump before doing anything:

> The dump is ready when, from it plus any survey, you could answer:
> 1. What is this and why — an outcome, not just a topic?
> 2. What does done look like — at least a fuzzy notion of success?
> 3. What's fixed — the constraints and decisions already made?
>
> "Too thin to interview against? **STOP:** list exactly what's missing as concrete questions to
> answer in dump.md, and tell me to flesh it out and re-run. **Never invent the missing content
> yourself — that defeats the gate.**"

That last clause is the load-bearing one. An agent that fills gaps silently produces a
confident deck about a situation that doesn't exist.

The interview style is also worth copying:
> "Close the gaps interactively — **small batches, most consequential first, each with your
> recommended default and its tradeoff** so I can confirm or redirect… Don't re-ask what the
> dump or the code already answers, and **don't over-interview**: the goal is an unambiguous
> ROADMAP and specs, not a complete requirements document."

**A deck dump gate needs different fields** — the McKinsey Problem Statement Worksheet's six
boxes are the natural analogue, plus audience, ask, budget, data inventory, constraints and
stakes. See `01-storyline/hypothesis-driven-problem-solving.md` §1.

---

## 5. The autonomy dial

From `WHY.md`:
> "**Treat autonomy as a dial.** Some nights I have an hour and want to aim the agent at one
> phase. Some nights I have zero time and want to wake up to a whole product. Some afternoons I
> want to sit in the loop and steer. Same machinery, one dial — **plus hardstops, so when the
> agent hits something it shouldn't decide alone, it stops and tells me instead of barrelling
> on.**"

pstack's realization: `/ps-build` (hands-on, one phase) and `/ps-dormammu` (autonomous,
everything) are the same machinery at two settings, with `continue` as a middle gear.

pstack-loki's realization of the same idea: `loki triage` (attended) then `loki run`
(autonomous), with per-stage manual invocation available. Its framing is good:

> "Long runs suit a headless box: close triage at your desk, execute on a server, find the
> terminal state in the repo at breakfast."

**Keep this.** It is the ergonomic the user named.

---

## 6. Dormammu — the conductor pattern

> "**You are the conductor, not the builder.** Hold only the map, the wave state, and the
> growing report. Each phase is built by a fresh-context worker you spawn… **late phases get the
> same clear head as early ones**, and the run's context never silts up with earlier phases'
> diffs."

Plus: pre-flight resolves open questions in one batch *while you're still at the keyboard*
("launch is the last attended moment — spend it"); explicit stop conditions ("don't thrash,
don't burn the night"); and a morning report ("this is the point").

For decks the mapping is clean: the conductor holds the storyline; each worker builds a slide or
a wave of slides with the *full* storyline in context but none of the other slides' mess.

---

## 7. Artifact discipline

pstack's artifacts, by rate of change:

| Artifact | Rate | Role |
|---|---|---|
| `dump.md` | Scratch — overwrite freely | The braindump inbox |
| `PRODUCT.md` | Slow | Vision, why |
| `CLAUDE.md` | Slow | How you build + Capabilities map |
| `ROADMAP.md` | Medium | The index: phases at a glance |
| `specs/NN-*.md` | Per phase | The contract |
| `STATE.md` | Per session | Where we are, next steps |
| `docs/adr/` | Append-only | Decisions and why |
| `CONTEXT.md` | Grows | The glossary — ubiquitous language, with `_Avoid_:` synonym bans |
| `BACKLOG.md` | As needed | Parked tangents |

Two details worth stealing:
- **`CONTEXT.md` with synonym bans.** For a deck project this is the client's vocabulary — the
  words the audience uses, and the ones to avoid. Directly useful for title register.
- **ADRs, append-only.** A deck has directional decisions too (which storyline pattern, which
  audience, what we decided not to argue). Recording them prevents re-litigation mid-build.
- **"A processed dump is spent — the specs become the record."**

---

## 8. Changing the plan — match the fix to the magnitude

> - A detail inside a phase → just say it while building
> - A phase's goal, order, or existence → `/ps-spec`
> - The product direction → `/ps-adr` the why, then `/ps-spec` the new phases
> - Docs and code disagree → `/ps-init`
> - A different product → new repo

The deck analogue: a wording fix is a sentence; a slide's existence is a storyline delta; the
governing thought changing is a re-compose. **Fixes route to the level that owns them** — the
same principle as pstack-loki's "fixes route upstream".

---

## 9. What pstack-bower should inherit, concretely

| Inherit | Why |
|---|---|
| **`dump.md` as the front door** | The honest input. Already the user's muscle memory. |
| **A real dump gate that refuses rather than invents** | The single highest-value guardrail |
| **Interview in small batches, recommended default + tradeoff each** | Fast, low-friction, keeps the user in charge |
| **One decisive attended gate, then autonomy** | The named ergonomic; matches where judgement actually is |
| **Measurement over exhortation** | The fix for bland titles is a lint and a judge, not more adjectives in a prompt |
| **Conductor/fresh-worker for the build** | Late slides get the same clear head as early ones |
| **Compose through files, no hidden state** | Stop, inspect, re-run at any point |
| **Capabilities named once, degrade visibly** | pptx engine, renderer, image model are providers |
| **Facts stored by rate of change** | Storyline (frozen) vs slide state (churns) vs session state |
| **Plain-intent triggers alongside slash commands** | "review the deck", "where were we" |
| **No skill where a sentence works** | Keeps the surface small |
| **The morning report** | For an autonomous run, the report *is* the product |

## Cross-references
- What went wrong in the deck-specific attempt → `06-prior-art/pstack-loki-postmortem.md`
- Where the gates should sit → `05-conventions/quality-rubrics-and-checklists.md` §9
- The synthesis → `07-synthesis/design-brief-pstack-bower.md`
