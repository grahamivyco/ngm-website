# Homepage

**WA page:** Home
**Live URL:** https://needleworkguildmn.org/ (confirm)

## Structure — 3 gadgets in ONE full-width layout row

Paste order, top to bottom:

1. `01-top.html`     → Custom HTML gadget #1
                        (Google Fonts + ALL page CSS + Hero → Marquee →
                         About → Meetings → "Mark your calendar" heading
                         + the event-tag + FAQ-anim scripts)
2. `02-wa-gadget.txt` → the NATIVE WA "Upcoming events" gadget
                        (add in WA, CSS class = `ngm-wa-events` — see file)
3. `03-bottom.html`  → Custom HTML gadget #2
                        (Calendar CTA → Retreat → Join → FAQ → Location)

All CSS lives inside `01-top.html`'s `<style>` block — `03-bottom.html`
has no `<style>` of its own and relies on it.

## Notes
- `01-top.html` and `03-bottom.html` are the exact code to paste into
  the two Custom HTML gadgets. `02-wa-gadget.txt` is instructions, not code.
- Design tokens are the `--ngm-` custom properties at the top of the style block.

## Open TODO / flags carried in the code
- Replace 3 photo placeholders (`REPLACE_WITH_..._URL_FROM_GALLERY`) in
  the Hero, About, and Retreat with real /gallery image URLs.
- Confirm day/time for **Potpourri Stitchers** and frequency for
  **Sunday Tea & Stitch** (FLAG comments in `01-top.html`).
- Confirm with Tasha/Linda whether "first meeting free to try" line should
  be added to the Join block (`03-bottom.html`).
- After theme cutover: re-verify `upcomingEventsStyle001` class name.
