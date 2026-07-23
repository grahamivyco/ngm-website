# Homepage

**WA page:** Home
**Live URL:** https://needleworkguildmn.org/ (confirm)

## Files (edit these)

Styling comes from `global-css/global.css` (see the repo-root `CLAUDE.md`).
The page markup is the two `.html` files below — these are the exact code to
paste into the WA Custom-HTML gadgets:

1. `01-top.html`  → Custom HTML gadget #1
                          (Hero → Marquee → "Upcoming meetings & events" heading
                           + the event-tagging script)
2. `02-wa-gadget.txt`  → the NATIVE WA "Upcoming events" gadget
                          (add in WA, CSS class = `ngm-wa-events` — see file)
3. `03-bottom.html` → Custom HTML gadget #2
                          (Retreat → About → Meetings → Location → Join)

These two files are the only page markup — they carry no embedded `<style>`
block; all CSS lives in `global.css`.

## Notes
- `02-wa-gadget.txt` is instructions for the native gadget, not code.
- Design tokens are the `--ngm-` custom properties near the top of `global.css`.

## Open TODO / flags carried in the code
- Replace the photo placeholders (`REPLACE_WITH_..._URL_FROM_GALLERY`) in the
  Hero and About with real gallery image URLs.
- Confirm day/time for **Potpourri Stitchers** and frequency for
  **Sunday Tea & Stitch**.
- After theme cutover: re-verify the `upcomingEventsStyle001` class name.
