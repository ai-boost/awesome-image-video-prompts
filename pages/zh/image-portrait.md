# 人像

[返回目录](../../README_zh.md) · 全部 213 条 · **1** · [2](image-portrait-2.md)

<a id="gpt-image-macbook-screen-photo-booth-selfie"></a>
### 笔记本屏幕上Photo Booth里的昏暗卧室自拍

<a href="https://x.com/tadasgedgaudas/status/2046877643929166330"><img src="../../previews/gpt-image-macbook-screen-photo-booth-selfie.jpg" width="360"></a>

提示词用结构化JSON，并以身份锁定块保留输入照片中的人脸。它把结果定义为对屏幕的拍摄而不是截图，列出像素网格、摩尔纹、灰尘和指纹等物理瑕疵，再用负面清单排除平整界面和过度精修。

GPT Image 2 · 上传图改图 · 出处: [@tadasgedgaudas on X](https://x.com/tadasgedgaudas/status/2046877643929166330) · 4,434 赞，统计于 2026-10-28

[`screen-photo`](tags.md#tag-screen-photo) [`json-prompt`](tags.md#tag-json-prompt) [`identity-lock`](tags.md#tag-identity-lock) [`low-light`](tags.md#tag-low-light) [`candid`](tags.md#tag-candid)

<details><summary><b>提示词</b></summary>

```text
{"image_settings": {"aspect_ratio": "3:4", "resolution": {"width": 1152, "height": 1536}}, "prompt": {"identity_lock": {"reference": "input_photo", "preserve": ["face", "facial proportions", "eye shape", "nose", "lips", "skin tone", "skin texture", "hairline", "overall identity"], "rules": ["no face swap", "no beautify", "no smoothing", "no reshaping", "no AI look"]}, "scene": {"camera_angle": "high-angle downward shot, POV", "composition": "MacBook screen fills most of the frame, thin strip of physical keyboard visible at the bottom", "screen_surface": ["visible RGB pixel grid", "subtle moire effect", "micro dust on glass", "faint fingerprints", "soft ambient reflections"]}, "digital_interface": {"os": "macOS dark mode", "background_app": {"name": "Spotify", "view": "Liked Songs", "visible_tracks": ["Blank Space \u2013 Taylor Swift", "Shake It Off \u2013 Taylor Swift", "Cruel Summer \u2013 Taylor Swift", "Love Story \u2013 Taylor Swift"]}, "foreground_app": {"name": "Photo Booth", "state": "live preview window", "position": "floating, center-right"}}, "photo_booth_content": {"environment": {"room": "dim bedroom", "background": "off-white wall, rumpled bedding", "lighting": "low-light, nocturnal, cool screen glow mixed with warm skin tones"}, "subject": {"pose": "lying down, relaxed, candid", "expression": "natural, slightly relaxed", "outfit": "light-colored tank top", "prop": {"item": "iPhone 15 Pro", "hand": "right hand"}}}, "realism_rules": ["this is a photo of a screen, not a screenshot", "raw smartphone photo look", "natural noise", "imperfect glass", "no studio lighting", "no HD polish"]}, "negative_prompt": ["screenshot", "flat UI", "perfect screen", "clean glass", "studio lighting", "beauty filter", "cartoon", "3d render", "painting", "watermark", "blurred face"]}
```

</details>

<a id="nano-banana-tongue-out-selfie-engraved-heart-pendant"></a>
### 金发女子吐舌自拍

<a href="https://x.com/KeorUnreal/status/2042931156333543781"><img src="../../previews/nano-banana-tongue-out-selfie-engraved-heart-pendant.jpg" width="360"></a>

竖版特写自拍构图加上刻字心形吊坠，为模型提供固定的文字锚点，负面提示词则锁定其拼写。漫画式的表情通过姿态和神态呈现，而非画风，因此画面保持照片级真实感。

Nano Banana 2 · 文生图 · 出处: [@KeorUnreal on X](https://x.com/KeorUnreal/status/2042931156333543781) · 3,443 赞，统计于 2026-10-29

[`selfie`](tags.md#tag-selfie) [`photorealistic`](tags.md#tag-photorealistic) [`manga-expression`](tags.md#tag-manga-expression)

<details><summary><b>提示词</b></summary>

```text
{
  "prompt": "Vertical close-up selfie of attractive woman with long blonde hair playfully sticking her tongue out and looking up with crossed eyes like iconic manga girl, wearing a electric pink ribbed tank top with deep cleavage, golden necklaces with a heart pendant engraved 'Keor', soft natural lighting, photorealistic, detailed skin and jewelry textures, playful glamorous vibe, 8k",
  "negative_prompt": "cropped, bad hands, blurry face, low quality, different pendant text, closed mouth",
  "parameters": {
    "aspect_ratio": "9:16",
    "lighting": "soft natural"
  }
}
```

</details>

<a id="gpt-image-bougainvillea-archway-courtyard-portrait"></a>
### 海边九重葛拱门下回眸的女子

<a href="https://x.com/abxxai/status/2097698712978087966"><img src="../../previews/gpt-image-bougainvillea-archway-courtyard-portrait.jpg" width="360"></a>

提示词细致描写近处人物，第二个人物只交代服装和姿态，并从花拱门、庭院到朦胧海面逐层铺开景深。模型保留了这种分层构图和暖色调，但画出的是柔和自然光，而非提示词要求的直闪效果。

GPT Image 2.5 · 文生图 · 出处: [@abxxai on X](https://x.com/abxxai/status/2097698712978087966) · 2,645 赞，统计于 2026-10-28

[`portrait`](tags.md#tag-portrait) [`mediterranean`](tags.md#tag-mediterranean) [`flash-photography`](tags.md#tag-flash-photography) [`y2k`](tags.md#tag-y2k) [`candid`](tags.md#tag-candid)

<details><summary><b>提示词</b></summary>

```text
Two women framed by a sun-bleached stone archway — one in the near foreground at frame right, a woman with long straight golden-brown hair loosely pulled back with soft face-framing pieces, warm honey-blonde balayage catching the light, an oval face with warm brown eyes, softly tanned olive-warm skin and full lips, small stud earrings, wearing a rust-terracotta linen wrap top and matching wide-leg linen trousers cinched with a woven raffia belt, hands clasped in front of her, turned back over her shoulder toward camera; a second woman, features unspecified, stands further back in the courtyard in a deep forest-green silk blouse and wide-leg cream trousers, leaning against a whitewashed stone pillar, gazing out toward the sea. Setting: the threshold of a Mediterranean cliffside courtyard, hand-laid terracotta mosaic floor and a weathered stone archway thick with trailing bougainvillea in the foreground, a sun-drenched courtyard beyond with wrought-iron lanterns, potted olive trees and a low stone fountain, whitewashed rooftops and a pale hazy sea filling the horizon, soft late-afternoon light. Shot on an early-2000s point-and-shoot digicam with harsh direct on-camera fill flash that aggressively illuminates the near woman and the archway, flattening her features and putting sharp specular highlights on the linen, the stone and her shoulders; the courtyard and sea beyond stay visible but hazy, milky and underexposed relative to the flash. Warm, slightly saturated CCD tones, strong bloom and halation at the archway edges, minor digital noise. Candid amateur, Y2K editorial, unpolished but stylized.
```

</details>

<a id="gpt-image-car-door-clifftop-2000s-film-snapshot"></a>
### 透过敞开车门拍摄的千禧年代胶片抓拍

<a href="https://x.com/abxxai/status/2102775797509722602"><img src="../../previews/gpt-image-car-door-clifftop-2000s-film-snapshot.jpg" width="360"></a>

上传角色设定图锁定人物身份，再用场景、服装、背景、光线、相机和真实感分块写清各项要求。旧胶片质感靠 28mm 桶形畸变、抬黑、光晕和颗粒等文字描述实现而非滤镜，车门框则提供自然的前景。

GPT Image 2.5 · 上传图改图 · 出处: [@abxxai on X](https://x.com/abxxai/status/2102775797509722602) · 1,687 赞，统计于 2026-10-28

[`film-look`](tags.md#tag-film-look) [`candid`](tags.md#tag-candid) [`road-trip`](tags.md#tag-road-trip) [`character-reference`](tags.md#tag-character-reference) [`2000s`](tags.md#tag-2000s)

<details><summary><b>提示词</b></summary>

```text
4/ the start frame, GPT Image 2.5 made

the old footage look is NOT a filter.. Opus wrote it into the prompt:

Promtp:

Use the uploaded character sheet as the strict identity reference. Keep her exact face, bone structure, brown eyes, light freckles across nose and cheeks, natural full lips, and long straight light-brown hair with sun-kissed caramel highlights parted in the middle. Keep the thin gold chain necklace with the small cross pendant.

SCENE: A candid photo taken from inside a parked silver sedan, looking out through the open rear passenger door. The door frame, the grey fabric headliner, the black door panel with its chrome handle, and part of the seat belt frame the shot on both sides. She stands just outside the open door on a rocky clifftop road above the ocean, both arms raised, one hand gripping the top of the door frame and the other resting on the roof edge, leaning slightly toward the camera. Relaxed, unposed, calm expression, looking straight into the lens.

WARDROBE: Fitted cropped white cotton baby tee with a faded, sun-washed vintage graphic print in pale blue and coral red, slightly worn and soft. Light-wash low-rise denim cutoff shorts with frayed hems. Thin brown leather cord bracelets on one wrist. Hair slightly messy and windblown, a few strands across her face.

BACKGROUND: Deep blue Mediterranean sea filling the frame behind her, sparkling sun glints on the water, a flat horizon line at chest height, pale hazy sky, dark rocks and sandy stones at the cliff edge below.

LIGHT: Harsh direct midday summer sun, bright and slightly overexposed. Sun-warmed skin with a natural sheen and slight glow on the cheeks and nose, soft shadows under the chin, a faint reflection of light off the white car interior.

CAMERA AND LOOK: Early 2000s point-and-shoot film photo, 35mm film, 28mm wide lens with slight barrel distortion at the edges, shot from chest height inside the car. Warm, faded, sun-bleached color grade, lifted blacks, low contrast, creamy highlights that gently blow out in the sky, slightly yellowed whites, soft halation around bright edges, fine visible film grain, a touch of softness and imperfect focus. Looks like a real candid snapshot from a summer road trip, not a studio shot.

REALISM: Real skin texture with visible pores and freckles, no retouching, no plastic skin, natural flyaway hairs, real fabric wrinkles on the tee, real dust and wear on the car interior.

Aspect ratio 4:3. No text, no watermark, no logos.
```

</details>

<a id="gpt-image-blue-hair-doodle-shadow-pose"></a>
### 蓝发女生与她的黑色涂鸦影子

<a href="https://x.com/Ciri_ai/status/2080580411487600862"><img src="../../previews/gpt-image-blue-hair-doodle-shadow-pose.jpg" width="360"></a>

参考照片锁定了人物的脸部特征、发型和服装，真人与线稿版本保持相似。提示词要求在干净的米色墙面上画黑色线稿并加入漫画动态线，使涂鸦读起来像手绘而不是阴影或第二个真人，线稿夸张的姿势与真人可爱写实的姿势形成对比。

GPT Image 2 · 上传图改图 · 出处: [@Ciri_ai on X](https://x.com/Ciri_ai/status/2080580411487600862) · 1,606 赞，统计于 2026-10-29

[`doodle-shadow`](tags.md#tag-doodle-shadow) [`mixed-media`](tags.md#tag-mixed-media) [`reference-identity`](tags.md#tag-reference-identity) [`playful-pose`](tags.md#tag-playful-pose)

<details><summary><b>提示词</b></summary>

```text
GPT image 2 on chatgpt

Prompt: Use the uploaded character reference image as the strict identity and outfit reference.

Preserve the reference character’s:
- face identity
- facial proportions
- eye shape
- nose
- lips
- skin tone
- hairstyle
- hair color
- visible hair accessories
- overall recognizable vibe
- outfit and styling shown in the reference image

Do not hardcode any specific character traits that are not present in the uploaded reference.
All identity, hairstyle, accessories, and clothing details must be inferred directly from the uploaded reference image.

Create a high-quality mixed-style vertical portrait showing:
1. a realistic full-body version of the uploaded character/person
2. a black hand-drawn doodle-shadow version of the same character/person on the wall beside them

Core concept:
The real person and their doodle-shadow are doing a playful mischievous pose together.
The real person performs a cute realistic version of the pose, while the doodle-shadow performs a much more exaggerated, chaotic, cartoonish version of the same pose idea.
The mood should feel cute, playful, mischievous, stylish, funny, and social-media-friendly.

Real person:
- Must remain realistic and photogenic
- Must wear the same outfit style and key visible details from the uploaded reference image
- Do not replace the reference styling with unrelated fashion
- Expression should be cute, slightly confused, mildly embarrassed, playful, as if thinking: “Why am I doing this with my shadow?”
- The real person should not stand stiffly
- The real person should actively participate in the pose, but in a natural realistic way

Doodle-shadow:
- Must be a black hand-drawn sketch version of the same person, drawn directly on the wall
- Not a realistic second person
- Not a normal physical shadow
- Not a full-color anime character
- Black sketch line-art only
- Should resemble the person through hairstyle silhouette, accessories, outfit silhouette, and pose structure
- The doodle-shadow should look more energetic, sillier, and more chaotic than the real person
- Add manga-like motion lines, hearts, stars, sparkles, and comic marks around the doodle if helpful

Random mischievous pose rule:
The pose must NOT be fixed.

For each generation, invent a new playful mischievous pose for both the real person and the doodle-shadow.
The real person and the doodle-shadow should share the same general pose idea, but they do not need to match perfectly.
The real person performs a cute realistic version.
The doodle-shadow performs a much more exaggerated, chaotic, cartoonish version.

Do not repeatedly use pointing poses.
Do not repeatedly use finger-gun poses.
Do not repeatedly use the same standing pose.
Do not always make both figures simply point at each other.

Create a different mischievous pose each time.

Possible pose directions are loose inspiration only, not a fixed menu:
- playful idol pose
- silly dance pose
- leaning sideways with one arm curved overhead
- making a big heart pose
- cheeky wink pose
- hands near cheeks in a cute teasing pose
- exaggerated “ta-da!” pose
- mock surprise pose
- playful running-in-place pose
- mischievous tiptoe pose
- arms stretched in opposite directions
- pretending to sneak away
- cute troublemaker pose
- dramatic overreaction pose
- goofy victory pose
- playful balance pose
- playful peekaboo pose
- shy but mischievous pose
- cute overconfident pose

The final pose should feel fresh, cute, mischievous, and slightly chaotic.
The real person should look like they are reluctantly playing along.
The doodle-shadow should look like it is having way too much fun.

Composition:
- vertical 4:5 or 9:16
- show the real person in full-body or nearly full-body framing
- place the real person on one side of the frame
- place the black doodle-shadow on a clean wall beside them
- the doodle-shadow should be roughly the same height or slightly taller
- keep enough space around both figures so the full pose is visible
- the connection between the real person and the doodle-shadow must be clear at a glance

Background:
- simple clean indoor studio wall or minimal room corner
- white, cream, or pale gray wall
- clean floor
- soft natural sunlight patch or gentle wall shadow allowed
- keep the background uncluttered

Lighting:
- soft natural studio lighting
- bright, clean, polished, playful mood
- keep the real person’s face clearly visible

Style quality:
- realistic human photography
- black hand-drawn doodle-shadow on wall
- matching mischievous pose interaction
- strong identity resemblance
- outfit and styling faithfully based on the uploaded reference
- cute and stylish mixed-media portrait
- clean composition
- social-media-friendly
- no obvious AI artifacts

Negative prompt:
hardcoded blue hair when not in reference, hardcoded cloud clip when not in reference, hardcoded fish clip when not in reference, hardcoded school uniform when not in reference, outfit change unrelated to reference, realistic second person, normal reflection, normal shadow only, solid black monster shadow, horror shadow, creepy shadow, full-color illustration, cartoon human, anime human, weak resemblance, unrelated sketch character, messy wall, cluttered background, repeated pointing pose, repeated finger-gun pose, same pose every time, fixed pose, boring mirrored pose, stiff pose, identical pose repetition, real person not matching shadow pose, text, watermark, logo, distorted body, extra limbs, extra fingers, bad hands
```

</details>

<a id="nano-banana-sunlit-smartphone-selfie-white-tee"></a>
### 窗边阳光下身穿白T恤的手机自拍

<a href="https://www.reddit.com/r/GeminiAI/comments/1x08axv/nano_banana_21_goes_crazy"><img src="../../previews/nano-banana-sunlit-smartphone-selfie-white-tee.jpg" width="360"></a>

用结构化JSON把面部、头发、服装、光线和相机拆成独立字段，每个细节都能单独控制。写明24到28毫米手机镜头、过曝高光，再配上很长的避免清单，画面保持随手拍的真实感，不会变成影棚质感。

Nano Banana 2.1 · 文生图 · 出处: [u/RIGHT200 on Reddit](https://www.reddit.com/r/GeminiAI/comments/1x08axv/nano_banana_21_goes_crazy) · 1,204 赞，统计于 2026-10-28

[`selfie`](tags.md#tag-selfie) [`smartphone-photo`](tags.md#tag-smartphone-photo) [`json-prompt`](tags.md#tag-json-prompt) [`natural-light`](tags.md#tag-natural-light) [`photorealistic`](tags.md#tag-photorealistic)

<details><summary><b>提示词</b></summary>

```text
{

"prompt_type": "detailed_image_reconstruction",

"aspect_ratio": "16:9 horizontal portrait",

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

<a id="gpt-image-cozy-hoodie-sleeve-selfie"></a>
### 奶油色宽松卫衣里的温柔自拍

<a href="https://x.com/MissDelulu9/status/2067555456688791598"><img src="../../previews/gpt-image-cozy-hoodie-sleeve-selfie.jpg" width="360"></a>

提示词先锁定贴脸自拍的构图和脸颊靠在袖口的姿势，再依次叠加五官细节、柔和光线、浅景深和 9:16 比例，让画面像真实的前置自拍。

GPT Image 2 · 文生图 · 出处: [@MissDelulu9 on X](https://x.com/MissDelulu9/status/2067555456688791598) · 996 赞，统计于 2026-10-29

[`selfie`](tags.md#tag-selfie) [`portrait`](tags.md#tag-portrait) [`cozy`](tags.md#tag-cozy) [`shallow-depth-of-field`](tags.md#tag-shallow-depth-of-field) [`photorealistic`](tags.md#tag-photorealistic)

<details><summary><b>提示词</b></summary>

```text
Photorealistic close-up selfie of an adorable young woman, face filling most of the frame, head slightly tilted with cheek resting inside a cozy cream oversized hoodie sleeve. Long silky hair with soft curtain bangs covering one eye, big expressive eyes with winged eyeliner, fluffy lashes, natural glowing skin, dusty pink lips, gentle pout, sweet and cute expression.

Hoodie slipping off one shoulder, visible collarbone. Warm indoor lighting, soft beige-gray blurred background, shallow depth of field, ultra-detailed eye focus, realistic hair texture, cozy aesthetic, authentic webcam selfie vibe, muted pastel tones, high realism, 9:16 portrait.
```

</details>

<a id="gpt-image-spotlight-museum-mural-portrait"></a>
### 暗色展厅里聚光灯下的日式壁画前女子肖像

<a href="https://x.com/oggii_0/status/2056647551470997670"><img src="../../previews/gpt-image-spotlight-museum-mural-portrait.jpg" width="360"></a>

开头先锁定参考照片的身份特征,再用单束斜向聚光灯、70度侧脸角度和前景暗影构图营造展厅氛围。相机、光线、氛围和负面提示分块书写,用Portra胶片色调保持写实质感。

GPT Image 2 · 上传图改图 · 出处: [@oggii_0 on X](https://x.com/oggii_0/status/2056647551470997670) · 672 赞，统计于 2026-10-29

[`spotlight`](tags.md#tag-spotlight) [`museum`](tags.md#tag-museum) [`film-grain`](tags.md#tag-film-grain) [`reference-photo`](tags.md#tag-reference-photo) [`low-light`](tags.md#tag-low-light)

<details><summary><b>提示词</b></summary>

```text
GPT Image 2 on
@itsPolloAI


Prompt: Use my reference photo to preserve the exact facial features, hairstyle, bangs, facial proportions, skin tone, body posture, and overall silhouette with high identity consistency.

Cinematic portrait of a woman standing alone inside a dark exhibition room. She wears a vintage white shirt layered with a soft pink outer jacket and a black vintage-textured skirt. Minimal makeup. Front-profile pose with her body facing the camera, relaxed posture, one shoulder slightly lowered, hands gently adjusting her hair. Calm, mysterious expression with an intellectual and elegant aura.

She is positioned in the lower center of the frame, surrounded by darkness. A single dramatic diagonal spotlight cuts across the scene from the upper right to the lower left, illuminating only half of her body while the rest fades into shadow. Behind her is a colorful vintage Japanese mural wall filled with retro cartoon illustrations and traditional artistic details.

Foreground shadows naturally frame the composition like torn darkness, creating a moody museum atmosphere with lonely artistic energy and a contemplative cinematic mood. Realistic photography with subtle film grain, analog texture, muted blacks, and vibrant mural accents.

Camera angle: eye-level shot, medium-close portrait framing, subject captured at approximately a 70-degree side profile angle, slight distance from the subject for environmental storytelling, centered cinematic composition.

Camera settings: cinematic low-light photography, shallow depth of field, realistic shadow falloff, Kodak Portra film color grading.

Lighting: harsh focused spotlight from the upper right creating a strong diagonal beam and deep high-contrast shadows, minimal ambient light, rich blacks, soft warm highlights along the face and glasses edges.

Vibe: mysterious, artistic, museum-core aesthetic, intelligent quiet energy, melancholic cinematic atmosphere, indie film still, luxury editorial photography, solitary nighttime mood, understated elegance.

Style: ultra-realistic cinematic photography, analog grain, editorial fashion portrait, natural skin texture, subtle imperfections, realistic color science, masterpiece quality.

Negative prompt: anime, smiling, overexposed lighting, extra limbs, bad anatomy, overly colorful outfit, cyberpunk neon, blurry face, low quality, distorted hands, unrealistic skin, HDR overload, exaggerated makeup, busy composition, duplicate person.
```

</details>

<a id="gpt-image-street-caricature-easel-art-market-portrait"></a>
### 女孩坐在画架旁，身边是她的街头漫画像

<a href="https://x.com/Emmma___0/status/2056061305640169643"><img src="../../previews/gpt-image-street-caricature-easel-art-market-portrait.jpg" width="360"></a>

提示词以上传的人像锁定身份，并要求漫画只夸张少数真实面部特征。长串负面词排除了默认的可爱Q版脸和吐舌表情，浅景深的集市背景让真人与画作都清晰可读。

GPT Image 2 · 上传图改图 · 出处: [@Emmma___0 on X](https://x.com/Emmma___0/status/2056061305640169643) · 538 赞，统计于 2026-10-28

[`caricature`](tags.md#tag-caricature) [`street-art`](tags.md#tag-street-art) [`easel`](tags.md#tag-easel) [`identity-reference`](tags.md#tag-identity-reference) [`lifestyle`](tags.md#tag-lifestyle)

<details><summary><b>提示词</b></summary>

```text
Use the uploaded portrait as the identity reference for the subject’s face, hairstyle, facial structure, and overall impression.

Create a high-quality lifestyle editorial portrait of the same person sitting outdoors beside a wooden easel displaying a colorful street-style caricature portrait of them.

The real person and the caricature must clearly resemble the same individual.

Scene:
- the person is seated on a simple wooden folding chair
- beside them is a wooden easel holding a large caricature drawing
- the setting is a sentimental urban art market
- include illustration booths, handmade craft stalls, sketch displays, posters, cozy creative shopfronts, and a few softly blurred pedestrians
- lively but not crowded
- bright soft daylight, warm natural tones, shallow depth of field
- realistic photography for the person and environment
- vertical composition showing both the person and the caricature clearly

Subject:
- preserve the uploaded person’s recognizable identity
- natural pose
- calm, relaxed, slightly amused expression
- stylish casual outfit that suits the subject
- clean editorial lifestyle photography
- do not force the same pose or expression for every subject

Caricature direction:
- the drawing on the easel must be a true observational street caricature, not a generic cute cartoon
- the caricature artist should exaggerate the subject’s actual most recognizable facial traits

- analyze the uploaded face and exaggerate only 2–4 distinctive features, such as eye shape, eyebrows, nose, lips, cheeks, jawline, chin, ears, hairstyle, or facial proportions
- each caricature should feel custom-made for that specific person
- avoid using the same default cute face for every person
- avoid generic big eyes plus tongue-out expression
- the caricature should be funny because it captures the person’s unique features, not because it uses a random silly pose

Caricature style:
- oversized head with smaller simplified body
- playful but recognizable facial proportions
- bold hand-drawn marker lines
- quick sketchy pen strokes
- colored pencil texture
- lively street-artist energy
- humorous but flattering
- witty, expressive, and personality-driven
- charming handmade imperfections
- colorful accent doodles may be added, but keep the focus on the face

Expression in the caricature:
- choose a natural funny expression that fits the person’s facial character
- possible expressions: raised eyebrow, shy smile, surprised eyes, confident smirk, awkward polite smile, exaggerated calm face, pouty lips, confused cute face, or gentle blank stare
- the expression should vary depending on the subject
- do not always use a tongue-out face
- do not always use the same wide-eyed cute expression

Caricature canvas:
- large vertical drawing board or canvas on a wooden easel
- the caricature should be clearly visible and occupy a major part of the image
- it should immediately read as a funny street caricature
- it should be more exaggerated than a portrait sketch
- it should not look like a realistic fashion illustration
- it should not look like a polished beauty drawing

Important:
- the caricature must be custom to the uploaded person
- preserve recognizable identity through the exaggerated features
- prioritize personality, likeness, and humor over generic cuteness
- make the caricature feel like a real street artist observed the person and drew a witty exaggerated version

Negative prompt:
- no generic cute chibi face
- no repeated default caricature face
- no tongue-out pose
- no identical silly expression for every subject
- no random anime expression
- no realistic portrait sketch
- no polished fashion illustration
- no beauty sketch
- no weak exaggeration
- no scary grotesque distortion
- no ugly horror exaggeration
- no distorted anatomy of the real person
- no extra fingers
- no badly drawn hands
- no messy crowded background
- no text
- no watermark
- no Eiffel Tower
- no famous landmarks.
```

</details>

<a id="nano-banana-satin-slip-dress-purple-sofa-portrait"></a>
### 金发女子穿白色缎面吊带裙坐在紫色沙发上

<a href="https://x.com/KeorUnreal/status/2065897085015064917"><img src="../../previews/nano-banana-satin-slip-dress-purple-sofa-portrait.jpg" width="360"></a>

结构化的 JSON 提示词把主体、服装、姿势、环境、光线和镜头拆分成带标签的字段，每个元素都可以单独修改。从地面高度的低机位，加上前景中带红底的高跟鞋，把画面重心推向双腿。

Nano Banana 2 · 文生图 · 出处: [@KeorUnreal on X](https://x.com/KeorUnreal/status/2065897085015064917) · 461 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`editorial-fashion`](tags.md#tag-editorial-fashion) [`structured-prompt`](tags.md#tag-structured-prompt) [`low-angle`](tags.md#tag-low-angle)

<details><summary><b>提示词</b></summary>

```text
"subject": {
    "Kate Upton lookalike",
    "build": "hourglass figure, large bust",
    "hair": {
      "color": "blonde",
      "length": "long, past shoulders, voluminous loose waves",
      "style": "side-parted, flowing over right shoulder and back",
      "texture": "shiny, silky, healthy"
    },
    "face": {
      "eyes": "sharp and seductive gaze",
      "lips": "full, glossy with deep red lipstick",
      "makeup": "flawless base, defined eyes with subtle eyeliner, contoured cheeks, glossy red lips",
      "glasses": "black frame glasses",
      "expression": "confident, seductive, slight head tilt, direct eye contact with viewer"
    },
    "skin": "smooth, glowing, with soft highlights on shoulders and legs"
  },
  "clothing_and_accessories": {
    "dress": "white satin/silk slip dress, thin gold chain straps, low sweetheart neckline, fitted bodice, short hem with high side slit revealing thigh, shiny reflective texture, small sign 'Keor' embroidered on border",
    "shoes": "white so kate Louboutin high heels with red sole, 12cm heel",
    "jewelry": "small gold hoop earrings, delicate gold chain necklace",
    "other": "subtle gold bracelet on left wrist"
  },
  "pose_and_action": {
    "overall_pose": "sitting on the edge of a large grey sofa, body angled slightly toward the camera, leaning back with weight on left arm",
    "legs": "right leg extended forward toward camera with foot in foreground, left leg bent with knee up, creating a strong, sensual leg focus",
    "hands": "right hand resting on the sofa behind her for support, left hand placed on the sofa cushion in front",
    "torso": "slightly twisted toward viewer, chest forward",
    "head": "turned toward camera with confident seductive expression"
  },
  "environment": {
    "setting": "luxurious modern living room at night",
    "furniture": "large purple velvet sectional sofa, dark wood coffee table with decorative vase containing red dried flowers",
    "background": "dark textured wall with large painting of Nami manga character in Francisco goya style, window with sheer white curtains allowing soft natural light",
    "floor": "dark patterned area rug with subtle texture",
    "decor": "minimalist elegant styling with soft ambient lighting"
  },
  "lighting": {
    "type": "soft cinematic mixed lighting — natural window light from the side combined with warm dramatic interior lighting",
    "quality": "high contrast with beautiful highlights on skin, satin dress, and hair, soft shadows that sculpt the body and legs",
    "mood": "sexy, sophisticated, intimate, high-fashion editorial"
  },
  "camera_and_composition": {
    "shot_type": "medium full-body shot with emphasis on legs and pose",
    "angle": "slightly low angle from floor level, making legs appear longer and more powerful",
    "framing": "subject centered with strong foreground focus on the red high heel and extended leg",
    "depth_of_field": "sharp focus on the woman and dress, softly blurred background",
    "aspect_ratio": "portrait orientation"
  },
  "style_and_quality": {
    "style": "photorealistic, hyper-detailed, commercial high-fashion photography",
    "aesthetic": "sexy confident woman in elegant red satin dress and red heels, luxurious intimate setting",
    "mood": "alluring, powerful, sensual, cinematic",
    "technical_quality": "8K resolution, extremely sharp details on fabric texture, skin, hair strands, and reflections on the patent leather shoes"
  },
```

</details>

<a id="nano-banana-chibi-twins-caricature-pairs"></a>
### 四位名人与皮克斯风格大头公仔合影

<a href="https://x.com/TechieBySA/status/2051378456982671545"><img src="../../previews/nano-banana-chibi-twins-caricature-pairs.jpg" width="360"></a>

将真人固定在右侧、卡通角色固定在左侧，身高约为真人的50至60%，并让真人单肘搭在角色头顶形成自然互动。服装一比一还原、浅灰无缝背景与左上方柔光让两者处于同一光影与空间中。

Nano Banana 2 · 上传图改图 · 出处: [@TechieBySA on X](https://x.com/TechieBySA/status/2051378456982671545) · 370 赞，统计于 2026-10-29

[`caricature`](tags.md#tag-caricature) [`bobblehead`](tags.md#tag-bobblehead) [`3d-render`](tags.md#tag-3d-render) [`celebrity`](tags.md#tag-celebrity)

<details><summary><b>提示词</b></summary>

```text
“Create a high-resolution, ultra-realistic studio composition in a 4:5 vertical aspect ratio, featuring a real person standing beside a stylized 3D caricature (bobblehead-style) version of the same individual. Use the provided reference image as the only source of identity. Strictly preserve the subject’s exact facial structure, proportions, skin tone, hairstyle, and all recognizable features. Do not alter or stylize the real face. Composition & Framing: Full-body vertical shot with a clean, centered layout. The real subject stands on the right, and the caricature stands on the left at approximately 50–60% of the real subject’s height. The real subject casually rests one elbow on the caricature’s oversized head, creating a natural, playful interaction. Real Subject (Photographic): Ultra-realistic rendering with natural skin texture and fine detail. Expression is warm, relaxed, and confident. Pose & Style (IMPORTANT): The subject stands in a slightly cool, stylish posture — relaxed stance with subtle asymmetry (one leg slightly forward or weight shifted), shoulders loose, not stiff. The hand resting on the caricature should feel effortless and natural. Clothing (Match Reference): Keep textures realistic and clearly visible. 3D Caricature (Stylized Version): Pixar/Disney-inspired 3D style with exaggerated proportions — large expressive head and smaller body. The height should be noticeably shorter, around the real subject's waist level. Facial features must remain recognizable but enhanced — larger eyes, softer forms, slightly amplified smile. Emotion & Body Movement (IMPORTANT): Expression is more playful and animated than the real subject Eyes brighter and more expressive, smile slightly exaggerated Body posture must NOT be stiff — use a natural, lively stance Add subtle movement according to the real subject's personality Pose should feel like a living, animated character, not a rigid figurine Clothing: Exact 1:1 stylized recreation of the real subject’s outfit with soft 3D textures. Lighting & Environment: Soft, diffused studio lighting from the upper-left, creating smooth highlights and gentle shadows. Clean light-gray gradient seamless background(lighter in the inner areas). Output Style: Ultra-clean, cinematic, high-detail render with strong contrast between realistic human and stylized 3D character. Both subjects grounded with soft natural shadows.”
```

</details>

<a id="nano-banana-cobalt-ring-fashion-editorial"></a>
### 铂金短发模特坐在天蓝色圆形拱洞中

<a href="https://x.com/Emmma___0/status/2109146295252459682"><img src="../../previews/nano-banana-cobalt-ring-fashion-editorial.jpg" width="360"></a>

提示词按场景、服装、姿势、光线、配色和摄影风格分成带标签的段落。指定85mm镜头、中画幅质感以及冷暖光对比，让高端时尚大片的质感保持统一。

Nano Banana 2.1 · 文生图 · 出处: [@Emmma___0 on X](https://x.com/Emmma___0/status/2109146295252459682) · 370 赞，统计于 2026-10-27

[`fashion-editorial`](tags.md#tag-fashion-editorial) [`architecture`](tags.md#tag-architecture) [`cobalt-blue`](tags.md#tag-cobalt-blue) [`studio-portrait`](tags.md#tag-studio-portrait) [`minimalist`](tags.md#tag-minimalist)

<details><summary><b>提示词</b></summary>

```text
Create an ultra-realistic, high-end fashion editorial photoshoot featuring a beautiful young adult woman with short, tousled platinum-blonde bob hair, delicate facial features, fair skin, natural rosy lips, light-colored eyes, and a calm, confident expression.

Scene and Environment: A futuristic minimalist architectural studio featuring a massive sculptural circular opening with thick, smooth, curved white walls. The interior of the circular structure is a rich cobalt-blue or vibrant cyan-blue, creating a striking contrast against the white architectural frame. Clean geometric shapes, curved surfaces, and a contemporary art-gallery aesthetic.

Outfit and Styling: The model wears a sophisticated, oversized black knit sweater or elegant black long-sleeved top paired with tailored black or ivory trousers. Minimal makeup, natural skin texture, understated accessories, and effortless luxury styling.

Pose and Composition: The model poses naturally within and around the giant circular opening. Create a series of artistic editorial poses: a close-up portrait leaning forward through the circular frame, a full-body seated pose inside the sculptural ring with one knee raised, and a standing or seated three-quarter portrait with one hand resting on the curved white surface. Relaxed hands, graceful posture, elongated silhouette, and direct eye contact with the camera.

Lighting: Soft natural daylight entering from one side, creating beautiful directional highlights on the platinum hair, subtle shadows across the face, realistic skin tones, and soft gradients on the white architectural surfaces. Cinematic interplay between cool blue ambient light and warm sunlight.

Color Palette: Vivid cobalt blue, turquoise, icy cyan, pure white, deep black, and platinum blonde. Clean, cool-toned color grading with balanced highlights and rich shadows.

Photography Style: Luxury fashion magazine editorial, contemporary avant-garde photography, minimalist Scandinavian design, architectural fashion campaign, medium-format camera aesthetics, 85mm portrait lens, subtle depth of field, precise focus on the eyes, realistic hair strands, detailed knit fabric, natural skin texture, sophisticated framing, and premium commercial photography quality.

Image Quality: Photorealistic, ultra-detailed, 8K appearance, professional art direction, anatomically accurate hands, realistic proportions, elegant negative space, clean architectural geometry, natural facial expression, crisp details, refined composition, no artificial-looking skin, no excessive retouching.

Vertical portrait composition, 2:3 aspect ratio.
```

</details>

<a id="nano-banana-seaside-wind-triptych-portrait"></a>
### 海风海鸥三联幅人像

<a href="https://x.com/rovvmut_/status/2028344848517062936"><img src="../../previews/nano-banana-seaside-wind-triptych-portrait.jpg" width="360"></a>

提示词先用上传照片锁定人物身份，再按景别逐幅定义：远景、侧面中景、特写。统一的场景、镜头、光线和调色说明让三幅画面保持一致。

Nano Banana 2 · 上传图改图 · 出处: [@rovvmut_ on X](https://x.com/rovvmut_/status/2028344848517062936) · 352 赞，统计于 2026-10-28

[`triptych`](tags.md#tag-triptych) [`identity-reference`](tags.md#tag-identity-reference) [`seaside`](tags.md#tag-seaside) [`cinematic-portrait`](tags.md#tag-cinematic-portrait) [`overcast-light`](tags.md#tag-overcast-light)

<details><summary><b>提示词</b></summary>

```text
Google Nano Banana 2 on Yapper

Prompt: Use the uploaded photo as the exact identity reference. Keep the same person, the same face, the same facial features, proportions, and natural expression.
Create a photorealistic cinematic triptych portrait, a three-frame composition combined into one image.
Scene: a windy seaside with a cold sea, overcast sky, flying seagulls, strong ocean wind, and a vivid, alive atmosphere.
Frame 1 (top): wide cinematic shot. The person stands by the sea, smiling naturally. Their hair is blowing in the wind. Seagulls are flying in the background.
Frame 2 (middle): medium shot from behind or from the side. The person is looking at the sea. Their coat and hair are moving in the wind. Seagulls fly nearby.
Frame 3 (bottom): close-up emotional portrait. Wind in the hair, natural skin texture, thoughtful gaze, cinematic mood.
Style: real photography, cinematic lifestyle portrait, documentary fashion photography.
Lighting: natural overcast daylight, soft shadows, cold seaside tones.
Camera: full-frame DSLR look, 85mm lens aesthetic, shallow depth of field.
Color grading: muted cinematic colors, cool palette, film-like mood.
Ultra photorealistic, natural skin texture, real moment. No illustration, no CGI. No text, no logos, no watermark.
```

</details>

<a id="gpt-image-dusk-film-portrait"></a>
### 黄昏低角度闪光灯胶片颗粒人像

<a href="https://x.com/chatgptpaglu/status/2105219509791678731"><img src="../../previews/gpt-image-dusk-film-portrait.jpg" width="360"></a>

正面直闪配合深蓝色黄昏天空，把人物从暗背景中提亮，低机位加上剪影树枝带来随手抓拍的感觉。明确写出衣服上的文字，模型就能把图案字样清晰渲染出来。

GPT Image 2.5 · 文生图 · 出处: [@chatgptpaglu on X](https://x.com/chatgptpaglu/status/2105219509791678731) · 318 赞，统计于 2026-10-27

[`portrait`](tags.md#tag-portrait) [`film-grain`](tags.md#tag-film-grain) [`golden-hour`](tags.md#tag-golden-hour)

<details><summary><b>提示词</b></summary>

```text
A low-angle, close-up photograph capturing a young woman with wavy brown hair outdoors at dusk. She is wearing a grey cropped t-shirt with a blue and white graphic text that reads 'DESTINED' above 'SET 1958' and black denim bottoms. Her head is tilted, and she is looking directly into the camera lens. The dark blue evening sky serves as the background, with silhouetted tree branches visible at the bottom of the frame. Strong flash lighting is directed from the front, illuminating her face and highlighting strands of her hair. The composition has a grainy film photography aesthetic.
```

</details>

<a id="nano-banana-night-flash-hair-tying-stone-steps"></a>
### 石阶上扎头发的夜间闪光抓拍

<a href="https://x.com/MahiraEhan/status/2107702956258685009"><img src="../../previews/nano-banana-night-flash-hair-tying-stone-steps.jpg" width="360"></a>

手机直闪在深色石阶上迅速衰减，加上扎发瞬间的抓拍姿势，让画面像真实的随手快照。提示词把姿势、头发、妆容、服装和相机分段写清，最后列出要避免的效果，让肤质和光线不会变成精修的影棚感。

Nano Banana 2.1 · 上传图改图 · 出处: [@MahiraEhan on X](https://x.com/MahiraEhan/status/2107702956258685009) · 296 赞，统计于 2026-10-28

[`candid`](tags.md#tag-candid) [`flash-photography`](tags.md#tag-flash-photography) [`iphone-style`](tags.md#tag-iphone-style) [`night`](tags.md#tag-night) [`portrait`](tags.md#tag-portrait)

<details><summary><b>提示词</b></summary>

```text
A spontaneous evening shot, a candid moment caught in motion. Taken on an iPhone 17 Pro with flash. The frame should look like a real photo from a personal gallery, not a staged fashion shoot.

POSE: The girl is sitting directly on wide, light-colored stone steps, with her torso slightly turned into a 3/4 angle. One leg is bent closer to her body, while the other rests on the step below.

At the moment of capture, the girl raises both hands to quickly tie her hair into a high, messy ponytail. Her elbows are positioned on opposite sides of her head, with her hands still in motion. Her head is slightly turned to the side, and her gaze is directed past the camera. Her lips are relaxed and slightly parted.

The frame is captured in the exact in-between second — her hair is not fully tied yet, part of it is still held in her hands, and several strands are flying freely near her face. Subtle directional motion blur on the hands, hair ends, and edges of the clothing. Do not blur or deform the facial features; the face must remain clear, recognizable, and true to the original.

HAIR: Very long, thick hair. Most of the hair is being lifted upward and backward by her hands, while the lower section still falls freely over her shoulders and back. A few thin strands have come loose around the temples and cheeks. Do not let them cover the eyes, nose, or lips.

MAKEUP: Expressive modern evening makeup. A thin, elongated black winged eyeliner, voluminous lashes with a fox-eye effect, laminated brows. The lips are outlined with a cool brownish-pink pencil slightly darker than the natural lip tone, with a translucent berry-nude gloss inside. Skin is slightly tanned, fresh, with visible real pores and natural micro-texture.

CLOTHING: A fitted white top with a wide boat neckline, revealing the collarbones and one shoulder. Long sleeves partially cover the hands. Bottoms: loose black low-rise trousers with soft folds.

ACCESSORIES: Large silver hoop earrings, one chunky silver ring. Manicure: short square nails, in a shade matching the top.

ENVIRONMENT: A wide outdoor stone staircase at night. Light-colored natural stone occupies almost the entire background and creates graphic horizontal lines. No restaurants, cars, signs, flowers, or decorative objects. The upper part of the frame gradually falls into darkness.

FLASH PHOTOGRAPHY: Deep night. The only main light source is the direct built-in iPhone flash. It sharply illuminates the face, collarbones, raised hands, top, and nearest steps.

The light falls off quickly into the depth of the staircase. Distant steps fade into gray-black shadow. No soft studio lighting and no evenly illuminated scene.

CAMERA: iPhone 17 Pro, vertical 9:16 format. Medium-close framing, approximately from mid-thighs to the space slightly above the raised hands. The camera is close, positioned slightly above and to the side, as if someone standing nearby suddenly raised their phone and pressed the shutter while the girl was tying her hair.

The girl is not perfectly centered. One elbow is close to the upper edge of the frame, and part of the jacket is naturally cropped at the bottom. Handheld, slightly imperfect framing.

Natural skin, realistic texture of hair, knit fabric, trousers, and stone. Slight digital noise, visible fine film grain, muted nighttime color rendering, deep shadows, subtle vignette, RAW unedited feeling.

Do not use 8K, ultra sharp, HDR, beauty filters, airbrushing, plastic skin, artificial bokeh, studio lighting, perfect symmetry, or a glossy AI look.
```

</details>

<a id="nano-banana-yellow-beaded-halter-wet-hair-portrait"></a>
### 黄色串珠挂颈上衣与湿发妆造人像

<a href="https://x.com/KeorUnreal/status/2113259619443159550"><img src="../../previews/nano-banana-yellow-beaded-halter-wet-hair-portrait.jpg" width="360"></a>

低机位加上头部微仰，让胸口和领口成为视觉重心；提示词逐一列出面料与装饰（透明网纱、丝绒上身、水晶刺绣、金属流苏），使模型能分别呈现这些材质。柔和的顶光与素净灰墙让注意力集中在纹理上。

Nano Banana 2.1 · 文生图 · 出处: [@KeorUnreal on X](https://x.com/KeorUnreal/status/2113259619443159550) · 290 赞，统计于 2026-10-29

[`fashion-portrait`](tags.md#tag-fashion-portrait) [`low-angle`](tags.md#tag-low-angle) [`beadwork`](tags.md#tag-beadwork) [`soft-lighting`](tags.md#tag-soft-lighting)

<details><summary><b>提示词</b></summary>

```text
Low-angle chest-up fashion portrait of a young american woman Emilia clarke Head tilted slightly back, half-lidded eyes looking down into the camera, lips slightly parted. Blonde hair in a messy low bun with thin damp strands framing the face and neck. Dewy wet-look makeup: luminous skin sheen on shoulders and collarbones, soft dark liner, glossy peach-pink lips. Neon yelloe halter high-collar piece with bronze beadwork on the collar, a sheer neon yelloe mesh panel edged with beads, and a velvet-like bodice covered in symmetrical gold-silver crystal floral embroidery with fine metallic fringe opened on a deep neckline. Multiple small silver hoop and stud earrings. Soft overhead light, neutral out-of-focus light-gray interior wall with a horizontal architectural line. High-fashion damp glam, sharp embroidery detail, no harsh flash.
```

</details>

<a id="gpt-image-black-blazer-editorial-portrait-reference"></a>
### 黑色超大西装的半身时尚人像

<a href="https://x.com/MissDelulu9/status/2078741062714356031"><img src="../../previews/gpt-image-black-blazer-editorial-portrait-reference.jpg" width="360"></a>

开头先锁定参考图的面部与身份，再依次交代构图、姿态、服装和妆容。指定相机镜头，用白墙加侧向柔光，结尾列出排除项，保证皮肤真实、五官不变。

GPT Image 2 · 上传图改图 · 出处: [@MissDelulu9 on X](https://x.com/MissDelulu9/status/2078741062714356031) · 282 赞，统计于 2026-10-29

[`editorial`](tags.md#tag-editorial) [`portrait`](tags.md#tag-portrait) [`black-blazer`](tags.md#tag-black-blazer) [`reference-image`](tags.md#tag-reference-image) [`fashion`](tags.md#tag-fashion)

<details><summary><b>提示词</b></summary>

```text
Use the girl from the reference image and preserve her face, identity, proportions, and overall appearance exactly. Ultra-realistic 9:16 chest-up editorial portrait. She sits with a slight head tilt, looking directly at the camera with a calm, confident expression. Long straight glossy hair with a clean center part.

Wearing a structured oversized black blazer with broad shoulders. Natural luxury makeup with luminous skin, soft brown eyeshadow, subtle eyeliner, defined lashes, and nude glossy lips. Clean white minimalist background with soft side sunlight creating elegant shadows. Shot on a Sony A7R IV, 85mm f/1.4, shallow depth of field, cinematic lighting, realistic skin texture, 8K RAW, premium fashion editorial, no facial changes, no distortion, no plastic skin, no text, logo, or watermark.
```

</details>

<a id="nano-banana-neon-yellow-dress-velvet-armchair"></a>
### 霓虹黄缎面迷你裙女子坐于天鹅绒扶手椅

<a href="https://x.com/KeorUnreal/status/2109984717160276438"><img src="../../previews/nano-banana-neon-yellow-dress-velvet-armchair.jpg" width="360"></a>

采用结构化 JSON 提示，将主体、服装、场景、光线和镜头分别写入独立字段，并精确指定领口与裙摆处的刺绣文字 Keor，输出中可见该文字。明确的三四分之三镜头角度与高细节时尚摄影风格，使画面保持真实的人像质感。

Nano Banana 2.1 · 文生图 · 出处: [@KeorUnreal on X](https://x.com/KeorUnreal/status/2109984717160276438) · 275 赞，统计于 2026-10-29

[`json-prompt`](tags.md#tag-json-prompt) [`fashion`](tags.md#tag-fashion) [`text-in-image`](tags.md#tag-text-in-image) [`portrait`](tags.md#tag-portrait)

<details><summary><b>提示词</b></summary>

```text
{
  "subject": {
    "description": "Young woman with fair skin, short black bob haircut with a center part, refined facial features, looking toward the camera with a calm expression",
    "hair": "Short black bob, sleek and straight with a clean center part",
    "body": "Slender yet curvy figure, small tattoos visible on both arms",
    "pose": "Seated in a velvet armchair, one leg extended forward, one hand holding a clutch, the other resting on her thigh near the dress hem",
    "expression": "Direct, slightly parted-lip gaze"
  },
  "outfit": {
    "dress": "Neon yellow satin mini dress with thin spaghetti straps, ruched sides, and a short fitted silhouette",
    "accessories": "Black choker with a small bow, dangling red earrings",
    "nails": "Neon yellow painted fingernails",
    "prop": "Black textured clutch held in one hand",
    "text": "The word 'Keor' written in small lettering along the border of the outfit (on the neckline or hem of the dress)"
  },
  "setting": {
    "location": "Elegant indoor room",
    "background": "Beige velvet armchair, wood-paneled walls, curtains, dark flooring, doorway in the distance"
  },
  "lighting": {
    "type": "Warm soft indoor lighting",
    "effects": "Gentle highlights on the neon yellow satin and skin, soft shadows in the room"
  },
  "camera": {
    "angle": "Slightly high three-quarter angle looking down at the seated subject",
    "framing": "Three-quarter body shot, subject centered in the armchair",
    "style": "Photorealistic, high-detail fashion photography, sharp focus"
  },
  "additional_details": {
    "skin": "Smooth with a natural sheen",
    "atmosphere": "Stylish indoor portrait with a bold neon yellow look"
  }
}
https://
x.com/mr_perfect1117
/mr_perfect1117/status/2108407417373692016
…
```

</details>

<a id="nano-banana-overhead-snow-portrait-school-uniform"></a>
### 身穿校服躺在雪地里的俯拍人像

<a href="https://x.com/VibeEverything/status/2113256906294796645"><img src="../../previews/nano-banana-overhead-snow-portrait-school-uniform.jpg" width="360"></a>

用 JSON 结构把人物身份锁定在参考图上，再把机位、镜头、对焦、姿势、服装和光线分字段写清。阴天柔光、雪花细节和防止改脸的负面提示共同保住了相貌和清冷氛围。

Nano Banana 2.1 · 上传图改图 · 出处: [@VibeEverything on X](https://x.com/VibeEverything/status/2113256906294796645) · 275 赞，统计于 2026-10-28

[`portrait`](tags.md#tag-portrait) [`snow`](tags.md#tag-snow) [`school-uniform`](tags.md#tag-school-uniform) [`overhead`](tags.md#tag-overhead) [`json-prompt`](tags.md#tag-json-prompt)

<details><summary><b>提示词</b></summary>

```text
{
  "reference_image": {
    "identity_preservation": "STRICT — The person's identity from the reference image must be preserved exactly. Keep facial structure, face shape, eye shape, nose, lips, skin tone, freckles/skin texture, and overall likeness identical. Do not alter, beautify, age, or stylize the face.",
    "use_reference_for": ["face", "hairstyle", "overall likeness"]
  },
  "image_type": "photorealistic portrait photograph",
  "aspect_ratio": "2:3 (vertical)",
  "camera": {
    "angle": "top-down overhead shot, camera directly above the subject",
    "framing": "close-up to medium close-up, head to upper chest",
    "lens": "85mm portrait lens look",
    "depth_of_field": "shallow, face in sharp focus",
    "focus": "eyes"
  },
  "subject": {
    "pose": "lying on her back in fresh snow, head slightly tilted, relaxed and calm",
    "gaze": "looking directly into the camera lens, eye contact with the viewer",
    "expression": "calm, dreamy, slightly melancholic, lips gently closed",
    "hair": {
      "color": "black",
      "length": "long",
      "style": "loose, fanned out across the snow, a few strands across the face, snowflakes caught in the hair"
    },
    "accessories": [
      "round tortoiseshell-frame glasses",
      "white wired earphones in both ears, cable running down over the chest"
    ],
    "makeup": "natural, minimal, soft coral lips"
  },
  "outfit": {
    "outerwear": "charcoal school uniform blazer with notched lapels, matte wool texture",
    "shirt": "white collared dress shirt",
    "tie": "navy striped tie with light blue and white diagonal stripes",
    "details": "snowflakes resting on the blazer shoulders and lapels"
  },
  "environment": {
    "setting": "outdoors, lying in a bed of fresh powdery snow",
    "weather": "light snowfall, individual snowflakes visible in the frame",
    "background": "white snow surface filling the background"
  },
  "lighting": {
    "type": "soft diffused natural daylight, overcast",
    "quality": "even, gentle, no harsh shadows",
    "skin_rendering": "natural skin texture, subtle cool tones on skin"
  },
  "color_palette": ["snow white", "charcoal gray", "navy", "black", "warm tortoiseshell brown", "soft coral"],
  "mood": "quiet, cold, cinematic winter, introspective",
  "style": "high-end editorial photography, film-like, realistic detail",
  "negative_prompt": "face alteration, identity change, distorted features, extra fingers, plastic skin, over-smoothing, cartoon, anime, heavy makeup, harsh flash, blurry eyes, looking away from camera"
}
```

</details>

<a id="gpt-image-golden-light-sunglasses-triptych-portrait"></a>
### 金色光线墨镜三联时尚人像

<a href="https://x.com/noorlewisx/status/2065652906209284292"><img src="../../previews/gpt-image-golden-light-sunglasses-triptych-portrait.jpg" width="360"></a>

把 9:16 画面分成三格，每格指定不同景别：中近景、眼部极致微距、特写。人脸参考的严格一致性指令，加上暖色百叶窗光线、镜头光圈参数和负面清单，让三格风格保持统一。

GPT Image 2 · 上传图改图 · 出处: [@noorlewisx on X](https://x.com/noorlewisx/status/2065652906209284292) · 271 赞，统计于 2026-10-28

[`triptych`](tags.md#tag-triptych) [`fashion-editorial`](tags.md#tag-fashion-editorial) [`golden-light`](tags.md#tag-golden-light) [`face-reference`](tags.md#tag-face-reference) [`macro-eye`](tags.md#tag-macro-eye)

<details><summary><b>提示词</b></summary>

```text
Use the uploaded face reference as a strict identity guide and preserve exact facial features, proportions, skin tone, eye shape, nose, lips, jawline, and overall recognizable identity with very high accuracy. Create an ultra-realistic cinematic high-end fashion editorial vertical triptych portrait in 9:16 format divided into three horizontal panels featuring a young Asian woman with elegant feminine beauty, soft natural styling, luxury aesthetic, silver hoop earring, minimal jewelry, and softly voluminous dark ash-brown wavy hair. Panel 1: medium close-up three-quarter portrait wearing black sunglasses, hand near lips, calm introspective expression, warm golden sunlight through window blinds casting striped shadows, cinematic mood. Panel 2: extreme macro close-up of one eye with sunglasses lowered in foreground, highly detailed iris, lashes, moist reflections, cinematic depth, emotional intimate feel. Panel 3: close-up without sunglasses, head turned toward light, hand behind neck, relaxed lips, soft distant gaze, subtle emotional tension. Outfit: smoky taupe or muted beige tailored silk-viscose blouse, minimal elegant luxury fashion styling, realistic fabric texture. Lighting: warm golden cinematic sunlight, soft indoor blinds shadows, luxury editorial lighting, soft contrast, glowing skin highlights. Camera: DSLR ultra-realism, 85mm lens, f/1.4 shallow depth of field, sharp facial detail, natural skin texture, 8K quality. Color grading: warm golden tones, soft amber highlights, cinematic contrast, filmic glow, luxury finish. Negative: no anime, no CGI, no plastic skin, no over-smoothing, no face change, no distortion, no watermark, no text, no logo.
```

</details>

<a id="gpt-image-sunny-park-bench-hoodie-portrait"></a>
### 公园长椅上穿灰色卫衣的女子

<a href="https://x.com/noorlewisx/status/2083775433485754565"><img src="../../previews/gpt-image-sunny-park-bench-hoodie-portrait.jpg" width="360"></a>

依次写清人物、穿搭和姿势，再加上85mm与f/1.8等镜头参数，以及透过树叶的阳光，营造柔和的焦外虚化。参考图一行用来保持面部一致。

GPT Image 2 · 上传图改图 · 出处: [@noorlewisx on X](https://x.com/noorlewisx/status/2083775433485754565) · 267 赞，统计于 2026-10-29

[`park`](tags.md#tag-park) [`bench`](tags.md#tag-bench) [`lifestyle`](tags.md#tag-lifestyle) [`bokeh`](tags.md#tag-bokeh) [`face-reference`](tags.md#tag-face-reference)

<details><summary><b>提示词</b></summary>

```text
A stunning young woman sitting casually on a wooden park bench in a lush green city park during a bright sunny afternoon, wearing a light gray oversized hoodie and matching sweatpants, clean white sneakers, messy high bun hairstyle with soft face-framing strands, natural makeup, warm gentle smile, looking directly at the camera, one hand touching her hair, relaxed and confident pose with one leg folded on the bench, cinematic lifestyle photography, vibrant flowers, tall green trees, soft sunlight filtering through leaves, shallow depth of field, creamy bokeh, ultra realistic skin texture, high-end fashion editorial, DSLR photography, 85mm lens, f/1.8, natural lighting, HDR, ultra-detailed, photorealistic, 8K, premium quality.
Same Face as reference image.
Camera Angle.Walk-behind shot.
```

</details>

<a id="nano-banana-denim-bob-beauty-contact-sheet"></a>
### 九宫格美妆写真 牛仔外套与黑框眼镜

<a href="https://x.com/kingofdairyque/status/2066122884859207815"><img src="../../previews/nano-banana-denim-bob-beauty-contact-sheet.jpg" width="360"></a>

编号的姿势描述为九个画面各自给出可核对的指令，共用的妆造段落保证整组一致。每格都重复同一人物、短发和牛仔外套，使其读起来像一张完整的接触表。

Nano Banana 2 · 文生图 · 出处: [@kingofdairyque on X](https://x.com/kingofdairyque/status/2066122884859207815) · 250 赞，统计于 2026-10-29

[`beauty`](tags.md#tag-beauty) [`contact-sheet`](tags.md#tag-contact-sheet) [`grid`](tags.md#tag-grid) [`portrait`](tags.md#tag-portrait)

<details><summary><b>提示词</b></summary>

```text
Ultra-realistic 3x3 beauty contact sheet featuring the same stunning woman in nine different poses and expressions, arranged in a clean square grid with thin black borders separating each frame. Professional studio portrait photography against a seamless light gray backdrop, editorial model test shoot aesthetic, modern beauty campaign, high-fashion contact sheet.

Poses & Expressions
1. Looking directly at the camera while holding black rectangular glasses near her lips, seductive expression, slightly parted glossy lips.

2. Winking with mouth open and tongue slightly out, playfully holding the glasses.

3. Three-quarter profile pose with tongue slightly out and a playful smirk.

4. Head tilted back, eyes closed, soft dreamy expression.

5. Side profile with chin raised, eyes closed, elegant editorial pose.

6. Over-the-shoulder pose with hair partially covering one eye, sultry direct gaze.

7. Facing forward, hands lifting hair on both sides, confident beauty campaign pose.

8. Relaxed direct gaze with black rectangular glasses resting on top of the head, soft smile.

9. Looking over black rectangular glasses worn low on the nose, seductive expression with slightly parted lips.

Face & Makeup
Soft ultra-feminine glam makeup with flawless radiant fair skin and warm pink undertones, smooth pore-visible skin texture, luminous satin-dewy finish, softly sculpted oval face with subtle contour and diffused bronzer. Strong blush-focused makeup with rosy pink blush heavily applied across the cheeks and lightly across the bridge of the nose for a youthful, doll-like flushed effect. Brightened under-eyes with soft matte highlights and a softly blurred complexion.
Large almond-shaped eyes enhanced with soft Korean-inspired glam makeup: beige-pink eyeshadow blended seamlessly with subtle brown depth on the outer corners, bright ivory shimmer on the inner corners and aegyosal highlights for wider, innocent-looking eyes. Long, thick, wispy curled lashes with a separated manga-like lash effect, softly defined eyeliner with lifted outer corners, fluffy natural dark brows with a softly straight arch.
Full, plump lips with an overlined soft cupid's bow, glossy reddish-pink gradient lips, glass-like shine, and hydrated juicy texture. Overall makeup aesthetic: clean girl glam mixed with soft baddie beauty, ultra-polished yet airy and feminine, doll-like elegance, luxury influencer makeup.

Hair
Short, sleek, straight bob haircut with a center part, smooth and glossy finish.

Outfit & Accessories
White lace balconette bra with delicate floral texture and thin straps, oversized medium-wash blue denim jacket worn off the shoulders, casual Y2K-inspired styling, small gold hoop earrings, black rectangular glasses used as a prop in several frames.

Photography
Professional studio beauty photography, soft diffused key light with subtle beauty dish lighting, editorial campaign quality, realistic skin texture, extremely detailed eyes and lips, fashion magazine contact sheet, luxury beauty advertisement, Vogue editorial aesthetic, ultra-realistic, high detail, 8K, sharp focus, premium retouching, photorealistic.
```

</details>

<a id="gpt-image-monochrome-red-streetwear-bean-bag-portrait"></a>
### 全红街头装男士坐在红色懒人沙发上

<a href="https://x.com/Xaroon_x/status/2076616202793939072"><img src="../../previews/gpt-image-monochrome-red-streetwear-bean-bag-portrait.jpg" width="360"></a>

服装、懒人沙发和背景统一为同一种红色，画面形成整块单色。逐件点名服装，用广告大片风格和戏剧化影棚光定调，并明确要求保持上传人脸不变以锁定身份。

GPT Image 2 · 上传图改图 · 出处: [@Xaroon_x on X](https://x.com/Xaroon_x/status/2076616202793939072) · 248 赞，统计于 2026-10-28

[`monochrome`](tags.md#tag-monochrome) [`streetwear`](tags.md#tag-streetwear) [`fashion-editorial`](tags.md#tag-fashion-editorial) [`studio-lighting`](tags.md#tag-studio-lighting) [`face-preservation`](tags.md#tag-face-preservation)

<details><summary><b>提示词</b></summary>

```text
Hyper-realistic cinematic fashion photoshoot of the uploaded person. Seated on a deep light red bean bag, he wears bold all-red oversized streetwear: trench coat, wide red pants, chunky sneakers, silver watch. Solid red background,. Powerful drip vibes, Adidas campaign editorial look, dramatic studio lighting. Keep my face exactly the same as the uploaded photo. Do not change or edit my face. --ar 4:5 ratio
```

</details>

<a id="nano-banana-half-face-name-portrait"></a>
### 半张脸肖像，名字字母透出另一半

<a href="https://x.com/Emmma___0/status/2108777847800426542"><img src="../../previews/nano-banana-half-face-name-portrait.jpg" width="360"></a>

提示词保留半张脸，在另一侧竖排名字，每个字母镂空透出被遮住那半张脸的对应部分，整张脸依然连贯。填入名字、背景和光线即可。

Nano Banana 2.1 · 上传图改图 · 出处: [@Emmma___0 on X](https://x.com/Emmma___0/status/2108777847800426542) · 244 赞，统计于 2026-10-27

[`typography`](tags.md#tag-typography) [`studio`](tags.md#tag-studio) [`template`](tags.md#tag-template)

<details><summary><b>提示词</b></summary>

```text
Transform the uploaded image into a modern studio portrait. Preserve the subject’s identity and features. Show half the face on the left; stack [NAME] vertically on the right, with each letter filled by matching details from the hidden half. Seamless alignment, [BACKGROUND] backdrop, [LIGHTING], modern typography.
```

</details>

<a id="gpt-image-candid-park-portrait-olive-cardigan-burgundy-bag"></a>
### 公园阳光下身穿橄榄绿开衫的抓拍人像

<a href="https://x.com/Aqsahere_/status/2095351414524608662"><img src="../../previews/gpt-image-candid-park-portrait-olive-cardigan-burgundy-bag.jpg" width="360"></a>

提示词按单品逐一写明颜色和面料，再分段交代姿势、场景和光线方向。结尾用手机摄影、胶片颗粒、镜头光晕和 4:5 竖构图等关键词，做出自然抓拍、不过度修饰的质感。

GPT Image 2 · 文生图 · 出处: [@Aqsahere_ on X](https://x.com/Aqsahere_/status/2095351414524608662) · 233 赞，统计于 2026-10-28

[`candid-portrait`](tags.md#tag-candid-portrait) [`smartphone-photography`](tags.md#tag-smartphone-photography) [`sunlight`](tags.md#tag-sunlight) [`film-grain`](tags.md#tag-film-grain) [`fashion`](tags.md#tag-fashion)

<details><summary><b>提示词</b></summary>

```text
A photorealistic candid outdoor portrait of a young woman standing in a peaceful urban park on a sunny afternoon. She has long dark-brown hair styled in a loose low ponytail, with wispy face-framing strands gently falling across her face. She gazes softly toward the side with a calm, thoughtful expression.
She wears an olive-green cardigan over a delicate white textured ruffle camisole, paired with a long dark-green skirt. A deep burgundy-red shoulder bag hangs naturally at her side. One hand rests gently near her neck while the other is relaxed in front of her.
She stands beside a paved walkway surrounded by green grass, mature leafy trees, and subtle urban buildings in the background. Strong sunlight filters through the trees, creating beautiful highlights in her hair, soft shadows, and a subtle lens flare in the upper corner.
Natural smartphone photography, candid lifestyle aesthetic, warm sunlight, realistic skin texture, detailed hair strands, authentic fabric textures, soft atmospheric contrast, gentle vintage film grain, muted earthy color palette, shallow depth of field, cinematic natural lighting, peaceful summer mood, highly photorealistic, vertical 4:5 composition.
```

</details>

<a id="gpt-image-golden-hour-newsstand-editorial-portrait"></a>
### 报刊亭前折叠椅上的金发女孩

<a href="https://x.com/SadiaMalik182/status/2081611030019572178"><img src="../../previews/gpt-image-golden-hour-newsstand-editorial-portrait.jpg" width="360"></a>

用结构化 JSON 把风格、相机、场景、人物、服装、姿势和光线拆成独立模块，每个要素都可单独控制。真实的相机镜头参数加柯达 Portra 调色，让黄金时刻的杂志感更稳定。

GPT Image 2 · 文生图 · 出处: [@SadiaMalik182 on X](https://x.com/SadiaMalik182/status/2081611030019572178) · 227 赞，统计于 2026-10-28

[`json-prompt`](tags.md#tag-json-prompt) [`street-fashion`](tags.md#tag-street-fashion) [`golden-hour`](tags.md#tag-golden-hour) [`editorial`](tags.md#tag-editorial) [`newsstand`](tags.md#tag-newsstand)

<details><summary><b>提示词</b></summary>

```text
"category": "Luxury Street Fashion Editorial Portrait",
  "style": {
    "genre": "Editorial Lifestyle Photography",
    "aesthetic": "Vintage Newsstand × Vogue Editorial × European Street Style × Pinterest Aesthetic × Gen-Z Fashion",
    "quality": "Ultra Photorealistic",
    "resolution": "4096×2304 (4K UHD)",
    "aspect_ratio": "16:9",
    "render_engine": "Octane Render / Unreal Engine 5 / Redshift",
    "editorial_reference": [
      "Vogue",
      "Zara",
      "Urban Outfitters",
      "Free People",
      "COS",
      "Pinterest Editorial"
    ],
    "mood": [
      "Golden Hour",
      "Warm",
      "Relaxed",
      "Vintage",
      "Editorial",
      "Natural",
      "Authentic"
    ]
  },
  "camera": {
    "camera": "Sony A7R V",
    "lens": "85mm f/1.4 GM",
    "orientation": "Landscape",
    "angle": "Eye Level",
    "aperture": "f/2.0",
    "iso": 100,
    "shutter_speed": "1/640s",
    "focus": "Eyes",
    "depth_of_field": "Cinematic Shallow",
    "sharpness": "Ultra Detailed"
  },
  "location": {
    "type": "Vintage Outdoor Newspaper & Magazine Stand",
    "environment": {
      "newsstand": true,
      "magazine_display": true,
      "newspaper_stacks": true,
      "bookstall": true,
      "city_sidewalk": true,
      "urban_news_kiosk": true,
      "authentic_street_environment": true
    }
  },
  "subject": {
    "gender": "Female",
    "age": "Early 20s",
    "appearance": {
      "skin": "Natural Fair Skin",
      "expression": "Calm Editorial Expression",
      "eye_contact": "Direct Camera",
      "makeup": {
        "style": "Natural Minimal",
        "skin_finish": "Soft Matte Glow",
        "lips": "Natural Nude",
        "eyes": "Soft Brown"
      }
    },
    "hair": {
      "style": "Messy Blonde Bun or Short Wavy Blonde Hair",
      "movement": "Light Breeze"
    }
  },
  "wardrobe": {
    "top": {
      "type": "Oversized White Graphic Sweatshirt",
      "fabric": "Premium Cotton",
      "fit": "Relaxed Oversized"
    },
    "bottom": {
      "type": "Red Athletic Shorts"
    },
    "socks": "White Ribbed Crew Socks",
    "shoes": "Black Chunky Sneakers"
  },
  "pose": {
    "position": "Relaxed Sitting On Folding Chair",
    "body_angle": "Three Quarter",
    "editorial": true
  },
  "lighting": {
    "time": "Golden Hour",
    "key_light": "Warm Natural Sunlight",
    "rim_light": "Golden Rim Light",
    "cinematic": true
  },
  "post_processing": {
    "hdr": true,
    "ray_tracing": true,
    "global_illumination": true,
    "clarity": "Ultra",
    "color_grading": "Kodak Portra 400",
    "film_grain": "Subtle"
  },
  "negative_prompt": [
    "low quality",
    "blur",
    "noise",
    "bad anatomy",
    "extra fingers",
    "duplicate person",
    "watermark",
    "logo",
    "text artifacts",
    "CGI look",
    "cartoon",
    "anime"
  ]
}
```

</details>

<a id="gpt-image-selfie-chibi-painting-cheek-brush"></a>
### 自拍中画布上的Q版自己为他涂脸颊

<a href="https://x.com/AiWithTariq/status/2098783770513948875"><img src="../../previews/gpt-image-selfie-chibi-painting-cheek-brush.jpg" width="360"></a>

提示词按头发、面部、服装、概念、画布角色、背景、风格和镜头分块标注,让真人自拍与3D Q版角色同框。两个角色重复使用同一组泼墨颜色,把现实与画中世界连在一起。

GPT Image 2.5 · 上传图改图 · 出处: [@AiWithTariq on X](https://x.com/AiWithTariq/status/2098783770513948875) · 219 赞，统计于 2026-10-28

[`selfie`](tags.md#tag-selfie) [`chibi`](tags.md#tag-chibi) [`paint-splatter`](tags.md#tag-paint-splatter) [`fourth-wall`](tags.md#tag-fourth-wall) [`art-studio`](tags.md#tag-art-studio)

<details><summary><b>提示词</b></summary>

```text
Study the uploaded photo's facial features and use them as inspiration to create a fun selfie-style photo of a similar-looking young man with a creative cartoon canvas twist.
Hair: Messy, tousled dark hair with paint splatters scattered across the hair and face, light stubble beard.
Face/Skin: Face and skin splattered with colorful paint speckles (purple, orange, blue), big laughing open-mouth smile, playful joyful expression, no jewelry, no tattoos.
Outfit: Purple/lavender knit sweater, paint-splattered casual look.
Concept: Taking a close-up selfie next to an easel canvas, where a cute chibi cartoon version of himself is painted on the canvas — the illustrated cartoon character reaching out of the canvas holding a paintbrush and playfully painting/touching the real man's cheek with colorful paint, breaking the fourth wall between reality and illustration.
Chibi cartoon (on canvas): Same messy hair and paint splatters, big expressive cartoon eyes, cheerful smile, wearing a purple off-shoulder top, leaning out of the canvas frame with one arm extended holding the paintbrush.
Background: Cozy art studio setting, softly blurred art supplies, paint bottles, and shelves in the background, warm natural lighting, wooden easel with visible paint-splattered edges.
Art style: Photorealistic selfie photography blended with vibrant 3D chibi cartoon illustration, playful colorful paint-splatter texture throughout, high detail, fun energetic composition.
Camera angle: Close-up selfie angle, slightly wide shot capturing both the real face and the canvas painting.
Text overlay:
Small stylish signature-style text in the top corner: "Mr. Tariq"
```

</details>

<a id="gpt-image-korean-cafe-mirror-selfie-portra-film"></a>
### 韩式咖啡馆庭院圆镜自拍胶片风

<a href="https://x.com/noorlewisx/status/2064996549747458319"><img src="../../previews/gpt-image-korean-cafe-mirror-selfie-portra-film.jpg" width="360"></a>

用外貌、服装、姿势、前景、中景、背景分段，围绕圆镜搭出清晰的景深层次。胶片型号、镜头和光圈（Portra 400、85mm、f/1.8）定下温暖柔焦的质感，负面提示词则让画面保持写实。

GPT Image 2 · 文生图 · 出处: [@noorlewisx on X](https://x.com/noorlewisx/status/2064996549747458319) · 214 赞，统计于 2026-10-28

[`film-photography`](tags.md#tag-film-photography) [`mirror-selfie`](tags.md#tag-mirror-selfie) [`korean-cafe`](tags.md#tag-korean-cafe) [`portra-400`](tags.md#tag-portra-400) [`lifestyle`](tags.md#tag-lifestyle)

<details><summary><b>提示词</b></summary>

```text
Hyper-realistic Kodak Portra 400 film photograph, dreamy soft aesthetic, warm natural sunlight, nostalgic Korean café atmosphere, vertical 9:16 composition.

A beautiful young woman crouching gracefully in front of a large round gold-framed mirror placed on a pebble-covered courtyard, taking a mirror selfie with her smartphone. She looks at the screen with a gentle smile and relaxed expression.

Appearance: Fair glowing skin, soft natural makeup, subtle peach blush, glossy pink lips, delicate eyeliner, bright expressive eyes. Long light-brown wavy hair with soft curtain bangs and romantic curls cascading over her shoulders.

Outfit: Oversized pastel lavender T-shirt featuring a small daisy illustration and subtle Korean typography, high-waisted butter-yellow pleated midi skirt, white crew socks, clean white canvas sneakers, soft pink shoulder tote bag.

Pose: Comfortable squat with knees together, one arm resting naturally on her leg while holding her phone. Relaxed shoulders, candid lifestyle photography feel, effortless charm.

Foreground: Two transparent iced latte cups with visible ice cubes, paper straws, soft condensation. Elegant pink tote bags beside the mirror. Creamy foreground bokeh and dreamy highlights.

Midground: Large circular gold-framed mirror reflecting the woman perfectly. Detailed gravel stones, warm sunlight, realistic reflections, soft shadows, potted plants surrounding the mirror, cinematic depth.

Background: Aesthetic Korean-style café exterior with cream-colored walls, wooden-framed windows, Korean signboard, lush ivy vines, flowers, potted plants, and a quiet pedestrian alley. Warm golden-hour sunlight filtering through trees, dreamy foliage bokeh.

Photography Style: Kodak Portra 400, warm pastel tones, soft focus, creamy highlights, realistic skin texture, subtle film grain, shallow depth of field, environmental portrait, HDR, photorealistic, magazine-quality editorial photography, 85mm lens, f/1.8, atmospheric depth, elegant composition, foreground-midground-background layering.

Negative Prompt: anime, cartoon, illustration, CGI, 3D render, painting, blurry face, distorted hands, extra fingers, duplicate objects, unrealistic proportions, overprocessed skin, harsh shadows, oversaturated colors, artificial lighting, watermark, logo, text, cropped subject, low quality.
```

</details>

<a id="nano-banana-bw-studio-portrait-white-shirt-contemplative-pose"></a>
### 白衬衫黑白棚拍男士肖像

<a href="https://x.com/weiinberg/status/2079797303280591190"><img src="../../previews/nano-banana-bw-studio-portrait-white-shirt-contemplative-pose.jpg" width="360"></a>

以上传照片为基础,先锁定面部特征、发型和胡须,再写服装与手托下巴的具体姿势。用明确的光线方向、无缝炭黑背景和85mm浅景深营造杂志感黑白效果。

Nano Banana 2 · 上传图改图 · 出处: [@weiinberg on X](https://x.com/weiinberg/status/2079797303280591190) · 211 赞，统计于 2026-10-29

[`black-and-white`](tags.md#tag-black-and-white) [`studio-portrait`](tags.md#tag-studio-portrait) [`identity-preserving`](tags.md#tag-identity-preserving) [`editorial`](tags.md#tag-editorial) [`85mm`](tags.md#tag-85mm)

<details><summary><b>提示词</b></summary>

```text
Nano Banana 2 on OpenArt.

Prompt: Create a premium black-and-white studio portrait of the uploaded man, preserving his recognizable facial identity, natural hairstyle, skin texture, and existing facial hair. Frame him from the upper thighs upward, standing confidently, subtle body tilt and facing the camera with an intense, sharp expression.Dress him in a crisp fitted white dress shirt with the collar slightly open and the sleeves neatly rolled to the elbows, paired with tailored black trousers. Pose him with one arm folded horizontally across his waist, supporting the opposite elbow, while the raised hand rests naturally against his lips or chin in a contemplative gesture. Add a classic round analog wristwatch with a dark leather strap on the raised wrist.
Place him against a clean, seamless charcoal-black studio background with a subtle soft gradient behind the upper body and no visible corners or props. Use soft directional light from the upper camera-right side, creating sculpted highlights on one side of the face and shirt while the opposite side falls into rich shadow. Keep strong subject-to-background separation, balanced contrast, crisp focus on the eyes, face, hands, and watch, realistic fabric folds, natural anatomy, and refined monochrome editorial toning. Shot with an 85mm portrait lens, shallow depth of field, high-end professional photography, 4:5 aspect ratio.
```

</details>

<a id="nano-banana-hibiscus-film-portrait"></a>
### 粉色木槿花环绕的复古胶片人像

<a href="https://x.com/ZaraIrahh/status/2107705937012142393"><img src="../../previews/nano-banana-hibiscus-film-portrait.jpg" width="360"></a>

镜头置于花丛中、透过前景花瓣拍摄，形成自然的花朵边框，并用侧分、单手入镜、头到胸构图等硬性规则锁定画面。胶片颗粒、光晕和漏光配合详细的负面词列表，避免成片变成精修棚拍感。

Nano Banana 2.1 · 文生图 · 出处: [@ZaraIrahh on X](https://x.com/ZaraIrahh/status/2107705937012142393) · 206 赞，统计于 2026-10-28

[`portrait`](tags.md#tag-portrait) [`film-look`](tags.md#tag-film-look) [`floral`](tags.md#tag-floral) [`photorealistic`](tags.md#tag-photorealistic) [`golden-light`](tags.md#tag-golden-light)

<details><summary><b>提示词</b></summary>

```text
Create a photorealistic portrait of her in a refined side-profile-inspired three-quarter angle, with her head naturally turned toward the camera and making direct eye contact. Clearly defined SIDE PART — NEVER a center or middle part.

She has extremely long, rich Dark Mocha Mousse curly hair, dramatically moved by a strong natural breeze, with realistic flyaways and loose strands. No ribbons, bows, headwear, hats, or hair accessories.

Soft-glam Korean-inspired makeup: visible natural pores, luminous realistic skin texture, rosy blush, subtle brown eyeliner, softly defined eyes, rosy gradient lips, and nude espresso nail art. She wears a magenta-soft-purple thin-strap mini dress with a subtle heart-shaped neckline barely visible at the chest. Gold fairy-wing pendant necklace with matching earrings.

ONE HAND is naturally raised in front of her face, gently pushing or clearing a hibiscus flower away from her line of sight. Fingers and joints must be anatomically realistic. Her other hand is completely outside the frame.

Expression: calm, intimate, slightly curious, natural and emotionally subtle.

EYE-LEVEL CAMERA positioned directly among dense blooming soft-pink and white hibiscus flowers, photographing THROUGH the flowers. Foreground petals, leaves, and stems are very close to the lens and naturally overlap the outer edges of the frame, creating an intimate organic floral frame. Flowers must not obscure her eyes or facial features.

NO WIDE VIEW. The subject fills approximately 85–95% of the frame. ONLY HEAD TO CHEST VISIBLE.

VISUAL STYLE:
Warm nostalgic historical-memory aesthetic. Authentic vintage Canon analog-film character, subtle natural film grain, delicate halation, slightly faded tones, gentle light leaks, realistic exposure imperfections, soft natural shadows, authentic raw human skin texture, and warm soft daylight. Strong wind visibly moves the curls and loose strands. Mild natural motion blur ONLY on moving hair and nearby flower petals.

The final image should feel like a candid, emotionally intimate photograph captured on vintage film rather than a polished studio portrait.

NEGATIVE PROMPT:
center part, middle part, ribbons, bows, headwear, hat, full body, waist-down, staircase focus, wide shot, distant subject, excessive background, artificial bokeh, studio lighting, smartphone photography, modern digital DSLR look, CGI, cartoon, anime, illustration, plastic skin, beauty filter, over-retouched skin, excessive facial smoothing, face swap, distorted facial anatomy, unnatural hands, malformed fingers, extra fingers, missing fingers, floating limbs, flower covering face, obscured eyes, closed eyes, facial distortion, unnatural pose, watermark, text, logo.
```

</details>

<a id="gpt-image-snowy-village-floral-shawl-portrait"></a>
### 雪村中披蓝色花披肩的女子肖像

<a href="https://x.com/noorlewisx/status/2067526808602542413"><img src="../../previews/gpt-image-snowy-village-floral-shawl-portrait.jpg" width="360"></a>

提示词依次交代服饰、肤色、眼神和表情，再用虚化木屋和远处模糊人影营造层次。85mm、浅景深、柔和漫射光和冷色调等镜头与光线描述带出电影感。

GPT Image 2 · 文生图 · 出处: [@noorlewisx on X](https://x.com/noorlewisx/status/2067526808602542413) · 201 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`winter`](tags.md#tag-winter) [`snow`](tags.md#tag-snow) [`cinematic`](tags.md#tag-cinematic) [`85mm`](tags.md#tag-85mm)

<details><summary><b>提示词</b></summary>

```text
A cinematic portrait of a young woman standing in a snowy village, softly falling snowflakes surrounding her. She wears a delicate blue floral shawl wrapped around her head and shoulders, dusted with snow. Her skin is fair with a natural glow, soft pink lips, and expressive light eyes looking slightly to the side. Her expression is calm and introspective. The background shows a blurred wooden cabin and a faint figure in the distance,creating depth. Cold winter atmosphere, soft diffused lighting, shallow depth of field, ultra-realistic, highly detailed textures, 85mm lens, bokeh, photorealistic, 8K resolution, muted cool color palette, cinematic mood."
```

</details>

<a id="gpt-image-orange-red-studio-portrait-turtleneck"></a>
### 橙红渐变背景下的黑色高领毛衣棚拍人像

<a href="https://x.com/iamsofiaijaz/status/2070714200306110845"><img src="../../previews/gpt-image-orange-red-studio-portrait-turtleneck.jpg" width="360"></a>

提示词把暖橙主光和深红轮廓光成对指定，直接决定整体配色以及发丝边缘的光晕。镜头焦段、光圈和感光参数配合紧凑的半身构图，让画面更接近杂志封面人像。

GPT Image 2 · 文生图 · 出处: [@iamsofiaijaz on X](https://x.com/iamsofiaijaz/status/2070714200306110845) · 195 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`studio-lighting`](tags.md#tag-studio-lighting) [`fashion`](tags.md#tag-fashion) [`gradient-background`](tags.md#tag-gradient-background)

<details><summary><b>提示词</b></summary>

```text
Ultra-photorealistic editorial fashion portrait of a beautiful young woman with straight blonde hair, piercing eyes, and an intense direct gaze, wearing a premium black high-neck turtleneck sweater. Tight head-and-shoulders close-up, shot from a slightly low angle to create a bold, heroic, commanding presence. Dramatic cinematic studio lighting with a warm orange key light and deep red rim lighting sculpting the face, emphasizing natural skin texture, pores, and fine facial detail while creating rich contrast and cinematic shadows. Clean seamless studio backdrop featuring a vivid orange-to-deep-red gradient background. Razor-sharp focus on the eyes, hyperrealistic skin detail, premium editorial fashion photography, luxury magazine cover aesthetic, ultra-detailed, 8K resolution, HDR, realistic color grading, soft falloff, subtle catchlights, professional medium-format camera, 85mm portrait lens, f/4, ISO 100, studio strobe lighting, high dynamic range, crisp details, minimal makeup, symmetrical composition, ultra-realistic, masterpiece quality, vertical 3:4 composition.
```

</details>

<a id="gpt-image-tokyo-night-flash-candid-snapshot"></a>
### 东京雨夜街头的闪光灯随手抓拍

<a href="https://x.com/frametheory058/status/2098413109258207670"><img src="../../previews/gpt-image-tokyo-night-flash-candid-snapshot.jpg" width="360"></a>

用参考图锁定人物与服装以保持系列一致，再逐项写明手机拍摄的瑕疵：直闪、行走抖动、卷帘快门、对焦不准和偏心构图。末尾列出棚拍光、HDR、磨皮等禁用项，避免画面显得摆拍。

GPT Image 2.5 · 上传图改图 · 出处: [@frametheory058 on X](https://x.com/frametheory058/status/2098413109258207670) · 191 赞，统计于 2026-10-28

[`smartphone-snapshot`](tags.md#tag-smartphone-snapshot) [`direct-flash`](tags.md#tag-direct-flash) [`night-street`](tags.md#tag-night-street) [`tokyo`](tags.md#tag-tokyo) [`character-consistency`](tags.md#tag-character-consistency)

<details><summary><b>提示词</b></summary>

```text
Ultra-realistic late-night smartphone snapshot, 9:16 vertical.

Use the reference only to establish the same fictional female character’s overall appearance and continuity. Keep her recognizable across the series with the same dark-brown wavy hair, natural features, black fitted sleeveless tank top, loose high-waisted light-blue jeans, small gold hoop earrings, delicate necklace, white sneakers, and small black shoulder bag.

Scene:
A quiet Tokyo side street late at night after light rain. She walks beside an off-white ceramic-tiled building while distant convenience-store lights, traffic signals, parked bicycles and small Japanese storefronts softly disappear into the darkness. Wet pavement catches scattered reflections.

New candid moment:
Photograph her from a slightly low rear three-quarter angle, about two steps behind her. She has just slowed down and casually turns only her upper body toward the camera while continuing forward. One hand is loosely tucking windblown hair behind her ear while the other hangs naturally beside her bag.

She looks toward the camera from the corner of her eyes with a tiny closed-mouth smile, as though she noticed her friend taking another photo and is trying not to laugh.

No deliberate fashion pose. No exaggerated expression. Her shoulders remain relaxed, hips and legs naturally positioned from walking, with one foot caught halfway through the next step.

Camera:
Modern smartphone rear camera with direct flash. Photographer walking at the same time, creating subtle accidental camera shake. Slight motion blur around her hair, moving leg and fingertips, while her eyes remain just barely readable. Mild rolling-shutter distortion, imperfect autofocus, slight edge softness and realistic digital noise.

Composition should feel accidental: her body sits slightly off-center, a little too much empty darkness on one side, with part of her shoe approaching the bottom edge of frame.

Flash & exposure:
Hard direct phone flash illuminates her face, shoulder, black top and denim while the street behind her falls rapidly into darkness. Slightly overexposed skin highlights, hard natural shadow against the tiled wall, shiny flash reflections on individual hair strands and subtle denim texture. Distant lights bloom and smear naturally.

Aesthetic:
Raw Pinterest night-photo-dump energy. Intimate, youthful, spontaneous and imperfect. It should look like a friend took the photo during a random Tokyo night walk—not a photographer conducting a photoshoot.

Real pores, tiny skin variations, flyaway hairs, natural fabric wrinkles, realistic body proportions and ordinary smartphone processing.

Absolutely no: studio lighting, cinematic teal-orange grading, professional bokeh, fashion-editorial posing, perfect symmetry, airbrushed skin, artificial beauty retouching, HDR look, DSLR sharpness, staged composition, AI-perfect anatomy or polished commercial photography.

The final result should feel like an unexpectedly beautiful photo hidden among 30 messy pictures from the same night.
```

</details>

<a id="gpt-image-warm-shadow-close-up-portrait"></a>
### 暖色阴影光下的女性极致特写

<a href="https://x.com/AizaAi12/status/2097143936024228151"><img src="../../previews/gpt-image-warm-shadow-close-up-portrait.jpg" width="360"></a>

上传照片作为面部身份锚点，提示词再分层描述肌肤、腮红、唇色和眼部细节，配合柔和戏剧光与浅景深。情绪描述引导表情，而非指定姿势。

GPT Image 2 · 上传图改图 · 出处: [@AizaAi12 on X](https://x.com/AizaAi12/status/2097143936024228151) · 191 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`photorealism`](tags.md#tag-photorealism) [`cinematic-lighting`](tags.md#tag-cinematic-lighting) [`identity-reference`](tags.md#tag-identity-reference)

<details><summary><b>提示词</b></summary>

```text
Use the uploaded image as the primary facial identity reference. Preserve the subject's recognizable facial structure, proportions, defining features, and natural appearance with maximum possible accuracy. Do not replace, reshape, or significantly alter her facial identity.

Create a cinematic, ultra-detailed extreme close-up portrait of the same young woman, captured with breathtaking photorealism. She has soft, natural facial features, luminous dewy glass skin with realistic fine pores and natural texture, a healthy subtle glow, and delicate peach-pink blush softly diffused across her cheeks.

Her eyebrows are naturally shaped and delicately arched. Her eyes are captivating, expressive, and detailed, with realistic reflections and individually defined eyelashes. Her lips are soft and slightly parted, finished with a subtle glossy coral-nude tint.

Create an intimate and emotionally cinematic atmosphere, as though she is silently holding back a thousand unspoken thoughts. Soft dramatic lighting, gentle shadows, shallow depth of field, cinematic color grading, realistic skin translucency, detailed eyes, natural hair strands, and subtle highlights.

Ultra-photorealistic, cinematic beauty portrait, extreme facial detail, editorial photography, premium film still aesthetic, high dynamic range, realistic lens depth, emotionally powerful composition, 8K quality.
```

</details>

<a id="nano-banana-pink-picnic-blanket-peony-portrait"></a>
### 粉色野餐芍药与草莓人像

<a href="https://x.com/Just_sharon7/status/2075819429372305722"><img src="../../previews/nano-banana-pink-picnic-blanket-peony-portrait.jpg" width="360"></a>

提示词让发色、裙子、野餐垫和花朵统一使用婴儿粉色调，整幅画面形成一致的色彩基调。黄金时刻逆光加上公园背景虚化，让场景柔和梦幻。

Nano Banana 2 · 文生图 · 出处: [@Just_sharon7 on X](https://x.com/Just_sharon7/status/2075819429372305722) · 186 赞，统计于 2026-10-28

[`picnic`](tags.md#tag-picnic) [`pink`](tags.md#tag-pink) [`peony`](tags.md#tag-peony) [`golden-hour`](tags.md#tag-golden-hour) [`top-down`](tags.md#tag-top-down)

<details><summary><b>提示词</b></summary>

```text
A beautiful young East Asian woman lying on her back on a soft baby pink floral picnic blanket, top-down view, long voluminous wavy platinum blonde hair with baby pink highlights dramatically spread out around her head like a golden-pink halo, soft bangs, fair flawless skin, bright cheerful smile showing perfect white teeth, large expressive brown eyes, wearing a cute baby pink summer dress with puffed short sleeves and square neckline showing cleavage, delicate gold layered necklaces with heart pendant, small gold hoop earrings, sunny outdoor park picnic scene, large vibrant baby pink peonies and roses placed around her, wicker picnic basket in the corner, glass of fresh lemonade with lemon slice nearby, soft golden hour sunlight with gentle pink tones, beautiful natural lighting, bokeh background, highly detailed, photorealistic, cinematic composition, vibrant baby pink color palette, dreamy summer atmosphere.
```

</details>

<a id="gpt-image-realistic-woman-3d-girl-night-park"></a>
### 公园长椅上的真人女子与3D动画女孩

<a href="https://x.com/Alina_with_Ai/status/2102960952266432853"><img src="../../previews/gpt-image-realistic-woman-3d-girl-night-park.jpg" width="360"></a>

上传的照片锁定女子的身份，另一段详细描述让女孩保持可爱的3D动画风格并穿着同款街头服装。暖色路灯轮廓光和柔和的城市散景把两种风格融进同一个夜景，不过模型对指定姿势的执行比较宽松。

GPT Image 2.5 · 上传图改图 · 出处: [@Alina_with_Ai on X](https://x.com/Alina_with_Ai/status/2102960952266432853) · 185 赞，统计于 2026-10-28

[`mixed-style`](tags.md#tag-mixed-style) [`3d-character`](tags.md#tag-3d-character) [`night-park`](tags.md#tag-night-park) [`identity-reference`](tags.md#tag-identity-reference) [`golden-light`](tags.md#tag-golden-light)

<details><summary><b>提示词</b></summary>

```text
Create a single cinematic vertical 9:16 image based closely on the uploaded reference.

Show TWO characters standing side by side at night in a beautiful city park.

The adult woman is the main realistic character. Use my uploaded photo as her identity reference and preserve my facial identity, facial structure, skin tone, and recognizable appearance. She has long dark brown hair and wears masculine oversized streetwear: a dark olive/black oversized utility jacket, black oversized hoodie, extremely loose black cargo pants, and white chunky sneakers.

The woman is standing naturally and looking DOWN toward the little girl with a warm, genuine smile. Her body is slightly turned toward the little girl. One hand is casually inside her jacket/pants pocket, while her other hand is raised and her index finger is POINTING toward the little girl, as if proudly introducing or showing her. Make the pointing gesture very clear and natural.

Beside her stands an adorable small 3D animated girl. Keep the little girl extremely cute: oversized expressive brown eyes, rosy cheeks, tiny face, brown hair in a messy high bun with loose strands, black oversized hoodie with a small crown emblem, loose black cargo pants, and white chunky sneakers. She is standing upright and looking up at the woman with a sweet playful smile.

IMPORTANT:
- Both characters must be FULLY STANDING.
- One single image only, NOT a collage or split screen.
- The woman must be pointing toward the little girl.
- The woman must be looking at the little girl and smiling.
- The little girl must be looking up at the woman.
- Keep a clear height difference between them.
- Do not make the little girl photorealistic; keep her cute high-quality 3D animated appearance.
- Do not change the little girl's outfit, hairstyle, facial style, or body proportions.

Set them on a nighttime park walkway with leafy trees, warm glowing streetlights, distant city lights, soft bokeh, golden rim lighting around their hair and shoulders, realistic shadows, and a cozy magical atmosphere.

Photorealistic adult woman + adorable 3D animated girl, seamless integration, cinematic photography, realistic skin and clothing textures, warm golden color grading, shallow depth of field, ultra-detailed, natural proportions, professional composition, vertical 9:16.

The final composition should clearly communicate: the big girl is proudly pointing at the cute little girl while smiling at her.
```

</details>

<a id="gpt-image-rainy-car-window-cream-sweater-portrait"></a>
### 雨天车窗旁穿奶油毛衣的女性肖像

<a href="https://x.com/itxabdullaa/status/2071516626886000850"><img src="../../previews/gpt-image-rainy-car-window-cream-sweater-portrait.jpg" width="360"></a>

将柔焦光学术语（黑色Pro Mist柔光滤镜、光晕、奶油般的焦外）与具体拍摄条件结合：85mm镜头 f/1.2、窗外雨滴和自然窗光。真实的物理线索让梦幻的雾感读起来像一张胶片照片，而不只是滤镜效果。

GPT Image 2 · 文生图 · 出处: [@itxabdullaa on X](https://x.com/itxabdullaa/status/2071516626886000850) · 183 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`soft-focus`](tags.md#tag-soft-focus) [`film-photography`](tags.md#tag-film-photography) [`rainy-day`](tags.md#tag-rainy-day)

<details><summary><b>提示词</b></summary>

```text
Ultra-realistic cinematic portrait of a beautiful young woman sitting inside a car, long dark brown hair partially covering one eye, soft porcelain skin, oversized cream sweater, resting her cheek on her hand, dreamy melancholic expression, soft focus, dreamy blur, diffusion filter effect, Black Pro Mist filter, subtle glow, cinematic haze, bloom lighting, ethereal atmosphere, shallow depth of field, creamy bokeh, warm muted color grading, rainy day outside the window, natural window light, low contrast, film photography, 85mm lens, f/1.2, photorealistic, editorial fashion portrait, masterpiece, ultra detailed, 9:16.

Dreamy soft blur, gauzy atmosphere, misty lens, delicate glow, cinematic diffusion, velvety focus, soft cinematic haze, romantic film look, gentle bloom, dreamy aesthetic.

Negative Prompt: sharp focus, overly detailed pores, harsh contrast, HDR, oversaturated, crisp edges, strong sharpening, digital look, cartoon, anime, CGI
```

</details>

<a id="nano-banana-bearded-man-teal-armchair-tablet-portrait"></a>
### 蓝绿丝绒扶手椅中手持平板的胡须男士

<a href="https://x.com/rovvmut_/status/2061464975408021993"><img src="../../previews/nano-banana-bearded-man-teal-armchair-tablet-portrait.jpg" width="360"></a>

将身体角度与头部朝向分开描述，并明确每只手持有的道具，使模型能清楚理解空间布局。指定50mm镜头、明暗对比的侧光以及纯色炭灰背景，让画面聚焦于人物。

Nano Banana 2 · 文生图 · 出处: [@rovvmut_ on X](https://x.com/rovvmut_/status/2061464975408021993) · 177 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`studio-lighting`](tags.md#tag-studio-lighting) [`chiaroscuro`](tags.md#tag-chiaroscuro) [`creative-professional`](tags.md#tag-creative-professional)

<details><summary><b>提示词</b></summary>

```text
Nano Banana 2 on Gemini.

Prompt: A professional, high-resolution portrait of a man with a neat beard and messy dark hair, sitting in a plush dark teal velvet armchair. He is seated at a slight three-quarter angle, body tilted toward the left while his head is turned to face the camera directly with a friendly expression. Details & Props: He is wearing a sophisticated tan or camel-colored blazer over a crisp white t-shirt. On his left wrist, a black smartwatch is visible. He is holding a sleek silver tablet in his right hand and a white stylus (Apple Pencil) in his left hand, resting them naturally on his lap. Lighting & Atmosphere: The scene features soft, cinematic side-lighting (Chiaroscuro style) that creates gentle shadows on one side of his face and body, adding depth. The background is a minimalist, solid dark charcoal grey, ensuring all focus remains on the subject. Technical Specifications: Ultra-realistic photography, 8K resolution, sharp focus on facial features, shallow depth of field, shot on a 50mm lens, professional studio lighting, clean composition, aspect ratio 4:5. Key Elements Noted: The Tilt: The "three-quarter" body position is crucial for that specific seated look. The Grip: I've specified the pen and tablet being held simultaneously to match the "creative professional" vibe.
The Backdrop: Keeping it "solid charcoal" avoids unwanted textures or distractions.
```

</details>

<a id="gpt-image-fisheye-selfie-doorstep-cat"></a>
### 门阶上与好奇猫咪的鱼眼自拍

<a href="https://x.com/MissDelulu9/status/2111697628941717933"><img src="../../previews/gpt-image-fisheye-selfie-doorstep-cat.jpg" width="360"></a>

提示词指定鱼眼镜头，并让猫的大鼻子占据近景，畸变带来纵深感和趣味。它逐件写明服装和斑驳的门板质感，并要求保留自拍中的面部特征。

GPT Image 2.5 · 上传图改图 · 出处: [@MissDelulu9 on X](https://x.com/MissDelulu9/status/2111697628941717933) · 173 赞，统计于 2026-10-28

[`fisheye`](tags.md#tag-fisheye) [`selfie`](tags.md#tag-selfie) [`pet`](tags.md#tag-pet) [`candid`](tags.md#tag-candid) [`street`](tags.md#tag-street)

<details><summary><b>提示词</b></summary>

```text
Create a realistic fisheye photo of the woman in my uploaded selfie, preserving her exact facial features. She sits on a doorstep in front of weathered green wooden doors, wearing a beige trench coat, ivory turtleneck, and light blue jeans. A curious tabby-and-white cat fills the right foreground with an oversized nose and expressive eyes. Soft daylight, natural textures, playful candid mood, ultra-realistic photography, landscape 16:9, no text.
```

</details>

<a id="nano-banana-y2k-flash-beauty-portrait-black-backdrop"></a>
### 黑色背景下的Y2K闪光灯美妆人像

<a href="https://x.com/SimplyAnnisa/status/2072293670007796111"><img src="../../previews/nano-banana-y2k-flash-beauty-portrait-black-backdrop.jpg" width="360"></a>

提示词按妆容、发型、表情、服装、光线分块标注，便于单独调整每个元素。直闪加轮廓逆光在纯黑背景上形成光晕，结尾的风格关键词串则锁定2000年代初数码相机的质感。

Nano Banana 2 · 文生图 · 出处: [@SimplyAnnisa on X](https://x.com/SimplyAnnisa/status/2072293670007796111) · 171 赞，统计于 2026-10-28

[`y2k`](tags.md#tag-y2k) [`flash-photography`](tags.md#tag-flash-photography) [`beauty-portrait`](tags.md#tag-beauty-portrait) [`rim-light`](tags.md#tag-rim-light) [`editorial`](tags.md#tag-editorial)

<details><summary><b>提示词</b></summary>

```text
Ultra-realistic beauty portrait of a stunning young woman, photographed from a slightly low-angle smartphone selfie perspective. Captured with an authentic early-2000s digital camera aesthetic using an intense direct flash. Deep pure-black background completely isolates the subject, creating dramatic contrast and making the face glow against darkness. Strong Y2K flash photography produces bright specular highlights, glass-like eye reflections, glossy skin sheen, and a nostalgic nightlife editorial atmosphere.

MAKEUP:
The woman has large almond-shaped hazel-brown eyes with luminous reflections, thick wispy manga-inspired lashes, naturally full fluffy eyebrows, soft freckles scattered across the bridge of the nose and upper cheeks, a delicate button nose with rosy blush concentrated on the tip, and full naturally plump lips wearing dusty rose pink lipstick with a subtle glossy finish. Flawless porcelain skin with realistic pores, natural texture, and soft peachy undertones. Soft feminine glam makeup. Neutral taupe eyeshadow, elongated fox-eye liner extending toward the temples, dramatic clustered lashes, luminous inner-corner shimmer, subtle contouring, flushed rosy cheeks and nose bridge, softly overlined lips, glossy highlights enhanced by direct flash. Luxury editorial beauty makeup.

HAIR
Extremely voluminous supermodel blowout hairstyle with rich chocolate-brown tones and warm caramel undertones. Dramatic crown lift, feathered layers, luxurious salon-finished texture, silky shine, flowing movement, soft flyaways. Powerful luminous halo surrounding the hair and face. Strong rim lighting traces every strand of hair, creating a radiant angelic aura. Backlit glow creates a dreamy cinematic effect with soft bloom around illuminated edges.

EXPRESSION:
Dreamy upward gaze looking away from the camera, confident yet ethereal expression.

OUTFIT
Sleeveless charcoal-gray pinstripe fitted top with black ribbon lace-up neckline. Elegant feminine silhouette. Modern Y2K-inspired styling.

LIGHTING
Strong direct Y2K camera flash combined with subtle backlighting. Bright flash creates crisp facial definition, intense eye reflections, glossy lips, luminous cheekbones, and reflective skin highlights. Ethereal halo surrounding the entire silhouette. Soft bloom effect around highlights, subtle lens glow, dreamy atmospheric diffusion.

Vogue beauty editorial, luxury cosmetics campaign, fashion magazine cover photography, cinematic beauty portrait, ultra-detailed skin texture, shallow depth of field, HDR photography, hyper-realistic eyes, nostalgic digital camera grain, flash bloom, glamorous nightlife energy, dark feminine aesthetic, angelic glow, luxury fashion campaign, 8K ultra realism.

STYLE BOOSTERS
Y2K digital camera flash, cyber-feminine glamour, dreamy halo glow, luminous aura, glowing silhouette, flash photography, nostalgic 2003 party photography, supermodel beauty campaign, luxury editorial portrait, soft bloom, cinematic rim light, glossy highlights, dark aesthetic, hyperrealism, magazine cover quality.
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

<a id="nano-banana-beach-portrait-ice-cream-cone"></a>
### 微笑女孩手持冰淇淋站在海滩小屋旁

<a href="https://x.com/SyntheSarah/status/2080972261335748910"><img src="../../previews/nano-banana-beach-portrait-ice-cream-cone.jpg" width="360"></a>

提示词按主体、服装、背景、光线、镜头的固定顺序分段描述，每个部分只说一次，画面因此保持一致。85mm f/1.8 镜头参数和指定的黄金时段光线方向，控制了浅景深以及面部和墨镜上柔和的暖色高光。

Nano Banana 2 · 文生图 · 出处: [@SyntheSarah on X](https://x.com/SyntheSarah/status/2080972261335748910) · 166 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`beach`](tags.md#tag-beach) [`golden-hour`](tags.md#tag-golden-hour) [`lifestyle`](tags.md#tag-lifestyle)

<details><summary><b>提示词</b></summary>

```text
A photorealistic, ultra-high-resolution lifestyle portrait of a smiling young woman standing beside a white wooden railing on a colorful beach promenade lined with vibrant pastel beach huts. She has long medium-brown hair styled into a single side braid draped over her right shoulder. She is wearing round black sunglasses with a thin gold metal frame, small silver stud earrings, and several stacked silver bracelets on her left wrist.
She is holding a vanilla-and-strawberry ice cream cone in her left hand near her face while looking slightly to her left, smiling broadly with visible white teeth and natural dimples. Her right hand is casually tucked into the pocket of her high-waisted white tailored shorts featuring belt loops, a visible black button, and crisp structured fabric.
She wears a fitted short-sleeve knit T-shirt with horizontal stripes in soft cream, pale yellow, light blue, and muted gray. The shirt has a fine ribbed texture and fits naturally without wrinkles.
The background features a row of colorful beach cabins painted in bright blue, turquoise, yellow, and orange, receding into the distance with strong perspective. A white wooden fence runs diagonally through the foreground, creating depth. The background is softly blurred with a creamy bokeh effect while the subject remains razor-sharp.
Golden-hour natural sunlight illuminates her face from the front-left, producing soft shadows, realistic skin texture, vibrant colors, and gentle highlights on the sunglasses and jewelry. Shot with an 85mm portrait lens at f/1.8, shallow depth of field, eye-level composition, vertical framing (9:16), DSLR-quality photography, HDR, ultra-detailed skin, natural proportions, realistic hands with five fingers, clean fingernails, highly detailed clothing fabric, cinematic color grading, no text, no watermark, no logo.
```

</details>

<a id="nano-banana-art-studio-man-miniature-self-figurine"></a>
### 微笑画师与桌上的迷你自己手办

<a href="https://x.com/Taaruk_/status/2039625508535885876"><img src="../../previews/nano-banana-art-studio-man-miniature-self-figurine.jpg" width="360"></a>

直接点明比例反差错觉，并用手办细节描述让桌上的迷你分身显得真实可信。暖色台灯、浅景深和 50mm 镜头让整个画室场景保持摄影质感。

Nano Banana 2 · 文生图 · 出处: [@Taaruk_ on X](https://x.com/Taaruk_/status/2039625508535885876) · 164 赞，统计于 2026-10-28

[`miniature`](tags.md#tag-miniature) [`scale-contrast`](tags.md#tag-scale-contrast) [`studio-portrait`](tags.md#tag-studio-portrait) [`shallow-depth-of-field`](tags.md#tag-shallow-depth-of-field) [`cinematic`](tags.md#tag-cinematic)

<details><summary><b>提示词</b></summary>

```text
Ultra-realistic cinematic portrait of a young man sitting at a wooden desk in a cozy art studio, smiling warmly at the camera, with a tiny miniature version of himself standing on the table in front of him, perfectly detailed like a small figurine, surrounded by paint brushes, sketches, and art tools, warm ambient lighting from a desk lamp, shallow depth of field, soft bokeh background, creative storytelling composition, scale contrast illusion, hyper-detailed textures, 50mm lens, photorealistic, 8K.
```

</details>

<a id="nano-banana-bearded-man-amber-sunglasses-blue-cardigan"></a>
### 戴琥珀色墨镜、穿蓝色针织开衫的胡须男士

<a href="https://x.com/rovvmut_/status/2052273526758121636"><img src="../../previews/nano-banana-bearded-man-amber-sunglasses-blue-cardigan.jpg" width="360"></a>

提示词按脸部、眼镜、服装和道具分句逐项描写，再交代明亮自然光和虚化的蓝色老车背景。点明材质细节，并用冷色背景衬托暖色镜框与肤色，画面更有电影感。

Nano Banana 2 · 文生图 · 出处: [@rovvmut_ on X](https://x.com/rovvmut_/status/2052273526758121636) · 163 赞，统计于 2026-10-28

[`portrait`](tags.md#tag-portrait) [`sunglasses`](tags.md#tag-sunglasses) [`knitwear`](tags.md#tag-knitwear) [`street-style`](tags.md#tag-street-style) [`cinematic`](tags.md#tag-cinematic)

<details><summary><b>提示词</b></summary>

```text
Nano Banana 2 on Gemini.

Prompt: A stylish, rugged portrait of a man with a relaxed yet sophisticated urban look. He features messy dark hair with natural highlights and a well-maintained, thick beard. He is wearing distinctive vintage-style sunglasses with translucent amber frames and dark, circular lenses that feature a unique metal flip-up bridge mechanism. He is dressed for cool weather in a chunky, blue ribbed-knit cardigan with a thick lapel, worn over a simple white t-shirt. In the foreground, his hand is partially visible, holding a white disposable coffee cup with a matching white lid. The lighting is bright and natural, casting soft shadows that emphasize the texture of his knitwear and facial hair. The background is a soft-focus blue vintage vehicle with horizontal grille lines, creating a cool-toned, cinematic backdrop that makes the warm tones of his sunglasses and skin pop.
```

</details>

<a id="gpt-image-wet-profile-portrait-green-eyes"></a>
### 湿发近景侧脸人像，绿褐色眼睛

<a href="https://x.com/j_smeaton99/status/2063088697495724500"><img src="../../previews/gpt-image-wet-profile-portrait-green-eyes.jpg" width="360"></a>

可见毛孔、水珠和自然眼神光等具体皮肤与眼部细节锁定写实质感，85mm f/1.8 镜头参数配合干净的浅灰色散景背景，把主体从环境中分离出来。

GPT Image 2 · 文生图 · 出处: [@j_smeaton99 on X](https://x.com/j_smeaton99/status/2063088697495724500) · 161 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`photorealistic`](tags.md#tag-photorealistic) [`close-up`](tags.md#tag-close-up) [`beauty`](tags.md#tag-beauty)

<details><summary><b>提示词</b></summary>

```text
Extreme wet close-up portrait of a young woman in side profile. Dark, rain-soaked hair naturally clinging to her skin and framing her face. Fine water droplets and a delicate layer of moisture glistening realistically across her cheeks, forehead, and jawline. Striking natural green-hazel eyes as the focal point, featuring subtle authentic reflections and lifelike depth without excessive shine. Soft, hydrated lips with realistic texture and a gentle natural gloss. Smooth skin with visible pores and nuanced facial details for maximum realism. Cinematic soft lighting with cool tones, creating a fresh atmospheric mood. Clean light gray and white bokeh background with shallow depth of field. Ultra-detailed photography, high-end editorial beauty portrait, natural facial proportions, realistic skin rendering, sharp eye focus, professional DSLR quality, photorealistic, 85mm lens, f/1.8, ultra-high resolution.
```

</details>

<a id="nano-banana-ccd-flash-sofa-selfie-portrait"></a>
### 米色圈圈绒沙发上的回眸CCD闪光自拍

<a href="https://x.com/Emmma___0/status/2107687127844856184"><img src="../../previews/nano-banana-ccd-flash-sofa-selfie-portrait.jpg" width="360"></a>

提示词把要求拆成姿势、发型、表情、服装、背景和相机等标注段落，并指定老式CCD相机直闪，营造随手抓拍的质感。长长的负面词列表排除了过于整齐的头发、塑料感皮肤和扭曲的脖子，让凌乱发丝、皮肤纹理和姿态都显得真实可信。

Nano Banana 2.1 · 上传图改图 · 出处: [@Emmma___0 on X](https://x.com/Emmma___0/status/2107687127844856184) · 157 赞，统计于 2026-10-27

[`ccd-flash`](tags.md#tag-ccd-flash) [`selfie`](tags.md#tag-selfie) [`korean-makeup`](tags.md#tag-korean-makeup) [`identity-preservation`](tags.md#tag-identity-preservation) [`labeled-blocks`](tags.md#tag-labeled-blocks)

<details><summary><b>提示词</b></summary>

```text
Create image: A hyper-photorealistic shot of the same subject in the attached image, detailed pores, rosy dewy skin, Douyin glass-skin, pink gloss lips, aegyosal, blush, grey contacts, wispy lashes, brushed brows, thin liner. Preserve her recognizable facial identity and natural proportions with a playful yet sophisticated Chryzleen-inspired indoor fashion aesthetic.

[POSE & COMPOSITION] A tight over-the-shoulder CCD selfie while she leans sideways into a plush sofa. The camera sits slightly behind and above her shoulder, creating a close three-quarter over-shoulder perspective. Only one eye, cheekbone, glossy lips, jawline, a sliver of neck, and the near shoulder are visible. The far side of her face is completely cropped out. Her head turns gently back toward the camera with a small natural tilt, keeping the neck relaxed and anatomically believable. One hand rests loosely on the sofa back behind her, with fingertips visible at the edge of the frame. The pose feels subtly seductive and candid rather than overly posed.

[HAIR] Deep side part with lifted roots and intentionally untidy, windswept volume. Several wispy strands fall across the forehead and cheek, while loose pieces spill naturally behind the shoulder. The hair should have irregular movement and soft imperfections, avoiding a freshly styled appearance.

[EXPRESSION] Half-lidded grey-contact gaze looking back toward the camera, relaxed brows, slightly lifted chin, soft jaw, glossy pink lips parted just enough to show a subtle glimpse of front teeth. Alluring, confident, and understated.

[OUTFIT] Sky-blue fitted sweetheart-neckline knit top with tiny white embroidered daisies, delicate scalloped edging, and miniature pearl-like buttons. Cute modern indoor fashion with a feminine fitted silhouette and soft textured fabric.

[BACKGROUND & ENVIRONMENT] A cozy contemporary living room with a warm beige boucle sofa, muted dusty-blue wall, softly blurred floor lamp, and a small cream cushion behind her. The room is visible only in narrow fragments around the extremely tight crop.

[BRANDING] A miniature Chryzleen engraving is physically placed on a tiny gold bracelet charm worn on the hand resting against the sofa. The Chryzleen mark should be naturally etched into the metal and remain subtle. This single Chryzleen accessory is the only visible branding treatment in the entire image.

[CAMERA] Old CCD digicam, direct flash, fine grain. Close over-the-shoulder three-quarter perspective with crisp detail on the visible eye, cheek, lips, messy hair wisps, shoulder, fingers, and tiny jewelry detail.

[QUALITY] Photorealistic pores and skin texture, natural facial asymmetry, believable hair movement, realistic hands and fingers, seamless neck anatomy, authentic knit texture, natural CCD grain, premium indoor fashion-editorial finish.

[MAKEUP] Fresh Korean soft-glam, natural glow, pink blush, wispy lashes, thin winged liner, shimmering rose-taupe eyeshadow, glossy pink lips.

Keep the Chryzleen branding physically integrated into the jewelry and visually understated, never functioning as graphic text.

1:1 aspect ratio.

[NEGATIVE PROMPT] cardigan, cardigan outfit, jacket, blazer, excessive head turn, extreme head tilt, extreme neck arch, twisted neck, unnatural neck curve, stiff pose, frontal selfie, symmetrical composition, perfectly polished hair, salon-perfect hair, no facial wisps, perfectly arranged strands, full body, half body, waist-up, loose crop, distant camera, excessive living room, hands covering face, hair-touching, malformed hands, extra fingers, missing fingers, warped eyes, plastic skin, over-smoothed face, pale washed-out skin, green cast, square skin artifacts, identity drift, multiple people, multiple Chryzleen marks, duplicate branding, watermark, floating text, random readable signage.
```

</details>

<a id="nano-banana-headphones-hoodie-motion-blur-portrait"></a>
### 居中黑卫衣男子，周围是动态模糊人影

<a href="https://x.com/rovvmut_/status/2063619957573963785"><img src="../../previews/nano-banana-headphones-hoodie-motion-blur-portrait.jpg" width="360"></a>

通过居中对称的中景构图、平光灰墙以及50mm镜头下f/2.8到f/4的景深，让主体清晰锐利。用定向横向运动模糊描述两侧人影，使静止的中心人物成为画面焦点。

Nano Banana 2 · 文生图 · 出处: [@rovvmut_ on X](https://x.com/rovvmut_/status/2063619957573963785) · 156 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`motion-blur`](tags.md#tag-motion-blur) [`editorial`](tags.md#tag-editorial) [`headphones`](tags.md#tag-headphones)

<details><summary><b>提示词</b></summary>

```text
Calm in the middle of the chaos. 🎧

Nano Banana 2 on Gemini.

Prompt: Cinematic fashion-editorial portrait of a person with messy hair, well groomed beard and glasses, framed as a centered medium shot from waist to head, subject perfectly aligned in the middle with symmetrical composition. Pose: Standing still facing camera directly, shoulders relaxed, hands in pockets, posture upright; facial expression neutral, calm, slightly detached. Wardrobe: Minimalist oversized black hoodie with matte fabric, no visible branding. Accessories: Large over-ear headphones worn on the head with a clean, modern design. Background: Flat, softly textured light gray wall (approx hex #d9d9d9) with subtle grain. Lighting: soft, diffused frontal lighting (5000-5500k) creating even illumination with minimal shadows and smooth skin tones; no harsh highlights, clean tonal transitions. Motion effect: Strong lateral motion blur silhouettes passing on both sides of the subject, creating ghosted human forms with directional blur, emphasizing stillness of the central figure. Optics: 50mm lens simulation, moderate depth of field (f/2.8-f/4) keeping subject sharp while motion-blurred elements streak across frame; slight film grain and soft contrast. Texture: Clean, natural skin detail with subtle softness, matte fabric rendering, minimal reflections. mood: introspective, isolated, urban, quiet contrast between stillness and surrounding motion. editorial, modern, high-detail, cinematic composition, ultra-realistic textures, professional fashion photography style.
```

</details>

<a id="nano-banana-white-halter-dress-keor-hem-portrait"></a>
### 白色吊带裙女子蹲坐，裙边绣有Keor字样

<a href="https://x.com/KeorUnreal/status/2064728849703748030"><img src="../../previews/nano-banana-white-halter-dress-keor-hem-portrait.jpg" width="360"></a>

提示词把主体、服装、环境和附加要求分开写，末尾的 full_prompt 再用一句话概括全部内容。把 Keor 文字放在裙摆并用细线绣制，使新增细节小而自然。

Nano Banana 2 · 文生图 · 出处: [@KeorUnreal on X](https://x.com/KeorUnreal/status/2064728849703748030) · 156 赞，统计于 2026-10-29

[`studio-portrait`](tags.md#tag-studio-portrait) [`glamour`](tags.md#tag-glamour) [`embroidered-text`](tags.md#tag-embroidered-text) [`dramatic-lighting`](tags.md#tag-dramatic-lighting)

<details><summary><b>提示词</b></summary>

```text
{
  "image_description": "A highly detailed, photorealistic studio portrait of a stunning young woman with long, wavy black hair, fair skin with natural freckles, and striking blue-green eyes. She sits on the floor against a solid black background in a dramatic pose with knees raised and legs apart, one hand running through her hair. She wears a form-fitting white short dress with a criss-cross halter neckline and glossy white high-heeled shoes. Her expression is confident and slightly vulnerable as she gazes directly at the camera.",
  "composition": "Low-angle medium full-body studio shot focusing on her pose, figure, and facial expression. Dramatic, high-contrast studio lighting with soft highlights on skin, hair, and the glossy shoes, creating a sensual and elegant atmosphere.",
  "details": {
    "woman": "Beautiful woman in her mid-20s, slim and toned build, long wavy black hair, expressive eyes, natural makeup with glossy lips.",
    "clothing": "Form-fitting white dress with criss-cross halter neckline, glossy white high-heeled shoes.",
    "environment": "Minimalist black studio backdrop.",
    "props": "None additional."
  },
  "modifications": {
    "additions": "Add a small, elegant embroidered sign reading 'Keor' in delicate cursive script on the visible border or hem of her white dress. Place it realistically along the lower hem, neckline edge, or side seam using fine white or metallic thread that blends naturally as a subtle, high-end custom detail."
  },
  "style": "Photorealistic, high-resolution glamour portrait photography, dramatic studio lighting, sharp focus on the subject, realistic skin texture, hair volume, fabric drape on the white dress, and glossy shoe reflections, confident and seductive mood.",
  "technical": {
    "resolution": "8K",
    "aspect_ratio": "portrait",
    "quality": "Extremely detailed wavy hair strands, skin texture with natural freckles, realistic white fabric folds and sheen, glossy white heels, and subtle embroidered 'Keor' sign."
  },
  "full_prompt": "Photorealistic studio portrait of a beautiful woman with long black hair wearing a form-fitting short white halter dress, sitting on the floor with knees raised and hand in hair, dramatic black background, confident gaze, add subtle embroidered 'Keor' on the border hem of the white dress --ar 2:3 --v 6 --q 2 --stylize 250"
}
```

</details>

<a id="nano-banana-rainy-car-window-night-portrait"></a>
### 雨夜车窗外拍的电影感人像

<a href="https://x.com/NikhilRajX/status/2035707444777865469"><img src="../../previews/nano-banana-rainy-car-window-night-portrait.jpg" width="360"></a>

把机位放在车外,让湿玻璃隔在镜头和人物之间,并明确写出雨滴、霓虹倒影和红蓝黄色虚化光斑。浅景深加低环境光打在脸上形成电影剧照氛围,上传的人脸图用来保持身份一致。

Nano Banana 2 · 上传图改图 · 出处: [@NikhilRajX on X](https://x.com/NikhilRajX/status/2035707444777865469) · 155 赞，统计于 2026-10-28

[`cinematic`](tags.md#tag-cinematic) [`rain`](tags.md#tag-rain) [`night`](tags.md#tag-night) [`portrait`](tags.md#tag-portrait) [`bokeh`](tags.md#tag-bokeh)

<details><summary><b>提示词</b></summary>

```text
Nano Banana 2 on Google Gemini

Prompt: Create a highly cinematic and realistic photo of a person using the face from the uploaded image. The person is sitting inside a car at night, looking out through a rain-covered window. The camera is positioned outside the car, capturing the person through the wet glass. Raindrops and streaks of water are clearly visible on the window, with reflections of city lights, neon signs, and passing cars blending into the glass. The person’s face is softly lit by ambient street lights and subtle interior car lighting, creating a moody and emotional expression. The background outside is blurred with colorful bokeh lights (red, blue, yellow), giving a deep cinematic feel. The person is wearing a modern outfit like a hoodie or jacket. The mood feels introspective and film-like. Ultra realistic photography, shallow depth of field, dramatic lighting, reflections, rain texture, Hollywood movie scene composition, high detail.
```

</details>

<a id="nano-banana-black-white-street-portrait-city-crowd"></a>
### 人群中静立的黑白街头肖像

<a href="https://x.com/iamrealsnow/status/2031179469617320282"><img src="../../previews/nano-banana-black-white-street-portrait-city-crowd.jpg" width="360"></a>

清晰的主体搭配动态模糊的人群和浅景深，让人物在喧闹场景中被单独突出。强对比光加脸部柔和轮廓光，保持夜晚街头的电影感。

Nano Banana 2 · 文生图 · 出处: [@iamrealsnow on X](https://x.com/iamrealsnow/status/2031179469617320282) · 152 赞，统计于 2026-10-28

[`street-portrait`](tags.md#tag-street-portrait) [`black-and-white`](tags.md#tag-black-and-white) [`motion-blur`](tags.md#tag-motion-blur) [`night`](tags.md#tag-night) [`cinematic`](tags.md#tag-cinematic)

<details><summary><b>提示词</b></summary>

```text
.
A cinematic black and white street portrait of a handsome man standing still in a busy city crowd, sharp focus on the subject while people around him are motion-blurred, shallow depth of field, intense masculine facial features textured beard, slightly messy wavy hair, wearing a dark tailored coat, calm yet powerful expression, dramatic contrast lighting, soft rim light on face, urban night atmosphere,
```

</details>

<a id="nano-banana-cgk-airport-travel-editorial"></a>
### 女子手持护照站在雅加达机场窗前

<a href="https://x.com/kingofdairyque/status/2073276310496129363"><img src="../../previews/nano-banana-cgk-airport-travel-editorial.jpg" width="360"></a>

提示词用真实地点细节（CGK、廊桥、牵引车、印尼尾旗）和明确的光源设定机场背景。按服装、妆容、手持道具等分段列出元素，让每个细节在输出中各自清晰呈现。

Nano Banana 2 · 文生图 · 出处: [@kingofdairyque on X](https://x.com/kingofdairyque/status/2073276310496129363) · 145 赞，统计于 2026-10-29

[`airport`](tags.md#tag-airport) [`travel`](tags.md#tag-travel) [`editorial`](tags.md#tag-editorial) [`portrait`](tags.md#tag-portrait)

<details><summary><b>提示词</b></summary>

```text
Create an ultra-realistic high-fashion travel editorial photographed inside Soekarno–Hatta International Airport (CGK), Jakarta, Indonesia. The model stands beside massive floor-to-ceiling glass windows overlooking the active airport apron. The background authentically showcases the airport's modern departure terminal architecture, featuring multiple passenger boarding bridges (garbarata), airport service vehicles, baggage carts, pushback tugs, runway markings, and several commercial aircraft parked at the gates. One aircraft prominently displays a red-and-white Indonesian flag on its tail, reinforcing the unmistakable Indonesian airport atmosphere.

Warm late-afternoon golden sunlight streams through the expansive terminal windows, naturally illuminating the model's face, collarbones, shoulders, and hair with soft golden highlights. Realistic glass reflections, cinematic shadows, atmospheric depth, and a vibrant blue sky with delicate clouds create an elegant luxury travel editorial mood.

Outfit:
Minimalist fitted white ribbed camisole tank top with a flattering body-hugging silhouette. Thick grey sporty headband. Oversized grey jacket casually draped over one forearm. Stacks of rose gold Cartier bracelets paired with a silver smartwatch. Milky white glossy nails. Delicate fine jewelry styled with a refined airport traveler aesthetic and understated luxury.

Hair:
Extreme-long, sleek, pin-straight jet-black hair with exceptional thickness and mirror-like shine. Soft front-layered face-framing C-curls. Visible individual hair strands, realistic flyaway hairs, and subtle natural movement created by a gentle breeze flowing through the terminal.

Skin & Face
Ultra-realistic skin with visible pores, delicate natural texture, and subtle imperfections for authentic photorealism. Healthy luminous glow without excessive skin smoothing or plastic appearance. Smooth even complexion with warm undertones, balanced facial proportions, refined editorial beauty, and naturally defined collarbones.

Makeup:
Radiant satin-glass complexion with naturally luminous skin. Bright diffused under-eyes for a refreshed youthful appearance. High-placement soft pink Igari-inspired blush across the cheeks and lightly over the bridge of the nose for a naturally flushed effect.
Soft neutral pink and taupe gradient eyeshadow blended seamlessly. Thin, precise eyeliner subtly elongates the eyes while maintaining a soft feminine appearance.
Large mesmerizing gray-green almond-shaped eyes with crystal-clear irises, subtle limbal rings, and multiple glossy catchlights reflecting the terminal windows. Thick black spiky manga-inspired mascara with individually separated wispy upper lashes and naturally defined lower lashes. Soft feathered taupe eyebrows with realistic individual hair strokes.
Full overlined lips in a delicate rosy pink shade with a subtle reddish ombré gradient. Ultra-glossy glass-like finish creates hydrated, plump, reflective lips that beautifully catch the warm golden sunlight.

Expression & Pose:
Elegant, calm, confident, sophisticated, and effortlessly luxurious. The model wears a subtle gentle smile, tilts her head slightly, and looks directly into the camera with a serene, dreamy expression. She holds an Indonesian passport and a boarding pass in her left hand, while her oversized grey jacket remains casually draped over one forearm, conveying the feeling of an exclusive international journey.

Photography:
Ultra-photorealistic. DSLR quality. 85mm lens. f/2.0. Shallow depth of field. HDR. Cinematic natural lighting. Realistic airport window reflections. Premium color grading. Soft bokeh. Subtle film grain. Razor-sharp facial focus. Highly detailed skin texture. Individually rendered hair strands. Realistic fabric textures. Hyper-realistic lighting. 8K resolution.
```

</details>

<a id="nano-banana-golden-hour-bridge-portrait"></a>
### 悬索桥上的黄金时刻人像

<a href="https://x.com/ZaraIrahh/status/2027672194805874699"><img src="../../previews/nano-banana-golden-hour-bridge-portrait.jpg" width="360"></a>

提示词先具体列出服装和配饰，再写明暖色日落光线方向，并用虚化天际线营造纵深。85mm、浅景深、柔和颗粒等镜头词把画面引向编辑感街拍。

Nano Banana 2 · 文生图 · 出处: [@ZaraIrahh on X](https://x.com/ZaraIrahh/status/2027672194805874699) · 143 赞，统计于 2026-10-28

[`golden-hour`](tags.md#tag-golden-hour) [`portrait`](tags.md#tag-portrait) [`street-photography`](tags.md#tag-street-photography) [`cinematic`](tags.md#tag-cinematic) [`bridge`](tags.md#tag-bridge)

<details><summary><b>提示词</b></summary>

```text
Cinematic golden hour portrait of a stylish young woman standing on a historic suspension bridge with a city skyline in the background. She has sleek brown hair tied in a high ponytail, natural glam makeup, and small elegant stud earrings. She is wearing a dark brown coat with a thick oversized brown scarf wrapped around her neck, and a shoulder bag with a gold chain strap. She gazes into camera with soft smile. Warm sunset light casts a soft amber glow across her face and the wooden bridge walkway. The skyline behind her is softly blurred, urban atmosphere with subtle pedestrian movement. Shot on 85mm lens, shallow depth of field, filmic tones, soft grain, editorial street photography style, photorealistic, high detail, 4K resolution.
```

</details>

<a id="gpt-image-vhs-camcorder-night-car-portrait"></a>
### 九十年代末夜间车内VHS摄像机人像

<a href="https://x.com/saniaspeaks_/status/2064192184698716186"><img src="../../previews/gpt-image-vhs-camcorder-night-car-portrait.jpg" width="360"></a>

叠加色度溢出、跟踪噪点、掉线条纹和带时间戳的REC画面信息等具体模拟瑕疵，再用明确色调锁定调色。结尾的负面清单排除单反、HDR和现代干净质感。

GPT Image 2 · 上传图改图 · 出处: [@saniaspeaks_ on X](https://x.com/saniaspeaks_/status/2064192184698716186) · 142 赞，统计于 2026-10-29

[`vhs`](tags.md#tag-vhs) [`retro`](tags.md#tag-retro) [`night`](tags.md#tag-night) [`portrait`](tags.md#tag-portrait) [`camcorder`](tags.md#tag-camcorder)

<details><summary><b>提示词</b></summary>

```text
Use the attached face as the only identity reference, preserving recognizable facial features and natural asymmetry. Create an authentic late-1990s VHS camcorder scene of a young woman riding in the backseat of a moving car at night, wearing a black off-shoulder top, long windblown dark hair, soft 90s makeup, and a romantic, lonely expression. Warm city lights, neon reflections, and blurred traffic streak past the windows while the dim car interior glows with sodium-vapor streetlight tones. Render as genuine pre-2000s VHS footage with magnetic tape softness, motion blur, scanlines, chroma bleed, focus drift, tape grain, tracking noise, RGB separation, dropout streaks, warped edges, flickering exposure, and a burned-in REC HUD with timestamp, battery icon, SP mode, and tape counter. Vertical 4:5 handheld framing with slight camera tilt, imperfect crop, and nostalgic analog nightlife color grading featuring dirty orange highlights, red neon spill, green-blue shadows, faded blacks, and low contrast. Romantic rediscovered VHS memory from a late-night drive in 1998. Negative: DSLR sharpness, HDR, smartphone look, cinematic grading, ultra-clean skin, influencer aesthetic, crisp digital detail, modern 4K rendering.
```

</details>

<a id="nano-banana-golden-rim-light-black-turtleneck-portrait"></a>
### 黑色背景下的金色轮廓光人像

<a href="https://x.com/Soaima_Ai/status/2064199999135907913"><img src="../../previews/nano-banana-golden-rim-light-black-turtleneck-portrait.jpg" width="360"></a>

提示词把具体的外貌细节和单一主光源叠加起来，用暖金橙色轮廓光穿过发丝，衬在纯黑影棚背景上。漂浮的金色光斑、浅景深和时尚摄影的取景让视觉重点落在发光的头发上。

Nano Banana 2 · 文生图 · 出处: [@Soaima_Ai on X](https://x.com/Soaima_Ai/status/2064199999135907913) · 140 赞，统计于 2026-10-28

[`portrait`](tags.md#tag-portrait) [`rim-lighting`](tags.md#tag-rim-lighting) [`bokeh`](tags.md#tag-bokeh) [`studio`](tags.md#tag-studio) [`fashion`](tags.md#tag-fashion)

<details><summary><b>提示词</b></summary>

```text
A hyper-realistic AI portrait of a beautiful young woman with long voluminous wavy black hair with stunning warm golden-orange rim lighting glowing through the hair, fair porcelain skin, soft hazel-brown eyes with warm eye makeup, soft pink lips with a gentle confident smile, small nose piercing, silver hoop earrings, wearing a black ribbed turtleneck sweater, one hand raised touching her hair gracefully, dramatic pitch black studio background with glowing golden bokeh particles floating in the air, cinematic rim lighting, ultra-realistic, 8K, shallow depth of field, professional fashion portrait photography
```

</details>

<a id="nano-banana-noir-portrait-man-vintage-convertible"></a>
### 老式敞篷车里的黑白男士肖像

<a href="https://x.com/pictsbyai/status/2039256212496163327"><img src="../../previews/nano-banana-noir-portrait-man-vintage-convertible.jpg" width="360"></a>

用结构化 JSON 逐项写明构图、光线、镜头和颗粒，再附上一段简短的自然语言提示，让模型得到精确的摄影控制。浅景深、单一方向光和胶片颗粒营造出黑色电影的杂志质感。

Nano Banana 2 · 文生图 · 出处: [@pictsbyai on X](https://x.com/pictsbyai/status/2039256212496163327) · 140 赞，统计于 2026-10-28

[`black-and-white`](tags.md#tag-black-and-white) [`json-prompt`](tags.md#tag-json-prompt) [`vintage-car`](tags.md#tag-vintage-car) [`editorial`](tags.md#tag-editorial) [`film-grain`](tags.md#tag-film-grain)

<details><summary><b>提示词</b></summary>

```text
{
"metadata": {
"image_type": "photograph",
"primary_purpose": "editorial"
},
"composition": {
"rule_applied": "rule of thirds",
"aspect_ratio": "4:5",
"layout": "layered",
"focal_points": [
"Man's face and intense eyes",
"Left hand resting near the chrome car mirror"
],
"visual_hierarchy": "Eye starts at the subject's face, follows the line of his left arm down to his hand, and reflects back along the glossy car edge",
"balance": "asymmetric"
},
"color_profile": {
"dominant_colors": [
{
"color": "Black",
"hex": "#0a0a0a",
"percentage": "45%",
"role": "background, car exterior, and clothing"
},
{
"color": "Mid-Gray",
"hex": "#5a5a5a",
"percentage": "40%",
"role": "skin tones and blurred background elements"
},
{
"color": "White",
"hex": "#f5f5f5",
"percentage": "15%",
"role": "highlights, car interior, and chrome reflections"
}
],
"color_palette": "monochromatic",
"temperature": "neutral",
"saturation": "black and white",
"contrast": "high contrast"
},
"lighting": {
"type": "natural window/outdoor diffused",
"source_count": "single source",
"direction": "front and slightly top",
"directionality": "highly directional",
"quality": "soft light with dramatic falloff",
"intensity": "moody",
"contrast_ratio": "high contrast (dramatic shadows)",
"mood": "dramatic",
"shadows": {
"type": "soft gradual edges",
"density": "deep black",
"placement": "under chin, right side of face, interior of car",
"length": "medium"
},
"highlights": {
"treatment": "preserved",
"placement": "on forehead, cheekbones, nose bridge, and specular highlights on car chrome"
},
"ambient_fill": "absent",
"light_temperature": "neutral"
},
"technical_specs": {
"medium": "digital photography",
"style": "realistic",
"texture": "grainy",
"sharpness": "tack sharp on subject face",
"grain": "film grain",
"depth_of_field": "shallow",
"perspective": "straight on slightly elevated"
},
"artistic_elements": {
"genre": "portrait",
"influences": [
"Classic Hollywood automotive photography",
"Cinematic noir"
],
"mood": "sophisticated",
"atmosphere": "Brooding, timeless, and elegant cinematic tension",
"visual_style": "clean"
},
"typography": {
"present": false,
"fonts": [],
"placement": "none",
"integration": "none"
},
"subject_analysis": {
"primary_subject": "Adult male, estimated 30s, with short dark hair, trimmed beard, wearing a dark collared shirt. Hair is 2-3 inches on top, styled back with natural volume and texture. Hair texture shows natural imperfections with slight flyaways, individual strands visible against the light, and uneven layering typical of a textured scissor cut. Styling indicates matte product use. Hair part is unrefined, pushed back organically rather than sharply divided.",
"positioning": "center",
"scale": "medium",
"interaction": "interacting with environment",
"facial_expression": {
"mouth": "closed neutral",
"smile_intensity": "no smile",
"eyes": "intense",
"eyebrows": "furrowed",
"overall_emotion": "serious",
"authenticity": "posed"
},
"hands_and_gestures": {
"left_hand": "resting on car door frame, index finger extended lightly touching or pointing near the chrome side mirror",
"right_hand": "not visible",
"finger_positions": "relaxed, index finger slightly extended, remaining fingers softly curled inward",
"finger_interlacing": "none",
"hand_tension": "relaxed",
"interaction": "resting on car exterior",
"naturalness": "deliberately posed"
},
"body_positioning": {
"posture": "sitting",
"angle": "facing camera",
"weight_distribution": "leaning left",
"shoulders": "tilted"
}
},
"background": {
"setting_type": "outdoor",
"spatial_depth": "shallow",
"elements_detailed": [
{
"item": "Vintage convertible car body",
"position": "bottom",
"distance": "foreground",
"size": "dominant",
"condition": "pristine",
"specific_features": "dark glossy paint with sharp reflections"
},
{
"item": "Chrome side mirror",
"position": "center",
"distance": "midground",
"size": "small",
"condition": "pristine",
"specific_features": "highly reflective, bullet-style vintage mirror"
},
{
"item": "Windshield frame",
"position": "left",
"distance": "midground",
"size": "medium",
"condition": "pristine",
"specific_features": "chrome trim"
}
],
"wall_surface": {
"material": "not applicable - outdoor background",
"surface_treatment": "blurred",
"texture": "perfectly smooth bokeh",
"finish": "matte",
"color": "mid-gray",
"color_variation": "gradient",
"features": "out of focus shapes indicating trees or street structures",
"wear_indicators": "none"
},
"floor_surface": {
"material": "asphalt",
"color": "dark gray",
"pattern": "blurred"
},
"objects_catalog": "Vintage convertible automobile, chrome side mirror, windshield trim, light-colored car interior seats",
"background_treatment": "blurred"
},
"generation_parameters": {
"prompts": [
"Black and white cinematic photography, medium shot of a handsome man in his 30s sitting in the driver's seat of a classic vintage convertible car. He is leaning his left arm on the car door, hand relaxed near a chrome side mirror. He has short textured dark hair, trimmed beard, furrowed brows, intense brooding gaze, wearing a dark collared shirt. Shallow depth of field, blurred outdoor background. High contrast, directional soft lighting, deep shadows, fine film grain, editorial fashion style.",
"Vintage Hollywood style portrait, black and white, man in classic car leaning out window, dramatic shadows, sharp focus on face, Leica 50mm, f/2.0."
],
"keywords": [
"black and white",
"cinematic portrait",
"vintage car",
"editorial",
"male model",
"brooding",
"film grain",
"classic automotive"
],
"technical_settings": "50mm lens, f/2.0 aperture for shallow depth of field, 1/250s shutter speed, ISO 400 to introduce natural film grain",
"post_processing": "Black and white conversion with crushed blacks, lifted midtone contrast, and added analog film grain"
}
}
```

</details>

<a id="nano-banana-woman-bikini-hoodie-rooftop-dusk"></a>
### 屋顶露台上身穿黑色比基尼与酒红色卫衣的女子

<a href="https://x.com/dreamydigiarts/status/2108112665818406964"><img src="../../previews/nano-banana-woman-bikini-hoodie-rooftop-dusk.jpg" width="360"></a>

提示词以 JSON 分段描述主体、姿势、镜头和光线，并用 DWPose 与 ZoeDepth 的 ControlNet 权重锁定身体布局与景深。黄金时段侧光配合 35 到 50 毫米镜头，保持体积感与背景分离的真实感。

Nano Banana 2.1 · 文生图 · 出处: [@dreamydigiarts on X](https://x.com/dreamydigiarts/status/2108112665818406964) · 140 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`golden-hour`](tags.md#tag-golden-hour) [`controlnet`](tags.md#tag-controlnet) [`rooftop`](tags.md#tag-rooftop)

<details><summary><b>提示词</b></summary>

```text
{ "subject": { "description": "A young woman with an athletic hourglass figure, featuring a slim waist and wide, prominent hips. She has tanned skin with visible natural texture and fine pores. Her face has sharp features, dark almond-shaped eyes, and well-defined eyebrows. Her hair is dark, sleek, and parted down the middle, tied back in a low style. She is wearing large silver cross-shaped earrings.", "anatomy_fidelity": "Exact preservation of the reference's wide hip-to-waist ratio. The bust volume is significant and naturally weighted, showing clear forward projection and a depth greater than the ribcage. Soft tissue follows gravity naturally within the bikini top. Shoulders are proportional to the torso width, and legs are toned with a visible gap.", "attire": "A black string bikini with a triangular top and high-cut, thin-strap bottoms that sit high on the hips. Over this, she wears an oversized, dark maroon or brownish-red zip-up hoodie, worn open and pushed back off the shoulders to expose her torso and arms." }, "pose": { "description": "Standing front-facing pose with a slight lean. The weight is distributed evenly. Her hands are tucked into the pockets of the oversized hoodie, pulling the fabric slightly forward while the sleeves drape over her arms. Her head is tilted slightly to her right, and she is looking directly into the camera with a neutral, confident gaze.", "posture": "Straight spine with a natural lumbar curve that accentuates the hip flare. Shoulders are relaxed but wide, framed by the bulky hoodie." }, "environment": { "location": "A rooftop or elevated balcony overlooking a coastal area at dusk. In the background, there is a calm blue sea under a sky with soft, scattered clouds. Below the balcony, an urban industrial area or parking lot with some greenery is visible. A spiked palm-like plant is partially visible in the bottom-left foreground.", "depth": "Clear separation between the sharp subject in the foreground and the slightly soft-focus coastal background." }, "camera": { "shot_type": "Medium full shot, framing the subject from the head to the mid-thigh.", "angle": "Eye-level, straight-on perspective.", "lens_characteristics": "Standard focal length (approx. 35-50mm) to avoid distortion while maintaining a realistic sense of depth and body volume." }, "lighting": { "type": "Golden hour natural light.", "direction": "Side-lit from the right, creating warm highlights on her skin and the left side of her face/body, while casting soft, natural shadows on the opposite side. The light enhances the three-dimensional volume of her torso and bust.", "temperature": "Warm, orange-gold tones." }, "mood_and_expression": { "expression": "Sultry and composed; a neutral, direct gaze with relaxed lips.", "atmosphere": "Serene, stylish, and high-end lifestyle aesthetic." }, "style_and_realism": { "type": "Photorealistic digital photography.", "details": "High fidelity to skin imperfections, fabric texture of the cotton hoodie, and the subtle sheen on the bikini material. No airbrushing or artificial smoothing." }, "colors_and_tone": { "palette": "Dominant tones of deep maroon, black, and warm tan skin, contrasted against the cool blue of the ocean and the pale orange/blue of the sunset sky.", "contrast": "Medium-high contrast with rich shadows." }, "quality_and_technical_details": { "resolution": "4K, highly detailed, sharp focus on the subject, natural film grain, realistic subsurface scattering on skin.", "sampling": "High-step count for texture preservation." }, "aspect_ratio_and_output": { "ratio": "16:9" }, "controlnet": { "pose_control": { "model_type": "DWPose", "purpose": "Exact skeletal and pose lock", "constraints": [ "preserve shoulder width", "preserve hip angle", "preserve spine curvature", "preserve limb placement" ], "recommended_weight": 1.0 }, "depth_control": { "model_type": "ZoeDepth", "purpose": "Depth, volume, and camera-to-body spatial lock", "constraints": [ "preserve chest foreground dominance", "prevent flat or compressed depth", "maintain clear torso-to-background separation" ], "recommended_weight": 0.8 } }, "negative_prompt": { "forbidden_elements": [ "anatomy normalization", "body proportion averaging", "smaller bust than reference", "reduced chest volume", "flattened or compressed breasts", "tightened, lifted, or artificially supported breasts", "slimmed torso", "aesthetic proportion correction", "beauty standard enforcement", "dataset-average female anatomy", "camera angles that reduce volume", "wide-angle distortion not in reference", "lens compression not in reference", "cropping that removes volume", "depth flattening", "mirror selfies", "phone-in-hand selfies", "reflections", "beautification filters", "skin smoothing", "plastic skin", "airbrushed texture", "stylized realism", "editorial fashion proportions", "more realistic reinterpretation", "naturalization of prominent features" ] }
```

</details>

<a id="nano-banana-seated-cap-hoodie-studio-portrait"></a>
### 戴棒球帽的男子坐在白色方块上

<a href="https://x.com/frametheory058/status/2037368955548152058"><img src="../../previews/nano-banana-seated-cap-hoodie-studio-portrait.jpg" width="360"></a>

通过参考图锁定人物身份，并把姿势、布光、镜头和服装拆分为独立的 JSON 字段，便于单独调整每一部分。负面提示词针对手部畸形和塑料感皮肤等常见人像问题。

Nano Banana 2 · 上传图改图 · 出处: [@frametheory058 on X](https://x.com/frametheory058/status/2037368955548152058) · 138 赞，统计于 2026-10-29

[`json-prompt`](tags.md#tag-json-prompt) [`reference-image`](tags.md#tag-reference-image) [`studio-portrait`](tags.md#tag-studio-portrait)

<details><summary><b>提示词</b></summary>

```text
{
  "Ultra-realistic studio portrait of the same man (strictly use provided reference image for identity consistency). Preserve exact facial structure, proportions, skin texture, hairstyle, and overall likeness with high fidelity. The subject is seated on a clean white block, legs slightly apart, leaning forward in a relaxed yet confident pose. Right elbow rests on the knee with the right hand lightly adjusting black sunglasses, left hand relaxed naturally on the thigh. Outfit includes a black cap, black sunglasses, a clean white hoodie with a subtle logo, light blue fitted jeans, crisp white sneakers, and a black wristwatch. Styling is modern, minimal, and polished with natural fabric behavior and realistic folds.",

  "style": {
    "photography_type": "studio fashion portrait",
    "aesthetic": "clean, minimal, premium lifestyle",
    "mood": "confident, relaxed, modern",
    "color_palette": ["pastel blue", "white", "soft neutrals"]
  },

  "environment": {
    "background": "clean pastel blue and white geometric studio backdrop",
    "props": "single white block only",
    "scene_cleanliness": "minimal, distraction-free, polished"
  },

  "lighting": {
    "setup": "soft diffused studio lighting",
    "quality": "even illumination with gentle falloff",
    "shadows": "minimal, soft, natural contact shadows only",
    "highlights": "controlled, soft highlights with no harsh glare"
  },

  "camera": {
    "lens": "50mm prime",
    "aperture": "f/4 for balanced depth of field",
    "angle": "slightly low eye-level for subtle dominance",
    "framing": "medium full-body (seated), centered composition",
    "focus": "tack sharp on face and upper body"
  },

  "composition": {
    "subject_position": "centered",
    "pose_details": [
      "legs apart seated stance",
      "forward lean for engagement",
      "right hand interacting with sunglasses",
      "left hand relaxed on thigh"
    ],
    "balance": "symmetrical with slight dynamic tilt from pose"
  },

  "identity_lock": {
    "priority": "very high",
    "requirements": [
      "accurate facial features",
      "consistent hairstyle",
      "natural skin texture (no plastic smoothing)",
      "correct proportions and anatomy"
    ]
  },

  "quality": {
    "resolution": "8K",
    "detail_level": "ultra high",
    "rendering": "photorealistic",
    "sharpness": "high micro-detail clarity"
  },

  "negative_prompt": [
    "face distortion",
    "identity mismatch",
    "extra or missing fingers",
    "bad anatomy",
    "blurry image",
    "low resolution",
    "overexposed highlights",
    "harsh shadows",
    "cinematic lighting",
    "messy background",
    "noise or grain",
    "text artifacts",
    "watermark",
    "logo distortion",
    "plastic skin",
    "unnatural fabric folds"
  ]
}
```

</details>

<a id="nano-banana-spinning-night-portrait-slow-shutter-blur"></a>
### 夜间街头旋转人像，慢快门动态模糊

<a href="https://x.com/MissDelulu9/status/2111012827213471883"><img src="../../previews/nano-banana-spinning-night-portrait-slow-shutter-blur.jpg" width="360"></a>

直接写明快门速度 1/8 到 1/15 秒，并列出对应的画面效果：残影拖尾、横向背景拉丝、双重曝光。结尾用排除句（不要冻结动作、不要清晰的手臂和头发），避免模型把动作拍定格。

Nano Banana 2.1 · 文生图 · 出处: [@MissDelulu9 on X](https://x.com/MissDelulu9/status/2111012827213471883) · 137 赞，统计于 2026-10-28

[`motion-blur`](tags.md#tag-motion-blur) [`slow-shutter`](tags.md#tag-slow-shutter) [`film-grain`](tags.md#tag-film-grain) [`night`](tags.md#tag-night) [`fashion`](tags.md#tag-fashion)

<details><summary><b>提示词</b></summary>

```text
Vertical 9:16 candid fashion portrait of a
beautiful East Asian girl wearing a fitted long-sleeve orange turtleneck and a black mini skirt, with long, messy, loose black hair. She spins rapidly while looking back at the camera, arms spread wide and hair flying. VERY SLOW SHUTTER SPEED 1/8–1/15 sec, extreme realistic motion blur, long ghost trails on arms and hair, blurred body, softly recognizable face, horizontal background streaks, camera shake, double-exposure effect, heavy 35mm film grain, dreamy, moody, underexposed, photorealistic. No CGI, no frozen motion, no sharp arms or hair.
```

</details>

<a id="nano-banana-cream-suit-dark-studio-portrait"></a>
### 黑色背景下的奶油色西装棚拍人像

<a href="https://x.com/iamsofiaijaz/status/2038838879852376336"><img src="../../previews/nano-banana-cream-suit-dark-studio-portrait.jpg" width="360"></a>

提示词写明面料、镶边颜色和手部动作，让西装质感与姿势准确呈现。85mm、浅景深和深色极简背景等镜头与光线用语带出杂志大片的质感。

Nano Banana 2 · 文生图 · 出处: [@iamsofiaijaz on X](https://x.com/iamsofiaijaz/status/2038838879852376336) · 136 赞，统计于 2026-10-28

[`fashion`](tags.md#tag-fashion) [`studio-portrait`](tags.md#tag-studio-portrait) [`editorial`](tags.md#tag-editorial) [`suit`](tags.md#tag-suit) [`low-key`](tags.md#tag-low-key)

<details><summary><b>提示词</b></summary>

```text
A cinematic portrait of a handsome young man with neatly styled brown hair and light stubble, wearing a cream-colored tailored suit with subtle gold trim details, paired with a black dress shirt and black tie. He is adjusting his jacket with one hand, wearing a luxury wristwatch. The background is dark and minimal, creating a dramatic contrast. Soft studio lighting highlights his face and the texture of the suit, with a moody, elegant, high-fashion editorial style. Ultra-realistic, sharp focus, shallow depth of field, 85mm lens, professional photography, luxury aesthetic, high contrast, warm tones.
```

</details>

<a id="nano-banana-warm-mirror-selfie-mirrorless-camera-portrait"></a>
### 手持无反相机的暖色镜前自拍人像

<a href="https://x.com/AIwithSarah_/status/2046180588886114701"><img src="../../previews/nano-banana-warm-mirror-selfie-mirrorless-camera-portrait.jpg" width="360"></a>

提示词把人像拆成取景、姿势、发型、妆容、场景和光线几个独立段落，便于分别控制。暖黄橙光线、奶油色虚化背景，加上结尾的保持面部不变，让人物一致且氛围温馨。

Nano Banana 2 · 上传图改图 · 出处: [@AIwithSarah_ on X](https://x.com/AIwithSarah_/status/2046180588886114701) · 133 赞，统计于 2026-10-28

[`mirror-selfie`](tags.md#tag-mirror-selfie) [`portrait`](tags.md#tag-portrait) [`warm-light`](tags.md#tag-warm-light) [`face-preserve`](tags.md#tag-face-preserve) [`shallow-depth-of-field`](tags.md#tag-shallow-depth-of-field)

<details><summary><b>提示词</b></summary>

```text
Nano Banana 2 on Higgsfield.

Prompt: A portrait of a young woman with a soft, natural expression, half-body close-up (shoulders up), side angle pose. Her head is slightly tilted to the right, looking at the camera with a subtle smile. She is taking a mirror selfie, holding a mirrorless camera in front of her face. Her hair partially covers one side of her face, giving a candid, relaxed feel.
She wears a fitted dusty pink / soft peach t-shirt, minimal and casual with no accessories.
Short shoulder-length bob haircut, slightly voluminous and naturally messy, soft and shiny texture, loosely parted, some strands covering one side of the face (only one side visible), natural black or dark brown hair.
Natural clean makeup look: light base, smooth glowing skin, soft peach/pink blush, natural pink lips (soft tint), minimal eye makeup, no bold eyeliner, fresh and youthful appearance.
Indoor setting, likely a bedroom or small studio, mirror selfie composition, minimal props. Background is plain beige / warm cream, softly blurred (shallow depth of field), clean and uncluttered.
Warm lighting (yellow/orange tones), soft light (indoor or sunset), gentle shadows, soft highlights on skin, cozy and intimate mood. Do not change the face.
```

</details>

<a id="nano-banana-candid-athleisure-smoothie-la-street"></a>
### 身穿橄榄绿运动套装、手拿绿色奶昔的街头抓拍

<a href="https://x.com/astronomerozge1/status/2045415777197518948"><img src="../../previews/nano-banana-candid-athleisure-smoothie-la-street.jpg" width="360"></a>

用结构化 JSON 把主体、场景、姿态、镜头和质感分块描述，并以参考图锁定人物身份。50mm 镜头、略偏离中心的机位和行走中的姿态带来抓拍感，负面清单保证背景干净。

Nano Banana 2 · 上传图改图 · 出处: [@astronomerozge1 on X](https://x.com/astronomerozge1/status/2045415777197518948) · 132 赞，统计于 2026-10-29

[`json-prompt`](tags.md#tag-json-prompt) [`candid`](tags.md#tag-candid) [`athleisure`](tags.md#tag-athleisure) [`reference-identity`](tags.md#tag-reference-identity) [`street-photo`](tags.md#tag-street-photo)

<details><summary><b>提示词</b></summary>

```text
{
  "generation_request": {
    "meta_data": {
      "tool": "Nano Banana 2",
      "task_type": "erewhon_wellness_luxury_candid",
      "language": "en",
      "priority": "highest",
      "version": "v2.0_LA_CLEAN_GIRL_LUXURY"
    },

    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "very_high",
      "preserve_identity": true,
      "notes": "Use the reference woman. Scene set outside Erewhon Market in Los Angeles. She exits holding a smoothie in a natural candid moment. The vibe is paparazzi-meets-editorial. She is not posing directly, caught mid-walk with confident effortless energy."
    },

    "output_settings": {
      "aspect_ratio": "4:5",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "luxury_wellness_editorial",
      "sharpness": "ultra_crisp",
      "dynamic_range": "clean_bright_daylight",
      "color_grade": "neutral_beige_green_wellness"
    },

    "subject": {
      "identity": "reference woman",
      "expression": "neutral confident face, slightly detached, cool-girl energy",
      "hair": "sleek high ponytail or slick bun, ultra clean finish",
      "makeup": "no-makeup makeup, dewy skin, subtle glow, natural lips",
      "outfit": "ultra premium fitted athleisure set (sculpting leggings + cropped top), neutral tones like beige, olive or soft grey",
      "accessories": "designer sunglasses, minimalist tote bag, smoothie cup",
      "body": "perfect anatomy, natural walking posture"
    },

    "scene": {
      "environment": "Erewhon Market exterior with clean modern facade, glass, greenery",
      "lighting": "bright soft California daylight, no harsh shadows",
      "mood": "clean, elite, wellness-focused, understated luxury"
    },

    "pose_language": {
      "pose": "mid-step walking out of store, one arm holding smoothie, other relaxed",
      "hands": "natural grip, relaxed fingers",
      "posture": "confident, straight, effortless"
    },

    "camera": {
      "lens": "50mm lifestyle lens",
      "angle": "slightly off-center candid angle",
      "framing": "mid-full body",
      "focus": "sharp subject, lightly blurred background",
      "depth_of_field": "moderately shallow"
    },

    "texture_details": {
      "skin_texture": "natural dewy skin with realistic pores",
      "fabric_texture": "tight athletic fabric with subtle stretch and sheen",
      "hair_texture": "clean sleek strands, controlled finish"
    },

    "color_grading": {
      "palette": "beige, soft greens, whites, clean neutral tones",
      "style": "minimal luxury wellness aesthetic"
    },

    "must_have": [
      "Erewhon style setting",
      "smoothie",
      "athleisure luxury",
      "clean girl aesthetic",
      "same identity",
      "perfect anatomy",
      "no text"
    ],

    "negative_prompt": [
      "messy background",
      "fast food setting",
      "heavy glam makeup",
      "cheap outfit",
      "bad anatomy",
      "extra fingers",
      "over-posed",
      "text",
      "logo",
      "watermark"
    ]
  }
}
```

</details>

<a id="gpt-image-hanbok-pink-pigment-explosion-portrait"></a>
### 粉色韩服化作爆散的颜料烟云

<a href="https://x.com/TaliaAariz/status/2091027170827116570"><img src="../../previews/gpt-image-hanbok-pink-pigment-explosion-portrait.jpg" width="360"></a>

把变化描述为物理过程，即衣料化作有明确方向的颜料云，让爆散动势在纯灰背景上清晰可读。保留脸部身份的要求使人脸保持稳定，其余描述则可以放手发挥戏剧感。

GPT Image 2 · 上传图改图 · 出处: [@TaliaAariz on X](https://x.com/TaliaAariz/status/2091027170827116570) · 130 赞，统计于 2026-10-29

[`hanbok`](tags.md#tag-hanbok) [`pigment-explosion`](tags.md#tag-pigment-explosion) [`fashion-portrait`](tags.md#tag-fashion-portrait) [`motion-transformation`](tags.md#tag-motion-transformation)

<details><summary><b>提示词</b></summary>

```text
Create an ultra-photorealistic Korean high-fashion studio portrait, full body, wearing an elegant pastel pink hanbok, long black hair with delicate flower ornaments on both sides. The hanbok physically transforms into enormous dense pastel pink pigment clouds exploding dramatically toward the right side. Preserve my exact face and identity. Medium grey studio background, cinematic softbox lighting, high-speed fashion photography, extreme detail, photorealistic, vertical 9:16."
```

</details>

<a id="nano-banana-bw-vogue-hard-light-portrait"></a>
### 硬侧光黑白时尚编辑人像

<a href="https://x.com/MissDelulu9/status/2113862505504407630"><img src="../../previews/nano-banana-bw-vogue-hard-light-portrait.jpg" width="360"></a>

先写姿态、发型和服装，再用硬侧光、明暗对比和暗背景锁定画面氛围。85mm、浅景深和胶片颗粒等镜头词让眼睛和皮肤保持锐利真实。

Nano Banana 2.1 · 文生图 · 出处: [@MissDelulu9 on X](https://x.com/MissDelulu9/status/2113862505504407630) · 126 赞，统计于 2026-10-29

[`black-and-white`](tags.md#tag-black-and-white) [`editorial`](tags.md#tag-editorial) [`chiaroscuro`](tags.md#tag-chiaroscuro) [`hard-light`](tags.md#tag-hard-light) [`fashion`](tags.md#tag-fashion)

<details><summary><b>提示词</b></summary>

```text
Ultra-realistic cinematic black-and-white Vogue editorial portrait of a beautiful Japanese woman. Three-quarter profile pose, shoulders turned away from the camera, head gently tilted upward and looking off-frame with a calm, dreamy expression and softly parted lips. Long, naturally wavy black hair with loose strands flowing across the face. Elegant off-shoulder white satin blouse, delicate sparkling earrings.

Dramatic hard side lighting casting bold diagonal shadows across the eyes and face, high-contrast chiaroscuro, minimal dark studio background. 85mm lens, shallow depth of field, razor-sharp eyes, hyper-detailed natural skin texture, subtle film grain, luxury fashion photography, timeless editorial aesthetic, ultra-photorealistic, 8K.
```

</details>

<a id="nano-banana-human-cat-shared-face-closeup"></a>
### 人脸与猫脸共享同一画面

<a href="https://x.com/Ozayrr_irl/status/2061332108967293372"><img src="../../previews/nano-banana-human-cat-shared-face-closeup.jpg" width="360"></a>

上传参考图锁定人物身份，再用精确的构图描述（竖版9:20特写，人眼与猫眼居中且位于同一焦平面）让两张脸平分画面。明确写出构图与对焦平面，是保证两张脸都清晰对齐的关键。

Nano Banana 2 · 上传图改图 · 出处: [@Ozayrr_irl on X](https://x.com/Ozayrr_irl/status/2061332108967293372) · 126 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`cat`](tags.md#tag-cat) [`reference-image`](tags.md#tag-reference-image) [`split-face`](tags.md#tag-split-face)

<details><summary><b>提示词</b></summary>

```text
[Upload your reference image and write this]
Use the exact same face from the reference image and generate a  photorealistic colour photo, vertical 9:20, extreme close up.
Half of a human face and half of my pet's face pressed closely together, and sharing the same frame equally. Faces are very close to the camera, and intimate contact. Tight crop, one human eye + one cat eye centered, perfectly aligned and both in sharp focus with the same intimate framing. Frame tightly filled with face, background barely visible.
```

</details>

<a id="gpt-image-sunlit-roadside-selfie-blue-sunglasses"></a>
### 阳光下路边自拍，蓝色墨镜与金色耳环

<a href="https://x.com/saniaspeaks_/status/2063952729689735634"><img src="../../previews/gpt-image-sunlit-roadside-selfie-blue-sunglasses.jpg" width="360"></a>

开头用人脸锁定指令，指明参考照片并列出需要保留的五官特征，再用明确的镜头和光线参数固定姿势、构图与光线。负面提示词排除动漫、CGI 和塑料皮肤等失真风格。

GPT Image 2 · 上传图改图 · 出处: [@saniaspeaks_ on X](https://x.com/saniaspeaks_/status/2063952729689735634) · 124 赞，统计于 2026-10-29

[`face-lock`](tags.md#tag-face-lock) [`street-fashion`](tags.md#tag-street-fashion) [`selfie`](tags.md#tag-selfie) [`portrait`](tags.md#tag-portrait)

<details><summary><b>提示词</b></summary>

```text
Edit the provided image using my uploaded face photo as the only facial identity reference with strict face-lock preservation (99–100% similarity). Keep the exact same eyes, eyebrows, eyelids, nose, lips, jawline, cheekbones, forehead, skin tone, ethnicity, age appearance, facial proportions, and natural skin texture with zero identity drift or beautification. Create an ultra-photorealistic DSLR luxury street-fashion portrait of a 23-year-old woman with a subtle teasing smirk, direct eye contact, glossy Korean-Douyin makeup, visible pores, realistic skin texture, messy high bun with loose wind-blown strands, oversized pastel-blue sunglasses, large textured gold earrings, gold bracelet, rings, decorative manicure, and an oversized designer silk shirt in light blue, ivory, and caramel monogram tones. Match the reference pose exactly: close-up selfie, one hand raised above the forehead blocking sunlight, head slightly tilted, centered vertical composition, tight upper-body crop. Outdoor urban roadside setting with blue sky, clouds, parked buses, distant vehicles, and bright afternoon sunlight creating natural shadows and glossy highlights. Professional DSLR 50mm RAW photography, HDR, ultra-sharp facial detail, realistic hair strands, fabric texture, jewelry reflections, modern Korean fashion editorial color grading, vibrant outdoor tones, luxury campaign quality, 8K realism. Negative prompt: anime, manga, cartoon, illustration, CGI, 3D render, plastic skin, beauty filters, face redesign, identity blending, hijab, flowers, gardens, forests, indoor studio, bob haircut, long curls, blurred face, oversmoothed skin, deformed hands, extra fingers, watermark, logo, text, low quality. --ar 3:4 --style raw --quality high
```

</details>

<a id="nano-banana-driver-aston-martin-golden-sunlight"></a>
### 戴墨镜的男子驾驶阿斯顿马丁内饰

<a href="https://x.com/pictsbyai/status/2050852588833132762"><img src="../../previews/nano-banana-driver-aston-martin-golden-sunlight.jpg" width="360"></a>

单一硬质定向光从左前方车窗射入，提示词逐一指定面部与方向盘哪些部位受光、哪些落入阴影，形成强对比。写明全画幅机身、35mm 镜头、光圈、快门和 ISO，让画面具有清晰的摄影质感。

Nano Banana 2 · 文生图 · 出处: [@pictsbyai on X](https://x.com/pictsbyai/status/2050852588833132762) · 124 赞，统计于 2026-10-29

[`golden-hour`](tags.md#tag-golden-hour) [`automotive`](tags.md#tag-automotive) [`lighting`](tags.md#tag-lighting) [`lifestyle`](tags.md#tag-lifestyle)

<details><summary><b>提示词</b></summary>

```text
A male in his 30s sits in profile as the primary subject, his relaxed shoulders carrying a serious, posed expression while his eyes remain hidden behind black sunglasses, focused straight ahead with a neutral, unsmiling mouth. He wears a crisp off-white long-sleeve shirt and a watch with a brown leather strap. His hair is styled in a textured quiff with moderate volume lifting off the forehead, fading down to a half-inch on the sides above the ears, displaying a natural slight wave on top enhanced by a dry-look matte paste; meticulous details reveal slightly uneven natural growth at the hairline, textural inconsistency near the crown, and visible flyaways illuminated by the sun, complemented by a short, even stubble beard of three to four days of growth with natural cheek lines. His hands naturally interact with the environment; his left hand grips the steering wheel rim near the ten o'clock position with the thumb resting seamlessly along the inner seam, while his right hand grips the top right at the two o'clock position, his fingers curled tightly over the leather rim with slightly prominent knuckles that maintain an organic tension without turning white. He is positioned within the pristine interior of an Aston Martin, observed from an isometric perspective from the passenger seat. In the foreground, a pristine gloss black center console houses glass-like gear selector buttons and climate controls featuring subtly integrated medium-weight sans-serif technical typography. The midground is dominated by the steering wheel wrapped in saddle brown leather with visible stitching, a matte black center, and a silver winged logo, situated beneath a new black alcantara suede sun visor bearing a yellow and white airbag warning label. The surrounding interior panels and seat bolsters are constructed from matte saddle brown and black leather mixed with carbon fiber, detailed with uniform diamond quilted stitching. Through the window, the medium-depth background transitions into smoothly blurred but distinct, thriving dense green evergreen bushes and trees. A bright, hard, and highly directional natural golden sunlight streams in from the front-left driver window, bathing the scene in a warm, energetic, and sophisticated atmosphere. This single-source lighting generates extreme high contrast, casting harsh, defined, deep black shadows across the right side of the driver's face and the right side of the center console, while brilliant highlights are perfectly preserved on his left cheek, nose, left forearm, and the top arc of the steering wheel. The scene leverages an earthy and analogous color palette heavily featuring saddle brown, off-white, and black, punctuated by the cool forest green contrast of the exterior. Captured as a tack-sharp piece of digital lifestyle photography using a full-frame camera with a 35mm lens set to an f/4.0 aperture, 1/1000s shutter speed, and ISO 100, freezing the motion with absolute clarity on the subject. Inspired by clean, luxury automotive influencer aesthetics, the image undergoes precise post-processing with enhanced contrast to deepen the shadows on the interior console, warm color grading to emphasize the leather and golden light, and is finally framed in a 4:5 aspect ratio.
```

</details>

<a id="nano-banana-gothic-vampire-foggy-alley-portrait"></a>
### 雾巷石墙边的哥特吸血鬼女子

<a href="https://x.com/The_Kremlinn/status/2054418680692228271"><img src="../../previews/nano-banana-gothic-vampire-foggy-alley-portrait.jpg" width="360"></a>

场景段落把具体的环境细节（湿砖墙、路灯倒影、体积雾）和35mm胶片感、颗粒、浅景深等电影术语叠在一起，得到电影感恐怖静帧。再加上从靴子升到眼睛的镜头路径和微笑、獠牙、低语、渐黑的节拍描述，可以顺势扩展成视频。

Nano Banana 2 · 文生图 · 出处: [@The_Kremlinn on X](https://x.com/The_Kremlinn/status/2054418680692228271) · 124 赞，统计于 2026-10-28

[`vampire`](tags.md#tag-vampire) [`gothic`](tags.md#tag-gothic) [`cinematic`](tags.md#tag-cinematic) [`fog`](tags.md#tag-fog) [`horror`](tags.md#tag-horror)

<details><summary><b>提示词</b></summary>

```text
Dark gothic alley at night, wet brick wall and rain-soaked pavement reflecting a dim street lamp. Heavy fog drifts slowly through the alley. A pale elegant vampire woman in a long black coat and dark red dress leans against the wall, motionless and mysterious. Cinematic horror lighting, dramatic shadows, shallow depth of field, ultra-realistic, 35mm film look, film grain, volumetric fog.
The camera begins at her black leather boots and performs a slow cinematic vertical dolly shot upward, moving smoothly from her feet → legs → waist → shoulders → lips → eyes. Suspense builds as the camera rises.
When the camera reaches her face, she slowly tilts her head and gives a cold villain smile. Her long sharp vampire fangs slide into view, fresh blood dripping slowly from the tips. Her eyes glow subtly in the darkness.
She whispers softly: “Welcome to the night…”
Immediately after, she lets out a quiet sinister villain laugh as the fog thickens and the lighting darkens.
The scene begins to slowly fade to black, while the camera continues pushing forward into an extreme close-up, zooming closer and closer until the camera enters her mouth, ending in darkness.
Style keywords: cinematic horror, gothic vampire, slow camera movement, dramatic lighting, suspenseful, photorealistic, moody atmosphere, shallow depth of field, film grain, volumetric fog.
```

</details>

<a id="nano-banana-color-block-fashion-high-angle-reaching-hand"></a>
### 撞色时装人像与伸向镜头的手

<a href="https://x.com/alizagori1/status/2078375640416313479"><img src="../../previews/nano-banana-color-block-fashion-high-angle-reaching-hand.jpg" width="360"></a>

俯拍广角加上伸向镜头的手,形成强烈的透视夸张效果。纯白无缝背景、明亮均匀的影棚光和明确的 24mm 镜头参数,让撞色服装成为画面重点。

Nano Banana 2 · 文生图 · 出处: [@alizagori1 on X](https://x.com/alizagori1/status/2078375640416313479) · 123 赞，统计于 2026-10-28

[`fashion`](tags.md#tag-fashion) [`editorial`](tags.md#tag-editorial) [`wide-angle`](tags.md#tag-wide-angle) [`studio-lighting`](tags.md#tag-studio-lighting) [`forced-perspective`](tags.md#tag-forced-perspective)

<details><summary><b>提示词</b></summary>

```text
Made with Gemini Nano Banana 2 on
@Lart_AI
.

Model: Gemini Nano Banana 2
Aspect Ratio: 9:16
Resolution: 2K

Prompt: Ultra-realistic, high-fashion editorial portrait of a stylish young model captured from a dramatic bird's-eye wide-angle perspective, reaching one hand toward the camera to create an exaggerated perspective effect. Vibrant color-block outfit with modern accessories, clean white seamless studio background, high-key studio lighting, playful Gen Z aesthetic, confident expression, commercial fashion photography, ultra-detailed skin texture, sharp focus, premium styling, 8K, HDR, magazine cover quality, DSLR, 24mm wide-angle lens, f/2.8, crisp details, natural colors.
Negative Prompt: Low quality, blurry, noisy, overexposed, underexposed, distorted anatomy, extra fingers, deformed hands, duplicate limbs, bad proportions, cropped, watermark, text, logo, artifacts, motion blur, oversaturated, cartoon, CGI, low resolution.
Settings: SDXL, DPM++ 2M Karras, Steps: 30, CFG: 7, Aspect Ratio: 4:5.
```

</details>

<a id="gpt-image-charcoal-sketch-wall-seated-portrait"></a>
### 巨幅炭笔素描前坐着的真人女性肖像

<a href="https://x.com/Kubra_286/status/2102597090534649952"><img src="../../previews/gpt-image-charcoal-sketch-wall-seated-portrait.jpg" width="360"></a>

同一张脸的棕褐色炭笔素描铺满墙面，前景是全彩写实坐姿人像，单色与全彩的对比拉开层次。用一整段身份锁定加明确的禁止条目，让素描和真人保持同一张脸。

GPT Image 2.5 · 上传图改图 · 出处: [@Kubra_286 on X](https://x.com/Kubra_286/status/2102597090534649952) · 122 赞，统计于 2026-10-29

[`charcoal-sketch`](tags.md#tag-charcoal-sketch) [`layered-composite`](tags.md#tag-layered-composite) [`identity-lock`](tags.md#tag-identity-lock) [`editorial-portrait`](tags.md#tag-editorial-portrait)

<details><summary><b>提示词</b></summary>

```text
Create a layered composite portrait of the SAME FEMALE PERSON from the uploaded face reference image.

CONCEPT:
A massive, highly detailed charcoal/pencil sketch portrait fills the background like a hand-drawn wall mural, while a sharp full-color photorealistic seated portrait of the same woman appears in the foreground on a dark reflective floor.

BACKGROUND SKETCH PORTRAIT:
Large detailed black-and-white pencil and charcoal sketch of the same woman, head turned slightly to the side. Preserve her exact hairstyle and hair texture, facial features, eyebrows, eyes, nose, lips, jawline and natural facial proportions. The sketch should have visible pencil hatch strokes, charcoal shading, fine facial linework and realistic hand-drawn texture. Add rough torn-paper edges, ink-splatter marks and charcoal dust surrounding the sketch, blending naturally into a warm sepia-grey textured wall.

FOREGROUND FEMALE SUBJECT:
The same woman is seated casually on the floor. One leg is bent with the knee raised and one forearm resting naturally on the knee; the other leg extends outward to the side. Her torso is slightly turned, head tilted while looking off to the side, with a calm, thoughtful and natural expression.

IDENTITY LOCK — HIGHEST PRIORITY:
Use ONLY the uploaded female face reference image for facial identity and facial structure in BOTH the background sketch and the foreground photorealistic woman.

The foreground woman and background sketch must represent EXACTLY the same real person.

Preserve the exact:

- Face shape
- Jawline and jaw width
- Cheek structure
- Forehead shape
- Exact hairline
- Hairstyle and hair texture
- Eyebrow shape
- Eye shape, size and spacing
- Nose structure
- Lip shape and proportions
- Natural facial features
- Skin tone
- Skin texture
- Natural facial imperfections
- Overall feminine facial proportions

ZERO identity change.

Do NOT beautify or alter the face.
Do NOT change her age or facial structure.
Do NOT feminize or masculinize the face.
Do NOT smooth away natural skin texture.
Do NOT make her look like a celebrity or model.
Do NOT use a generic female face.
Do NOT introduce facial morphing.
Do NOT change her hairstyle or hairline unless required by the reference.
Do NOT create a different person.

The uploaded reference image is the ONLY source of facial identity.

BODY:
Natural feminine body proportions, realistic physique, natural skin tone and relaxed seated posture.

OUTFIT:
Black hooded sweatshirt with visible drawstrings, light grey jogger sweatpants and clean white-and-grey sneakers.

ENVIRONMENT:
Warm sepia-grey textured wall covered by the giant detailed pencil/charcoal portrait. Rough ink-splatter, charcoal dust and expressive pencil marks spread naturally around the sketch. Dark polished reflective floor beneath the seated woman, creating a subtle soft mirror reflection.

COMPOSITION:
Vertical editorial poster composition.
The large background sketch dominates the frame while the full-color seated woman is clearly separated in the foreground.
Strong visual depth between the hand-drawn portrait and realistic subject.
Balanced negative space.
Premium fashion-editorial composition.

LIGHTING:
Soft, even studio lighting from the front.
Minimal harsh shadows.
Warm neutral illumination.
Natural skin highlights.
Subtle controlled reflections on the dark floor.

COLOR GRADING:
Background: sepia-grey monochrome charcoal/pencil aesthetic.
Foreground: natural full-color female subject with realistic warm skin tones.
Strong but elegant contrast between the monochrome sketch and realistic woman.
Clean high-contrast editorial poster color grading.

CAMERA / QUALITY:
Sony A7R IV
50mm lens
f/1.8
Foreground subject tack sharp.
Extremely detailed skin texture, individual hair strands and clothing fabric.
Background pencil strokes, charcoal shading and ink-splatter texture highly detailed.
Ultra-photorealistic.
Premium editorial photography.
Natural depth of field.
Realistic materials and reflections.
4K-level detail.
Zero AI-looking artifacts.

NEGATIVE PROMPT:
No identity change, no different face, no generic female face, no celebrity resemblance, no face-swap artifacts, no facial distortion, no asymmetrical eyes, no extra fingers, no extra limbs, no malformed hands, no duplicated body parts, no plastic skin, no excessive skin smoothing, no beauty filter, no cartoon, no anime, no unrealistic body proportions, no blurry face, no low resolution, no watermark, no text, no logo.

OUTPUT:
Aspect Ratio: 3:4
Photorealistic female portrait
Identity preservation is the absolute highest priority.
```

</details>

<a id="nano-banana-golden-hour-cliff-portrait-ponytail"></a>
### 金色时刻悬崖边的高马尾女性肖像

<a href="https://x.com/Its_shah2i0/status/2071142207697121705"><img src="../../previews/nano-banana-golden-hour-cliff-portrait-ponytail.jpg" width="360"></a>

提示词按固定顺序分层描述：主体、发型、手部与首饰、服装，再到场景和光线，细节具体。用电影感景深和黄金时刻阳光定义画面质感，无需指定相机型号。

Nano Banana 2 · 文生图 · 出处: [@Its_shah2i0 on X](https://x.com/Its_shah2i0/status/2071142207697121705) · 122 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`golden-hour`](tags.md#tag-golden-hour) [`coastal`](tags.md#tag-coastal) [`fashion`](tags.md#tag-fashion)

<details><summary><b>提示词</b></summary>

```text
A stunning, high-fashioned cinematic portrait of a beautiful young woman with a flawless complexion and expressive brown eyes. Her long, rich brown hair is styled in a voluminous, perfectly detailed high ponytail with soft, elegant face-framing strands catching the golden sunlight. She has soft, natural makeup with long lashes and a subtle, thoughtful expression, looking off into the distant horizon away from the camera. Her hands are delicately held together in front of her, showcasing intricately detailed shimmering silver glitter nail art and wearing thin, minimal silver rings on her fingers. She is wearing a modern, chic off-white asymmetric one-shoulder top and a thin silver chain necklace with a small heart pendant. The background features a breathtaking, highly detailed coastal landscape, standing on a rocky cliff overlooking a vast deep-blue ocean with realistic crashing white waves. The scene is illuminated by soft, warm golden hour sunlight, creating beautiful highlights on her hair and a cinematic depth of field with a softly blurred background.
```

</details>

<a id="nano-banana-red-latex-superhero-studio-portrait"></a>
### 红色乳胶超级英雄风棚拍人像，涂鸦墙背景

<a href="https://x.com/KeorUnreal/status/2115436047664287827"><img src="../../previews/nano-banana-red-latex-superhero-studio-portrait.jpg" width="360"></a>

提示词采用结构化 JSON，将主体、服装、场景、灯光和镜头分开描述，各要素不易互相干扰。明确写出涂鸦文字 Keor 的拼写，并描述乳胶的光泽，可以让文字和材质在结果中保持清晰。

Nano Banana 2.1 · 文生图 · 出处: [@KeorUnreal on X](https://x.com/KeorUnreal/status/2115436047664287827) · 122 赞，统计于 2026-10-29

[`json-prompt`](tags.md#tag-json-prompt) [`studio-portrait`](tags.md#tag-studio-portrait) [`latex-outfit`](tags.md#tag-latex-outfit) [`superhero`](tags.md#tag-superhero)

<details><summary><b>提示词</b></summary>

```text
{
 "subject": {
 "description": "Young woman Sadie Sink with fair skin, voluminous curly platinum-white red hair, dramatic eye makeup, looking directly at the camera with a confident expression",
 "hair": "Huge, wavy platinum-white red curls cascading around the shoulders and back",
 "body": "Curvy figure in a form-fitting suit",
 "pose": "Standing facing the camera, both hands on her hips, elbows out",
 "expression": "Bold, direct gaze"
 },
 "outfit": {
 "suit": "Glossy neon red latex full-body suit with a deep neckline and long sleeves",
 "emblem": "Bronze metallic X-shaped emblem on a chain at the chest, small circular emblems on the shoulders",
 "accessories": "Large gold hoop earrings"
 },
 "setting": {
 "location": "Studio with a plain gradient backdrop",
 "background": "Soft white-to-pink gradient wall with a huge gold X sculpture with a stargate inside",
 "added_element": "Graffiti sign reading 'Keor' on the wall in an X-Men superhero style in the backdrop"
 },
 "lighting": {
 "type": "Studio lighting with white and pink rim lights",
 "effects": "Strong glossy highlights on the neon red latex, colorful glow on the white hair"
 },
 "camera": {
 "angle": "Slightly low full-body angle",
 "framing": "Full-body shot, subject centered against the gradient wall",
 "style": "Photorealistic, high-detail fashion photography, sharp focus"
 },
 "additional_details": {
 "skin": "Smooth with a slight sheen",
 "atmosphere": "Bold superhero-inspired studio portrait"
 }
}
```

</details>

<a id="nano-banana-blue-lit-hoodie-portrait"></a>
### 蓝光棚拍中戴琥珀色墨镜的胡须男子

<a href="https://x.com/weiinberg/status/2080518616131469475"><img src="../../previews/nano-banana-blue-lit-hoodie-portrait.jpg" width="360"></a>

用参考图加明确的五官清单锁定主体身份，并以构图参考固定裁切、头部角度和取景。光线分为镜头左侧的蓝色主光和另一侧的中性正面补光，使肤色保持真实。

Nano Banana 2 · 上传图改图 · 出处: [@weiinberg on X](https://x.com/weiinberg/status/2080518616131469475) · 121 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`identity-reference`](tags.md#tag-identity-reference) [`studio-lighting`](tags.md#tag-studio-lighting) [`blue-light`](tags.md#tag-blue-light)

<details><summary><b>提示词</b></summary>

```text
Nano Banana 2 on OpenArt

Prompt: Use the uploaded character image as the sole identity reference for the person in the final photograph. Completely replace the original model with the uploaded reference character while maintaining the reference character's exact face, age range, natural skin tone, facial proportions, forehead, eyebrows, eye shape and eye color, nose, lips, cheekbones, jawline, chin, ears, facial hair pattern, beard density, hairstyle, hairline, hair texture, neck anatomy, shoulders, and recognizable body proportions
ne original model's identity must not remain in any form. Do not blend the two faces. The final subject must accurately and consistently resemble only the uploaded reference character.
Recreate the supplied blue-lit studio portrait scene with the same pose, camera angle, lighting, clothing style, background, crop, and atmosphere.
Create a hyper-realistic 4:5 vertical close-up editorial portrait of the uploaded reference character wearing a black hoodie against a smooth blue-grey studio background.
POSE AND COMPOSITION:
Position the character in a three-quarter portrait angle, with the torso and head turned slightly away from the camera while the eyes look directly toward the lens. Keep the head tilted very subtly, producing a calm, mysterious, confident expression.
Reserve the exact head angle, shoulder orientation, camera height, camera-to-subject distance, crop, facial scale, eye placement, negative space, and overall framing from the composition reference. Frame the character from approximately the upper chest to shoulders upward.
Place the face slightly off-center, with the visible shoulder and hoodie creating depth in the lower portion of the image. Keep the composition intimate and cinematic.
CLOTHING:
Dress the uploaded reference character in a premium plain black hoodie. Preserve the oversized hood structure around the neck, soft matte fabric, black drawstrings, thick neckline folds, relaxed fit, and minimal design. The hoodie must contain no visible logo, print, text,
or neon.
If the uploaded reference character naturally wears a small earring or has a visible ear accessory in the reference image, preserve it accurately. Do not introduce unrelated accessories.
Recreate the cool cinematic lighting from the reference scene.
Use an intense electric-blue light from the camera-left side, illuminating one side of the forehead, eyebrow, eye, cheek, nose, beard, jawline, neck, and hoodie. Use a soft neutral frontal fill light on the opposite side to retain realistic skin color and facial detail.
ad a subtle blue glow on the background behind the illuminated side or the face, gradually fading into a cooler grey-blue tone on the opposite side. Maintain gentle falloff, controlled contrast, soft shadows, natural catchlights, detailed skin texture, and realistic facial hair.
The blue lighting must feel photographic and physically accurate. Avoid excessive neon saturation or artificial plastic skin.
CAMERA AND QUALITY:
Shot with a full-frame professional camera and an 85mm portrait lens, shallow depth of field, sharp focus on the nearest eye, soft background separation, realistic lens compression, detailed pores, natural beard texture, cinematic studio photography, premium fashion editorial aesthetic, realistic color grading, high dynamic range, ultra-photorealistic, 8K resolution.
No text, no logo, no watermark, no identity mixing, no altered hairstyle, no inaccurate beard, no excessive retouching, no unrealistic eye color, no deformed ears, no duplicate accessories, no cartoon or CGI appearance.
```

</details>

<a id="nano-banana-fisheye-vintage-cafe-mirror-selfie"></a>
### 青绿色复古咖啡馆的鱼眼镜面自拍

<a href="https://x.com/TheVirtualMuse/status/2108762311251116034"><img src="../../previews/nano-banana-fisheye-vintage-cafe-mirror-selfie.jpg" width="360"></a>

用身份锁定段落保住参考图人脸，再按场景、背景、光线、相机分段写清各自要求。鱼眼畸变与圆形黄铜镜绑定，并用严格规则约束倒影和单张连续照片，保证真实感。

Nano Banana 2.1 · 上传图改图 · 出处: [@TheVirtualMuse on X](https://x.com/TheVirtualMuse/status/2108762311251116034) · 121 赞，统计于 2026-10-28

[`fisheye`](tags.md#tag-fisheye) [`mirror-selfie`](tags.md#tag-mirror-selfie) [`vintage-film`](tags.md#tag-vintage-film) [`cafe`](tags.md#tag-cafe) [`identity-lock`](tags.md#tag-identity-lock)

<details><summary><b>提示词</b></summary>

```text
Using the uploaded reference image, create an ultra-realistic 1990s vintage café mirror selfie with a playful fisheye photography aesthetic.

IDENTITY LOCK: Preserve the exact facial identity of the reference person with maximum accuracy. Maintain the original eye shape, nose, lips, jawline, facial proportions, natural skin tone, age, and recognizable features. No facial alterations, beautification, or artificial skin smoothing.

SCENE & COMPOSITION: The subject is naturally taking a mirror selfie inside a beautiful vintage European café, standing in front of a large circular mirror with an aged brass frame. Use a strong fisheye lens perspective, creating dramatic yet realistic curvature around the café interior while keeping the subject's face naturally proportioned. The phone must appear correctly reflected in the mirror.

BACKGROUND: A charming retro café featuring turquoise accent walls, vintage wooden furniture, small round café tables, patterned tiled flooring, warm hanging pendant lights, antique decorative details, and soft daylight entering through large windows. The entire interior should curve naturally around the circular mirror.

LIGHTING & COLOR: Authentic 1990s analog film photography, warm golden highlights, slightly faded vintage colors, natural skin tones, soft shadows, subtle 35mm film grain, gentle contrast, and realistic reflections.

CAMERA & REALISM: Strong fisheye wide-angle perspective, authentic mirror reflections, natural handheld selfie composition, realistic optical distortion, detailed skin texture, individual hair strands, accurate fabric textures, and natural imperfections. Premium 8K photographic quality with the organic character of a genuine vintage film photograph.

STRICT RULES: One continuous photograph, no collage, no split screen, no additional people, no distorted facial features, no extra fingers, no incorrect reflections, no CGI, no artificial AI-generated appearance, no readable text, no logos, and no watermark.

FINAL LOOK: A beautiful, effortlessly candid vintage café mirror selfie that looks like a genuine photograph captured on a real fisheye lens, not an AI-generated image.
```

</details>

<a id="nano-banana-pointe-ballerina-butterfly-wing-gown"></a>
### 踮脚芭蕾舞者与蝶翼羽裙

<a href="https://x.com/yourPlugAI/status/2109858986711240822"><img src="../../previews/nano-banana-pointe-ballerina-butterfly-wing-gown.jpg" width="360"></a>

用方括号模板固定主体、姿态、材质和三种配色，同一结构可以换出多种礼服变体。深色舞台地面的倒影加上高反差聚光灯，让羽毛和蝶翼的质感更突出。

Nano Banana 2.1 · 文生图 · 出处: [@yourPlugAI on X](https://x.com/yourPlugAI/status/2109858986711240822) · 120 赞，统计于 2026-10-28

[`ballet`](tags.md#tag-ballet) [`avant-garde-fashion`](tags.md#tag-avant-garde-fashion) [`butterfly`](tags.md#tag-butterfly) [`studio-lighting`](tags.md#tag-studio-lighting) [`template`](tags.md#tag-template)

<details><summary><b>提示词</b></summary>

```text
Full-body studio photograph of a [SUBJECT, e.g., female ballerina / model / dancer] poised in a graceful [POSTURE / ACTION, e.g., en pointe / reaching upward / mid-leap].

She wears an intricate, avant-garde outfit crafted from [PRIMARY MATERIAL / MOTIF, e.g., layered peacock feathers / butterfly wings / botanical petals] featuring [SECONDARY MATERIAL / DETAIL, e.g., delicate lace / fractal filigree / iridescent crystals].

The gown is designed in a striking color palette of [COLOR 1], [COLOR 2], and [COLOR 3] against a dark studio background with soft reflections on a dark stage floor. High-contrast dramatic spotlighting highlights fine textures and details.

📌Variable Guide attached below
```

</details>

<a id="nano-banana-dark-cinematic-skin-detail-portrait"></a>
### 极致皮肤细节的暗调电影感特写人像

<a href="https://x.com/Ozayrr_irl/status/2078676250244354493"><img src="../../previews/nano-banana-dark-cinematic-skin-detail-portrait.jpg" width="360"></a>

先锁定参考图人脸，再规定紧凑裁切、高位侧向单一窄光斑、无补光和一道细边缘光。皮肤按毛孔、胡茬、油光、毛细血管红润和虹膜纤维逐项描述，让侧逆光呈现出质感。

Nano Banana 2 · 上传图改图 · 出处: [@Ozayrr_irl on X](https://x.com/Ozayrr_irl/status/2078676250244354493) · 119 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`close-up`](tags.md#tag-close-up) [`skin-detail`](tags.md#tag-skin-detail) [`dramatic-lighting`](tags.md#tag-dramatic-lighting) [`face-reference`](tags.md#tag-face-reference)

<details><summary><b>提示词</b></summary>

```text
Use the exact same face from the reference image and generate a dark cinematic portrait where obsessive skin detail and dramatic lighting collide into a single devastating image — where every pore becomes a universe and the darkness makes the face feel sacred.

Extreme close-up — face filling 90% of the frame, tight crop from just above the brows to just below the lips, ears dissolving at the edges into darkness. No outfit visible. No distractions. Just the face and the dark consuming everything around it.

Expression carries absolute still weight — eyes open and fully present, staring directly into the lens with a calm devastating intensity that requires no performance. Lips naturally sealed with the faintest natural tension. Every facial muscle completely still — the specific stillness of someone who knows exactly who they are and needs nothing from the world to confirm it.

Skin is the complete obsession — rendered at a level that makes dermatologists lean forward and photographers put down their cameras. Every individual pore with its own unique diameter, depth, shadow and raised wall structure simultaneously visible. Sebaceous filaments as dark pinpoint details across the nose wings and chin. The micro-topography of real skin — hills valleys ridges plateaus all visible as a landscape under raking light. Individual stubble hairs at follicle level — each one with its own emergence angle, thickness tapering from root to glowing tip, its own micro-shadow cast across the surrounding skin. Some hairs just breaking the surface, some fully emerged, some curling slightly — completely individual and real. Natural skin pigmentation variation — micro spots, subtle uneven tone, the biological truth of real skin. The specific oil distribution of real skin — slight natural sheen concentrated at the nose tip center forehead and cupid's bow, more matte at the jaw and temples. Natural capillary flush beneath the skin surface at the cheeks and nose — warmth visible under the skin like embers under ash. Under-eye skin showing its specific delicate thinness, the faint natural shadow of the tear trough. Every eyelash rendered individually with unique length thickness curl spacing and the way they catch the single light source and glow at their tips. Iris at microscopic fiber-pattern level — individual collagen fibers radiating from the pupil, natural color variation within the iris, the limbal ring a precise dark circle, the pupil a deep black with internal dimensional depth. A single sharp catch light in each eye from the key source — small, precise, alive.

Lighting is a single narrow Fresnel spotlight from high above and sharply to one side — the most brutal and revealing light possible, a column of cold white-blue light cutting across the face at a steep diagonal angle. The lit side of the face mercilessly exposed — every pore every follicle every skin surface variation caught by the raking light and made three-dimensional by micro-shadows. The light transition across the nose bridge razor sharp — lit side in brilliant cold detail, shadow side dissolving gradually into absolute black. No fill light anywhere — the shadow side is genuine darkness, total and final, only the faintest ghost of a razor-thin cold rim light from directly behind tracing the ear edge and jaw line with a thread of blue-white light — the only evidence the shadow side of the face exists.

The lit areas of skin catch the cold spotlight with scientific precision — the nose tip the highest highlight point, the forehead plane catching a wide sweep of light, the cheekbone a sharp bright ridge, the upper lip a subtle highlight above the sealed mouth. Every surface variation between these points creating its own micro-shadow under the raking light — the face as a topographic map of human biology.
```

</details>

<a id="gpt-image-1998-coastal-summer-travel-editorial"></a>
### 九十年代末海岛夏日旅行杂志人像

<a href="https://x.com/AIwithWania/status/2098773641303310647"><img src="../../previews/gpt-image-1998-coastal-summer-travel-editorial.jpg" width="360"></a>

先定年代、地域氛围和胶片质感（柯达颗粒、褪色高光、金色阳光），让画面统一成一本旧杂志的拍摄风格。服装、姿态、场景逐项写清，再用排除清单保持自然写实。

GPT Image 2.5 · 文生图 · 出处: [@AIwithWania on X](https://x.com/AIwithWania/status/2098773641303310647) · 118 赞，统计于 2026-10-28

[`travel-editorial`](tags.md#tag-travel-editorial) [`film-photography`](tags.md#tag-film-photography) [`1990s`](tags.md#tag-1990s) [`coastal`](tags.md#tag-coastal) [`fashion`](tags.md#tag-fashion)

<details><summary><b>提示词</b></summary>

```text
Create an ultra-realistic late-1990s summer travel editorial featuring a stylish young woman and a stylish young man in two separate portrait frames with the exact same visual theme and color grading.

The setting is a dreamy coastal destination inspired by Jeju Island and the Greek islands, with crystal-blue sea, rocky coastline, white seaside cafés, flowering plants, distant mountains, small boats, warm wooden furniture, and bright clear summer skies.

The woman is seated naturally at a charming seaside café. She wears a modest but fashionable pastel-blue puff-sleeve blouse with a flowing cream floral midi skirt, elegant minimal jewelry, and a relaxed straw hat. Her outfit must be tasteful and not revealing. Give her soft, slightly wavy shoulder-length hair with natural movement. Her pose should feel spontaneous and stylish—one hand resting lightly near her hat or hair, the other relaxed beside her, with a gentle natural smile.

The man is seated casually in the same coastal atmosphere, wearing a cream linen shirt, relaxed beige trousers, classic sunglasses, minimal wristwatch, and clean white sneakers. Give him naturally messy wavy hair and an effortless vintage European summer look. One arm rests casually on the chair while the other hand is near his face, creating a relaxed editorial pose.

Use warm 1990s film photography, subtle Kodak-style grain, slightly faded highlights, soft golden sunlight, realistic skin texture, gentle shadows, natural imperfections, rich ocean blues, creamy whites, muted pastels, and nostalgic analog color grading.

Make both portraits look like they were photographed for a rare 1998 international summer travel magazine, candid rather than posed, sophisticated but effortless, cinematic yet completely realistic.

No modern influencer look, no heavy makeup, no bold/revealing clothes, no artificial CGI appearance, no plastic skin, no excessive blur, no text or logos.

Vibe: “A forgotten summer somewhere by the sea — 1998.”
```

</details>

<a id="gpt-image-low-angle-selfie-bucket-hat-sky"></a>
### 仰拍自拍，破边渔夫帽配蓝天背景

<a href="https://x.com/Zoyavelle/status/2096105094425240028"><img src="../../previews/gpt-image-low-angle-selfie-bucket-hat-sky.jpg" width="360"></a>

指定仰视机位、逆光形成发丝轮廓光，并把云层集中在画面一侧，构图方向感明确。加入智能手机摄影和不要美颜等限定词，让画面接近随手拍的真实质感。

GPT Image 2 · 文生图 · 出处: [@Zoyavelle on X](https://x.com/Zoyavelle/status/2096105094425240028) · 118 赞，统计于 2026-10-29

[`selfie`](tags.md#tag-selfie) [`portrait`](tags.md#tag-portrait) [`backlight`](tags.md#tag-backlight) [`outdoor`](tags.md#tag-outdoor)

<details><summary><b>提示词</b></summary>

```text
Ultra-realistic high-resolution outdoor selfie portrait of a young adult woman, shot from a low-angle perspective with a smartphone camera. She has long, straight, dark brown hair flowing naturally in the wind, soft natural facial features, smooth realistic skin, subtle pink lips, and a calm neutral expression. She is wearing a black distressed/frayed bucket hat with a small white Nike-style logo on the front, narrow black oval sunglasses with dark reflective lenses, and a light pastel sage-green ribbed tank top with wide straps. Bright sunlight is positioned behind her head, creating a natural glowing rim light and subtle lens flare around her hair and hat. The background is a vivid deep blue summer sky filled with large fluffy white cumulus clouds, with dramatic cloud formations mainly on the right side and scattered clouds near the lower edges. Natural outdoor daylight, realistic skin texture, detailed individual hair strands, authentic smartphone photography, sharp facial details, high dynamic range, balanced exposure, cinematic sunlight, realistic shadows, vibrant but natural colors, slight wide-angle perspective, shallow atmospheric depth, photorealistic, 8K detail, no artificial beauty filter, candid Instagram-style aesthetic. Vertical composition, subject centered and filling most of the frame, low-angle close-up selfie.
```

</details>

<a id="nano-banana-neon-cyberpunk-bearded-man-portrait"></a>
### 粉色墨镜络腮胡男子的霓虹肖像

<a href="https://x.com/Sheldon056/status/2033335996889379057"><img src="../../previews/nano-banana-neon-cyberpunk-bearded-man-portrait.jpg" width="360"></a>

先写明人物、神态和服装，再用青色与洋红色光源在脸上打出强烈明暗。结尾的风格句（赛博朋克风格影棚摄影）定下整体气质，反光镜片则增加了霓虹细节。

Nano Banana 2 · 文生图 · 出处: [@Sheldon056 on X](https://x.com/Sheldon056/status/2033335996889379057) · 117 赞，统计于 2026-10-28

[`portrait`](tags.md#tag-portrait) [`neon`](tags.md#tag-neon) [`cyberpunk`](tags.md#tag-cyberpunk) [`studio-lighting`](tags.md#tag-studio-lighting) [`sunglasses`](tags.md#tag-sunglasses)

<details><summary><b>提示词</b></summary>

```text
Generated with Nano Banana 2 on
@yapper_so
.

Prompt: Create a bold, cinematic portrait 8k ultra HD high details resulation of a confident young man a well groomed beard, looking upward with purpose. He wears vibrant pink sunglasses reflecting neon lights, He wears a black t-shirts. Dramatic lighting in teal and magenta casts bold shadows and highlights across his face. Style: edgy, modern, cyberpunk-inspired studio photography.
```

</details>

<a id="nano-banana-venice-lagoon-suited-man-balustrade"></a>
### 威尼斯泻湖栏杆旁穿西装的男子

<a href="https://x.com/pictsbyai/status/2060272145377235381"><img src="../../previews/nano-banana-venice-lagoon-suited-man-balustrade.jpg" width="360"></a>

为前景、中景和背景的每一层都写明材质与位置，让植物、船只和乔治教堂的位置固定。相机、镜头、光圈、快门和ISO参数，加上指定的青橙调色，共同塑造真实的编辑风格摄影效果。

Nano Banana 2 · 文生图 · 出处: [@pictsbyai on X](https://x.com/pictsbyai/status/2060272145377235381) · 117 赞，统计于 2026-10-29

[`venice`](tags.md#tag-venice) [`portrait`](tags.md#tag-portrait) [`menswear`](tags.md#tag-menswear) [`editorial`](tags.md#tag-editorial)

<details><summary><b>提示词</b></summary>

```text
A handsome young male adult leans casually with shifted weight against a weathered stone balustrade, facing the camera with a candid, serious expression, his dark, messy, wind-swept hair catching the sunlight. His direct gaze, unsmiling neutral mouth, and relaxed neutral eyebrows convey a confident calm. He is dressed in a well-fitted dark charcoal grey suit jacket and matching trousers over a crisp white t-shirt. His relaxed left hand is tucked inside his left trouser pocket, pushing the jacket back slightly to reveal the shirt, while his right arm rests casually at his side, hanging naturally out of frame against his leg. He interacts with an intricate foreground featuring a flat-topped, off-white matte stone balustrade with classical carved pillars showing slight discoloration, patchy warm cream undertones, and weathered water stains, flanked by the stiff, dark green feather-like fronds of a thriving cycad plant extending into the frame on the bottom left and a palm on the bottom right above medium warm brown striped wooden decking. In the midground, a vibrant turquoise lagoon ripples with boat wakes as a pristine classic wooden motorboat with a white interior glides across the right, balanced by a white vaporetto to the left. The deep background opens up to the stunning historical architecture of San Giorgio Maggiore, showcasing a vintage white marble facade and brick bell tower alongside other classical buildings with warm terracotta roofs. Bright, hard, highly directional natural midday sunlight floods the scene from the front, casting deep black, harshly defined shadows under the subject's chin, beneath the balustrade railing, and from the lush plant leaves. Radiant specular highlights glimmer across the rippling water surface, the tips of the man's hair, his right cheekbone, and his bright white shirt, creating a high-contrast, energetic, and sophisticated upscale Mediterranean travel atmosphere. Shot straight-on as realistic, tack-sharp digital photography using a 35mm to 50mm lens at an aperture between f/8 and f/11 with a fast 1/1000s shutter speed and ISO 100 to freeze the boat motion and maintain a deep depth of field across the layered composition, this clean luxury menswear editorial image features contrast enhancement, highlight recovery, and a subtle teal and orange color grade to elevate the cool tones against the warm architecture, all naturally framed in a 4:5 aspect ratio.
```

</details>

<a id="nano-banana-wet-pool-portrait-pearl-heart-necklace"></a>
### 绿松石泳池中佩戴珍珠项链的雀斑女子

<a href="https://x.com/Just_sharon7/status/2044359258008113552"><img src="../../previews/nano-banana-wet-pool-portrait-pearl-heart-necklace.jpg" width="360"></a>

开头用锁脸指令保持参考图人物不变，再叠加雀斑、水珠和湿润肌肤等细节，并写明首饰与手部姿势。结尾的浅景深、35mm镜头和柔和日光营造出护肤广告质感。

Nano Banana 2 · 上传图改图 · 出处: [@Just_sharon7 on X](https://x.com/Just_sharon7/status/2044359258008113552) · 116 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`reference-face`](tags.md#tag-reference-face) [`wet-skin`](tags.md#tag-wet-skin) [`skincare-commercial`](tags.md#tag-skincare-commercial) [`shallow-depth-of-field`](tags.md#tag-shallow-depth-of-field)

<details><summary><b>提示词</b></summary>

```text
Use the same face from the reference image without changing facial features.
Cinematic fashion portrait of a young western woman with light freckles across her nose and cheeks, striking bright blue eyes, and fair skin. She is emerging gracefully from a turquoise swimming pool, water dripping from her wet, dark curly hair that clings to her shoulders. Her skin is glistening and damp under soft natural daylight. She wears a delicate light blue pearl necklace featuring a small glass heart pendant and matching diamond stud earrings. One hand is softly touching her cheek, displaying elegant white manicured nails. The image has a luxurious high-end skincare commercial aesthetic, shallow depth of field with a beautifully blurred water background, hyper-realistic details, 8k resolution, shot on a 35mm lens, cinematic lighting.
```

</details>

<a id="gpt-image-emerald-golden-light-beauty-portrait"></a>
### 翡翠绿渐变背景下的金色侧光女性肖像

<a href="https://x.com/mehvishs25/status/2072321898973892923"><img src="../../previews/gpt-image-emerald-golden-light-beauty-portrait.jpg" width="360"></a>

先用参考图锁定面部特征，再指定对角金色主光、一明一暗的光影和85mm f/1.8镜头参数，能稳定得到时尚大片的质感。皮肤纹理、高光和发丝细节的描述则让成片更接近杂志级写实。

GPT Image 2 · 上传图改图 · 出处: [@mehvishs25 on X](https://x.com/mehvishs25/status/2072321898973892923) · 115 赞，统计于 2026-10-29

[`beauty`](tags.md#tag-beauty) [`portrait`](tags.md#tag-portrait) [`cinematic lighting`](tags.md#tag-cinematiclighting) [`fashion editorial`](tags.md#tag-fashioneditorial)

<details><summary><b>提示词</b></summary>

```text
Create an ultra-realistic luxury beauty portrait using the exact same facial identity as the reference image. Preserve the face, facial structure, eye shape, nose, lips, skin characteristics, and overall appearance with maximum accuracy and consistency. The woman has long, silky jet-black hair, naturally luminous fair skin with subtle freckles across the nose and cheeks, striking emerald-green eyes, detailed eyelashes, naturally full eyebrows, and soft matte rose-pink lips. A delicate gold hoop earring adds a refined editorial touch.
The composition is a sophisticated medium close-up, capturing the head, neck, and upper torso. The subject faces the camera with a confident yet enigmatic expression, maintaining strong eye contact. A few loose strands of hair drift across her face, adding movement and visual interest while keeping her features clearly recognizable.
Lighting is cinematic and dramatic, featuring a diagonal beam of golden sunlight crossing the face from the upper corner, creating a beautiful interplay of highlights and shadows. One side of the face is softly illuminated while the opposite side falls into rich, atmospheric shadow. The background is a deep emerald-to-black gradient with subtle depth and smooth bokeh, creating a premium fashion-editorial mood.
Emphasize ultra-realistic skin texture, visible pores, natural complexion details, glossy eyes with crisp catchlights, and highly detailed hair strands. Use elegant cinematic color grading with rich contrast, realistic dynamic range, and luxury magazine aesthetics. Shot on an 85mm portrait lens, f/1.8, shallow depth of field, HDR photography, professional studio quality, Vogue-inspired beauty editorial, luxurious minimalism, photorealistic rendering, premium fashion campaign quality, hyper-detailed 8K resolution.

Portrait style

Style: Hyper-realistic, cinematic luxury beauty photography, high-end fashion editorial, premium magazine cover, sophisticated and emotionally captivating.
```

</details>

<a id="nano-banana-teen-suit-supercar-sunset-skyline"></a>
### 黄昏城市天际线下坐在超跑车顶的黑西装少年

<a href="https://x.com/Zarlish_Shahid/status/2078634279895248920"><img src="../../previews/nano-banana-teen-suit-supercar-sunset-skyline.jpg" width="360"></a>

单一主体、明确场景和一组道具搭起画面，金色夕阳天际线增加纵深。浅景深、光泽反射和杂志封面质感等摄影词让画面保持写实。要求无标志让车型保持通用。

Nano Banana 2 · 文生图 · 出处: [@Zarlish_Shahid on X](https://x.com/Zarlish_Shahid/status/2078634279895248920) · 114 赞，统计于 2026-10-28

[`fashion-editorial`](tags.md#tag-fashion-editorial) [`supercar`](tags.md#tag-supercar) [`golden-hour`](tags.md#tag-golden-hour) [`cityscape`](tags.md#tag-cityscape) [`luxury`](tags.md#tag-luxury)

<details><summary><b>提示词</b></summary>

```text
Luxury Has No Age

A confident 16-year-old boy sitting on the roof of a futuristic luxury supercar (Bugatti-inspired, no logos), wearing an expensive black tailored suit, premium designer sneakers, a luxury watch, and stylish sunglasses. Surrounded by luxury shopping bags, high-end fashion accessories, and elegant designer clothing. A modern city skyline with golden sunset lighting in the background. Ultra-realistic, cinematic composition, glossy reflections, shallow depth of field, dramatic lighting, luxury lifestyle, rich colors, 8K, hyper-detailed, magazine cover quality, photorealistic, premium fashion editorial style.

If you could create your dream luxury lifestyle with AI, what would be the first thing you'd add?
```

</details>

<a id="gpt-image-windswept-meadow-editorial-portrait"></a>
### 身穿象牙白长裙立于风中青草间的女子

<a href="https://x.com/MahnoorAi12/status/2101997367641751808"><img src="../../previews/gpt-image-windswept-meadow-editorial-portrait.jpg" width="360"></a>

前景草叶遮挡人物营造层次，再用鼠尾草绿与森林绿的低饱和配色、柔和阴天光、85mm f/1.8 景深和胶片颗粒定调。1:1 构图让人物偏右、上方留白，形成杂志感。

GPT Image 2.5 · 上传图改图 · 出处: [@MahnoorAi12 on X](https://x.com/MahnoorAi12/status/2101997367641751808) · 113 赞，统计于 2026-10-28

[`editorial`](tags.md#tag-editorial) [`meadow`](tags.md#tag-meadow) [`film-grain`](tags.md#tag-film-grain) [`fashion`](tags.md#tag-fashion) [`cinematic`](tags.md#tag-cinematic)

<details><summary><b>提示词</b></summary>

```text
A cinematic fashion-editorial portrait of a young East Asian woman standing partially concealed within tall, windswept green grass in an expansive meadow. She wears a loose, flowing off-white or ivory linen dress that moves softly with the breeze, contrasting gently against the rich natural surroundings.
Her dark hair appears naturally tousled by the wind, with soft strands falling across her face, partially veiling her eyes. Her head is gently lowered, gaze directed downward or slightly to the side, conveying a quiet, dreamy, introspective mood. The tall grass surrounds and partially obscures her figure, creating layered foreground elements, immersive depth, and a sense of visual intimacy.
Wind moves through the grass with subtle motion blur, while the subject remains sharply focused. The environment feels calm, isolated, and poetic, enhanced by a faint atmospheric haze and a muted palette of sage green, deep forest green, and soft neutral tones. Soft overcast daylight provides diffused, shadowless illumination with smooth tonal transitions, low contrast, gentle highlights, and realistic skin rendering.
Shallow depth of field produces creamy bokeh and natural background separation, while fine film grain adds an organic editorial texture. Minimalist composition emphasizing solitude and emotional storytelling. Square 1:1 composition, subject positioned slightly right of center with generous negative space above and around her, balanced visual weight, refined framing, sophisticated Korean and Japanese fashion magazine aesthetic, cinematic realism, highly detailed photorealistic photography, 85mm portrait lens, f/1.8, natural lens compression, ultra-realistic skin texture, premium color grading, atmospheric depth, elegant visual storytelling, award-winning editorial photography, masterfully composed, authentic and emotionally resonant.
```

</details>

<a id="nano-banana-emerald-blazer-fashion-grid-sunglasses"></a>
### 祖母绿西装墨镜四宫格时尚写真

<a href="https://x.com/weiinberg/status/2033048967777497600"><img src="../../previews/nano-banana-emerald-blazer-fashion-grid-sunglasses.jpg" width="360"></a>

以上传照片作为身份参考，明确 2x2 版式、服装和四个姿势。再用布光位置、相机参数和皮肤细节描述把画面推向杂志级写实。

Nano Banana 2 · 上传图改图 · 出处: [@weiinberg on X](https://x.com/weiinberg/status/2033048967777497600) · 113 赞，统计于 2026-10-28

[`fashion`](tags.md#tag-fashion) [`studio-portrait`](tags.md#tag-studio-portrait) [`grid-layout`](tags.md#tag-grid-layout) [`identity-reference`](tags.md#tag-identity-reference) [`editorial`](tags.md#tag-editorial)

<details><summary><b>提示词</b></summary>

```text
Use my uploaded photo as the identity reference.
Create a professional studio fashion photoshoot in a 2×2 grid collage showing four poses of the same person wearing black sunglasses.

Outfit: deep emerald green tailored blazer, cream/off-white dress shirt, black slim trousers, burgundy tie, optional silver watch. Blazer appears differently across frames (worn, draped over shoulder, partially removed, held).
Background: clean teal-to-turquoise gradient studio backdrop, minimal fashion studio setting.
Poses:
1.Close portrait adjusting tie.
2.Seated editorial pose leaning forward with elbow on knee.
3.Relaxed pose with vintage camera around neck.
4.Stylish pose running hand through hair while holding blazer.
Lighting: professional three-point studio lighting — softbox key light 45° camera left, soft fill light camera right, subtle rim light behind subject.
Camera: Sony A7R V, 85mm portrait lens, f/2.2, ISO 100, 1/160s, WB 5600K, shallow depth of field, focus on eyes.
Realism: natural skin pores, hair strands, subtle fabric wrinkles, realistic shadows, lens compression, reflections in sunglasses.
Output: ultra-realistic GQ/Vogue-style editorial photography, sharp detail, 4K resolution, clean 2×2 grid layout.
```

</details>

<a id="gpt-image-damp-hair-beauty-portrait"></a>
### 湿发近景美妆人像

<a href="https://x.com/mehvishs25/status/2082648912981328244"><img src="../../previews/gpt-image-damp-hair-beauty-portrait.jpg" width="360"></a>

先用上传的参考图锁定五官，再把每个特征逐条列成清单，使编辑后的脸部保持一致。85mm 镜头和眼睛位于上三分之一处的构图要求，形成紧凑的时尚大片式取景。

GPT Image 2 · 上传图改图 · 出处: [@mehvishs25 on X](https://x.com/mehvishs25/status/2082648912981328244) · 112 赞，统计于 2026-10-29

[`beauty`](tags.md#tag-beauty) [`portrait`](tags.md#tag-portrait) [`reference-image`](tags.md#tag-reference-image) [`golden-hour`](tags.md#tag-golden-hour)

<details><summary><b>提示词</b></summary>

```text
Ultra-photorealistic RAW beauty portrait using the uploaded reference image to preserve the subject's exact facial identity, proportions, and defining facial features. The woman in the final image must closely match the reference while appearing naturally more polished and editorial, without altering her recognizable face.

An extraordinary young woman with captivating soft emerald-green eyes featuring subtle golden sunburst details around the irises and crystal-clear natural catchlights. She looks directly into the camera with a calm, confident expression and a faint, elegant smile, creating an intimate luxury beauty campaign aesthetic.

Her porcelain-fair skin glows with healthy natural radiance, displaying authentic pores, delicate freckles across the bridge of the nose and cheeks, gentle peach undertones, and realistic skin texture without excessive smoothing. Naturally full dark eyebrows, long separated lashes, a refined straight nose, softly sculpted cheekbones, and hydrated satin rose lips complete her timeless beauty.

Her silky jet-black hair is slightly damp, with glossy strands framing her face naturally. Soft curtain bangs and loose textured wisps fall across one side of her forehead, creating effortless movement and cinematic elegance. Tiny highlights shimmer along the damp hair, enhancing realism.

Golden-hour sunlight filters through sheer curtains, wrapping her face in warm, diffused light while casting delicate organic shadow patterns across her skin. The lighting creates luminous highlights, rich dimensional contrast, and sparkling reflections inside her eyes without appearing overly dramatic.

The background fades into a luxurious creamy bokeh of warm ivory, champagne, and soft beige tones, keeping complete attention on her face. The composition is slightly asymmetrical for a modern editorial feel, with the eyes positioned near the upper third of the frame for a more striking visual impact.

Luxury skincare campaign, Vogue Italia beauty editorial, high-fashion cosmetic advertisement, quiet luxury aesthetic, old-money elegance, cinematic realism, premium natural beauty, ultra-detailed DSLR photography, 85mm portrait lens, f/1.2 aperture, ultra-shallow depth of field, razor-sharp focus on the eyes, HDR lighting, realistic micro skin detail, global illumination, premium cinematic color grading, hyper-realistic, 8K, award-winning beauty photography, sophisticated editorial masterpiece, visually unforgettable, trending luxury beauty campaign.
```

</details>

<a id="gpt-image-convenience-store-flash-found-photo"></a>
### 深夜便利店里的闪光灯随手拍人像

<a href="https://x.com/Ciri_ai/status/2101253843870707722"><img src="../../previews/gpt-image-convenience-store-flash-found-photo.jpg" width="360"></a>

把杂志编辑感与具体的卡片机参数（30mm、ISO 640、f/3.2）和直闪叠加，再刻意加入高光溢出、偏色白平衡和随意构图等瑕疵。长负面清单排除影棚质感、HDR 与塑料皮肤，让画面像翻出来的旧照片。

GPT Image 2.5 · 文生图 · 出处: [@Ciri_ai on X](https://x.com/Ciri_ai/status/2101253843870707722) · 111 赞，统计于 2026-10-29

[`found-photo`](tags.md#tag-found-photo) [`direct-flash`](tags.md#tag-direct-flash) [`y2k-compact`](tags.md#tag-y2k-compact) [`convenience-store`](tags.md#tag-convenience-store) [`fashion-editorial`](tags.md#tag-fashion-editorial)

<details><summary><b>提示词</b></summary>

```text
GINZA Magazine-inspired Japanese lifestyle fashion editorial × early-2000s Y2K consumer compact digital camera × Korean female idol × raw documentary-fashion hybrid × found photograph aesthetic.

The image must feel like a real photograph discovered inside an old digital camera rather than a deliberately retro-styled AI image.

Japanese urban lifestyle sensibility, understated fashion intelligence, quiet observational storytelling, mundane everyday environment transformed into subtle fashion imagery.

A beautiful young adult Korean female idol standing inside a small Japanese convenience store late at night, casually holding a bottled milk drink while looking directly into the camera.

She wears a faded navy oversized zip hoodie over a white fitted ribbed tank top, low-rise charcoal mini skirt, worn sneakers, tiny silver shoulder bag and thin silver necklace.

Long platinum-blonde hair, slightly messy straight bangs, loose strands around her face.

Soft Korean-Japanese makeup, natural flushed cheeks, subtle taupe eyeshadow, soft pink lips, realistic visible pores.

She stands between narrow convenience-store aisles, refrigerators glowing behind her, shelves of snacks and drinks creating visual clutter.

Photographed extremely close with a late-2000s consumer compact digital camera, 30mm equivalent, ISO 640, f/3.2.

DIRECT ON-CAMERA FLASH, slightly harsh frontal flash, realistic specular highlights on skin and packaging, warm fluorescent ambient light mixing with cooler refrigerator illumination.

Slightly imperfect white balance, clipped highlights on reflective packaging, darker corners, subtle digital noise, mild chromatic aberration, slight edge softness.

The framing feels accidental: part of a shelf enters the foreground, one product is slightly cropped, subject not perfectly centered.

GINZA-inspired quiet Japanese lifestyle sensibility, understated fashion intelligence, raw documentary observation.

LUT: Warm Convenience Digital / muted highlights / fluorescent contamination
Harmony: navy × white × charcoal × refrigerator cyan
sRef: [Y2K-COMPACT-SREF]
Tokens: found photograph, direct flash, consumer digital, mundane location, incidental framing, not retro filter.
Real photograph, not AI fashion campaign.

3:4 portrait.

NEGATIVE:
studio lighting, beauty campaign, luxury advertising, perfect symmetry, HDR, smartphone photography, cinematic teal orange, plastic skin, excessive bokeh, flawless skin, CGI, illustration, anime, overly posed idol photoshoot.
```

</details>

<a id="gpt-image-emerald-cafe-sage-green-fashion-portrait"></a>
### 翠绿咖啡馆外的鼠尾草绿穿搭人像

<a href="https://x.com/hey_am_cherry/status/2112044506514440506"><img src="../../previews/gpt-image-emerald-cafe-sage-green-fashion-portrait.jpg" width="360"></a>

先定场景，再逐件列出服饰配饰并指定颜色，让整体色调统一。平视全身构图、浅景深和黄金时段光线带来杂志感，结尾的负面提示词用来防止人体结构出错。

GPT Image 2.5 · 文生图 · 出处: [@hey_am_cherry on X](https://x.com/hey_am_cherry/status/2112044506514440506) · 111 赞，统计于 2026-10-28

[`fashion`](tags.md#tag-fashion) [`cafe`](tags.md#tag-cafe) [`golden-hour`](tags.md#tag-golden-hour) [`editorial`](tags.md#tag-editorial) [`full-body`](tags.md#tag-full-body)

<details><summary><b>提示词</b></summary>

```text
Create a realistic lifestyle fashion portrait, subject stands casually outside a premium modern café with deep emerald green exterior panels and large glass windows revealing a warm, softly lit interior. Minimal Scandinavian café aesthetic with hanging pendant lights, wooden furniture, and subtle reflections on the glass.

The model wears a pastel sage-green baseball cap, fitted white tube top, olive-green denim overall shorts with one strap unfastened, matching green sneakers, delicate gold jewelry, and a luxury black quilted mini handbag with pearl chain placed on a small marble café table beside a takeaway coffee cup.

Natural relaxed pose with one leg slightly crossed, one hand inside the pocket, calm confident expression, looking directly at the camera. Eye-level composition, full-body framing, shallow depth of field, creamy bokeh, soft golden-hour daylight, premium editorial fashion photography, ultra-realistic skin texture, luxury color grading, crisp details, cinematic realism, high-end Vogue campaign quality.

Negative Prompt: low quality, blurry, extra fingers, bad anatomy, distorted face, duplicate person, cartoon, CGI, oversaturated colors, watermark, logo, text, cropped body, unnatural pose, plastic skin, noise.
```

</details>

<a id="gpt-image-surveillance-hud-street-portrait-russian-text"></a>
### 街头人像叠加俄文监控界面

<a href="https://x.com/codewithhajra/status/2074473336327802940"><img src="../../previews/gpt-image-surveillance-hud-street-portrait-russian-text.jpg" width="360"></a>

以监控视角的抓拍照为底，再列出人脸框、身份卡、扫描线、时间戳等具体界面元素。要求所有界面文字统一为俄语并禁用英文，保证标签一致，服装、地点、动物和色板用方括号留空，可直接套用。

GPT Image 2 · 文生图 · 出处: [@codewithhajra on X](https://x.com/codewithhajra/status/2074473336327802940) · 111 赞，统计于 2026-10-29

[`hud-overlay`](tags.md#tag-hud-overlay) [`surveillance-style`](tags.md#tag-surveillance-style) [`street-photography`](tags.md#tag-street-photography) [`multilingual-text`](tags.md#tag-multilingual-text) [`template`](tags.md#tag-template)

<details><summary><b>提示词</b></summary>

```text
Cyber-core editorial photography of [your details] wearing [clothing], walking through [location] with [animal]. A realistic candid street photograph captured from a slightly elevated surveillance-style angle, featuring natural movement, stylish everyday fashion, and a calm cinematic atmosphere. Add elegant digital interface elements, including a facial detection frame, object labels, an identity card panel, subtle scan lines, thin HUD boxes, small data text, tracking points, a timestamp, and minimal biometric graphics. Keep the interface clean, refined, and well-spaced. All visible interface text, labels, captions, ID panel content, biometric data, object tags, timestamps, and digital overlay elements must be written entirely in Russian. Do not use any English text anywhere in the image. Use a [color palette] with realistic lighting, polished editorial photography, soft contrast, sharp details, and a sophisticated futuristic design language. Beautiful, minimal, and uncluttered. Aspect ratio: 4:5.
```

</details>

<a id="nano-banana-cheetah-red-velvet-sofa-luxury"></a>
### 红色丝绒沙发上抱着猎豹的男人

<a href="https://x.com/auqibhabib/status/2029721401033384149"><img src="../../previews/nano-banana-cheetah-red-velvet-sofa-luxury.jpg" width="360"></a>

以参考图锁定人物面部，再依次列出服装、道具、沙发场景和虚化背景中的保镖来营造层次。结尾的电影感光线和戏剧氛围用来定下整体情绪。

Nano Banana 2 · 上传图改图 · 出处: [@auqibhabib on X](https://x.com/auqibhabib/status/2029721401033384149) · 111 赞，统计于 2026-10-28

[`reference-image`](tags.md#tag-reference-image) [`luxury`](tags.md#tag-luxury) [`cinematic-lighting`](tags.md#tag-cinematic-lighting) [`animal`](tags.md#tag-animal) [`portrait`](tags.md#tag-portrait)

<details><summary><b>提示词</b></summary>

```text
Using the reference picture, create A stylish man sitting on a luxurious vintage red velvet sofa, wearing black silk shirt, sunglasses, confi-dently holding a cheetah adorned with cinematic lighting, dollars are spread on sofa too and there are two guards on back side in blur bg, luxury life-style, dramatic atmosphere." 100% Real Face 8K Resolution
```

</details>

<a id="nano-banana-miniature-self-figurine-in-hand"></a>
### 女子掌托自己的迷你手办

<a href="https://x.com/HaniaAi12/status/2031190193253056883"><img src="../../previews/nano-banana-miniature-self-figurine-in-hand.jpg" width="360"></a>

用24mm广角和强制透视，把手办放在前景、真人放在中景。真人和手办共用同一张上传的人脸参考，并重复描述服装让两者保持一致。手部皮肤细节清晰，花园背景虚化柔和，强化了大小反差的错觉。

Nano Banana 2 · 上传图改图 · 出处: [@HaniaAi12 on X](https://x.com/HaniaAi12/status/2031190193253056883) · 111 赞，统计于 2026-10-29

[`forced-perspective`](tags.md#tag-forced-perspective) [`miniature-figurine`](tags.md#tag-miniature-figurine) [`face-reference`](tags.md#tag-face-reference) [`wide-angle`](tags.md#tag-wide-angle) [`scale-illusion`](tags.md#tag-scale-illusion)

<details><summary><b>提示词</b></summary>

```text
A hyper-realistic, forced-perspective wide-angle photography shot captured with a 24mm lens, featuring a woman holding a highly detailed miniature figurine of herself in her outstretched right hand, creating a playful scale illusion. The woman in the mid-ground, identified by the uploaded face as reference, wears a black and grey plaid flannel shirt left unbuttoned over a black graphic t-shirt with a yellow and white logo, paired with blue jeans, and is smiling warmly with a soft focus applied to her face.

The miniature figurine in the immediate foreground is a perfect scale replica, also featuring the uploaded face as reference but with a slightly stylized, hand-painted resin texture, wearing the exact same outfit including the plaid shirt, graphic tee, distressed denim jeans with rips, and grey sneakers, standing on a small circular grey concrete base.

The hand holding the base is rendered with extreme dermatological fidelity, showing skin pores, knuckles, and fingerprints in razor-sharp focus. The background is a picturesque English countryside garden featuring a stone cottage with a chimney, a wooden archway covered in climbing purple wisteria, lush green lawns, and vibrant pink rose bushes, all bathed in soft, diffused natural daylight with a shallow depth of field that creates a creamy bokeh effect on the distant architecture and foliage.

8K resolution, cinematic lighting, photorealistic textures, 2:3 ratio.
```

</details>

<a id="nano-banana-burgundy-satin-editorial-portrait"></a>
### 酒红缎面高定与金色耳饰的时尚人像

<a href="https://x.com/MissDelulu9/status/2109630710642528421"><img src="../../previews/nano-banana-burgundy-satin-editorial-portrait.jpg" width="360"></a>

提示词按面部、发型服装、姿势、背景、光线和摄影风格分块书写，结构清晰。85mm、柔光箱、毛孔与香槟色高光等具体镜头、光线和皮肤质感词，让画面接近真实杂志大片。

Nano Banana 2.1 · 文生图 · 出处: [@MissDelulu9 on X](https://x.com/MissDelulu9/status/2109630710642528421) · 110 赞，统计于 2026-10-28

[`editorial`](tags.md#tag-editorial) [`fashion`](tags.md#tag-fashion) [`portrait`](tags.md#tag-portrait) [`satin`](tags.md#tag-satin) [`studio-lighting`](tags.md#tag-studio-lighting)

<details><summary><b>提示词</b></summary>

```text
Create an ultra-realistic, high-fashion editorial portrait of a stunning adult woman with striking blue-grey eyes, naturally full lips with glossy coral-red lipstick, defined eyebrows, sharp black winged eyeliner, long eyelashes, subtle freckles, and luminous dewy skin with realistic pores and a soft champagne highlight.

Her sleek, jet-black hair is neatly center-parted and pulled back into a long, straight, low ponytail. She wears an elegant deep burgundy satin couture dress featuring an exaggerated sculptural high collar, dramatic draped fabric, and an asymmetrical sleeveless design. Large, polished gold geometric statement earrings complete the luxurious look.

Pose: Three-quarter over-the-shoulder pose, body turned away from the camera while her face looks directly toward the viewer, with a confident, elegant, slightly mysterious expression.

Background: Minimalist muted sage-green and turquoise studio backdrop with soft, atmospheric gradients.

Lighting: Professional softbox lighting, cinematic shadows, delicate highlights on the cheekbones, realistic satin reflections, beautiful skin texture, and sophisticated color grading.

Photography style: Luxury beauty campaign, Vogue-inspired editorial photography, 85mm portrait lens, shallow depth of field, sharp focus on the eyes, photorealistic details, premium fashion magazine aesthetic,  vertical 9:16 composition.
```

</details>

<a id="gpt-image-halftone-windswept-hair-portrait-ivory-paper"></a>
### 象牙纸上的飞发网点肖像

<a href="https://x.com/hey_am_cherry/status/2111324127378416005"><img src="../../previews/gpt-image-halftone-windswept-hair-portrait-ivory-paper.jpg" width="360"></a>

提示词点明网点、点刻阴影和丝网印刷质感，并限定为深黑与奶油两色，复古印刷感很到位。独立的反向提示排除彩色、3D 和塑料皮肤，同时明确了胸部以上的构图。

GPT Image 2.5 · 文生图 · 出处: [@hey_am_cherry on X](https://x.com/hey_am_cherry/status/2111324127378416005) · 108 赞，统计于 2026-10-29

[`halftone`](tags.md#tag-halftone) [`monochrome`](tags.md#tag-monochrome) [`portrait`](tags.md#tag-portrait) [`vintage-print`](tags.md#tag-vintage-print) [`negative-prompt`](tags.md#tag-negative-prompt)

<details><summary><b>提示词</b></summary>

```text
{
  "aspect_ratio": "9:16",
  "prompt": "A beautiful young woman with long, messy black hair blowing dramatically across her face, eyes closed, lips slightly parted, head tilted back, elegant elongated neck, wearing a simple black V-neck top. Chest-up portrait, slightly right of center. Vintage monochrome halftone print art, tiny black ink dots, stippled shading, high contrast, warm ivory textured paper background, deep black shadows, cream highlights, retro editorial photography, moody, dreamy, melancholic, intricate details, sharp facial features, authentic screen-print texture.",
  "negative_prompt": "color, 3D, anime, plastic skin, open eyes, exaggerated expression, deformed face, bad anatomy, extra features, busy background, text, watermark, excessive blur"
}
```

</details>

<a id="gpt-image-cream-hoodie-selfie-portrait"></a>
### 特写自拍，女子穿奶油色连帽衫

<a href="https://x.com/mehvishs25/status/2067641812165243390"><img src="../../previews/gpt-image-cream-hoodie-selfie-portrait.jpg" width="360"></a>

用参考图锁定人物身份，并具体描述妆容、衣物与姿态，让结果紧贴原图。手机自拍取景、素净暖色墙面，以及对眼睛和袖口的清晰对焦，共同营造浅景深的真实质感。

GPT Image 2 · 上传图改图 · 出处: [@mehvishs25 on X](https://x.com/mehvishs25/status/2067641812165243390) · 106 赞，统计于 2026-10-29

[`selfie`](tags.md#tag-selfie) [`portrait`](tags.md#tag-portrait) [`reference-identity`](tags.md#tag-reference-identity) [`photorealistic`](tags.md#tag-photorealistic)

<details><summary><b>提示词</b></summary>

```text
Photorealistic close-up selfie portrait of the same girl from the reference image, using the reference as the only source for facial identity. Preserve her exact face shape, skin tone, eye shape, nose, lips, age, proportions, and all recognizable features with high accuracy. Do not alter her identity or make her appear as a different person.

She fills almost the entire frame, creating an intimate and authentic selfie composition. Her head is slightly tilted to one side, with her cheek gently resting against her shoulder and partially tucked inside the long cream-colored sleeve of an oversized zip-up hoodie draped casually over one shoulder. Long, straight dark hair with soft curtain bangs falls naturally along the left side of her face, partially covering one eye.

Her expression is calm and slightly pouting, with a relaxed, effortless mood. She looks directly into the camera, with visible eyelashes and subtle eye contact. Makeup is soft and natural, featuring laminated brows, elongated black winged eyeliner extending the eye shape, and matte dusty-pink lips.

The camera is positioned extremely close to her face, recreating the authentic feel of a webcam or phone selfie. The frame has a slight tilt and an unposed, spontaneous appearance. Sharp focus on the visible eye, lips, hair strands, skin texture, and the thick cream-colored hoodie sleeve, while the background softly blurs away.

Behind her is a simple warm gray-beige wall with no distracting details. Warm indoor ambient lighting mixed with subtle screen light from the front-left softly illuminates her face and hair, creating gentle highlights and natural shadows. The color palette is muted and cozy, dominated by cream, beige-gray, black, and dusty-pink tones.

Ultra-photorealistic, authentic smartphone selfie aesthetic, natural skin texture, realistic hair detail, subtle imperfections, shallow depth of field, intimate composition, candid everyday atmosphere, high detail, premium photography quality.
```

</details>

<a id="nano-banana-blue-haze-hoodie-studio-portrait"></a>
### 深蓝雾气影棚中的深色连帽衫电影感肖像

<a href="https://x.com/Emmma___0/status/2108109236555403768"><img src="../../previews/nano-banana-blue-haze-hoodie-studio-portrait.jpg" width="360"></a>

对称的中近景构图,边缘冷蓝光配背景一侧的暖橙光,形成电影感色彩对比。皮肤瑕疵、85mm 镜头感,再加上排除塑料皮肤和过度 HDR 的负面提示,让人脸保持真实。

Nano Banana 2.1 · 文生图 · 出处: [@Emmma___0 on X](https://x.com/Emmma___0/status/2108109236555403768) · 102 赞，统计于 2026-10-28

[`portrait`](tags.md#tag-portrait) [`cinematic`](tags.md#tag-cinematic) [`studio-lighting`](tags.md#tag-studio-lighting) [`photorealistic`](tags.md#tag-photorealistic) [`negative-prompt`](tags.md#tag-negative-prompt)

<details><summary><b>提示词</b></summary>

```text
Create a highly photorealistic cinematic portrait of a person standing centered and facing the camera with a calm, serious expression. Natural facial proportions, realistic skin texture, detailed eyes, subtle skin imperfections, and naturally styled hair. The subject wears a simple oversized dark hoodie with a minimal light-colored shirt visible underneath.
Use a symmetrical composition with the subject occupying the central portion of the frame, medium close-up framing, and a clean professional presentation. The background is a dark deep-blue studio environment with atmospheric haze and subtle volumetric fog. Add cool blue lighting around the edges of the subject and a soft warm orange glow in the distant background on one side, creating a cinematic color contrast.
Dramatic but natural studio lighting, soft directional key light, subtle rim lighting, realistic shadows, controlled highlights, shallow depth of field, smooth background falloff, premium editorial photography, modern cinematic aesthetic, high contrast, realistic colors, detailed clothing texture, realistic hair and skin, professional camera photography, 85mm lens look, crisp focus, subtle film grain, ultra-photorealistic, highly detailed, 8K quality.
Negative prompt: cartoon, illustration, CGI, plastic skin, excessive HDR, oversharpening, distorted face, unnatural anatomy, extra limbs, blurry subject, low resolution, artificial skin, text, logo, watermark.
```

</details>

<a id="nano-banana-bw-seaside-windblown-portrait"></a>
### 黑白海边风吹发丝特写肖像

<a href="https://x.com/SimplyAnnisa/status/2070720737426428068"><img src="../../previews/nano-banana-bw-seaside-windblown-portrait.jpg" width="360"></a>

先用参考图锁定面部并明确禁止美化，再叠加一次性胶片颗粒、85mm浅景深和极致微距构图描述。结尾的否定清单（不要数码锐利、不要居中构图）让画面保持抓拍感。

Nano Banana 2 · 上传图改图 · 出处: [@SimplyAnnisa on X](https://x.com/SimplyAnnisa/status/2070720737426428068) · 102 赞，统计于 2026-10-28

[`black-and-white`](tags.md#tag-black-and-white) [`film-grain`](tags.md#tag-film-grain) [`macro-portrait`](tags.md#tag-macro-portrait) [`face-reference`](tags.md#tag-face-reference) [`coastal`](tags.md#tag-coastal)

<details><summary><b>提示词</b></summary>

```text
Nano banana 2 on
@Lart_AI


https://
lartai.com/?TG=10259
Intimate Wind Whisper
Composition: Extreme macro close-up focusing tightly on the face with wind-blown hair strands delicately framing the features and shallow focus on natural skin texture
Prompt: Using the uploaded photo as the exact face reference. Keep the face identity 100% unchanged, do not alter facial features, proportions, expression structure, or skin details. No face distortion, no beautification, no AI-looking changes. Photorealistic candid snapshot taken on a low-quality disposable film camera, black and white cinematic film photography, authentic 35mm grain, subtle imperfections, natural texture, vintage analog look. The woman has full voluminous hair slightly messy and blown by ocean wind, strands of hair falling naturally across the face, chin slightly raised, eyes gently closed, dreamy peaceful expression, soft genuine smile. She is wearing a voluminous white dress, sitting on wet textured seaside rocks. The background shows a dramatic massive coastal cliff covered in mist under a heavy overcast grey sky creating a moody coastal atmosphere with raw cinematic realism. Natural diffused daylight casts soft shadows in an emotional editorial photography style, realistic film exposure, high dynamic range, shallow depth of field, shot on 85mm lens, cinematic framing, authentic documentary feeling. Extreme close-up macro framing tightly captures her face, highlighting the texture of her skin and the delicate strands of wind-blown hair resting across her closed eyes and smile, with the white dress softly visible at the lower frame edge and the misty cliff gently out of focus behind.
no clean digital sharpness, no CGI look, no poster composition, no centered portrait, no black bars –ar 9:16
```

</details>

<a id="nano-banana-bedroom-selfie-white-duvet"></a>
### 卧室自拍，女子躺在白色被子下

<a href="https://x.com/jzaib4269/status/2068317754466451676"><img src="../../previews/nano-banana-bedroom-selfie-white-duvet.jpg" width="360"></a>

手机自拍视角，脸部占满画面，被子遮住一侧，使画面显得随性自然而非摆拍。同时写明窗光、中性色调和拍摄角度，让光线与氛围保持统一。

Nano Banana 2 · 文生图 · 出处: [@jzaib4269 on X](https://x.com/jzaib4269/status/2068317754466451676) · 101 赞，统计于 2026-10-29

[`selfie`](tags.md#tag-selfie) [`portrait`](tags.md#tag-portrait) [`bedroom`](tags.md#tag-bedroom) [`natural-light`](tags.md#tag-natural-light)

<details><summary><b>提示词</b></summary>

```text
low quality, blurry, overprocessed skin, heavy makeup, exaggerated facial features, distorted eyes, extra fingers, duplicate features, cartoon, CGI, painting, illustration, harsh shadows, oversaturated colors, grainy image, watermark, text, logo, cropped face, unnatural pose, artificial lighting, bad anatomy, low resolution.
```

</details>

<a id="nano-banana-mirror-shard-self-reflections"></a>
### 居中男子被漂浮的破碎镜片包围

<a href="https://x.com/Ozayrr_irl/status/2050471266843582688"><img src="../../previews/nano-banana-mirror-shard-self-reflections.jpg" width="360"></a>

先用参考人脸和明确的身份锁定指令固定主体，再为每块碎片分别描述角度、服装和情绪，让重复的人物呈现为多个版本。纯黑场景配单一冷白主光，使碎片成为画面中唯一的亮部。

Nano Banana 2 · 上传图改图 · 出处: [@Ozayrr_irl on X](https://x.com/Ozayrr_irl/status/2050471266843582688) · 100 赞，统计于 2026-10-29

[`mirror-shards`](tags.md#tag-mirror-shards) [`reflections`](tags.md#tag-reflections) [`identity-lock`](tags.md#tag-identity-lock) [`cinematic-portrait`](tags.md#tag-cinematic-portrait)

<details><summary><b>提示词</b></summary>

```text
"Use the facial identity given and keep the facial features exactly same, and generate a picture standing in a pitch-black studio, surrounded by dozens of broken mirror shards floating mid-air around him at different angles — each shard reflecting a different version of him, different expressions, different outfits, different emotions. He stands perfectly still in the center, wearing a crisp black turtleneck, arms at his sides, staring forward. The only light source is cold white light hitting each shard differently, fracturing the room into infinite reflections. Vertical 9:13 format. Ultra photorealistic, 8K, no text overlays, cinematic color grading."
```

</details>

<a id="nano-banana-subway-stairs-black-coat-street-portrait"></a>
### 地铁楼梯上身穿黑色大衣的男子

<a href="https://x.com/pictsbyai/status/2032375474999964121"><img src="../../previews/nano-banana-subway-stairs-black-coat-street-portrait.jpg" width="360"></a>

结构化 JSON 提示词把画面拆成构图、色彩、光线、主体和背景几个块，明确给出十六进制色值、光线方向和阴影位置。对发丝质感和手部姿态的细致描述，避免人脸过于光滑。

Nano Banana 2 · 文生图 · 出处: [@pictsbyai on X](https://x.com/pictsbyai/status/2032375474999964121) · 100 赞，统计于 2026-10-28

[`street-photography`](tags.md#tag-street-photography) [`json-prompt`](tags.md#tag-json-prompt) [`fashion`](tags.md#tag-fashion) [`moody-lighting`](tags.md#tag-moody-lighting) [`editorial`](tags.md#tag-editorial)

<details><summary><b>提示词</b></summary>

```text
{
"metadata": {
"image_type": "photograph",
"primary_purpose": "editorial"
},
"composition": {
"rule_applied": "rule of thirds",
"aspect_ratio": "4:5",
"layout": "single subject",
"focal_points": [
"Subject's face and dark sunglasses",
"Yellow fluorescent light fixture leading to the subject"
],
"visual_hierarchy": "Eye starts at the subject's face due to contrast with sunglasses, follows the V-neck down the black coat, moves outward along the metallic handrails, and catches the bright sunlight shaft on the left wall and the yellow light on the right.",
"balance": "asymmetric"
},
"color_profile": {
"dominant_colors": [
{
"color": "Black",
"hex": "#111111",
"percentage": "45%",
"role": "primary subject"
},
{
"color": "Warm Gray",
"hex": "#7A7269",
"percentage": "35%",
"role": "background"
},
{
"color": "Golden Yellow",
"hex": "#E5B05C",
"percentage": "10%",
"role": "accent"
}
],
"color_palette": "complementary",
"temperature": "warm",
"saturation": "moderate",
"contrast": "high contrast"
},
"lighting": {
"type": "mixed",
"source_count": "multiple sources",
"direction": "front",
"directionality": "highly directional",
"quality": "dramatic",
"intensity": "moody",
"contrast_ratio": "high contrast (dramatic shadows)",
"mood": "mysterious",
"shadows": {
"type": "harsh defined edges",
"density": "deep black",
"placement": "under handrails, within stair treads, and engulfing the subject's lower body",
"length": "medium"
},
"highlights": {
"treatment": "blown out",
"placement": "on upper left wall from sun shaft, fluorescent light fixture, and reflective handrails"
},
"ambient_fill": "present",
"light_temperature": "warm (golden)"
},
"technical_specs": {
"medium": "digital photography",
"style": "realistic",
"texture": "sharp",
"sharpness": "tack sharp",
"grain": "digital noise",
"depth_of_field": "medium",
"perspective": "high angle"
},
"artistic_elements": {
"genre": "street",
"influences": [
"Urban street style fashion photography",
"Cinematic cyberpunk/matrix aesthetic"
],
"mood": "sophisticated",
"atmosphere": "Gritty yet polished urban transit environment with a moody, imposing, and highly stylized fashion presence",
"visual_style": "structured"
},
"typography": {
"present": false,
"fonts": [],
"placement": "",
"integration": ""
},
"subject_analysis": {
"primary_subject": "Young male model wearing an oversized, structured long black overcoat, black V-neck top, black trousers, and dark rectangular sunglasses, walking down stairs. Hair: Medium length, textured cut (e.g., modern shag/tapered cut). Length: Roughly ear-level/temple-level on the sides, slightly longer and voluminous on top (3-4 inches), with soft layers and natural movement. Texture: Natural wavy texture, showing varied strands, slight frizz, and natural volume (imperfections visible, not 'AI smooth'), styled loosely back from the forehead without a distinct part. Evidence of light matte product application.",
"positioning": "center",
"scale": "medium",
"interaction": "interacting with environment",
"facial_expression": {
"mouth": "neutral",
"smile_intensity": "no smile",
"eyes": "direct gaze",
"eyebrows": "neutral",
"overall_emotion": "serious",
"authenticity": "posed"
},
"hands_and_gestures": {
"left_hand": "resting at waist level, lightly holding the edge of the black overcoat, silver ring visible on finger",
"right_hand": "not visible, hidden behind the coat's bulk or swinging backward",
"finger_positions": "left hand thumb and index finger slightly curled and gripping fabric, remaining fingers obscured",
"finger_interlacing": "none",
"hand_tension": "relaxed",
"interaction": "holding coat",
"naturalness": "deliberately posed"
},
"body_positioning": {
"posture": "standing",
"angle": "facing camera",
"weight_distribution": "shifted",
"shoulders": "level"
}
},
"background": {
"setting_type": "indoor",
"spatial_depth": "medium",
"elements_detailed": [
{
"item": "Stainless steel handrail",
"position": "left",
"distance": "foreground",
"size": "medium",
"condition": "worn",
"specific_features": "Tubular metal with distinct mounting brackets and subtle reflections"
},
{
"item": "Stainless steel handrail",
"position": "right",
"distance": "midground",
"size": "medium",
"condition": "worn",
"specific_features": "Tubular metal matching the left side, catching edge highlights"
},
{
"item": "Fluorescent light fixture",
"position": "top right",
"distance": "background",
"size": "medium",
"condition": "vintage",
"specific_features": "Rectangular housing emitting a strong, warm amber/yellow light"
}
],
"wall_surface": {
"material": "tile",
"surface_treatment": "finished",
"texture": "perfectly smooth",
"finish": "satin",
"color": "warm grayish-brown",
"color_variation": "patchy",
"features": "clean, distinct grid-like grout lines separating large rectangular stone/granite panels, sharp diagonal shaft of warm sunlight hitting the upper left section",
"wear_indicators": "industrial"
},
"floor_surface": {
"material": "concrete",
"color": "dark gray with yellow accents",
"pattern": "striped"
},
"objects_catalog": "Metal diamond-plate stair treads with yellow painted safety edges running horizontally across the bottom and midground, dual tubular stainless steel handrails flanking the stairs, rectangular yellow light fixture mounted to the ceiling angled directly above the stairwell, large rectangular stone tiles covering the walls.",
"background_treatment": "sharp"
},
"generation_parameters": {
"prompts": [
"Editorial street style photography, a handsome young man with medium length, textured modern shag haircut showing natural wavy movement and styled loosely back. He wears dark rectangular sunglasses, a long black oversized wool coat, and an all black outfit, walking down urban subway stairs. The walls are made of large polished brown-gray stone tiles with visible grid grout lines. A dramatic shaft of warm golden sunlight hits the upper left wall. A vintage yellow fluorescent light fixture is on the upper right ceiling. The stairs are concrete with metal edges and yellow safety paint. Stainless steel handrails. Cinematic lighting, deep dramatic black shadows, sharp focus, 85mm lens, high contrast, moody, fashionable underground matrix aesthetic.",
"Cinematic fashion portrait, male model in structural black overcoat descending transit stairs, medium length textured hair with soft waves, tinted glasses. High angle shot looking down the steps. Brutalist architecture background, granite wall panels. Mixed lighting featuring harsh geometric sunbeams on the wall contrasting with artificial yellow ambient light. Gritty texture, high dynamic range, hyper-realistic, sophisticated urban mood."
],
"keywords": [
"street style",
"oversized black coat",
"subway stairs",
"cinematic lighting",
"medium length hair",
"textured hair",
"modern shag"
],
"technical_settings": "85mm lens, f/4.0 aperture for medium depth of field keeping background architectural elements recognizable, 1/250s shutter speed, ISO 400. Metered to preserve the sun shaft highlight while letting shadows fall to deep blacks.",
"post_processing": "Color grading to enhance warm golden highlights against neutral/cool shadows, boosted contrast curve, subtle film grain introduced in the deep shadow areas for texture."
}
}
```

</details>

<a id="gpt-image-rooftop-sunset-smoke-disintegration-portrait"></a>
### 日落屋顶上身体化作烟尘消散的男子

<a href="https://x.com/AiWithTariq/status/2101869465977897075"><img src="../../previews/gpt-image-rooftop-sunset-smoke-disintegration-portrait.jpg" width="360"></a>

提示词先定下服装、侧面姿势和场景，再把消散效果限定在身体一侧，人物依然清晰可辨。烟、灰烬、金色火星分别点名，再配上暖色日落光和湿润反光地面，让过渡有明确光源和层次。

GPT Image 2.5 · 文生图 · 出处: [@AiWithTariq on X](https://x.com/AiWithTariq/status/2101869465977897075) · 98 赞，统计于 2026-10-28

[`disintegration`](tags.md#tag-disintegration) [`smoke-effect`](tags.md#tag-smoke-effect) [`rooftop`](tags.md#tag-rooftop) [`sunset`](tags.md#tag-sunset) [`cinematic`](tags.md#tag-cinematic)

<details><summary><b>提示词</b></summary>

```text
Create an ultra-realistic cinematic portrait of a young man standing on a rooftop at sunset, wearing a light grey t-shirt, beige cargo pants, white high-top sneakers, a wristwatch, and black sunglasses. The subject stands in a calm side profile pose with hands in pockets, looking downward thoughtfully.

Apply a dramatic disintegration effect where the left side of his body transforms into swirling dark smoke, floating ash, glowing golden sparks, and particle fragments, blending naturally into the environment. Use a cloudy sunset sky with warm orange light, a distant city skyline, and a wet reflective ground surface.

Make the smoke highly detailed, volumetric, and realistic, with cinematic lighting, soft depth of field, high contrast, and photorealistic textures. The final image should have an epic fantasy-action mood, ultra-detailed 8K quality, and a seamless smoke-to-human transition effect.
```

</details>

<a id="nano-banana-y2k-wardrobe-flash-portrait"></a>
### 衣柜里的笑脸女孩，Y2K闪光快照

<a href="https://x.com/SimplyAnnisa/status/2083149439917867340"><img src="../../previews/nano-banana-y2k-wardrobe-flash-portrait.jpg" width="360"></a>

高俯拍视角配合直射闪光、胶片颗粒和轻微运动模糊，营造21世纪初狗仔快照的质感。具体描述衣柜杂物、闪光高光和配饰，让场景落到实处，相机风格则负责氛围。

Nano Banana 2 · 文生图 · 出处: [@SimplyAnnisa on X](https://x.com/SimplyAnnisa/status/2083149439917867340) · 98 赞，统计于 2026-10-29

[`y2k`](tags.md#tag-y2k) [`flash-photography`](tags.md#tag-flash-photography) [`film-grain`](tags.md#tag-film-grain) [`portrait`](tags.md#tag-portrait)

<details><summary><b>提示词</b></summary>

```text
Ultra-realistic candid dynamic portrait captured from a high top-angle perspective, creating a spontaneous, editorial fashion composition.

A young woman stands in a wardrobe/closet area, wearing a fitted light grey long-sleeve scoop-neck crop top with distressed, frayed white hem detailing and low-rise oversized grey ripped jeans, subtly revealing a delicate silver belly piercing. She accessorizes with thin silver oval-frame eyeglasses with clear lenses, medium-sized silver hoop earrings, and stacked silver rings. Her long oval-shaped nails feature a glossy soft pink manicure with elegant cream tortoiseshell accent nails.

Face & Skin
She has an elegant oval face with an extremely fair complexion and soft pink undertones. Her skin retains realistic pores and delicate natural freckles across the bridge of her nose and cheeks. The complexion appears luminous with a soft matte finish that preserves authentic skin texture without excessive retouching or artificial smoothing.

Makeup
Refined Clean Girl makeup featuring naturally full dark brows, subtle taupe eyeshadow, softly sculpted nose contour, diffused rosy blush blended across both cheeks and the bridge of the nose, and glossy overlined ombré pink lips with a wet reflective finish.
Her striking light sage-green eyes feature glass-like reflections and luxurious salon-quality manga-inspired lashes with ultra-defined D-curl spiky lash clusters. Thick upper and lower lashes, deep black mascara, crisp lash separation, and a bold doll-eye effect create dramatic yet realistic eye detail.

Hair
Deep side part with hip-length, sleek straight chestnut hair, exceptionally silky, thick, and glossy. The hair has soft natural movement with subtle flyaways and polished layering for a realistic editorial finish.

Pose & Expression
She stands with both hands resting confidently on her hips, creating a playful, dynamic silhouette. Her body is slightly angled while the camera looks down from above, emphasizing long legs and natural proportions. She looks directly into the camera with a joyful, playful, intentionally goofy ("ugly cute") expression—wide smile, expressive eyes, and an energetic candid vibe. The pose feels spontaneous, fun, and full of personality, as though captured in the middle of laughing.

Lighting
Harsh direct on-camera flash photography creates bright highlights, strong shadows, glowing overexposed skin, and high contrast, inspired by the early-2000s paparazzi aesthetic.

Camera Style
Point-and-shoot digital camera aesthetic with slight overexposure, authentic analog film grain, subtle sensor noise, slight motion blur, and slightly imperfect focus for a nostalgic Y2K snapshot feel.

Environment
Indoor wardrobe or dressing room with visible clothing racks, hanging garments, mirror reflections, and a dim cool-toned background. The setting feels authentic, lived-in, and naturally cluttered.

Mood & Vibe
Off-duty model, spontaneous, playful, intimate, candid, effortlessly stylish, Y2K fashion aesthetic, raw editorial energy, cinematic framing, shallow depth of field, realistic textures, analog film finish, and an authentic unfiltered moment.
```

</details>

<a id="nano-banana-sepia-flash-photobooth-linen-shirt-grid"></a>
### 亚麻衬衫棕褐闪光照相亭四宫格

<a href="https://x.com/SimplyAnnisa/status/2066054801226379621"><img src="../../previews/nano-banana-sepia-flash-photobooth-linen-shirt-grid.jpg" width="360"></a>

用参考图锁定人物身份，再逐格写明2x2四宫格每一格的姿势与视线。直闪加墙面硬阴影、棕褐色调以及相机镜头参数，共同营造复古拍立得质感。

Nano Banana 2 · 上传图改图 · 出处: [@SimplyAnnisa on X](https://x.com/SimplyAnnisa/status/2066054801226379621) · 97 赞，统计于 2026-10-29

[`photobooth`](tags.md#tag-photobooth) [`grid`](tags.md#tag-grid) [`sepia`](tags.md#tag-sepia) [`flash-photography`](tags.md#tag-flash-photography) [`identity-preserve`](tags.md#tag-identity-preserve)

<details><summary><b>提示词</b></summary>

```text
Nano banana 2

Create an ultra-realistic  using the reference image as the identity source.
Preserve the exact facial features, bone structure, proportions, skin tone, and identity of the subject.
Do not beautify, reshape, or alter the face in any way. Maintain natural likeness and authentic facial geometry.   Subject & Core Identity
An ultra-realistic, high-fidelity portrait of a 28-year-old woman with soft, defined facial structures, an elegant jawline, full natural lips, and expressive dark eyes. The subject possesses a distinct, unaltered facial identity that must be replicated with 100% accuracy, maintaining her natural features with zero modifications and absolutely no nose piercings.
Pose & Composition
Format: A 4-panel photo grid layout (2x2 matrix) showcasing a continuous sequence of candid poses in a photo-booth style.
Top-Left Panel: Close-up, side profile angled slightly toward the camera. Her right arm is raised, hand resting casually behind her head, pulling her hair up slightly. The white linen shirt drops slightly off her right shoulder.
Top-Right Panel: Side-profile view looking slightly off-camera to the left. A contemplative, elegant posture with a neutral gaze.
Bottom-Left Panel: A direct, slightly tilted head-on shot looking straight into the lens with a soft, confident tilt.
Bottom-Right Panel: Frontal shot, eyes closed, playfully puckering her lips in a kiss-face expression, with both hands raised, fingers running lightly through the sides of her hair.
Framing: Medium close-ups focusing on the upper torso, shoulders, and head.
Hairstyle & Makeup
Hairstyle: Long, voluminous brunette hair with soft, effortless waves and natural, layered movement. The texture is textured and slightly tousled, with a relaxed, effortless middle part and occasional loose strands framing her face.
Makeup: Minimalist, "no-makeup" makeup look. Subtle, natural brow definition, clean skin texture with a soft matte finish, light mascara enhancing the eyelashes, and a natural nude-toned lip color matching the subject’s authentic features perfectly.
Wardrobe & Styling
Attire: An oversized, relaxed-fit white linen button-down shirt. The fabric texture shows visible, realistic linen creases, weave patterns, and soft folds. The collar is loosely unbuttoned to create a casual, editorial look.
Accessories: Minimalist, classic styling including a delicate silver chain bracelet on the right wrist and a classic metal link watch on the left wrist. Subtle, small metallic hoop earrings.
Setting, Lighting & Atmosphere
Setting: A minimalist, clean studio setting against a solid, neutral off-white/light gray studio wall backdrop.
Lighting: Direct, high-contrast flash photography casting a soft, distinct shadow against the wall directly behind the subject, simulating an authentic polaroid or retro photo-booth flash. The lighting creates clean highlights on her skin, shoulders, and the fabric of the shirt.
Color Grading: Monochromatic desaturated tone with a warm, muted sepia-vintage tint, reminiscent of a classic 90s fashion polaroid or silver-halide film aesthetic.
Camera Details & Texture Boosters
Camera Hardware: Shot on a high-end mirrorless camera, Sony A7R V or Canon EOS R5, paired with an 85mm f/1.4 lens for a perfect portrait perspective with zero distortion.
Image Quality: Ultra-HD, 32K resolution, capturing hyper-detailed skin texture, individual hair strands, micro-folds in the linen fabric, and a subtle, authentic fine-grain film texture. Super-sharp focus on the facial features, preserving every authentic detail with lifelike cinematic realism.   Negative Prompt
low quality, blurry, flat lighting, dull colors, bad anatomy, extra limbs, distorted face, stiff pose, cartoon, anime, CGI, plastic skin, cheap costume, repetitive outfit, watermark, logo, text
```

</details>

<a id="nano-banana-mirror-hallway-satin-slip-woman"></a>
### 镜面走廊中穿白色缎面吊带裙的女子

<a href="https://x.com/KeorUnreal/status/2109735577436275182"><img src="../../previews/nano-banana-mirror-hallway-satin-slip-woman.jpg" width="360"></a>

提示词采用结构化 JSON，将主体、服装、次要人物、场景、光线与镜头分块描述，每一块都对应画面中可见的元素。把神秘人物放在镜面反射中并指定略高的自拍视角，使画面有纵深和层次。

Nano Banana 2.1 · 文生图 · 出处: [@KeorUnreal on X](https://x.com/KeorUnreal/status/2109735577436275182) · 94 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`structured-json`](tags.md#tag-structured-json) [`mirror-reflection`](tags.md#tag-mirror-reflection)

<details><summary><b>提示词</b></summary>

```text
{
  "subject": {
    "description": "Young woman with fair skin, dark wet-look hair falling over her shoulders, full lips slightly parted, looking toward the camera",
    "hair": "Dark brown hair with a wet, slicked appearance, partially covering one shoulder",
    "body": "Curvy figure with a glossy sheen on the skin",
    "pose": "Standing in a narrow hallway, both arms extended to the sides with hands resting on the wooden door frames, body facing the camera",
    "expression": "Calm, direct gaze with slightly parted lips"
  },
  "outfit": {
    "dress": "White satin slip short dress with a deep cowl neckline, ruched waist, and fitted silhouette",
    "accessories": "Small white quilted shoulder bag with a gold chain strap",
    "embroidery": "A small sign reading 'Keor' embroidered in elegant lettering along the border of the dress (on the neckline or side seam)"
  },
  "secondary_subject": {
    "description": "Mystery figure of a woman in a long red outfit with high heels and a hat that completely covers her face, giving a sense of mystery",
    "placement": "Standing further down the hallway or visible in a mirror reflection in the backdrop"
  },
  "setting": {
    "location": "Narrow wood-paneled hallway with mirrors",
    "background": "Warm wooden walls, multiple mirrors reflecting the subject, ceiling lights, white walls visible in reflections"
  },
  "lighting": {
    "type": "Warm indoor ceiling lighting",
    "effects": "Soft highlights on the satin dress and skin, gentle shadows in the hallway"
  },
  "camera": {
    "angle": "Slightly high selfie-style angle looking down the hallway",
    "framing": "Three-quarter body shot, subject centered between the mirrors, mystery figure visible in the background or reflection",
    "style": "Photorealistic, high-detail indoor photography, sharp focus"
  },
  "additional_details": {
    "skin": "Smooth with a dewy, slightly glossy finish",
    "atmosphere": "Intimate hallway portrait with a mysterious second figure"
  }
}
```

</details>

<a id="nano-banana-wet-profile-close-up-green-eyes"></a>
### 湿发侧脸特写，绿棕色眼睛

<a href="https://x.com/j_smeaton99/status/2039209681789595747"><img src="../../previews/nano-banana-wet-profile-close-up-green-eyes.jpg" width="360"></a>

通过上传的参考图锁定五官，同时明确指定水珠、汗珠和贴肤湿发等细节，使湿润质感更真实。限定高光只出现在眼睛和嘴唇，并指定冷灰色景深背景，让光线更可控。

Nano Banana 2 · 上传图改图 · 出处: [@j_smeaton99 on X](https://x.com/j_smeaton99/status/2039209681789595747) · 93 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`wet-skin`](tags.md#tag-wet-skin) [`water-droplets`](tags.md#tag-water-droplets) [`reference-photo`](tags.md#tag-reference-photo)

<details><summary><b>提示词</b></summary>

```text
Extreme wet close-up portrait. Young woman's face in profile (use uploaded pictures for proper reference) Dark wet hair naturally glued to the skin. Fine droplets of water and thin sweat glistening realistically on her face. Focus on bright natural green/hazel eyes with realistic reflection avoid excessive shine. Moist and shiny lips, soft natural texture. Soft lighting and cool shades with a light grey/white bokeh background colour. Keep same facial features
```

</details>

<a id="gpt-image-selfie-giant-portrait-beach-birthday-cake"></a>
### 海滩日落生日蛋糕后的巨幅人像

<a href="https://x.com/Adnan_Ai2/status/2104759717289681001"><img src="../../previews/gpt-image-selfie-giant-portrait-beach-birthday-cake.jpg" width="360"></a>

先用参考图锁定面部，再让大尺寸特写与坐在蛋糕上的小型全身像同框，形成比例错位的效果。牌子和蛋糕正面的文字逐字给出，并要求拼写清晰，字迹因此保持可读。

GPT Image 2.5 · 上传图改图 · 出处: [@Adnan_Ai2 on X](https://x.com/Adnan_Ai2/status/2104759717289681001) · 92 赞，统计于 2026-10-28

[`selfie`](tags.md#tag-selfie) [`miniature-world`](tags.md#tag-miniature-world) [`birthday-cake`](tags.md#tag-birthday-cake) [`golden-hour`](tags.md#tag-golden-hour) [`face-reference`](tags.md#tag-face-reference)

<details><summary><b>提示词</b></summary>

```text
Use the uploaded girl reference image as the exact facial and appearance reference. Create a highly detailed cinematic fantasy birthday portrait inspired by the provided cake-and-beach composition. Show the same girl in two versions: a large realistic close-up portrait rising behind the cake, and a smaller full-body version sitting naturally on top of the cake. Keep her recognizable facial features, hairstyle, soft smile, eyes, and overall appearance consistent with the reference image. Dress her in an elegant cozy cream-white knitted outfit with a soft feminine look.
Place everything on a beautiful beach during golden-hour sunset, with a glowing orange sky, soft clouds, ocean waves, warm sunlight, and cinematic reflections on the water. Create a huge luxurious round vanilla-and-chocolate drip cake in the foreground, covered with creamy white and chocolate frosting swirls, chocolate pieces, truffles, small decorative pearls, and realistic glossy chocolate drips. The small girl should sit naturally on the cake with a relaxed, cute pose, while the large portrait appears behind her with soft glowing edges and artistic depth.
Add a chocolate plaque beside the girl with the text “Girls Make Life Sweeter ♥” and write “Stay Awesome ♡” on the front of the cake with a small crown above it. Make the text clean, readable, and correctly spelled. Use realistic skin texture, detailed hair strands, natural fabric texture, accurate proportions, soft shadows, warm rim lighting, shallow depth of field, photorealistic details, premium editorial photography, dreamy cinematic color grading, 8K quality, highly polished composition, vertical portrait format.
```

</details>

<a id="nano-banana-colosseum-seated-man-golden-hour-portrait"></a>
### 夕阳下坐在罗马斗兽场矮墙上的男子

<a href="https://x.com/pictsbyai/status/2061848357283266661"><img src="../../previews/nano-banana-colosseum-seated-man-golden-hour-portrait.jpg" width="360"></a>

提示词用具体的肢体位置（左手放在大腿上，右手抓住左袖口）固定姿势，并指定一个45度左前方的单一光源及其投下的阴影，让光线保持一致。85mm镜头配大光圈让主体清晰锐利，背景中的地标仍可辨认但略微虚化。

Nano Banana 2 · 文生图 · 出处: [@pictsbyai on X](https://x.com/pictsbyai/status/2061848357283266661) · 92 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`golden-hour`](tags.md#tag-golden-hour) [`rome`](tags.md#tag-rome) [`menswear`](tags.md#tag-menswear)

<details><summary><b>提示词</b></summary>

```text
A young adult male sits calmly on a highly eroded, unfinished ancient stone wall, his body angled slightly to the right while his weight is comfortably centered. He wears a textured, off-white button-down shirt and deep brown trousers. His face bears a contemplative, confident expression with a neutral mouth and eyes focused distantly off to the right. His wavy brown hair features subtle, natural flyaways catching the warm light. His left hand rests naturally on his left thigh with loosely curled fingers, revealing a silver ring on the ring finger and a square-dial watch with a black leather strap, while his relaxed right hand reaches organically across his torso to gently grip and adjust the cuff of his left sleeve. He is layered over a monumental, deep background featuring the awe-inspiring architecture of the Roman Colosseum, its massive, weathered travertine stone arcades and interior ruins stretching expansively into the center and top of the frame. To the top left, the thriving dark green needle clusters of a Mediterranean pine tree and leafy midground bushes organically frame the ancient structures against a clear blue sky. The foreground seating wall beneath him features a rough, matte masonry surface of warm grays and earth tones, rich with pitted textures, deep crevices, and organic debris. A bright, highly directional single light source of warm golden hour sunlight pours in from a 45-degree front-left angle, creating a striking, high-contrast cinematic mood. This hard light preserves brilliant golden ochre highlights on the left side of his face, hair tips, left shoulder, and arm, while casting dramatic, deep black, harsh-edged shadows across the right side of his face, neck, and torso, including a distinct nose shadow cleanly defined on his right cheek. Shot as a realistic digital photograph on an 85mm lens at a wide aperture, the image maintains tack-sharp focus on the subject and the foreground stone's rugged texture, while a medium depth of field renders the architectural background slightly soft yet distinctly recognizable without any film grain. Post-processing enhances the warm golden and orange highlights, deepens the shadowy blacks for pronounced dramatic effect, and slightly lifts clarity on the fabric and masonry, perfectly encapsulating contemporary lifestyle travel portraiture framed in a 4:5 aspect ratio.
```

</details>

<a id="nano-banana-hooded-bw-eye-light-portrait"></a>
### 黑白兜帽人像与眼部光束

<a href="https://x.com/ChillaiKalan__/status/2073609440037597601"><img src="../../previews/nano-banana-hooded-bw-eye-light-portrait.jpg" width="360"></a>

堆叠的布光、镜头和调色术语（伦勃朗光、85mm f/1.8、高对比黑白）为模型提供了精确的摄影指令。兜帽变体将窄光束只打在眼部，背景设为纯黑，形成强烈的明暗对比。

Nano Banana 2 · 文生图 · 出处: [@ChillaiKalan__ on X](https://x.com/ChillaiKalan__/status/2073609440037597601) · 92 赞，统计于 2026-10-29

[`black-and-white`](tags.md#tag-black-and-white) [`fashion-portrait`](tags.md#tag-fashion-portrait) [`chiaroscuro`](tags.md#tag-chiaroscuro) [`studio-lighting`](tags.md#tag-studio-lighting)

<details><summary><b>提示词</b></summary>

```text
Ultra-realistic fine art black-and-white portrait, editorial fashion photography, close-up centered composition, direct eye contact, calm yet emotionally powerful expression, flawless natural skin texture with subtle freckles and pores, cinematic high-contrast monochrome grading, dramatic Rembrandt lighting with soft directional light, deep blacks and luminous highlights, razor-sharp eyes with catchlights, premium medium-format camera quality, 85mm portrait lens, f/1.8, shallow depth of field, museum-quality fine art photography, minimalist composition, timeless elegance, luxury Vogue-style editorial, rich tonal range, ultra-detailed facial features, photorealistic, HDR, 8K resolution, award-winning portrait photography.

Variation 1 (Underwater): Half-submerged underwater portrait, crystal-clear water surface crossing the forehead, natural water caustic light patterns dancing across the face and shoulders, floating hair, tiny air bubbles, soft underwater haze, blurred fish in the distant background, tranquil atmosphere, surreal yet realistic, monochrome fine-art aesthetic.

Variation 2 (Studio Hood): Black hooded outfit against a pure black background, narrow beam of light illuminating only the eyes and upper face, soft shadow falloff, symmetrical composition, dramatic chiaroscuro, elegant fashion editorial styling, mysterious cinematic mood, luxury magazine cover aesthetic.

Negative Prompt: low resolution, blurry, overprocessed skin, waxy face, plastic texture, extra limbs, deformed eyes, asymmetrical face, duplicated features, noisy image, oversharpened, artifacts, watermark, logo, text, cropped head, bad anatomy, unrealistic lighting, cartoon, CGI, low quality, distorted proportions.
```

</details>

<a id="nano-banana-seated-woman-fan-wall-vintage-portrait"></a>
### 女子坐在复古明星海报墙前的肖像

<a href="https://x.com/mehvishs25/status/2042256010040197281"><img src="../../previews/nano-banana-seated-woman-fan-wall-vintage-portrait.jpg" width="360"></a>

提示词用中景、居中构图和 35mm 胶片质感锁定画面与色调。背景描述为杂志剪贴拼贴墙，既交代场景又不点名任何人。

Nano Banana 2 · 文生图 · 出处: [@mehvishs25 on X](https://x.com/mehvishs25/status/2042256010040197281) · 92 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`film-look`](tags.md#tag-film-look) [`vintage`](tags.md#tag-vintage) [`warm-tones`](tags.md#tag-warm-tones)

<details><summary><b>提示词</b></summary>

```text
A cinematic portrait of a young elegant woman sitting in a softly lit room, medium shot, warm ambient lighting, vintage aesthetic. She sits calmly facing the camera with a subtle confident smile. Behind her is a wall covered with magazine cutouts and posters of famous actors and celebrities, creating a fan-wall collage. She is wearing an elegant, classy outfit — a long stylish skirt and refined top, sophisticated and graceful. Soft film grain, shallow depth of field, cozy indoor atmosphere, warm tones, cinematic color grading, realistic skin texture, 35mm film look, portrait photography, centered composition.
```

</details>

<a id="gpt-image-iphone-photo-woman-in-cafe"></a>
### 咖啡馆里女生的真实iPhone照片

<a href="https://x.com/blueemi99/status/2097602273085931662"><img src="../../previews/gpt-image-iphone-photo-woman-in-cafe.jpg" width="360"></a>

只点明拍摄设备和简单场景，就能触发随手拍的手机照片质感，包含暖色吊灯光、柔和虚化背景和托腮的自然姿态。极简提示词把构图交给模型，结果反而更自然。

GPT Image 2.5 · 文生图 · 出处: [@blueemi99 on X](https://x.com/blueemi99/status/2097602273085931662) · 91 赞，统计于 2026-10-28

[`iphone-photo`](tags.md#tag-iphone-photo) [`cafe`](tags.md#tag-cafe) [`candid`](tags.md#tag-candid) [`short-prompt`](tags.md#tag-short-prompt) [`realistic`](tags.md#tag-realistic)

<details><summary><b>提示词</b></summary>

```text
GPT Image 2.5

"make me a realistic iphone photo of a woman in a cafe"

I dont get how people are getting bad results from this model, genuinely few words prompt and looks so good and realistic
```

</details>

<a id="nano-banana-douyin-doll-top-down-selfie"></a>
### 俯拍自拍，娃娃妆女生躺在床上

<a href="https://x.com/kingofdairyque/status/2078461655726592211"><img src="../../previews/nano-banana-douyin-doll-top-down-selfie.jpg" width="360"></a>

先点名风格，再用具体细节把妆容和服装拆成清单，如衣服款式、美瞳颜色、假睫毛类型和腮红位置，模型更容易还原。开头和结尾都要求保持原脸，并给出俯拍、柔光等构图和光线指令。

Nano Banana 2 · 上传图改图 · 出处: [@kingofdairyque on X](https://x.com/kingofdairyque/status/2078461655726592211) · 91 赞，统计于 2026-10-29

[`douyin-makeup`](tags.md#tag-douyin-makeup) [`selfie`](tags.md#tag-selfie) [`top-down`](tags.md#tag-top-down) [`portrait`](tags.md#tag-portrait)

<details><summary><b>提示词</b></summary>

```text
Don't change her face original—100% authentic with perfect facial symmetry. She should have a youthful, feminine appearance. Create a captivating, intimate top-down portrait selfie inspired by the popular Douyin makeup aesthetic, featuring a young woman lying comfortably on her back in a relaxed pose that radiates femininity and grace. The image is captured directly from above in a slightly tilted bird's-eye perspective, creating a spontaneous, alluring composition focused entirely on her captivating facial features and her direct gaze into the camera. She looks at the lens with wide, sharp eyes and a calm, relaxed expression without an open smile, giving the portrait a mysterious, dramatic, and confident mood. Her makeup follows the signature Douyin doll style with enchanting gray or light-blue colored contact lenses, long, thick, wispy manga-style false lashes, highlighted aegyo-sal to make the eyes appear larger and more alluring, and perfectly brushed, precisely defined eyebrows. Intense pink blush is generously applied beneath the eyes, across the cheeks, and over the tip of the nose to create a soft, flushed complexion, while a delicate beauty mark is clearly visible on the right side of her nose tip. Her lips are full, well-defined, and finished in a matte berry-pink shade that enhances their soft, attractive shape. She wears a fitted, short-sleeved ribbed Henley-style top in light gray with a wide open neckline and small front buttons. Her thick, dark chocolate-brown hair falls naturally in a loose, messy style across the pillow surrounding her head and forehead, emphasizing the relaxed atmosphere. She is lying on a cozy bed or sofa with a soft white or cream-colored pillow featuring an embossed textured pattern behind her head. Soft, diffused indoor lighting evenly illuminates her face, highlighting her velvety skin texture and intricate makeup details without harsh shadows, creating an intimate, cozy mood. Preserve her original facial features exactly without any alteration. Ultra-realistic, HD image quality, 9:16 aspect ratio.
```

</details>

<a id="nano-banana-peony-bouquet-terracotta-portrait"></a>
### 赭红背景下手捧巨型芍药花束的女子

<a href="https://x.com/TheVirtualMuse/status/2109224903732089215"><img src="../../previews/nano-banana-peony-bouquet-terracotta-portrait.jpg" width="360"></a>

开头用身份锁定段落保住参考图的面部特征，随后逐种列出花材，用百分比限定构图占比，并以具体相机镜头和光线方向定下质感。

Nano Banana 2.1 · 上传图改图 · 出处: [@TheVirtualMuse on X](https://x.com/TheVirtualMuse/status/2109224903732089215) · 90 赞，统计于 2026-10-28

[`floral`](tags.md#tag-floral) [`fashion-editorial`](tags.md#tag-fashion-editorial) [`identity-lock`](tags.md#tag-identity-lock) [`golden-hour`](tags.md#tag-golden-hour) [`studio-portrait`](tags.md#tag-studio-portrait)

<details><summary><b>提示词</b></summary>

```text
Using the uploaded reference image as the ONLY facial identity source, create an ultra-realistic, high-end luxury fashion editorial portrait featuring the exact same person holding an oversized, beautifully arranged floral bouquet.

MASTER IDENTITY LOCK (CRITICAL):

Preserve the reference person's facial identity with maximum possible accuracy. Maintain the exact facial structure, eye shape, eyebrows, nose, lips, jawline, cheekbones, natural skin tone, age, and recognizable facial characteristics.

Retain authentic skin texture, visible pores, natural facial asymmetry, and realistic imperfections. No beautification, facial reconstruction, artificial skin smoothing, or identity changes.

SUBJECT & STYLING:

The woman stands elegantly against a warm, burnt-terracotta studio backdrop, wearing a luxurious oversized beige tailored blazer with structured shoulders, notched lapels, refined stitching, and realistic linen-wool fabric texture.

Her dark brown hair is styled in a voluminous, softly tousled side-parted bob with natural movement, individual flyaway strands, and realistic shine.

Minimal sophisticated makeup, softly defined eyebrows, natural eyelashes, subtle warm blush, and muted nude-pink lips.

Her expression is calm, intimate, and effortlessly confident, looking directly into the camera.

FLORAL ARRANGEMENT (CRITICAL):

She holds an enormous, luxurious asymmetrical bouquet covering most of her upper torso and partially concealing the left side of her face.

The arrangement features:

Large, fully bloomed coral-pink peonies with intricate layered petals and golden centers.

Three prominent ivory-white anthurium flowers with delicate veining, glossy sculptural petals, and pale cream spadices.

Smaller blush-pink peonies and unopened flower buds.

Delicate dried pink astilbe and soft peach botanical fillers.

Pale ivory blossoms scattered naturally throughout the arrangement.

Sculptural dried golden palm leaves extending upward between the flowers.

Every flower must display extraordinary botanical realism, natural petal translucency, delicate imperfections, and physically accurate textures.

The bouquet is wrapped in oversized, sculptural charcoal-black textured floral paper with dramatic angular folds, finished with a long, luxurious matte-black satin ribbon tied into an elegant bow.

POSE & COMPOSITION:

Vertical medium portrait, framed from the upper thighs to slightly above the head.

The subject stands slightly right of center, holding the bouquet naturally across her chest with both arms.

The bouquet dominates the left and central portions of the composition.

One large white anthurium partially overlaps her left eye and cheek, while her right eye remains clearly visible and sharply focused.

Her face emerges naturally from behind the flowers, creating an intimate, mysterious editorial composition.

The flowers occupy approximately 60% of the frame, with the subject's face positioned in the upper-right third.

LIGHTING & ATMOSPHERE:

Dramatic late-afternoon sunlight enters from the upper left, producing warm directional illumination across her face, blazer, and flowers.

Strong yet naturally softened shadows create beautiful dimensional contrast.

Distinct botanical shadows fall across her beige blazer and the terracotta wall behind her.

Rich burnt-orange background tones contrast elegantly with the ivory flowers, coral-pink peonies, beige tailoring, and deep-black bouquet wrapping.

Authentic golden-hour warmth, sophisticated editorial contrast, subtle film grain, natural highlight roll-off, and rich cinematic shadows.

CAMERA & IMAGE QUALITY:

Photographed as a real luxury fashion campaign using a Hasselblad X2D 100C medium-format camera with an 80mm portrait lens.

f/2.8 aperture, ISO 100, realistic optical depth of field, precise eye focus, beautifully resolved flower details, and subtle background softness.

Premium Vogue-inspired floral fashion photography, authentic medium-format rendering, refined luxury magazine color grading, extraordinary photographic detail, realistic dynamic range, and natural skin tones.

8K-quality appearance, exceptionally sharp where focused, physically accurate materials, realistic hands and fingers, and professional studio photography.

FINAL REQUIREMENTS:

The final result must look like an authentic photograph captured by a world-class fashion photographer, not an AI-generated image.

Preserve natural human anatomy, believable flower proportions, realistic shadows, and accurate fabric behavior.

No CGI, 3D rendering, illustration, plastic skin, excessive retouching, artificial HDR, oversaturation, distorted facial features, unnatural hands, duplicated flowers, text, logos, or watermarks.

Aspect Ratio: 9:16 vertical.
```

</details>

<a id="nano-banana-olive-sweater-terracotta-studio-portrait"></a>
### 橄榄绿毛衣与米色长裤的坐姿棚拍人像

<a href="https://x.com/frametheory058/status/2061830756364947855"><img src="../../previews/nano-banana-olive-sweater-terracotta-studio-portrait.jpg" width="360"></a>

通过锁定参考图的姿势、构图和手部位置，只替换人物身份与服装，避免模型重新构图。陶土到浅沙色的背景与橄榄绿和米色服装相呼应，相机与镜头参数则增强摄影写实感。

Nano Banana 2 · 上传图改图 · 出处: [@frametheory058 on X](https://x.com/frametheory058/status/2061830756364947855) · 89 赞，统计于 2026-10-29

[`studio-portrait`](tags.md#tag-studio-portrait) [`reference-pose`](tags.md#tag-reference-pose) [`fashion-photo`](tags.md#tag-fashion-photo) [`color-palette`](tags.md#tag-color-palette)

<details><summary><b>提示词</b></summary>

```text
Create an ultra premium studio portrait using the uploaded person’s REAL face, hairstyle, beard style, and facial identity. Do NOT copy the reference model’s facial features or hair. Preserve the uploaded person’s natural appearance completely.

Match only the EXACT sitting pose, body angle, hand placement, camera framing, composition, and relaxed posture from the reference image. Maintain the same modern editorial studio aesthetic and confident lifestyle vibe.

Dress the person in a luxurious olive green knitted sweater paired with tailored beige trousers. The background should be a smooth warm terracotta-to-soft sand gradient studio backdrop that perfectly complements the outfit tones and creates a premium harmonious color palette.

Lighting should be soft professional studio lighting with subtle warm highlights, realistic shadows, cinematic depth, and clean luxury contrast. Keep the mood minimal, modern, stylish, and highly Instagram-worthy.

Ultra realistic skin texture, natural body proportions, premium fashion photography style, shallow depth of field, soft background blur, realistic fabric texture, luxury creator-brand photoshoot aesthetic.

Shot on Sony A7 IV, 50mm lens, f/2.2, photorealistic, ultra detailed, high-end color grading, editorial magazine quality, 8k.
```

</details>

<a id="gpt-image-selfie-chibi-self-painting-cheek-canvas"></a>
### 自拍中画布上的Q版自己为她涂画脸颊

<a href="https://x.com/Arina_hoqe/status/2098966830874595582"><img src="../../previews/gpt-image-selfie-chibi-self-painting-cheek-canvas.jpg" width="360"></a>

提示词按发型、面部、服装、概念、Q版形象、背景、风格、镜头分块，让真人与画中的自己保持一致。相同的颜料飞溅和打破第四面墙的动作把写实照片与3D Q版插画融为一体，面部参考规则则保留上传照片中的人物特征。

GPT Image 2.5 · 上传图改图 · 出处: [@Arina_hoqe on X](https://x.com/Arina_hoqe/status/2098966830874595582) · 85 赞，统计于 2026-10-28

[`selfie`](tags.md#tag-selfie) [`chibi`](tags.md#tag-chibi) [`paint-splatter`](tags.md#tag-paint-splatter) [`fourth-wall`](tags.md#tag-fourth-wall) [`art-studio`](tags.md#tag-art-studio)

<details><summary><b>提示词</b></summary>

```text
Study the uploaded photo’s facial features and use them as inspiration to create a fun selfie-style photo of a similar-looking young woman with a creative cartoon canvas twist.

Hair: Messy, tousled dark hair with colorful paint splatters scattered naturally across the hair and face, soft loose strands, light natural texture.

Face/Skin: Preserve the recognizable facial features and overall identity from the reference image while creating a female version. Natural youthful skin with colorful paint speckles in purple, orange, and blue across the face. Big laughing open-mouth smile, playful joyful expression, expressive eyes, natural feminine appearance, no jewelry, no tattoos.

Outfit: Purple/lavender knit sweater, casual artistic look with colorful paint splatters on the clothing.

Concept: Taking a close-up selfie next to an easel canvas, where a cute chibi cartoon version of herself is painted on the canvas. The illustrated cartoon character is playfully reaching out of the canvas, holding a paintbrush and painting/touching the real woman’s cheek with colorful paint, creating a fun fourth-wall-breaking interaction between the real person and the illustration.

Chibi Cartoon on Canvas: A cute female chibi version of the same woman, with the same messy dark hair, colorful paint splatters, big expressive cartoon eyes, cheerful laughing smile, wearing a purple/lavender off-shoulder top. She is leaning out of the canvas frame with one arm extended, holding a paintbrush and playfully touching the real woman’s cheek.

Background: Cozy creative art studio, softly blurred art supplies, colorful paint bottles, brushes, canvases, and wooden shelves in the background. Warm natural window lighting. Wooden easel with clearly visible paint-splattered edges.

Art Style: Photorealistic selfie photography seamlessly blended with a vibrant high-quality 3D chibi cartoon illustration. Realistic skin texture, natural facial details, colorful paint-splatter texture throughout, playful energetic composition, premium photography, high detail.

Camera: Close-up selfie perspective, slightly wide-angle lens, natural handheld selfie framing, capturing both the real woman’s face and the full interaction with the canvas painting. Realistic depth of field, cinematic lighting, sharp facial details.

Face Reference Rules: Use the uploaded image as the primary facial reference. Preserve the same recognizable facial structure, eyes, nose, lips, face shape, skin tone, and overall identity as closely as possible. Do not replace the identity with a generic face. Keep the woman looking naturally like the reference person while adapting the appearance into a feminine version of the concept.

Text Overlay: Small stylish signature-style text in the top corner reading exactly: “Arina Ai”

Negative Prompt: blurry face, distorted facial features, extra fingers, extra limbs, duplicate person, deformed hands, bad anatomy, jewelry, tattoos, masculine body, plastic skin, unrealistic face, anime real person, low quality, excessive makeup, text errors, misspelled “Arina Ai”, watermark, logo.
```

</details>

<a id="nano-banana-london-townhouse-street-style-identity-lock"></a>
### 伦敦联排屋前的皮夹克街拍人像

<a href="https://x.com/iamrealsnow/status/2107680165736468917"><img src="../../previews/nano-banana-london-townhouse-street-style-identity-lock.jpg" width="360"></a>

开头先把面部、发型和身材比例锁定到参考图，再逐项写明地点、门和铁栏杆以及每件服装的材质。结尾补上阴天光线、50mm 镜头、浅景深、胶片颗粒和禁止文字水印的约束。

Nano Banana 2.1 · 上传图改图 · 出处: [@iamrealsnow on X](https://x.com/iamrealsnow/status/2107680165736468917) · 85 赞，统计于 2026-10-28

[`street-style`](tags.md#tag-street-style) [`fashion`](tags.md#tag-fashion) [`identity-reference`](tags.md#tag-identity-reference) [`london`](tags.md#tag-london) [`photorealistic`](tags.md#tag-photorealistic)

<details><summary><b>提示词</b></summary>

```text
Use the reference image as the exact identity reference. Preserve the subject’s facial identity, facial proportions, hairstyle, body proportions and natural appearance. Create a photorealistic high-fashion street-style photograph in London. The subject is standing outside a classic British townhouse with a muted blue-gray paneled door and black wrought-iron railings. She wears a fitted black ribbed turtleneck, oversized dark brown vintage leather jacket with a soft shearling collar, brown mini skirt, and carries a structured dark brown leather handbag with gold hardware. Oversized dark sunglasses, minimal makeup, effortless model-off-duty expression. Overcast natural daylight, muted neutral color palette, realistic shadows, authentic leather texture, subtle film grain, editorial fashion photography, candid street photography, 50mm lens, shallow depth of field, extremely photorealistic, no text, no watermark.
```

</details>

<a id="nano-banana-cafe-woman-matcha-candid-portrait"></a>
### 年轻女子在咖啡馆享用抹茶拿铁

<a href="https://x.com/Sairah_0/status/2050817729767276713"><img src="../../previews/nano-banana-cafe-woman-matcha-candid-portrait.jpg" width="360"></a>

具体道具、简单穿搭和柔和日光锁定场景，candid 一词要求随性、未摆拍的质感。浅景深与生活方式取景让画面接近真实的手机抓拍。

Nano Banana 2 · 文生图 · 出处: [@Sairah_0 on X](https://x.com/Sairah_0/status/2050817729767276713) · 83 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`cafe`](tags.md#tag-cafe) [`lifestyle`](tags.md#tag-lifestyle) [`natural-light`](tags.md#tag-natural-light)

<details><summary><b>提示词</b></summary>

```text
A stylish young woman sitting in the driver’s seat of a luxury convertible car with a red leather interior, parked in front of an elegant modern building. She wears a black sheer blouse and slim black sunglasses, with wavy brown hair and minimal makeup. She turns back over her shoulder, giving a confident, composed look toward the camera. The setting has clean architectural lines and muted colors, enhancing a high-fashion, editorial vibe. Shot in soft daylight, cinematic composition, ultra-realistic, sharp focus, luxury aesthetic.
```

</details>

<a id="gpt-image-lace-dress-cafe-window-portrait"></a>
### 蕾丝连衣裙女子坐在咖啡馆窗边

<a href="https://x.com/DaniaSafvi/status/2071477298944164056"><img src="../../previews/gpt-image-lace-dress-cafe-window-portrait.jpg" width="360"></a>

从窗外隔着玻璃拍摄，让街景反光叠加在温暖的室内之上，形成层次与抓拍感。指定相机与镜头（Sony A7R V、85mm f/1.4）并加入皮肤质感描述，可以让画面更接近真实摄影。

GPT Image 2 · 文生图 · 出处: [@DaniaSafvi on X](https://x.com/DaniaSafvi/status/2071477298944164056) · 82 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`cafe`](tags.md#tag-cafe) [`glass-reflection`](tags.md#tag-glass-reflection) [`bokeh`](tags.md#tag-bokeh)

<details><summary><b>提示词</b></summary>

```text
Ultra-realistic cinematic street portrait photography, 9:16 vertical ratio. A young Asian woman with fair, bright skin sitting alone inside a modern cafe near a large glass window facing the city street.
Pose: sitting sideways on a chair, body slightly turned away from the camera, head turned back to gaze directly at the camera with a calm, elegant, and mysterious expression. And one of her hands is resting on her chin. Wearing a white embroidered lace dress.
Long, voluminous black hair cascading naturally, minimal natural makeup.
The shot is taken from outside the cafe through the glass window, creating a soft reflection of vehicles, city buildings, and pedestrians on the glass surface. A small wooden table beside her with a cup of white coffee and a glass of latte. The cafe interior is warm with golden-yellow round pendant lights producing large, soft bokeh. The city background appears blurred with a shallow depth of field.
Natural spotlight from nighttime street lamps, soft ambient light, cinematic mood, muted colors, premium editorial photography, candid lifestyle shot, realistic skin texture, healthy skin with visible natural pores, high detail face, sharp eyes, soft shadows, creamy bokeh, glass reflection effect, shallow depth of field, Sony A7R V, 85mm f/1.4 lens, photorealistic, HDR, 8K, masterpiece, highly detailed, magazine-quality street cafe portrait.
```

</details>

<a id="nano-banana-embroidered-dress-beige-tile-portrait"></a>
### 微笑女性身穿刺绣长裙立于米色瓷砖墙前

<a href="https://x.com/HaniaAi12/status/2060664884035981663"><img src="../../previews/nano-banana-embroidered-dress-beige-tile-portrait.jpg" width="360"></a>

用精确的主体描述叠加光线、景深和调色提示，例如柔和日光、浅景深和暖色调，能生成可信的写实人像。明确写出服装配色与米色瓷砖墙，可以让色彩和背景与画面保持一致。

Nano Banana 2 · 文生图 · 出处: [@HaniaAi12 on X](https://x.com/HaniaAi12/status/2060664884035981663) · 82 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`photorealistic`](tags.md#tag-photorealistic) [`fashion`](tags.md#tag-fashion) [`natural-light`](tags.md#tag-natural-light)

<details><summary><b>提示词</b></summary>

```text
A beautiful young woman with fair skin and long, silky dark-brown hair cascading over her shoulders, standing in front of a modern beige tiled wall. She wears a stylish black embroidered ethnic dress featuring vibrant red and orange floral patterns. Soft natural daylight illuminates her face, creating a warm, glowing complexion with subtle makeup and a gentle smile. Ultra-realistic portrait photography, shallow depth of field, soft cinematic lighting, high-detail skin texture, elegant and graceful expression, warm color grading, aesthetic social media reel style, 4K quality, DSLR photography, natural beauty, dreamy atmosphere, highly detailed, photorealistic.
```

</details>

<a id="nano-banana-low-key-studio-portrait-black-backdrop"></a>
### 纯黑背景下的低调影棚人像

<a href="https://x.com/john_my07/status/2107801411711123546"><img src="../../previews/nano-banana-low-key-studio-portrait-black-backdrop.jpg" width="360"></a>

单侧方向光让半边脸渐隐在阴影中，背景为无缝纯黑。点名毛孔和绒毛等皮肤细节，再配合35mm镜头与胶片颗粒，让画面更像真实摄影而非光滑的AI皮肤。

Nano Banana 2.1 · 文生图 · 出处: [@john_my07 on X](https://x.com/john_my07/status/2107801411711123546) · 82 赞，统计于 2026-10-28

[`portrait`](tags.md#tag-portrait) [`low-key`](tags.md#tag-low-key) [`studio-lighting`](tags.md#tag-studio-lighting) [`photorealistic`](tags.md#tag-photorealistic) [`skin-texture`](tags.md#tag-skin-texture)

<details><summary><b>提示词</b></summary>

```text
Create an ultra-realistic, high-end cinematic portrait of a beautiful young woman, framed in a tight head-and-shoulders composition. She faces the camera directly with a calm yet intense expression and a confident, captivating gaze.

Use dramatic low-key studio lighting with a strong directional light illuminating one side of her face while the opposite side gradually disappears into deep, atmospheric shadow. Keep the background completely black and seamless, creating a striking contrast around her silhouette.

Her eyes are deep brown with subtle geometric catchlights. Give her naturally textured, slightly damp-looking hair with individual strands visible and realistic volume. She wears a simple, elegant black crew-neck top with no visible logos or patterns.

Capture extremely realistic skin with visible pores, fine facial texture, subtle imperfections, delicate peach fuzz, natural lips, and detailed eyelashes. Avoid overly smooth or plastic-looking skin.

Photographed with a cinematic 35mm lens aesthetic, shallow depth of field, soft optical falloff, realistic tonal range, subtle analog film grain, and premium editorial photography quality. The final image should feel like an authentic photograph captured in a professional studio — sophisticated, raw, atmospheric, and completely photorealistic, with no obvious AI-generated appearance.
```

</details>

<a id="nano-banana-striped-tee-blue-eyes-portrait"></a>
### 黑长发女性身穿绿白条纹T恤微笑

<a href="https://x.com/Zarlish_Shahid/status/2079734611962405293"><img src="../../previews/nano-banana-striped-tee-blue-eyes-portrait.jpg" width="360"></a>

相机与镜头参数（DSLR、85mm、浅景深、柔和阳光）锁定写实摄影风格，逐项描述的外貌特征让人物形象具体且稳定。

Nano Banana 2 · 文生图 · 出处: [@Zarlish_Shahid on X](https://x.com/Zarlish_Shahid/status/2079734611962405293) · 82 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`photorealism`](tags.md#tag-photorealism) [`85mm-lens`](tags.md#tag-85mm-lens) [`soft-sunlight`](tags.md#tag-soft-sunlight)

<details><summary><b>提示词</b></summary>

```text
A breathtakingly beautiful young woman with long silky black hair, mesmerizing large crystal-blue eyes, flawless fair glowing skin, soft rosy pink lips, naturally defined eyebrows, and a gentle heartwarming smile. She is wearing a stylish green and white T-shirt. Ultra-realistic face, perfect symmetrical features, soft natural makeup, cinematic lighting, shallow depth of field, elegant pose, luxurious hair, photorealistic, DSLR portrait, 85mm lens, soft sunlight, highly detailed skin texture, masterpiece, 8K, ultra HD, realistic photography.
```

</details>

<a id="gpt-image-cafe-golden-hour-over-shoulder-portrait"></a>
### 透过前景虚化人物的金色光咖啡馆人像

<a href="https://x.com/mehvishs25/status/2105280094994587829"><img src="../../previews/gpt-image-cafe-golden-hour-over-shoulder-portrait.jpg" width="360"></a>

两个虚化的前景人物形成过肩取景，像从缝隙中偷拍，85mm f/1.4 浅景深把焦点锁在眼睛上。逆光金色阳光加上点名的胶片型号（Portra 400、Gold 200）、颗粒和光晕，营造出温暖的胶片质感。

GPT Image 2.5 · 文生图 · 出处: [@mehvishs25 on X](https://x.com/mehvishs25/status/2105280094994587829) · 78 赞，统计于 2026-10-28

[`candid-portrait`](tags.md#tag-candid-portrait) [`golden-hour`](tags.md#tag-golden-hour) [`film-look`](tags.md#tag-film-look) [`bokeh`](tags.md#tag-bokeh) [`cafe`](tags.md#tag-cafe)

<details><summary><b>提示词</b></summary>

```text
Candid cinematic portrait of a woman with a warm, playful, knowing smile, seated at a café table and looking directly at the camera through a gap between two out-of-focus people in the foreground. She has voluminous, tousled, shoulder-length curly hair in honey-brown and caramel tones with sun-lightened highlights, messy shaggy curtain bangs falling across her forehead and eyes, strands catching the light like a glowing halo. Her skin is sun-kissed and warm, with natural texture, minimal makeup, a soft muted-rose lip, and a slight smirk that reads as relaxed and flirtatious. She wears a black oversized knit cardigan or soft black jacket, layered with delicate thin gold necklaces of different lengths.
On the wooden table in front of her sits a white-lidded brown paper takeaway coffee cup, and beside it a small glass of amber tea. In the extreme foreground, blurred shoulders and heads frame the shot: on the left, a person in a striped beanie and white t-shirt, on the right, a person in a dark brown top with dark curly hair, both heavily out of focus.
Setting: a sunlit café interior beside a large window, with a blurred street scene, a soft peach and white building, and a pale sky visible outside.
Lighting: Strong golden-hour sunlight pouring in from the side and behind, creating a glowing rim light through her hair, warm orange highlights across her face, and deep chocolate-brown shadows. Sun-drenched, hazy, slightly overexposed highlights with a soft bloom.
Style / Mood: Warm, nostalgic, effortless, and intimate. Candid lifestyle photography with a "captured in the moment" feel. Analog film aesthetic, Kodak Portra 400 / Kodak Gold 200 look, visible film grain, lifted warm blacks, rich amber, honey, and brown color palette, gentle halation and lens glow.
Camera details: 85mm f/1.4 lens, very shallow depth of field, sharp focus on her eyes and face, layered foreground bokeh (over-the-shoulder framing), vertical 4:5 composition, eye-level shot, slight vignette.
```

</details>

<a id="nano-banana-sunflower-wooden-frame-portrait"></a>
### 蓄须男子站在向日葵田的木质相框中

<a href="https://x.com/AiWithTariq/status/2068925139111358658"><img src="../../previews/nano-banana-sunflower-wooden-frame-portrait.jpg" width="360"></a>

提示词用具体的裁切、相框角度和前景虚化锁定构图，并加上保留原样的指令，让编辑时保持取景、服装和光晕不被重画。

Nano Banana 2 · 上传图改图 · 出处: [@AiWithTariq on X](https://x.com/AiWithTariq/status/2068925139111358658) · 75 赞，统计于 2026-10-29

[`sunflower`](tags.md#tag-sunflower) [`portrait`](tags.md#tag-portrait) [`soft-focus`](tags.md#tag-soft-focus) [`framing`](tags.md#tag-framing)

<details><summary><b>提示词</b></summary>

```text
Gpt Image 2 | Nano banana 2 | Grok | Gemini Prompt 👇

A very tight vertical frame with strong crop pressure, the subject positioned inside a dense sunflower and orange flower field while partially framed by a large tilted wooden picture frame near the center of the image. Large blurred sunflower blooms dominate the upper-right foreground and left foreground edges, partially blocking the frame and subject. The wooden frame leans diagonally from lower-left toward upper-right, surrounding the face and upper torso area while several edges are cropped by foreground flowers and frame borders. Pale blue sky with soft white clouds occupies the upper-left background, with dense green foliage and orange flowers filling the lower and middle background. Preserve the exact asymmetrical placement and tight crop without revealing more body or environment. The face appears near the upper-center area inside the wooden frame, tilted slightly downward toward viewer’s left, eyes open wide directed toward the camera axis, pupils centered, lips softly closed with a slight pout shape and faint glossy pink color. Makeup is soft and bright with pale pink blush, peach-pink eyeshadow, subtle eyeliner, glossy pink lips, smooth bright skin with warm highlights. Small flower stickers remain visible on the cheek. Dark medium-length hair falls around both sides of the face and shoulder area with loose strands near the forehead and cheek, a yellow flower accessory tucked into the hair near the viewer’s left side of the head. One hand grips the lower-left side of the wooden frame while the other arm remains lower and partly hidden by flowers and leaves. Clothing must remain unchanged: a vivid cobalt-blue short-sleeve knit top, close-fitting over the upper torso, with a simple round crew neckline sitting close to the base of the neck, smooth fine-knit fabric texture, short sleeves ending around the upper arm, sleeve edges slightly curved around the arms, fabric softly stretched across the chest and shoulder area with mild natural folds and highlights, no visible logo or pattern. Dense sunflower leaves and stems overlap the lower foreground and right side with several leaves and flowers heavily blurred and cropped by the frame edges. Bright warm sunlight creates strong dreamy haze, pale overexposed highlights, and soft translucent lens flare artifacts near the upper-left and lower-left areas. Dreamy soft-focus image quality, reduced edge sharpness, shallow depth of field, blurred foreground flowers, and soft yellow-green background separation. Preserve the soft haze, bloom lighting, blur, overexposed highlights, and dreamy low-detail quality exactly as visible.
```

</details>

<a id="gpt-image-1980s-fashion-editorial-red-suit-portrait"></a>
### 红色西装的八十年代时尚杂志人像

<a href="https://x.com/mehvishs25/status/2098090489811746853"><img src="../../previews/gpt-image-1980s-fashion-editorial-red-suit-portrait.jpg" width="360"></a>

用参考图锁定面部身份，再逐项写出年代服装与配饰来定义八十年代造型。影棚背景、暖色模拟光、胶片颗粒和镜头柔化营造杂志质感，结尾的排除清单避免现代元素混入。

GPT Image 2.5 · 上传图改图 · 出处: [@mehvishs25 on X](https://x.com/mehvishs25/status/2098090489811746853) · 74 赞，统计于 2026-10-28

[`1980s`](tags.md#tag-1980s) [`fashion-editorial`](tags.md#tag-fashion-editorial) [`film-grain`](tags.md#tag-film-grain) [`reference-image`](tags.md#tag-reference-image) [`vintage`](tags.md#tag-vintage)

<details><summary><b>提示词</b></summary>

```text
Create a vertical, ultra-photorealistic portrait of the same clearly adult woman from the reference image, preserving her facial identity, facial structure, skin tone, hair characteristics, and overall appearance.

Give her an authentic 1980s fashion-editorial look with a confident, effortless attitude. She is posing confidently with relaxed shoulders, strong posture, and a subtle self-assured expression, looking directly toward the camera. Her pose should feel natural and charismatic rather than overly staged.

Style her in an elegant vintage 80s outfit: a sophisticated fitted top or blouse with tasteful coverage, high-waisted trousers or a classic high-waisted skirt, subtle shoulder structure, and period-accurate accessories such as small statement earrings, a delicate necklace, and a vintage wristwatch. Use rich but tasteful 1980s colors and textures.

Set the scene in a classic 1980s studio fashion environment, with a softly textured backdrop, warm analog lighting, gentle film grain, subtle lens softness, and authentic vintage color rendering. The overall aesthetic should resemble a high-end fashion photograph from an 80s magazine—glamorous, confident, sophisticated, and nostalgic.

Natural skin texture, realistic fabric detail, authentic proportions, realistic hands, cinematic lighting, 35mm film photography aesthetic, subtle grain, soft highlights, shallow depth of field, no modern objects, no contemporary styling, no text or watermark.
```

</details>

<a id="nano-banana-half-face-soccer-ball-stitch-portrait"></a>
### 半张脸与半个足球缝合的写实肖像

<a href="https://x.com/ShamsAmin56/status/2066220842485469445"><img src="../../previews/nano-banana-half-face-soccer-ball-stitch-portrait.jpg" width="360"></a>

[Player Full Name] 占位符让同一条提示词可以套用到任意球员。细致描述皮肤毛孔、汗水以及足球面板与缝线，让人脸与皮革的交界看起来真实，纯白无缝背景和 9:16 棚拍构图则保持画面干净。

Nano Banana 2 · 文生图 · 出处: [@ShamsAmin56 on X](https://x.com/ShamsAmin56/status/2066220842485469445) · 74 赞，统计于 2026-10-29

[`surreal-composite`](tags.md#tag-surreal-composite) [`soccer`](tags.md#tag-soccer) [`template`](tags.md#tag-template) [`portrait`](tags.md#tag-portrait)

<details><summary><b>提示词</b></summary>

```text
Ultra-realistic photorealistic portrait of [Player Full Name]'s half face seamlessly stitched to half of a classic soccer ball, intricate stitching details where skin meets leather, highly detailed skin texture, pores, sweat, realistic football panels and seams, dramatic cinematic lighting, sharp focus, white seamless background, 9:16 aspect ratio, professional studio photography, 4k resolution.

Super Easy to Edit:

Replace [Player Full Name] with the player’s name.
Example: Cristiano Ronaldo

Disclaimer:
AI-generated images • Creative artistic concept • Not a real photo or real stitches.
```

</details>

<a id="nano-banana-mirror-selfie-sofa-warm-light"></a>
### 沙发上女子暖光镜面自拍

<a href="https://x.com/j_smeaton99/status/2050418977697145019"><img src="../../previews/nano-banana-mirror-selfie-sofa-warm-light.jpg" width="360"></a>

参考图锁定面部身份，提示词再用构图、姿势和前置摄像头画质来约束画面。裁掉下半身，并要求颗粒感与浅景深，让照片更像随手拍而不是棚拍。

Nano Banana 2 · 上传图改图 · 出处: [@j_smeaton99 on X](https://x.com/j_smeaton99/status/2050418977697145019) · 74 赞，统计于 2026-10-29

[`selfie`](tags.md#tag-selfie) [`mirror`](tags.md#tag-mirror) [`portrait`](tags.md#tag-portrait) [`warm-lighting`](tags.md#tag-warm-lighting)

<details><summary><b>提示词</b></summary>

```text
Ultra-realistic iPhone mirror selfie of a young woman indoors, with facial identity matching exactly the provided reference image. She is seated casually on a modern sofa in a softly lit, warm-toned room with a wooden-framed mirror behind her.

Framing: mid-body composition (waist-up focus), ensuring her legs are minimally visible or mostly cropped out of the frame. Slight natural perspective as seen in casual selfies.

Pose: She holds her phone in one hand at chest level, angled slightly outward. Her head is turned slightly to the side in a soft, flattering profile with a subtle pout or relaxed expression. The pose should feel candid and natural.

Outfit: She is wearing a fitted half-sleeved top (instead of sleeveless), paired with a soft-colored skirt or shorts, but the lower body is mostly out of frame.

Hair & styling: Hair tied back in a neat ponytail, with a few soft strands framing her face. Natural makeup with smooth skin tones and gentle highlights.

Lighting: Soft indoor ambient lighting with a slightly cinematic glow, subtle shadows, and warm color grading. Slight reflection imperfections on the mirror for realism.

Environment details: Minimal, cozy interior, sofa, mirror, wooden textures, possibly a framed picture in the background. Clean but lived-in aesthetic.

Camera style: iPhone front-camera look, ultra-realistic, shallow depth of field, slight grain, natural skin texture, no over-smoothing.
```

</details>

<a id="nano-banana-streetwear-motion-blur-walk"></a>
### 街头风男模特行走配垂直动态残影

<a href="https://x.com/SadiaMalik182/status/2078088218462007462"><img src="../../previews/nano-banana-streetwear-motion-blur-walk.jpg" width="360"></a>

逐件列出服装并把人物身份锚定在上传的参考图上，能让人物和服饰在编辑后保持一致。动态模糊与故障拖影被单独描述为一层特效，叠加在干净的影棚背景上，形成身后的残影。

Nano Banana 2 · 上传图改图 · 出处: [@SadiaMalik182 on X](https://x.com/SadiaMalik182/status/2078088218462007462) · 73 赞，统计于 2026-10-29

[`fashion`](tags.md#tag-fashion) [`streetwear`](tags.md#tag-streetwear) [`portrait`](tags.md#tag-portrait) [`motion-blur`](tags.md#tag-motion-blur)

<details><summary><b>提示词</b></summary>

```text
A stylish young man in a premium editorial fashion photoshoot, wearing an oversized black/dark charcoal T-shirt, relaxed beige or white wide-leg trousers, premium Nike sneakers, optional black sunglasses, silver chain, and luxury wristwatch. Dynamic walking or standing pose with a confident expression, looking slightly away or toward the camera. Minimal clean white/light gray studio background, dramatic soft lighting, soft shadows, high contrast, artistic vertical motion blur and subtle glitch smear effect around the body, ultra-realistic skin texture, luxury streetwear campaign, Vogue-inspired fashion photography, cinematic color grading, 2K resolution, razor-sharp details, masterpiece quality, preserve the exact reference face and identity 100%, do not change my real face.
```

</details>

<a id="nano-banana-amber-glasses-beanie-side-profile-portrait"></a>
### 琥珀眼镜与针织帽的四分之三侧脸肖像

<a href="https://x.com/weiinberg/status/2071813959901143140"><img src="../../previews/nano-banana-amber-glasses-beanie-side-profile-portrait.jpg" width="360"></a>

参考图只用于锁定面部身份，服装、姿势和背景由提示词重写。四分之三侧脸角度、85mm f/1.8 镜头、单侧窗光加上较长的负面提示，让皮肤质感真实且眼部清晰。

Nano Banana 2 · 上传图改图 · 出处: [@weiinberg on X](https://x.com/weiinberg/status/2071813959901143140) · 72 赞，统计于 2026-10-29

[`portrait`](tags.md#tag-portrait) [`eyewear`](tags.md#tag-eyewear) [`identity-lock`](tags.md#tag-identity-lock) [`window-light`](tags.md#tag-window-light) [`shallow-depth-of-field`](tags.md#tag-shallow-depth-of-field)

<details><summary><b>提示词</b></summary>

```text
Use the uploaded reference image only for preserving the subject's facial identity, facial proportions, skin tone, hairstyle (unless specified otherwise), and overall likeness. Do not copy the original background, pose, clothing, or lighting.

Create a hyper-realistic close-up portrait from a 3/4 side profile (30–45° angle), with the subject looking slightly away from the camera. Frame from the upper chest to the top of the head, filling 80–90% of the frame. Maintain natural facial anatomy and realistic skin texture with visible pores, subtle imperfections, and authentic details.

Style the subject with transparent amber acetate eyeglasses, a rust-colored ribbed knit beanie, a clean white crew-neck t-shirt, and a thin silver chain necklace. Keep the expression neutral, calm, and thoughtful.

Use soft diffused natural window light from one side, creating gentle shadows and smooth highlights across the face. Background should be a clean off-white or light beige studio wall with minimal distractions. Apply a very shallow depth of field with creamy bokeh and crisp focus on the eyes and face.

Editorial fashion photography, minimalist aesthetic, premium lifestyle portrait, luxury eyewear campaign, muted warm color grading, soft contrast, realistic color tones, DSLR quality, 85mm lens, f/1.8, ISO 100, ultra-sharp focus, photorealistic, HDR, 8K, magazine-quality, high-detail facial features, natural skin, cinematic composition.

Negative prompt: low quality, blurry, oversharpened, plastic skin, extra facial features, distorted anatomy, asymmetrical eyes, duplicate glasses, unrealistic beard or hair, oversaturated colors, watermark, logo, text, frame, cartoon, CGI, illustration, low resolution, noise, artifacts.
```

</details>

<a id="gpt-image-realistic-big-head-miniature-pinwheel-portrait"></a>
### 手持风车的写实大头小身人像

<a href="https://x.com/oggii_0/status/2114231078843973707"><img src="../../previews/gpt-image-realistic-big-head-miniature-pinwheel-portrait.jpg" width="360"></a>

用头部占身高比例和肩宽占头宽比例等数值锁定夸张程度，再分段固定姿势、五官、服装和场景，让结果保持真实照片质感。

GPT Image 2.5 · 上传图改图 · 出处: [@oggii_0 on X](https://x.com/oggii_0/status/2114231078843973707) · 70 赞，统计于 2026-10-29

[`big-head`](tags.md#tag-big-head) [`miniature`](tags.md#tag-miniature) [`photo-edit`](tags.md#tag-photo-edit) [`realistic`](tags.md#tag-realistic) [`chibi`](tags.md#tag-chibi)

<details><summary><b>提示词</b></summary>

```text
Turn any image into realistic chibi-style portrait using Chat GPT Image 2.5

Prompt: Task: Strictly edit the uploaded original photograph to transform the person or animal into a hyper-realistic, extremely exaggerated big-head miniature figure, matching the visual style of the provided reference image.

Highest Priority: Transform the head-to-body proportions while preserving the subject's recognizable identity, natural facial features, original expression, hairstyle, clothing, accessories, pose, and overall photographic realism. The final result must resemble a real photograph, not a cartoon or CGI creation.

1. Head-to-Body Proportions (Highest Priority)

- Giant Head: Dramatically enlarge the entire head, including hair, hats, ears, and other existing head accessories. The head should dominate the figure, occupying approximately 65–75% of the total visible silhouette height in a full-body composition.
- Extremely Narrow Shoulders: Reduce shoulder width to approximately 40–50% of the head width. Create a tiny neck and narrow shoulder structure that transitions naturally into the miniature torso.
- Miniature Body: Compress the torso, waist, hips, and limbs into an extremely small body beneath the oversized head. The torso should be short and narrow, with realistic anatomical connections.
- Miniature Arms and Hands: Reduce the arms, palms, and fingers proportionally. Keep the arms naturally close to the body, preserving the original gestures and hand positions.
- Tiny Legs and Feet: Dramatically shorten and narrow the legs, feet, and shoes while preserving the original stance, footwear design, and points of contact with the ground.
- Strong Proportional Contrast: The head must be unmistakably oversized relative to the tiny body. Preserve the subject's original clothing design while naturally adapting its fit to the miniature proportions.

The transformation must create an extreme, visually striking big-head miniature effect without making the subject look like a toy, doll, or digitally assembled figure.

2. Pose and Actions (Strictly Preserve)

Preserve the original subject's exact pose, body orientation, gestures, facial expression, gaze direction, and interactions with the environment.

- If standing, keep the subject standing in the same position.
- If sitting, crouching, leaning, kneeling, or lying down, preserve that exact posture.
- Retain the original hand positions, held objects, arm placement, leg orientation, and contact points.
- Maintain the original head tilt and gaze direction unless a slight anatomical adjustment is necessary for a seamless transformation.
- Keep the subject's original framing. For full-body photographs, preserve the entire figure. For selfies, close-ups, and partial-body images, do not invent missing body parts or expand the frame unnecessarily.

The miniature body must adapt to the original pose rather than forcing the subject into a new pose.

3. Facial Features, Hair, and Clothing (Fully Preserve)

- Identity: Preserve the same recognizable person or animal from the original image. Do not replace, reinterpret, or redesign the subject.
- Face: Retain the original facial structure, eye shape, nose, lips, cheeks, skin tone, expression, and natural facial proportions. Do not apply beauty filters, artificial eye enlargement, face reshaping, or excessive skin smoothing.
- Hair: Preserve the original hairstyle, hair color, hairline, texture, volume, and distinctive strands. Scale the hair naturally with the enlarged head.
- Clothing: Preserve the exact original garments, colors, materials, prints, patterns, logos, folds, and textures. Adapt their dimensions to fit the miniature body without changing their design.
- Accessories: Retain all original jewelry, glasses, hats, bags, watches, and other visible accessories, resizing them only when necessary to fit the transformed proportions.
- Animals: Preserve the original species, recognizable features, fur patterns, ears, eyes, and expression. Apply the same oversized-head and miniature-body transformation without changing the animal's identity.

4. Scene and Composition (Fully Preserve)

Use the uploaded photograph as the sole reference for the subject and environment.

- Preserve the original background, architecture, furniture, plants, ground surface, and environmental objects.
- Maintain the original camera angle, perspective, framing, subject placement, composition, and aspect ratio.
- Keep the surrounding environment at its original scale. The subject's altered proportions should create a striking contrast with the realistic environment.
- Preserve the original lighting direction, color tones, shadows, reflections, and depth of field.
- Ensure the miniature figure remains naturally grounded in the scene, with realistic contact shadows beneath the feet and physically consistent lighting across the enlarged head and reduced body.
- Do not remove, replace, or introduce environmental elements unless a minor reconstruction is essential to repair an editing artifact.

5. Photographic Realism and Visual Quality

The entire image must retain the appearance of an authentic, high-resolution photograph.

- Realistic skin pores, fine facial details, and natural skin texture.
- Individual hair strands with believable highlights and shadows.
- Authentic fabric weave, clothing folds, and accessory details.
- Natural lighting, physically accurate shadows, and consistent reflections.
- Seamless transitions between the enlarged head, neck, and miniature body.
- Realistic anatomy, natural edges, and coherent perspective.
- Subtle photographic imperfections consistent with the original image.

The oversized head must remain fully photorealistic, with the original person's natural facial anatomy and expression intact. The miniature body must look like a physically plausible part of the same person.

6. Strictly Prohibited

- Cartoon, anime, illustration, or stylized 3D figurine aesthetics.
- Plastic skin, toy-like materials, doll faces, or artificial beauty enhancements.
- Changing the subject's identity, facial features, expression, hairstyle, or clothing design.
- Normal adult shoulder width or a body that appears too large relative to the head.
- Oversized hands, fingers, feet, or shoes.
- Disconnected heads, visible neck seams, floating limbs, malformed joints, or duplicated body parts.
- Altered poses, invented gestures, or changed interactions with the environment.
- Unnecessary background replacement, camera-angle changes, or aspect-ratio changes.
- Unnatural shadows, inconsistent lighting, visible compositing artifacts, text, watermarks, or interface elements.

Final Output

Transform the original photograph into an ultra-photorealistic big-head miniature portrait with a dramatically enlarged head, extremely narrow shoulders, a tiny compressed body, and proportionally miniature limbs.

Preserve the original subject's identity, expression, pose, clothing, accessories, background, and photographic characteristics as faithfully as possible. The exaggerated head-to-body ratio should be the defining visual transformation, producing the same realistic, charming, oversized-head aesthetic as the reference image.

Editing Rule: Change the subject's proportions only. Preserve everything else from the original photograph.
```

</details>

<a id="nano-banana-man-beside-anime-self-graffiti-mural"></a>
### 男子站在自己动漫形象的涂鸦墙前

<a href="https://x.com/Minahil42298354/status/2032956520057414135"><img src="../../previews/nano-banana-man-beside-anime-self-graffiti-mural.jpg" width="360"></a>

写实前景人物与同一人物的赛璐璐漫画风壁画同框，形成真人与动漫的对照。提示词点明壁画配色、片假名文字和涂鸦签名，再用脏旧的小巷地面收住前景，让墙面鲜艳而前景保持照片质感。

Nano Banana 2 · 文生图 · 出处: [@Minahil42298354 on X](https://x.com/Minahil42298354/status/2032956520057414135) · 70 赞，统计于 2026-10-29

[`graffiti`](tags.md#tag-graffiti) [`anime-mural`](tags.md#tag-anime-mural) [`mixed-style`](tags.md#tag-mixed-style) [`street-art`](tags.md#tag-street-art) [`portrait`](tags.md#tag-portrait)

<details><summary><b>提示词</b></summary>

```text
A medium shot of a real-life man with short dark hair and a beard, wearing a black hoodie, standing in a pensive pose with his fingers to his temple. He is positioned in front of a massive, vibrant graffiti mural on a concrete wall. The mural depicts an anime-style version of the same man in a dynamic action pose, holding a spray paint can. The art style is bold cel-shaded manga with thick outlines, featuring Japanese katakana text, bright orange and purple splashes, and "
http://
YAPPER.SO" tags. Hyper-realistic foreground, gritty urban alleyway floor with scattered paint cans.
```

</details>

**1** · [2](image-portrait-2.md)
