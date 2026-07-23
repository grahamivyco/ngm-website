# Working conventions for this repo

This repo holds the source for the Needlework Guild of Minnesota's Wild Apricot
(WA) website. Read this before editing.

## Single source of truth: slim HTML + global.css

- **Styling lives in `ngm-website/global-css/global.css`.** The live site loads
  this one file (served via jsDelivr:
  `https://cdn.jsdelivr.net/gh/grahamivyco/ngm-website@main/ngm-website/global-css/global.css`).
  To change how anything looks, edit `global.css`.
- **Page markup lives in the `*.slim.html` files** under
  `ngm-website/pages/<page>/` (and `ngm-website/system-pages/<page>/`) — e.g.
  `01-top.slim.html`, `03-bottom.slim.html`. These are the canonical page files:
  the ones to edit and to paste into the WA Custom-HTML gadgets. They carry no
  embedded `<style>`; they rely on `global.css`.

## Do NOT recreate the old self-contained `.html` files

The old self-contained page files (`01-top.html` / `03-bottom.html` with an
embedded `<style>` block) have been **removed**. They were duplicates of the
slim markup plus a copy of the CSS, and keeping two copies in sync was
error-prone.

- **Only edit the `.slim.html` files.** Do not recreate `01-top.html` /
  `03-bottom.html` for a page, and do not add an embedded `<style>` block to a
  slim file.
- When a change needs new CSS, put it in `global-css/global.css`.

## Exceptions (leave as-is unless asked)

A few files are legitimately self-contained because they have **no** slim
variant — do not delete these and do not "slim" them unless explicitly asked:

- `ngm-website/layout/header/`, `layout/footer/`, `layout/wrapper-reset/`
- A handful of `system-pages/` (e.g. `contact-profile`, `member-profile`,
  `renewal`, and the `mockups/`).

## Images

Photos are hosted on the WA file manager and referenced by full URL, e.g.
`https://needleworkguildmn.org/resources/Pictures/Website%20Update%20Photos/<file>`.
Reference images by URL; don't commit large binaries to the repo.

## Summary

Edit `*.slim.html` for markup and `global-css/global.css` for styling. That's
it — there is no second copy to keep in sync.
