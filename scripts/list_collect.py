"""Collect candidate prompts from open-licensed prompt collections on GitHub, without touching X.

Each source is a JSON export that keeps the original post link, date and result media for every case.
Cases already in the list are skipped. Candidates land where scripts/x_collect.py puts them, so
scripts/x_draft.py reviews and drafts them the same way.

  python3 scripts/list_collect.py --since 2026-07-01            # every source
  python3 scripts/list_collect.py --only H3 --max 50
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUT = Path(os.environ.get("X_CANDIDATES", ROOT / ".x-candidates"))
# A line that only announces the prompt ("Prompt:", "Seedance 2.5 prompt 👇", "提示词：").
MARK = re.compile(r"^\s*(\*\*)?[^\n]{0,30}(prompt|提示词)[^\n]{0,30}$", re.I)



def seedance(c):
    """LearnPrompt/awesome-seedance: posts checked against the original, scored by weighted interactions."""
    if not (c.get("provenanceVerified") and c.get("promptFull")):
        return None
    return {"url": c.get("sourceUrl"), "posted": c.get("sourcePublishedAt"), "score": c.get("weightedInteractions"),
            "likes": None, "credit": None, "prompt": c["promptFull"], "poster": c.get("posterUrl"),
            "media": c.get("mediaUrl"), "text": " ".join(str(c.get(k) or "") for k in ("promptFull", "title", "titleEn", "summary", "summaryEn"))}


PER_AUTHOR = 4  # most candidates one author can add per source and run

H3_SITE = "https://awesome-minimax-h3-cases.zzskysilent.com"


def h3(c):
    """SkyNotSilent/awesome-MiniMax-H3-cases: only prompts the creator published in full, scored by likes."""
    likes = (c.get("engagement") or {}).get("likes")
    if c.get("promptProvenance") != "creator-verbatim" or not likes:
        return None
    return {"url": c.get("sourceUrl"), "posted": c.get("publishedAt"), "score": likes, "likes": likes,
            "credit": c.get("author"), "prompt": c["prompt"], "poster": H3_SITE + c["posterUrl"],
            "media": H3_SITE + c["mediaUrl"], "text": " ".join(str(c.get(k) or "") for k in ("sourceCaption", "summaryEn", "model"))}


def x_date(url):
    """Post date from an X status id (the id encodes its creation time)."""
    m = re.search(r"/status/(\d+)", url or "")
    if not m:
        return None
    return datetime.fromtimestamp(((int(m.group(1)) >> 22) + 1288834974657) / 1000, timezone.utc).date().isoformat()


def gpt_image(posted, text):
    """GPT Image 2 shipped 2026-04-21 and 2.5 on 2026-09-08. After that only a post naming 2.5 counts as 2.5."""
    if not posted or posted < "2026-04-21":
        return None
    if posted < "2026-09-08":
        return "GPT Image 2"
    return "GPT Image 2.5" if re.search(r"(image|gpt)[\s_-]*2\.5", text, re.I) else None


FF_RAW = "https://raw.githubusercontent.com/freestylefly/awesome-gpt-image-2/main/data/"


def freestylefly(c):
    """freestylefly/awesome-gpt-image-2: GPT Image 2 cases with the original post and its result image."""
    posted = x_date(c.get("sourceUrl"))
    text = " ".join(str(c.get(k) or "") for k in ("title", "category", "prompt"))
    return {"url": c.get("sourceUrl"), "posted": posted, "score": 1, "likes": None, "credit": None,
            "prompt": c.get("prompt") or "", "poster": FF_RAW + c["image"].lstrip("/") if c.get("image") else None,
            "media": None, "text": text, "model": gpt_image(posted, text)}


def wangrunlin(c):
    """wangrunlin/awesome-gpt-image-2-5-prompts: each entry checked against a post that names GPT Image 2.5."""
    src, steps = c.get("source") or {}, (c.get("prompt") or {}).get("steps") or []
    if src.get("platform") != "x" or (c.get("model") or {}).get("family") != "GPT Image 2.5" or len(steps) != 1:
        return None
    prev = [p["url"] for p in c.get("previews") or [] if p.get("kind") == "source-result"]
    first = steps[0]
    return {"url": src.get("url"), "posted": x_date(src.get("url")), "score": 1, "likes": None, "credit": src.get("author"),
            "prompt": first.get("en") or next(iter(first.values()), ""), "poster": prev[0] if prev else None, "media": None,
            "text": "GPT Image 2.5 " + str((c.get("title") or {}).get("en", "")), "model": "GPT Image 2.5"}


def readme_cases(md):
    """Cases written as a heading, an image, a fenced prompt and an X source link (YouMind and ZeroLu READMEs)."""
    out = []
    for block in re.split(r"\n#{2,3} ", md)[1:]:
        title = block.split("\n", 1)[0]
        prompt = re.search(r"```[a-z]*\n(.+?)\n```", block, re.S)
        img = re.search(r'<img[^>]+src="(https?://[^"]+)"', block) or re.search(r"!\[[^]]*\]\((https?://[^)]+)\)", block)
        src = re.search(r"https://(?:x|twitter)\.com/[A-Za-z0-9_]+/status/\d+", block)
        if prompt and img and src:
            out.append({"title": title, "prompt": prompt.group(1), "image": img.group(1), "url": src.group(0).replace("twitter.com", "x.com")})
    return out


def gpt_readme(c):
    posted = x_date(c["url"])
    text = c["title"] + " " + c["prompt"]
    return {"url": c["url"], "posted": posted, "score": 1, "likes": None, "credit": None, "prompt": c["prompt"],
            "poster": c["image"], "media": None, "text": text, "model": gpt_image(posted, text)}


SOURCES = [
    {"repo": "LearnPrompt/awesome-seedance", "path": "data/cases.json", "read": seedance, "min_score": 300,
     "model": "Seedance 2.5", "kind": "video", "model_re": r"seedance\s*2\.5"},
    {"repo": "SkyNotSilent/awesome-MiniMax-H3-cases", "path": "data/cases.json", "read": h3, "min_score": 50,
     "model": "MiniMax H3", "kind": "video", "model_re": r"\bH3\b"},
    {"repo": "wangrunlin/awesome-gpt-image-2-5-prompts", "path": "data/catalog.json", "list": "entries", "read": wangrunlin,
     "min_score": 0, "kind": "image"},
    {"repo": "freestylefly/awesome-gpt-image-2", "path": "data/cases.json", "read": freestylefly, "min_score": 0, "kind": "image"},
    {"repo": "YouMind-OpenLab/awesome-gpt-image-2", "path": "README.md", "parse": readme_cases, "read": gpt_readme,
     "min_score": 0, "kind": "image"},
    {"repo": "ZeroLu/awesome-gpt-image", "path": "README.md", "parse": readme_cases, "read": gpt_readme,
     "min_score": 0, "kind": "image"},
]


def gh_raw(repo, path):
    return subprocess.run(["gh", "api", f"repos/{repo}/contents/{path}", "-H", "Accept: application/vnd.github.raw"],
                          capture_output=True, check=True).stdout


def cases(src):
    raw = gh_raw(src["repo"], src["path"])
    if "parse" in src:
        return src["parse"](raw.decode("utf-8"))
    data = json.loads(raw)
    return data[src.get("list", "cases")] if isinstance(data, dict) else data


def known_posts():
    ids = set()
    for f in glob.glob(str(ROOT / "prompts/*/*.yaml")) + glob.glob(str(OUT / "**/*.json"), recursive=True):
        text = Path(f).read_text(encoding="utf-8")
        ids.update(re.findall(r"/status/(\d+)", text))
    return ids


def clean(prompt):
    """Drop the post's preamble when a line announces the prompt below it."""
    lines = prompt.strip().splitlines()
    for i, line in enumerate(lines[:15]):
        if MARK.match(line) and i + 1 < len(lines):
            return "\n".join(lines[i + 1:]).strip()
    return prompt.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default="2026-07-01", help="earliest post date")
    ap.add_argument("--max", type=int, default=200, help="most candidates per source, highest score first")
    ap.add_argument("--only", help="run only the source whose repo contains this text")
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    have = known_posts()
    for src in SOURCES:
        if a.only and a.only not in src["repo"]:
            continue
        pick = []
        for c in cases(src):
            r = src["read"](c)
            m = r and re.search(r"x\.com/([^/]+)/status/(\d+)", r["url"] or "")
            if not (m and r["poster"]) or m.group(2) in have or (r["posted"] or "") < a.since:
                continue
            model = r.get("model", src.get("model"))
            if not model or (r["score"] or 0) < src["min_score"] or not re.search(src.get("model_re", ""), r["text"], re.I):
                continue
            have.add(m.group(2))  # the same post often sits in several collections
            pick.append((r, m, model))
        pick.sort(key=lambda p: -p[0]["score"])
        saved, per_author = 0, {}
        for r, m, model in pick:
            if saved >= a.max:
                break
            author = (m.group(1) + model).lower()
            if per_author.get(author, 0) >= PER_AUTHOR:  # a few accounts post the same template over and over
                continue
            per_author[author] = per_author.get(author, 0) + 1
            prompt = clean(r["prompt"])
            if len(prompt) < 60:
                continue
            cid = m.group(2)
            thumb = OUT / f"{cid}.jpg"
            # curl, because Python's TLS breaks on some image hosts behind a local proxy
            got = subprocess.run(["curl", "-sfL", "--max-time", "60", "-A", "Mozilla/5.0", "-o", str(thumb), r["poster"]])
            if got.returncode or not thumb.exists() or thumb.stat().st_size < 2000:
                print("skip", r["url"], "image download failed", file=sys.stderr)
                thumb.unlink(missing_ok=True)
                continue
            (OUT / f"{cid}.json").write_text(json.dumps({
                "cid": cid, "kind": src["kind"], "model": model, "url": f"https://x.com/{m.group(1)}/status/{cid}",
                "handle": m.group(1), "credit": r["credit"] or m.group(1), "likes": r["likes"], "posted": r["posted"][:10],
                "post_text": r["text"][:1500], "prompt": prompt, "media": r["media"] or r["poster"], "thumb": str(thumb),
                "via": src["repo"],
            }, ensure_ascii=False, indent=1))
            saved += 1
        print(f"{src['repo']}: {len(pick)} new cases match, saved {saved} candidates")


if __name__ == "__main__":
    main()
