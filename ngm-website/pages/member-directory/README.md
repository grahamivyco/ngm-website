# Member Directory  (members-only)

A custom page that **wraps** Wild Apricot's native **Member Directory** gadget. A
short branded intro band sits above the gadget, and a compact "keep your listing
current" band sits below it — the "sandwich" pattern. The searchable list of
members is the native WA gadget itself; we don't rebuild it.

## Sections (top to bottom)
1. **Intro band** (`01-top.html`) — eyebrow, heading, and one intro paragraph
   explaining what the directory is and who can see it.
2. **Native Member Directory gadget** (`02-wa-gadget.txt`) — WA's built-in gadget,
   in its own slot. Inherits styling from the Global CSS; nothing to paste.
3. **Keep your listing current** (`03-bottom.html`) — reminds members their entry
   comes from their own profile, with buttons to edit it or adjust privacy.

## Wild Apricot setup (the sandwich)
1. Create a new page (e.g. **Member Directory** at `/member-directory`).
2. **Restrict it to members** — page settings → Access → *Members only*.
3. Add three gadgets, top to bottom:
   - **Custom HTML** gadget → paste `01-top.html`.
   - **Member Directory** (native WA gadget) → default settings.
   - **Custom HTML** gadget → paste `03-bottom.html`.

## Profile links (the important part)
The bottom band's two buttons point at **bare** `/Sys/Profile` and
`/Sys/Profile/Privacy` paths — **no `?memberId=`**. WA resolves a bare path to
*whoever is logged in*, so every member edits their own listing. **Never add a
member ID** — a hardcoded ID would expose one person's profile to everyone.

## Styling
`01-top.html` and `03-bottom.html` are markup only — no inline `<style>`/fonts.
Styling comes from the Global CSS (it carries the `.ngm-*` base classes and the
`.ngm-dir-*` skins), which must be live in WA.
