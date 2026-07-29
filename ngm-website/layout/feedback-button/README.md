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

## The one thing to edit

In `01-top.html`, replace the `href` on the `#ngmfb` link
(`https://forms.gle/REPLACE-WITH-YOUR-GOOGLE-FORM-LINK`) with your Google
Form's share link.

**To wire the form to a Sheet:** open the Form → **Responses** tab →
**Link to Sheets** → *Create new spreadsheet*. Every submission then lands
as a row in that sheet.

## Notes

- Label is `Ideas or bugs on the new site?` on wider screens and shortens to
  `Feedback` at ≤560px so the pill stays small on phones.
- `z-index` sits just below the header, so the open mobile menu covers it.
- Self-contained on purpose (like `layout/header`, `layout/footer`,
  `layout/wrapper-reset`) — do **not** move its styles into `global.css`.
