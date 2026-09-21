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
                          (Advertisers strip → About → Meetings group cards →
                           Events (Retreat tile + event cards) → Location → Join)

These two files are the only page markup — they carry no embedded `<style>`
block; all CSS lives in `global.css`.

## Advertiser logo strip

The **Our advertisers** strip is the FIRST section of `03-bottom.html`, so it
renders directly below the native Upcoming-events gadget. It is not a
separate gadget — to publish a change to it, paste `03-bottom.html` (from
`dist/pages/homepage/`) into Custom HTML gadget #2, and paste `global.css`
into WA → Website → CSS if the styling changed.

**Before the first paste:** upload the logo PNGs via WA → Website → Files,
then do one find-and-replace in the markup — every `LOGO_BASE/` becomes the
folder they landed in, e.g. `/resources/Pictures/advertisers/`. Each
advertiser needs the charcoal file (resting state) and the full-colour file
(hover/focus). Print & Frame is charcoal-only on purpose: its colour
original is white lettering, invisible on the cream band.

**To remove an advertiser:** delete its whole `<li>` block, comment markers
and all, then re-run `tools/build-dist.py` and re-paste the gadget. The row
re-centres itself — nothing else needs editing. National Academy of
Needlearts is **paid for three months from Sept 2026 (term ends Dec 2026)**
and is fenced off with its own comment markers for exactly this.

**To add one:** copy any `<li>` block, swap the business name (in both the
`alt` and the comment), the two filenames and the link, and drop it in
alphabetical order.

**To preview locally:** `previews/advertisers-strip.html` renders the real
markup against the real `global.css` at desktop and 375px. It reads the
source files over HTTP, so serve the folder first:
`cd ngm-website && python3 -m http.server 8000`, then open
`http://localhost:8000/previews/advertisers-strip.html`.

## Notes
- `02-wa-gadget.txt` is instructions for the native gadget, not code.
- Design tokens are the `--ngm-` custom properties near the top of `global.css`.

## Open TODO / flags carried in the code
- Replace the photo placeholders (`REPLACE_WITH_..._URL_FROM_GALLERY`) in the
  Hero and About with real gallery image URLs.
- Confirm day/time for **Potpourri Stitchers** and frequency for
  **Sunday Tea & Stitch**.
- After theme cutover: re-verify the `upcomingEventsStyle001` class name.
