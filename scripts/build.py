"""Generate README.md and README_zh.md from prompts/ and recipes/.

Run from the repository root:  python scripts/build.py
"""
import glob
import re

import yaml

# Display order; entries not listed follow alphabetically.
ORDER = ["subway-kitten-tote-bag", "hk-noodle-stall-1960s", "kitten-and-fish-jar", "night-train-ticket",
         "late-night-office", "neon-night-market-alley", "headphone-macro-commercial", "morning-tea-stall",
         "panda-web-comic", "teaser-montage", "bilingual-subtitles", "vertical-blur-fill", "split-shots",
         "readme-preview-gif"]

MODE_ORDER = ["text-to-video", "image-to-video", "keyframes-to-video", "reference-to-video"]

T = {
    "en": {
        "file": "README.md",
        "title": "Awesome Image & Video Prompts",
        "tagline": "Tested prompts for AI video and image generation, plus agent recipes for editing video. "
                   "Every entry ships with the exact prompt, the settings it ran with, and the real output.",
        "switch": '<b>English</b> · <a href="README_zh.md">简体中文</a>',
        "formerly": "Formerly **Awesome-GPTs**. The original GPTs list lives on in [legacy/awesome-gpts.md](legacy/awesome-gpts.md).",
        "contents": "Contents",
        "video": "Video prompts",
        "mode_compare": "One scene, four modes",
        "recipes": "Agent recipes: editing video",
        "recipes_intro": "Tell a coding agent what you want in plain words. Each recipe records the request, the commands the agent ran, and the result.",
        "image": "Image prompts",
        "image_body": "The first batch is being tested. Entries go live once each prompt has a real output to show.",
        "threed": "3D with agents",
        "threed_body": "Recipes for building 3D scenes with coding agents (Blender MCP, three.js) are being tested.",
        "tags": "Browse by tag",
        "how": "How to read an entry",
        "how_body": [
            "**Prompt**: the exact text sent to the model. Copy it with the button on the code block.",
            "**Settings**: model, mode, resolution, length, sampler steps, whether audio was generated.",
            "**Preview**: a silent GIF. Open **Full video** for the original file with sound.",
            "**Source**: each entry is one YAML file. This README is generated from them.",
        ],
        "prompt": "Prompt",
        "full": "Full video with sound",
        "source": "Entry file",
        "inputs": "Input images",
        "request": "Request to the agent",
        "commands": "Commands the agent ran",
        "result": "Result",
        "agent": "Agent",
        "tools": "Tools",
        "contrib": "Contributing",
        "contrib_body": [
            "Add one YAML file under `prompts/` or `recipes/` (copy any existing entry as a template).",
            "Include the exact prompt, the model and settings, and the unedited output in `samples/`.",
            "Run `python scripts/build.py` to regenerate both READMEs, then open a pull request.",
            "Entries without a real output are closed. Promotional links are closed.",
        ],
        "related": "Related lists by the same maintainers",
        "related_items": [
            "[awesome-prompts](https://github.com/ai-boost/awesome-prompts): prompts for LLMs and agents",
            "[awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering): building reliable agent harnesses",
        ],
        "license": "License",
        "license_body": "GPL-3.0, unchanged from the original repository.",
        "items": "entries",
    },
    "zh": {
        "file": "README_zh.md",
        "title": "Awesome Image & Video Prompts",
        "tagline": "实测过的 AI 视频、图片生成提示词，加上用 Agent 剪视频的配方。每条都附原样提示词、运行参数和真实成片。",
        "switch": '<a href="README.md">English</a> · <b>简体中文</b>',
        "formerly": "本仓原名 **Awesome-GPTs**，原来的 GPTs 清单保存在 [legacy/awesome-gpts_zh.md](legacy/awesome-gpts_zh.md)。",
        "contents": "目录",
        "video": "视频提示词",
        "mode_compare": "同一场景的四种生成方式",
        "recipes": "Agent 配方：剪视频",
        "recipes_intro": "用大白话告诉编程 Agent 你要什么。每条配方记下交给 Agent 的原话、它实际跑的命令和成品。",
        "image": "图片提示词",
        "image_body": "第一批正在实测，每条有了真实出图再上线。",
        "threed": "用 Agent 做 3D",
        "threed_body": "用编程 Agent 搭 3D 场景的配方（Blender MCP、three.js）正在实测。",
        "tags": "按标签浏览",
        "how": "条目怎么看",
        "how_body": [
            "**提示词**：发给模型的原文，代码块右上角可一键复制。",
            "**参数**：模型、生成方式、分辨率、时长、采样步数、是否带声音。",
            "**预览**：无声 GIF，点 **完整视频** 看带声音的原片。",
            "**源文件**：每条是一个 YAML 文件，本 README 由它们自动生成。",
        ],
        "prompt": "提示词",
        "full": "完整视频（有声）",
        "source": "条目文件",
        "inputs": "输入图",
        "request": "交给 Agent 的原话",
        "commands": "Agent 实际跑的命令",
        "result": "成品",
        "agent": "Agent",
        "tools": "工具",
        "contrib": "投稿",
        "contrib_body": [
            "在 `prompts/` 或 `recipes/` 下加一个 YAML 文件，照任意现有条目的格式写。",
            "附上原样提示词、模型和参数，以及放在 `samples/` 里的未剪辑成片。",
            "运行 `python scripts/build.py` 重新生成两份 README，再提 PR。",
            "没有真实成片的条目会被关闭，推广链接会被关闭。",
        ],
        "related": "同一维护者的其他清单",
        "related_items": [
            "[awesome-prompts](https://github.com/ai-boost/awesome-prompts)：大模型与 Agent 提示词",
            "[awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering)：搭建可靠的 Agent harness",
        ],
        "license": "许可证",
        "license_body": "GPL-3.0，沿用原仓。",
        "items": "条",
    },
}

MODE_NAMES = {
    "en": {"text-to-video": "Text-to-video", "image-to-video": "Image-to-video",
           "keyframes-to-video": "Keyframes-to-video", "reference-to-video": "Reference-to-video"},
    "zh": {"text-to-video": "文生视频", "image-to-video": "图生视频",
           "keyframes-to-video": "首尾帧生视频", "reference-to-video": "参考图生视频"},
}


def load(pattern):
    items = [yaml.safe_load(open(f, encoding="utf-8")) for f in glob.glob(pattern)]
    return sorted(items, key=lambda e: (ORDER.index(e["id"]) if e["id"] in ORDER else len(ORDER), e["id"]))


def anchor(s):
    return re.sub(r"[^a-z0-9-]", "", s.lower())


def tag_line(tags):
    return " ".join(f"[`{t}`](#tag-{anchor(t)})" for t in tags)


def settings_line(e, run, lang):
    s = run["settings"]
    parts = [e["model"], MODE_NAMES[lang][run["mode"]], s["resolution"], f'{s["duration_s"]} s',
             f'{s["steps"]} steps ({s["sampler"]})' if lang == "en" else f'{s["steps"]} 步（{s["sampler"]}）']
    if s.get("audio"):
        parts.append("audio" if lang == "en" else "带声音")
    return " · ".join(parts)


def video_entry(e, lang, t):
    out = [f'<a id="{e["id"]}"></a>', f'#### {e["title"][lang]}', ""]
    multi = len(e["runs"]) > 1
    if multi:
        cells = "".join(
            f'<td align="center"><img src="{r["preview"]}" width="200"><br><sub>{MODE_NAMES[lang][r["mode"]]}</sub></td>'
            for r in e["runs"])
        out += [f"<table><tr>{cells}</tr></table>", ""]
    else:
        out += [f'<img src="{e["runs"][0]["preview"]}" height="240">', ""]
    out += [e["notes"][lang], "", tag_line(e["tags"]), ""]
    for r in e["runs"]:
        label = f'{t["prompt"]}: {MODE_NAMES[lang][r["mode"]]}' if multi else t["prompt"]
        out += [f"<details><summary><b>{label}</b> · {settings_line(e, r, lang)}</summary>", "",
                "```text", r["prompt"].rstrip(), "```", ""]
        if r.get("inputs"):
            out += [f'{t["inputs"]}: ' + " ".join(f'<img src="{i}" height="80">' for i in r["inputs"]), ""]
        out += ["</details>", ""]
    links = " · ".join(f'[{t["full"]}{" (" + MODE_NAMES[lang][r["mode"]] + ")" if multi else ""}]({r["sample"]})'
                       for r in e["runs"])
    out += [f'{links} · [{t["source"]}](prompts/video/{e["id"]}.yaml)', ""]
    return out


def recipe_entry(e, lang, t):
    return [
        f'<a id="{e["id"]}"></a>', f'### {e["title"][lang]}', "",
        f'<img src="{e["preview"]}" height="240">', "",
        f'**{t["request"]}**', "", f'> {e["ask"][lang]}', "",
        e["notes"][lang], "", tag_line(e["tags"]), "",
        f'<details><summary><b>{t["commands"]}</b> · {t["agent"]}: {e["agent"]} · {t["tools"]}: {", ".join(e["tools"])}</summary>',
        "", "```bash", e["commands"].rstrip(), "```", "", "</details>", "",
        f'[{t["result"]}]({e["output"]}) · [{t["source"]}](recipes/{e["id"]}.yaml)', "",
    ]


def build(lang, videos, recipes):
    t = T[lang]
    single = [v for v in videos if len(v["runs"]) == 1]
    multi = [v for v in videos if len(v["runs"]) > 1]
    showcase = [v for v in single if v["id"] in
                ("subway-kitten-tote-bag", "hk-noodle-stall-1960s", "kitten-and-fish-jar", "neon-night-market-alley")]
    out = [
        '<div align="center">', "", f'<h1>{t["title"]}</h1>', "", f'<p>{t["tagline"]}</p>', "",
        f'<p>{t["switch"]}</p>', "",
        '<p><a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a></p>', "",
        "".join(f'<a href="#{v["id"]}"><img src="{v["runs"][0]["preview"]}" height="160"></a> ' for v in showcase),
        "", "</div>", "", f'> {t["formerly"]}', "", f'## {t["contents"]}', "",
    ]
    by_mode = {m: [v for v in single if v["runs"][0]["mode"] == m] for m in MODE_ORDER}
    out.append(f'- [{t["video"]}](#video) ({len(videos)} {t["items"]})')
    for m in MODE_ORDER:
        if by_mode[m]:
            out.append(f'  - [{MODE_NAMES[lang][m]}](#{m}) ({len(by_mode[m])})')
    out += [f'  - [{t["mode_compare"]}](#mode-comparison)',
            f'- [{t["recipes"]}](#recipes) ({len(recipes)} {t["items"]})',
            f'- [{t["image"]}](#image)', f'- [{t["threed"]}](#threed)',
            f'- [{t["tags"]}](#tags)', f'- [{t["how"]}](#how)', f'- [{t["contrib"]}](#contributing)', ""]

    out += ['<a id="video"></a>', f'## {t["video"]}', ""]
    for m in MODE_ORDER:
        if by_mode[m]:
            out += [f'<a id="{m}"></a>', f"### {MODE_NAMES[lang][m]}", ""]
            for v in by_mode[m]:
                out += video_entry(v, lang, t)
    out += ['<a id="mode-comparison"></a>', f'### {t["mode_compare"]}', ""]
    for v in multi:
        out += video_entry(v, lang, t)

    out += ['<a id="recipes"></a>', f'## {t["recipes"]}', "", t["recipes_intro"], ""]
    for r in recipes:
        out += recipe_entry(r, lang, t)

    out += ['<a id="image"></a>', f'## {t["image"]}', "", t["image_body"], "",
            '<a id="threed"></a>', f'## {t["threed"]}', "", t["threed_body"], ""]

    tags = {}
    for e in videos + recipes:
        for tg in e["tags"]:
            tags.setdefault(tg, []).append(e)
    out += ['<a id="tags"></a>', f'## {t["tags"]}', ""]
    for tg in sorted(tags):
        links = ", ".join(f'[{e["title"][lang]}](#{e["id"]})' for e in tags[tg])
        out.append(f'- <a id="tag-{anchor(tg)}"></a>`{tg}` ({len(tags[tg])}): {links}')
    out.append("")

    out += ['<a id="how"></a>', f'## {t["how"]}', ""] + [f"- {x}" for x in t["how_body"]] + [""]
    out += ['<a id="contributing"></a>', f'## {t["contrib"]}', ""] + [f"{i}. {x}" for i, x in enumerate(t["contrib_body"], 1)] + [""]
    out += [f'## {t["related"]}', ""] + [f"- {x}" for x in t["related_items"]] + [""]
    out += [f'## {t["license"]}', "", t["license_body"], ""]
    open(t["file"], "w", encoding="utf-8").write("\n".join(out))


if __name__ == "__main__":
    videos = load("prompts/video/*.yaml")
    recipes = load("recipes/*.yaml")
    for lang in T:
        build(lang, videos, recipes)
    print(f"built README.md and README_zh.md: {len(videos)} video entries, {len(recipes)} recipes")
