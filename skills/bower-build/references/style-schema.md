# STYLE.md Schema — the design contract

Emitted by bower-triage; consumed by bower-build and bower-qa. Two scales because density is a
delivery-mode parameter (BCG Key Message vs Detail), not a style.

```yaml
source:  house-template <path> | likaku-fallback
mode:    projected | read | both        # from dump.md brief; "both" = body projected, appendix read

fonts:
  title: Georgia bold                    # or derived from template
  body:  Arial

scale.projected:                         # BCG Key Message floors are HARD minimums
  title: 28   kicker: 18   body: 20   secondary: 16   chart_labels: 14   chrome: 12
  floor: nothing below 16 except chart/label/caption text (14)
scale.read:                              # likaku, verbatim
  cover: 44   section: 28   title: 22   subheader: 18   body: 14   chrome: 9
  floor: nothing below 9; chart labels >= 10

palette:
  NAVY: "#051C2C"        # primary — titles, section markers
  DARK_GRAY: "#333333"   # body text
  MED_GRAY: "#666666"    # secondary text, labels, source
  LINE_GRAY: "#CCCCCC"   # rules, separators
  BG_GRAY: "#F2F2F2"     # panels, takeaway areas
  accents:               # ONLY when a slide has 3+ parallel items
    ["#006BA6", "#007A53", "#D46A00", "#C62828"]
  negative: "#C62828"

geometry:                                # 16:9
  slide: 13.333in x 7.5in
  margins: 0.8in
  title_box: top 0.15in, height 0.9in
  title_rule: 1.05in
  content_band: 1.3in - 6.5in
  source_line: 7.05in                    # bottom-left
  page_number: bottom-right, chrome size, "n" only

chart_tokens:
  base: grey monochrome first; accent carries the message only
  leader_lines: manual only
  backfill: never
```

## Rules the schema encodes

- **Cut content, never shrink type.** The floors are content constraints. Overflow = build
  error → split the slide or flag the spec.
- **Appendix (X## rows) always uses scale.read**, whatever the deck mode.
- **Emphasis ladder** (strongest → weakest): solid fill+reversed text → tinted fill → outline →
  accent text → bold. Cap the top two rungs at ONE element per slide (two only if the message
  genuinely has two anchors). Never stack rungs. Keep each rung's meaning constant deck-wide.
- **No emphasis inside titles or subtitles, ever** — no bold, colour, italics, caps, underline.
- Size, colour and bold are the only emphasis styles anywhere. Italics/caps/underline banned
  (underline = hyperlinks only).
- **No colour-filled boxes behind body text.** Fills only on hierarchically superior text
  (column/section headers), applied consistently across that level.
- Greyscale survival: accent and dark grey must stay separable in mono print; meaning never
  depends on hue alone (labels/signs/position carry it too).
- Effects banned: 3D, gradients, shadows, bevels, decorative bars of any orientation.

## Template-derived styles

When `source: house-template`, intake flags the file and triage reads palette, fonts and slide
size from its theme/master (tokens only — v1 does not inherit masters/layouts). The derived
style still fills BOTH scales and still honours the floors: a client template does not license
12pt body on a projector.
