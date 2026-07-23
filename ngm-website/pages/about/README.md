# About

**WA page:** About  ·  **Structure:** SINGLE Custom HTML gadget — `01-top.html`.
Sections: Hero, History, Member perks, Photo bento gallery, Come Visit (closing CTA).
(The former "Mission" values cards were merged into the belonging/learning/craft
purpose line above the member-perk tiles.)

**Photo bento gallery:** a responsive masonry grid (`.ngm-bento`) under Member
perks. Each `.ngm-bento-item` tile holds one photo; size it with
`ngm-bento-big` (2×2), `ngm-bento-wide` (2×1), `ngm-bento-tall` (1×2), or leave
plain for 1×1. Tiles currently use `REPLACE_WITH_GALLERY_PHOTO_N` placeholders
that fall back to known-good gallery photos via `onerror` — swap in real URLs
from `…/resources/Pictures/Gallery Photos/`. Add or remove tiles freely; the
grid reflows at every width (4 cols → 3 → 2).

This is the PUBLIC version: the Leadership section shows roles + role
emails only, no personal names. Names live in the archived with-names copy
(`about-page-WITH-NAMES-member-hub.html`) used for the members-only Member Hub.

## Open TODO
- Leadership: role-based emails rarely change — only update when a role is
  added or retired.
