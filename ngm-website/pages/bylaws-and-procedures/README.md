# Bylaws & Policies

Members' page listing the Guild's governing PDFs: bylaws, org chart,
policies, waivers. Same component as the board minutes page. See
`pages/board-minutes/` for how the list styling works.

**Slug: `/bylaws-and-procedures`.** The Member Hub tile points there.

## Structure

```
01-top.html       Custom HTML — hero (with the way back) + intro line
                  + the shared document-list script
02-wa-gadget.txt  native WA CONTENT gadget(s), with the
                  exact content to paste
```

No `03-bottom`. Nothing sits under the cards.

## Wild Apricot setup

1. Open the page with slug `/bylaws-and-procedures`, restricted to members like the
   rest of the Member Hub.
2. Paste `dist/pages/bylaws-and-procedures/01-top.html` into a Custom HTML gadget at the
   top. `global.css` must already be live in the CSS tab.
3. Add one **Content** gadget below it, CSS class `ngm-wa-docs`, and
   paste the three blocks from `02-wa-gadget.txt` via the editor's source
   view.
4. All gadgets in the same layout row, row background transparent.

## Updating it

`docs/updating-bylaws.md` is the handout for whoever maintains the page:
plain editor steps, no HTML. The HTML paste is a one-time setup.

## Notes

- Group cards have no year in their title, so the script doesn't
  reorder them. They show in gadget order.
- The script is shared verbatim with `board-minutes` and
  `newsletter-archive`. Change all three together.
