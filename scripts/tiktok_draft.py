"""Editorial pass for TikTok candidates from scripts/tiktok_collect.py.

Same rules and output as scripts/x_draft.py (the model checks the thumbnail against the prompt,
rejects or drafts the entry); only the candidate folder and the id prefix differ, since TikTok
creators name the app they used (ChatGPT, Gemini ...) rather than a model version.

  python3 scripts/tiktok_draft.py       # then: python3 scripts/build.py
"""
import json
import re
import subprocess
import sys

import x_draft as X

X.CAND = X.ROOT / ".tt-candidates"
X.DONE = X.CAND / "done"


def ask(c):
    prefix = re.sub(r"[^a-z0-9]+", "-", c["model"].split(" / ")[0].lower()).strip("-")
    text = X.RULES.format(thumb=c["thumb"], prefix=prefix, modes=", ".join(X.MODES[c["kind"]]),
                          cat_line=f"- category: one of {', '.join(X.CATS[c['kind']])}",
                          cat_key=', "category": "..."',
                          model=c["model"], post=c["post_text"][:1500], prompt=c["prompt"])
    out = subprocess.run(["claude", "-p", "--model", "haiku", "--allowedTools", "Read", "--output-format", "text"],
                         input=text, capture_output=True, text=True, timeout=600).stdout
    m = re.search(r"\{.*\}", out, re.S)
    return json.loads(m.group(0)) if m else {"accept": False, "reason": "no answer"}


X.ask = ask

if __name__ == "__main__":
    sys.exit(X.main())
