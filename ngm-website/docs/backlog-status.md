# Board backlog — status

Working through the backlog compiled 2026-09-21 from board emails.

**Nothing here has been checked against the live site.** Outbound access to
`needleworkguildmn.org` is blocked by this environment's network policy (the
proxy refuses the connection outright), so every finding below comes from
reading the repo. Anything marked ⚠ needs someone with WA access to confirm.

**Nothing below is live yet.** This repo is not published from. Every change
reaches the site only when someone pastes it into WA — the CSS tab for
`global.css`, the matching Custom-HTML gadget for a page. See
`publishing-guide.md`.

---

## Done in this repo

### Calendar event formatting — centered images and red text (Kym, Aug 24 + Sep 10)
**Root cause found, fixed, needs a CSS-tab re-paste to go live.**

This was not WA dropping the edits. Two rules in `global.css` were
overriding the editor:

- Images: `margin: 6px 0 18px !important`. The shorthand set the side
  margins too, and auto side margins are exactly how the editor centers a
  photo, so every centered image rendered flush left. Made worse by the
  Event-details script, which lifted the `<img>` out of its centered
  wrapper and then deleted the wrapper.
- Red text: `color: … !important` on `font`, `p` and `strong`. An
  `!important` rule outranks both a `<font color="#FF0000">` attribute and a
  non-important inline `style`, which is how the WA editor writes colour —
  so red registration notes were repainted charcoal and sage.

Fixed in `global-css/global.css` (section "EVENT — SINGLE EVENT DETAIL
PAGE") and `system-pages/event-details/01-top.html`. Colour and side margins
now defer to whatever the editor set; font family, size and weight are still
ours. Details and the rule for future edits: `system-pages/event-details/README.md`.

**ETA Kym asked for:** the fix is written. It goes live the moment the CSS
tab and the Event-details top gadget are re-pasted — one sitting. What can't
be promised from here is that it's the *whole* story, because the live page
couldn't be loaded to confirm. Re-paste, open one event with a centered
photo and one with red text, and if either is still wrong, the console
snippet workflow in the repo-root `CLAUDE.md` is the next step.

### "Kris Hennum" → "Kris H" (Michelle, Sep 20)
Changed in `pages/member-hub/01-top.html` (the Sunday Tea & Stitch row of
the Member Hub roster). That is the **only** place in this repo that carried
the last name.

⚠ Jody says the event page still shows it. That will be the event record in
WA itself (Events → the event → title/description), not this repo — nothing
here writes a presenter's name onto an event page. Someone with WA access
needs to check the event records and the event category.

### Events page — hero removed, opens on the events list (Vivien, Sep 3)
The "More than the everyday / See the calendar" `.ngm-phero` block is gone
from `pages/events-home/01-top.html`. The page now opens on a compact title
band (`.ngm-events-open`) and goes straight into the events list, then the
full card list below it — the same shape as the monthly-meetings overview,
which was the other half of Vivien's ask from the Sep 2 meeting.

### 5th Tuesday Open Stitching moved from Events to Meetings (Kym Aug 24, Jody Sep 10)
Moved in both places it appears: out of the Events dropdown and into the
Meetings dropdown (`layout/header/01-top.html`, desktop **and** mobile), and
its card moved off the Events page onto the Meetings page under a new
"Bonus sessions" row.

⚠ Jody's open question — whether it should get its own event category — is a
WA Events setting, not a repo change, and it is worth deciding **before**
this is pasted: the Meetings page's native Upcoming-events gadget is
filtered by category, so 5th Tuesday sessions will only appear in that list
if the category filter includes them.

### Events dropdown — Retreat 2027, Annual Meeting 2027 (Vivien, Sep 19; Jody, Sep 15)
Events menu is now: Annual Retreat 2027 · Annual Meeting 2027 · March to the
Finish · A Fall Finish · Traditional Japanese Embroidery · Workshops.

Retreat 2026 ran 12–15 August 2026, so everything that pointed at it as the
*upcoming* retreat now points at 2027: the header, the footer's Retreat
link, the homepage featured tile, the Events page featured tile, and the
Event-details "More about the Annual Retreat" pill. The date rows on the two
featured tiles are commented out rather than left showing August 2026 —
restore them from git history once the 2027 dates are set.

### Zoom and Stitch added to the menu (Jody, Sep 15)
Added to the Meetings dropdown, desktop and mobile. Menu entry only — there
is no Zoom and Stitch page in this repo, and no copy for one in the backlog.

### Retreat 2026 page — invitation out, photo gallery in (Kym, Aug 24)
`pages/retreat/01-top.html` now reads as the record of a past event. Both
"Download the invitation" buttons are gone, the registration-open framing is
past tense, and Jane's photo album leads the page.

⚠ **Blocked on one URL.** The album link is the placeholder
`REPLACE_WITH_GOOGLE_PHOTOS_ALBUM_URL`, in **two** places (the gallery band
and the hero button). Do not paste this page into WA until Jane's Google
Photos link has replaced both — it is a broken link until then.

### Advertiser logos on the homepage (Kym, Sep 3 + Sep 10 + Sep 20 + Sep 21)
A five-logo strip sits **directly below the Upcoming events gadget** on the
homepage — it is the first section of `pages/homepage/03-bottom.html`,
styled under `.ngm-advertisers` in `global.css`. (It used to be a row of
bordered white cards above the Join band; Sep 21 replaced it with a plain
logo strip and moved it up under the events list.)

Built as a **static strip, not a rotating banner**. Kym asked for rotation
first; a static strip shows every advertiser at once instead of one in five
at a time, needs no script, and doesn't move under a cursor. Easy to change
if she'd rather have rotation — say so.

**How the strip behaves**

- Resting state is the single-colour charcoal logo at 70% opacity, so five
  mismatched logos read as one quiet row rather than five competing marks.
- Hover **and keyboard focus** cross-fade to the advertiser's full-colour
  logo at 100%. Two stacked `<img>` layers, pure CSS, no JS. Muted under
  `prefers-reduced-motion`.
- Nothing is ever scaled UP: the source PNGs are small (Needle Bling is
  200px wide, Seed Stitch 209px), so `width`/`height` stay `auto` and only
  `max-height: 60px` / `max-width: 180px` pull an oversized logo down.
- The row is `flex-wrap` + `justify-content: center`, so deleting one `<li>`
  re-centres the rest with no other edit. Phones get two columns with the
  odd logo centred.
- Links carry `target="_blank" rel="noopener sponsored"`; alt text is the
  business name.

**Answering Kym's two questions:**

1. *Will the logo files work?* Upload them to WA → Website → Files, then do
   ONE find-and-replace in the markup: every `LOGO_BASE/` becomes the folder
   they landed in (e.g. `/resources/Pictures/advertisers/`). The filenames
   in the markup match the files Kym supplied. Print & Frame has no usable
   colour version (the original is white lettering, invisible on cream), so
   it uses the charcoal file for both states and only brightens on hover —
   that's the `ngm-adv-mono` class on its link.
2. *How does NAN get removed after three months?* National Academy of
   Needlearts is **paid for three months from Sept 2026 — term ends Dec
   2026**. Its `<li>` is fenced between `▼ NATIONAL ACADEMY OF NEEDLEARTS`
   and `▲ END NATIONAL ACADEMY OF NEEDLEARTS` comments in
   `pages/homepage/03-bottom.html`. Delete everything between them, rebuild
   `dist/`, re-paste that one gadget. Nothing else refers to NAN and the
   strip re-centres itself.

Links wired, alphabetical: National Academy of Needlearts · Needle Bling
Designs (formerly Black Cat Stitchery) · Print & Frame · Seed Stitch Studio
· Welcome Stitchery.

**Previewing it locally** — `previews/advertisers-strip.html` renders the
real markup and the real `global.css` at desktop and 375px widths. It reads
the source files over HTTP, so serve the folder first:
`cd ngm-website && python3 -m http.server 8000`.

---

## Needs WA access — can't be done from this repo

### Sunday Tea & Stitch menu link (Jody, Sep 10)
The broken URL is `https://needleworkguildmn.org/sys/website/?pageId=18169`.
That `?pageId=` shape is WA's internal page-id link — WA writes it, not this
repo, and it breaks when the page it points at is deleted or replaced.

Worth knowing before hunting for it: **the site's visible menu is not WA's
menu.** WA's own navigation is hidden by `global.css`; the header gadget
(`layout/header/01-top.html`) is what visitors actually see, and it links to
`/sunday-tea-&-stitch`. So a stale entry in WA's menu produces a link that
nobody can reach by clicking — which means Jody most likely hit this from
somewhere that still holds a `pageId` link: WA's own menu editor, a page
body, or an old email or event description.

⚠ To fix: find where that URL is used. Then either repoint it at
`/sunday-tea-&-stitch` or, if the header link is itself wrong, correct the
header here. Also worth confirming the slug — the `&` in
`/sunday-tea-&-stitch` is unusual for a URL and shows up in several menu
entries (`/Come-&-Stitch`, `/daytime-counted-thread-&-needlepoint`).

### Feedback & Ideas button — submissions go nowhere (Kym Aug 24, Michelle Aug 30 + Sep 20)
The button itself is fine. `layout/feedback-button/01-top.html` points at
`https://forms.gle/BPz9eZNpCSxLpEmNA` and has done all along, so this is not
a markup bug — the form is either not wired to a sheet, wired to one nobody
on the board can open, or owned by an account no longer in use.

Still blocked on the Google access Michelle offered (Aug 30, Sep 20). Once
someone can open the form: confirm it has a linked response sheet
(Responses → link to Sheets), confirm the board can read that sheet, send a
test submission and check it lands. If the form needs rebuilding, only the
one `href` in that file changes.

### Advertiser image files can't be deleted (Kym, Sep 20)
⚠ WA file manager, no repo involvement. The usual cause is that the file is
still referenced by a page or gadget — WA refuses to delete a file in use.
Worth checking whether the files are in a folder her account has only read
access to, which produces the same symptom.

### Janet Rock in the Come & Stitch photos (Vivien, Jul 31) — no permission given
Can't be resolved from here: this session can't see the photos, and the
repo only holds URLs.

What the repo *can* tell you is that the fix is **one file each, not a page
edit**, because both Come & Stitch photos are reused across the site. Crop
or replace the file in the WA file manager under the same name and every
page below is fixed at once. Editing the page files would fix one page and
leave the rest.

- `Website Update - Photos/NGM Circle Stitch.jpeg` — used on **11 pages**:
  about, come-stitch, events-home, fifth-tuesday, homepage,
  japanese-embroidery, march-to-the-finish, meetings, potpourri-stitchers,
  sunday-tea-stitch, workshops.
- `Website Update - Photos/IMG_0480.jpg` — used on **5 pages**: about,
  come-stitch, fifth-tuesday, homepage, japanese-embroidery.

⚠ Vivien also asked to check other pages. Any photo showing Janet needs the
same treatment, and the same one-file-fixes-many logic applies.

### Showing Jody how to edit the top menu (Jody, Sep 10 + Sep 15)
She sees it in the template but can't edit the entries — and she is right
that she can't. The menu is markup inside the header Custom-HTML gadget, not
a WA menu, so WA's menu editor does nothing to it and there are no entries
there to drag.

Editing it means: change `layout/header/01-top.html` here (desktop `<ul
class="ngm-drop">` **and** the mobile `.ngm-mob-sub` — they hold the same
entries and must change together), run the `dist/` build, then paste
`dist/layout/header/01-top.html` into the header gadget in the site-wide
template. GitHub's web editor is enough for the first step; no command line
needed. Current menu contents and this warning are in
`layout/header/README.md`.

---

## Slugs to confirm before pasting the header ⚠

Three menu hrefs are best guesses — the pages are being written by Jody and
Vivien, and the live site couldn't be reached to read the real slugs. Check
each in WA (Website → Site pages) and correct it in
`layout/header/01-top.html` (**both** the desktop and mobile copies) before
pasting:

| Menu entry | href used | where else it appears |
|---|---|---|
| Annual Retreat 2027 | `/annual-retreat-2027` | footer, homepage tile, Events page tile, Event-details script, Retreat 2026 page |
| Annual Meeting 2027 | `/annual-meeting-2027` | Events page card |
| Zoom and Stitch | `/zoom-and-stitch` | header only |

Vivien noted Annual Meeting currently sits under `/workshops`; if it keeps
that URL, point the menu entry and the Events-page card there instead.

---

## Replies owed — not repo work

Listed so they don't get lost. The technical answers above cover Kym's
advertiser questions (logo files, NAN removal) and the calendar-formatting
ETA; the training answer is under "Showing Jody how to edit the top menu".

- **Kym** — Member Hub documents timeline (job descriptions, newsletters,
  minutes); Creativity Committee interactive idea list; training on editing
  static pages; project finish timeline.
  *Minutes are now built* — see `pages/board-minutes/`. Two things surfaced
  that need her or the secretary: the existing Meeting Minutes page shows
  **no members-only padlock** in WA, and **nothing has been posted since
  November 2025**. Newsletters and job descriptions can reuse the same
  document-list component.
- **Jody** — should 5th Tuesday Open Stitching get its own event category
  (Aug 27; see the note above — decide before the Meetings page is pasted);
  her Retreat 2027 question, so she can publish the page.
- **Vivien** — sharing the board meeting Zoom recording from her iCloud with
  Karen (Sep 19).
- **Jody** — change the temp password Michelle posted in the group thread
  (Sep 20). ⚠ Worth doing first: a working password sat in a thread. Change
  it, and send the next one by a different route than the one everybody
  reads.

---

## Publishing checklist for this batch

1. `python3 ngm-website/tools/build-dist.py` (already run for this batch).
2. Confirm the three slugs above, and Jane's album URL, and the advertiser
   logo filenames.
3. Paste `dist/global-css/global.css` into WA → Website → CSS. **Do this
   first** — the page markup below depends on it.
4. Paste the changed gadgets:
   - `dist/layout/header/01-top.html` and `dist/layout/footer/01-top.html`
     → site-wide template
   - `dist/pages/homepage/03-bottom.html`
   - `dist/pages/events-home/01-top.html` and `03-bottom.html`
   - `dist/pages/meetings/03-bottom.html`
   - `dist/pages/member-hub/01-top.html`
   - `dist/pages/retreat/01-top.html` (**only** after the album URL is in)
   - `dist/system-pages/event-details/01-top.html`
5. Spot-check logged out: one event with a centered photo, one with red
   text, the homepage advertiser row, the Events page opening on the list,
   and both menus on a phone.
