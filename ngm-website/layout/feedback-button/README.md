# Feedback Button (global, floating)

**Structure:** SINGLE self-contained Custom HTML gadget — `01-top.html`
(its own `<style>` + markup, no dependency on `global.css`).

A small pill fixed in the **bottom-right** of every page, on **every
viewport**, that opens a **Google Form** where visitors can share opinions
or report bugs about the site refresh. The form is linked to a **Google
Sheet**, so responses are collected and viewable in one place.

## Publish

Paste the whole `01-top.html` block into a Custom HTML gadget in the
**site-wide page template** (the same template that carries the header and
footer). It is `position:fixed`, so it floats no matter where the gadget
sits in the layout.

## Form link

The `href` on the `#ngmfb` link points at the live NGM feedback form:
`https://forms.gle/BPz9eZNpCSxLpEmNA`. If the form is ever rebuilt or moved
(e.g. re-created under a different owner), just swap that one `href`.

The form is linked to a Google Sheet (Form → **Responses** → **Link to
Sheets**), so every submission lands as a row for tracking.

## The Google Form itself (build it like this)

Set the form up in Google Forms with these fields:

1. **Name** — short answer, *optional*.
2. **Email** — short answer, *optional* (so people can be shy or reachable,
   their choice).
3. **Subject** — dropdown, *required*: `Website ideas` · `Program ideas` ·
   `Event or calendar ideas` · `Something's broken` · `Other`.
4. **Your feedback or idea** — **paragraph** (long answer), *required* —
   the big box where the actual feedback goes.

Once the form exists, its share link goes in two places: the `#ngmfb` href
here, and the "Want to add something to the calendar?" CTA in
`pages/calendar/03-bottom.html`.

## Notes

- **Copy:** `Feedback & Ideas` on wider screens, shortening to `Ideas` at
  ≤560px so the pill stays small on phones. Lightbulb icon.
- **Color:** light sage (`#C7D4B6`) with deep-green text (`#35472F`).
- **Docks above the footer:** a small script watches the footer (`#ngmf`) and
  lifts the pill to rest just above it once the footer scrolls into view, so
  it never overlaps the footer. Floats normally elsewhere. Falls back to the
  plain fixed position if no footer is present.
- `z-index` sits just below the header, so the open mobile menu covers it.
- Self-contained on purpose (like `layout/header`, `layout/footer`,
  `layout/wrapper-reset`) — do **not** move its styles into `global.css`.
