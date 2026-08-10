# Change password

**WA page:** system page `/Sys/Password/Change`.
**How members get here:** the redesign header does NOT carry WA's native
account dropdown (it's a custom header with Log Out / Member Hub buttons),
so the only links to this page are the ones the redesign adds itself: the
"Change password" text link on the Member Hub's My-profile card and the
"Change password" banner button on `/Sys/Profile`.
**Structure:** CSS-ONLY — WA does not allow Custom-HTML gadgets on this
screen (see `docs/wa-notes.md`), so there is no `01-top.html`. The whole
skin lives in `global-css/global.css` under the **CHANGE PASSWORD** banner
and hangs off the automatic `.WaGadgetChangePassword` gadget class.

## Verified DOM (live, theme casefile_guardian)

- `.introContainer … .inner` — "Change password for {name}" → styled as
  the card's serif title.
- Table-based form rows: `.fieldContainer > .fieldSubContainer > table`
  with `td.left .fieldLabel` / `td.right .fieldBody` → stacked to
  label-above-field. Label cells without a real `<label>` (requirements
  and button rows) are hidden via `td.left:not(:has(label))`.
- Each password input: `.password-wrapper > input.typeText` + the same
  broken-Font-Awesome `.toggle-password` eye as the login form (glyph
  collapsed, SVG eye drawn in its place).
- `.password-strength-meter` bar — the score div carries a `psms-N` class
  (0/25/50/75/100, verified live at `psms-25`), so the stage colours are
  restyled to brand tones (rose → sage) directly by class.
- `.password-strength-status` requirements list (shown in a sage panel).
  Verified live: an unmet row starts with a bare `-` text node; when met,
  the script swaps it for a green-check GIF `<img>`. The skin hides both
  (font-size 0 swallows the text node, the img is display:none) and draws
  its own marker via `::before` — outlined dot unmet, sage SVG check when
  met, detected with `:has(img)`.
- Buttons are `input[type=submit]` with **stable names**
  `submitNewPasswordButton` (Save → filled sage pill) and `cancelButton`
  (Cancel → outline pill). The `ctl00_*` ids are unstable — never used.

## Publishing

Nothing to paste on the page itself — the skin ships with `global.css`
(WA admin → Website → CSS). Verify by opening `/Sys/Password/Change`
logged in and running the change-password flow.
