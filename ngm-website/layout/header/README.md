# Site Header / Nav (global)

**Structure:** SINGLE Custom HTML gadget — `01-top.html`. Login-state aware
via `body.memberContentView` / `body.publicContentView` (CSS + JS). Paste into
the site-wide page template so it appears on every page.

**Favicon:** the top of `01-top.html` also injects the site favicon (from
`brand/favicon.*`) into `<head>`, replacing Wild Apricot's default. It lives
here because it's the only site-wide, CDN-loaded gadget whose JS can reach
`<head>`. Update the icon by replacing the files in `brand/`.
