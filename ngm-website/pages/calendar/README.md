# Calendar

**WA page:** Calendar  ·  **Structure:** 3 gadgets in one row.
1. `01-top.html` — Custom HTML (hero) — OPENS wrapper divs, does NOT close them
2. `02-wa-gadget.txt` — native WA month-grid "Events Calendar", class `ngm-cal`
3. `03-bottom.html` — Custom HTML — CLOSES the wrapper divs, then the **Key** module + Join CTA

## Toolbar / weekday JS
`01-top.html` (and `01-top.html`) ship a small inline `<script>` the calendar
needs — it (1) strips the `Month:` label from the title and (2) wraps each weekday
header in a full + 3-letter + single-letter span so CSS can swap them by width.
Both are things CSS can't do here (single text node; this theme won't paint
`::after` on table cells). Keep the script when pasting either block. Everything
else — round Prev/Next icon buttons, the Today pill, nav sitting next to the month
name, the abbreviation swap — is CSS, live-scoped under `#idViewSwitchersTable` /
`.WaGadgetEventsStateCalendar` in `global.css` (the `.ngm-cal` class does NOT stick
on the live gadget).

### Weekday abbreviations (3 tiers)
`desktop (>1024)` full name · `tablet (601–1024)` 3-letter · `mobile (≤600)` single
letter. Each tier shows one of the JS-emitted spans (`.ngm-wd-f` / `.ngm-wd-a` /
`.ngm-wd-1`); a letter always shows, so the header row never goes blank.

### Key / legend
`03-bottom.html` carries a `.ngm-key` module whose swatches use the **exact**
category colours the calendar paints on its event chips (the `--cat` map in
global.css). If you add or recolour an event category, update both places.

## Status
- ✅ All three blocks present. Paste order: `01-top` → WA Calendar gadget
  (CSS class `ngm-cal`) → `03-bottom`. The wrapper divs opened in `01-top` are
  closed in `03-bottom`.
