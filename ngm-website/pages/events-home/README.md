# Events

**WA page:** Events  ·  **Structure:** 3 gadgets in one row.
1. `01-top.html` — Custom HTML (the page opener + Upcoming-events heading).
   The page **opens straight on the events list** — no hero (Vivien, Sep 3).
   The old "More than the everyday / See the calendar" `.ngm-phero` block is
   gone; `.ngm-events-open` now carries the page title above the list.
2. `02-wa-gadget.txt` — native WA "Upcoming events", class `ngm-wa-events`, filtered to special events
3. `03-bottom.html` — Custom HTML ("Find your event" section with subhead rows:
   Featured event (full-width Retreat tile) → Signature events (March to the
   Finish, A Fall Finish, Annual Meeting 2027) → Workshops & programs →
   registering note → Join CTA).
   Event cards carry no location tag — Guild events are members-only.

**Sep 2026 changes.** Featured tile is **Retreat 2027** (2026 has happened);
**Annual Meeting 2027** was added under Signature events; **5th Tuesday Open
Stitching** moved off this page to `pages/meetings/03-bottom.html`, matching
the menu move (Kym Aug 24, Jody Sep 10). See `docs/backlog-status.md` for the
slugs that still need confirming.
