# Photo realism

[Back to the list](../../README.md) · All 17 entries

<a id="gpt-image-failed-photos-grid"></a>
### Nine failed photos of any character

<a href="https://x.com/DeepBlueX0/status/2099481521983995971"><img src="../../previews/gpt-image-failed-photos-grid.jpg" width="360"></a>

Seven words. The author's point: fewer restrictions give more authentic-looking mistakes.

GPT Image 2.5 · Text-to-image · Source: [@DeepBlueX0 on X](https://x.com/DeepBlueX0/status/2099481521983995971) · 2,646 likes on 2026-10-27

[`grid`](tags.md#tag-grid) [`humor`](tags.md#tag-humor) [`template`](tags.md#tag-template)

<details><summary><b>Prompt</b></summary>

```text
Vertical 3×3 failed photos × {Character}
```

</details>

<a id="nano-banana-sunlit-smartphone-selfie-white-tee"></a>
### Sunlit smartphone selfie of woman in white tee

<a href="https://www.reddit.com/r/GeminiAI/comments/1x08axv/nano_banana_21_goes_crazy"><img src="../../previews/nano-banana-sunlit-smartphone-selfie-white-tee.jpg" width="360"></a>

A structured JSON spec splits face, hair, clothing, lighting and camera into separate fields, so each detail is controlled on its own. Naming a 24 to 28mm phone lens, clipped HDR highlights and a long avoid list keeps the result casual instead of studio polished.

Nano Banana 2.1 · Text-to-image · Source: [u/RIGHT200 on Reddit](https://www.reddit.com/r/GeminiAI/comments/1x08axv/nano_banana_21_goes_crazy) · 1,204 likes on 2026-10-28

[`selfie`](tags.md#tag-selfie) [`smartphone-photo`](tags.md#tag-smartphone-photo) [`json-prompt`](tags.md#tag-json-prompt) [`natural-light`](tags.md#tag-natural-light) [`photorealistic`](tags.md#tag-photorealistic)

<details><summary><b>Prompt</b></summary>

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

<a id="gpt-image-six-photo-portrait-grid"></a>
### Six-photo portrait grid of one person

<a href="https://x.com/john_my07/status/2112737725430554781"><img src="../../previews/gpt-image-six-photo-portrait-grid.jpg" width="360"></a>

Describes the person once in detail, then six shots. Asks for no gutters so the grid reads as one seamless image.

GPT Image 2.5 · Text-to-image · Source: [@john_my07 on X](https://x.com/john_my07/status/2112737725430554781) · 651 likes on 2026-10-27

[`portrait`](tags.md#tag-portrait) [`grid`](tags.md#tag-grid) [`consistency`](tags.md#tag-consistency)

<details><summary><b>Prompt</b></summary>

```text
Create an ultra-realistic 6-photo portrait collage arranged in a seamless 3×2 grid, featuring a naturally beautiful young Portuguese woman in her early 20s. She has warm olive-toned skin, expressive hazel-brown eyes, long chestnut-brown hair with subtle natural highlights, soft face-framing layers, naturally full eyebrows, and delicate, distinctive facial features. Her appearance should feel authentic and individual, with realistic skin texture, tiny imperfections, and minimal everyday makeup.

Visual aesthetic: Effortless European Instagram photo dump, reminiscent of candid photographs taken on a Canon PowerShot G7 X Mark III. Direct built-in camera flash, crisp details, bright facial highlights, hard shadows, slightly imperfect framing, subtle digital noise, and a nostalgic early-2000s point-and-shoot feel.

Setting and styling: A warm off-white bedroom wall with subtle texture, a few natural shadows, and no distracting decorations. She wears a fitted burgundy scoop-neck top, tiny gold hoop earrings, and a delicate necklace. Her makeup is understated, with softly flushed cheeks, natural glossy lips, and lightly defined lashes. Her long hair remains the same color and length but falls differently in every photograph.

Six distinct photographs:

1. Sweet candid: Sitting close to the camera, resting her cheek against one hand, smiling gently with relaxed eyes and loose hair framing her face.
2. Playful snapshot: Looking directly into the lens with a mischievous half-smile, one eyebrow slightly raised, fingers casually tucked behind her ear.
3. Messy-girl moment: Eyes closed and laughing softly, both hands lifting her hair away from her shoulders, a few loose strands catching the flash.
4. Effortless confidence: Turning her face over one shoulder, giving the camera a subtle side-eye, with one hand lightly resting against her neck.
5. Caught laughing: Looking toward someone outside the frame, laughing naturally with her head tilted to the side and hair falling across one cheek.
6. Quiet evening mood: Leaning against the wall, gazing thoughtfully into the lens, lips relaxed, fingertips gently twisting a strand of hair.

Identity consistency: The same Portuguese woman must appear in all six frames, with identical facial proportions, eye color, skin tone, hair color, and recognizable features. Each photograph should have a different pose, expression, head angle, and hair arrangement, as if captured within the same casual photo session.

Photography details: Realistic compact-camera flash, authentic skin pores, fine baby hairs, natural facial asymmetry, believable hands, sharp eyes, slight variations in exposure, and candid framing. Avoid excessive retouching, artificial skin smoothing, exaggerated beauty standards, duplicated expressions, malformed fingers, distorted anatomy, or the overly polished appearance of AI-generated portraits.

Output: Vertical 3:4 aspect ratio, exactly six photographs in a balanced 3-column × 2-row grid, clean alignment, no gutters, no text, no watermark. Photorealistic, youthful, spontaneous, intimate, and effortlessly stylish.
```

</details>

<a id="gpt-image-pencil-essay-coffee-stain"></a>
### Pencil handwritten essay on lined paper with coffee stain

<a href="https://x.com/chetaslua/status/2095556181012128005"><img src="../../previews/gpt-image-pencil-essay-coffee-stain.jpg" width="360"></a>

The prompt fixes the medium (pencil on 8.5x11 lined paper) and the capture method (phone photo). It asks for stroke variance and one small flaw, a coffee stain in a named corner, which gives the realism.

GPT Image 2.5 · Text-to-image · Source: [@chetaslua on X](https://x.com/chetaslua/status/2095556181012128005) · 614 likes on 2026-10-27

[`handwriting`](tags.md#tag-handwriting) [`paper`](tags.md#tag-paper) [`phone-photo`](tags.md#tag-phone-photo) [`texture`](tags.md#tag-texture) [`coffee-stain`](tags.md#tag-coffee-stain)

<details><summary><b>Prompt</b></summary>

```text
🚨 GPT-Image-2.5 Output

I said it to write like einstein it did it without reference < i did not give image or anything   >

left side is AI and right side is real photo from reddit to compare

Prompt : a photorealistic, taken by phone photo of a handwritten essay in pencil, albert einstein handwriting, on an 8.5x11 piece of lined paper, about the history of money in world. make sure there is variance in the writing in a very einstein way. give it a slight coffee stain on the top right corner
```

</details>

<a id="nano-banana-monstera-leaf-hidden-words"></a>
### Monstera leaf gaps forming hidden words

<a href="https://x.com/fofrAI/status/2107509669514113058"><img src="../../previews/nano-banana-monstera-leaf-hidden-words.jpg" width="360"></a>

The prompt names one real object and asks for the text to emerge organically from its natural features, so the lettering follows the leaf's own cut-outs instead of sitting on top. A simple backdrop keeps the gaps readable as letterforms.

Nano Banana 2.1 · Text-to-image · Source: [@fofrAI on X](https://x.com/fofrAI/status/2107509669514113058) · 549 likes on 2026-10-28

[`text-in-image`](tags.md#tag-text-in-image) [`monstera`](tags.md#tag-monstera) [`nature`](tags.md#tag-nature) [`typography`](tags.md#tag-typography) [`photo`](tags.md#tag-photo)

<details><summary><b>Prompt</b></summary>

```text
A photo of a monstera leaf against a simple backdrop, cleverly and organically appearing within the natural gaps of the leaf are the words Nano Banana
```

</details>

<a id="gpt-image-forest-clearing-foliage-noise-test"></a>
### Sunlit woodland clearing with dense green foliage

<a href="https://x.com/mark_k/status/2097411028510179759"><img src="../../previews/gpt-image-forest-clearing-foliage-noise-test.jpg" width="360"></a>

A single plain sentence that names the subject, the photo medium, and a highly detailed cue works as a noise artifact test, because dense repeating foliage exposes texture smearing and grain. The short wording leaves the model free to choose light and composition.

GPT Image 2.5 · Text-to-image · Source: [@mark_k on X](https://x.com/mark_k/status/2097411028510179759) · 415 likes on 2026-10-27

[`forest`](tags.md#tag-forest) [`nature`](tags.md#tag-nature) [`foliage`](tags.md#tag-foliage) [`texture-test`](tags.md#tag-texture-test) [`landscape`](tags.md#tag-landscape)

<details><summary><b>Prompt</b></summary>

```text
GPT-Image-2.5 has arrived in
@ChatGPT
 🔥

It features many improvements, but I couldn't help myself from doing the infamous "noise artifact" test.

The results are mixed!

Prompt: "Photo of a clearing in the woods with lots of green foliage, highly detailed"

See for yourself:
```

</details>

<a id="nano-banana-json-reconstruction"></a>
### JSON prompt that reconstructs a photo shot for shot

<a href="https://x.com/ViralOps_/status/2107538470818484305"><img src="../../previews/nano-banana-json-reconstruction.jpg" width="360"></a>

Structured as JSON fields (framing, light, colour, negatives). The post compares the same JSON on Nano Banana 2.1 and GPT Image 2.5.

Nano Banana 2.1 · Edit · Source: [@ViralOps_ on X](https://x.com/ViralOps_/status/2107538470818484305) · 326 likes on 2026-10-27

[`json`](tags.md#tag-json) [`reconstruction`](tags.md#tag-reconstruction) [`comparison`](tags.md#tag-comparison)

<details><summary><b>Prompt</b></summary>

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

<a id="gpt-image-dusk-film-portrait"></a>
### Low-angle dusk portrait with film grain

<a href="https://x.com/chatgptpaglu/status/2105219509791678731"><img src="../../previews/gpt-image-dusk-film-portrait.jpg" width="360"></a>

Under 600 characters. Camera angle, clothing detail, one light source, one film look.

GPT Image 2.5 · Text-to-image · Source: [@chatgptpaglu on X](https://x.com/chatgptpaglu/status/2105219509791678731) · 318 likes on 2026-10-27

[`portrait`](tags.md#tag-portrait) [`film-grain`](tags.md#tag-film-grain) [`golden-hour`](tags.md#tag-golden-hour)

<details><summary><b>Prompt</b></summary>

```text
A low-angle, close-up photograph capturing a young woman with wavy brown hair outdoors at dusk. She is wearing a grey cropped t-shirt with a blue and white graphic text that reads 'DESTINED' above 'SET 1958' and black denim bottoms. Her head is tilted, and she is looking directly into the camera lens. The dark blue evening sky serves as the background, with silhouetted tree branches visible at the bottom of the frame. Strong flash lighting is directed from the front, illuminating her face and highlighting strands of her hair. The composition has a grainy film photography aesthetic.
```

</details>

<a id="gpt-image-train-platform-snapshot"></a>
### Phone snapshot on a train platform

<a href="https://x.com/MissDelulu9/status/2114965450425868519"><img src="../../previews/gpt-image-train-platform-snapshot.jpg" width="360"></a>

Realism through phone-camera flaws: motion blur on the train, real mobile noise, slight wide-angle distortion.

GPT Image 2.5 · Text-to-image · Source: [@MissDelulu9 on X](https://x.com/MissDelulu9/status/2114965450425868519) · 305 likes on 2026-10-27

[`phone-photo`](tags.md#tag-phone-photo) [`street`](tags.md#tag-street) [`motion-blur`](tags.md#tag-motion-blur)

<details><summary><b>Prompt</b></summary>

```text
Realistic vertical phone street snapshot of a young woman on an urban train platform, slightly right of center, as a silver train with a green stripe rushes behind in horizontal motion blur. Low angle from waist height, close half-body to mid-thigh, handheld and imperfect.

Long deep-black hair sweeps left in station wind. Oversized brown gradient sunglasses hide her eyes; head tilted upward, lips relaxed, cool distant expression. Small oval face, soft jawline, clean East Asian Y2K makeup, nude-pink lips. Warm-white cropped halter tank, low neckline, fitted ribbed cotton, subtle wrinkles, hem above waist. Low-rise loose vintage gray-brown jeans, layered gold necklaces, black quilted chain bag.

Warm-beige skin with natural texture on shoulders, collarbones, arms, waist and abdomen. Cool fluorescent station light, metallic reflections, yellow tactile paving, concrete floor, blurred passengers in train windows. Real mobile noise, slight wide-angle feel.
```

</details>

<a id="gpt-image-wine-bar-ugc-color-reference"></a>
### Woman in brown leather jacket at wine bar

<a href="https://x.com/Mho_23/status/2097483045221917131"><img src="../../previews/gpt-image-wine-bar-ugc-color-reference.jpg" width="360"></a>

A reference photo is first analysed into a detailed JSON of color grading, lighting and exact colors. That JSON plus an attached product image then drives the generation, which avoids the flat AI look and keeps the style consistent.

GPT Image 2.5 · Edit · Source: [@Mho_23 on X](https://x.com/Mho_23/status/2097483045221917131) · 298 likes on 2026-10-27

[`ugc`](tags.md#tag-ugc) [`json-prompt`](tags.md#tag-json-prompt) [`color-grading`](tags.md#tag-color-grading) [`reference-image`](tags.md#tag-reference-image) [`product-photo`](tags.md#tag-product-photo)

<details><summary><b>Prompt</b></summary>

```text
how to generate AI photos that look 100% real with GPT-Image 2.5:

GPT-Image 2.5 looks slightly better than GPT-Image 2, but it still has some of the same characteristics. out of the box, you can still get that noticeable AI look without references, which is why we are going to be using inspiration photos for color grading and creative direction

> find a photo that has the aesthetic you want

> upload that photo into GPT-6 Astra in ChatGPT and ask for this:

“analyze this photo and give me a very detailed json prompt describing its visual style. really make sure to break down the color grading, lighting and all the exact colors in the photo so i can apply that look to my own images”

we’re using GPT-6 Astra here to break down the reference into a detailed prompt instead of trying to describe every little detail ourselves

> take the json prompt Astra gives you and put it into GPT-Image 2.5 on Higgsfield

> upload your product image and prompt: “using this json as reference, generate a person holding my product [attach product image]”

> GPT-Image 2.5 generates the photo with that person holding your product

compare it with a version generated without the reference and look at the difference in the lighting and color grading

> save the generated character photo you’re happy with as your reference

> for future generations, attach the character photo each time and ask it to preserve the same facial features

now you have a reference character you can use across multiple product photos

you can also iterate the base json prompt and chat back and forth with GPT-6 Astra based on what you want, then repeat the same process..

i like this because it gives you much more direction over the color grading instead of leaving everything up to the model

the basic colours and grainy look are some of the things that can make an image feel AI-generated, so pay attention to those when comparing your results

this is how you can start building a library of high quality ugc images around your own products

the json gives GPT-Image 2.5 the lighting and color direction, your character reference helps with consistency, and you control the product placement

once you have that starting point, you can keep creating variations without writing everything from scratch

GPT-Image 2.5 Sunburst & Flare are available on Higgsfield. try this with your own product and reference images there
```
```

</details>

<a id="gpt-image-tree-sun-skyline-frozen-lake"></a>
### Tree silhouette against huge sun over frozen lake

<a href="https://x.com/churvikv/status/2110114825082945740"><img src="../../previews/gpt-image-tree-sun-skyline-frozen-lake.jpg" width="360"></a>

The prompt is split into labeled blocks for sky, sun, tree, city, water, reflection and palette, so each element gets its own placement rules. A long negative list and explicit rules such as buildings never overlapping the tree or sun keep the symmetrical composition intact.

GPT Image 2.5 · Text-to-image · Source: [@churvikv on X](https://x.com/churvikv/status/2110114825082945740) · 150 likes on 2026-10-28

[`silhouette`](tags.md#tag-silhouette) [`sunset`](tags.md#tag-sunset) [`skyline`](tags.md#tag-skyline) [`reflection`](tags.md#tag-reflection) [`panoramic`](tags.md#tag-panoramic)

<details><summary><b>Prompt</b></summary>

```text
Photorealistic silhouette sunset composite, wide 16:9 panoramic composition, cinematic, ultra-detailed. Edge to edge, no frame, no border.

SKY: the upper half is a furnace of amber, apricot and burnt gold, deepest at the horizon, cooling to smoky blue-grey at the very top. Long streaky cirrus clouds sweep diagonally across it, undersides lit gold, edges trailing thin warm wisps.

SUN: one huge perfectly round pale white-hot sun disc sits exactly at the centre of the frame just above the treeline, its rim glowing and bleeding a soft warm halo into the surrounding orange.

TREE: dead centre, in front of the sun, a single massive spreading broadleaf tree in pure black silhouette — a thick trunk flaring at the base into a rounded knoll, and a vast dense canopy of fine branch tracery and leaf clusters spreading wide and symmetrical, its edges softly dissolving into the glow.

CITY: flanking the tree, a dense skyline of black skyscraper silhouettes stands along a low ridge of rooftops. Left, a tall stepped tower with twin thin antennae, ringed by shorter blocks. Right, three dark high-rises of graduated height, one carrying a slender spire. The buildings never overlap the tree and never cross the sun.

WATER: the entire lower third is a frozen lake surface, not smooth water — a turbulent marbled expanse of glacial ice and flowed stone, banded in chalky white, sea-green, slate grey and warm tan in long swirling veins.

REFLECTION: sky, sun, tree and skyline all mirror downward into that marbled surface, broken and stretched by the ice grain. The reflected sun lies as a broad soft gold field beneath the trunk, the reflected tree spreads as a dark root-mass of branching veins below it, and the reflected towers hang as vertical dark bars, all smeared by the swirling white and green stone.

PALETTE: pure black, apricot, amber gold, burnt orange, smoky grey, chalk white, glacier green, tan. Sharp silhouette edges against soft glow, high dynamic range, clean and unmarked.

text, watermark, logo, signature, artist signature, handwritten signature, initials, monogram, date, stamp, seal, lettering of any kind, any words, digits, frame, border, picture frame, mat, bevel, molding, plaque, rectangular outline, painting, illustration, oil painting, impasto, watercolor, colored pencil, airbrush, digital art, cartoon, anime, chibi, flat 2d vector, blurry, soft focus, noisy grain, neon, fluorescent, oversaturated greens, blue midday sky, sunrise pink, purple sky, night, moon, stars, clouds covering the sun, rain, storm, lightning, snow falling, second tree, forest, multiple trees, leaves visible on tree with colour, lit windows on buildings, people, faces, birds, animals, deer, boat, ship, dock, bridge, road, cars, traffic, streetlamps, palm trees, mountains, desert, ocean waves, beach, sun cut off, tree cut off, off-centre tree, asymmetric composition
```

</details>

<a id="gpt-image-robot-chef-futuristic-kitchen-tray"></a>
### Silver robot chef holding a tray in neon kitchen

<a href="https://x.com/Adnan_Ai2/status/2102217167458754843"><img src="../../previews/gpt-image-robot-chef-futuristic-kitchen-tray.jpg" width="360"></a>

The prompt lists the robot's parts in order (silver body, mechanical joints, cyan eyes, ear components), then the pose and gaze, then the kitchen. Cyan neon is paired with warm cinematic light, and steam, reflections and depth of field add realism. The 9:16 ratio is stated at the end.

GPT Image 2.5 · Text-to-image · Source: [@Adnan_Ai2 on X](https://x.com/Adnan_Ai2/status/2102217167458754843) · 58 likes on 2026-10-28

[`robot`](tags.md#tag-robot) [`futuristic`](tags.md#tag-futuristic) [`kitchen`](tags.md#tag-kitchen) [`cinematic`](tags.md#tag-cinematic) [`photorealistic`](tags.md#tag-photorealistic)

<details><summary><b>Prompt</b></summary>

```text
A highly realistic humanoid futuristic robot chef standing inside a premium futuristic restaurant kitchen. The robot has a sleek silver metallic body with detailed mechanical joints and realistic humanoid proportions. It has glowing cyan-blue eyes, circular futuristic ear components, a metallic face and neck, and an advanced sophisticated robotic design. The robot is holding a large white serving tray with both hands and looking slightly toward the left with a calm and helpful expression. The background features a stainless-steel futuristic kitchen with modern cooking equipment, metallic countertops, ovens, and ventilation systems. Cyan neon accent lights illuminate the kitchen, combined with warm cinematic lighting. Realistic metallic reflections, subtle steam rising in the background, highly detailed mechanical textures, photorealistic 3D rendering, cinematic composition, ultra-realistic, 4K quality, sharp details, natural depth of field, vertical 9:16 composition.
```

</details>

<a id="gpt-image-driver-seat-smartphone-selfie"></a>
### Smartphone selfie of a woman in a car

<a href="https://x.com/ZarnishNael/status/2104090733305319799"><img src="../../previews/gpt-image-driver-seat-smartphone-selfie.jpg" width="360"></a>

Fixes a vertical 9:16 selfie framing, then lists specific hair, skin and clothing details alongside the car interior and soft daylight. Casual phone softness and a long list of anti-filter negatives (no plastic skin, no CGI look) keep the result candid and photographic.

GPT Image 2.5 · Text-to-image · Source: [@ZarnishNael on X](https://x.com/ZarnishNael/status/2104090733305319799) · 55 likes on 2026-10-28

[`selfie`](tags.md#tag-selfie) [`smartphone-photo`](tags.md#tag-smartphone-photo) [`car-interior`](tags.md#tag-car-interior) [`natural-light`](tags.md#tag-natural-light) [`candid`](tags.md#tag-candid)

<details><summary><b>Prompt</b></summary>

```text
Create a highly realistic vertical 9:16 smartphone selfie of a young woman sitting inside a modern car in the driver’s seat. She has long, straight, naturally voluminous dark-brown hair falling over both shoulders, soft natural facial features, warm fair skin with realistic texture, expressive brown eyes, natural eyebrows, subtle rosy cheeks, and a gentle smiling expression. She is wearing a simple fitted black long-sleeve top with black trousers. One hand is holding the steering wheel while she looks naturally toward the camera.
Capture the scene like an authentic casual smartphone photo, with soft natural daylight entering through the car windows, realistic car interior, dashboard and steering wheel visible, urban buildings and parked cars softly visible outside. Natural proportions, realistic skin pores and hair strands, subtle shadows, slight smartphone-camera softness, authentic colors, candid lifestyle photography, photorealistic, high detail, no artificial beauty filter, no plastic skin, no face distortion, no CGI look, no wa
```

</details>

<a id="nano-banana-1960s-car-mirror-fashion-reflection"></a>
### 1960s Fashion Portrait Reflected in Car Mirror

<a href="https://x.com/mehvishs25/status/2107858748882690121"><img src="../../previews/nano-banana-1960s-car-mirror-fashion-reflection.jpg" width="360"></a>

The whole scene is framed as a reflection in a curved chrome side mirror, with the camera position and walking pose spelled out so the reflection stays physically believable. A fixed four colour palette and 35mm film grain and scratch cues give an authentic aged editorial look, and the reference identity is locked with an explicit do not alter her face line.

Nano Banana 2.1 · Edit · Source: [@mehvishs25 on X](https://x.com/mehvishs25/status/2107858748882690121) · 23 likes on 2026-10-28

[`vintage`](tags.md#tag-vintage) [`fashion`](tags.md#tag-fashion) [`mirror-reflection`](tags.md#tag-mirror-reflection) [`film-grain`](tags.md#tag-film-grain) [`identity-preservation`](tags.md#tag-identity-preservation)

<details><summary><b>Prompt</b></summary>

```text
Create a hyper-realistic 1960s vintage editorial fashion photograph in a vertical 9:16 composition, featuring the girl from the reference image. Preserve her identity and appearance exactly as shown in the reference — including her facial structure, proportions, distinctive features, skin tone, hairstyle characteristics, and overall natural appearance. Do not alter or reinterpret her face.

The scene is captured as a full-body fashion portrait reflected inside a small, oval chrome side mirror of a vintage car. The mirror has naturally curved, slightly distorted edges and realistic reflections. The camera is positioned close to the driver's window, angled toward the side mirror.

Inside the mirror reflection, the girl is fully visible with generous background space. She is walking toward the rear of the car while slightly turning her head toward the mirror, creating a subtle candid moment. She has a calm, confident expression with a soft, understated smile.

She wears a beautifully tailored powder-blue midi dress with a slim waist belt, paired with a burgundy silk scarf, elegant cat-eye sunglasses, a small ivory handbag, and classic white pointed heels. Her styling has an authentic polished 1960s fashion aesthetic.

The environment is a retro Mediterranean-American street with a palm-lined road, pastel-colored storefronts, a vintage station wagon, and distant mountains. Bright golden morning sunlight creates warm, natural highlights and soft shadows across the scene.

Use a refined color palette of powder blue, ivory, burgundy, and warm beige. The image should look like an authentic aged 35mm film photograph, with natural analog grain, subtle film imperfections, tiny scratches, realistic exposure, authentic skin texture, and physically accurate mirror reflections.

The overall mood should feel chic, nostalgic, elegant, and slightly mysterious — like a genuine fashion editorial photograph captured in the 1960s rather than an AI-generated image. Photorealistic, cinematic, highly detailed, natural proportions, realistic fabric texture, authentic vintage photography aesthetics.
```

</details>

<a id="gpt-image-1969-festival-crowd"></a>
### Festival crowd in Bethel, New York, August 1969

<a href="https://developers.openai.com/api/docs/guides/image-prompting#use-historical-and-real-world-context"><img src="../../previews/gpt-image-1969-festival-crowd.jpg" width="360"></a>

A place and a date are enough for the model to infer clothing, staging and setting. Inspect the result for period accuracy. Preview: the Sunburst variant.

GPT Image 2.5 · Text-to-image · Source: [OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting#use-historical-and-real-world-context)

[`historical`](tags.md#tag-historical) [`crowd`](tags.md#tag-crowd) [`photorealism`](tags.md#tag-photorealism)

<details><summary><b>Prompt</b></summary>

```text
Create a realistic outdoor crowd scene in Bethel, New York on August 16, 1969.
Photorealistic, period-accurate clothing, staging, and environment.
```

</details>

<a id="gpt-image-candid-sailor-35mm"></a>
### Candid 35mm portrait of an old sailor mending a net

<a href="https://developers.openai.com/api/docs/guides/image-prompting#control-style-and-lighting"><img src="../../previews/gpt-image-candid-sailor-35mm.jpg" width="360"></a>

Skin texture, lens, light and grain are each named, and the last line rules out glamour and retouching, so the result reads as an unposed photo. Preview: the Sunburst variant.

GPT Image 2.5 · Text-to-image · Source: [OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting#control-style-and-lighting)

[`photorealism`](tags.md#tag-photorealism) [`film`](tags.md#tag-film) [`portrait`](tags.md#tag-portrait)

<details><summary><b>Prompt</b></summary>

```text
Create a photorealistic candid photograph of an elderly sailor standing on a small fishing boat.
He has weathered skin with visible wrinkles, pores, and sun texture, and a few faded traditional sailor tattoos on his arms.
He is calmly adjusting a net while his dog sits nearby on the deck. Shot like a 35mm film photograph, medium close-up at eye level, using a 50mm lens.
Soft coastal daylight, shallow depth of field, subtle film grain, natural color balance.
The image should feel honest and unposed, with real skin texture, worn materials, and everyday detail. No glamorization, no heavy retouching.
```

</details>

<a id="gpt-image-sketch-to-photo-valley"></a>
### Line drawing of a river valley rendered as a photo

<a href="https://developers.openai.com/api/docs/guides/image-prompting#turn-a-drawing-into-a-realistic-image"><img src="../../previews/gpt-image-sketch-to-photo-valley.jpg" width="360"></a>

Locks layout, proportions and perspective, lets the model choose materials and light, and bans new elements so it does not reinterpret the sketch. Preview: the Sunburst variant.

GPT Image 2.5 · Edit · Source: [OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting#turn-a-drawing-into-a-realistic-image)

[`sketch`](tags.md#tag-sketch) [`photorealism`](tags.md#tag-photorealism) [`landscape`](tags.md#tag-landscape)

<details><summary><b>Prompt</b></summary>

```text
Turn this drawing into a photorealistic image.
Preserve the exact layout, proportions, and perspective.
Choose realistic materials and lighting consistent with the sketch intent.
Do not add new elements or text.
```

</details>

Inputs: [1](https://developers.openai.com/images/platform/guides/image-prompting/drawings.webp)
