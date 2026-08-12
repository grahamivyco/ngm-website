# Access denied (403)

**WA system page:** Access denied (403)

Shown when the visitor **IS signed in** but their account doesn't have
rights to the page — wrong membership level, or a lapsed / pending
membership. That is NOT the same as being signed out:

| | Access denied (403) | Authorization required |
|---|---|---|
| Visitor state | Signed in | Signed out |
| Problem | Account lacks rights | No session |
| Fix | Different membership / renew / different account | Sign in |

So this page must not simply say "log in" (that's the
`authorization-required` page's message). It offers three routes:
**Member Hub** (check membership + renewals), **Log in** (for someone
signed in under the wrong account), and a Contact link in the copy.

- `01-top.html` &mdash; markup only; styling comes from the Global CSS (must be live in WA).

The `.ngm-sys` intro-band skin lives in the master `global.css` (SYSTEM-PAGE INTRO BANDS section).
