# Change password

**WA page:** system page `/Sys/Password/Change`.
**Structure:** CSS skin + ONE optional Custom-HTML gadget (`01-top.html`,
the branded "Change password" banner — same pattern as the member-profile
banner). The form skin lives in `global-css/global.css` under the
**CHANGE PASSWORD** banner and hangs off the automatic
`.WaGadgetChangePassword` gadget class, so it works even without the
gadget. The gadget also adds `body.ngm-password-page`; the CSS carries a
`body:has(.WaGadgetChangePassword)` fallback so the cream page background
applies either way.

**How members get here:** the redesign header does NOT carry WA's native
account dropdown (it's a custom header with Log Out / Member Hub buttons),
so the only links to this page are the ones the redesign adds itself: the
"Change password" text link on the Member Hub's My-profile card and the
"Change password" banner button on `/Sys/Profile`.

## Verified DOM (live, theme casefile_guardian)

- `.introContainer … .inner` — "Change password for {name}" → the card's
  serif title (design-system Cormorant 400; the theme's uppercase/bold is
  cleared).
- Table-based form rows: `.fieldContainer > .fieldSubContainer > table`
  with `td.left .fieldLabel` / `td.right .fieldBody` → stacked to
  label-above-field, left-aligned (the theme right-aligns the cells).
  Label cells without a real `<label>` are hidden via
  `td.left:not(:has(label))`.
- Each password input: `.password-wrapper > input.typeText` + the same
  broken-Font-Awesome `.toggle-password` eye as the login form (glyph
  collapsed, SVG eye drawn in its place).
- `.password-strength-meter` bar — HIDDEN by design (the requirements
  checklist already shows progress). If it ever comes back: the score div
  carries a `psms-N` class (0/25/50/75/100, verified live at `psms-25`),
  so stage colours can be restyled directly by class.
- `.password-strength-status` requirements list (shown in a sage panel).
  Verified live: an unmet row starts with a bare `-` text node; when met,
  the script swaps it for a green-check GIF `<img>`. The skin hides both
  (font-size 0 swallows the text node, the img is display:none) and draws
  its own marker in a constant 15px box: a small grey dot while unmet, the
  About-page "why people join" check (`.ngm-feat li::before` idiom: bare
  15px masked sage check) once met.
- `.validationError` ("Current password incorrect" etc.) — the theme
  positions these absolutely to the RIGHT of the field (they escaped the
  card and clipped); forced static, full-width, below the field.
- Buttons are `input[type=submit]` with **stable names**
  `submitNewPasswordButton` (Save → filled sage pill) and `cancelButton`
  (Cancel → outline pill). The `ctl00_*` ids are unstable — never used.

## Publishing

1. `global.css` → WA admin → Website → CSS (the skin + background).
2. Optional but recommended: paste `01-top.html` into a Custom-HTML gadget
   at the top of Website → System pages → Change password.
3. Verify by opening `/Sys/Password/Change` logged in and running the
   change-password flow (including a wrong current password, to see the
   inline error sit below the field).
