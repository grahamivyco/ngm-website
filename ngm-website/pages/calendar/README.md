# Calendar

**WA page:** Calendar  ·  **Structure:** 3 gadgets in one row.
1. `01-top.html` — Custom HTML (hero) — OPENS wrapper divs, does NOT close them
2. `02-wa-gadget.txt` — native WA month-grid "Events Calendar", class `ngm-cal`
3. `03-bottom.html` — Custom HTML — the **Key** module (INSIDE the calendar
   section, right under the month grid), then CLOSES the wrapper divs, then
   the **Visit** section (same "Where we meet" block as the homepage). No Join
   CTA (removed).

## Toolbar / weekday JS
`01-top.html` ships a small inline `<script>` the calendar
needs — it (1) strips the `Month:` label from the title and (2) wraps each weekday
header in a full + 3-letter + single-letter span so CSS can swap them by width.
Both are things CSS can't do here (single text node; this theme won't paint
`::after` on table cells). Keep the script when pasting either block. Everything
else — round Prev/Next icon buttons, the Today pill, nav sitting next to the month
name, the abbreviation swap — is CSS, live-scoped under `#idViewSwitchersTable` /
`.WaGadgetEventsStateCalendar` in `global.css` (the `.ngm-cal` class does NOT stick
on the live gadget).

### Weekday abbreviations (3 tiers)
`desktop (>1024)` full name (`.ngm-wd-f`, Sunday…) · `tablet (601–1024)` the
3-letter abbreviation (`.ngm-wd-a`, Sun Mon Tue…) · `mobile (≤600)` the single
letter (`.ngm-wd-1`, S M T W T F S) — the 7 narrow phone columns can't fit 3
letters. The JS emits all three spans; CSS shows one per breakpoint. Each shown
tier is `display:inline-block` (a plain `inline` span was collapsing to 0px wide
in WA's table, which blanked the letters).

### Key module
`03-bottom.html` carries a `.ngm-key` module that sits INSIDE the calendar
section (before the wrapper divs close), styled as a compact card: "Key"
title top-left, then the items. Swatches use the **exact** category colours
the calendar paints on its event chips (the `--cat` map in global.css). If
you add or recolour an event category, update both places. Beneath the items
sits a "Want to add something to the calendar?" tile — no button; the words
"Ideas &amp; Feedback form" in the copy link to the **Ideas & Feedback Google
Form**. Keep that href in sync with `layout/feedback-button/01-top.html`.

### Grid look
No card/frame around the calendar — the month title, nav and grid sit on the
plain page background. Vertical column dividers plus ONE thin horizontal
line where each week row meets the next (the row's top border — no doubled
inset line inside cells). Event chips are solid category tiles that **wrap**
to the full title (rounded corners, never clipped). At ≤1100px the gadget
carries its own 12px side gutters (on top of the section padding) so the grid
and the ‹/Today/› buttons never run edge-to-edge at any width.

## Status
- ✅ All three blocks present. Paste order: `01-top` → WA Calendar gadget
  (CSS class `ngm-cal`) → `03-bottom`. The wrapper divs opened in `01-top` are
  closed in `03-bottom`.
