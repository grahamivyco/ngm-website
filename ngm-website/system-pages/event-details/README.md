# Event details (single event page, `/event-XXXXXXX`)

The WA **Event details** system page renders every individual event. It allows
the Custom-HTML sandwich (see `docs/wa-notes.md`), so the layout is:

1. `01-top.html` — Custom HTML above the native gadget: script only — it
   appends a pill-button row (`.ngm-evd-btns`) at the **end of the event
   description**: primary filled pill back to the calendar, plus an
   outline "More about {type}" pill when the title matches a known
   group/event type. It also moves a description's first embedded photo
   to the **top of the copy** (events without one just start with text).
   The "Event description" eyebrow over the title is pure CSS
   (`h1.pageTitle::before`).
2. **Native WA "Event details" gadget** (`.WaGadgetEventsStateDetails`) — the
   event title, When/Location box, description, and registration. Skinned from
   `global-css/global.css` (section "EVENT — SINGLE EVENT DETAIL PAGE").
3. `03-bottom.html` — Custom HTML below the gadget: the **Visit** section with
   the Member Hub / Request-the-Link tiles (same module as the homepage and
   contact page), with the login-aware Member Hub link script, followed by
   the standard closing **Join CTA** band (`.ngm-about-cta`, event-agnostic
   copy).
   **Adaptive:** a script reads the gadget's Location row — the location
   is authoritative (descriptions say things like "not at MVUUF", so
   venue names are NOT scanned there). MVUUF or "Hybrid" location → full
   block (address, photo, video band); virtual-only → just the
   Joining-by-video band (no rule line above it); a **known venue** from
   the script's VENUES table (e.g. City Bella for Sunday Tea & Stitch) →
   that venue's own note, address and photo, mirroring its meeting page;
   any other venue → just the venue text with a Google-Maps directions
   link, no photo. For in-person venues the video band stays only if the
   description mentions zoom/video. No readable location → full block.

Because this is a system page, these two gadgets appear on **every** event's
page. Keep the copy event-agnostic — each event's own time/location comes from
the native gadget above.

## Verified DOM (live, Aug 2026)

`.WaGadgetEventsStateDetails` → `pageTitleOuterContainer` (back link
`a.eventBackLink`, empty `pageViewSwitcherOuterContainer` chrome — hidden,
`h1.pageTitle.SystemPageTitle`) → `boxContainer` wrapped in the theme's
corners + `d1–d9` chrome (flattened, like change-password) →
`boxBodyInfoContainer > .boxInfoContainer > ul.boxInfo` with
`li.eventInfoStartDate` / `li.eventInfoStartTime` (its label is a bare
`&nbsp;` — hidden) / `li.eventInfoLocation`, each `label.eventInfoBoxLabel`
+ `.eventInfoBoxValue` → `.registrationInfoContainer` (VERIFIED on the
Retreat 2026 event: `h4.infoTitle` + `.infoText` + `ul.registrationInfo`
of types — `label.regTypeLiLabel > strong` + `.regTypeLiValue >
.regTypeLiValueSpan`, `li.disabled` for closed/full types; empty on
non-registrable events; the Register button itself is still unverified —
see `../event-registration/README.md`) → `boxBodyContentContainer.fixedHeight`
(height unclamped) whose `.inner.gadgetEventEditableArea` holds the
description with legacy `<font face="Lato">` tags (overridden directly —
a font tag's face attribute beats inherited fonts).

## Author formatting must survive (Sep 2026 fix)

Kym reported that centered top images and red registration text saved fine
in Admin but rendered plain on the live site (Aug 24, Sep 10). Both were
this skin overriding the editor, not WA losing the edit:

- **Centering.** `global.css` set `margin: 6px 0 18px !important` on
  description images. The shorthand also set the *side* margins, and auto
  side margins are how the editor centers a photo — so every centered image
  came out flush left. Only the vertical margin is forced now, and a
  companion rule re-centers the two shapes the editor writes
  (`text-align:center` on the wrapper, or `margin-left:auto` on the image).
  The script above made it worse by lifting the `<img>` out of its centered
  wrapper and deleting the wrapper; it now hoists the wrapper itself.
- **Colour.** `color: var(--ngm-charcoal) !important` on `font`/`p`, and
  `var(--ngm-sage-dk) !important` on `strong`, outrank both a `<font color>`
  attribute (specificity 0) and a non-important inline `style`, so red text
  was repainted. Colour is now a separate rule that skips any element the
  editor coloured, and `font[color] strong` inherits instead of repainting.

**The rule for anything added here:** never force `color` or a margin
shorthand onto `.gadgetEventEditableArea` content with `!important`. That
content is written by board members in the WA editor, and an `!important`
in this file silently overrules them with no error anywhere.

Both fixes are in `global-css/global.css`, section "EVENT — SINGLE EVENT
DETAIL PAGE", and go live only when the CSS tab is re-pasted.
