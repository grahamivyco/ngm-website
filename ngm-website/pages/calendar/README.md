# Calendar

**WA page:** Calendar  ·  **Structure:** 3 gadgets in one row.
1. `01-top.html` — Custom HTML (hero) — OPENS wrapper divs, does NOT close them
2. `02-wa-gadget.txt` — native WA month-grid "Events Calendar", class `ngm-cal`
3. `03-bottom.html` — Custom HTML — CLOSES the wrapper divs, then the **Key** module + Join CTA

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
`desktop (>1024)` full name (`.ngm-wd-f`) · `tablet (601–1024)` 3-letter
(`.ngm-wd-a`) · `mobile (≤600)` single letter. Mobile's single letter is
**derived from the 3-letter span** via `::first-letter` (not the separate
`.ngm-wd-1` span), so it depends only on the span tablet already uses — if a
letter shows on tablet it shows on mobile too, and the header never goes blank
even if a re-pasted gadget didn't emit `.ngm-wd-1`.

### Key module
`03-bottom.html` carries a `.ngm-key` module whose swatches use the **exact**
category colours the calendar paints on its event chips (the `--cat` map in
global.css). If you add or recolour an event category, update both places. The
module also holds an email tile ("Want to add something to the calendar?" →
`admin@mneedlework.org`) for event submissions.

### Grid look
No card/frame around the calendar — the month title, nav and grid sit on the
plain page background. Only vertical column dividers + the weekday underline
remain (no horizontal week-separator lines). Event chips are solid category
tiles that **wrap** to the full title (rounded corners, never clipped).

## Status
- ✅ All three blocks present. Paste order: `01-top` → WA Calendar gadget
  (CSS class `ngm-cal`) → `03-bottom`. The wrapper divs opened in `01-top` are
  closed in `03-bottom`.
