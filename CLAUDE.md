# Working conventions for this repo

This repo holds the source for the Needlework Guild of Minnesota's Wild Apricot
(WA) website. Read this before editing.

## Single source of truth: page HTML + global.css

- **Styling lives in `ngm-website/global-css/global.css`.** The whole live site is
  styled by this one file, which is **pasted inline into the Wild Apricot CSS tab**
  (WA admin → **Website → CSS**). `global.css` is the master copy you edit — the
  readable, commented source of truth and change history. The stylesheet must live
  in the CSS tab itself — WA's Content Security Policy refuses externally hosted
  CSS, so it can't be linked from an outside URL; publishing is always a manual paste.
- **Publish the minified copy, `global-css/global.min.css`.** WA's CSS field has a
  length limit that the full commented `global.css` now exceeds — pasting the full
  file can fail to save and leave the whole site unstyled. So after editing
  `global.css`, regenerate the minified file and paste **that** into the WA CSS tab:

  ```
  npx clean-css-cli -o ngm-website/global-css/global.min.css ngm-website/global-css/global.css
  ```

  `global.min.css` is a generated artifact (never hand-edit it) and renders
  identically to the master. Commit both together so they stay in sync.
- **Page markup lives in the `*.html` files** under `ngm-website/pages/<page>/`
  (and `ngm-website/system-pages/<page>/`) — e.g. `01-top.html`,
  `03-bottom.html`. These are the canonical page files: the ones to edit and to
  paste into the WA Custom-HTML gadgets. They carry **no embedded `<style>`
  block** — all styling comes from `global.css`.

## One copy only — no self-contained duplicates

There used to be two copies of every page (a self-contained `01-top.html` with
an embedded `<style>` block, plus a `01-top.slim.html` markup-only twin).
Keeping them in sync was error-prone, so the self-contained copies were removed
and the markup-only files were renamed to plain `01-top.html` / `03-bottom.html`.

- **Do not add an embedded `<style>` block to a page file**, and do not create a
  second "self-contained" copy of a page. One `.html` file per gadget, markup
  only.
- When a change needs new CSS, put it in `global-css/global.css`.

## Exceptions (leave as-is unless asked)

A few files are legitimately self-contained (their own CSS/fonts) because they
have no global-CSS equivalent — do not "slim" or delete them unless explicitly
asked:

- `ngm-website/layout/header/`, `layout/footer/`, `layout/wrapper-reset/`
- A handful of `system-pages/` (e.g. `contact-profile`, `member-profile`,
  `renewal`, and the `mockups/`).

## Images

Photos are hosted on the WA file manager and referenced by full URL, e.g.
`https://needleworkguildmn.org/resources/Pictures/Website%20Update%20Photos/<file>`.
Reference images by URL; don't commit large binaries to the repo.

## Summary

Edit the page `*.html` files for markup and `global-css/global.css` for
styling. That's it — there is no second copy to keep in sync.
