# Login page (skin + sandwich)

**WA page:** `/Sys/Login` — a built-in system page (CSS + Custom HTML around the native form)
**Live URL:** `/sys/login`

## Login architecture (decided — don't undo)
There are TWO branded entry points, on purpose:
- **`/log-in`** — a separate custom branded login page. This is what the header
  and footer **"Log In" buttons point to.** Do NOT repoint them at `/sys/login`.
- **`/Sys/Login`** — WA's built-in login page, skinned by the files in this folder.
  WA auto-redirects logged-out visitors here whenever they open a members-only
  page (`/Sys/Login?ReturnURL=…`), and that target can't be changed in WA
  settings — so this page is branded with this skin so those redirects look
  right. WA's native `ReturnURL` flow keeps working (no JS redirect involved).

## What this is
Wild Apricot already has a login page with a native login form. You are **customising
that system page**, not creating a new one. These three files wrap the native form
with NGM branding, laid out as a **split screen**: a branded sage hero on the left,
the login form card on the right.

## Page setup — a 2-column layout ROW
Split the login page content into a **2-column layout row** in the WA editor, then:
- **Left column:** `01-top.html` as a Custom HTML gadget — the branded sage **hero**
  (needle-mark, "Welcome back, stitchers", benefits list). Also sets `body.ngm-login-page`.
- **Right column:** the **native WA login gadget** (`.WaGadgetLoginForm`, already on the
  page — see `02-wa-gadget.txt`), then `03-bottom.html` (the "not a member? Join" line)
  beneath it.

The Global CSS (scoped to `body.ngm-login-page`) styles each side: the hero fills the
left column as a full-height sage panel, and the form is skinned into a centred card in
the right column. **No fixed positioning** — everything is in normal flow, so the page
scrolls cleanly and the site footer sits below. On narrow screens (≤640px) WA stacks the
two columns; the hero then collapses to a slim strip and the form leads.

## If it needs a nudge on the live site
The side-by-side ↔ stacked switch is the `@media(min-width:981px)` /
`@media(max-width:980px)` pair in the login block of `global.css`. `981/980` matches
where the WA 2-column row collapses (same as the header's mobile-nav breakpoint). If your
row actually stacks at a different width, raise/lower both numbers together: above the
breakpoint you get the full side-by-side hero, at/below it the slim stacked strip (like
mobile).

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
- **Log out:** native `/Sys/Login/SignOut` (linked in the header).
- **View profile:** native `/sys/profile` (linked from the member hub). Skinning that
  page is the separate `system-pages/member-profile/` task.

## URLs (set)
- `03-bottom.html` / `03-bottom.html` "Join the guild" link → `/Join-Duplicate` (the real Join page slug).
