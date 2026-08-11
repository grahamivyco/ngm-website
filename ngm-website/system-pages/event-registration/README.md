# Event registration

**WA system page:** Event registration — the multi-step form members land
on after clicking **Register** on any event (the target of the "How to
register" bands on the event pages).

## Status: awaiting the live DOM dump

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
