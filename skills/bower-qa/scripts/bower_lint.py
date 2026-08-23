#!/usr/bin/env python3
"""bower-qa pass 0: deterministic lint on fragments + rendered PDF. stdlib only.

Usage: bower_lint.py <project_dir> [--pdf deck.pdf] [--fonts "Georgia,Arial"]
Reads: fragments/S*.json (and G*/X*), data/*.csv, refs/inventory.md.
Findings to stdout as 'SEV-n | S## | lint | message'. Exit 1 if any SEV-1/SEV-2.

Design: style compliance is BY CONSTRUCTION (the assembler owns fonts/sizes/colors),
so this lint guards the construction: fragments must carry no style, no banned chart
types, and every number must have a home. Fonts are verified on the PDF via pdffonts.
"""
import argparse, glob, json, os, re, shutil, subprocess, sys

FORBIDDEN_KEYS = {"font", "fontface", "fontsize", "size", "color", "colour", "fill",
                  "bold", "italic", "x", "y", "w", "h", "align"}
BANNED_EXHIBITS = {"pie", "doughnut", "donut", "pie3d", "bar3d", "gauge"}
SLOP = {"unlock", "leverage", "journey", "robust", "holistic", "empower",
        "transformative", "landscape", "delve", "synergy", "seamless", "best-in-class"}
ARCHETYPES = {"exec-summary", "single-chart", "bullets", "comparison-table", "2x2",
              "bucket-list", "options-matrix", "roadmap", "big-number", "quote",
              "table", "ask", "cover", "agenda", "divider", "closing", "appendix-sep"}

def walk_keys(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield k.lower(), f"{path}.{k}"
            yield from walk_keys(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk_keys(v, f"{path}[{i}]")

def texts_of(obj):
    if isinstance(obj, str): yield obj
    elif isinstance(obj, dict):
        for v in obj.values(): yield from texts_of(v)
    elif isinstance(obj, list):
        for v in obj: yield from texts_of(v)

def numbers_in(text):
    # 35, 3.5, 1,200, 35%, ~20bps -> normalized tokens without separators/sigils
    for m in re.finditer(r"(?<![A-Za-z])\d[\d,]*(?:\.\d+)?", text):
        yield m.group(0).replace(",", "")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("--pdf", default=None)
    ap.add_argument("--fonts", default="Georgia,Arial")
    a = ap.parse_args()
    root = a.project
    findings = []
    def add(sev, sid, msg): findings.append(f"SEV-{sev} | {sid} | lint | {msg}")

    frags = sorted(glob.glob(os.path.join(root, "fragments", "*.json")))
    if not frags:
        add(2, "--", "no fragments/ found - fragment lint skipped (built by hand?)")
    # grounding corpus: all CSV cells + inventory numbers, as normalized strings
    corpus = set()
    for csvf in glob.glob(os.path.join(root, "data", "**", "*.csv"), recursive=True):
        with open(csvf, errors="ignore") as f:
            for tok in re.split(r"[,\s;|]+", f.read()):
                for n in numbers_in(tok): corpus.add(n)
    inv = os.path.join(root, "refs", "inventory.md")
    inventory_present = os.path.isfile(inv)
    if inventory_present:
        with open(inv, errors="ignore") as f:
            for n in numbers_in(f.read()): corpus.add(n)

    seen_ids = set()
    for fp in frags:
        try:
            frag = json.load(open(fp))
        except Exception as e:
            add(1, os.path.basename(fp), f"unparseable JSON: {e}"); continue
        sid = frag.get("id") or os.path.basename(fp).split(".")[0]
        if sid in seen_ids: add(2, sid, "duplicate fragment id")
        seen_ids.add(sid)
        # forbidden style keys — the by-construction guard
        for k, path in walk_keys(frag):
            if k in FORBIDDEN_KEYS:
                add(1, sid, f"forbidden style/geometry key '{path.lstrip('.')}' - styling belongs to STYLE.md + builders")
        arch = (frag.get("archetype") or "").lower()
        if arch and arch not in ARCHETYPES:
            add(3, sid, f"unknown archetype '{arch}'")
        structural = sid.startswith("G") or arch in {"cover", "agenda", "divider", "closing", "appendix-sep"}
        title = (frag.get("title") or "").strip()
        if not structural:
            if not title:
                add(1, sid, "content slide with no title")
            else:
                low = title.lower()
                hits = sorted(w for w in SLOP if re.search(rf"\b{re.escape(w)}\w*", low))
                if hits: add(2, sid, f"slop lexicon in title: {', '.join(hits)}")
                if len(title) > 12 and title.isupper():
                    add(2, sid, "ALL-CAPS title - sentence case only")
                if len(title.split()) > 30:
                    add(3, sid, f"title is {len(title.split())} words - likely >2 lines; split or sharpen")
                # grounding: every number in the title must have a home
                for n in numbers_in(title):
                    if n not in corpus:
                        where = "data CSVs or refs/inventory.md" if inventory_present else "data CSVs (no inventory.md found)"
                        add(1, sid, f"title number '{n}' has no home in {where} - claims need evidence")
                # body numbers: softer
                for t in texts_of(frag.get("blocks", [])):
                    for n in numbers_in(t):
                        if n not in corpus:
                            add(2, sid, f"body number '{n}' has no home - trace it or cut it")
        ex = frag.get("exhibit") or {}
        if ex:
            et = (ex.get("type") or "").lower()
            if et in BANNED_EXHIBITS:
                add(1, sid, f"banned exhibit type '{et}' (house decision #3 / effects ban)")
            csvref = ex.get("csv")
            if csvref and not os.path.isfile(os.path.join(root, csvref)):
                add(1, sid, f"exhibit csv '{csvref}' does not exist")
            ct = (ex.get("chartTitle") or "").strip()
            if ct and title and ct.lower() == title.lower():
                add(3, sid, "chartTitle identical to action title - drop the chart title (dedup rule)")

    # PDF font check
    pdf = a.pdf
    if not pdf:
        cands = glob.glob(os.path.join(root, "*.pdf")) + glob.glob(os.path.join(root, "slides", "*.pdf"))
        pdf = cands[0] if cands else None
    if pdf and os.path.isfile(pdf):
        if shutil.which("pdffonts"):
            out = subprocess.run(["pdffonts", pdf], capture_output=True, text=True).stdout
            allowed = {f.strip().lower() for f in a.fonts.split(",") if f.strip()}
            bad = set()
            for line in out.splitlines()[2:]:
                name = line.split()[0] if line.split() else ""
                base = re.sub(r"^[A-Z]{6}\+", "", name)         # strip subset prefix
                fam = re.split(r"[-,]", base)[0].lower()
                if fam and fam not in {"[none]"} and not any(al in fam for al in allowed):
                    bad.add(base)
            for b in sorted(bad):
                add(2, "--", f"PDF embeds off-style font '{b}' - a substituted font ships a different deck than QA saw")
        else:
            add(3, "--", "pdffonts not on PATH - font verification skipped (install poppler)")
    else:
        add(3, "--", "no rendered PDF found - font verification skipped (run bower_render first)")

    if not findings:
        print("lint clean"); return 0
    for f in sorted(findings): print(f)
    return 1 if any(f.startswith(("SEV-1", "SEV-2")) for f in findings) else 0

if __name__ == "__main__":
    sys.exit(main())
