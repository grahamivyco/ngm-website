# Event details (single event page, `/event-XXXXXXX`)

The WA **Event details** system page renders every individual event. It allows
the Custom-HTML sandwich (see `docs/wa-notes.md`), so the layout is:

1. `01-top.html` — Custom HTML above the native gadget: script only — it
   appends a pill-button row (`.ngm-evd-btns`) at the **end of the event
   description**: primary filled pill back to the calendar, plus an
   outline "More about {type}" pill when the title matches a known
   group/event type.
2. **Native WA "Event details" gadget** (`.WaGadgetEventsStateDetails`) — the
   event title, When/Location box, description, and registration. Skinned from
   `global-css/global.css` (section "EVENT — SINGLE EVENT DETAIL PAGE").
3. `03-bottom.html` — Custom HTML below the gadget: the **Visit** section with
   the Member Hub / Request-the-Link tiles (same module as the homepage and
   contact page), with the login-aware Member Hub link script.
   **Adaptive:** a script reads the gadget's Location row and reshapes the
   section — MVUUF (checked first, so "MVUUF and Zoom" hybrids keep
   everything) → full block; virtual-only → just the Joining-by-video band;
   any other venue → just that venue with a Google-Maps directions link (no
   MVUUF photo, no Zoom band). No readable location → full block.

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
+ `.eventInfoBoxValue` → empty `.registrationInfoContainer` (register
buttons unverified — no live event takes registration; see
`../event-registration/README.md`) → `boxBodyContentContainer.fixedHeight`
(height unclamped) whose `.inner.gadgetEventEditableArea` holds the
description with legacy `<font face="Lato">` tags (overridden directly —
a font tag's face attribute beats inherited fonts).
