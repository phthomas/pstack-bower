# INSTALL.md — agent runbook: install & initialize pstack-bower in a deck folder

**Audience: an AI agent** (Claude Code or similar) running in a new or empty project folder.
Follow this document top to bottom. The outcome is a deck workspace with the eight `bower-*`
skills installed **project-level** (`./.claude/skills/`, never `~/.claude/skills/`), scaffolded
and verified — ready for the user to start with `/bower-grillme <topic>`.

The human typically kicks this off with something like:

> Install pstack-bower into this folder, project-level, per
> https://github.com/phthomas/pstack-bower/blob/main/INSTALL.md

## Ground rules

1. **Project-level only.** Everything you install lands inside this folder. Do not write to
   `~/.claude/`, and do not modify anything outside the current directory except the temporary
   clone in step 1.
2. **Install ends with a report, not a deck.** Do NOT invoke any bower skill, do NOT create
   dump.md, do NOT start a storyline. The user brings the topic.
3. **Degradation is visible, never silent.** A missing dependency is reported in the readiness
   table, not papered over — and it does not abort the install (triage re-checks later).
4. This folder will hold **client material**. Do not `git init`, publish, or push anything
   from it unless the user explicitly asks.

## Step 1 — fetch the repo (it is private; auth may be needed)

```bash
TMP=$(mktemp -d)
gh repo clone phthomas/pstack-bower "$TMP/pstack-bower" -- --depth 1 \
  || git clone --depth 1 https://github.com/phthomas/pstack-bower.git "$TMP/pstack-bower" \
  || git clone --depth 1 git@github.com:phthomas/pstack-bower.git "$TMP/pstack-bower"
```

If all three fail with an auth error: **STOP and tell the user** the repo is private and this
machine isn't authenticated — ask them to run `gh auth login` (or set up SSH keys) and re-invoke
you. Do not retry with invented credentials or fall back to a different repo.

## Step 2 — install the skills, project-level and idempotent

```bash
mkdir -p .claude/skills
rm -rf .claude/skills/bower-*                      # idempotent: re-running == updating
cp -r "$TMP/pstack-bower/skills/"* .claude/skills/
ls .claude/skills | grep -c '^bower-'              # must print 8
```

Keep the eight directories as **siblings** — the skills cross-reference each other by relative
path (`../bower-storyline/references/…`). Never install a subset.

## Step 3 — scaffold the workspace

```bash
mkdir -p refs
```

Then write `./CLAUDE.md` with exactly this content (substitute the folder name):

```markdown
# <folder-name> — pstack-bower deck project

Toolkit: pstack-bower (github.com/phthomas/pstack-bower), installed project-level in
.claude/skills/. To update it, re-run the repo's INSTALL.md.

Workflow: /bower-grillme <topic> → user edits dump.md → /bower-triage → "closed" →
/bower-run → revise via /bower-triage <objection>. Slash commands start stages; replies
inside a stage ("closed", objections, grilling answers) are plain words.

Artifacts, by stage: dump.md · refs/ (sources; manifest.md + inventory.md after intake) ·
storyline.md (FROZEN — titles immutable within a version) · slideplan.md · STYLE.md ·
exhibits/ · data/ · fragments/ · deck.pptx · qa.md · TIMELINE.md.

Standing rules: never edit deck.pptx by hand mid-loop (route changes through
/bower-triage); never restyle by hand (STYLE.md owns style); client material may be
confidential — do not commit or push this folder unless the user explicitly asks.
```

If a `CLAUDE.md` already exists in the folder, append the block instead of overwriting, under
a `## pstack-bower` heading.

## Step 4 — pptxgenjs, local to the project

```bash
node -e "require('pptxgenjs')" 2>/dev/null && echo "pptxgenjs: available" || {
  [ -f package.json ] || npm init -y >/dev/null
  npm install pptxgenjs
}
```

A local `node_modules/` in a deck folder is fine — it keeps the install self-contained, which
is the point of project-level.

## Step 5 — preflight (report, don't block)

Run each check; collect results:

```bash
node --version                                   # writer runtime
node -e "require('pptxgenjs')"                   # the writer
soffice --version || libreoffice --version       # renderer (LibreOffice)
pdftoppm -v                                      # PDF → PNG (poppler)
pdffonts -v                                      # font verification (poppler)
python3 --version                                # QA + theme scripts (stdlib only)
fc-list 2>/dev/null | grep -ci "georgia"         # fallback-style fonts…
fc-list 2>/dev/null | grep -ci "arial"           # …only needed if no client template
```

Missing items: report them with the matching fix (`npm install pptxgenjs` ·
`sudo pacman -S libreoffice-fresh poppler` / `sudo apt install libreoffice poppler-utils` ·
MS core fonts package for Georgia/Arial). Font absence matters less if the user will supply a
client template — say so.

## Step 6 — clean up and verify

```bash
rm -rf "$TMP"
ls .claude/skills/bower-storyline/references/title-bank.md \
   .claude/skills/bower-qa/scripts/bower_lint.py \
   .claude/skills/bower-triage/scripts/bower_theme.py     # all three must exist
python3 -m py_compile .claude/skills/bower-qa/scripts/*.py \
   .claude/skills/bower-triage/scripts/*.py && echo "scripts OK"
```

## Step 7 — the readiness report

End your turn with exactly this shape, then stop:

```
pstack-bower installed (project-level).

| Check                 | Status |
|-----------------------|--------|
| 8 skills in .claude/skills | ✓ / ✗ |
| scripts compile       | ✓ / ✗  |
| node + pptxgenjs      | ✓ / missing → <fix> |
| soffice               | ✓ / missing → <fix> |
| pdftoppm / pdffonts   | ✓ / missing → <fix> |
| python3               | ✓ / ✗  |
| Georgia / Arial       | ✓ / missing (irrelevant if a client template is supplied) |

Workspace: refs/ created · CLAUDE.md written.
Drop source materials and any client template into refs/, then start with:
  /bower-grillme <your topic>
```

**Then wait.** The user brings the topic; the deck is theirs to start.
