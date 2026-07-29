# Meeting access — login-aware "Join us on Zoom" band

A slim, site-wide band that keeps the Zoom link **off public pages** while still
giving guests a way in. It shows one of two states depending on whether the
visitor is signed in:

- **Members (logged in)** → a button to the **Member Hub**, where the Zoom link
  lives.
- **Guests (logged out)** → a **"Request the Zoom link"** button → the
  Request-the-Link page, which emails the link automatically.

This is the "small barrier" the board agreed on (Jul 2026): the link is never on
a public page, but an interested guest is one form away from it, and a member is
one click away.

## Files

| File | What it is |
| --- | --- |
| `01-top.html` | **The gadget.** Self-contained (own scoped CSS + JS). Paste into a site-wide Custom HTML gadget, just above the footer. |
| `mockups/preview.html` | **Standalone visual** — both states stacked, for showing the board. Not for pasting into WA. |
| `mockups/preview.png` | Screenshot of both states. |

Like `layout/header/`, `layout/footer/`, and `layout/suggestion-button/`, this is
a **self-contained layout gadget** — a documented exception to the "styling lives
in global.css" rule (see the root `CLAUDE.md`), because it's site-wide HTML+JS,
not just styling. Fonts come from WA's page head, same as the footer.

## Where it goes

Paste the entire contents of `01-top.html` into a **Custom HTML gadget in the
Wild Apricot page template, just above the footer gadget**, so it appears
site-wide. It renders as a full-width band.

## How the two states work

WA adds `body.memberContentView` on member-view pages. Both states live in the
HTML; the CSS **and** a small JS enforcer (same pattern as the footer) show the
right one — guests see `.ma-guest`, members see `.ma-member`.

## Set two URLs

In `01-top.html`, update the two links marked `SET URL`:

- the **Request-the-Link** page (guest button) — currently `/request-the-link`
- the **Member Hub** page (member button) — currently `/member-hub`

The guest state also links "Sign in for the link" to `/log-in` — adjust if your
login page differs.

## How this fits the rest of the Zoom plan

- **Zoom side (done):** waiting room off, only the host (SIG chair) can start the
  meeting, passcode on. Early arrivals wait on Zoom's "waiting for the host"
  screen and are let in automatically once the chair starts — no waiting room for
  volunteers to manage.
- **Members:** the Zoom link lives in the Member Hub (`pages/member-hub/`), behind
  login.
- **Guests:** the Request-the-Link page (`pages/request-the-link/`) auto-sends the
  link via the WA form's autoresponder (see that page's dev notes).
- **This band:** the front door that routes each visitor to the right one of
  those, on every page.

## Keeping the preview in sync

`mockups/preview.html` inlines the gadget's CSS and both markup states (fonts
embedded, links defanged to `#`). If you change `01-top.html`, mirror it here so
the screenshot stays honest.
