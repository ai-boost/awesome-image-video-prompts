"""Collect candidate prompts from X posts, using the ego-browser session that is signed in to X.

For one model and one query: search top posts, keep those with media and enough likes that are
not in the list yet, open each post, pull the prompt from the post or the author's own replies,
and save a candidate with its thumbnail. scripts/x_draft.py turns candidates into entries.

  python3 scripts/x_collect.py --model "Seedance 2.5" --kind video \
      --query '"Seedance 2.5" prompt min_faves:300 filter:videos' --max 15
  python3 scripts/x_collect.py --config scripts/x_queries.yaml      # every search in the weekly list
  python3 scripts/x_collect.py --model "GPT Image 2.6" --kind image --urls leads.txt   # posts found elsewhere

An image post whose output is an animated GIF keeps the GIF (anim) and a frame sheet for the review.

Candidates land in .x-candidates/ (git-ignored). Keep runs small: this is a real account.
"""
import argparse
import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(os.environ.get("X_CANDIDATES", ROOT / ".x-candidates"))
FFMPEG = shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg"
# Runs in the Ego Lite profile "Default", where X is signed in; ego's default profile is a different one.
SPACE = "awesome-ivp x refresh"

# A line that only announces the prompt ("Prompt:", "Prompt 👇", "提示词：", "Full prompt below").
MARK = re.compile(r"^\s*(\*\*)?[^\n]{0,30}(prompt|提示词)[^\n]{0,30}$", re.I)


def ego(js):
    """Run a script in ego-browser; the script must write JSON to the path in TMP."""
    tmp = OUT / f".ego-{hashlib.sha1(js.encode()).hexdigest()[:8]}.json"
    code = f"const TMP={json.dumps(str(tmp))};\nconst N={json.dumps(SPACE)};const ex=(await listTaskSpaces()).find(s=>s.name===N);if(ex&&ex.profileId!=='Default')throw new Error(N+' is in profile '+ex.profileId+', not Default');const t=ex?await taskSpace(ex.id):await taskSpace(N,{{profileId:'Default'}}); const p=t.page('p1');\n" + js + \
        "\nconst fs=await import('node:fs/promises'); await fs.writeFile(TMP, JSON.stringify(RESULT));"
    subprocess.run(["ego-browser", "nodejs"], input=code, capture_output=True, text=True, timeout=900)
    data = json.loads(tmp.read_text())
    tmp.unlink()
    return data


def search(query, rounds=6, tab="top"):
    js = f"""
await p.goto("https://x.com/search?q="+encodeURIComponent({json.dumps(query)})+"&src=typed_query&f={tab}");
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
    // X auto-translates posts for this account; a prompt must be the author's own words, so switch every post back.
    const original=(click)=>p.evaluate((click)=>{{const bs=[...document.querySelectorAll('article *')].filter(e=>e.childElementCount===0&&e.textContent.trim()==='Show original').map(e=>e.closest('button,[role=button],a')||e); if(click) bs.forEach(b=>b.click()); return bs.length;}},click);
    if(await original(true)) await p.waitForTimeout(1500);
    if(await original(false)) throw new Error('still showing X translations');
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


def faves(query):
    """The like threshold a query already asks X for, so results are not filtered twice."""
    m = re.search(r"min_faves:(\d+)", query)
    return int(m.group(1)) if m else 150


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", help="YAML list of {model, kind, query, max, min_likes, months, tab, model_re}; months limits a seasonal query "
                    "to those months, tab=live searches Latest instead of Top, model_re is the pattern a post must match to count for the model")
    ap.add_argument("--model")
    ap.add_argument("--kind", choices=["video", "image"])
    ap.add_argument("--query")
    ap.add_argument("--min-likes", type=int, help="defaults to the query's min_faves, else 150")
    ap.add_argument("--max", type=int, default=15)
    ap.add_argument("--tab", default="top", choices=["top", "live"])
    ap.add_argument("--model-re", help="pattern a post must match to count for the model; defaults to the model's first word")
    ap.add_argument("--urls", help="file of post URLs found elsewhere, fetched instead of searching")
    a = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    if a.config:
        for q in yaml.safe_load(open(a.config, encoding="utf-8")):
            if "months" in q and time.localtime().tm_mon not in q["months"]:
                continue
            run(argparse.Namespace(model=q["model"], kind=q["kind"], query=q["query"], urls=None, tab=q.get("tab", "top"),
                                   model_re=q.get("model_re"), min_likes=q.get("min_likes", faves(q["query"])), max=q.get("max", 10)))
            time.sleep(20)
    else:
        if not (a.model and a.kind and (a.query or a.urls)):
            ap.error("--model, --kind and --query or --urls are required without --config")
        a.min_likes = a.min_likes if a.min_likes is not None else faves(a.query or "")
        run(a)


def run(a):

    seen = known_urls() | {json.loads(open(f).read())["url"] for f in glob.glob(str(OUT / "*.json"))}
    if a.urls:
        leads = dict.fromkeys(re.sub(r"https://(?:www\.)?twitter\.com", "https://x.com", l.strip().split("?")[0])
                              for l in open(a.urls) if "/status/" in l)
        urls = [u for u in leads if u not in seen][: a.max]
        print(f"{len(leads)} leads, {len(urls)} new", file=sys.stderr)
    else:
        found = search(a.query, tab=a.tab) or search(a.query, tab=a.tab)  # X sometimes renders an empty first page
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
    alltext = " ".join([post["main"]["text"], *post.get("thread", [])])
    if not re.search(getattr(a, "model_re", None) or re.escape(a.model.split()[0]), alltext, re.I):
        print("skip", post["url"], "does not mention", a.model, file=sys.stderr)
        return 0
    prompt, truncated = pick_prompt(post)
    m = post["main"]
    media = m["poster"] if a.kind == "video" else (m["imgs"][0] if m["imgs"] else m["poster"])
    cid = post["url"].rstrip("/").split("/")[-1]
    anim = gif_of(cid) if a.kind == "image" and not m["imgs"] else None
    # A GIF prompt is often one short line ("make a GIF of a pelican riding a bicycle"); a still needs more to be a prompt.
    if truncated or len(prompt) < (12 if anim else 60) or not media:
        print("skip", post["url"], "truncated" if truncated else "no prompt or media", file=sys.stderr)
        return 0
    thumb = OUT / f"{cid}.jpg"
    get(re.sub(r"name=\w+", "name=medium", media), thumb)
    extra = {}
    if anim:
        extra = {"anim": str(anim), "sheet": str(OUT / f"{cid}-sheet.jpg")}
        subprocess.run([FFMPEG, "-v", "error", "-y", "-i", str(anim), "-vf", "fps=4,scale=240:-2,tile=4x1", "-frames:v", "1",
                        extra["sheet"]], check=True)
    (OUT / f"{cid}.json").write_text(json.dumps({
        "cid": cid, "kind": a.kind, "model": a.model, "url": post["url"],
        "handle": post["url"].split("/")[3], "credit": m["name"], "likes": likes(m["stats"]),
        "posted": m["time"][:10], "post_text": m["text"], "prompt": prompt,
        "media": media, "thumb": str(thumb), **extra,
    }, ensure_ascii=False, indent=1))
    return 1


def get(url, path=None):
    """Download with retries: X's media and syndication hosts answer 403 for a while after a burst of requests."""
    for wait in (0, 10, 30, 90):
        time.sleep(wait)
        try:
            data = urllib.request.urlopen(url, timeout=60).read()
            return path.write_bytes(data) if path else data
        except urllib.error.HTTPError as e:
            if e.code not in (403, 429) or wait == 90:
                raise


def gif_of(cid):
    """The MP4 that X serves for a post's animated GIF, saved next to the candidate; None when the post has no GIF.
    A post's video counts only when it is GIF length: longer ones are screen recordings or clips, not the output."""
    url = f"https://cdn.syndication.twimg.com/tweet-result?id={cid}&token=a"
    for md in json.loads(get(url)).get("mediaDetails", []):
        vi = md.get("video_info") or {}
        if md.get("type") == "animated_gif" or (md.get("type") == "video" and vi.get("duration_millis", 1e9) <= 8000):
            mp4 = max((v for v in vi.get("variants", []) if v.get("content_type") == "video/mp4"),
                      key=lambda v: v.get("bitrate", 0), default=None)
            if mp4:
                path = OUT / f"{cid}.mp4"
                get(mp4["url"], path)
                return path
    return None


if __name__ == "__main__":
    main()
