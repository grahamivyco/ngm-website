# Member Hub  (members-only landing page)

A custom **Member Home** page that fronts Wild Apricot's built-in member pages.
Every link points at a real WA page that keeps full functionality. It's now
**static HTML** (no native gadget), built around the four things members actually
do: see/renew membership, get the meeting Zoom link, reach resources, and manage
their profile.

## Sections
Hero + **Membership & renewal** strip → **Top tasks** (Meeting Zoom links · My
event registrations) → **Member resources** → **Manage your account** →
**Meet our leadership** (board directory with names).

## Wild Apricot setup
1. Create a new page (e.g. **Member Home** at `/member-home`).
2. **Restrict it to members** — page settings → Access → *Members only*.
3. Set it as the **landing page after login** — Settings → Members → **Starting
   page** (default, or per membership level).
4. Paste `01-top.html` into one **Custom HTML gadget**, and `03-bottom.html` into
   a second one below it. (There's no native gadget between them anymore, so you
   could also combine both into a single Custom HTML gadget.)

`*.slim.html` are the same body without the inline `<style>`/fonts — use those
once the new Global CSS is live (it carries the `.ngm-hub-*` and `.ngm-lcard-*`
skins).

## Why no "Upcoming events" or "my meetings"
Only **events** are registerable in WA, and only event registrations appear in a
member's profile — monthly **meetings** don't. So a "my meetings" view and an
"upcoming meetings" gadget would show nothing useful. Instead, **My event
registrations** links straight to the member's Event Registrations profile tab.

## What's static (by WA limitation)
- The **Membership & renewal** strip is a link, not a live status — WA can't print
  a member's renewal date on a custom page; the real date + renew live one click
  away on their Profile (WA also nags them within a week of expiry).
- **Generic welcome** — no member-name macro exists for Custom HTML; the header
  login gadget already greets members by name.

## URLs / content to confirm before go-live
- `/resources` — the real Member Resources page slug (Zoom-links task + all
  resource tiles).
- **"My event registrations"** card and **"Change password"** point at
  `/Sys/Profile` with a `SET URL` note — replace with the exact profile-tab URLs
  (open the tab in the member area and copy the URL; it auto-resolves per member).
- **Board:** *Website Manager* and *Website Communications* have no name yet;
  confirm the *Librarian* name ("Janet Rock & Jeanne Cur…").
