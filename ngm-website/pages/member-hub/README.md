# Member Hub  (members-only dashboard)

**WA page:** Member Home (`/member/`), members-only, set as the landing page
after login. ONE Custom-HTML gadget holding `01-top.html`.

Redesigned as a **dashboard, not a landing page** — the page is organized
around what members come to DO, not around telling a story:

1. **Hero** — "Welcome back. / Everything included with your membership,
   all in one place." plus the THREE quick actions members use most:
   - **Join today's meeting** (featured sage card) — the single guild Zoom
     link (`SET URL`), with "room opens 5 minutes early" folded in.
   - **My profile** → `/Sys/Profile` (bare path — resolves to whoever is
     logged in; NEVER add a `?memberId=`).
   - **Member resources** → in-page anchor `#ngm-hub-resources`.
2. **Member resources** (white) — tiles GROUPED for scanning:
   - *Stay Connected* — Member directory (`/member-directory`), Newsletter
     archive (`SET URL`).
   - *Learn & Create* — Lending library (`/lending-library`), Meeting
     handouts (`SET URL`).
   - *Guild Information* — Bylaws & policies (`SET URL`), Board minutes
     (`SET URL` Drive), Financial reports (`SET URL` Drive 990s),
     Financial forms (`SET URL` Drive).
   - *Get Involved* — ONE Volunteer-positions tile → `/volunteer` (the old
     14-card volunteer section was removed; the roles live on /volunteer).
3. **Guild leadership** (cream) — person cards, NAME first, role second,
   email quiet/small, grouped by team: *Executive Board* / *Programs* /
   *Member Services*. Roles without a person show the role as the card
   title with "Open position".
4. **Help bar** — "Can't find what you're looking for? Email our volunteer
   website team at admin@needleworkguildmn.org."

Styling: global.css `.ngm-hub-*` (dashboard additions: `.ngm-hub-qgrid`,
`.ngm-hub-task-featured`, `.ngm-hub-rgroup*`, `.ngm-hub-team*`,
`.ngm-hub-person*`).

## SET URLs still to fill (search `SET URL` in 01-top.html)
- Guild Zoom meeting link (hero featured card).
- Newsletter archive, Meeting handouts, Bylaws & policies (currently
  `/resources` fallback).
- Board minutes, Financial reports, Financial forms (Google Drive links).

## Parked idea — "alive" meeting card
Making the featured Zoom card show the actual next meeting ("Evening
Stitch-In · Tuesday 7:00 PM · Room opens 6:55" / "No meetings today — see
the calendar") needs a data source: either a small inline schedule JSON
someone maintains monthly, or reading WA's upcoming-events gadget with JS.
Doable later; skipped for now to keep the page zero-maintenance.

## Leadership roster (single source of truth)
Update names here when officers change. Website Manager and Website
Communications are open positions; confirm the Librarian name
("Janet Rock & Jeanne Cur…" was truncated in the source roster).
