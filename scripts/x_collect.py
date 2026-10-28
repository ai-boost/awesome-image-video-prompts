"""Collect candidate prompts from X posts, using the ego-browser session that is signed in to X.

For one model and one query: search top posts, keep those with media and enough likes that are
not in the list yet, open each post, pull the prompt from the post or the author's own replies,
and save a candidate with its thumbnail. scripts/x_draft.py turns candidates into entries.

  python3 scripts/x_collect.py --model "Seedance 2.5" --kind video \
      --query '"Seedance 2.5" prompt min_faves:300 filter:videos' --max 15
  python3 scripts/x_collect.py --config scripts/x_queries.yaml      # every search in the weekly list

Candidates land in .x-candidates/ (git-ignored). Keep runs small: this is a real account.
"""
import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(os.environ.get("X_CANDIDATES", ROOT / ".x-candidates"))
SPACE = "awesome-ivp x refresh"

# A line that only announces the prompt ("Prompt:", "Prompt 👇", "提示词：", "Full prompt below").
MARK = re.compile(r"^\s*(\*\*)?[^\n]{0,30}(prompt|提示词)[^\n]{0,30}$", re.I)


def ego(js):
    """Run a script in ego-browser; the script must write JSON to the path in TMP."""
    tmp = OUT / f".ego-{hashlib.sha1(js.encode()).hexdigest()[:8]}.json"
    code = f"const TMP={json.dumps(str(tmp))};\nconst t=await taskSpace({json.dumps(SPACE)}); const p=t.page('p1');\n" + js + \
        "\nconst fs=await import('node:fs/promises'); await fs.writeFile(TMP, JSON.stringify(RESULT));"
    subprocess.run(["ego-browser", "nodejs"], input=code, capture_output=True, text=True, timeout=900)
    data = json.loads(tmp.read_text())
    tmp.unlink()
    return data


def search(query, rounds=6):
    js = f"""
await p.goto("https://x.com/search?q="+encodeURIComponent({json.dumps(query)})+"&src=typed_query&f=top");
await p.waitForSelector('article',{{timeout:20000}}).catch(()=>{{}});
const seen=new Map();
for(let i=0;i<{rounds};i++){{
  const rows=await p.evaluate(()=>[...document.querySelectorAll('article')].map(a=>({{
    link:[...a.querySelectorAll('a[href*="/status/"]')].map(x=>x.getAttribute('href')).find(h=>/^\\/[^/]+\\/status\\/\\d+$/.test(h)),
    stats:a.querySelector('[role=group]')?.getAttribute('aria-label')||'',
    media:!!a.querySelector('video,[data-testid=videoPlayer],[data-testid=tweetPhoto]')}})));
  for(const r of rows) if(r.link) seen.set(r.link,r);
  await p.evaluate(()=>window.scrollBy(0,2500)); await p.waitForTimeout(1800);
}}
const RESULT=[...seen.values()];"""
    return ego(js)


def fetch_posts(urls):
    js = f"""
const RESULT=[];
for (const u of {json.dumps(urls)}){{
  try{{
    await p.goto(u); await p.waitForSelector('article',{{timeout:20000}}); await p.waitForTimeout(2500);
    await p.evaluate(()=>document.querySelectorAll('[data-testid=tweet-text-show-more-link]').forEach(b=>b.click()));
    await p.waitForTimeout(800);
    const handle=u.split('/')[3].toLowerCase();
    const arts=await p.evaluate(()=>[...document.querySelectorAll('article')].map(a=>({{
      user:([...a.querySelectorAll('[data-testid=User-Name] a')].map(x=>x.getAttribute('href'))[0]||'').slice(1).toLowerCase(),
      name:a.querySelector('[data-testid=User-Name] span')?.innerText||'',
      text:a.querySelector('[data-testid=tweetText]')?.innerText||'',
      stats:a.querySelector('[role=group]')?.getAttribute('aria-label')||'',
      time:a.querySelector('time')?.getAttribute('datetime')||'',
      poster:[...a.querySelectorAll('video')].map(v=>v.poster).filter(Boolean)[0]||'',
      imgs:[...a.querySelectorAll('[data-testid=tweetPhoto] img')].map(i=>i.src)}})));
    const own=arts.filter(a=>a.user===handle);
    RESULT.push({{url:u,main:own[0]||arts[0],thread:own.slice(1).map(a=>a.text).filter(Boolean)}});
  }}catch(e){{RESULT.push({{url:u,error:String(e.message||e)}});}}
  await p.waitForTimeout(2000);
}}"""
    return ego(js)


def likes(stats):
    m = re.search(r"([\d,]+) likes", stats or "")
    return int(m.group(1).replace(",", "")) if m else 0


def extract(text):
    """Drop everything up to the last line that only announces the prompt, then an inline 'Prompt:'."""
    lines = text.split("\n")
    cut = max([i for i, l in enumerate(lines[:25]) if MARK.match(l) and len(l) < 60] or [-1])
    body = "\n".join(lines[cut + 1:]).strip()
    body = re.sub(r"^\s*(prompt|提示词)\s*[:：-]\s*", "", body, flags=re.I)
    body = re.sub(r"(\n\s*(#\S+\s*)+)+\s*$", "", body)
    return "\n".join(l.rstrip() for l in body.strip().split("\n"))


def pick_prompt(post):
    """The longest prompt-looking text among the post and the author's replies."""
    texts = [post["main"]["text"]] + post.get("thread", [])
    best = max(texts, key=len)
    raw = best
    p = extract(best)
    # X cuts long posts near 4,000 characters; a cut prompt is useless.
    truncated = 3850 <= len(raw) <= 4000 and p[-1:] not in ".。」!！)）\"”’'"
    return p, truncated


def known_urls():
    urls = set()
    for f in glob.glob(str(ROOT / "prompts/*/*.yaml")):
        urls.add(yaml.safe_load(open(f, encoding="utf-8"))["source"]["url"])
    return urls


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", help="YAML list of {model, kind, query, max, min_likes}")
    ap.add_argument("--model")
    ap.add_argument("--kind", choices=["video", "image"])
    ap.add_argument("--query")
    ap.add_argument("--min-likes", type=int, default=150)
    ap.add_argument("--max", type=int, default=15)
    a = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    if a.config:
        for q in yaml.safe_load(open(a.config, encoding="utf-8")):
            run(argparse.Namespace(model=q["model"], kind=q["kind"], query=q["query"],
                                   min_likes=q.get("min_likes", 150), max=q.get("max", 10)))
            time.sleep(20)
    else:
        if not (a.model and a.kind and a.query):
            ap.error("--model, --kind and --query are required without --config")
        run(a)


def run(a):

    seen = known_urls() | {json.loads(open(f).read())["url"] for f in glob.glob(str(OUT / "*.json"))}
    found = search(a.query) or search(a.query)  # X sometimes renders an empty first page
    hits = [r for r in found if r["media"] and likes(r["stats"]) >= a.min_likes]
    urls = [u for u in ("https://x.com" + r["link"] for r in sorted(hits, key=lambda r: -likes(r["stats"]))) if u not in seen][: a.max]
    print(f"{len(hits)} posts with media over {a.min_likes} likes, {len(urls)} new", file=sys.stderr)
    saved = 0
    for post in fetch_posts(urls):
        try:
            saved += save(a, post)
        except Exception as e:  # one bad post must not lose the rest
            print("skip", post.get("url"), repr(e), file=sys.stderr)
    print(f"saved {saved} candidates for {a.model}", file=sys.stderr)


def save(a, post):
    """Write one candidate and its thumbnail; return 1 when saved."""
    if post.get("error") or not post.get("main"):
        return 0
    alltext = " ".join([post["main"]["text"], *post.get("thread", [])]).lower()
    if a.model.split()[0].lower() not in alltext:
        print("skip", post["url"], "does not mention", a.model, file=sys.stderr)
        return 0
    prompt, truncated = pick_prompt(post)
    m = post["main"]
    media = m["poster"] if a.kind == "video" else (m["imgs"][0] if m["imgs"] else m["poster"])
    if truncated or len(prompt) < 60 or not media:
        print("skip", post["url"], "truncated" if truncated else "no prompt or media", file=sys.stderr)
        return 0
    cid = post["url"].rstrip("/").split("/")[-1]
    thumb = OUT / f"{cid}.jpg"
    urllib.request.urlretrieve(re.sub(r"name=\w+", "name=medium", media), thumb)
    (OUT / f"{cid}.json").write_text(json.dumps({
        "cid": cid, "kind": a.kind, "model": a.model, "url": post["url"],
        "handle": post["url"].split("/")[3], "credit": m["name"], "likes": likes(m["stats"]),
        "posted": m["time"][:10], "post_text": m["text"], "prompt": prompt,
        "media": media, "thumb": str(thumb),
    }, ensure_ascii=False, indent=1))
    return 1


if __name__ == "__main__":
    main()
