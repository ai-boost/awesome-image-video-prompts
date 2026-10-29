# 照片编辑

[返回目录](../../README_zh.md) · 全部 22 条

<a id="gpt-image-selfie-chibi-sticker-doodle-edit"></a>
### 电梯镜面自拍加Q版贴纸涂鸦

<a href="https://x.com/ChillaiKalan__/status/2050614367536939243"><img src="../../previews/gpt-image-selfie-chibi-sticker-doodle-edit.jpg" width="360"></a>

提示词先锁定原图光线与色调，再叠加白色描边、多姿势的同脸Q版小人和简短手写字。限制文字数量并让吉祥物保持克制，避免画面拥挤。

GPT Image 2 · 上传图改图 · 出处: [@ChillaiKalan__ on X](https://x.com/ChillaiKalan__/status/2050614367536939243) · 1,255 赞，统计于 2026-10-28

[`doodle`](tags.md#tag-doodle) [`chibi`](tags.md#tag-chibi) [`sticker-outline`](tags.md#tag-sticker-outline) [`xiaohongshu`](tags.md#tag-xiaohongshu) [`selfie`](tags.md#tag-selfie)

<details><summary><b>提示词</b></summary>

```text
Edit this photo into a cute Pinterest/Xiaohongshu-style doodle aesthetic edit while keeping the original composition and colors natural. Do NOT heavily change the original lighting or color grading. Keep the tones soft, airy, warm, and realistic. Avoid oversaturated colors, HDR effects, strong orange filters, or excessive contrast.￼ Add hand-drawn doodle elements around the main objects: * white outline strokes * sketchy sparkles * stars * hearts * arrows * tiny flowers * playful swirls * mini handwritten notes Add small cute mascot-style doodles that match the vibe of the photo (tiny bear, smiling drink, cute food character, sleepy cloud, etc.) but keep them subtle and balanced. Use handwritten white text with short relatable captions only. Do NOT add too many words or overcrowd the image.Use a real face as a reference photo. The background is the same as in the photo. The lighting is warm, soft, and clean, with subtle shadows. Around the image, add several mini chibi (3D cute style) versions of the character, while maintaining the original facial features.Chibi characters have various poses and expressions: jumping cheerfully waving sitting relaxed holding a drink cute and playful expressions.￼ ￼ Add hand-drawn white doodle elements: outline around the main body stars, hearts, sparkles motion lines small cute icons Add aesthetic handwriting such as: "shine," "bright day," "happy," "smile," etc. (casual doodle font) Overall style: clean & aesthetic composition white sticker outline soft pastel color tone high detail 3D chibi glossy look cute Korean.￼
```

</details>

<a id="nano-banana-json-reconstruction"></a>
### 逐项复刻一张照片的 JSON 提示词

<a href="https://x.com/ViralOps_/status/2107538470818484305"><img src="../../previews/nano-banana-json-reconstruction.jpg" width="360"></a>

按 JSON 字段写（构图、光线、色彩、负面词）。原帖用同一段 JSON 对比了 Nano Banana 2.1 和 GPT Image 2.5。

Nano Banana 2.1 · 上传图改图 · 出处: [@ViralOps_ on X](https://x.com/ViralOps_/status/2107538470818484305) · 326 赞，统计于 2026-10-27

[`json`](tags.md#tag-json) [`reconstruction`](tags.md#tag-reconstruction) [`comparison`](tags.md#tag-comparison)

<details><summary><b>提示词</b></summary>

```text
{
  "prompt_type": "detailed_image_reconstruction",
  "aspect_ratio": "4:5 vertical portrait",
  "overall_goal": "Recreate the visual appearance, framing, lighting, styling, and casual smartphone-photo feel of the reference image as closely as possible while keeping the result photorealistic and natural.",

  "subject": {
    "type": "young adult woman",
    "age_range": "early to mid 20s",
    "pose": "standing indoors, upper body turned slightly away from the camera while her face turns toward the lens",
    "body_position": "relaxed casual posture with shoulders slightly angled",
    "expression": "soft neutral expression with a subtle pout, calm and confident",
    "gaze": "looking directly toward the camera",
    "styling": "minimal everyday styling, clean and natural"
  },

  "face": {
    "shape": "soft oval face with a gently tapered jawline",
    "forehead": "medium-height forehead partly framed by center-parted hair",
    "eyebrows": "natural medium-thick dark brown eyebrows with a soft arch",
    "eyes": {
      "shape": "almond-shaped",
      "color": "light brown to hazel",
      "appearance": "bright eyes with visible catchlights",
      "lashes": "long defined eyelashes with subtle mascara"
    },
    "nose": "small straight nose with a softly rounded tip",
    "lips": {
      "shape": "full lips with a defined cupid's bow",
      "color": "natural rosy pink",
      "finish": "soft satin finish, not glossy"
    },
    "skin": {
      "tone": "light warm-neutral skin tone",
      "texture": "smooth natural skin with subtle pores and realistic tonal variation",
      "cheeks": "soft natural pink flush",
      "finish": "fresh luminous skin without heavy retouching"
    },
    "makeup": "very light natural makeup, softly defined lashes, subtle blush, natural pink lips, no dramatic contour"
  },

  "hair": {
    "color": "rich medium-to-dark chocolate brown",
    "length": "very long, extending well below the chest",
    "parting": "clean center part",
    "texture": "mostly straight with very soft natural bends through the lower lengths",
    "density": "thick and healthy-looking",
    "finish": "smooth and glossy but still realistic",
    "front_sections": "two thin face-framing strands falling naturally along both sides of the face",
    "details": "visible individual strands, subtle flyaways near the crown, realistic highlights from sunlight, natural uneven strand separation",
    "movement": "hair hanging naturally over both shoulders and down the front of the shirt"
  },

  "clothing": {
    "top": "oversized plain white crew-neck T-shirt",
    "fit": "loose casual fit",
    "fabric": "soft slightly wrinkled cotton",
    "logos": "none",
    "accessories": "no visible jewelry or prominent accessories"
  },

  "composition": {
    "shot_type": "close upper-body portrait",
    "camera_angle": "slightly above chest level, close to eye level",
    "camera_distance": "approximately arm's-length smartphone distance",
    "subject_position": "face slightly right of center with long hair occupying much of the lower frame",
    "crop": "top of head fully visible, image extending down to around lower torso",
    "orientation": "vertical",
    "perspective": "natural wide smartphone-camera perspective with mild close-range distortion"
  },

  "lighting": {
    "primary_source": "strong warm natural sunlight entering from the side/front through a nearby window",
    "direction": "sunlight striking the subject from camera-left/front",
    "face_effect": "bright warm illumination across the forehead, cheeks, nose, and hair",
    "hair_effect": "distinct brown highlights and soft reflective streaks along individual strands",
    "shadow_quality": "strong but soft-edged natural indoor shadows",
    "exposure": "face slightly brightly exposed while the room behind remains much darker",
    "color_temperature": "warm daylight"
  },

  "environment": {
    "location": "casual indoor residential room",
    "background": "dark gray walls with a white ceiling cornice",
    "left_background": "open doorway or darker hallway area",
    "right_background": "dark wall and partially visible household objects",
    "lower_right": "part of a black tripod or light stand visible",
    "overall_feel": "ordinary lived-in room rather than a studio",
    "depth": "background moderately out of focus but still recognizable"
  },

  "camera": {
    "capture_device": "modern smartphone camera",
    "lens_equivalent": "approximately 24-28mm full-frame equivalent",
    "focus": "sharp focus on face and front hair",
    "depth_of_field": "mostly natural smartphone depth of field with gentle background softness",
    "dynamic_range": "realistic phone-camera HDR with slightly clipped highlights in direct sun",
    "image_character": "casual social-media selfie/photo, not professionally staged"
  },

  "photorealism_details": [
    "real individual hair strands",
    "natural skin pores and micro-texture",
    "subtle peach fuzz",
    "realistic eyelash separation",
    "tiny variations in lip texture",
    "slight fabric creases in the T-shirt",
    "small flyaway hairs around the crown",
    "natural sunlight falloff across the face",
    "slightly imperfect casual framing",
    "realistic indoor shadow noise"
  ],

  "style": {
    "visual_style": "highly photorealistic casual smartphone portrait",
    "mood": "soft, youthful, relaxed, sunlit",
    "processing": "light social-media style processing with warm skin tones and slightly enhanced clarity",
    "avoid": [
      "cinematic movie lighting",
      "studio portrait lighting",
      "overly smooth plastic skin",
      "CGI appearance",
      "anime or illustration",
      "heavy beauty filter",
      "extreme facial symmetry",
      "over-sharpened hair",
      "artificial jet-black hair",
      "dramatic makeup",
      "excessive background blur",
      "professional studio backdrop",
      "text",
      "watermarks",
      "logos"
    ]
  },

  "negative_prompt": "cartoon, anime, illustration, CGI, plastic skin, waxy face, over-retouched skin, excessive beauty filter, unnatural facial symmetry, distorted eyes, crossed eyes, malformed lips, warped face, duplicate hair strands, fake wig appearance, overly black hair, metallic hair shine, stiff hair, messy anatomy, distorted shoulders, extra limbs, extra fingers, studio backdrop, cinematic lighting, dramatic color grading, excessive bokeh, oversaturated colors, text, logo, watermark"
}
```

</details>

<a id="gpt-image-mural-twin-half-heart-illusion"></a>
### 女子与壁画分身合成一颗爱心

<a href="https://x.com/Kubra_286/status/2102235098703880428"><img src="../../previews/gpt-image-mural-twin-half-heart-illusion.jpg" width="360"></a>

把壁画和真人分成两个带标签的段落并保持同款穿搭，指尖才能拼成完整爱心。结尾补充强制透视和砖纹叠加，让画面看起来像画在墙上。

GPT Image 2.5 · 上传图改图 · 出处: [@Kubra_286 on X](https://x.com/Kubra_286/status/2102235098703880428) · 241 赞，统计于 2026-10-28

[`mural`](tags.md#tag-mural) [`trompe-l-oeil`](tags.md#tag-trompe-l-oeil) [`forced-perspective`](tags.md#tag-forced-perspective) [`street-art`](tags.md#tag-street-art) [`selfie`](tags.md#tag-selfie)

<details><summary><b>提示词</b></summary>

```text
Ultra realistic cinematic photo of a young woman making a half heart sign with her mural twin, interactive street art illusion.

Face match 100%

Mural on brick wall: giant hyper-realistic painting of the same woman, shoulder-length wavy blonde hair with dark roots, smiling side profile, wearing light pink ribbed cropped t-shirt, small hoop earrings, delicate 'Clariz' name necklace, right hand raised making half heart shape with thumb and index finger. Photorealistic mural style, brick texture visible through paint, black graffiti background.

Real woman: same woman, same face, shoulder-length wavy blonde hair, same pink ribbed crop top, brown dark cargo pants with side pockets, blue and white sneakers. Standing on sidewalk facing the mural, left hand raised completing the other half of the heart shape with the painted hand, fingers almost touching, perfect alignment forming a full heart. Smiling at mural.

Environment: urban alley brick wall with graffiti, posters and stickers on adjacent wall, small green plants growing along wall base, concrete sidewalk, soft natural daylight.

Style: true to life color grading, photorealistic, DSLR 8K, ultra detailed skin, same face recognizable, natural shadows, 9:16 vertical portrait, trompe-l'oeil, Instagram couple bestie heart hand trend.
*Pro tip to get it perfect:*
two people making heart shape, one real one painted, fingertip connection point, forced perspective heart illusion, brick overlay on mural, same outfit mural and real
```

</details>

<a id="gpt-image-minimi-tiny-figures-photo-world"></a>
### 人像照片周围的迷你3D小人互动

<a href="https://x.com/Zyrellix/status/2055486410749309438"><img src="../../previews/gpt-image-minimi-tiny-figures-photo-world.jpg" width="360"></a>

提示词列出小人的具体互动，如坐在肩上和包上、挥手、模仿姿势，每个小人都有明确动作。同时要求保留原照片并带真实阴影和景深，让小人自然融入而不是重绘照片。

GPT Image 2 · 上传图改图 · 出处: [@Zyrellix on X](https://x.com/Zyrellix/status/2055486410749309438) · 212 赞，统计于 2026-10-28

[`minimi`](tags.md#tag-minimi) [`miniature`](tags.md#tag-miniature) [`photo-to-3d`](tags.md#tag-photo-to-3d) [`portrait`](tags.md#tag-portrait) [`chibi`](tags.md#tag-chibi)

<details><summary><b>提示词</b></summary>

```text
Transform this photo into a tiny “Minimi” world where miniature 3D characters interact naturally around me — sitting on my shoulder and bag, waving, copying my pose, and exploring the scene. Keep the original photo intact with realistic shadows, depth, motion, warm emotions. Title: “Tiny Moments Beside Me”
```

</details>

<a id="gpt-image-big-head-miniature-person-photo-edit"></a>
### 商场自拍照变超大头迷你人像

<a href="https://x.com/oggii_0/status/2113887497751253111"><img src="../../previews/gpt-image-big-head-miniature-person-photo-edit.jpg" width="360"></a>

按优先级排列指令并给出数值比例，例如头宽为肩宽的2.5到3倍、四肢缩到25%到35%。姿势、面部、服装和场景各设保留章节，再用禁止清单排除卡通和娃娃脸。

GPT Image 2.5 · 上传图改图 · 出处: [@oggii_0 on X](https://x.com/oggii_0/status/2113887497751253111) · 180 赞，统计于 2026-10-28

[`chibi`](tags.md#tag-chibi) [`big-head`](tags.md#tag-big-head) [`photo-edit`](tags.md#tag-photo-edit) [`photorealistic`](tags.md#tag-photorealistic) [`proportion`](tags.md#tag-proportion)

<details><summary><b>提示词</b></summary>

```text
Turn any photo into a hyper-realistic chibi-style portrait using GPT Image 2.5

Prompt : Hyper-Realistic Big-Head Miniature Person | Photo Editing Prompt

Strictly edit the uploaded original photograph to transform the person or animal into a hyper-realistic, extremely exaggerated big-head miniature figure.

Highest Priority: Change only the head-to-body proportions. Preserve the original appearance, pose, actions, clothing, accessories, background, and aspect ratio of the photograph completely.

1\. Head-to-Body Proportions (Highest Priority)

* Giant Head: Dramatically enlarge the entire head, including hair, hats, and ears. The head width should be approximately 2.5–3 times the width of the reduced shoulders.

* Extremely Narrow Shoulders: Make the shoulders significantly narrower than the head, with a short, small neck. Do not retain normal adult shoulder width.

* Miniature Body: In full-body photographs, the body height (excluding the head) should be approximately 0.9–1.1 times the head height. Scale down the torso, waist, hips, and limbs proportionally.

* Miniature Hands and Feet: Reduce the arms, palms, fingers, legs, feet, and shoes to approximately 25–35% of their normal proportions. The limbs must be short and slender. Never leave the hands or feet at normal size.

* Strong Proportional Contrast: Regardless of whether the subject wears a skirt, trousers, or loose-fitting clothing, the result must clearly emphasize a giant, realistic head, extremely narrow shoulders, and an ultra-miniature body.

### 2\. Pose and Actions (Strictly Preserve)

Preserve the original subject's exact pose, actions, gestures, gaze direction, and interactions.

* If the subject is standing in the original image, keep them standing. If sitting, crouching, lying down, or leaning against an object, preserve that exact position.

* Retain the original hand positions, held objects, leg positions, and all points of contact with the surrounding environment.

* If the original image is a half-body portrait, selfie, or partial-body photograph, maintain the original framing. Do not invent or generate legs, shoes, or a complete body that was not visible in the original image.

* Never alter the pose, actions, or composition simply to accommodate the miniature body proportions.

### 3\. Facial Features and Clothing (Fully Preserve)

* Preserve the original face shape, facial features, facial proportions, expression, skin tone, hairstyle, and recognizable identity. Do not apply beauty filters, skin smoothing, eye enlargement, or face reshaping.

* Preserve the original clothing styles, materials, colors, patterns, and all accessories. Naturally scale the clothing to fit the miniature body without changing its design.

* For animals, preserve the original species, fur color, ears, facial characteristics, and expression. Only modify the head-to-body proportions.

### 4\. Scene and Composition (Fully Preserve)

* Use the original photograph as the sole reference for the scene. Preserve the background, architecture, furniture, environmental objects, lighting, shadows, and color tones.

* Maintain the original camera angle, perspective, subject placement, composition, and image aspect ratio.

* Keep all background elements at their normal, realistic sizes. Do not replace the scene or introduce new objects.

* Ensure the subject blends naturally into the environment, with realistic proportions relative to the scene and physically consistent shadows.

### 5\. Visual Style

The entire image must maintain an extremely photorealistic photographic quality. Preserve realistic skin texture, individual hairs, fabric details, and natural lighting. The transition between the enlarged head and miniature body must appear seamless, with no visible compositing artifacts.

Strictly Prohibited:

* Cartoon, anime, or stylized 3D figurine aesthetics.

* Doll-like faces or AI beauty enhancements.

* Normal adult shoulder width.

* Oversized hands or feet.
```

</details>

<a id="nano-banana-chiaroscuro-portrait"></a>
### 把你的照片拍成明暗对比强烈的电影特写

<a href="https://x.com/rovvmut_/status/2107691827323392159"><img src="../../previews/nano-banana-chiaroscuro-portrait.jpg" width="360"></a>

单侧光，明确要求看得见毛孔，皮肤就不会像磨过皮。

Nano Banana 2.1 · 上传图改图 · 出处: [@rovvmut_ on X](https://x.com/rovvmut_/status/2107691827323392159) · 170 赞，统计于 2026-10-27

[`chiaroscuro`](tags.md#tag-chiaroscuro) [`cinematic`](tags.md#tag-cinematic) [`skin-detail`](tags.md#tag-skin-detail)

<details><summary><b>提示词</b></summary>

```text
A hyper-realistic, 8K resolution cinematic close-up portrait of the person in the uploaded image. The image features dramatic chiaroscuro lighting, heavily illuminating the left side of his face while casting deep, moody shadows on the right against a solid black background. He has an intense, direct gaze, dark brown eyes with square catchlights, and textured, wet-styled hair. He is wearing a plain black t-shirt. Render with 35mm film grain and a shallow depth of field, prioritizing extreme character consistency and highly detailed skin texture, including visible pores.
```

</details>

<a id="gpt-image-blue-backdrop-studio-portrait-character-swap"></a>
### 蓝色背景棚拍肖像角色替换

<a href="https://x.com/john_my07/status/2099162876842049901"><img src="../../previews/gpt-image-blue-backdrop-studio-portrait-character-swap.jpg" width="360"></a>

先逐项列出参考图的构图、姿态、视线和光线要求,再替换为指定角色并锁定面部特征。结尾用一组明确的禁止修改条款,固定背景、取景和五官。

GPT Image 2.5 · 上传图改图 · 出处: [@john_my07 on X](https://x.com/john_my07/status/2099162876842049901) · 85 赞，统计于 2026-10-28

[`studio-portrait`](tags.md#tag-studio-portrait) [`character-swap`](tags.md#tag-character-swap) [`blue-backdrop`](tags.md#tag-blue-backdrop) [`editorial`](tags.md#tag-editorial) [`fashion`](tags.md#tag-fashion)

<details><summary><b>提示词</b></summary>

```text
Do not alter the background color or studio environment. Do not change the pose, framing, crop, perspective, subject distance, lighting direction, or gaze. Do not modify facial identity, facial proportions, skin tone, or hairstyle. Avoid excessive retouching, artificial skin smoothing, stylized illustration effects, exaggerated sharpening, extra accessories, text overlays, logos, watermarks, duplicate subjects, or unrealistic clothing physics.
```

</details>

<a id="gpt-image-storyboard-panels-to-photographic-frames"></a>
### 屋顶追逐分镜稿转为写实摄影画面

<a href="https://x.com/umesh_ai/status/2110761775067230600"><img src="../../previews/gpt-image-storyboard-panels-to-photographic-frames.jpg" width="360"></a>

一句简短指令把六格铅笔分镜转成写实摄影，同时锁定构图、主体位置和机位，镜头设计在风格转换后依然保留。把两张分镜板并排放置，前后对比一目了然。

GPT Image 2.5 · 上传图改图 · 出处: [@umesh_ai on X](https://x.com/umesh_ai/status/2110761775067230600) · 68 赞，统计于 2026-10-28

[`storyboard`](tags.md#tag-storyboard) [`pencil-sketch`](tags.md#tag-pencil-sketch) [`photorealistic`](tags.md#tag-photorealistic) [`film-previs`](tags.md#tag-film-previs) [`layout-preservation`](tags.md#tag-layout-preservation)

<details><summary><b>提示词</b></summary>

```text
Big news!

Krea 3 is promising Nano Banana Pro/GPT Image 2.5  quality, 5x faster.

Imagine turning storyboard images into photographic frames you could put in front of a director.

The prompt I’d use: “Make every panel photographic. Preserve the composition, subject placement and camera angle.”

Then put the two boards side by side.

Some ideas become much harder to leave in a folder once you can see what they could look like.
```

</details>

<a id="gpt-image-1942-arcade-city-pilot-walk"></a>
### 飞行员走过街机空战主题的战时城市

<a href="https://x.com/Xaroon_x/status/2056940561148363010"><img src="../../previews/gpt-image-1942-arcade-city-pilot-walk.jpg" width="360"></a>

提示词按世界观、喜剧细节、光线和镜头分段列出清单，让背景塞满层次分明的小细节。用 exact face 锁定参考人脸，同时把服装逐件写明。

GPT Image 2 · 上传图改图 · 出处: [@Xaroon_x on X](https://x.com/Xaroon_x/status/2056940561148363010) · 发现于 [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)

[`wwii`](tags.md#tag-wwii) [`arcade`](tags.md#tag-arcade) [`cinematic`](tags.md#tag-cinematic) [`worldbuilding`](tags.md#tag-worldbuilding) [`face-reference`](tags.md#tag-face-reference)

<details><summary><b>提示词</b></summary>

```text
Ultra-realistic cinematic “1942 City” scene, retro WWII arcade-shooter-inspired metropolis in real life, intense aerial-war atmosphere, vertical 4:5 editorial composition

Male, exact face, vintage military-pilot-inspired streetwear from head to toe, bomber jacket with retro aviation patches, fitted cargo trousers, rugged combat boots, fingerless gloves, pilot goggles hanging around neck, walking through the city with fearless ace-pilot expression while fighter planes soar overhead

✈️ 1942 CITY WORLDBUILDING

entire city functions like a living 1942 arcade shooter universe
• massive WWII fighter planes dogfighting above skyscrapers
• giant anti-aircraft cannons mounted across rooftops
• endless bullet patterns streaking through cloudy skies
• retro military airfields integrated into urban districts
• giant “MISSION START” alerts projected into the clouds
• dramatic explosion trails lighting the skyline at night
• aircraft carriers docked beside futuristic city ports
• glowing power-up icons floating through aerial battle zones
• giant radar systems rotating above downtown towers
• endless enemy squadrons emerging from storm clouds
• cinematic ocean-and-warzone environments surrounding the metropolis

😂 COMEDIC DETAILS

• random civilians casually dodging fighter planes on the way to work 😭
• one pilot barrel-rolling dramatically for absolutely no reason
• giant billboard flashing: “PLAYER 1 READY.”
• pedestrians treating near-miss explosions like normal traffic
• somebody still trying to collect every floating power-up midair
• random mechanic repairing planes using pure confidence
• one legendary pilot surviving impossible situations through arcade logic alone

💡 LIGHTING & STYLE

retro war-film cinematic lighting, fiery aerial-battle atmosphere, dramatic clouds and explosion reflections, hyper-detailed realistic textures mixed with nostalgic arcade-shooter aesthetics, intense blockbuster-war energy, masterpiece quality

🎥 CAMERA

cinematic aerial tracking shot, immersive dogfight atmosphere, dynamic motion blur from fighter planes and explosions, documentary-meets-retro-arcade realism, futuristic Manila-inspired 1942 metropolis, “classic arcade air combat became civilization” atmosphere
```

</details>

<a id="gpt-image-billboard-winter-evening"></a>
### 同一块广告牌改成下雪的冬夜

<a href="https://developers.openai.com/api/docs/guides/image-prompting#refine-an-image-across-turns"><img src="../../previews/gpt-image-billboard-winter-evening.jpg" width="360"></a>

把上一步的成品作为输入，只提一个改动。每次只改一处，才看得出是哪一步起了作用。预览图为 Sunburst 版本。

GPT Image 2.5 · 上传图改图 · 出处: [OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting#refine-an-image-across-turns)

[`multi-turn`](tags.md#tag-multi-turn) [`weather`](tags.md#tag-weather) [`edit`](tags.md#tag-edit)

<details><summary><b>提示词</b></summary>

```text
Make it look like a winter evening with snowfall.
```

</details>

输入素材: [1](https://developers.openai.com/images/platform/guides/image-prompting/billboard-gpt-image-2-5-sunburst.webp)

<a id="gpt-image-japanese-film-garden-color-grade"></a>
### 春日庭园的日系胶片调色

<a href="https://x.com/HoodyLiu/status/2099115784417251690"><img src="../../previews/gpt-image-japanese-film-garden-color-grade.jpg" width="360"></a>

提示词先锁定构图和所有物体，再分别给天空、樱花、绿植和水面设定调色目标。末尾列出大量禁用效果并以柯达 Portra 400 为参照，让结果像调过色的 RAW 原片而不是重新生成的图。

GPT Image 2.5 · 上传图改图 · 出处: [@HoodyLiu on X](https://x.com/HoodyLiu/status/2099115784417251690) · 发现于 [wangrunlin/awesome-gpt-image-2-5-prompts](https://github.com/wangrunlin/awesome-gpt-image-2-5-prompts)

[`color-grading`](tags.md#tag-color-grading) [`japanese-film`](tags.md#tag-japanese-film) [`cherry-blossom`](tags.md#tag-cherry-blossom) [`portra-400`](tags.md#tag-portra-400) [`photo-retouch`](tags.md#tag-photo-retouch)

<details><summary><b>提示词</b></summary>

```text
Please only perform professional color grading and light and shadow optimization on the original photos, strictly retain the original composition, scenery positions, cherry blossoms, trees, water reflections and screen proportions, and do not add, delete or change any objects. The overall style is adjusted to a high-end, restrained, and quiet Japanese film style, presenting the quiet atmosphere of a Japanese garden in early spring. Moderately brighten the dark details in the woods, waterfronts and ponds, and restore the layers of tree trunks, shrubs and water surfaces, but retain deep shadows and do not turn black areas into gray. Reduce the sky highlights and blue saturation, and adjust the sky to a transparent, calm gray-blue to avoid excessive brightness and HDR effects. Highlight the cherry blossoms in the center of the picture, making the flowers a natural pale pink-white color to add soft sunlight transparency and delicate layers. Do not turn it into pure white or fluorescent pink. The green plants are adjusted to low-saturated moss green, forest green and slight olive green, reducing the yellow-green and digital feel. The water surface maintains a deep blue-black color, enhancing the subtle reflections and layers of fallen cherry blossoms, making the reflection clear but not sharp. The overall design uses soft highlights, deep shadows, medium to strong contrast, and slightly increases the contrast between warm sunlight and cool shadows. Adding slight film fog, natural halo, fine 35mm film grain and soft sharpening, the color refers to Kodak Portra 400 and Japanese film photography, which is real, natural, subtle, airy and high-end. It is prohibited to change the composition, add cherry blossoms, clouds, buildings, people or lights, generate new branches, change the season, overexposure, dead black, HDR, over-sharpening, fluorescent green, brilliant blue sky, heavy filters, oil painting feeling, illustration feeling and AI redrawing feeling. The end result must be like a professional color correction of the original RAW photo, not a regenerated image.
```

</details>

<a id="gpt-image-laptop-screen-spreadsheet-to-workflow-diagram"></a>
### 笔记本屏幕换成自动化流程图

<a href="https://x.com/ai_kairos_jp/status/2097679848475099159"><img src="../../previews/gpt-image-laptop-screen-spreadsheet-to-workflow-diagram.jpg" width="360"></a>

只点名要改的屏幕区域和替换内容，再逐项列出必须保持不变的桌面、便签、灯光和夜景窗外。明确写出保留项，局部编辑时其余画面才不容易跑偏。

GPT Image 2.5 · 上传图改图 · 出处: [@ai_kairos_jp on X](https://x.com/ai_kairos_jp/status/2097679848475099159) · 发现于 [wangrunlin/awesome-gpt-image-2-5-prompts](https://github.com/wangrunlin/awesome-gpt-image-2-5-prompts)

[`local-edit`](tags.md#tag-local-edit) [`screen-replacement`](tags.md#tag-screen-replacement) [`workflow-diagram`](tags.md#tag-workflow-diagram) [`preserve-scene`](tags.md#tag-preserve-scene) [`desk-scene`](tags.md#tag-desk-scene)

<details><summary><b>提示词</b></summary>

```text
Replace the spreadsheet with an automation workflow diagram. Do not change the desk, sticky notes, lighting or the nighttime view through the window.
```

</details>

<a id="gpt-image-outfit-swap-keep-identity"></a>
### 用三件参考服装换装，人物不变

<a href="https://developers.openai.com/api/docs/guides/image-prompting#preserve-identity-and-change-clothing"><img src="../../previews/gpt-image-outfit-swap-keep-identity.jpg" width="360"></a>

先列出人物身上所有必须不变的东西，只放开服装，再要求光影匹配原图。要让产品保持可辨认也可以照这个写。预览图为 Sunburst 版本。

GPT Image 2.5 · 上传图改图 · 出处: [OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting#preserve-identity-and-change-clothing)

[`virtual-try-on`](tags.md#tag-virtual-try-on) [`fashion`](tags.md#tag-fashion) [`identity`](tags.md#tag-identity)

<details><summary><b>提示词</b></summary>

```text
Edit the image to dress the woman using the provided clothing images. Do not change her face, facial features, skin tone, body shape, pose, or identity in any way. Preserve her exact likeness, expression, hairstyle, and proportions. Replace only the clothing, fitting the garments naturally to her existing pose and body geometry with realistic fabric behavior. Match lighting, shadows, and color temperature to the original photo so the outfit integrates photorealistically, without looking pasted on. Do not change the background, camera angle, framing, or image quality, and do not add accessories, text, logos, or watermarks.
```

</details>

输入素材: [1](https://developers.openai.com/images/platform/guides/image-prompting/woman-in-museum.webp) · [2](https://developers.openai.com/images/platform/guides/image-prompting/jacket.webp) · [3](https://developers.openai.com/images/platform/guides/image-prompting/tank-top.webp) · [4](https://developers.openai.com/images/platform/guides/image-prompting/boots.webp)

<a id="gpt-image-person-into-campsite-scene"></a>
### 把人物放进黄昏营地逃跑的场景

<a href="https://developers.openai.com/api/docs/guides/image-prompting#insert-a-person-into-a-scene"><img src="../../previews/gpt-image-person-into-campsite-scene.jpg" width="360"></a>

写清姿态、视线、服装、地点和时间，并反复要求像真实照片，不要电影海报感。预览图为 Sunburst 版本。

GPT Image 2.5 · 上传图改图 · 出处: [OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting#insert-a-person-into-a-scene)

[`identity`](tags.md#tag-identity) [`action`](tags.md#tag-action) [`photorealism`](tags.md#tag-photorealism)

<details><summary><b>提示词</b></summary>

```text
Generate a highly realistic action scene where this person is running away from a large, realistic brown bear attacking a campsite. The image should look like a real photograph someone could have taken, not an overly enhanced or cinematic movie-poster image.
She is centered in the image but looking away from the camera, wearing outdoorsy camping attire, with dirt on her face and tears in her clothing. She is clearly afraid but focused on escaping, running away from the bear as it destroys the campsite behind her.
The campsite is in Yosemite National Park, with believable natural details. The time of day is dusk, with natural lighting and realistic colors. Everything should feel grounded, authentic, and unstyled, as if captured in a real moment. Avoid cinematic lighting, dramatic color grading, or stylized composition.
```

</details>

输入素材: [1](https://developers.openai.com/images/platform/guides/image-prompting/woman-in-museum.webp)

<a id="gpt-image-photo-background-doodle-people-swap"></a>
### 海边栈道上的涂鸦母女

<a href="https://x.com/Emmma__0/status/2091391958128251286"><img src="../../previews/gpt-image-photo-background-doodle-people-swap.jpg" width="360"></a>

提示词先立下核心规则，背景保持实拍、人物改为涂鸦，再逐项锁定人数、位置、朝向、姿态和服装颜色。末尾的优先级排序和禁止清单让背景不被涂鸦化。

GPT Image 2 · 上传图改图 · 出处: [@Emmma__0 on X](https://x.com/Emmma__0/status/2091391958128251286) · 发现于 [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)

[`doodle`](tags.md#tag-doodle) [`photo-edit`](tags.md#tag-photo-edit) [`people-replacement`](tags.md#tag-people-replacement) [`hand-drawn`](tags.md#tag-hand-drawn) [`background-preserve`](tags.md#tag-background-preserve)

<details><summary><b>提示词</b></summary>

```text
Transform ONLY the people in the uploaded photo into adorable hand-drawn doodle characters while keeping the original photographic background unchanged.

CORE RULE:
Background = original realistic photo.
People = cute hand-drawn doodle characters.

PRESERVE THE BACKGROUND:
Keep the original sky, landscape, buildings, water, furniture, ground, plants, railings, objects, lighting, colors, perspective, camera angle, framing, and textures as close to the original photo as possible.

Do NOT redraw, simplify, illustrate, or apply doodle/crayon/pencil effects to the background or environmental objects.

TRANSFORM ONLY PEOPLE:
Replace each person with a charming, naive doodle version while preserving:
- exact number of people
- original position and relative scale
- front/back/side/three-quarter orientation
- head and body direction
- pose and gesture
- arm and leg positions
- interactions with people or objects
- hairstyle, clothing colors, and major accessories

IMPORTANT:
If someone faces away, keep them back-facing.
If sideways, keep them sideways.
If facing forward, keep them forward.
Never rotate a person toward the viewer or invent a face that is not visible.

CUTE DOODLE STYLE:
Freely reinterpret realistic anatomy into an adorable, imperfect character:
- oversized round head
- tiny compact body
- short simplified arms and legs
- tiny hands and feet
- cute awkward proportions
- loose scribbled hair
- tiny dot eyes and simple facial features when visible
- rosy scribbled cheeks when appropriate

Keep the original pose recognizable, but simplify and slightly exaggerate it for cuteness.

DRAWING STYLE:
Loose naive hand-drawn doodle, like a quick children's sketch.
Use thin shaky black outlines, imperfect shapes, overlapping sketch lines, scribbled colored-pencil or crayon fills, uneven coloring, white gaps, and slightly messy edges.

The character should look intentionally roughly drawn but extremely cute.

OBJECTS:
Objects, furniture, scenery, and items around the people should remain photographic whenever possible. A doodle character may naturally touch or hold a real photographic object.

INTEGRATION:
Keep correct scale, ground contact, depth, and occlusion so the doodle characters naturally occupy the same locations as the original people.

FINAL LOOK:
It should feel like the real people were removed from the original photograph and replaced with adorable little hand-drawn doodle versions of themselves, while the real-world background remained untouched.

Prioritize:
1. Original photographic background
2. Person position and scale
3. Exact body orientation
4. Pose and gesture
5. Cute exaggerated doodle character design

Avoid full-image illustration, background doodling, realistic anatomy, anime, manga, 3D cartoon, polished digital art, vector lines, changed poses, changed orientation, added people, or invented faces.
```

</details>

<a id="gpt-image-place-dog-into-scene"></a>
### 把一张照片里的狗放进另一张照片

<a href="https://developers.openai.com/api/docs/guides/image-prompting#combine-references"><img src="../../previews/gpt-image-place-dog-into-scene.jpg" width="360"></a>

按编号指明图片，写清移动什么、放到哪里、什么不变。预览图为 Sunburst 版本。

GPT Image 2.5 · 上传图改图 · 出处: [OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting#combine-references)

[`composite`](tags.md#tag-composite) [`reference`](tags.md#tag-reference) [`pets`](tags.md#tag-pets)

<details><summary><b>提示词</b></summary>

```text
Place the dog from the second image into the setting of image 1, right next to the woman, use the same style of lighting, composition and background. Do not change anything else.
```

</details>

输入素材: [1](https://developers.openai.com/images/platform/guides/image-prompting/test-woman.webp) · [2](https://developers.openai.com/images/platform/guides/image-prompting/test-woman-2.webp)

<a id="gpt-image-pro-instagram-pasta-photo-enhance"></a>
### 手机拍摄的意面照片优化成 Instagram 水准

<a href="https://x.com/dezainaz_ceo/status/2047172512551977162"><img src="../../previews/gpt-image-pro-instagram-pasta-photo-enhance.jpg" width="360"></a>

一句话同时设定摄影师和设计师两个角色，让模型一并处理光线调色和版面润色。适用于随手拍的手机照片，具体风格交给模型自行决定。

GPT Image 2 · 上传图改图 · 出处: [@dezainaz_ceo on X](https://x.com/dezainaz_ceo/status/2047172512551977162) · 发现于 [ZeroLu/awesome-gpt-image](https://github.com/ZeroLu/awesome-gpt-image)

[`photo-enhance`](tags.md#tag-photo-enhance) [`food`](tags.md#tag-food) [`instagram`](tags.md#tag-instagram) [`iphone-photo`](tags.md#tag-iphone-photo) [`retouch`](tags.md#tag-retouch)

<details><summary><b>提示词</b></summary>

```text
Enhance this iPhone photo with ChatGPT so it looks like a professional photographer and designer worked on it.
```

</details>

<a id="gpt-image-product-cutout-transparent"></a>
### 产品抠图，透明背景

<a href="https://developers.openai.com/api/docs/guides/image-prompting#create-a-transparent-product-cutout"><img src="../../previews/gpt-image-product-cutout-transparent.jpg" width="360"></a>

要求轮廓干净无白边、形状和标签原样保留，并禁止背景和画出来的棋盘格。输出用 PNG 或 WebP，并设 background=transparent。预览图为 Sunburst 版本。

GPT Image 2.5 · 上传图改图 · 出处: [OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting#create-a-transparent-product-cutout)

[`product`](tags.md#tag-product) [`transparent`](tags.md#tag-transparent) [`cutout`](tags.md#tag-cutout)

<details><summary><b>提示词</b></summary>

```text
Extract the product from the input image and isolate it on a fully transparent background.
Output: centered product, crisp silhouette, no halos/fringing.
Preserve product geometry and label legibility exactly.
Add only light polishing. Do not add a solid backdrop, checkerboard, scenery, or shadow.
Do not restyle the product; remove the background and preserve clean alpha transparency.
```

</details>

输入素材: [1](https://developers.openai.com/images/platform/guides/image-prompting/shampoo.webp)

<a id="gpt-image-remove-object-from-hand"></a>
### 去掉男人手里的花

<a href="https://developers.openai.com/api/docs/guides/image-prompting#remove-an-object"><img src="../../previews/gpt-image-remove-object-from-hand.jpg" width="360"></a>

只点名要去掉的那一个物体，并要求其他都不变，不用蒙版也能把改动限制在局部。预览图为 Sunburst 版本。

GPT Image 2.5 · 上传图改图 · 出处: [OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting#remove-an-object)

[`remove`](tags.md#tag-remove) [`inpainting`](tags.md#tag-inpainting) [`local-edit`](tags.md#tag-local-edit)

<details><summary><b>提示词</b></summary>

```text
Remove the flower from man's hand. Do not change anything else.
```

</details>

输入素材: [1](https://developers.openai.com/images/platform/guides/image-prompting/man-with-blue-hat.webp)

<a id="gpt-image-sketch-to-photo-valley"></a>
### 河谷线稿渲染成照片

<a href="https://developers.openai.com/api/docs/guides/image-prompting#turn-a-drawing-into-a-realistic-image"><img src="../../previews/gpt-image-sketch-to-photo-valley.jpg" width="360"></a>

锁定布局、比例和透视，材质和光线交给模型，并禁止添加新元素，避免它自由发挥。预览图为 Sunburst 版本。

GPT Image 2.5 · 上传图改图 · 出处: [OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting#turn-a-drawing-into-a-realistic-image)

[`sketch`](tags.md#tag-sketch) [`photorealism`](tags.md#tag-photorealism) [`landscape`](tags.md#tag-landscape)

<details><summary><b>提示词</b></summary>

```text
Turn this drawing into a photorealistic image.
Preserve the exact layout, proportions, and perspective.
Choose realistic materials and lighting consistent with the sketch intent.
Do not add new elements or text.
```

</details>

输入素材: [1](https://developers.openai.com/images/platform/guides/image-prompting/drawings.webp)

<a id="gpt-image-swap-kitchen-chairs"></a>
### 厨房照片里只换椅子

<a href="https://developers.openai.com/api/docs/guides/image-prompting#change-furniture-in-a-room"><img src="../../previews/gpt-image-swap-kitchen-chairs.jpg" width="360"></a>

用大写的 ONLY 限定唯一要换的东西，并列出要保留的机位、光线、地面阴影和周围物品。预览图为 Sunburst 版本。

GPT Image 2.5 · 上传图改图 · 出处: [OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting#change-furniture-in-a-room)

[`interior`](tags.md#tag-interior) [`local-edit`](tags.md#tag-local-edit) [`photorealism`](tags.md#tag-photorealism)

<details><summary><b>提示词</b></summary>

```text
In this room photo, replace ONLY the white chairs with chairs made of wood.
Preserve camera angle, room lighting, floor shadows, and surrounding objects.
Keep all other aspects of the image unchanged.
Photorealistic contact shadows and fabric texture.
```

</details>

输入素材: [1](https://developers.openai.com/images/platform/guides/image-prompting/kitchen.webp)

<a id="gpt-image-translate-infographic-spanish"></a>
### 把信息图翻译成西班牙语，版式不动

<a href="https://developers.openai.com/api/docs/guides/image-prompting#translate-while-preserving-layout"><img src="../../previews/gpt-image-translate-infographic-spanish.jpg" width="360"></a>

在咖啡机信息图上做的一句话编辑。出图后检查有没有漏翻的词。预览图为 Sunburst 版本。

GPT Image 2.5 · 上传图改图 · 出处: [OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting#translate-while-preserving-layout)

[`translation`](tags.md#tag-translation) [`edit`](tags.md#tag-edit) [`text-render`](tags.md#tag-text-render)

<details><summary><b>提示词</b></summary>

```text
Translate the text in the infographic to Spanish. Do not change any other aspect of the image.
```

</details>

输入素材: [1](https://developers.openai.com/images/platform/guides/image-prompting/infographic-coffee-machine-gpt-image-2-5-sunburst.webp)
