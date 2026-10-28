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
import urllib.request
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


SOURCES = [
    {"repo": "LearnPrompt/awesome-seedance", "path": "data/cases.json", "read": seedance, "min_score": 300,
     "model": "Seedance 2.5", "kind": "video", "model_re": r"seedance\s*2\.5"},
    {"repo": "SkyNotSilent/awesome-MiniMax-H3-cases", "path": "data/cases.json", "read": h3, "min_score": 50,
     "model": "MiniMax H3", "kind": "video", "model_re": r"\bH3\b"},
]


def gh_json(repo, path):
    raw = subprocess.run(["gh", "api", f"repos/{repo}/contents/{path}", "-H", "Accept: application/vnd.github.raw"],
                         capture_output=True, check=True).stdout
    return json.loads(raw)


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
        data = gh_json(src["repo"], src["path"])
        pick = []
        for c in data["cases"] if isinstance(data, dict) else data:
            r = src["read"](c)
            m = r and re.search(r"x\.com/([^/]+)/status/(\d+)", r["url"] or "")
            if not (m and r["poster"]) or m.group(2) in have or (r["posted"] or "") < a.since:
                continue
            if (r["score"] or 0) < src["min_score"] or not re.search(src["model_re"], r["text"], re.I):
                continue
            pick.append((r, m))
        pick.sort(key=lambda p: -p[0]["score"])
        saved, per_author = 0, {}
        for r, m in pick:
            if saved >= a.max:
                break
            author = m.group(1).lower()
            if per_author.get(author, 0) >= PER_AUTHOR:  # a few accounts post the same template over and over
                continue
            per_author[author] = per_author.get(author, 0) + 1
            prompt = clean(r["prompt"])
            if len(prompt) < 60:
                continue
            cid = m.group(2)
            thumb = OUT / f"{cid}.jpg"
            try:
                req = urllib.request.Request(r["poster"], headers={"User-Agent": "Mozilla/5.0"})
                thumb.write_bytes(urllib.request.urlopen(req, timeout=60).read())
            except OSError as e:
                print("skip", r["url"], e, file=sys.stderr)
                continue
            (OUT / f"{cid}.json").write_text(json.dumps({
                "cid": cid, "kind": src["kind"], "model": src["model"], "url": f"https://x.com/{m.group(1)}/status/{cid}",
                "handle": m.group(1), "credit": r["credit"] or m.group(1), "likes": r["likes"], "posted": r["posted"][:10],
                "post_text": r["text"][:1500], "prompt": prompt, "media": r["media"] or r["poster"], "thumb": str(thumb),
                "via": src["repo"],
            }, ensure_ascii=False, indent=1))
            saved += 1
        print(f"{src['repo']}: {len(pick)} new cases match, saved {saved} candidates")


if __name__ == "__main__":
    main()
