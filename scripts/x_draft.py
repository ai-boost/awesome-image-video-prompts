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
VIDEO_CATS = ["cinematic", "action", "scifi-fantasy", "anime", "commercial", "dialogue", "music-dance", "vlog", "nature", "animal", "vfx"]
IMAGE_CATS = ["poster", "infographic", "ui-mockup", "product", "brand", "realism", "portrait", "character", "illustration",
              "comic", "photo-to-art", "architecture", "map", "collage", "edit"]
CATS = {"video": VIDEO_CATS, "image": IMAGE_CATS}

RULES = """You are the editor of awesome-image-video-prompts, a curated list of AI video and image prompts.
Look at the thumbnail with the Read tool first: {thumb}

Reject the candidate when any of these hold:
- explicit nudity or sex acts, or minors in any suggestive context (sexy, suggestive, lingerie or swimwear looks are fine)
- the prompt is not a usable prompt (an ad, a teaser, truncated, only a negative prompt)
- the prompt tells the user to bypass a safety or face-detection system
- the output contradicts the prompt: its subject, text, colours or style differ from what the prompt asks for, or an image entry whose prompt is for a video. This means the image did not come from this prompt, so reject it; never treat it as a notes problem
- quality: the output is clearly broken (garbled text, broken anatomy, muddy); a simple prompt is fine when the output is good
Not violations: brands, celebrities, fan art and copyrighted characters, posts shared on X are fine to list; a small detail that differs while the subject and layout match,
and a template written with fill-in slots such as [TOPIC] or {{NAME}}.

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
    prefix = {"Seedance": "seedance", "Wan": "wan", "Kling": "kling", "Veo": "veo", "MiniMax": "h3",
              "Gemini": "omni", "GPT Image": "gpt-image", "Nano Banana": "nano-banana"}
    pre = next((v for k, v in prefix.items() if c["model"].startswith(k)), re.sub(r"[^a-z0-9]+", "-", c["model"].lower()))
    text = RULES.format(thumb=c["thumb"], prefix=pre, modes=", ".join(MODES[c["kind"]]),
                        cat_line=f"- category: one of {', '.join(CATS[c['kind']])}",
                        cat_key=', "category": "..."',
                        model=c["model"], post=c["post_text"][:1500], prompt=c["prompt"])
    out = subprocess.run(["claude", "-p", "--model", "haiku", "--allowedTools", "Read", "--output-format", "text"],
                         input=text, capture_output=True, text=True, timeout=600).stdout
    m = re.search(r"\{.*\}", out, re.S)
    return json.loads(m.group(0)) if m else {"accept": False, "reason": "no answer"}


def write_entry(c, d):
    kind = c["kind"]
    eid = re.sub(r"[^a-z0-9-]+", "-", d["id"].lower()).strip("-")
    while (ROOT / f"prompts/{kind}/{eid}.yaml").exists():
        eid += "-2"
    e = {"id": eid, "title": d["title"], "model": c["model"], "mode": d["mode"]}
    e["category"] = d["category"]
    e.update({"tags": d["tags"],
              "source": {"name": c.get("source_name") or f"@{c['handle']} on X", "url": c["url"], "credit": c["credit"] or c["handle"],
                         "likes": c["likes"], "captured": date.today().isoformat(), "posted": c["posted"]}})
    if e["source"]["likes"] in (None, ""):  # found through a collection that reports no like count
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
    ok = ok and d.get("category") in CATS[c["kind"]]
    return ok and not any(ch in json.dumps([d["title"], d["notes"]], ensure_ascii=False) for ch in "—–")


def prompt_key(text):
    return re.sub(r"\s+", " ", text).strip().lower()[:400]


def image_hash(path):
    """64x4 bit difference hash; two images within 8 bits are the same picture."""
    from PIL import Image
    px = list(Image.open(path).convert("L").resize((17, 16)).getdata())
    return sum(1 << k for k in range(256) if px[(k // 16) * 17 + k % 16] > px[(k // 16) * 17 + k % 16 + 1])


def duplicates(cands):
    """Candidates whose prompt or picture is already in the list, or repeats an earlier candidate."""
    keys = {prompt_key(yaml.safe_load(f.read_text())["prompt"]) for f in ROOT.glob("prompts/*/*.yaml")}
    hashes = [image_hash(f) for f in ROOT.glob("previews/*.jpg")]
    dup = set()
    for c in cands:
        k, h = prompt_key(c["prompt"]), image_hash(c["thumb"])
        if k in keys or any(bin(h ^ o).count("1") <= 8 for o in hashes):
            dup.add(c["cid"])
        keys.add(k)
        hashes.append(h)
    return dup


def main():
    DONE.mkdir(parents=True, exist_ok=True)
    cands = [json.loads(p.read_text()) for p in sorted(CAND.glob("[!.]*.json"))]
    if not cands:
        print("no candidates")
        return
    log = []
    dup = duplicates(cands)
    for c in cands:
        if c["cid"] in dup:
            log.append(f"skipped {c['url']}  duplicate of an entry already listed")
            for ext in ("json", "jpg"):
                src = CAND / f"{c['cid']}.{ext}"
                if src.exists():
                    shutil.move(src, DONE / src.name)
    cands = [c for c in cands if c["cid"] not in dup]
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
