# Login page (skin + sandwich)

**WA page:** `/Sys/Login` — a built-in system page (CSS + Custom HTML around the native form)
**Live URL:** `/sys/login` — this is the target of the "Log In" button in the header.

## What this is
Wild Apricot already has a login page with a native login form. You are **customising
that system page**, not creating a new one. These three files wrap the native form
with NGM branding, laid out as a **split screen**: a branded sage hero on the left,
the login form card on the right.

## Paste order (top → bottom, same single layout column)
1. `01-top.html` — Custom HTML gadget: the branded sage **hero** (needle-mark, "Welcome
   back, stitchers", benefits list). Also sets `body.ngm-login-page`.
2. **Native WA login gadget** (`.WaGadgetLoginForm`, already on the page) — see `02-wa-gadget.txt`
3. `03-bottom.html` — Custom HTML gadget: "not a member? Join" line

**No 2-column WA row needed.** Paste all three stacked in one column — the Global CSS
(scoped to `body.ngm-login-page`) does the split: it fixes the hero to the left half of
the viewport and pushes the form + join line into the right half. Under 861px it collapses
back to a single stacked column automatically.

## If the split needs a nudge on the live site
Two CSS variables at the top of the login block in `global.css` tune it:
`--ngm-hero-w` (left-panel width, default `50vw`) and `--ngm-head-h` (header height to
clear, default `86px`). To revert to a simple centred card, delete the
`@media(min-width:861px)` block in that section — everything else still works.

## The form skin lives in Global CSS (done)
The login form and the account dropdown are skinned in `global-css/global.css`,
which targets WA's real `.WaGadgetLoginForm` classes site-wide — verified against
the live `/Sys/Login` page (both the logged-out form and the logged-in account
menu). **Nothing to assign to the gadget**; just make sure `global.css` is pasted
into the WA "Global CSS" tab.

## Good to know: it's a dropdown-style login
Visitors click "Log in" to expand the form (email/password + Google/Microsoft/Apple
+ remember-me + forgot-password). If you'd rather the form show expanded by default
on this page, that's a WA gadget-style setting, not a CSS change.

## Already handled elsewhere (no work needed here)
- **Log In / Log Out / Member Hub buttons:** the header (`layout/header/01-top.html`)
  already swaps these based on login state (`body.memberContentView`).
- **Log out:** native `/sys/logout` (linked in the header).
- **View profile:** native `/sys/profile` (linked from the member hub). Skinning that
  page is the separate `system-pages/member-profile/` task.

## Before it goes live — set this URL
- `03-bottom.html` "Join the guild" link → your real Join page (placeholder `/join`, marked `<!-- SET URL -->`).
