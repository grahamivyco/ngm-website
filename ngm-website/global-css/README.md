# Global CSS

This folder holds the site-wide CSS for the WA **CSS** tab.

## The files

### `global.css` — PASTE THIS into Wild Apricot
Paste-ready, **minified** (~121 KB). This is the file you copy into WA's CSS box:
open it on GitHub → **Copy raw file** → paste into the CSS tab → Save.

> **Why minified:** WA's CSS box has a size limit the full readable stylesheet
> (~196 KB) exceeds — WA silently truncates it, dropping whatever sits at the end
> (that's what kept the member-profile skin from ever going live). The minified
> build fits, so it's what actually goes on the site.

### `global.source.css` — the readable MASTER (edit here)
The consolidated sage/cream NGM redesign, fully commented (~196 KB): design tokens,
reset, typography, layout, buttons, badges once at the top, then each page's styles
and the native WA gadget skins (login/account, calendar, member profile). **Make CSS
changes here** so it stays understandable, then regenerate `global.css` (below).

### `current-live-backup.css` — the RESTORE file
A snapshot of the old CSS that was live before the redesign. **Use it to revert:** if a
paste goes wrong, replace the WA CSS tab with this file and save to get back to a known
state.

## After editing `global.source.css`, regenerate `global.css`

```bash
python3 - <<'PY'
import re
src=open('global-css/global.source.css').read()
s=re.sub(r'/\*.*?\*/','',src,flags=re.S)
t=[]
s=re.sub(r'"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'|url\([^)]*\)',lambda m:(t.append(m.group(0)) or f"\x00{len(t)-1}\x00"),s)
s=re.sub(r'\s+',' ',s); s=re.sub(r'\s*([{}:;,>~+])\s*',r'\1',s); s=s.replace(';}','}').strip()
mini=re.sub(r'\x00(\d+)\x00',lambda m:t[int(m.group(1))],s)
assert mini.count('{')==mini.count('}'), "unbalanced braces"
open('global-css/global.css','w').write("/* NGM Global CSS - PASTE-READY (minified) - copy this whole file into Wild Apricot's CSS box. Do NOT hand-edit: the readable master is global.source.css; regenerate this from it after changes. */\n"+mini)
print('regenerated global.css:', len(open('global-css/global.css').read()), 'bytes')
PY
```
