"""Generate README.md and README_zh.md from prompts/ and recipes/.

Run from the repository root:  python scripts/build.py
"""
import glob
import os
import re

import yaml

# Model sections, ordered by the Artificial Analysis video arena (October 2026).
MODELS = ["Wan 3.0", "MiniMax H3", "Seedance 2.5", "Gemini Omni Flash", "Kling 4.0", "Kling 3.0", "Veo 3.1", "Veo 3", "Sora 2"]
# Image sections by use case, in display order.
CATEGORIES = {
    "poster": {"en": "Posters and editorial layouts", "zh": "海报与编辑排版"},
    "photo-to-art": {"en": "Photo to art", "zh": "照片转艺术风格"},
    "realism": {"en": "Photo realism", "zh": "写实照片"},
    "portrait": {"en": "Portraits", "zh": "人像"},
    "illustration": {"en": "Illustration", "zh": "插画"},
    "ui-mockup": {"en": "Phone and UI mockups", "zh": "手机与界面截图"},
    "map": {"en": "Maps", "zh": "地图"},
    "collage": {"en": "Collage", "zh": "拼贴"},
    "infographic": {"en": "Infographics and slides", "zh": "信息图与幻灯片"},
    "brand": {"en": "Logos, ads and packaging", "zh": "标志、广告与包装"},
    "edit": {"en": "Photo editing", "zh": "照片编辑"},
}
# The README shows the most-liked TOP entries of each section; pages/<lang>/ holds every entry of every section.
TOP = 6
PAGE_BYTES = 350_000
SHOWCASE = ["seedance-seoul-subway-revenge", "wan-time-space-train", "h3-starship-hyperspace-jump", "omni-four-style-progression",
            "kling-moonlit-garden-run", "veo-off-road-rally"]

T = {
    "en": {
        "file": "README.md",
        "title": "Awesome Image & Video Prompts",
        "tagline": "Copy-ready prompts for the leading AI video and image models, each with its real output and a link to where it came from. "
                   "Plus agent recipes for editing video.",
        "switch": '<b>English</b> · <a href="README_zh.md">简体中文</a>',
        "gallery": 'Search, filter and copy in the <a href="https://agentcraft.dev/en/prompts/">online gallery</a>',
        "formerly": "Formerly **Awesome-GPTs**. The original GPTs list lives on in [legacy/awesome-gpts.md](legacy/awesome-gpts.md).",
        "contents": "Contents",
        "video": "Video prompts",
        "video_intro": "Every prompt below is quoted verbatim from its source: the model maker's own guide or model card, or a creator's post on X with the video attached. "
                       "Click a thumbnail to watch the original with sound. Sections follow the [Artificial Analysis video arena](https://artificialanalysis.ai/video/leaderboard/text-to-video) ranking; "
                       "creator posts are sorted by likes, counted on the date shown.",
        "recipes": "Agent recipes: editing video",
        "recipes_intro": "Tell a coding agent what you want in plain words. Each recipe records the request and the commands the agent ran. Swap in your own clips.",
        "guides": "Guides and skills",
        "guides_official": "Official prompt guides",
        "guides_community": "Community skills and libraries",
        "image": "Image prompts",
        "image_body": "The most-liked prompts for the top image models on the [Artificial Analysis image arena](https://artificialanalysis.ai/text-to-image/arena), each with its result: shared on X by its author, or from the model maker's own guide. Grouped by what you want to make. Many work on an uploaded photo; the ones marked *Edit* expect one.",
        "threed": "3D with agents",
        "threed_body": "Recipes for building 3D scenes with coding agents (Blender MCP, three.js) are in progress.",
        "tags": "Browse by tag",
        "prompt": "Prompt",
        "inputs": "Inputs",
        "source": "Source",
        "watch": "Watch the original",
        "likes": "likes on",
        "request": "Request to the agent",
        "commands": "Commands the agent ran",
        "agent": "Agent",
        "tools": "Tools",
        "contrib": "Contributing",
        "contrib_body": [
            "Add one YAML file under `prompts/video/` or `prompts/image/` (copy any entry as a template).",
            "Link the original post or page where the prompt and its output were published, and credit the author.",
            "Run `python scripts/build.py` to regenerate both READMEs, then open a pull request.",
            "Entries without a visible output or a traceable source are closed. Promotional links are closed.",
        ],
        "related": "Related lists by the same maintainers",
        "related_items": [
            "[awesome-prompts](https://github.com/ai-boost/awesome-prompts): prompts for LLMs and agents",
            "[awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering): building reliable agent harnesses",
        ],
        "license": "License",
        "license_body": "Repository code and notes: GPL-3.0. Prompts and videos belong to their original publishers and are linked or quoted with credit.",
        "items": "entries",
        "all": "All {n} entries",
        "via": "found via",
        "all_tags": "All {n} tags",
        "back": "Back to the list",
    },
    "zh": {
        "file": "README_zh.md",
        "title": "Awesome Image & Video Prompts",
        "tagline": "主流 AI 视频和图片模型的提示词，拿来就能用。每条都附真实成品和出处链接。另有用 Agent 剪视频的配方。",
        "switch": '<a href="README.md">English</a> · <b>简体中文</b>',
        "gallery": '在<a href="https://agentcraft.dev/zh/prompts/">在线画廊</a>里搜索、筛选、一键复制',
        "formerly": "本仓原名 **Awesome-GPTs**，原来的 GPTs 清单保存在 [legacy/awesome-gpts_zh.md](legacy/awesome-gpts_zh.md)。",
        "contents": "目录",
        "video": "视频提示词",
        "video_intro": "下面每条提示词都原样摘自出处：模型厂商自己的指南或模型卡，或创作者在 X 上附带成片发布的帖子。"
                       "点缩略图看带声音的原片。分组顺序按 [Artificial Analysis 视频榜](https://artificialanalysis.ai/video/leaderboard/text-to-video)排名，"
                       "创作者帖子按点赞数排序，点赞数以标注日期为准。",
        "recipes": "Agent 配方：剪视频",
        "recipes_intro": "用大白话告诉编程 Agent 你要什么。每条配方记下交给 Agent 的原话和它实际跑的命令，换成你自己的素材即可。",
        "guides": "指南与 skill",
        "guides_official": "官方提示词指南",
        "guides_community": "社区 skill 与案例库",
        "image": "图片提示词",
        "image_body": "[Artificial Analysis 图像榜](https://artificialanalysis.ai/text-to-image/arena)前排模型上点赞最多的提示词，每条都附成图，出自作者在 X 上的帖子或模型官方指南。按用途分组。很多要配一张自己的照片，标着「上传图改图」的就是。",
        "threed": "用 Agent 做 3D",
        "threed_body": "用编程 Agent 搭 3D 场景的配方（Blender MCP、three.js）正在整理。",
        "tags": "按标签浏览",
        "prompt": "提示词",
        "inputs": "输入素材",
        "source": "出处",
        "watch": "看原片",
        "likes": "赞，统计于",
        "request": "交给 Agent 的原话",
        "commands": "Agent 实际跑的命令",
        "agent": "Agent",
        "tools": "工具",
        "contrib": "投稿",
        "contrib_body": [
            "在 `prompts/video/` 或 `prompts/image/` 下加一个 YAML 文件，照任意现有条目的格式写。",
            "附上提示词和成片最初发布的帖子或页面链接，并署上作者。",
            "运行 `python scripts/build.py` 重新生成两份 README，再提 PR。",
            "看不到成片、查不到出处的条目会被关闭，推广链接会被关闭。",
        ],
        "related": "同一维护者的其他清单",
        "related_items": [
            "[awesome-prompts](https://github.com/ai-boost/awesome-prompts)：大模型与 Agent 提示词",
            "[awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering)：搭建可靠的 Agent harness",
        ],
        "license": "许可证",
        "license_body": "仓库代码和说明文字：GPL-3.0。提示词和视频归原发布者所有，本仓注明出处后链接或引用。",
        "items": "条",
        "all": "全部 {n} 条",
        "via": "发现于",
        "all_tags": "全部 {n} 个标签",
        "back": "返回目录",
    },
}

MODE_NAMES = {
    "en": {"text-to-video": "Text-to-video", "image-to-video": "Image-to-video",
           "keyframes-to-video": "First & last frame", "reference-to-video": "Reference-to-video",
           "video-edit": "Video edit", "extend": "Extend",
           "text-to-image": "Text-to-image", "image-edit": "Edit"},
    "zh": {"text-to-video": "文生视频", "image-to-video": "图生视频",
           "keyframes-to-video": "首尾帧", "reference-to-video": "参考生视频",
           "video-edit": "视频编辑", "extend": "续写",
           "text-to-image": "文生图", "image-edit": "上传图改图"},
}


def load(pattern):
    return [yaml.safe_load(open(f, encoding="utf-8")) for f in sorted(glob.glob(pattern))]


def anchor(s):
    return re.sub(r"[^a-z0-9-]", "", s.lower())


def tag_line(tags, href):
    """href is the path to pages/<lang>/tags.md from the output file."""
    return " ".join(f"[`{t}`]({href}#tag-{anchor(t)})" for t in tags)


def video_entry(e, lang, t, root=""):
    """root is the path from the output file back to the repository root."""
    s = e["source"]
    meta = f'{e["model"]} · {MODE_NAMES[lang][e["mode"]]} · {t["source"]}: [{s["name"]}]({s["url"]})'
    if s.get("likes"):
        meta += f' · {s["likes"]:,} {t["likes"]} {s["captured"]}'
    if s.get("via"):
        meta += f' · {t["via"]} [{s["via"].split("github.com/")[-1]}]({s["via"]})'
    out = [f'<a id="{e["id"]}"></a>', f'### {e["title"][lang]}', "",
           f'<a href="{e.get("video", s["url"])}"><img src="{root}previews/{e["id"]}.jpg" width="360"></a>', "",
           e["notes"][lang], "", meta, "", tag_line(e["tags"], "tags.md" if root else f"pages/{lang}/tags.md"), "",
           f'<details><summary><b>{t["prompt"]}</b></summary>', "", "```text", e["prompt"].rstrip(), "```", "", "</details>", ""]
    if e.get("inputs"):
        out += [f'{t["inputs"]}: ' + " · ".join(f'[{i + 1}]({u})' for i, u in enumerate(e["inputs"])) + "", ""]
    return out


def recipe_entry(e, lang, t):
    return [
        f'<a id="{e["id"]}"></a>', f'### {e["title"][lang]}', "",
        f'**{t["request"]}**', "", f'> {e["ask"][lang]}', "",
        e["notes"][lang], "", tag_line(e["tags"], f"pages/{lang}/tags.md"), "",
        f'<details><summary><b>{t["commands"]}</b> · {t["agent"]}: {e["agent"]} · {t["tools"]}: {", ".join(e["tools"])}</summary>',
        "", "```bash", e["commands"].rstrip(), "```", "", "</details>", "",
    ]


def rel(link, lang, t):
    """Turn a README-relative entry link into one relative to pages/<lang>/."""
    return f"../../{t['file']}{link}" if link.startswith("#") else link.removeprefix(f"pages/{lang}/")


def write_pages(lang, t, key, title, entries):
    """Write every entry of one section to pages/<lang>/<key>.md, <key>-2.md, ...; return {id: page path}."""
    root, chunks, size = "../../", [[]], 0
    for e in entries:
        md = "\n".join(video_entry(e, lang, t, root))
        if chunks[-1] and size + len(md.encode()) > PAGE_BYTES:
            chunks.append([])
            size = 0
        chunks[-1].append((e, md))
        size += len(md.encode())
    names = [f"pages/{lang}/{key}.md"] + [f"pages/{lang}/{key}-{i}.md" for i in range(2, len(chunks) + 1)]
    where = {}
    for i, (name, chunk) in enumerate(zip(names, chunks)):
        nav = " · ".join(f"**{j + 1}**" if j == i else f"[{j + 1}]({os.path.basename(n)})" for j, n in enumerate(names))
        head = f"[{t['back']}]({root}{t['file']}) · {t['all'].format(n=len(entries))}" + (f" · {nav}" if len(names) > 1 else "")
        out = [f"# {title}", "", head, ""] + [md for _, md in chunk] + ([nav, ""] if len(names) > 1 else [])
        open(name, "w", encoding="utf-8").write("\n".join(out))
        where.update({e["id"]: name for e, _ in chunk})
    return where


def build(lang, videos, images, recipes):
    t = T[lang]
    by_model = {m: sorted((v for v in videos if v["model"] == m), key=lambda v: -v["source"].get("likes", 0))
                for m in MODELS}
    assert sum(map(len, by_model.values())) == len(videos), "entry with a model missing from MODELS"
    by_cat = {c: sorted((i for i in images if i["category"] == c), key=lambda i: -i["source"].get("likes", 0))
              for c in CATEGORIES}
    assert sum(map(len, by_cat.values())) == len(images), "image with a category missing from CATEGORIES"
    # (pages key, README anchor, heading, entries) for every non-empty section
    sections = [(f"video-{anchor(m)}", anchor(m), m, by_model[m]) for m in MODELS if by_model[m]] + \
               [(f"image-{c}", f"img-{c}", CATEGORIES[c][lang], by_cat[c]) for c in CATEGORIES if by_cat[c]]
    loc, more = {e["id"]: f'#{e["id"]}' for e in videos + images + recipes}, {}
    for key, _, title, es in sections:
        if len(es) > TOP:
            where = write_pages(lang, t, key, title, es)
            more[key] = where[es[0]["id"]]
            loc.update({e["id"]: f'{where[e["id"]]}#{e["id"]}' for e in es[TOP:]})

    out = [
        '<div align="center">', "", f'<h1>{t["title"]}</h1>', "", f'<p>{t["tagline"]}</p>', "",
        f'<p>{t["switch"]}</p>', "", f'<p>{t["gallery"]}</p>', "",
        '<p><a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a></p>', "",
        "".join(f'<a href="{loc[i]}"><img src="previews/{i}.gif" height="150"></a> ' for i in SHOWCASE if i in loc),
        "", "</div>", "", f'> {t["formerly"]}', "", f'## {t["contents"]}', "",
        f'- [{t["video"]}](#video) ({len(videos)} {t["items"]})',
    ]
    out += [f'  - [{m}](#{anchor(m)}) ({len(by_model[m])})' for m in MODELS if by_model[m]]
    out += [f'- [{t["image"]}](#image) ({len(images)} {t["items"]})']
    out += [f'  - [{CATEGORIES[c][lang]}](#img-{c}) ({len(by_cat[c])})' for c in CATEGORIES if by_cat[c]]
    out += [f'- [{t["recipes"]}](#recipes) ({len(recipes)} {t["items"]})',
            f'- [{t["guides"]}](#guides)', f'- [{t["threed"]}](#threed)',
            f'- [{t["tags"]}](#tags)', f'- [{t["contrib"]}](#contributing)', ""]

    for key, anc, title, es in sections:
        if key == sections[0][0]:
            out += ['<a id="video"></a>', f'## {t["video"]}', "", t["video_intro"], ""]
        if key.startswith("image-") and not any(k.startswith("image-") for k, *_ in sections[:sections.index((key, anc, title, es))]):
            out += ['<a id="image"></a>', f'## {t["image"]}', "", t["image_body"], ""]
        out += [f'<a id="{anc}"></a>', f"## {title}", ""]
        for e in es[:TOP]:
            out += video_entry(e, lang, t)
        if key in more:
            out += [f'**[{t["all"].format(n=len(es))}]({more[key]})**', ""]

    out += ['<a id="recipes"></a>', f'## {t["recipes"]}', "", t["recipes_intro"], ""]
    for r in recipes:
        out += recipe_entry(r, lang, t)

    res = yaml.safe_load(open("resources.yaml", encoding="utf-8"))
    out += ['<a id="guides"></a>', f'## {t["guides"]}', ""]
    for key in ("official", "community"):
        out += [f'### {t["guides_" + key]}', ""] + [f'- [{r["name"]}]({r["url"]}): {r[lang]}' for r in res[key]] + [""]

    out += ['<a id="threed"></a>', f'## {t["threed"]}', "", t["threed_body"], ""]

    tags = {}
    for e in videos + images + recipes:
        for tg in e["tags"]:
            tags.setdefault(tg, []).append(e)
    # The full index lives on pages/<lang>/tags.md; the README keeps the tags used three times or more.
    page = [f"# {t['tags']}", "", f"[{t['back']}](../../{t['file']})", ""]
    for tg in sorted(tags):
        links = ", ".join(f'[{e["title"][lang]}]({rel(loc[e["id"]], lang, t)})' for e in tags[tg])
        page.append(f'- <a id="tag-{anchor(tg)}"></a>`{tg}` ({len(tags[tg])}): {links}')
    open(f"pages/{lang}/tags.md", "w", encoding="utf-8").write("\n".join(page) + "\n")
    common = sorted((tg for tg in tags if len(tags[tg]) >= 3), key=lambda tg: -len(tags[tg]))
    out += ['<a id="tags"></a>', f'## {t["tags"]}', "",
            " · ".join(f'[`{tg}`](pages/{lang}/tags.md#tag-{anchor(tg)}) {len(tags[tg])}' for tg in common), "",
            f'**[{t["all_tags"].format(n=len(tags))}](pages/{lang}/tags.md)**', ""]

    out += ['<a id="contributing"></a>', f'## {t["contrib"]}', ""] + [f"{i}. {x}" for i, x in enumerate(t["contrib_body"], 1)] + [""]
    out += [f'## {t["related"]}', ""] + [f"- {x}" for x in t["related_items"]] + [""]
    out += [f'## {t["license"]}', "", t["license_body"], ""]
    open(t["file"], "w", encoding="utf-8").write("\n".join(out))


if __name__ == "__main__":
    videos = load("prompts/video/*.yaml")
    images = load("prompts/image/*.yaml")
    recipes = load("recipes/*.yaml")
    for lang in T:
        os.makedirs(f"pages/{lang}", exist_ok=True)
        for f in glob.glob(f"pages/{lang}/*.md"):
            os.remove(f)
    for lang in T:
        build(lang, videos, images, recipes)
    print(f"built README.md and README_zh.md: {len(videos)} video, {len(images)} image entries, {len(recipes)} recipes")
