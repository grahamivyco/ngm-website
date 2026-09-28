# Retreat 2027  (`/annual-retreat-2027`)

Single Custom-HTML gadget (`01-top.html`). Paste
`dist/pages/retreat-2027/01-top.html`; `global.css` must be live first
(section "RETREAT 2027" holds the `.ngm-rt-*` rules).

⚠ The slug `/annual-retreat-2027` is what the header, footer and homepage
link to. Confirm it matches the page in WA (see `docs/backlog-status.md`).

## Content rule

Everything here comes from the draft the Guild wrote in WA (Sep 2026).
The refinement changed layout and fixed typos only. Nothing was added:

- the fee is "to be announced" (the draft said `$TBD`)
- the invitation and registration are "spring 2027"; there is no link yet,
  so there are no buttons pointing nowhere
- duplicated paragraphs in the draft (Lee's bio, Beth's class blurbs) were
  merged into one copy each, keeping every fact

When the invitation is out, add its link to the hero buttons and the
closing CTA, and put the fee in the Registration fee tile.

## Sections

1. Theme band: date + "Stitching with Sass" (not a link).
2. Hero: title, venue, date, the Sass copy, buttons to the classes and
   the schedule, "invitation in spring 2027" note, theme image.
3. Location: standard Visit block.
4. Good to know: fee, meeting rooms, parking.
5. Faculty: teacher names as tags (`#ngm-rt-classes`).
6. One band per teacher: portrait, bio, then class cards. One class =
   a wide card (`.ngm-rt-class-wide`); several = a grid
   (`.ngm-rt-classes-3` for three across).
7. Class schedule table (`#ngm-rt-schedule`), scrolls sideways on phones.
8. Closing CTA.

Photos: WA → Files → Pictures → `retreat2027`. Class-card photos are
shown whole, never cropped; teacher portraits are cropped to a fixed box.
