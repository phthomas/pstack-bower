# Action Title Examples Bank

A calibration corpus. Rules describe the target; examples locate it. Sources are marked:

- **[REAL]** — verbatim from a real MBB/Accenture deck, as reproduced in Dave McKinsey's
  teardowns of the USPS engagement.
- **[BOOK]** — verbatim from one of the reference books.
- **[SKILL]** — from a prior-art skill repository.
- **[DERIVED]** — constructed here from the corpus's rules and worked scenarios, to fill gaps
  in coverage. Not from a real deck; use as illustration, not as evidence about firm practice.

---

## Part 1 — Before / after pairs

The core calibration device: same content, wrong title vs right title.

### Topic label → claim

| Topic title (bad) | Action title (good) | Src |
|---|---|---|
| Market Overview | The market is consolidating around three players, who now hold 71% share | [SKILL] |
| Customer Segments | Two of our four segments generate 85% of profit | [SKILL] |
| Cost Analysis | Procurement and logistics together account for 60% of controllable costs | [SKILL] |
| Recommendation | We recommend exiting Segment C and reinvesting in Enterprise within 12 months | [SKILL] |
| Product and Service Initiatives | The "Actions within Postal Service control" case includes product and service initiatives above the baseline to grow volume | [REAL] |
| Deposit Overview | Deposit growth stalled at 2% while funding costs rose 60bps | [SKILL] |
| NIM Trends | NIM compresses ~35bps by Q4 unless the mix shifts | [SKILL] |
| CASA Campaign Results | CASA campaigns alone recovered only a third of past gaps | [SKILL] |
| RBPE Proposal | Repricing the top decile via RBPE protects ~20bps at low attrition risk | [SKILL] |
| Q2 Performance | One-off recoveries drove the entire Q2 beat | [SKILL] |
| Revenue Trends | Revenue grew 23% YoY, driven by enterprise | [SKILL] |
| EBIT margin, % | EBIT margin declines despite growth | [SKILL] |
| Company Sales Trend | Sales have risen steadily since January | [BOOK] |
| Productivity by Region | *(pick the message — Zelazny's point is that the topic title hides it)* | [BOOK] |
| Profits by Region | North generates the smallest share of profits | [BOOK] |
| Number of Contracts | In August, the number of contracts reached its highest point | [BOOK] |
| Relationship of Compensation to Profitability | CEO compensation does not vary with size of company | [BOOK] |
| International Post Diversification (I) / (II) | Diversification is a global phenomenon | [REAL] |

### Question title → statement title

| Question (avoid) | Statement (prefer) | Src |
|---|---|---|
| What actions within USPS control can increase volume? | The "Actions within Postal Service control" case includes product and service initiatives above the baseline to grow volume | [REAL] |

### Vague verb → end product (Minto Exhibit 30)

| What was said | What was meant | Src |
|---|---|---|
| Strengthen regional effectiveness | Assign planning responsibility to the regions | [BOOK] |
| Reduce accounts receivable | Establish a system for following up overdue accounts | [BOOK] |
| Review management processes | Determine whether management processes need to be revised | [BOOK] |
| Improve financial reporting | Install a system that gives early notice of change | [BOOK] |
| Tackle strategic issues | Define a clear long-term strategy | [BOOK] |
| Redeploy manpower resources | Place people in positions of comparable responsibility | [BOOK] |

### Blank assertion → completed thinking

| Blank | Completed | Src |
|---|---|---|
| The company has two organization problems | The major organizational problem you face is your inability to delegate authority | [BOOK] |
| The company should have three objectives | *(state what the three objectives jointly achieve)* | [BOOK] |
| We recommend five changes | *(state the effect of making all five)* | [BOOK] |
| John Wain says he is well placed to write this biography for three reasons | John Wain says he is well placed to write this biography of Samuel Johnson because he and Johnson are essentially the same kind of people | [BOOK] |
| There are three options | Of the four options, Black Inc. provides the best solution for our needs | [BOOK] |
| Planning | The planning system needs to become lean | [BOOK] |

### Fact → insight (summarise → synthesise)

| Fact (summary) | Insight (synthesis) | Src |
|---|---|---|
| We win 40% of negotiations | Negotiation conversion declined from 55% to 40%, likely driven by recent scaling of the sales team | [SKILL] |
| All Australian surfboards are great to surf with | When choosing a new surfboard, you must choose an Australian board as they are the best | [BOOK] |
| Revenue is doing well | Revenue grew 23% YoY, driven by enterprise expansion | [SKILL] |

---

## Part 2 — Real deck titles, verbatim

From the USPS engagement decks (McKinsey, BCG, Accenture), as reproduced in Dave McKinsey's
teardowns. These are the closest thing in the corpus to ground truth about how the firms
actually write.

**McKinsey:**
- "USPS is experiencing unprecedented losses"
- "Losses have been driven by volume declines, RHB pre-funding requirements, and limitations on cost savings"
- "The 'Actions within Postal Service control' case includes product and service initiatives above the baseline to grow volume"

**Accenture:**
- "Lower cost competitors are gaining share from legacy postal operators in liberalized markets…"
- "… as the elimination of the postal monopoly is likely to exacerbate the structural decline of mail volumes"
- *(suggested improvement to a repeated title)* "Diversification is a Global Phenomenon"
- *(cited as an excellent title, though wrong for its position)* "The USPS Is Under-Diversified Relative to Global Benchmarks"

**Note the register.** Real firm titles are plainer and longer than skill-generated titles tend
to be. They do not sparkle. They are specific, complete sentences that assert one thing. Several
run well past ten words. None contain a metaphor.

### Presentation-level titles (real McKinsey)
- "Sustaining Quality and Operational Excellence"
- "Capturing the Full Electricity Efficiency Potential of the U.K."
- "Evolving USSA's Alpine Domestic Development System in Partnership with Clubs"
- "Quantum Leap – What Will It Take to Double Serbia's Economic Growth in the Next Decade?"
- *(critiqued as a weak "what" title)* "USPS Future Business Model"
- *(the SMART repair)* "Restoring the USPS to Profitability by 2020"

---

## Part 3 — Governing thoughts

The apex sentence. Held to a higher bar than any other title.

### Bad
| Governing thought | Why it fails | Src |
|---|---|---|
| We should think about international expansion | Vague; not falsifiable | [SKILL] |
| Our growth strategy | Topic, not a thought | [SKILL] |
| Customers want more features | Insight, but no implication for action | [SKILL] |
| Offer $500,000 for a share of the Swell Boards start-up | Incomplete; no owner, no stake, no why, no horizon | [BOOK] |
| We should be concerned about meeting the new standards | Obvious, not insightful | [BOOK] |
| We should take steps to meet the new standards | Obvious | [BOOK] |

### Good
| Governing thought | Src |
|---|---|
| Acme should enter Germany and France in 2026 via direct sales, funded by exiting the SMB tier | [SKILL] |
| The decline in Q3 margin is caused by raw material costs, not pricing — we should hedge, not raise prices | [SKILL] |
| We can hit our 2027 EBITDA target by capturing three identified cost-out opportunities worth $42M | [SKILL] |
| SurfCo should offer $500,000 for 51% of the Swell Boards start-up to regain market share from competitors within the next two years | [BOOK] |
| Coonawarra Corp should invest in Black's intelligent cloud-based storage solution | [BOOK] |
| Pioneer needs to acquire Shanghai Bank and invest $60 million in building capabilities to establish a winning position | [BOOK] |
| Acme should reposition around premium segments and divest the value tier within 12 months | [SKILL] |

---

## Part 4 — Complete title ladders

Titles are only assessable in sequence. These are full ladders, with the connective marked.

### Ladder A — passing (banking / NIM) [SKILL]
```
S04  Deposit growth stalled at 2% while funding costs rose 60bps
        ↓ but
S05  NIM compresses ~35bps by Q4 unless the mix shifts
        ↓ but
S06  CASA campaigns alone recovered only a third of past gaps
        ↓ therefore
S07  Repricing the top decile via RBPE protects ~20bps at low attrition risk
```

### Ladder A′ — the same content, failing
```
S04  Deposit Overview
        ↓ and then
S05  NIM Trends
        ↓ and then
S06  CASA Campaign Results
        ↓ and then
S07  RBPE Proposal
```
Every title is individually defensible. The sequence argues nothing. **This is precisely what
per-slide title generation produces from an unordered dump.**

### Ladder B — question-chain, real deck [REAL]
```
S02  USPS is experiencing unprecedented losses
        ↓ reader asks: "why?"
S03  Losses have been driven by volume declines, RHB pre-funding requirements,
     and limitations on cost savings
        ↓ reader asks: "what's the impact of each?"
     (waterfall chart decomposing the decline in net income 2006 → 2009)
```

### Ladder C — To B or Not to B, full storyline → memo [BOOK]
```
GOVERNING  Coonawarra Corp should invest in Black's intelligent cloud-based storage solution
  ├─ We investigated four options to deliver intelligent cloud-based data storage capabilities
  │     ├─ Option 1 – Outsourcing to Yellow Company is possible but risky
  │     ├─ Option 2 – Purchasing tools and technology from Pink Corporation is overly complicated
  │     ├─ Option 3 – Insourcing to our internal IT team is possible, but expensive and risky
  │     └─ Option 4 – Outsourcing to Black Inc. meets all criteria
  ├─ Of the four options, Black Inc. provides the best solution for our needs
  └─ As a result, we recommend undertaking a 10-week program to initiate the migration to Black
```
Note that even the *option sub-headings* are verdicts, not labels. "Option 1 – Yellow Company"
would be a topic label; "Option 1 – Outsourcing to Yellow Company is possible but risky" is an
action title. Discipline holds all the way down.

### Ladder D — ellipsis span [REAL / BOOK]
```
S12  USPS should pursue volume boosting initiatives…
S13  … by taking critical actions leading to ~$2 billion of incremental net income in 2020
```

### Ladder E — Close the Gap, agile stand-up (verbal) [BOOK]
```
So what   We need Mary and Jane to help Fred fix XYZ fields so the model can be delivered by Friday
  ├─ S:  For the model to be delivered by Friday, we need all XYZ fields complete
  ├─ C:  But when we were testing last night we found three of the fields had corrupted
  └─ T:  So Mary and Jane down tools and help Fred fix these three fields straight away
```

### Ladder F — Traffic Light, verbal update [BOOK]
```
So what   We are changing the way we think and communicate about maintenance tasks to cut the
          risk of downtime, such as last month's major shutdown
  ├─ We are now successfully prioritising maintenance tasks according to the impact on
  │  production rather than the time when the task was logged
  ├─ We are continuing to improve communication between shift supervisors and the maintenance
  │  team by ensuring they discuss priorities at the start of each shift
  └─ We are working towards operators consistently telling supervisors as soon as they see a
     potential problem rather than waiting until something breaks
```
Note the parallel grammar — all three begin "We are [verb]-ing", all three state a behaviour
change and its object. That parallelism is Minto rule 2 made visible.

---

## Part 5 — The improvement ladder, worked

Climb every title to rung 4. [SKILL]

| Rung | Example |
|---|---|
| 1. Topic label | Market dynamics |
| 2. Generic claim | Focus on expansion to attractive geographies |
| 3. Specific but wordy | We should prioritise Asia Pacific and North America because they have better margins and growth and are large markets |
| 4. Concise quantified insight | Asia Pacific and North America prioritized due to margins, growth and 100+ EUR mn market size |

---

## Part 6 — Titles by storyline role [DERIVED]

Constructed to show how the title register shifts with the box's job in a Stanley & Castles
pattern. Scenario: a mid-market lender whose cost-to-income has drifted.

### Houston, We Have a Problem
```
So what     Cost-to-income reaches 62% by FY27 unless we consolidate origination;
            consolidating recovers 7pts for a $9M one-off
  ├─ S:  Cost-to-income rose from 51% to 58% over eight quarters while revenue was flat
  ├─ C:  Six of the seven points came from duplicated origination across three channels
  └─ T:  Consolidating origination onto one platform recovers 7pts by FY27 for a $9M one-off
```

### Watch Out (same firm, different situation)
```
So what     Protecting the FY27 margin plan needs three risk actions approved this quarter
  ├─ S:  The channel programme delivered 7pts of cost-to-income improvement, ahead of plan
  ├─ C:  But attrition in the top origination decile has doubled since the platform migration,
  │      which would give back 4 of those 7 points by FY27
  └─ T:  Approve the retention package, the migration pause, and the Q3 re-baseline
```

### Close the Gap
```
So what     Meeting the FY27 55% cost-to-income target needs $14M of the $22M identified cost-out
  ├─ S:  The FY27 plan requires cost-to-income of 55%, a 3pt improvement on today
  ├─ C:  Current initiatives deliver 1.2pts, leaving a 1.8pt gap worth $14M
  └─ T:  Three of the seven identified opportunities close the gap; approve them by Q3
```

Observe: **the So what carries both the action and its reason in all three deductive patterns.**
That is a pattern requirement, not a stylistic preference.

---

## Part 7 — Anti-pattern gallery

Titles that look professional and say nothing. Recognising these is most of the skill. [DERIVED
except where marked]

| Anti-title | Defect |
|---|---|
| Key Considerations for the Transformation | Intellectually blank assertion |
| Strategic Priorities Overview | Topic label + blank |
| We Conducted 15 Stakeholder Interviews | Process narration |
| Managing Risk Is Important for Success [BOOK-adjacent] | General truth |
| All Divisions Fail to Follow Best Practices [SKILL] | Absolute, no room for outliers |
| Significant Pressure on Margins [SKILL] | Unquantified |
| Unlocking Value Across the Portfolio | Slop lexicon |
| Our Journey to Operational Excellence | Slop + no claim |
| The Market Landscape Is Evolving Rapidly | General truth + slop |
| Revenue Grew 23% and Costs Rose 8% and Headcount Fell 4% | Compound — three claims |
| It Might Be Worth Considering an Exit [SKILL] | Passive, no recommendation |
| Q3 Results | Topic label |
| Next Steps | Topic label (extremely common; still wrong) |
| Appendix | *(legitimate — divider slides are exempt)* |

---

## Part 8 — What exempt slides look like

Not every slide carries an action title. Do not force one onto:

- **Title / cover slide** — deck title, client, date, author.
- **Section dividers** — section name and, optionally, a one-line promise of the section.
- **Agenda slides** — Dave McKinsey tip 11: *"Keep agenda slide titles short and sweet so they
  can be ignored."* Unlike content slides, agenda titles are deliberately visually skippable.
  Tip 14 is the exception worth applying: **start agenda items with action verbs** to signal
  which mental mode you want the audience in.
- **Appendix separators.**
- **Quote slides** — the quote is the message.

Everything else gets an action title. No exceptions for "the chart explains it".

## Cross-references
- Rules and diagnosis → `02-action-titles/action-title-craft.md`
- Ladder tests → `01-storyline/storyline-quality-tests.md`
- Patterns these ladders instantiate → `01-storyline/seven-storyline-patterns.md`
