# Site-wide consistency pass

Run a consistency pass over this repo's styling and markup, following the
conventions in CLAUDE.md (all styling in `ngm-website/global-css/global.css`,
markup-only page files, no embedded `<style>` blocks).

## Steps

1. **Scan `global-css/global.css` for drift.** Look for near-duplicate literal
   values that should share a token: font sizes and clamp() heading recipes,
   letter-spacing, focus rings, hover lifts/transforms, box-shadows,
   max-widths, border-radii, colors, and media-query breakpoints. The file
   already has a token block (`--ngm-h1`, `--ngm-h2`, `--ngm-eyebrow-size`,
   `--ngm-ring`, `--ngm-lift`, `--ngm-sh`/`--ngm-shm`, `--ngm-maxw`, etc.) —
   new duplicates should be rewired to existing tokens, or a new token added
   if three or more places share a value.

2. **Scan the page files** under `ngm-website/pages/` and
   `ngm-website/system-pages/` for violations of repo conventions:
   embedded `<style>` blocks (not allowed outside the documented exceptions
   in CLAUDE.md), inline `style=""` attributes that duplicate global CSS,
   and class names that don't exist in `global.css`.

3. **Check breakpoint hygiene.** Media queries should use the site's shared
   breakpoints (640px, 900px; 700px is deliberately kept for form stacking).
   Fold any stray one-off breakpoints into the nearest shared one unless a
   comment documents why it differs.

4. **Apply the fixes.** Rendered output should stay near-identical — the
   changes are the unifications themselves. Call out in the commit message
   any place where a value shifts visibly (e.g. a title moving a few px onto
   the shared type scale).

5. **Commit and push** to the designated feature branch with a commit message
   listing each unification (token added → literals replaced, with counts).
   Do not open a PR unless asked.

6. **Remind the user how to publish:** paste the full updated
   `global-css/global.css` into the Wild Apricot CSS tab (WA admin →
   Website → CSS) and Save; paste any changed page `.html` files into their
   Custom-HTML gadgets.

## Ground rules

- Never create self-contained duplicate copies of pages.
- Leave the documented exceptions (`layout/header/`, `layout/footer/`,
  `layout/wrapper-reset/`, and the self-contained `system-pages/`) alone.
- Prefer few, well-named tokens over many; don't tokenize a value used in
  only one or two places.
