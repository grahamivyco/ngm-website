# Member Hub  (members-only landing page)

A custom **Member Home** page that fronts Wild Apricot's built-in member pages.
It does NOT replace them — every link points at a real WA page that keeps full
functionality. Built as the usual 3-part sandwich.

## Wild Apricot setup
1. Create a new page (e.g. **Member Home** at `/member-home`).
2. **Restrict it to members** — page settings → Access → *Members only*.
3. Set it as the **landing page after login** — Settings → Member area (or per
   membership level → starting page).
4. Add **Custom HTML gadget #1** → paste `01-top.html`.
5. Add the native **Upcoming events** gadget → see `02-wa-gadget.txt`.
6. Add **Custom HTML gadget #2** → paste `03-bottom.html`.

`*.slim.html` are the same body without the inline `<style>`/fonts — use those
once the new Global CSS is live (it carries the `.ngm-hub-*` skin).

## What's real vs static
- **Live:** the "Upcoming events" gadget (step 5) — real events from the calendar.
- **Static (by WA limitation):** the "Membership & renewal" strip is a link, not a
  live status. WA can't print a logged-in member's renewal date on a custom page,
  so the real date + renew flow live one click away on their **Profile**. WA also
  shows its own renewal reminder within a week of expiry.
- **Generic welcome:** no member-name macro exists for Custom HTML; the header
  login gadget already greets members by name.

## URLs to confirm before go-live
- `/resources` — the real Member Resources page slug (used by the Zoom-links task
  and all resource tiles).
- **"My meetings & registrations"** and **"Change password"** point at `/Sys/Profile`
  — replace with the exact profile-tab URLs (open the tab in the member area and
  copy the URL; each auto-resolves to the logged-in member).
- **Board emails** are PLACEHOLDERS following the domain pattern. Replace with the
  real addresses from the contact-page directory.
- `/contact`, `/calendar` — confirm slugs.
