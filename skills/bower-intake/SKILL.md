---
name: bower-intake
description: Ingest source materials (xlsx, csv, prior decks, PDFs, screenshots, docs) into a provenance-tagged, citable data inventory for a presentation project. Use when the user says "ingest these files", "read these refs", drops files into refs/, or when bower-grillme or bower-triage needs the [D#] registry built or refreshed. Every number that later appears on a slide must trace back to what this skill produces.
---

# bower-intake

Turn a pile of source files into evidence with provenance. Downstream, `bower-exhibit` refuses
any number without a home here, and QA pass 5 traces every slide number back to this registry.

## Procedure

1. **Inventory `refs/`.** List every file. For each, assign a role — ask only when ambiguous:
   - **material** — carries claims and numbers for THIS story (reports, memos, prior analyses)
   - **data** — spreadsheets and extracts; the numeric backbone
   - **exemplar** — "learn how we present": register, rhythm, anatomy. Never copied, only
     imitated — its diseases (topic titles) stay banned
   - **template** — a style-token source; flag it for bower-triage's STYLE.md derivation
   One file can hold two roles; record both.
2. **Write `refs/manifest.md`** — one entry per source:
   `<file> | role(s) | origin/owner | as-of date | notes`
3. **Extract data.**
   - xlsx/csv → `data/src/<slug>.csv`, one table per file, with a provenance header comment
     (`# source: <file>!<sheet>!<range>, as-of <date>`).
   - Tables inside PDFs and screenshots → transcribe to `data/src/`, **tagged EST until
     verified against a real file** — transcription is not provenance.
4. **Write `refs/inventory.md`** — the [D#] registry. One line per citable fact or number:

   ```
   [D1] FACT  FY25 cost-to-income 58%          — src/finance-pack.csv:B14 (as-of 2026-06)
   [D2] EST   Attrition in top decile ~2x      — transcribed from board-pack p.12 (UNVERIFIED)
   [D3] JUDG  Client unwilling to divest       — per CFO conversation 2026-08-02
   ```

   Tags: **FACT** (traces to a real cell/document) · **EST** (estimate or transcription —
   method/source noted, verify when possible) · **JUDG** (judgement — disclosed as such).
5. **Report**: sources by role, [D#] count by tag, UNVERIFIED items, and what looks missing
   for the story at hand (grillme and triage act on this).

## Re-runs are diffs

Idempotent. On a changed `refs/`, re-run and report: new [D#]s · changed values (**flag any
[D#] already cited by a frozen storyline — that is a claim-level event, route per the revision
protocol**) · stale as-of dates.

## Rules

- Never invent, estimate, or "reasonably assume" a value. A gap is reported, not filled.
- Never regenerate or retouch real photography or brand assets; place as-is or not at all.
- Numbers keep their basis (currency, FX, fiscal vs calendar) attached from the moment of
  extraction — ambiguity here becomes a lying axis later.
- The registry is append-mostly: a corrected value keeps its [D#] with the correction noted.
