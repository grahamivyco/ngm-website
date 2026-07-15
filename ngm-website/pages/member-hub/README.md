# Member Hub  (members-only landing page)

A custom **Member Home** page that fronts Wild Apricot's built-in member pages.
Every link points at a real WA page that keeps full functionality. It's **static
HTML** (no native gadget), reorganized around what members actually do: get the
meeting Zoom link, manage their account/membership, reach resources, and find the
board.

## Sections (top to bottom)
1. **Hero** — generic welcome.
2. **Meeting Zoom links** — a bold sage band with **one card per meeting**; the
   Zoom link is *inline* (member clicks the card to join — no click-through to
   another page). See the monthly-refresh note below.
3. **Manage your account** — a module per profile tab (see URL table below);
   membership & renewal is folded in here as the first tile.
4. **Members-only materials** — the full launchpad: 10 tiles covering every member
   resource (directory, newsletter archive, handouts, library, photos, minutes,
   bylaws & policies, volunteer opportunities, financial summaries, financial
   forms). Financial forms live here with everything else — not gated.
5. **Meet our leadership** — board directory with names + emails (this is the
   single source of truth for the old "Officers & Group Leaders" roster).

## Meeting Zoom links — monthly refresh (IMPORTANT)
Each meeting card's link is `href="#"` with a `SET URL` comment. WA publishes the
Zoom links monthly, shortly before each meeting, so **someone must paste that
month's five links into these cards each month** (edit the Custom HTML gadget).
This is the tradeoff for having the links inline instead of on a separate page —
if monthly editing is too much, revert to a single card linking to the Member
Resources page.

## Members-only materials — link targets
All 10 tiles currently point at `/resources` (functional fallback) with a `SET URL`
note naming the exact document/page to repoint each to (online directory,
newsletter archive, handouts, library holdings, photo gallery, minutes page,
bylaws/policies, job descriptions, IRS 990s, check/deposit forms). Icons are one
consistent outline set (Feather/Lucide, 24 viewBox, ~1.7 stroke, round caps).

## Profile-tab deep links (the important part)
Each account tile links to a **bare** `/Sys/Profile/*` path — **no `?memberId=`**.
WA resolves a bare path to *whoever is logged in*, so every member sees their own
data. **Never add a member ID** — a hardcoded ID would show one person's private
info to everyone.

| Tile | Link | Status |
|------|------|--------|
| Membership & renewal | `/Sys/Profile` | renewal lives on the Profile page — confirm |
| Profile & details | `/Sys/Profile` | confirmed base |
| My event registrations | `/Sys/Profile/EventRegistrations` | confirmed |
| Invoices & payments | `/Sys/Profile/Finances` | confirmed |
| Email preferences | `/Sys/Profile/EmailSubscriptions` | confirm exact tab name |
| Privacy | `/Sys/Profile/Privacy` | confirmed |
| My donations | `/Sys/Profile/Donations` | confirmed |

### Must-test before go-live
Log in as a **regular member** (not admin) and click each account tile — confirm
each opens **that member's own** tab, not yours. This is standard WA behavior, but
it's privacy-sensitive, so verify it rather than assume. Fallback if any bare path
misbehaves: point that tile at `/Sys/Profile` and let the member tap the tab.

## Wild Apricot setup
1. Create a new page (e.g. **Member Home** at `/member-home`).
2. **Restrict it to members** — page settings → Access → *Members only*.
3. Set it as the **landing page after login** — Settings → Members → **Starting
   page** (default, or per membership level).
4. Paste `01-top.html` and `03-bottom.html` into Custom HTML gadget(s). There's no
   native gadget between them, so a single combined gadget works too.

`*.slim.html` are the same body without the inline `<style>`/fonts — use those once
the new Global CSS is live (it carries the `.ngm-hub-*`, `.ngm-hub-zoom`, and
`.ngm-lcard-*` skins).

## Why no "Upcoming events" or "my meetings"
Only **events** are registerable in WA, and only event registrations appear in a
member's profile — monthly **meetings** don't. So a "my meetings" view would show
nothing useful. Instead, **My event registrations** links straight to the member's
Event Registrations profile tab.

## What's static (by WA limitation)
- **Membership & renewal** is a link, not a live status — WA can't print a member's
  renewal date on a custom page; the real date + renew live on their Profile (WA
  also nags them within a week of expiry).
- **Generic welcome** — no member-name macro exists for Custom HTML; the header
  login gadget already greets members by name.

## Other URLs / content to confirm
- `/resources` — the real Member Resources page slug (meeting-links band + tiles).
- **Board:** *Website Manager* and *Website Communications* have no name yet;
  confirm the *Librarian* name ("Janet Rock & Jeanne Cur…").
