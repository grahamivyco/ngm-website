# Newsletter Archive

Members' archive of Guild newsletters, grouped by year. Same component as
the board minutes page — see `pages/board-minutes/` for the full write-up
of how the list styling works.

⚠ **The site already has a "Newsletter Archive" page** (it appears under
*Pages not in menu* in WA → Site pages). Update that one; don't make a
second. Its existing issue links come across as they are.

⚠ **Slug not confirmed.** The Member Hub tile points at
`/newsletter-archive`. This session can't reach the live site, so check the
real slug in WA and fix whichever end is wrong. The minutes page had the
same problem and turned out to be `/meeting-minutes`, not `/board-minutes`.

## Structure

```
01-top.html       Custom HTML — hero (with the way back) + intro line
                  + the shared document-list script
02-wa-gadget.txt  native WA CONTENT gadget(s) — one per year
```

No `03-bottom`. Nothing sits under the cards.

## Adding an issue

1. Upload the PDF via **WA → Website → Files**.
2. Open the page in WA and edit the year's content gadget.
3. Type the issue name at the top of the list, select it, insert the link.

`docs/adding-minutes.md` is the handout for the minutes page and the steps
are identical bar the wording. Worth forking it into its own handout if a
different person looks after newsletters.

## ⚠ The script is duplicated

`01-top.html` carries the same script as
`pages/board-minutes/01-top.html`, verbatim. **Change one, change both**,
and re-paste both gadgets.

A WA Custom-HTML gadget has nowhere shared to put a script, and the repo
already duplicates the event-tagging script across several pages for the
same reason. The alternative — moving it into the site-wide chrome so it
loads everywhere — is worth doing if a third page ever wants this list,
but it makes the header gadget riskier to paste for the sake of two pages.

## What's NOT here

No claim about who can see it. The minutes page says "Open to current
members" while carrying no members-only restriction in WA, which is a
promise the site isn't keeping. This page doesn't repeat that — decide the
restriction first, then add wording to match if it's wanted.

Nothing about publication schedule, back-issue policy, or who edits the
newsletter. None of that was supplied, and the last round of invented
"good to know" copy had to be deleted.
