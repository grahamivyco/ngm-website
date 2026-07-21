# Wild Apricot — notes & gotchas

Working reference so the next editor (human or AI) doesn't relearn the hard parts.

## Specificity
- `casefile_guardian` uses very high-specificity selectors. Custom overrides must be
  `body`-prefixed. Chaining a custom ID directly onto the WA class (no space, same
  element) is the reliable way to win specificity battles.
- Per-instance IDs (e.g. `id_JOFpmm7_*`) are unstable — never use them in selectors.

## Gadget architecture
- Native WA gadgets can't be nested inside Custom HTML gadgets. Use the sandwich:
  Custom HTML -> native WA gadget -> Custom HTML.

## System-page editability
- Event registration / System pages: allow gadget sandwiching + template changes.
- Profile / change-password / membership screens: **CSS-only**.
- Admin backend: out of reach.
- No custom 404 — only CSS branding of `/Sys/Error/404` (+ blunt JS redirect).
- Theme Overrides (WA 4.2+) allow HTML-level control of the login presentation.

## Login state
- `document.body.classList.contains('memberContentView')` is the authoritative
  member-vs-guest signal. `{isMember:}` macros work in Custom HTML gadgets, not in
  template/layout contexts.

## Login / account gadget (WaGadgetLoginForm, LoginFormStyle001)
Verified against the live /Sys/Login page. Skinned in `global-css/global.css` by
STABLE classes (never the per-instance `id_JOFpmm7`). It's a dropdown: a `.loginLink`
trigger opens a `.loginPanel`.
- **Logged out:** `.loginContainer` (no `.authenticated`); panel holds
  `.oAuthButtonsContainer > a.wa-authenticateLoginLink.{googlePlus|microsoft|apple}`,
  then `form.generalLoginBox` with `.emailTextBoxControl`, `.passwordTextBoxControl`
  (+ `.toggle-password` eye), `.rememberMeCheckboxControl`, `.loginButton`, and
  `.loginPasswordForgot a` → /Sys/ResetPasswordRequest.
- **Logged in:** `.loginContainer.authenticated`; trigger = member name; panel holds
  `.loggedName`, `.profileBox a` (View profile → /Sys/Profile, Change password →
  /Sys/Password/Change), and `.loginBoxLogout` (posts to /Sys/Login/SignOut).
- Scope form-only rules with `.loginContainer:not(.authenticated)` and menu-only rules
  with `.authenticated` — the panel is shared. `.loginBoxLogout` is an
  `input[type=submit]`, so exclude it from form-submit rules with `:not(.loginBoxLogout)`.
- To show the form expanded (not behind the "Log in" trigger) is a WA gadget-style
  setting, not CSS.

## Favicon
- Set it the **native** way: **Settings → Site → Meta-tags → Raw Headers**, add a
  `<link rel="icon">` tag. That lands in the server-rendered `<head>`, so the icon
  is in the initial HTML — shows in the browser tab/bookmarks with no flash.
- Upload the icon under **Website → Files** (Pictures folder); reference it as
  `/Resources/Pictures/<filename>`. Use `brand/favicon.ico` (16/32/48/64 px).
- Do **not** inject it from a Custom HTML gadget — it loads after WA's default
  icon (visible flash) and never reaches the browser tab.

## Assets & API
- Image paths: `needleworkguildmn.org/resources/Pictures/[folder]/[filename]`
  (gallery images render via JS; can't be fetched).
- `authservice.wildapricot.org` blocks browser fetch (CORS) — the calendar is a
  hand-maintained styled event list as a result.

## Admin paths
- `needleworkguildmn.org/admin/` or `needleworkguildmn.wildapricot.org/admin/`
- Page editor: `needleworkguildmn.org/sys/website/?pageId=[ID]`

## Open items to fold in
- Replace `REPLACE_HUB` in Wrapper Reset with the real gadget ID.
- Re-verify `upcomingEventsStyle001` class after the theme cutover.
- Verify macro tokens: `{Contact_First_Name}`, `{Membership_Level}`, `{Renewal_Date}`, `{Balance}`.
