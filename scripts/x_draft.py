"""Turn candidates from scripts/x_collect.py into entries, with a model doing the editorial pass.

For each candidate the model looks at the thumbnail and the prompt, rejects it when it breaks the
list's rules, and otherwise drafts the bilingual title, notes, tags and mode. Accepted candidates
become prompts/<kind>/<id>.yaml plus previews/<id>.jpg; every candidate moves to .x-candidates/done/.

  python3 scripts/x_draft.py            # then: python3 scripts/build.py
"""
import concurrent.futures as cf
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CAND = Path(os.environ.get("X_CANDIDATES", ROOT / ".x-candidates"))
DONE = CAND / "done"
FFMPEG = shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg"

MODES = {"video": ["text-to-video", "image-to-video", "keyframes-to-video", "reference-to-video", "video-edit", "extend"],
         "image": ["text-to-image", "image-edit"]}
IMAGE_CATS = ["poster", "infographic", "ui-mockup", "product", "brand", "realism", "portrait", "character", "illustration",
              "comic", "photo-to-art", "architecture", "map", "collage", "edit"]

RULES = """You are the editor of awesome-image-video-prompts, a curated list of AI video and image prompts.
Look at the thumbnail with the Read tool first: {thumb}

Reject the candidate when any of these hold:
- the prompt names, or the image clearly is, a real public figure or celebrity (a passing resemblance is fine)
- a brand logo, product or trademark is the subject (incidental background signage is fine)
- a copyrighted character, film still, anime or game character is the subject
- explicit nudity or sex acts, or minors in any suggestive context (sexy, suggestive, lingerie or swimwear looks are fine)
- the prompt is not a usable prompt (an ad, a teaser, truncated, a half filled template, only a negative prompt)
- the prompt tells the user to bypass a safety or face-detection system
- the output contradicts the prompt (different text, subject or style than the prompt asks for)
- quality: the output is clearly broken (garbled text, broken anatomy, muddy); a simple prompt is fine when the output is good

Otherwise accept and write, in the house style:
- id: short kebab-case slug starting with "{prefix}-"
- title.en and title.zh: what the result shows, plain and specific, at most 9 English words
- notes.en and notes.zh: one or two sentences on the technique that makes this prompt work (structure, camera, sound, references), not praise
- tags: 2 to 5 lowercase kebab-case tags
- mode: one of {modes}
{cat_line}
No quotation marks and no dashes in any title or note.

Reply with JSON only:
{{"accept": true|false, "reason": "...", "id": "...", "title": {{"en": "...", "zh": "..."}},
  "notes": {{"en": "...", "zh": "..."}}, "tags": [...], "mode": "..."{cat_key}}}

Model: {model}
Post text:
{post}

Prompt:
{prompt}
"""


class Lit(str):
    pass


yaml.add_representer(Lit, lambda d, s: d.represent_scalar("tag:yaml.org,2002:str", s, style="|"))


def ask(c):
    prefix = {"Seedance": "seedance", "Wan": "wan", "Kling": "kling", "Veo": "veo", "Sora": "sora", "MiniMax": "h3",
              "Gemini": "omni", "GPT Image": "gpt-image", "Nano Banana": "nano-banana"}
    pre = next((v for k, v in prefix.items() if c["model"].startswith(k)), re.sub(r"[^a-z0-9]+", "-", c["model"].lower()))
    text = RULES.format(thumb=c["thumb"], prefix=pre, modes=", ".join(MODES[c["kind"]]),
                        cat_line=f"- category: one of {', '.join(IMAGE_CATS)}" if c["kind"] == "image" else "",
                        cat_key=', "category": "..."' if c["kind"] == "image" else "",
                        model=c["model"], post=c["post_text"][:1500], prompt=c["prompt"][:6000])
    out = subprocess.run(["claude", "-p", "--model", "opus", "--allowedTools", "Read", "--output-format", "text"],
                         input=text, capture_output=True, text=True, timeout=600).stdout
    m = re.search(r"\{.*\}", out, re.S)
    return json.loads(m.group(0)) if m else {"accept": False, "reason": "no answer"}


def write_entry(c, d):
    kind = c["kind"]
    eid = re.sub(r"[^a-z0-9-]+", "-", d["id"].lower()).strip("-")
    while (ROOT / f"prompts/{kind}/{eid}.yaml").exists():
        eid += "-2"
    e = {"id": eid, "title": d["title"], "model": c["model"], "mode": d["mode"]}
    if kind == "image":
        e["category"] = d["category"]
    e.update({"tags": d["tags"],
              "source": {"name": c.get("source_name") or f"@{c['handle']} on X", "url": c["url"], "credit": c["credit"] or c["handle"],
                         "likes": c["likes"], "captured": date.today().isoformat(), "posted": c["posted"]}})
    if e["source"]["likes"] is None:  # found through a collection that reports no like count
        del e["source"]["likes"]
    if c.get("via"):
        e["source"]["via"] = f"https://github.com/{c['via']}"
    if kind == "video":
        e["video"] = c["url"]
    e.update({"notes": d["notes"], "prompt": Lit(c["prompt"].rstrip() + "\n")})
    with open(ROOT / f"prompts/{kind}/{eid}.yaml", "w", encoding="utf-8") as f:
        yaml.dump(e, f, allow_unicode=True, sort_keys=False, width=1000)
    subprocess.run([FFMPEG, "-v", "error", "-y", "-i", c["thumb"], "-vf", "scale=480:-2", "-q:v", "4",
                    str(ROOT / f"previews/{eid}.jpg")], check=True)
    return eid


def valid(c, d):
    ok = d.get("accept") and d.get("mode") in MODES[c["kind"]] and d.get("id") and d.get("tags")
    ok = ok and all(d.get(k, {}).get(l) for k in ("title", "notes") for l in ("en", "zh"))
    if c["kind"] == "image":
        ok = ok and d.get("category") in IMAGE_CATS
    return ok and not any(ch in json.dumps([d["title"], d["notes"]], ensure_ascii=False) for ch in "—–")


def main():
    DONE.mkdir(parents=True, exist_ok=True)
    cands = [json.loads(p.read_text()) for p in sorted(CAND.glob("*.json"))]
    if not cands:
        print("no candidates")
        return
    log = []
    with cf.ThreadPoolExecutor(4) as ex:
        for c, d in zip(cands, ex.map(ask, cands)):
            if valid(c, d):
                eid = write_entry(c, d)
                log.append(f"added   {eid}  ({c['model']}, {c['likes'] or c.get('via')})")
            else:
                log.append(f"skipped {c['url']}  {d.get('reason', 'invalid draft')}")
            for ext in ("json", "jpg"):
                src = CAND / f"{c['cid']}.{ext}"
                if src.exists():
                    shutil.move(src, DONE / src.name)
    print("\n".join(log))
    (DONE / f"log-{date.today().isoformat()}.txt").open("a").write("\n".join(log) + "\n")


if __name__ == "__main__":
    sys.exit(main())
