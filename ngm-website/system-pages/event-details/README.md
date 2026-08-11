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
   contact page), with the login-aware Member Hub link script.
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
