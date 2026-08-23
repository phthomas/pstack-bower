#!/usr/bin/env python3
"""Render a .pptx to per-slide PNGs: soffice -> PDF -> pdftoppm.

Usage: bower_render.py deck.pptx outdir [--dpi 120]
Emits outdir/S01.png ... plus renders.txt manifest. Exit 2 on missing tools.
"""
import argparse, glob, os, shutil, subprocess, sys, tempfile

def die(msg, code=2):
    print(f"RENDER FAIL: {msg}", file=sys.stderr); sys.exit(code)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pptx"); ap.add_argument("outdir")
    ap.add_argument("--dpi", type=int, default=120)
    a = ap.parse_args()

    if not os.path.isfile(a.pptx): die(f"not found: {a.pptx}")
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice: die("LibreOffice (soffice) not on PATH — preflight should have caught this")
    if not shutil.which("pdftoppm"): die("pdftoppm not on PATH (install poppler)")

    os.makedirs(a.outdir, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        # Isolated profile: parallel-safe and immune to a locked user profile.
        r = subprocess.run(
            [soffice, "--headless", f"-env:UserInstallation=file://{td}/lo",
             "--convert-to", "pdf", "--outdir", td, os.path.abspath(a.pptx)],
            capture_output=True, text=True, timeout=300)
        pdfs = glob.glob(os.path.join(td, "*.pdf"))
        if not pdfs:
            die(f"soffice produced no PDF.\nstdout: {r.stdout}\nstderr: {r.stderr}")
        shutil.copy(pdfs[0], os.path.join(a.outdir, "deck.pdf"))  # kept for pdffonts (lint)
        subprocess.run(["pdftoppm", "-png", "-r", str(a.dpi), pdfs[0],
                        os.path.join(td, "slide")], check=True, timeout=300)
        pages = sorted(glob.glob(os.path.join(td, "slide-*.png")))
        if not pages: die("pdftoppm produced no pages")
        width = max(2, len(str(len(pages))))
        names = []
        for i, p in enumerate(pages, 1):
            name = f"S{str(i).zfill(width)}.png"
            shutil.copy(p, os.path.join(a.outdir, name)); names.append(name)
    with open(os.path.join(a.outdir, "renders.txt"), "w") as f:
        f.write("\n".join(names) + "\n")
    print(f"rendered {len(names)} slides -> {a.outdir}/ (dpi {a.dpi})")

if __name__ == "__main__":
    main()
