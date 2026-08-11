# Event registration

**WA system page:** Event registration — the multi-step form members land
on after clicking **Register** on any event (the target of the "How to
register" bands on the event pages).

## Status: partially unblocked (Aug 2026)

The **details-page registration block** is now verified and styled: the
Retreat 2026 event's `registrationInfoContainer` carries `h4.infoTitle`
+ `.infoText` + `ul.registrationInfo` of registration types
(`regTypeLiLabel`/`regTypeLiValueSpan`, `li.disabled` when closed/full)
— skinned in `global.css` under the EVENT — SINGLE EVENT DETAIL PAGE
banner. Still unverified: the **Register button** (the Retreat's window
is closed, so none renders) and the **multi-step registration wizard**
this system page hosts. Two ways to capture those:

1. **Fast path:** in WA admin, create a temporary test event (any far
   future date, titled "TEST — ignore"), add one free registration
   type, open its public page → Register, run the structure snippet,
   then delete the event.
2. **Otherwise:** wait for the first real registration window (A Fall
   Finish opens September 1, 2026).

## Original plan

Per the console-first rule (repo CLAUDE.md), the form skin is written
only against verified live markup — the gadget's class is unconfirmed
(possibly shared with `.WaGadgetPublicWizard`, which already carries the
membership-application skin in `global.css`; if so, much of the styling
may already apply). To capture it: open any event → click Register →
run the structure-dump snippet from the maintainer conversation (it
walks every `WaGadget` on the page) and paste the output back.

## Planned shape (mirrors the other system pages)

1. Skin in `global.css` under an **EVENT REGISTRATION** banner, hung off
   the verified stable gadget class — body-prefixed `!important` font
   pins, sage/outline pill buttons by stable name/class, left-aligned
   labels, inline errors below fields.
2. If the editor allows a Custom-HTML gadget: an optional `.ngm-sys`
   banner (`01-top.html`, change-password pattern).
3. Verify with a real test registration end-to-end.
