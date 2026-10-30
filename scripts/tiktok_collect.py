"""Turn TikTok posts that contain a prompt into candidates for scripts/tiktok_draft.py.

Input is a JSONL file with one prompt per line: {"video_id", "prompt", "type": "image"|"video"}.
The posts were found by mining public TikTok captions for prompts; this script re-reads each post
from TikTok itself, so every entry carries the post as it is now:
  - the prompt must still appear in the caption, word for word
  - the caption must name the tool the creator used (ChatGPT, Gemini, Veo ...), which becomes the model
  - the cover (or first photo) becomes the thumbnail the editor checks against the prompt
  - at most PER_AUTHOR prompts per creator, so one account cannot fill a section
Candidates go to .tt-candidates/<cid>.json and .jpg.

  python3 scripts/tiktok_collect.py prompts.jsonl
"""
import hashlib
import json
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAND = ROOT / ".tt-candidates"
FFMPEG = shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg"
API = "https://www.tikwm.com/api/?hd=1&url="
PER_AUTHOR = 3  # input is sorted by views, so each creator keeps their most-viewed prompts
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"}

# Tools a caption may name, most specific first. Several matches mean the creator says it works in each.
TOOLS = [
    (r"nano\s?banana\s?pro", "Nano Banana Pro"),
    (r"nano\s?banana", "Nano Banana"),
    (r"chat\s?gpt|\bgpt\b", "ChatGPT"),
    (r"gemini", "Gemini"),
    (r"\bveo\b", "Veo"),
    (r"kling", "Kling"),
    (r"seedance", "Seedance"),
    (r"hailuo", "Hailuo"),
    (r"\bsora\b", "Sora"),
    (r"\bgrok\b", "Grok"),
    (r"midjourney", "Midjourney"),
    (r"dreamina", "Dreamina"),
    (r"higgsfield", "Higgsfield"),
    (r"capcut", "CapCut"),
]


def model_of(caption):
    names = []
    for rx, name in TOOLS:
        if re.search(rx, caption, re.I) and not any(name in n or n in name for n in names):
            names.append(name)
    return " / ".join(names[:2]) if names else None


def comparable(s):
    s = re.sub(r"[​-‏⁠﻿\U0001F000-\U0001FAFF☀-➿️]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def fetch(video_id):
    url = API + urllib.parse.quote(f"https://www.tiktok.com/@_/video/{video_id}")
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        d = json.load(r)
    return d.get("data") if d.get("code") == 0 else None


def save_jpg(src_url, path):
    tmp = path.with_suffix(".src")
    with urllib.request.urlopen(urllib.request.Request(src_url, headers=UA), timeout=30) as r:
        tmp.write_bytes(r.read())
    subprocess.run([FFMPEG, "-v", "error", "-y", "-i", str(tmp), "-frames:v", "1", str(path)], check=True)
    tmp.unlink()


def main(inp):
    CAND.mkdir(exist_ok=True)
    stats, per_author = {}, {}
    for line in open(inp):
        p = json.loads(line)
        if p["type"] not in ("image", "video"):
            continue
        cid = f"tt-{p['video_id']}-{hashlib.sha1(p['prompt'].encode()).hexdigest()[:6]}"
        if (CAND / f"{cid}.json").exists() or (CAND / "done" / f"{cid}.json").exists():
            continue
        try:
            d = fetch(p["video_id"])
        except Exception as e:  # network or API hiccup: count and move on
            d, why = None, f"fetch error {type(e).__name__}"
        else:
            why = "post gone"
        time.sleep(1.1)  # tikwm allows about one request per second
        caption, model = "", None
        if d:
            caption = d.get("title") or ""
            model = model_of(caption)
            if comparable(p["prompt"]) not in comparable(caption):
                why, d = "prompt not in caption", None
            elif not model:
                why, d = "no tool named", None
        if not d:
            stats[why] = stats.get(why, 0) + 1
            continue
        handle = d["author"]["unique_id"]
        per_author[handle] = per_author.get(handle, 0) + 1
        if per_author[handle] > PER_AUTHOR:
            stats["author limit"] = stats.get("author limit", 0) + 1
            continue
        thumb = CAND / f"{cid}.jpg"
        try:
            save_jpg((d.get("images") or [None])[0] or d.get("origin_cover") or d["cover"], thumb)
        except Exception:
            stats["no thumbnail"] = stats.get("no thumbnail", 0) + 1
            continue
        c = {"cid": cid, "kind": p["type"], "model": model, "prompt": p["prompt"], "post_text": caption,
             "url": f"https://www.tiktok.com/@{handle}/video/{d['id']}", "handle": handle,
             "credit": d["author"].get("nickname") or handle, "source_name": f"@{handle} on TikTok",
             "likes": int(d.get("digg_count") or 0),
             "posted": datetime.fromtimestamp(int(d["create_time"]), timezone.utc).date().isoformat(),
             "thumb": str(thumb)}
        (CAND / f"{cid}.json").write_text(json.dumps(c, ensure_ascii=False, indent=1))
        stats["candidate"] = stats.get("candidate", 0) + 1
    print(stats)


if __name__ == "__main__":
    main(sys.argv[1])
