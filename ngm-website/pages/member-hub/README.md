# Member Hub

**WA page:** Member Hub (members-only)
**Live URL:** `/members`  — this is the target of the "Member Hub" button in the header.

## Paste order (top → bottom, all in the SAME layout row)
1. `01-top.html` — Custom HTML gadget (welcome banner + "Upcoming events" intro)
2. **Native WA "Upcoming events" gadget** — see `02-wa-gadget.txt`; give it CSS class `ngm-wa-events`
3. `03-bottom.html` — Custom HTML gadget (member quick-links + resources + help strip)

This is the "sandwich" pattern (Custom HTML → native gadget → Custom HTML) because a
native WA gadget can't be nested inside a Custom HTML block.

## Before it goes live — set these real URLs
The quick-link cards in `03-bottom.html` have placeholder links marked `<!-- SET URL -->`.
Point each at the correct Wild Apricot page:

| Card | Placeholder `href` | Point it at |
|------|--------------------|-------------|
| Member Directory | `/directory` | your WA member directory page |
| My Profile & Renewal | `/sys/profile` | usually correct as-is (WA profile) |
| Resources & Documents | `/resources` | your member-only resources / document page |
| Contact the guild | `/contact-us` | your contact page or a `mailto:` link |

## Notes
- **Page access:** set the WA page to members-only. Everything here assumes the viewer
  is logged in.
- **The name greeting** uses the `{Contact_First_Name}` macro. Per `docs/wa-notes.md`
  this macro is still to be verified — a script in `01-top.html` falls back to plain
  "Welcome back" if the macro doesn't resolve, so a raw `{Contact_First_Name}` is never
  shown. Once verified working, you can add `{Membership_Level}` / `{Renewal_Date}` here too.
- **Why the events list is a native gadget:** the WA event API is CORS-blocked in the
  browser, so a hand-built list can't auto-update. The native gadget is the only piece
  that stays current with no code change.
- Related CSS: all styling lives inside `01-top.html` and `03-bottom.html` (self-contained).
