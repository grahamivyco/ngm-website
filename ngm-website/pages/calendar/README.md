# Calendar

**WA page:** Calendar  ·  **Structure:** 3 gadgets in one row.
1. `01-top.html` — Custom HTML (hero) — OPENS wrapper divs, does NOT close them
2. `02-wa-gadget.txt` — native WA month-grid "Events Calendar", class `ngm-cal`
3. `03-bottom.html` — Custom HTML — CLOSES the wrapper divs, then legend + CTA  ⚠ NOT YET RECEIVED

## Toolbar / weekday JS
`01-top.html` (and `01-top.slim.html`) ship a small inline `<script>` the calendar
needs — it (1) strips the `Month:` label from the title and (2) wraps each weekday
header in a full + 3-letter span so CSS can swap them by width. Both are things CSS
can't do here (single text node; this theme won't paint `::after` on table cells).
Keep the script when pasting either block. Everything else — round Prev/Next icon
buttons, the Today pill, nav sitting next to the month name, the abbreviation swap —
is CSS, live-scoped under `#idViewSwitchersTable` / `.WaGadgetEventsStateCalendar`
in `global.css` (the `.ngm-cal` class does NOT stick on the live gadget).

## Status
- Block 2 (`03-bottom.html`) still to be pasted. Until then the wrapper divs
  opened in `01-top.html` are unclosed — do not publish without Block 2.
