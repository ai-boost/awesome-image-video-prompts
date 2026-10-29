# 标志、广告与包装

[返回目录](../../README_zh.md) · 全部 11 条

<a id="gpt-image-bakery-logo-transparent"></a>
### 透明背景的面包店标志

<a href="https://developers.openai.com/api/docs/guides/image-prompting#design-a-reusable-logo"><img src="../../previews/gpt-image-bakery-logo-transparent.jpg" width="360"></a>

要求原创、在大小尺寸下都清楚，再把透明背景写到位：干净的 alpha 边缘、不要底色、不要棋盘格。调用时同时设 background=transparent。预览图为 Sunburst 版本。

GPT Image 2.5 · 文生图 · 出处: [OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting#design-a-reusable-logo)

[`logo`](tags.md#tag-logo) [`transparent`](tags.md#tag-transparent) [`vector`](tags.md#tag-vector)

<details><summary><b>提示词</b></summary>

```text
Create an original, non-infringing logo for a company called Field & Flour, a local bakery.
The logo should feel warm, simple, and timeless. Use clean, vector-like shapes, a strong silhouette, and balanced negative space.
Favor simplicity over detail so it reads clearly at small and large sizes. Flat design, minimal strokes, no gradients unless essential.
Fully transparent background. Deliver a single centered logo with generous padding, clean alpha edges, and no solid backdrop, scenery, checkerboard, or watermark.
```

</details>

<a id="gpt-image-bichon-shop-skeuomorphic-app-icon"></a>
### 粉色购物袋里的比熊幼犬应用图标

<a href="https://x.com/iamaiistudio/status/2071923809788285125"><img src="../../previews/gpt-image-bichon-shop-skeuomorphic-app-icon.jpg" width="360"></a>

提示词用单个圆角方块、画布占比八成和白底锁定版式，再点明 macOS App Store 拟物风格。只给出简短的应用名，主体和文字都由模型自行补全。

GPT Image 2 · 文生图 · 出处: [@iamaiistudio on X](https://x.com/iamaiistudio/status/2071923809788285125) · 发现于 [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)

[`app-icon`](tags.md#tag-app-icon) [`skeuomorphic`](tags.md#tag-skeuomorphic) [`macos`](tags.md#tag-macos) [`squircle`](tags.md#tag-squircle) [`cute`](tags.md#tag-cute)

<details><summary><b>提示词</b></summary>

```text
A macOS app icon for an app named 'Bichon Shop'. A single squircle icon with smooth continuous rounded corners, centered on a white canvas with padding, occupying about 80% of the canvas. Modern light skeuomorphic macOS App Store style. Only one icon.
```

</details>

<a id="gpt-image-brand-envelope-coffee-four-styles"></a>
### 同一只咖啡杯的四种品牌世界

<a href="https://x.com/SRKDAN/status/2051482047248560393"><img src="../../previews/gpt-image-brand-envelope-coffee-four-styles.jpg" width="360"></a>

四阶段模板：先用两行文字锚定品牌的色板、质感和情绪，再把产品放进这个世界，最后指定输出格式和一个标志性元素。只替换品牌、产品和格式三项，结构不变而风格随之改变。

GPT Image 2 · 文生图 · 出处: [@SRKDAN on X](https://x.com/SRKDAN/status/2051482047248560393) · 发现于 [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)

[`brand-identity`](tags.md#tag-brand-identity) [`product-ad`](tags.md#tag-product-ad) [`prompt-template`](tags.md#tag-prompt-template) [`coffee`](tags.md#tag-coffee) [`packaging`](tags.md#tag-packaging)

<details><summary><b>提示词</b></summary>

```text
The Brand Envelope | GPT Image-2 Prompt #89

This takes any product photo and wraps it in your specific brand world. Different product each time. Same brand, every time.

PHASE 1 / ANCHOR: Describe [BRAND IDENTITY] in 2 lines. Palette, texture, mood.
PHASE 2 / INJECT: Place [PRODUCT] inside that brand world, not the reverse.
PHASE 3 / FORMAT: Set [OUTPUT FORMAT]. Hero, square ad, or story.
PHASE 4 / SIGNATURE: Apply [BRAND ELEMENT]. Grain, shadow, or overlay.

Swap: [BRAND IDENTITY] / [PRODUCT] / [FORMAT]
```

</details>

<a id="gpt-image-dark-minimal-avatar-site-vi-system"></a>
### 暗黑极简头像网站视觉识别系统

<a href="https://x.com/xiaoxiaodong01/status/2046556758521573546"><img src="../../previews/gpt-image-dark-minimal-avatar-site-vi-system.jpg" width="360"></a>

只用一个风格关键词（黑色封面设计）加一句品牌简介，就能生成完整的多格视觉识别板。模型会自动补全标志、色板、字体、界面页面和周边样机。

GPT Image 2 · 文生图 · 出处: [@xiaoxiaodong01 on X](https://x.com/xiaoxiaodong01/status/2046556758521573546) · 发现于 [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)

[`vi-system`](tags.md#tag-vi-system) [`brand-board`](tags.md#tag-brand-board) [`dark-minimal`](tags.md#tag-dark-minimal) [`bilingual`](tags.md#tag-bilingual) [`website-design`](tags.md#tag-website-design)

<details><summary><b>提示词</b></summary>

```text
[中文]
用 ABCD（a black cover design) 的风格，为 图你太美 设计一个 vi 系统。图你太美是一个头像美图分享 网站。

[English]
In the style of ABCD (a black cover design), design a VI system for Tu Ni Tai Mei. Tu Ni Tai Mei is an avatar and beauty photo sharing website.
```

</details>

<a id="gpt-image-four-seasons-packaging-campaign-grid"></a>
### 四季包装宣传图 2x2 宫格

<a href="https://x.com/SRKDAN/status/2048582939504431195"><img src="../../previews/gpt-image-four-seasons-packaging-campaign-grid.jpg" width="360"></a>

提示词按产品、宫格、构图、一致性四个编号阶段拆分。锁定同一产品轮廓，只让每格的色调和道具变化，整组画面保持统一，方括号占位符便于替换复用。

GPT Image 2 · 文生图 · 出处: [@SRKDAN on X](https://x.com/SRKDAN/status/2048582939504431195) · 发现于 [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)

[`packaging`](tags.md#tag-packaging) [`seasonal`](tags.md#tag-seasonal) [`grid`](tags.md#tag-grid) [`campaign`](tags.md#tag-campaign) [`template`](tags.md#tag-template)

<details><summary><b>提示词</b></summary>

```text
PHASE 1 - PRODUCT: [ITEM] in [MATERIAL] packaging, minimal label design
PHASE 2 - GRID: 2x2 seasonal grid, four distinct brand worlds
PHASE 3 - COMPOSITION: each quadrant a full campaign scene with props and environment
PHASE 4 - CONSISTENCY: same product silhouette, four distinct palettes

Swap: [ITEM] / [MATERIAL] / [LABEL STYLE]
```

</details>

<a id="gpt-image-jewelry-necklace-miniature-city-poster"></a>
### 红宝石项链微缩城市广告海报

<a href="https://x.com/Umar__786Ai/status/2055664244138349055"><img src="../../previews/gpt-image-jewelry-necklace-miniature-city-poster.jpg" width="360"></a>

把珠宝放大成建筑地标，再列出高速路、桥梁、无人机、小人等微缩城市元素围绕它。深红单色配金色点缀，加移轴景深和顶部引号标题文字，整体保持高端广告质感。

GPT Image 2 · 文生图 · 出处: [@Umar__786Ai on X](https://x.com/Umar__786Ai/status/2055664244138349055) · 发现于 [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)

[`jewelry`](tags.md#tag-jewelry) [`miniature-world`](tags.md#tag-miniature-world) [`luxury-ad`](tags.md#tag-luxury-ad) [`monochrome`](tags.md#tag-monochrome) [`typography`](tags.md#tag-typography)

<details><summary><b>提示词</b></summary>

```text
Create a hyper-detailed luxury advertising poster in a cinematic miniature-world style. A gigantic royal diamond necklace with intricate gold filigree and massive ruby gemstones stands in the center like an architectural monument. Surround the necklace with a futuristic miniature city built around and inside the jewelry piece, including skyscrapers, elevated highways, bridges, spiral staircases, tiny human figures, luxury billboards, drones, helicopters, and cinematic urban activity. Use a deep crimson red monochrome background with gold and ruby accents. Add premium fashion-ad aesthetics, ultra-realistic textures, glossy reflections, dramatic studio lighting, depth of field, tilt-shift miniature effect, and high-end commercial composition. Include bold elegant typography at the top saying: “EMBRACE THE EXTRAORDINARY”. Style inspired by luxury jewelry campaigns, surreal city-building concepts, and premium 3D advertising renders. Ultra realistic, 8K, octane render, sharp focus, highly detailed, cinematic shadows, symmetrical composition.
```

</details>

<a id="gpt-image-logo-concepts-ai-newsletter-sheet"></a>
### AI 通讯品牌的五个 Logo 概念展示板

<a href="https://x.com/wanerfu/status/2048659924822184026"><img src="../../previews/gpt-image-logo-concepts-ai-newsletter-sheet.jpg" width="360"></a>

提示词先设定资深设计师角色，再用品牌信息模板要求五个互不相同的概念，每个概念按象征意义、形状、字体、情感、受众和名片、App 图标、广告牌应用逐项说明。固定的逐项结构让结果成为整齐的对比展示板，并给出最终推荐。

GPT Image 2 · 文生图 · 出处: [@wanerfu on X](https://x.com/wanerfu/status/2048659924822184026) · 发现于 [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)

[`logo`](tags.md#tag-logo) [`brand-identity`](tags.md#tag-brand-identity) [`concept-sheet`](tags.md#tag-concept-sheet) [`mockup`](tags.md#tag-mockup) [`template`](tags.md#tag-template)

<details><summary><b>提示词</b></summary>

```text
你是一位拥有20年经验的顶级Logo设计师，为全球知名品牌设计过即时识别且深具意义的标志。

品牌名称：[你的品牌名]
行业：[你的行业]
品牌个性：[描述]
目标受众：[描述]
欣赏的视觉身份：[列举3个]
讨厌的视觉身份：[列举3个]
偏好风格：[如极简、大胆、几何、有机、复古、未来]

为我的品牌生成5个完全不同的Logo概念。

对每个概念提供：

- 核心视觉理念及象征意义
- 形状语言及为何适合品牌
- 字体方向建议
- 第一眼的情感触发
- 为何适合目标受众
- 在名片、App图标和广告牌上的效果
- 何为永恒而非潮流

然后告诉我，如果这是你的品牌，你会选哪个以及原因。

2. 品牌身份基础提示词

你是为财富500强公司和初创企业建立品牌身份的顶级品牌战略师，这些企业后来融资数百万。

业务名称：[你的业务名]
业务描述：[一句话]
目标受众：[详细描述]
竞争对手：[列举3-5个]
想触发的感受：[如信任、兴奋、奢华、亲近、力量]
想关联的词汇：[列举5-10个]
不想关联的词汇：[列举5-10个]

在设计任何视觉效果之前建立完整的品牌身份基础。

为我提供：

- 品牌原型及为何完美契合
- 5个具体人类特征描述的品牌个性
- 带示例的品牌语调指南
- 核心品牌承诺（一句话）
- 3个品牌应触发的情感层级
- 与竞争对手的根本差异
- 定义品牌的唯一关键词

3. 配色方案提示词

你是色彩心理学专家和品牌设计师，深知色彩如何触发情感、建立信任和驱动购买决策。

品牌名称：[你的品牌名]
行业：[你的行业]
目标受众：[年龄、性别、收入、生活方式]
想触发的首要情感：[如信任、能量、奢华、平静、兴奋]
前3名竞争对手颜色：[列举]
喜欢的颜色：[列举]
讨厌的颜色：[列举]

为我建立完整品牌配色板。

为我提供：

- 主色及其HEX代码和心理学解释
- 两个辅助色及HEX代码
- 一个强调色用于CTA和高亮
- 一个中性色用于背景和文字
- 每种颜色对目标受众的影响
- 与竞争对手的差异化
- 在网站、社交媒体和包装上的应用示例
- 永远不要搭配的颜色组合及原因

4. 字体方向提示词

你是字体专家和品牌设计师，深知字体如何传达个性、建立可信度和实现品牌即时识别。

品牌名称：[你的品牌名]
品牌个性：[5个词]
行业：[你的行业]
目标受众：[描述]
字体应触发的感受：[如权威、友好、创新、优雅、能量]
喜欢的品牌字体：[列举3个]

为我建立完整字体系统。

为我提供：

- 标题用主显示字体名称及为何完美
- 长文本的辅助字体
- 引言或重点的强调字体
- 标题、副标题、正文、说明文字的精确字号层级
- 字距和行高建议
- 字体搭配方法
- 预算有限时的免费替代方案
- 你所在行业应避免的字体错误

5. 完整品牌身份包提示词

你是顶级品牌代理创意总监，交付覆盖每个触点的完整品牌身份系统。

业务名称：[你的业务名]
业务描述：[一句话]
目标受众：[详细描述]
品牌个性：[5个词]
行业：[你的行业]
竞争对手：[列举3个]
设计工具预算：[免费或付费]
时间表：[你需要的时间]

在一个回复中交付我的完整品牌身份系统。

包含所有元素：

- 品牌战略基础、原型、个性、承诺和定位
- Logo概念及3个变体
- 完整配色板、HEX代码和使用规则
- 字体系统、名称、字号和层级
- 视觉方向指南
- 品牌语调指南和标语选项
- 社交媒体视觉模板
- 3条永远不要打破的核心品牌规则

将一切作为结构化品牌手册交付，任何设计师、开发者或AI工具都能在10分钟内完全理解你的品牌。
```

</details>

<a id="gpt-image-matcha-brand-touchpoint-board"></a>
### 抹茶品牌视觉板与包装触点系统

<a href="https://x.com/Preda2005/status/2049846981271699685"><img src="../../previews/gpt-image-matcha-brand-touchpoint-board.jpg" width="360"></a>

先写主视觉场景，再逐项列出杯子、包装盒、帆布袋、标签和带价格的菜单，让模型在一张网格版面里生成完整品牌系统。限定绿色色板、日式极简排版和细微瑕疵，使整板风格统一且真实。

GPT Image 2 · 文生图 · 出处: [@Preda2005 on X](https://x.com/Preda2005/status/2049846981271699685) · 发现于 [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)

[`brand-identity`](tags.md#tag-brand-identity) [`matcha`](tags.md#tag-matcha) [`packaging`](tags.md#tag-packaging) [`mockup-board`](tags.md#tag-mockup-board) [`minimalist`](tags.md#tag-minimalist)

<details><summary><b>提示词</b></summary>

```text
Create a premium “Matcha Brand Touchpoint System” visual board for a modern lifestyle brand called:

“MATCHA MODE”

Build a full brand identity system, not a single image.

HERO SCENE:

A hyper-realistic matcha drink in a ceramic cup placed on a clean natural surface.

– vibrant green matcha foam with micro-bubbles
– bamboo whisk (chasen) nearby
– soft natural light
– slight matcha powder dust on the surface
– minimal Japanese aesthetic
ATMOSPHERE:
– calm, warm, soft daylight
– clean background (off-white or beige)
– subtle shadows and reflections
– feeling of wellness and luxury
FULL BRAND SYSTEM:
– takeout cups (paper + glass bottles)
– packaging boxes (minimalist design)
– tote bags (premium lifestyle)
– labels, stickers, seals
– menu cards with pricing ($6.50, $8.90, etc.)
– small typography everywhere
– subtle imperfections (realism)

DESIGN LANGUAGE:

– modern minimalist typography
– Japanese-inspired layout
– soft green palette
– elegant spacing

INCLUDE:
– matcha latte
– iced matcha
– matcha desserts
– combo sets
– lifestyle shots
The composition must feel like a high-end design agency presentation.

Ultra-detailed, realistic, clean, aesthetic, and highly shareable.
```

</details>

<a id="gpt-image-restaurant-shaped-standee-template"></a>
### 夏日饮品餐饮异形立牌设计图

<a href="https://x.com/MrLarus/status/2059248197910827364"><img src="../../previews/gpt-image-restaurant-shaped-standee-template.jpg" width="360"></a>

用方括号字段模板填写品牌、产品、卖点和促销信息，可复用于任何菜单。它限定纯白背景、完整异形轮廓和可见底座，并规定从标题到主推产品再到价格的阅读层级。

GPT Image 2 · 文生图 · 出处: [@MrLarus on X](https://x.com/MrLarus/status/2059248197910827364) · 发现于 [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)

[`standee`](tags.md#tag-standee) [`restaurant`](tags.md#tag-restaurant) [`food-photography`](tags.md#tag-food-photography) [`template`](tags.md#tag-template) [`pop-signage`](tags.md#tag-pop-signage)

<details><summary><b>提示词</b></summary>

```text
请生成一张高完成度的「餐饮异形展架 / 立牌」设计图，用于展示餐饮门店的新品推荐、招牌产品、套餐促销或品牌活动信息。

【基础信息】
品牌名：【品牌名】
主标题：【主标题】
副标题：【副标题】
辅助短句：【短句1】｜【短句2】｜【短句3】
主题方向：【主题方向，例如：爆辣夜市风 / 金黄浓郁风 / 清新轻食风 / 山野自然风 / 甜品下午茶风 / 快餐促销风】
主色调：【主色调】
辅助色：【辅助色】
点缀色：【点缀色】
画幅比例：【建议 3:4 竖版】

【产品内容】
主推产品：【主推产品】
辅助产品1：【辅助产品1】
辅助产品2：【辅助产品2】
辅助产品3：【辅助产品3】
辅助产品4：【辅助产品4】
加料 / 配角产品：【加料或配角产品，例如：饮品 / 小食 / 配菜 / 酱料 / 甜品】

【卖点标签】
【卖点1】
【卖点2】
【卖点3】
【卖点4】
【卖点5】
【卖点6】

【促销信息】
【促销信息1】
【促销信息2】
【促销信息3】

【最重要要求】
避免生成门店场景效果图或墙上海报展示图。请直接生成“一张完整的异形立牌成品展示图”：
- 背景必须为纯白色
- 画面中只保留一个完整的异形餐饮立牌主体
- 不要餐厅环境
- 不要商场背景
- 不要玻璃门、桌椅、墙面、人物、地面透视场景
- 不要任何真实空间背景
- 立牌主体必须完整显示
- 异形轮廓必须完整清晰
- 底座必须完整露出
- 整体像一张已经抠好的门店物料成品图 / 设计提案展示图 / 电商展示图

【画面形式】
这是一张“门店异形展架 / 立牌”的完整设计，避免普通矩形海报处理。
整体应采用明显的“不规则异形裁切轮廓”，有完整外边缘，边缘可带白色或浅色描边，具有真实门店物料感。
立牌应有明确底座，整体像可落地摆放的 KT 板 / 泡沫板 / 亚克力 / 写真喷绘展架成品。

【构图结构】
整体采用竖版、中心聚焦、信息分层清楚的结构：

1. 顶部区域：
放超大主标题，标题必须醒目、有冲击力、有餐饮 POP 招贴感。
字体可以厚重、手写感、招贴感、潮流感，但要清晰易读。
标题是整张图的第一视觉焦点。

2. 中部核心区域：
中间放最大主推产品，作为主视觉主体。
主菜必须最大、最饱满、最诱人，突出食欲感。
围绕主菜搭配 2~5 个辅助产品，形成丰富的产品组合，前后层次明确，主次分明。

3. 周边信息区域：
在主菜和辅助产品四周加入少量标签元素、推荐标、贴纸框、手写箭头、卖点说明、小标题、小气泡标签等，使其具有“餐饮门店促销物料”的视觉特征。
但要控制层级，做到“热闹但不乱”。

4. 底部促销区域：
底部放价格信息、套餐信息、活动信息或新品尝鲜信息。
价格数字要相对突出，易读清晰。
如果没有特别要求，默认不要二维码。

【视觉风格要求】
整体风格应属于“餐饮转化型视觉 + 门店 POP 异形立牌”：
- 强调食欲感
- 强调信息可读性
- 强调商业落地感
- 强调门店物料感
- 强调异形轮廓感

避免极简杂志海报、电商详情页、纯平面插画海报方向。

【食物表现要求】
所有食物必须采用真实商业美食摄影质感：
- 食物清晰真实
- 有食材颗粒感
- 有酱汁、汤汁、油光、热气、层次感
- 有丰富细节，如葱花、辣椒、芝士、香草、蔬菜、水果、虾仁、肉块等
- 主食要饱满，不能扁平
- 看起来必须“能激发食欲”
禁止过度插画化、卡通化、低质拼贴化。

【版式与信息层级】
整张立牌的阅读顺序应为：
主标题 → 主推产品 → 辅助产品 → 卖点标签 → 价格 / 活动信息

信息量可以较丰富，但必须有明确层级：
- 主标题最大
- 主菜次大
- 辅助菜稍小
- 卖点标签较小
- 底部促销清晰醒目

【适配范围】
该模板需要适用于不同主题餐饮内容，例如：
- 面 / 饭 / 粉 / 小吃
- 火锅 / 菌汤 / 地方菜
- 轻食 / 沙拉 / 咖啡简餐
- 早餐 / 套餐 / 快餐
- 茶饮 / 甜品 / 下午茶
- 节日促销 / 新品上市 / 爆品推荐 / 双人套餐

【输出要求】
请输出一张高清、清晰、商业完成度高的异形立牌设计图，满足以下条件：
- 白色背景
- 完整异形轮廓
- 完整底座
- 只展示立牌本体
- 不带真实场景环境
- 不带人物
- 不带门店背景
- 默认不带二维码
- 适合用于系列案例展示、设计提案、社交媒体发布、模板复用
```

</details>

<a id="gpt-image-streetwear-campaign-tagline"></a>
### 街头服饰广告大片，标语只出现一次

<a href="https://developers.openai.com/api/docs/guides/image-prompting#render-exact-text"><img src="../../previews/gpt-image-streetwear-campaign-tagline.jpg" width="360"></a>

标语加引号，并要求只出现一次，再禁止多余文字、水印和无关标志。凡是有固定文案的广告都可以照这个写。预览图为 Sunburst 版本。

GPT Image 2.5 · 文生图 · 出处: [OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting#render-exact-text)

[`ad`](tags.md#tag-ad) [`fashion`](tags.md#tag-fashion) [`text-render`](tags.md#tag-text-render)

<details><summary><b>提示词</b></summary>

```text
Give me a cool in culture ad / fashion shot for a brand called Thread.
It's a hip young street brand. The ad shows a group of friends hanging out together with the tagline "Yours to Create."
Make it feel like a polished campaign image for a youth streetwear audience: stylish, contemporary, energetic, and tasteful.
Use clean composition, strong color direction, natural poses, and premium fashion photography cues.
Render the tagline exactly once, clearly and legibly, integrated into the ad layout.
No extra text, no watermarks, no unrelated logos.
```

</details>

<a id="gpt-image-toy-airplane-collectible-box"></a>
### 节日限定玩具飞机收藏版包装

<a href="https://developers.openai.com/api/docs/guides/image-prompting#design-collectible-merchandise"><img src="../../previews/gpt-image-toy-airplane-collectible-box.jpg" width="360"></a>

用产品摄影的说法写材质、灯光和标签印刷，要求原创设计，包装文字逐字固定。预览图为 Sunburst 版本。

GPT Image 2.5 · 文生图 · 出处: [OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting#design-collectible-merchandise)

[`packaging`](tags.md#tag-packaging) [`product`](tags.md#tag-product) [`toy`](tags.md#tag-toy)

<details><summary><b>提示词</b></summary>

```text
Create a collectible action figure of a vintage-style toy propeller airplane with rounded wings, a front-mounted spinning propeller, slightly worn paint edges, classic childhood proportions, designed as a nostalgic holiday collectible, in blister packaging.

Concept:
A nostalgic holiday collectible inspired by the simple toy airplanes
children used to play with during winter holidays.
Evokes warmth, imagination, and childhood wonder.

Style:
Premium toy photography, realistic plastic and painted metal textures,
studio lighting, shallow depth of field,
sharp label printing, high-end retail presentation.

Constraints:
- Original design only
- No trademarks
- No watermarks
- No logos

Include ONLY this packaging text (verbatim):
"Christmas Memories Edition"
```

</details>
