#!/usr/bin/env python3
"""Build ngm-website/dist — PRODUCTION-CLEAN copies of every paste file.

The canonical sources (pages/, system-pages/, layout/, global-css/) keep
their maintainer comments; this tool writes comment-stripped twins under
dist/ with the same relative paths. Paste INTO Wild Apricot from dist/;
edit only the sources, then re-run:

    python3 ngm-website/tools/build-dist.py

What gets stripped:
  - HTML comments (<!-- ... -->)
  - CSS comments (/* ... */) in <style> blocks and in global.css
  - JS block comments (/* ... */) and whole-line // comments in <script>
  - runs of blank lines collapse to one

Never hand-edit dist/ — it is overwritten on every run.
"""
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"


def strip_css(text: str) -> str:
    return re.sub(r"/\*[\s\S]*?\*/", "", text)


def strip_js(text: str) -> str:
    # Safe for this codebase: no JS string/regex literal contains "/*",
    # and no code line begins with "//" that isn't a comment.
    text = re.sub(r"/\*[\s\S]*?\*/", "", text)
    text = re.sub(r"(?m)^[ \t]*//.*$", "", text)
    return text


def tidy(text: str) -> str:
    text = re.sub(r"\n[ \t]+\n", "\n\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.lstrip("\n")


def clean_html(text: str) -> str:
    text = re.sub(r"<!--[\s\S]*?-->", "", text)
    text = re.sub(
        r"(<style[^>]*>)([\s\S]*?)(</style>)",
        lambda m: m.group(1) + tidy(strip_css(m.group(2))) + m.group(3),
        text,
    )
    text = re.sub(
        r"(<script[^>]*>)([\s\S]*?)(</script>)",
        lambda m: m.group(1) + tidy(strip_js(m.group(2))) + m.group(3),
        text,
    )
    return tidy(text)


def main() -> int:
    if DIST.exists():
        shutil.rmtree(DIST)

    built = []
    for base in ("layout", "pages", "system-pages"):
        for src in sorted((ROOT / base).rglob("*.html")):
            if "mockups" in src.parts:
                continue
            out = DIST / src.relative_to(ROOT)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(clean_html(src.read_text(encoding="utf-8")), encoding="utf-8")
            built.append(out)

    css_src = ROOT / "global-css" / "global.css"
    css_out = DIST / "global-css" / "global.css"
    css_out.parent.mkdir(parents=True, exist_ok=True)
    cleaned = tidy(strip_css(css_src.read_text(encoding="utf-8")))
    css_out.write_text(cleaned, encoding="utf-8")
    built.append(css_out)

    # sanity: brace balance must survive the strip
    if cleaned.count("{") != cleaned.count("}"):
        print("ERROR: global.css brace count changed after stripping", file=sys.stderr)
        return 1

    # ONE-GADGET PAGES — for every sandwich page (01-top + 03-bottom around
    # a native WA gadget), emit <page>/one-gadget.html: paste it as a SINGLE
    # Custom-HTML gadget ABOVE the native gadget. The top half renders in
    # place; the bottom half ships hidden and moves itself to just AFTER
    # the first native (non-CustomHTML) gadget that follows, then reveals —
    # the footer's lift-and-reveal pattern, so there is no flash.
    MOVER = """<script>
(function(){
  function cls(el){ var c=el.className; return typeof c==='string'?c:''; }
  function isNative(el){ var c=cls(el); return /WaGadget[A-Z]/.test(c) && c.indexOf('WaGadgetCustomHTML')===-1; }
  function mine(bot){ var p=bot.parentNode; while(p&&p!==document.body){ if(/WaGadgetCustomHTML/.test(cls(p))) return p; p=p.parentNode; } return null; }
  function findNative(bot){
    var own=mine(bot), all=document.querySelectorAll('[class*="WaGadget"]'), after=null, any=null;
    for(var i=0;i<all.length;i++){
      var el=all[i];
      if(!isNative(el)) continue;
      if(own&&(el.contains(own)||own.contains(el))) continue;
      if(el.contains(bot)) continue;
      if(!any) any=el;
      if(own&&!after&&(own.compareDocumentPosition(el)&Node.DOCUMENT_POSITION_FOLLOWING)) after=el;
    }
    return after||any;
  }
  function anchorFor(el){
    var a=el,p=a.parentNode;
    while(p&&p!==document.body){
      var c=cls(p), t=p.tagName;
      if(/WaLayoutItem|WaLayoutContainer|WaLayoutTable|WaLayoutRow/.test(c)||t==='TD'||t==='TR'||t==='TBODY'||t==='TABLE'){ a=p; p=a.parentNode; }
      else break;
    }
    /* climb out of WA's unclassed gadget-stack wrapper (it carries inline
       padding, which was insetting the moved band) and land as a direct
       child of the placeholder, still after the native gadget */
    while(a.parentNode&&a.parentNode!==document.body&&a.parentNode.tagName==='DIV'&&!/WaPlaceHolder|WaGadget/.test(cls(a.parentNode))){ a=a.parentNode; }
    return a;
  }
  function place(tries){
    var bot=document.getElementById('ngm-pg-bottom'); if(!bot) return;
    var native=findNative(bot);
    if(native){
      var a=anchorFor(native);
      if(a.parentNode) a.parentNode.insertBefore(bot,a.nextSibling);
      /* wear the custom-HTML gadget classes so every full-bleed rule that
         zeroes gadget padding applies to the moved band too */
      bot.className='WaGadget WaGadgetCustomHTML gadgetStyleNone';
      bot.style.display='';
      return;
    }
    if(tries>0){ setTimeout(function(){ place(tries-1); },100); return; }
    bot.style.display='';
  }
  function start(){ place(30); }
  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',start);}else{start();}
})();
</script>
"""
    combined = 0
    for base in ("pages", "system-pages"):
        for d in sorted((ROOT / base).iterdir()):
            top, bot = d / "01-top.html", d / "03-bottom.html"
            if not (top.is_file() and bot.is_file()):
                continue
            top_html = clean_html(top.read_text(encoding="utf-8")).strip()
            bot_html = clean_html(bot.read_text(encoding="utf-8")).strip()
            # BALANCE THE HALVES. Some pages (calendar) deliberately leave
            # wrappers open in 01-top and close them in 03-bottom, so the
            # native gadget sits INSIDE them. Wrapped in one div that would
            # end #ngm-pg-bottom early — only the first section would move.
            # Move those trailing opening tags into the bottom half instead.
            opens, i = [], None
            for m in re.finditer(r"<(div|section)\b[^>]*>|</(?:div|section)\s*>", top_html, re.I):
                if m.group(0).startswith("</"):
                    if opens:
                        opens.pop()
                else:
                    opens.append(m.start())
            if opens:
                i = opens[0]
                tail = top_html[i:]
                if re.sub(r"<[^>]+>", "", tail).strip() == "":
                    top_html, bot_html = top_html[:i].rstrip(), tail.strip() + "\n" + bot_html
                else:  # content after the open tag: close here, reopen below
                    names = re.findall(r"<(div|section)\b[^>]*>", tail, re.I)
                    top_html += "".join("</%s>" % n for n in reversed(names))
                    bot_html = "".join(re.findall(r"<(?:div|section)\b[^>]*>", tail, re.I)) + "\n" + bot_html
            out = DIST / base / d.name / "one-gadget.html"
            out.write_text(
                top_html + "\n\n"
                + '<div id="ngm-pg-bottom" style="display:none">\n'
                + bot_html
                + "\n</div>\n" + MOVER,
                encoding="utf-8",
            )
            built.append(out)
            combined += 1
    print(f"one-gadget pages: {combined}")

    # ONE-PASTE SITE CHROME — header + footer + feedback pill in a single
    # gadget. Paste it at the BOTTOM of the page template (the footer's
    # slot): the header lifts itself to <body> and is position:fixed, the
    # pill floats, and the footer renders right where the gadget sits.
    # Replaces the three separate template gadgets.
    chrome = "\n\n".join(
        (DIST / rel).read_text(encoding="utf-8").strip()
        for rel in (
            "layout/header/01-top.html",
            "layout/footer/01-top.html",
            "layout/feedback-button/01-top.html",
        )
    ) + "\n"
    chrome_out = DIST / "layout" / "site-chrome" / "01-top.html"
    chrome_out.parent.mkdir(parents=True, exist_ok=True)
    chrome_out.write_text(chrome, encoding="utf-8")
    built.append(chrome_out)

    (DIST / "README.md").write_text(
        "# dist — production paste copies (GENERATED)\n\n"
        "Comment-free twins of every paste file. Paste into Wild Apricot\n"
        "from HERE. Never edit these — edit the sources and re-run\n"
        "`python3 ngm-website/tools/build-dist.py`.\n",
        encoding="utf-8",
    )
    print(f"dist built: {len(built)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
