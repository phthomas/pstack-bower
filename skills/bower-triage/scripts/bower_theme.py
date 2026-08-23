#!/usr/bin/env python3
"""Read exact style tokens from a .pptx template - stdlib only (a pptx is a zip).

Usage: bower_theme.py template.pptx
Prints the theme colour scheme (hex), major/minor fonts, and slide size - the
deterministic half of STYLE.md derivation. The other half (which colour is the
accent, title treatment, geometry, register) comes from LOOKING at the rendered
template pages (bower_render.py) - usage is visual, and pixels are the truth.
"""
import sys, zipfile, xml.etree.ElementTree as ET

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
ROLES = {"dk1": "text (dark 1)", "lt1": "background (light 1)", "dk2": "text (dark 2)",
         "lt2": "background (light 2)", "accent1": "accent 1", "accent2": "accent 2",
         "accent3": "accent 3", "accent4": "accent 4", "accent5": "accent 5",
         "accent6": "accent 6", "hlink": "hyperlink", "folHlink": "followed link"}

def main():
    if len(sys.argv) != 2:
        print(__doc__.strip(), file=sys.stderr); return 2
    try:
        z = zipfile.ZipFile(sys.argv[1])
    except Exception as e:
        print(f"THEME FAIL: cannot open as pptx/zip: {e}", file=sys.stderr); return 1

    themes = sorted(n for n in z.namelist()
                    if n.startswith("ppt/theme/") and n.endswith(".xml"))
    if not themes:
        print("THEME FAIL: no ppt/theme/*.xml - not a PowerPoint file?", file=sys.stderr)
        return 1
    root = ET.fromstring(z.read(themes[0]))

    print(f"# tokens from {sys.argv[1]} ({themes[0]})")
    scheme = root.find(f".//{A}clrScheme")
    if scheme is not None:
        print(f"\n[palette]  scheme: {scheme.get('name', '?')}")
        for child in scheme:
            tag = child.tag.replace(A, "")
            srgb, sysc = child.find(f"{A}srgbClr"), child.find(f"{A}sysClr")
            val = srgb.get("val") if srgb is not None else \
                  (sysc.get("lastClr", "?") if sysc is not None else "?")
            print(f"  {tag:10s} #{val}   ({ROLES.get(tag, tag)})")

    fs = root.find(f".//{A}fontScheme")
    if fs is not None:
        major = fs.find(f"{A}majorFont/{A}latin")
        minor = fs.find(f"{A}minorFont/{A}latin")
        print(f"\n[fonts]")
        print(f"  major (headings) {major.get('typeface') if major is not None else '?'}")
        print(f"  minor (body)     {minor.get('typeface') if minor is not None else '?'}")

    try:
        pres = ET.fromstring(z.read("ppt/presentation.xml"))
        sz = pres.find(f"{P}sldSz")
        if sz is not None:
            cx, cy = int(sz.get("cx")) / 914400, int(sz.get("cy")) / 914400
            ratio = "16:9" if abs(cx / cy - 16 / 9) < 0.02 else \
                    ("4:3" if abs(cx / cy - 4 / 3) < 0.02 else f"{cx / cy:.2f}:1")
            print(f"\n[slide]    {cx:.3f}in x {cy:.3f}in  ({ratio})")
    except KeyError:
        pass
    print("\n# note: theme fonts are the SPEC - check they are installed (preflight),")
    print("# and derive accent USAGE + geometry from the rendered pages, not from here.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
