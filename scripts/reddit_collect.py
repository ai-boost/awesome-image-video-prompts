"""Collect candidate prompts from Reddit, through the ego-browser session (Reddit blocks plain HTTP clients).

For each search: open Reddit's top results, visit each post, take the prompt from the post body or the
poster's own comments, and save a candidate with its first image or video poster. Candidates land where
scripts/x_collect.py puts them, so scripts/x_draft.py reviews and drafts them the same way.

  python3 scripts/reddit_collect.py --config scripts/reddit_queries.yaml
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
import urllib.parse
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(os.environ.get("X_CANDIDATES", ROOT / ".x-candidates"))
SPACE = "awesome-ivp reddit"
MARK = re.compile(r"^\s*(\*\*)?[^\n]{0,40}(prompt|提示词)[^\n]{0,40}$", re.I)


def ego(js):
    """Run a script in ego-browser; the script sets RESULT, which comes back as JSON."""
    tmp = OUT / f".ego-{hashlib.sha1(js.encode()).hexdigest()[:8]}.json"
    code = f"const t=await taskSpace({json.dumps(SPACE)}); const p=t.page('p1');\n" + js + \
        f"\nconst fs=await import('node:fs/promises'); await fs.writeFile({json.dumps(str(tmp))}, JSON.stringify(RESULT));"
    subprocess.run(["ego-browser", "nodejs"], input=code, capture_output=True, text=True, timeout=900)
    data = json.loads(tmp.read_text())
    tmp.unlink()
    return data


def search(q):
    sub = f"r/{q['sub']}/" if q.get("sub") else ""
    url = f"https://www.reddit.com/{sub}search/?q={urllib.parse.quote(q['query'])}&sort=top&t={q.get('t', 'month')}"
    return ego(f"""
await p.goto({json.dumps(url)}); await p.waitForTimeout(3500);
for (let i=0;i<3;i++){{ await p.evaluate(()=>window.scrollBy(0,3000)); await p.waitForTimeout(1500); }}
const RESULT=await p.evaluate(()=>[...new Set([...document.querySelectorAll('a[data-testid=post-title]')].map(a=>a.getAttribute('href')))]);""")


def fetch(links):
    return ego(f"""
const RESULT=[];
for (const h of {json.dumps(links)}) {{
  try {{
    await p.goto("https://www.reddit.com"+h); await p.waitForSelector('shreddit-post',{{timeout:20000}}); await p.waitForTimeout(2500);
    RESULT.push(await p.evaluate(()=>{{
      const sp=document.querySelector('shreddit-post'); const a=n=>sp.getAttribute(n)||'';
      const op=a('author');
      const imgs=[...sp.querySelectorAll('img')].map(i=>i.src).filter(s=>/(i|preview)\\.redd\\.it/.test(s));
      const poster=sp.querySelector('shreddit-player, shreddit-player-2')?.getAttribute('poster')||'';
      const own=[...document.querySelectorAll('shreddit-comment')].filter(c=>c.getAttribute('author')===op)
        .map(c=>c.querySelector('[slot=comment]')?.innerText||'');
      return {{url:location.href.split('?')[0], title:a('post-title'), author:op, score:+a('score'), posted:a('created-timestamp'),
        type:a('post-type'), nsfw:sp.hasAttribute('nsfw'), sub:a('subreddit-name'),
        body:sp.querySelector('[slot=text-body]')?.innerText||'', own, imgs, poster}};
    }}));
  }} catch(e) {{ RESULT.push({{url:h, error:String(e)}}); }}
}}""")


def norm(text):
    return re.sub(r"\W+", "", text.lower())[:300]


def known():
    urls, prompts = set(), set()
    for f in glob.glob(str(ROOT / "prompts/*/*.yaml")):
        e = yaml.safe_load(open(f, encoding="utf-8"))
        urls.add(e["source"]["url"].rstrip("/"))
        prompts.add(norm(e["prompt"]))
    for f in glob.glob(str(OUT / "**/*.json"), recursive=True):
        try:
            c = json.loads(Path(f).read_text())
            urls.add(c["url"].rstrip("/"))
            prompts.add(norm(c["prompt"]))
        except (ValueError, KeyError):
            pass
    return urls, prompts


def pick_prompt(post):
    """The longest block from the body or the poster's comments, minus any line that only announces it."""
    best = ""
    for block in [post["body"], *post["own"]]:
        lines = block.strip().splitlines()
        for i, line in enumerate(lines[:15]):
            if MARK.match(line) and i + 1 < len(lines):
                block = "\n".join(lines[i + 1:])
                break
        block = block.strip()
        if len(block) > len(best):
            best = block
    return best


def run(q):
    urls, prompts = known()
    links = [h for h in search(q) if "https://www.reddit.com" + h.rstrip("/") not in urls][: q.get("max", 10) * 2]
    print(f"{q['query']} in r/{q.get('sub', 'all')}: {len(links)} new posts", file=sys.stderr)
    saved = 0
    for post in fetch(links):
        if saved >= q.get("max", 10):
            break
        if post.get("error") or post["nsfw"] or post["score"] < q.get("min_score", 50):
            continue
        text = " ".join([post["title"], post["body"], *post["own"]])
        prompt = pick_prompt(post)
        media = next(iter(post["imgs"]), "") if q["kind"] == "image" else (post["poster"] or next(iter(post["imgs"]), ""))
        why = ("does not mention the model" if not re.search(q["model_re"], text, re.I) else
               "no prompt" if len(prompt) < 60 else "no media" if not media else
               "prompt already listed" if norm(prompt) in prompts else "")
        if why:
            print("skip", post["url"], why, file=sys.stderr)
            continue
        cid = "rd-" + post["url"].rstrip("/").split("/comments/")[1].split("/")[0]
        thumb = OUT / f"{cid}.jpg"
        # curl, not urllib: Reddit's image hosts drop urllib's TLS through a local proxy
        got = subprocess.run(["curl", "-sfL", "-m", "60", "-A", "Mozilla/5.0", "-o", str(thumb), media.replace("&amp;", "&")])
        if got.returncode:
            print("skip", post["url"], "image download failed", file=sys.stderr)
            continue
        (OUT / f"{cid}.json").write_text(json.dumps({
            "cid": cid, "kind": q["kind"], "model": q["model"], "url": post["url"].rstrip("/"),
            "handle": post["author"], "credit": post["author"], "likes": post["score"], "posted": post["posted"][:10],
            "source_name": f"u/{post['author']} on Reddit", "post_text": f"{post['title']}\n{post['body']}"[:1500],
            "prompt": prompt, "media": media, "thumb": str(thumb),
        }, ensure_ascii=False, indent=1))
        prompts.add(norm(prompt))
        saved += 1
    print(f"saved {saved} candidates for {q['model']}", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True, help="YAML list of {model, kind, model_re, query, sub, t, min_score, max}")
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    for q in yaml.safe_load(open(a.config, encoding="utf-8")):
        try:
            run(q)
        except Exception as e:  # one failed search must not stop the rest
            print("search failed", q["query"], repr(e), file=sys.stderr)
        time.sleep(15)


if __name__ == "__main__":
    main()
