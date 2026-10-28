<div align="center">

<h1>Awesome Image & Video Prompts</h1>

<p>Copy-ready prompts for the leading AI video models, each with its real output and a link to where it came from. Plus agent recipes for editing video.</p>

<p><b>English</b> · <a href="README_zh.md">简体中文</a></p>

<p><a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a></p>

<a href="#h3-starship-hyperspace-jump"><img src="previews/h3-starship-hyperspace-jump.gif" height="150"></a> <a href="#omni-four-style-progression"><img src="previews/omni-four-style-progression.gif" height="150"></a> <a href="#kling-moonlit-garden-run"><img src="previews/kling-moonlit-garden-run.gif" height="150"></a> <a href="#veo-off-road-rally"><img src="previews/veo-off-road-rally.gif" height="150"></a> 

</div>

> Formerly **Awesome-GPTs**. The original GPTs list lives on in [legacy/awesome-gpts.md](legacy/awesome-gpts.md).

## Contents

- [Video prompts](#video) (39 entries)
  - [MiniMax H3](#minimaxh3) (3)
  - [Gemini Omni Flash](#geminiomniflash) (13)
  - [Kling 3.0](#kling30) (15)
  - [Veo 3](#veo3) (5)
  - [Sora 2](#sora2) (3)
- [Agent recipes: editing video](#recipes) (5 entries)
- [Image prompts](#image)
- [3D with agents](#threed)
- [Browse by tag](#tags)
- [Contributing](#contributing)

<a id="video"></a>
## Video prompts

Every prompt below is copied verbatim from the model maker's own guide or model card, next to the video it produced. Click a thumbnail to watch the original with sound. Sections follow the [Artificial Analysis video arena](https://artificialanalysis.ai/video/leaderboard/text-to-video) ranking.

<a id="minimaxh3"></a>
## MiniMax H3

<a id="h3-pink-suit-lip-sync-edit"></a>
### Make the man in an existing clip speak, in a borrowed voice

<a href="https://huggingface.co/MiniMaxAI/MiniMax-H3/resolve/main/assets/r2va_2k.mp4"><img src="previews/h3-pink-suit-lip-sync-edit.jpg" width="360"></a>

Edit-mode prompt with six fields. `retention_analysis` says what to keep from each input: the source video fully, its music partly, and only the voice timbre from the second audio clip.

MiniMax H3 · Video edit · Source: [MiniMax H3 model card](https://huggingface.co/MiniMaxAI/MiniMax-H3)

[`lip-sync`](#tag-lip-sync) [`voice-reference`](#tag-voice-reference) [`multi-reference`](#tag-multi-reference) [`structured-prompt`](#tag-structured-prompt) [`dialogue`](#tag-dialogue)

<details><summary><b>Prompt</b></summary>

```text
subject_definitions:
<Subject 1> is the young man with short wavy blonde hair, wearing a bright pink suit jacket, matching pink trousers, an unbuttoned white shirt, and silver rings, holding a small black lamb in his arms in <Video 1>.
<Video 1> is the source video for the editing task.
<Audio 1> is the synchronized audio track of <Video 1>, providing the background music.
<Audio 2> is the voice timbre reference for <Subject 1>'s voice, containing a spoken male voiceover.

summary:
[video editing + audio reference + audio reuse] The target video is an edited version of <Video 1>. <Subject 1>, wearing a bright pink suit and holding a black lamb, stands in a grassy field with other white lambs in the background. The edit animates <Subject 1>'s face to speak the user-provided dialogue. <Audio 1> is partially reused as the continuous background music, while the target references the calm male voice timbre of <Audio 2> for <Subject 1>'s spoken lines.

retention_analysis:
<Subject 1> (appears in [Shot 1]): fully_preserved - the man retains his identity, wavy blonde hair, pink suit, white shirt, accessories, and the black lamb he holds, with his mouth newly animated to speak.
<Video 1> (source video editing): fully_preserved - the original camera framing, warm golden hour lighting, grassy hill setting, and background white lambs are maintained while the central character is edited.
<Audio 1>: partially_copy - the atmospheric background music from <Audio 1> is reused in the target video, mixed beneath the newly added spoken dialogue.
<Audio 2>: reference - the target audio references the male voice timbre from <Audio 2> to generate <Subject 1>'s spoken dialogue.

detailed_description:
The target video is in realistic photographic style.
[Shot 1] The shot begins from the source <Video 1>, showing <Subject 1>, a young man with short wavy blonde hair, wearing a bright pink suit jacket, matching pink trousers, and a casually unbuttoned white shirt. He stands confidently in a sunlit green pasture, gently holding a small black lamb securely in his arms. The warm, golden hour lighting casts soft shadows across his face and the bright pink fabric of his suit. Behind him, several white lambs stand and graze on the rolling grassy hill against a clear, pale blue sky. The atmospheric background music from <Audio 1> plays continuously throughout the scene. <Subject 1> physically speaks, his mouth movements naturally syncing to the new dialogue, with his voice timbre referencing the calm male delivery from <Audio 2>. Looking thoughtfully forward, <Subject 1> (S1) speaks softly, <d>[English] Follow the wind, live free.</d> As he delivers the line, he subtly shifts his weight, cradling the resting black lamb while the camera slowly pushes in. <Subject 1> (S1) continues his thought, <d>[English] Leave worries behind, enjoy the moment.</d> Exactly as his voice stops, his lips meet in a relaxed, peaceful smile, and his jaw ceases speaking motion. He then turns his gaze slightly away toward the horizon, gently stroking the black lamb's fleece with his fingers as the camera holds on this tranquil, sunlit state through the end of the video.

overall_soundscape:
The soundscape consists of the continuous, atmospheric background music from <Audio 1>, overlaid with the clear, calm male dialogue spoken by the main character, referencing the voice timbre of <Audio 2>.

non_diegetic_music:
The atmospheric, sustained background music from <Audio 1> is reused as the continuous score, playing quietly beneath the spoken dialogue.
```

</details>

<a id="h3-ramen-focus-pull"></a>
### Ramen in front, family dinner behind, one focus pull

<a href="https://huggingface.co/MiniMaxAI/MiniMax-H3/resolve/main/assets/i2va_2k.mp4"><img src="previews/h3-ramen-focus-pull.jpg" width="360"></a>

The first line pins the input photo to frame 0, then the prompt describes the whole eight seconds as one locked-off shot whose only move is the focus shifting from the bowl to the family.

MiniMax H3 · Image-to-video · Source: [MiniMax H3 model card](https://huggingface.co/MiniMaxAI/MiniMax-H3)

[`focus-pull`](#tag-focus-pull) [`static-camera`](#tag-static-camera) [`structured-prompt`](#tag-structured-prompt) [`food`](#tag-food) [`sfx`](#tag-sfx)

<details><summary><b>Prompt</b></summary>

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] This is a live-action, cinematic shot with a shallow depth of field. The camera holds a perfectly static shot throughout the entire eight-second duration, capturing a cozy family gathering in a traditional Japanese dining room. The scene opens with a large, intricately patterned blue and white ceramic bowl of ramen in the immediate foreground, rendered in crisp, sharp focus. The bowl sits on a smooth, polished long wooden table. Inside the bowl, a rich, oily golden-brown broth surrounds yellow wavy noodles, topped with two thick, round slices of chashu pork featuring visible fat marbling and a distinct spiral meat pattern. A generous mound of freshly chopped, bright green scallions rests in the center, and a crisp, dark green rectangular sheet of nori seaweed is tucked into the right edge. To the left of the bowl, a pair of light brown wooden chopsticks rests horizontally on a small, dark rectangular chopstick rest, near a small cylindrical ceramic teacup with blue painted patterns. On the right side of the table, a spherical paper lantern with a ribbed bamboo frame sits on a black wooden base. In the background, a large family of seven is gathered around the table, initially appearing as a soft, blurred presence. Behind them, traditional Japanese sliding shoji screens with wooden lattice frames are open, revealing a bright outdoor scene with lush green trees. Early in the clip, the thick, white steam rising from the hot ramen broth immediately intensifies, billowing upwards in thick, swirling clouds that dance continuously above the bowl. As the clip progresses into the middle seconds, the camera maintains its static position while the focus begins a deliberate, smooth shift deeper into the room. The foreground ramen bowl, its vibrant ingredients, and the rising steam gradually soften into a hazy, out-of-focus blur. Simultaneously, the family members in the background come into sharp, detailed clarity. The heavy steam continues to rise from the foreground, creating a dynamic, translucent veil between the camera and the family. With the focus now firmly locked on the background, the vibrant family dinner comes alive. The man in the dark navy blue long-sleeved shirt on the left leans forward, his mouth moving animatedly in a silent exchange. The young girl in the crisp white short-sleeved t-shirt beside him smiles brightly, looking toward the center of the table. The woman on the far left, wearing a soft light blue long-sleeved blouse, turns her head slightly, smiling gently. Across the table, the woman in the light grey button-down shirt smiles broadly, her eyes crinkling, as she rests her hands near her plate. The woman in the dark grey top further back uses her wooden chopsticks to pick up a small piece of food from a central ceramic dish filled with bright red pickled vegetables. The woman in the center back in the light grey sweater smiles gently, her hands clasped softly in front of her, observing the interaction. Throughout the remainder of the clip, the family continues their lively physical interaction, their mouths moving in continuous, silent cadences of conversation, while the thick, white steam from the blurred ramen bowl in the foreground never stops rising, adding a comforting atmosphere to the warm gathering.

overall_soundscape: The soundscape begins with a quiet room tone mixed with the faint, airy rustle of the thick steam billowing from the hot ramen bowl in the foreground, accompanied by the subtle, continuous hissing and bubbling of the rich broth. As the visual focus shifts deeper into the room, the physical sounds of the bustling family dinner become dominant in the foreground. The clear, sharp clinking of ceramic bowls and wooden chopsticks touching plates is clearly heard as the family members reach for food. This is followed by the faint, muffled thud of a cup being set down on the smooth wooden table, and the subtle, rhythmic rustle of cotton and wool clothing as the family members lean forward and gesture, perfectly capturing the lively, physical atmosphere of the shared meal.

non_diegetic_music: A gentle, heartwarming acoustic guitar melody plays softly in the background, accompanied by the subtle, resonant notes of a traditional Japanese koto. The music maintains a slow, comforting tempo that enhances the cozy, nostalgic, and joyful atmosphere of the family gathering.
```

</details>

<a id="h3-starship-hyperspace-jump"></a>
### Starship bridge, the fleet jumps to hyperspace

<a href="https://huggingface.co/MiniMaxAI/MiniMax-H3/resolve/main/assets/t2va_2k.mp4"><img src="previews/h3-starship-hyperspace-jump.jpg" width="360"></a>

The full H3-Context-IR format: numbered shots with a timed cut at 00:04.500, then separate fields for sound and score. Most local H3 runs skip this rewriting step, which is why they look flat.

MiniMax H3 · Text-to-video · Source: [MiniMax H3 model card](https://huggingface.co/MiniMaxAI/MiniMax-H3)

[`multi-shot`](#tag-multi-shot) [`timed-cut`](#tag-timed-cut) [`structured-prompt`](#tag-structured-prompt) [`sfx`](#tag-sfx) [`score`](#tag-score) [`sci-fi`](#tag-sci-fi)

<details><summary><b>Prompt</b></summary>

```text
integrated_multimodal_description: [Shot 1] Cinematic, medium wide shot, pushing in slowly. In the cavernous, dimly lit bridge of a starship, sleek metallic consoles with glowing amber displays flank a massive, curved observation window. A female captain, in her late 40s with an athletic build and short silver-streaked black hair, stands in the center midground. She wears a structured, high-collared dark navy military tunic with silver chest insignias. Her back is to the camera, silhouetted against the cool, ambient starlight pouring through the thick glass. She stands perfectly still with her hands clasped tightly behind her back. Outside the window, a massive armada of jagged, dark grey dreadnoughts hovers in tight formation against a deep purple space nebula. The fleet's massive rear thrusters begin to glow with an intense, escalating bright blue light. [Shot 2] At 00:04.500, the camera cuts to a close-up of the captain's face and shakes strongly. The brilliant blue-white light from the fleet's gathering energy reflects vividly in her dark eyes. Suddenly, a blinding white flash floods through the window, completely washing out the background as the fleet jumps to hyperspace. The sheer spatial force violently jolts the bridge, causing the captain from Shot 1 to stagger slightly forward, her shoulders tensing as she visibly braces herself against the physical tremors. As the intense white light fades abruptly, leaving only the dim, empty expanse of the purple nebula reflected on her starkly lit skin, her jaw clenches, and she slowly closes her eyes in the newly emptied space.
overall_soundscape: A low, resonant hum of the ship's ambient life support systems serves as the baseline, soon drowned out by an audible, escalating, high-pitched electronic whine as the fleet outside charges its hyperdrives. A massive, deafening, bass-heavy boom and sharp crackle erupts during the blinding flash, accompanied by the loud metallic creaking, rattling, and deep thuds of the bridge's bulkheads vibrating under immense physical stress. The intense roaring impact then cuts abruptly back to a hollow, echoing room tone, leaving only the faint, steady hum of the isolated bridge.
non_diegetic_music: Cinematic space-opera orchestral score, slow tempo, featuring a solitary, mournful French horn melody over deep, sustained string dissonances that build rapidly in volume and intensity, swelling to a massive orchestral peak before snapping immediately into silence right after the jump.
```

</details>

<a id="geminiomniflash"></a>
## Gemini Omni Flash

<a id="omni-astronaut-three-swaps"></a>
### Ships to origami, astronaut to anemone, ships to stingrays

<a href="https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/FfbFqJ8qhY_ZWZyz/gemini-omni__prompt-guide_astro-stingray.webm"><img src="previews/omni-astronaut-three-swaps.jpg" width="360"></a>

Three edits in a row on one shot. The scene and camera stay consistent across every turn.

Gemini Omni Flash · Video edit · Source: [Gemini Omni prompt guide](https://deepmind.google/models/gemini-omni/prompt-guide/)

[`multi-turn-edit`](#tag-multi-turn-edit) [`object-swap`](#tag-object-swap) [`consistency`](#tag-consistency)

<details><summary><b>Prompt</b></summary>

```text
Change the ships to be made from white origami paper.
Change the astronaut to a sea anemone.
Change the small ships to stingrays.
```

</details>

Inputs: [1](https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/FfbFqJ8qhY_ZWZyz/gemini-omni__prompt-guide_astro-spaceship.webm)

<a id="omni-birds-form-a-bird"></a>
### A flock of birds forms the shape of a bird, to music

<a href="https://storage.googleapis.com/deepmind-media/DeepMind.com/Models/gemini-omni/prompt-guide/gemini-omni__prompt-guide__birds-shape.webm"><img src="previews/omni-birds-form-a-bird.jpg" width="360"></a>

Three inputs, each with its own tag: `<video>` for motion, `<image>` for shape, `<audio>` for timing.

Gemini Omni Flash · Reference-to-video · Source: [Gemini Omni prompt guide](https://deepmind.google/models/gemini-omni/prompt-guide/)

[`multi-reference`](#tag-multi-reference) [`audio-sync`](#tag-audio-sync)

<details><summary><b>Prompt</b></summary>

```text
The birds from <video> loosely form the imperfect shape of a bird based on <image>. They move to the music from <audio> and dissipate as they fly
```

</details>

Inputs: [1](https://storage.googleapis.com/deepmind-media/DeepMind.com/Models/gemini-omni/prompt-guide/gemini-omni__reference-anything-inputs__bird-shape.webm) · [2](https://storage.googleapis.com/deepmind-media/DeepMind.com/Models/gemini-omni/prompt-guide/gemini-omni__reference-anything-combine-multi-ingredient-01.webp)

<a id="omni-butterfly-bee-fireflies"></a>
### Butterfly to bee to fireflies, one change per turn

<a href="https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/FfbFqJ8qhY_ZWZyz/gemini-omni__prompt-guide__firefly.webm"><img src="previews/omni-butterfly-bee-fireflies.jpg" width="360"></a>

Two short edit turns on the same clip. Each turn names one subject and its replacement, and everything else stays put.

Gemini Omni Flash · Video edit · Source: [Gemini Omni prompt guide](https://deepmind.google/models/gemini-omni/prompt-guide/)

[`multi-turn-edit`](#tag-multi-turn-edit) [`object-swap`](#tag-object-swap)

<details><summary><b>Prompt</b></summary>

```text
Change the butterfly to a bee.
Change the bee into a small swarm of fireflies.
```

</details>

Inputs: [1](https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/FfbFqJ8qhY_ZWZyz/gemini-omni__prompt-guide__butterfly.webm)

<a id="omni-drummer-whip-pan"></a>
### Whip-pan from drummer to saxophonist and dancer

<a href="https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/YMgFKThN-vej75eW/gemini-omni__first-last-frame__dummer-ballet.webm"><img src="previews/omni-drummer-whip-pan.jpg" width="360"></a>

First and last frames fix both ends. The prompt describes the move between them and closes with `One continuous shot, no jump cuts`.

Gemini Omni Flash · First & last frame · Source: [Gemini Omni prompt guide](https://deepmind.google/models/gemini-omni/prompt-guide/)

[`first-last-frame`](#tag-first-last-frame) [`camera-move`](#tag-camera-move) [`long-take`](#tag-long-take) [`music`](#tag-music)

<details><summary><b>Prompt</b></summary>

```text
A close-up low-angle shot of a stylish drummer in a beige suit playing a red drum kit in a grand hall transitions as the camera whip-pans to the side, revealing an older saxophonist playing alongside a ballet dancer spinning in a white outfit under soft purple stage lights. One continuous shot, no jump cuts.
```

</details>

<a id="omni-four-style-progression"></a>
### One clip through crayon, pencil, glass and risograph

<a href="https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/FfbFqJ8qhY_ZWZyz/gemini_omni__prompt-guide__astro-sketch-valley.webm"><img src="previews/omni-four-style-progression.jpg" width="360"></a>

Restyles a reference video in four stages. Each stage gets its own texture words, so the transitions read clearly.

Gemini Omni Flash · Video edit · Source: [Gemini Omni prompt guide](https://deepmind.google/models/gemini-omni/prompt-guide/)

[`style-transfer`](#tag-style-transfer) [`animation`](#tag-animation)

<details><summary><b>Prompt</b></summary>

```text
Create a four-part stylistic progression of the video reference that begins with a vibrant colored crayon aesthetic, featuring rich, waxy, textured strokes and playful, hand-drawn character designs against a backdrop of heavily granulated paper. Transition seamlessly into a graphite pencil sketch on textured paper, utilizing cross-hatching, varying line weights, and a 12fps "line boiling" effect to emphasize a hand-drawn feel. Next, morph into a hyper-realistic 3D translucent glass style, characterized by complex light refractions, caustic patterns, and soft internal glows within a minimalist studio setting. Conclude the sequence with a tactile risograph print look, applying a limited three-color palette, grainy halftone textures, and intentional registration overlays for a retro, mechanical finish.
```

</details>

Inputs: [1](https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/FfbFqJ8qhY_ZWZyz/gemini_omni__prompt-guide__astro-sketch-valley_input.webm)

<a id="omni-harbour-extend"></a>
### Harbour conversation extended twice

<a href="https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/YMgFKThN-vej75eW/gemini-omni__extend__boats_1080.webm"><img src="previews/omni-harbour-extend.jpg" width="360"></a>

Each extension only says what happens next: one line of dialogue, then a camera pull-back and a music cue.

Gemini Omni Flash · Extend · Source: [Gemini Omni prompt guide](https://deepmind.google/models/gemini-omni/prompt-guide/)

[`extend`](#tag-extend) [`dialogue`](#tag-dialogue) [`long-take`](#tag-long-take)

<details><summary><b>Prompt</b></summary>

```text
The man in the blue sweater replies: "Did your father go out on the boat too?"
The camera pulls back in one continuous movement as he continues his story: "He used to say that this harbour had a soul. And that the boats were a part of us." The music swells.
```

</details>

<a id="omni-lights-sync-to-music"></a>
### Apartment lights switch on to the beat

<a href="https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/FfbFqJ8qhY_ZWZyz/gemini-omni__prompt-guide__building-light.webm"><img src="previews/omni-lights-sync-to-music.jpg" width="360"></a>

Syncs a visual event to an audio track by naming both in one sentence. No timestamps needed.

Gemini Omni Flash · Video edit · Source: [Gemini Omni prompt guide](https://deepmind.google/models/gemini-omni/prompt-guide/)

[`audio-sync`](#tag-audio-sync) [`music`](#tag-music)

<details><summary><b>Prompt</b></summary>

```text
The lights of the apartments start turning on in sync with the music.
```

</details>

Inputs: [1](https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/FfbFqJ8qhY_ZWZyz/gemini-omni__prompt-guide__building-no-light.webm)

<a id="omni-quantum-explainer"></a>
### Quantum computing explained in risograph flat style

<a href="https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/FfbFqJ8qhY_ZWZyz/gemini-omni__prompt-guide__quantum.webm"><img src="previews/omni-quantum-explainer.jpg" width="360"></a>

Asks for an explanation and leaves the content to the model's world knowledge. The prompt only pins down the visual style.

Gemini Omni Flash · Text-to-video · Source: [Gemini Omni prompt guide](https://deepmind.google/models/gemini-omni/prompt-guide/)

[`explainer`](#tag-explainer) [`motion-graphics`](#tag-motion-graphics) [`style-lock`](#tag-style-lock)

<details><summary><b>Prompt</b></summary>

```text
Explain the difference between regular computing and quantum computing. Visualize this sentence using a contemporary flat-media style that blends minimalist vector shapes with rich organic textures. The aesthetic is defined by a high-contrast, "electric" color palette of neon pinks, cyans, and limes set against a deep navy background. A hallmark of this style is the use of stipple shading and grainy gradients, which adds a tactile, risograph-like quality to the otherwise simple geometric forms. By combining sharp edges with these softened, speckled transitions, the illustration achieves a playful, editorial feel.
```

</details>

<a id="omni-shoes-tilt-up"></a>
### Start on the shoes, tilt up, then widen

<a href="https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/FfbFqJ8qhY_ZWZyz/gemini-omni__prompt-guide__boots.webm"><img src="previews/omni-shoes-tilt-up.jpg" width="360"></a>

Three camera moves chained in one line, in the order they happen.

Gemini Omni Flash · Video edit · Source: [Gemini Omni prompt guide](https://deepmind.google/models/gemini-omni/prompt-guide/)

[`camera-move`](#tag-camera-move) [`multi-turn-edit`](#tag-multi-turn-edit)

<details><summary><b>Prompt</b></summary>

```text
Change the camera angle, a close-up on his shoes, quickly tilting up to medium shot, then widening.
```

</details>

<a id="omni-skateboard-motion-fx"></a>
### Add cartoon motion lines to live skateboarding

<a href="https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/FfbFqJ8qhY_ZWZyz/gemini-omni__prompt-guide__skateboard.webm"><img src="previews/omni-skateboard-motion-fx.jpg" width="360"></a>

`keeping everything the same` locks the footage, so the edit only layers effects on top.

Gemini Omni Flash · Video edit · Source: [Gemini Omni prompt guide](https://deepmind.google/models/gemini-omni/prompt-guide/)

[`vfx`](#tag-vfx) [`mixed-media`](#tag-mixed-media)

<details><summary><b>Prompt</b></summary>

```text
Edit this keeping everything the same. Add animated motion effects coming out of the skateboard.
```

</details>

<a id="omni-storyboard-to-video"></a>
### Hand it a storyboard, get the scene

<a href="https://storage.googleapis.com/deepmind-media/DeepMind.com/Models/gemini-omni/prompt-guide/gemini_omni__prompt-guide__storyboard.webm"><img src="previews/omni-storyboard-to-video.jpg" width="360"></a>

The storyboard image carries the plot. The text only sets reading order, total length and tone.

Gemini Omni Flash · Reference-to-video · Source: [Gemini Omni prompt guide](https://deepmind.google/models/gemini-omni/prompt-guide/)

[`storyboard`](#tag-storyboard) [`multi-shot`](#tag-multi-shot)

<details><summary><b>Prompt</b></summary>

```text
Show me in this story. Follow the story exactly in order starting top left. Entire story in 10 seconds. Cinematic
```

</details>

Inputs: [1](https://storage.googleapis.com/deepmind-media/DeepMind.com/Models/gemini-omni/prompt-guide/gemini-omni__reference-anything-storyboard-ingredient-01.webp) · [2](https://storage.googleapis.com/deepmind-media/DeepMind.com/Models/gemini-omni/prompt-guide/gemini-omni__reference-anything-storyboard-ingredient-02.webp)

<a id="omni-violinist-over-shoulder"></a>
### Move the camera over the violinist's shoulder

<a href="https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/3cYlYfozIFs5_Ngj/gemini-omni__edit-over-multiple-turns-with-consistency__angle.webm"><img src="previews/omni-violinist-over-shoulder.jpg" width="360"></a>

A camera change written as one plain sentence. Omni re-renders the same performance from the new angle.

Gemini Omni Flash · Video edit · Source: [Gemini Omni prompt guide](https://deepmind.google/models/gemini-omni/prompt-guide/)

[`multi-turn-edit`](#tag-multi-turn-edit) [`camera-angle`](#tag-camera-angle)

<details><summary><b>Prompt</b></summary>

```text
Change the camera angle to be over the violinist’s shoulder.
```

</details>

Inputs: [1](https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/3cYlYfozIFs5_Ngj/gemini-omni__edit-over-multiple-turns-with-consistency__invisible.webm)

<a id="omni-word-by-word-sizzle"></a>
### Kinetic type, one word per beat

<a href="https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/FfbFqJ8qhY_ZWZyz/gemini-omni__prompt-guide__text.webm"><img src="previews/omni-word-by-word-sizzle.jpg" width="360"></a>

Lists the exact words in order and asks for a new animation style on each. Good test of on-screen text.

Gemini Omni Flash · Text-to-video · Source: [Gemini Omni prompt guide](https://deepmind.google/models/gemini-omni/prompt-guide/)

[`text-render`](#tag-text-render) [`motion-graphics`](#tag-motion-graphics)

<details><summary><b>Prompt</b></summary>

```text
word by word, one word on a the screen at a time: did, you, know, that, this, model, can, do, pretty, good, text!? each word appears with a different animated style, perfect pacing to a rhythm, sizzle reel.
```

</details>

<a id="kling30"></a>
## Kling 3.0

<a id="kling-baseball-bat-logo"></a>
### Logo on a baseball bat stays sharp through the swing

<a href="https://static-54.klingai-cdn-aws.com/kling-blog/presigned_url/50fdd9a7-e3d7-4d62-8715-edaa9b3003bc_文字_棒球.mp4"><img src="previews/kling-baseball-bat-logo.jpg" width="360"></a>

One sentence that ties the camera to a word on a moving object. A quick test for text stability.

Kling 3.0 · Image-to-video · Source: [Kling VIDEO 3.0 user guide](https://app.klingai.com/global/quickstart/klingai-video-3-model-user-guide)

[`text-render`](#tag-text-render) [`sports`](#tag-sports)

<details><summary><b>Prompt</b></summary>

```text
The camera remains fixed on the word "KLING" emblazoned on the baseball bat as the player swings and hits the ball.
```

</details>

Inputs: [1](https://static-3.klingai-cdn-aws.com/kling-blog/file_by_url/a8527e3967d0a358562fddac74c2c9e13c98135619da9af77ea326fe756fb0ff.png)

<a id="kling-family-reacts-to-twist"></a>
### Four family members react to a plot twist

<a href="https://static-86.klingai-cdn-aws.com/kling-blog/presigned_url/8aa6f5a2-b121-4b08-840d-827cc670c4be_kling_20260202_作品_居家环境_背景有轻微_5022_0.mp4"><img src="previews/kling-family-reacts-to-twist.jpg" width="360"></a>

Four speakers, each tagged by role and tone (`Mom (softly, in a surprised tone)`), so lines land on the right face.

Kling 3.0 · Image-to-video · Source: [Kling VIDEO 3.0 user guide](https://app.klingai.com/global/quickstart/klingai-video-3-model-user-guide)

[`dialogue`](#tag-dialogue) [`multi-speaker`](#tag-multi-speaker) [`ambience`](#tag-ambience)

<details><summary><b>Prompt</b></summary>

```text
Home setting with a faint hum of the living room air conditioner in the background for a realistic daily vibe. Mom (softly, in a surprised tone): Wow, I didn’t expect this plot at all. Dad (in a low voice, agreeing, in a calm tone): Yeah, it’s totally unexpected. Never thought that would happen. Boy (in an excited tone): It’s the best twist ever! Girl (nodding along, in an enthusiastic tone): I can’t believe they did that!
```

</details>

Inputs: [1](https://static--49.klingai-cdn-aws.com/kling-blog/file_by_url/006b3efc9ecef758c2aac2e8765f63e4b0f7d684de4d8e6e40e50a90fdb426ce.png)

<a id="kling-indian-accent-order"></a>
### Ordering dinner with an Indian English accent

<a href="https://static-78.klingai-cdn-aws.com/kling-blog/presigned_url/29736974-c5c6-46d2-a9af-ec0413fb74ef_kling_20260204_作品_多镜头_一位中年男子_5210_1.mp4"><img src="previews/kling-indian-accent-order.jpg" width="360"></a>

Accent is named once before the line. The pause between the two sentences is written as an action (`then he looks up`).

Kling 3.0 · Image-to-video · Source: [Kling VIDEO 3.0 user guide](https://app.klingai.com/global/quickstart/klingai-video-3-model-user-guide)

[`dialogue`](#tag-dialogue) [`accent`](#tag-accent) [`multi-shot`](#tag-multi-shot)

<details><summary><b>Prompt</b></summary>

```text
A middle-aged man is ordering food in a Western restaurant. He speaks in English with an Indian accent and says: "excuse me, I would like to order a seafood pasta, and a filet mignon. medium-rare", then he looks up and continues: “And, do you have any drink recommendations?”
```

</details>

Inputs: [1](https://static--52.klingai-cdn-aws.com/kling-blog/file_by_url/4a06a8651731e50c212477bcb626257d4e1ba3576eb48ff57aa077cd6a5d9d4f.png)

<a id="kling-japanese-station-bento"></a>
### Bento handed over at a misty station, in Japanese

<a href="https://static--87.klingai-cdn-aws.com/kling-blog/presigned_url/3d106f34-7b24-462f-9238-0a9d4c3981dc_kling_20260204_作品_清晨薄雾的小站_男生_5550_3.mp4"><img src="previews/kling-japanese-station-bento.jpg" width="360"></a>

Japanese lines in corner brackets, no speaker labels beyond `the boy` and `the girl`. Shows Kling's Japanese lip sync.

Kling 3.0 · Image-to-video · Source: [Kling VIDEO 3.0 user guide](https://app.klingai.com/global/quickstart/klingai-video-3-model-user-guide)

[`dialogue`](#tag-dialogue) [`multilingual`](#tag-multilingual) [`japanese`](#tag-japanese)

<details><summary><b>Prompt</b></summary>

```text
On a small station shrouded in morning mist, the boy smiled and handed over the bento: 「急いで作ったけど、大丈夫？ お母さんのレシピだよ。」The girl took it with a smile: 「うん、きっと美味しい！ 到着したら LINE するね。」
```

</details>

Inputs: [1](https://static-39.klingai-cdn-aws.com/kling-blog/file_by_url/1e96651baca4447550008b624ccb8723fb4d5aa383734b8744042d031532e619.jpg)

<a id="kling-joseon-lady-and-maid"></a>
### Joseon noblewoman and her maid

<a href="https://static-41.klingai-cdn-aws.com/kling-blog/presigned_url/d7236484-7cf3-4092-a019-4321dbc661b4_kling_20260202_作品_镜头聚焦两人的互动__4898_0.mp4"><img src="previews/kling-joseon-lady-and-maid.jpg" width="360"></a>

Period drama in Korean. Tone words (`warm, gentle`, `with deference`) set the social register between the two.

Kling 3.0 · Image-to-video · Source: [Kling VIDEO 3.0 user guide](https://app.klingai.com/global/quickstart/klingai-video-3-model-user-guide)

[`dialogue`](#tag-dialogue) [`multilingual`](#tag-multilingual) [`period`](#tag-period)

<details><summary><b>Prompt</b></summary>

```text
The camera lingers on their interaction— the noble lady’s gaze soft and mild, her maid listening with her head bowed. The lady lifts a hand to smooth her sleeve gently, and speaks in a warm, gentle tone: “오늘 후원에서 피어난 꽃을 보니, 시원한 바람이 분다. 너도 함께 걸어볼까?” The maid inclines her body slightly forward, and replies with deference: “네, 아씨님. 따라갈게요.
```

</details>

Inputs: [1](https://static-10.klingai-cdn-aws.com/kling-blog/file_by_url/6ea73c8a737512559f23bb74328f56539882634fa386241b340d5af0c0314b93.jpg)

<a id="kling-korean-rooftop"></a>
### Korean high-school rooftop at night

<a href="https://static-74.klingai-cdn-aws.com/kling-blog/presigned_url/43cd806c-13a5-4375-906d-7c29f632b04c_kling_20260202_作品_韩国高中屋顶场景下__5286_0.mp4"><img src="previews/kling-korean-rooftop.jpg" width="360"></a>

Language is declared inside each speaker tag: `Boy (casual tone, Korean)`.

Kling 3.0 · Image-to-video · Source: [Kling VIDEO 3.0 user guide](https://app.klingai.com/global/quickstart/klingai-video-3-model-user-guide)

[`dialogue`](#tag-dialogue) [`multilingual`](#tag-multilingual) [`korean`](#tag-korean)

<details><summary><b>Prompt</b></summary>

```text
On the rooftop of a Korean high school, distant city lights glimmer in the background with a soft wind rustling, and stars twinkle in the night sky. The girl leans against the railing, lost in thought. The boy walks over with two cans of cola, hands one to her, and she takes it and pops the tab open. Boy (casual tone, Korean): "숙제 다 했어? 왜 여기 있어?" Girl (sighing, Korean): "시험이 너무 무서워". Boy (gentle tone, Korean): “걱정 마, 넌 잘할 거야.”
```

</details>

Inputs: [1](https://static-46.klingai-cdn-aws.com/kling-blog/file_by_url/f04a52d4d7bbeb30091cb136cd8623e84bd995776b765099fcc5ddcbbaf07391.png)

<a id="kling-madrid-asking-directions"></a>
### Asking directions in Madrid, in halting Spanish

<a href="https://static-45.klingai-cdn-aws.com/kling-blog/presigned_url/10902407-6b2f-4e1c-86f4-ae81f9da21c2_kling_20260204_作品_阳光洒满马德里老街__3484_0.mp4"><img src="previews/kling-madrid-asking-directions.jpg" width="360"></a>

Three speakers with different fluency: the tourist is told to speak slowly with an awkward accent, the clerk lightly and cheerfully.

Kling 3.0 · Image-to-video · Source: [Kling VIDEO 3.0 user guide](https://app.klingai.com/global/quickstart/klingai-video-3-model-user-guide)

[`dialogue`](#tag-dialogue) [`multilingual`](#tag-multilingual) [`spanish`](#tag-spanish) [`accent`](#tag-accent)

<details><summary><b>Prompt</b></summary>

```text
Sunlight fills the old streets of Madrid. In front of a street-side bakery, a Chinese female tourist and a male tourist wearing a gray hoodie walk toward the shop clerk, both wearing polite smiles. Female tourist (speaking slightly slowly, with an awkward accent, in Spanish):Disculpe, ¿dónde está la plaza mayor? A white-haired Spanish shop clerk (turning slightly and pointing forward, with a light and cheerful tone, in Spanish):Por allí, a dos calles. Muy cerca. The female tourist nods to express her thanks. The male tourist also nods in agreement and says (in Spanish): Muchas gracias. The shop clerk smiles and nods in response. The two tourists then turn and walk in the indicated direction.
```

</details>

Inputs: [1](https://static--53.klingai-cdn-aws.com/kling-blog/file_by_url/e4699b0ea66d1a1b6b94dcc1dedc462be6136f1a4fe5d263b719f7bd54dc8992.png)

<a id="kling-moonlit-garden-run"></a>
### Woman in green runs across a moonlit garden, 15 s

<a href="https://static--79.klingai-cdn-aws.com/kling-blog/presigned_url/3f219e9a-5e38-46ed-af01-9831ebce2f2a_kling_20260203_作品_超广角中远景横向跟拍_4556_0.mp4"><img src="previews/kling-moonlit-garden-run.jpg" width="360"></a>

A 15-second continuous shot written as a director's paragraph: lens, rig height, grade, then action in order.

Kling 3.0 · Image-to-video · Source: [Kling VIDEO 3.0 user guide](https://app.klingai.com/global/quickstart/klingai-video-3-model-user-guide)

[`long-take`](#tag-long-take) [`film-look`](#tag-film-look) [`camera-move`](#tag-camera-move)

<details><summary><b>Prompt</b></summary>

```text
Opening with an ultra-wide-angle medium-long shot tracking horizontally, the stabilizer moves low to the ground, with a highly contrasting romantic cinematic tone of cold blue night and silvery white starry sky, exuding a strong poetic realism and classical epic temperament. The protagonist is a young woman in a dark green long dress, running with all her might on the garden lawn illuminated by moonlight; her skirt billows in the wind forming surging dynamic curves, she clutches a small white flower in her right hand and lifts the hem of her dress with her left, breathing rapidly yet with a firm gaze. At the 4th second, the camera accelerates forward with her, and multiple men and women in old-era ball gowns break into the frame one after another from the left and right sides in the background, running alongside her—some try to approach, some turn back to shout, yet none truly touch her, implying pursuit and escape. At the 8th second, the camera gradually zooms in to a medium shot, pans to track forward in front of the protagonist and lifts slightly; she glances back briefly at a young male character behind her, their gazes meet for a split second, emotions erupt mid-run, and the woman and man join hands to run together. At the 12th second, the music and movement reach a climax; the camera moves forward close to her side face and fluttering hair, she releases the white flower and tosses it into the air, the flower drifting down in slow motion as the crowd behind brushes past it. In the final 3 seconds, the camera keeps moving forward, the woman and man break through the crowd and dash toward the starry sky at the end of the garden, their figures gradually taking over the center of the frame. The overall atmosphere is fiery, romantic and resolute, a burst of narrative about fate, choice and freedom.
```

</details>

Inputs: [1](https://static--91.klingai-cdn-aws.com/kling-blog/file_by_url/21ef15bece0400c220dd7db92c388544a486345d867b33673fec8ba66b1ee2c6.png)

<a id="kling-office-long-take"></a>
### One take follows a woman from elevator to desk

<a href="https://static--46.klingai-cdn-aws.com/kling-blog/presigned_url/cf695909-2395-4433-a0b1-caeb28df578d_kling_20260201_作品_平稳跟拍长镜头一镜到_3635_0.mp4"><img src="previews/kling-office-long-take.jpg" width="360"></a>

Start frame plus a bound character element. The prompt spells out how the camera moves with her: track when she walks, stop when she stops.

Kling 3.0 · Image-to-video · Source: [Kling VIDEO 3.0 user guide](https://app.klingai.com/global/quickstart/klingai-video-3-model-user-guide)

[`long-take`](#tag-long-take) [`character-consistency`](#tag-character-consistency) [`tracking-shot`](#tag-tracking-shot)

<details><summary><b>Prompt</b></summary>

```text
Authentic workplace texture, one continuous long take without any cuts. The camera follows the professional woman steadily in a medium shot throughout, moving in sync with her: the camera tracks her as she walks and freezes instantly when she pauses, with natural and smooth movements and fluid camera work. The woman walks forward out of the elevator, and the elevator doors close slowly and naturally behind her; she steps into the office area, takes off her sunglasses by hand, tucks them into her commuter bag casually, and nods politely to colleagues passing by; she pauses briefly, the camera freezes in sync, she hangs her commuter bag on the coat rack in the office area, then takes off her outer coat and hangs it on the same rack; after hanging up her clothes, she walks forward again, the camera tracks her in sync; a young man in a formal shirt walks towards her, hands her a document and a signature pen, she pauses, the camera freezes in sync, takes them and signs the document; after signing, she walks forward again, the camera tracks her in sync; finally, she walks to her desk, sits down by the chair, reaches out to pick up a cup of tea on the desk, and sips it with her head down, her movements relaxed and natural.
```

</details>

Inputs: [1](https://static-44.klingai-cdn-aws.com/kling-blog/file_by_url/f810ae350b11c0469938a2dc73724c09618b56830d84f506027187df168c830e.png)

<a id="kling-orbit-to-smile"></a>
### Camera circles to her face, she looks up and smiles

<a href="https://static-36.klingai-cdn-aws.com/kling-blog/presigned_url/53d2490e-3ad9-4d84-b74f-bc0b1fcc4151_kling_20260204_作品_镜头逐渐环绕至女孩的_4266_2.mp4"><img src="previews/kling-orbit-to-smile.jpg" width="360"></a>

Same one-line prompt run twice, with and without a bound element. The page shows both outputs so you can compare face consistency.

Kling 3.0 · Image-to-video · Source: [Kling VIDEO 3.0 user guide](https://app.klingai.com/global/quickstart/klingai-video-3-model-user-guide)

[`character-consistency`](#tag-character-consistency) [`orbit`](#tag-orbit) [`image-to-video`](#tag-image-to-video)

<details><summary><b>Prompt</b></summary>

```text
The camera gradually moves around to the front of the girl, who then lifts her head and smiles warmly at the camera, as if seeing an old friend after many years.
```

</details>

Inputs: [1](https://static--64.klingai-cdn-aws.com/kling-blog/file_by_url/445147e8acb2e81e4c06a4a819081baeacbdbcf1824946cf1cd9b5a2f0c4e0f5.png)

<a id="kling-perfume-paris-ad"></a>
### Perfume ad by a Paris window

<a href="https://static--72.klingai-cdn-aws.com/kling-blog/presigned_url/27107c4f-403c-412d-94b7-20a8835c8ffa_kling_20260202_作品_巴黎公寓窗边场景下__5018_0.mp4"><img src="previews/kling-perfume-paris-ad.jpg" width="360"></a>

Product shot that keeps the bottle's printed name legible. Voiceover, accent and BGM are all specified in the prompt.

Kling 3.0 · Image-to-video · Source: [Kling VIDEO 3.0 user guide](https://app.klingai.com/global/quickstart/klingai-video-3-model-user-guide)

[`product-ad`](#tag-product-ad) [`text-render`](#tag-text-render) [`voiceover`](#tag-voiceover)

<details><summary><b>Prompt</b></summary>

```text
By the window of a Parisian apartment, with soft French piano BGM in the background, the gilded afternoon sunlight filters through the shutters onto the perfume bottle, casting dappled light and shadow. The camera pans slowly in from the scattered rose petals, shifting focus to the faceted cut of the Kling perfume bottle. Voiceover (lazy French female voice, British accent, slow pace): Bathe in the golden hour. The camera orbits the perfume bottle in slow motion, capturing the play of light and shadow on the golden lettering and bottle body. Voiceover: Kling, a whisper of Parisian elegance. The camera pulls back and freezes on the complete scene—the Kling perfume bottle standing on a velvet pedestal, with Parisian buildings faintly visible outside the window. Voiceover: Wrap yourself in luxury with every breath.
```

</details>

Inputs: [1](https://static--74.klingai-cdn-aws.com/kling-blog/file_by_url/3de2fbc80df150e68fc05823f829a0fd88e2145ed4b4dbfb2f6a6a4fd5dbea87.png)

<a id="kling-plaster-tower-dinosaur"></a>
### Inside a plaster-statue tower, a dinosaur reunion

<a href="https://static-17.klingai-cdn-aws.com/kling-blog/presigned_url/9d0eec96-49d3-4229-a2c0-f38ceb5974e0_没想到吧Alex是只恐龙.mp4"><img src="previews/kling-plaster-tower-dinosaur.jpg" width="360"></a>

Declares `single unbroken shot with no edited transitions` up front, then carries one emotional arc from despair to reunion.

Kling 3.0 · Image-to-video · Source: [Kling VIDEO 3.0 user guide](https://app.klingai.com/global/quickstart/klingai-video-3-model-user-guide)

[`long-take`](#tag-long-take) [`emotion`](#tag-emotion) [`creature`](#tag-creature)

<details><summary><b>Prompt</b></summary>

```text
This is a 15-second cinematic long take, a single unbroken shot with no edited transitions. The scene is set inside a tower of plaster statues dappled with light and shadow, surrounded by towering white plaster sculptures, evoking an air of mystery and oppression. The shot opens with the protagonist skidding to a halt at the center of the scene after a frantic run, chest heaving, expression dazed and helpless, fear glinting in their eyes. The camera orbits the protagonist in a smooth 360-degree pan. As the camera rotates, the protagonist glances anxiously around and shouts: "Alex! Alex where are you! Are you here?" A cute dinosaur cry then echoes in the background, and the camera pushes in over the protagonist’s shoulder to their back— a small to medium-sized, adorable baby dinosaur steps out from behind a plaster pillar, letting out a sweet chirp. Startled by the sound, the protagonist whips around; catching sight of the dinosaur, they burst into tears instantly and rush forward without hesitation to clasp it tightly in their arms. The dinosaur nestles obediently against them. Sobbing, the protagonist strokes the dinosaur gently and trembles: "I found you! Thank God, I’m so scared!" The overall lighting and shadow boast a cinematic texture, with the emotion shifting from despair to an overwhelmingly touching reunion.
```

</details>

Inputs: [1](https://static-47.klingai-cdn-aws.com/kling-blog/file_by_url/fe49a43ec06b9e0cdf7f555268cbe2a18c35175ab6cc25fc2b1150218076b6d9.png)

<a id="kling-snowmobile-six-shots"></a>
### Snowmobile run in six shots

<a href="https://static-14.klingai-cdn-aws.com/kling-blog/presigned_url/fbf5a59b-e1c0-45ee-9ec8-13726d3d3887_kling_20260202_作品_镜头_1_2s_后远_4947_0.mp4"><img src="previews/kling-snowmobile-six-shots.jpg" width="360"></a>

Six shots, each defined only by angle and camera move. The landscape is described once, in the last shot.

Kling 3.0 · Image-to-video · Source: [Kling VIDEO 3.0 user guide](https://app.klingai.com/global/quickstart/klingai-video-3-model-user-guide)

[`multi-shot`](#tag-multi-shot) [`camera-move`](#tag-camera-move) [`action`](#tag-action)

<details><summary><b>Prompt</b></summary>

```text
Shot 1, Low-angle rear wide shot, tracking behind the rider as they move forward. Shot 2, Low-angle side close-up, a detailed shot of the motorcycle wheel. Shot 3, First-person POV from the rider, with the handlebars and instrument panel visible ahead. Shot 4, Frontal medium shot, tracking backward in front of the motorcycle, the rider’s helmet facing the camera. Shot 5, Side-on eye-level tracking shot with slight lateral movement. Shot 6, High-angle wide shot with a gentle downward tilt. The camera rises as the snowmobile rides deeper into the snowfield, leaving winding tracks carved into the pristine white snow, with snow-covered forests scattered on both sides.
```

</details>

Inputs: [1](https://static-29.klingai-cdn-aws.com/kling-blog/file_by_url/ef7ccbdcafe3af9d5fbbe492976b10793b302cc4ecab0778734b129dc7db9570.png)

<a id="kling-truck-driver-four-shots"></a>
### Truck driver in four handheld shots

<a href="https://static-94.klingai-cdn-aws.com/kling-blog/presigned_url/b77930c4-755d-4035-ba98-842446609ea8_Dave_multi.mp4"><img src="previews/kling-truck-driver-four-shots.jpg" width="360"></a>

Custom Multi-Shot from Kling creative partner Dave Clark. Every shot repeats `cinematic handheld` so the look holds across cuts.

Kling 3.0 · Image-to-video · Source: [Kling VIDEO 3.0 user guide](https://app.klingai.com/global/quickstart/klingai-video-3-model-user-guide)

[`multi-shot`](#tag-multi-shot) [`handheld`](#tag-handheld) [`film-look`](#tag-film-look)

<details><summary><b>Prompt</b></summary>

```text
shot 1, profile shot of black man driving a truck, cinematic handheld. Shot 2, frontal macro shot of black man driving a truck, cinematic handheld. Shot 3, macro shot of hands on the steering wheel, cinematic handheld. Shot 4, macro shot of a weathered picture of a young black child laying on the passenger side seat, cinematic handheld.
```

</details>

Inputs: [1](https://static--56.klingai-cdn-aws.com/kling-blog/file/0c5b8af23bea126e21beac535408c4cf6020f44cc773e2985ab1c32c42756216.jpg)

<a id="kling-villa-terrace-dialogue"></a>
### Villa terrace, a two-person summer dialogue

<a href="https://static-37.klingai-cdn-aws.com/kling-blog/presigned_url/206908e5-edd9-4f12-a7cb-2baca6a0f2bd_kling_20260203_作品_欧洲别墅户外露台场景_4118_0.mp4"><img src="previews/kling-villa-terrace-dialogue.jpg" width="360"></a>

Multi-Shot on: the model plans the shot-reverse-shot by itself from one paragraph of action and dialogue.

Kling 3.0 · Image-to-video · Source: [Kling VIDEO 3.0 user guide](https://app.klingai.com/global/quickstart/klingai-video-3-model-user-guide)

[`multi-shot`](#tag-multi-shot) [`dialogue`](#tag-dialogue) [`shot-reverse-shot`](#tag-shot-reverse-shot)

<details><summary><b>Prompt</b></summary>

```text
Outdoor terrace of a European villa, by a dining table with a blue and white checkered tablecloth, a young white woman in a blue and white striped short-sleeve shirt and khaki shorts, with a brown belt, sits barefoot, opposite a young white man in a white T-shirt. The camera zooms in, the woman swirls the juice in a glass, her eyes looking at the distant woods, and says "These trees will turn yellow in a month, won't they?". Close-up of the man, he lowers his head and says, "but they'll be green again next summer.". Then the woman turns her head, smiles at the man opposite, and says, "Are you always this optimistic? Or just about summer?". Then the man lifts his head, looks at the woman and says, “Only about summers with you.”
```

</details>

Inputs: [1](https://static-6.klingai-cdn-aws.com/kling-blog/file_by_url/1e8ad2ce90036c01aa7fe86c89178590aaf136880206c40d8fc0f99e68d93445.png)

<a id="veo3"></a>
## Veo 3

<a id="veo-camper-and-bear"></a>
### Stop-motion camper and a bear with a comeback

<a href="https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/media/veo__veo-3__camper.webm"><img src="previews/veo-camper-and-bear.jpg" width="360"></a>

The whole prompt is a format label plus two lines of dialogue. Veo fills in the scene.

Veo 3 · Text-to-video · Source: [Veo 3 prompt guide](https://deepmind.google/models/veo/prompt-guide/)

[`stop-motion`](#tag-stop-motion) [`dialogue`](#tag-dialogue) [`comedy`](#tag-comedy)

<details><summary><b>Prompt</b></summary>

```text
Camping (Stop Motion): Camper: "I'm one with nature now!" Bear: "Nature would prefer some personal space."
```

</details>

<a id="veo-candy-keyboard"></a>
### Keyboard made of candy

<a href="https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/media/veo__veo-3__keyboard.webm"><img src="previews/veo-candy-keyboard.jpg" width="360"></a>

A separate `Audio:` line tells the model what the scene should sound like.

Veo 3 · Text-to-video · Source: [Veo 3 prompt guide](https://deepmind.google/models/veo/prompt-guide/)

[`sfx`](#tag-sfx) [`product`](#tag-product) [`whimsical`](#tag-whimsical)

<details><summary><b>Prompt</b></summary>

```text
A keyboard whose keys are made of different types of candy. Typing makes sweet, crunchy sounds. Audio: Crunchy, sugary typing sounds, delighted giggles.
```

</details>

<a id="veo-moon-dust-flowers"></a>
### Crystal flowers on a moon-dust plain

<a href="https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/media/veo__veo-3__moon-dust.webm"><img src="previews/veo-moon-dust-flowers.jpg" width="360"></a>

Short world-building prompt. One striking detail (`the only footprints in untouched dust`) does more than a long list.

Veo 3 · Text-to-video · Source: [Veo 3 prompt guide](https://deepmind.google/models/veo/prompt-guide/)

[`world-building`](#tag-world-building) [`fantasy`](#tag-fantasy)

<details><summary><b>Prompt</b></summary>

```text
A snow-covered plain of iridescent moon-dust under twilight skies. Thirty-foot crystalline flowers bloom, refracting light into slow-moving rainbows. A fur-cloaked figure walks between these colossal blossoms, leaving the only footprints in untouched dust.
```

</details>

<a id="veo-off-road-rally"></a>
### Off-road rally through a river crossing

<a href="https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/media/veo__veo-3__off-road.mp4"><img src="previews/veo-off-road-rally.jpg" width="360"></a>

A play-by-play for an 8-second action beat. It also asks for unbranded vehicles, which keeps logos out of the frame.

Veo 3 · Text-to-video · Source: [Veo 3 prompt guide](https://deepmind.google/models/veo/prompt-guide/)

[`action`](#tag-action) [`handheld`](#tag-handheld) [`sfx`](#tag-sfx)

<details><summary><b>Prompt</b></summary>

```text
The scene explodes with the raw, visceral, and unpredictable energy of a hardcore off-road rally, captured with a dynamic, almost found-footage or embedded sports documentary aesthetic. The camera is often shaky, seemingly mounted inside one of the vehicles or held by a daring spectator very close to the action, frequently splattered with mud or water, catching unintentional lens flares from the natural, often harsh, sunlight filtering through trees or reflecting off wet surfaces. We are immersed in a challenging, untamed natural environment – perhaps a dense, muddy forest trail, a treacherous rocky incline littered with loose scree, or a series_of shallow, fast-flowing river crossings. Several heavily modified, entirely unidentifiable, and unbranded off-road vehicles are engaged in a frenetic, no-holds-barred race. These are not showroom models; they are custom-built, rugged machines – open-wheeled buggies with exposed engines and prominent roll cages, heavily armored pickup trucks with oversized, knobby tires and snorkel exhausts, their original forms and manufacturers completely obscured by extreme modifications, layers of caked-on mud, and a general air of brutal functionality. The dominant sounds are the deafening, guttural roar of powerful, untamed engines, the whine of transmissions, the percussive impact of suspension bottoming out, and the constant spray of mud and water. Within an 8-second sequence, one of the lead vehicles, a low-slung, open-cockpit buggy so caked in thick, brown mud that its original color is a mystery, approaches a wide, shallow river crossing at incredible speed. Without the slightest hesitation, its unseen driver powers straight into the water. The impact sends an enormous, almost solid, opaque sheet of muddy water, mixed with stones and debris from the riverbed, spectacularly high into the air, completely engulfing the small buggy for a terrifying moment, obscuring it from view as if it has been swallowed by the river itself. Right on its tail, a pursuing, equally mud-encrusted, custom-built truck – a hulking, high-clearance beast with a heavily reinforced external roll cage and no discernible badging – arrives at the river crossing just as this massive wall of airborne water reaches its peak. Instead of slowing or attempting to find a clearer path, the truck's driver, with unwavering aggression, plunges directly into and through this opaque, turbulent curtain of muddy spray at full throttle. A split second later, the truck bursts out from the other side of the deluge, water cascading from its roof and chassis, its oversized windshield wipers struggling frantically to clear the torrent of muddy water obscuring the driver's vision. It lands heavily on the far bank, suspension groaning, but still in hot pursuit of the now-reappearing buggy. This thrilling, messy, and visually spectacular sequence of one vehicle creating a massive environmental obstacle and the next immediately conquering it through sheer force, forms the core, immersive, attention-grabbing event of the 8-second sequence. The race continues with undiminished ferocity, the natural terrain itself an active participant in the conflict.
```

</details>

<a id="veo-old-sailor-verse"></a>
### Old sailor speaks in verse

<a href="https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/media/veo__veo-3__sailor.webm"><img src="previews/veo-old-sailor-verse.jpg" width="360"></a>

Character first (hat, beard, pipe), then the spoken line in quotes. Veo 3 lip-syncs the quoted text.

Veo 3 · Text-to-video · Source: [Veo 3 prompt guide](https://deepmind.google/models/veo/prompt-guide/)

[`dialogue`](#tag-dialogue) [`character`](#tag-character)

<details><summary><b>Prompt</b></summary>

```text
A medium shot frames an old sailor, his knitted blue sailor hat casting a shadow over his eyes, a thick grey beard obscuring his chin. He holds his pipe in one hand, gesturing with it towards the churning, grey sea beyond the ship's railing. "This ocean, it's a force, a wild, untamed might. And she commands your awe, with every breaking light"
```

</details>

<a id="sora2"></a>
## Sora 2

<a id="sora-fridge-monster"></a>
### A chubby purple monster comes out of the fridge

<a href="https://cdn.openai.com/API/docs/images/sora/sora_monster_original.gif"><img src="previews/sora-fridge-monster.jpg" width="360"></a>

Two short beats: the door opens, the monster comes out.

Sora 2 · Image-to-video · Source: [Sora 2 prompting guide](https://cookbook.openai.com/examples/sora/sora2_prompting_guide)

[`image-to-video`](#tag-image-to-video) [`creature`](#tag-creature) [`whimsical`](#tag-whimsical)

<details><summary><b>Prompt</b></summary>

```text
The fridge door opens. A cute, chubby purple monster comes out of it.
```

</details>

Inputs: [1](https://cdn.openai.com/API/docs/images/sora/monster_original_720p.jpeg)

<a id="sora-monster-edits"></a>
### Edit the monster: recolour it, then add a second one

<a href="https://cdn.openai.com/API/docs/images/sora/sora_monster_2monsters.gif"><img src="previews/sora-monster-edits.jpg" width="360"></a>

Each edit is a separate run on the original clip and changes one thing. OpenAI's advice: describe only the tweak.

Sora 2 · Video edit · Source: [Sora 2 prompting guide](https://cookbook.openai.com/examples/sora/sora2_prompting_guide)

[`multi-turn-edit`](#tag-multi-turn-edit) [`object-swap`](#tag-object-swap)

<details><summary><b>Prompt</b></summary>

```text
Change the color of the monster to orange
A second monster comes out right after
```

</details>

Inputs: [1](https://cdn.openai.com/API/docs/images/sora/sora_monster_original.gif)

<a id="sora-skyline-turn-and-walk"></a>
### She turns, smiles and walks out of frame

<a href="https://cdn.openai.com/API/docs/images/sora/sora_woman_skyline_video.gif"><img src="previews/sora-skyline-turn-and-walk.jpg" width="360"></a>

With an input image the first frame is set, so the prompt only describes what happens next.

Sora 2 · Image-to-video · Source: [Sora 2 prompting guide](https://cookbook.openai.com/examples/sora/sora2_prompting_guide)

[`image-to-video`](#tag-image-to-video) [`character`](#tag-character)

<details><summary><b>Prompt</b></summary>

```text
She turns around and smiles, then slowly walks out of the frame.
```

</details>

Inputs: [1](https://cdn.openai.com/API/docs/images/sora/woman_skyline_original_720p.jpeg)

<a id="recipes"></a>
## Agent recipes: editing video

Tell a coding agent what you want in plain words. Each recipe records the request and the commands the agent ran. Swap in your own clips.

<a id="bilingual-subtitles"></a>
### Transcribe dialogue and burn in Chinese and English subtitles

**Request to the agent**

> Transcribe the Chinese dialogue in samples/night-train-ticket.mp4, check it against the script in prompts/video/night-train-ticket.yaml, add an English line under each Chinese line, and burn the subtitles in.

Whisper gets homophones wrong in Chinese (他 and 她 sound identical). When a script exists, tell the agent to use it for wording and whisper only for timing.

[`agent-editing`](#tag-agent-editing) [`ffmpeg`](#tag-ffmpeg) [`whisper`](#tag-whisper) [`subtitles`](#tag-subtitles) [`bilingual`](#tag-bilingual) [`chinese-dialogue`](#tag-chinese-dialogue)

<details><summary><b>Commands the agent ran</b> · Agent: Claude Opus 5.5 in Claude Code · Tools: ffmpeg 9 with libass, openai-whisper medium</summary>

```bash
whisper samples/night-train-ticket.mp4 --model medium --language zh --output_format srt
# whisper heard 我等了他八年 / 就等着一趟车; the script says 我等了她八年 / 就等这一趟车.
# The agent kept whisper's timing, took the wording from the script, and added English lines:
#   1  00:00:00,000 --> 00:00:02,100  我等了她八年， / I waited eight years for her,
#   2  00:00:02,200 --> 00:00:04,200  就等这一趟车。 / all for this one train.
ffmpeg -i samples/night-train-ticket.mp4 \
  -vf "subtitles=subs.srt:force_style='FontName=PingFang SC,FontSize=15,Outline=1,Shadow=0,MarginV=22'" \
  -c:v libx264 -crf 20 -c:a copy subtitled.mp4
```

</details>

<a id="readme-preview-gif"></a>
### Make a small looping GIF preview for a README

**Request to the agent**

> Make a looping GIF preview of every mp4 in samples/ for the README. Keep each under about 1.5 MB. Speed up clips longer than 8 seconds so the whole story still plays.

Every preview in this repository was made this way: 0.5 to 2 MB each. A per-clip palette with 96 colours and Bayer dithering keeps skin tones and neon clean at a small size.

[`agent-editing`](#tag-agent-editing) [`ffmpeg`](#tag-ffmpeg) [`gif`](#tag-gif) [`preview`](#tag-preview)

<details><summary><b>Commands the agent ran</b> · Agent: Claude Opus 5.5 in Claude Code · Tools: ffmpeg 9</summary>

```bash
# landscape: 360 px wide; vertical: 300 px tall; 2x speed when longer than 8 s
ffmpeg -i in.mp4 -vf "setpts=PTS/2,fps=8,scale=360:-2:flags=lanczos,split[a][b];[a]palettegen=max_colors=96[p];[b][p]paletteuse=dither=bayer:bayer_scale=4" -loop 0 out.gif
```

</details>

<a id="split-shots"></a>
### Split a multi-shot clip into separate shots at the hard cuts

**Request to the agent**

> samples/late-night-office.mp4 should contain nine shots. Find the hard cuts, split the clip into one file per shot, and give me a storyboard strip with the middle frame of every shot.

Doubles as a QA check for generated video: all eight cuts landed within 0.17 s of the timestamps written in the prompt. Lower the threshold for soft cuts, raise it for handheld footage with lots of motion.

[`agent-editing`](#tag-agent-editing) [`ffmpeg`](#tag-ffmpeg) [`scene-detection`](#tag-scene-detection) [`storyboard`](#tag-storyboard) [`qa`](#tag-qa)

<details><summary><b>Commands the agent ran</b> · Agent: Claude Opus 5.5 in Claude Code · Tools: ffmpeg 9</summary>

```bash
# 1. find cuts
T=$(ffmpeg -i samples/late-night-office.mp4 -vf "scdet=threshold=8" -f null - 2>&1 \
    | grep -o "lavfi.scd.time: [0-9.]*" | awk '{print $2}' | paste -sd, -)
# -> 3.04,5.04,6.0,6.54,7.0,7.46,9.67,12.17  (prompt asked for 3.0,5.0,6.0,6.5,7.0,7.5,9.5,12.0)
# 2. split, forcing keyframes at the cuts so every file starts clean
ffmpeg -i samples/late-night-office.mp4 -c:v libx264 -crf 20 -force_key_frames "$T" -c:a aac \
  -f segment -segment_times "$T" -reset_timestamps 1 shot_%02d.mp4
# 3. storyboard strip
for f in shot_*.mp4; do
  mid=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f" | awk '{printf "%.3f", $1/2}')
  ffmpeg -ss "$mid" -i "$f" -frames:v 1 -vf scale=-2:320 "${f%.mp4}.jpg"
done
ffmpeg -pattern_type glob -i "shot_*.jpg" -vf "tile=9x1:padding=4:color=white" -frames:v 1 storyboard.jpg
```

</details>

<a id="teaser-montage"></a>
### Cut a teaser from clips of different sizes, with title and crossfades

**Request to the agent**

> Make a 720p teaser called RAIN CITY from the first 4.5 seconds of the neon alley, noodle stall and night train clips. Half-second crossfades on picture and sound, the title over the opening, loudness normalised for social media, fade out at the end.

The inputs are 864x480 and 1344x768; every branch is scaled, cropped and resampled to the same size, frame rate and sample rate first, otherwise xfade and acrossfade refuse to join them. Total length is 3 x 4.5 s minus two 0.5 s overlaps = 12.5 s.

[`agent-editing`](#tag-agent-editing) [`ffmpeg`](#tag-ffmpeg) [`montage`](#tag-montage) [`title-card`](#tag-title-card) [`loudness`](#tag-loudness)

<details><summary><b>Commands the agent ran</b> · Agent: Claude Opus 5.5 in Claude Code · Tools: ffmpeg 9</summary>

```bash
ffmpeg -i samples/neon-night-market-alley.mp4 -i samples/hk-noodle-stall-1960s.mp4 -i samples/night-train-ticket.mp4 -filter_complex "
[0:v]trim=0:4.5,setpts=PTS-STARTPTS,scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,format=yuv420p,setsar=1[v0];
[1:v]trim=0:4.5,setpts=PTS-STARTPTS,scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,format=yuv420p,setsar=1[v1];
[2:v]trim=0:4.5,setpts=PTS-STARTPTS,scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,fps=24,format=yuv420p,setsar=1[v2];
[0:a]atrim=0:4.5,asetpts=PTS-STARTPTS,aresample=48000[a0];
[1:a]atrim=0:4.5,asetpts=PTS-STARTPTS,aresample=48000[a1];
[2:a]atrim=0:4.5,asetpts=PTS-STARTPTS,aresample=48000[a2];
[v0][v1]xfade=transition=fade:duration=0.5:offset=4[x1];
[x1][v2]xfade=transition=fade:duration=0.5:offset=8[x2];
[a0][a1]acrossfade=d=0.5[ax1];
[ax1][a2]acrossfade=d=0.5[ax2];
[x2]drawtext=fontfile=/System/Library/Fonts/Supplemental/Futura.ttc:text='RAIN CITY':fontcolor=white:fontsize=110:x=(w-tw)/2:y=h*0.70:alpha='if(lt(t,0.3),t/0.3,if(lt(t,2.0),1,if(lt(t,2.5),(2.5-t)/0.5,0)))',fade=t=in:st=0:d=0.4,fade=t=out:st=12.1:d=0.4[v];
[ax2]loudnorm=I=-16:TP=-1.5:LRA=11,afade=t=out:st=12:d=0.5[a]" \
  -map "[v]" -map "[a]" -c:v libx264 -crf 20 -c:a aac -b:a 160k -ar 48000 teaser.mp4
```

</details>

<a id="vertical-blur-fill"></a>
### Turn a 16:9 clip into a 9:16 short with a blurred background

**Request to the agent**

> Make a 1080x1920 vertical version of samples/night-train-ticket.mp4 for TikTok. Keep the full frame visible in the middle and fill the top and bottom with a blurred, slightly darkened copy of the same video. Keep the original audio.

One ffmpeg call, 1.5 s on an M-series Mac for a 5 s clip. Use it when the subject spans the whole width; crop instead when the subject sits in the centre.

[`agent-editing`](#tag-agent-editing) [`ffmpeg`](#tag-ffmpeg) [`vertical`](#tag-vertical) [`reframe`](#tag-reframe)

<details><summary><b>Commands the agent ran</b> · Agent: Claude Opus 5.5 in Claude Code · Tools: ffmpeg 9</summary>

```bash
ffmpeg -i samples/night-train-ticket.mp4 -filter_complex "
  [0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=40,eq=brightness=-0.08[bg];
  [0:v]scale=1080:-2[fg];
  [bg][fg]overlay=(W-w)/2:(H-h)/2,format=yuv420p" \
  -c:v libx264 -crf 20 -c:a copy vertical.mp4
```

</details>

<a id="image"></a>
## Image prompts

Coming next, built the same way: official and widely shared prompts, each with its output.

<a id="threed"></a>
## 3D with agents

Recipes for building 3D scenes with coding agents (Blender MCP, three.js) are in progress.

<a id="tags"></a>
## Browse by tag

- <a id="tag-accent"></a>`accent` (2): [Ordering dinner with an Indian English accent](#kling-indian-accent-order), [Asking directions in Madrid, in halting Spanish](#kling-madrid-asking-directions)
- <a id="tag-action"></a>`action` (2): [Snowmobile run in six shots](#kling-snowmobile-six-shots), [Off-road rally through a river crossing](#veo-off-road-rally)
- <a id="tag-agent-editing"></a>`agent-editing` (5): [Transcribe dialogue and burn in Chinese and English subtitles](#bilingual-subtitles), [Make a small looping GIF preview for a README](#readme-preview-gif), [Split a multi-shot clip into separate shots at the hard cuts](#split-shots), [Cut a teaser from clips of different sizes, with title and crossfades](#teaser-montage), [Turn a 16:9 clip into a 9:16 short with a blurred background](#vertical-blur-fill)
- <a id="tag-ambience"></a>`ambience` (1): [Four family members react to a plot twist](#kling-family-reacts-to-twist)
- <a id="tag-animation"></a>`animation` (1): [One clip through crayon, pencil, glass and risograph](#omni-four-style-progression)
- <a id="tag-audio-sync"></a>`audio-sync` (2): [A flock of birds forms the shape of a bird, to music](#omni-birds-form-a-bird), [Apartment lights switch on to the beat](#omni-lights-sync-to-music)
- <a id="tag-bilingual"></a>`bilingual` (1): [Transcribe dialogue and burn in Chinese and English subtitles](#bilingual-subtitles)
- <a id="tag-camera-angle"></a>`camera-angle` (1): [Move the camera over the violinist's shoulder](#omni-violinist-over-shoulder)
- <a id="tag-camera-move"></a>`camera-move` (4): [Woman in green runs across a moonlit garden, 15 s](#kling-moonlit-garden-run), [Snowmobile run in six shots](#kling-snowmobile-six-shots), [Whip-pan from drummer to saxophonist and dancer](#omni-drummer-whip-pan), [Start on the shoes, tilt up, then widen](#omni-shoes-tilt-up)
- <a id="tag-character"></a>`character` (2): [She turns, smiles and walks out of frame](#sora-skyline-turn-and-walk), [Old sailor speaks in verse](#veo-old-sailor-verse)
- <a id="tag-character-consistency"></a>`character-consistency` (2): [One take follows a woman from elevator to desk](#kling-office-long-take), [Camera circles to her face, she looks up and smiles](#kling-orbit-to-smile)
- <a id="tag-chinese-dialogue"></a>`chinese-dialogue` (1): [Transcribe dialogue and burn in Chinese and English subtitles](#bilingual-subtitles)
- <a id="tag-comedy"></a>`comedy` (1): [Stop-motion camper and a bear with a comeback](#veo-camper-and-bear)
- <a id="tag-consistency"></a>`consistency` (1): [Ships to origami, astronaut to anemone, ships to stingrays](#omni-astronaut-three-swaps)
- <a id="tag-creature"></a>`creature` (2): [Inside a plaster-statue tower, a dinosaur reunion](#kling-plaster-tower-dinosaur), [A chubby purple monster comes out of the fridge](#sora-fridge-monster)
- <a id="tag-dialogue"></a>`dialogue` (11): [Make the man in an existing clip speak, in a borrowed voice](#h3-pink-suit-lip-sync-edit), [Four family members react to a plot twist](#kling-family-reacts-to-twist), [Ordering dinner with an Indian English accent](#kling-indian-accent-order), [Bento handed over at a misty station, in Japanese](#kling-japanese-station-bento), [Joseon noblewoman and her maid](#kling-joseon-lady-and-maid), [Korean high-school rooftop at night](#kling-korean-rooftop), [Asking directions in Madrid, in halting Spanish](#kling-madrid-asking-directions), [Villa terrace, a two-person summer dialogue](#kling-villa-terrace-dialogue), [Harbour conversation extended twice](#omni-harbour-extend), [Stop-motion camper and a bear with a comeback](#veo-camper-and-bear), [Old sailor speaks in verse](#veo-old-sailor-verse)
- <a id="tag-emotion"></a>`emotion` (1): [Inside a plaster-statue tower, a dinosaur reunion](#kling-plaster-tower-dinosaur)
- <a id="tag-explainer"></a>`explainer` (1): [Quantum computing explained in risograph flat style](#omni-quantum-explainer)
- <a id="tag-extend"></a>`extend` (1): [Harbour conversation extended twice](#omni-harbour-extend)
- <a id="tag-fantasy"></a>`fantasy` (1): [Crystal flowers on a moon-dust plain](#veo-moon-dust-flowers)
- <a id="tag-ffmpeg"></a>`ffmpeg` (5): [Transcribe dialogue and burn in Chinese and English subtitles](#bilingual-subtitles), [Make a small looping GIF preview for a README](#readme-preview-gif), [Split a multi-shot clip into separate shots at the hard cuts](#split-shots), [Cut a teaser from clips of different sizes, with title and crossfades](#teaser-montage), [Turn a 16:9 clip into a 9:16 short with a blurred background](#vertical-blur-fill)
- <a id="tag-film-look"></a>`film-look` (2): [Woman in green runs across a moonlit garden, 15 s](#kling-moonlit-garden-run), [Truck driver in four handheld shots](#kling-truck-driver-four-shots)
- <a id="tag-first-last-frame"></a>`first-last-frame` (1): [Whip-pan from drummer to saxophonist and dancer](#omni-drummer-whip-pan)
- <a id="tag-focus-pull"></a>`focus-pull` (1): [Ramen in front, family dinner behind, one focus pull](#h3-ramen-focus-pull)
- <a id="tag-food"></a>`food` (1): [Ramen in front, family dinner behind, one focus pull](#h3-ramen-focus-pull)
- <a id="tag-gif"></a>`gif` (1): [Make a small looping GIF preview for a README](#readme-preview-gif)
- <a id="tag-handheld"></a>`handheld` (2): [Truck driver in four handheld shots](#kling-truck-driver-four-shots), [Off-road rally through a river crossing](#veo-off-road-rally)
- <a id="tag-image-to-video"></a>`image-to-video` (3): [Camera circles to her face, she looks up and smiles](#kling-orbit-to-smile), [A chubby purple monster comes out of the fridge](#sora-fridge-monster), [She turns, smiles and walks out of frame](#sora-skyline-turn-and-walk)
- <a id="tag-japanese"></a>`japanese` (1): [Bento handed over at a misty station, in Japanese](#kling-japanese-station-bento)
- <a id="tag-korean"></a>`korean` (1): [Korean high-school rooftop at night](#kling-korean-rooftop)
- <a id="tag-lip-sync"></a>`lip-sync` (1): [Make the man in an existing clip speak, in a borrowed voice](#h3-pink-suit-lip-sync-edit)
- <a id="tag-long-take"></a>`long-take` (5): [Woman in green runs across a moonlit garden, 15 s](#kling-moonlit-garden-run), [One take follows a woman from elevator to desk](#kling-office-long-take), [Inside a plaster-statue tower, a dinosaur reunion](#kling-plaster-tower-dinosaur), [Whip-pan from drummer to saxophonist and dancer](#omni-drummer-whip-pan), [Harbour conversation extended twice](#omni-harbour-extend)
- <a id="tag-loudness"></a>`loudness` (1): [Cut a teaser from clips of different sizes, with title and crossfades](#teaser-montage)
- <a id="tag-mixed-media"></a>`mixed-media` (1): [Add cartoon motion lines to live skateboarding](#omni-skateboard-motion-fx)
- <a id="tag-montage"></a>`montage` (1): [Cut a teaser from clips of different sizes, with title and crossfades](#teaser-montage)
- <a id="tag-motion-graphics"></a>`motion-graphics` (2): [Quantum computing explained in risograph flat style](#omni-quantum-explainer), [Kinetic type, one word per beat](#omni-word-by-word-sizzle)
- <a id="tag-multi-reference"></a>`multi-reference` (2): [Make the man in an existing clip speak, in a borrowed voice](#h3-pink-suit-lip-sync-edit), [A flock of birds forms the shape of a bird, to music](#omni-birds-form-a-bird)
- <a id="tag-multi-shot"></a>`multi-shot` (6): [Starship bridge, the fleet jumps to hyperspace](#h3-starship-hyperspace-jump), [Ordering dinner with an Indian English accent](#kling-indian-accent-order), [Snowmobile run in six shots](#kling-snowmobile-six-shots), [Truck driver in four handheld shots](#kling-truck-driver-four-shots), [Villa terrace, a two-person summer dialogue](#kling-villa-terrace-dialogue), [Hand it a storyboard, get the scene](#omni-storyboard-to-video)
- <a id="tag-multi-speaker"></a>`multi-speaker` (1): [Four family members react to a plot twist](#kling-family-reacts-to-twist)
- <a id="tag-multi-turn-edit"></a>`multi-turn-edit` (5): [Ships to origami, astronaut to anemone, ships to stingrays](#omni-astronaut-three-swaps), [Butterfly to bee to fireflies, one change per turn](#omni-butterfly-bee-fireflies), [Start on the shoes, tilt up, then widen](#omni-shoes-tilt-up), [Move the camera over the violinist's shoulder](#omni-violinist-over-shoulder), [Edit the monster: recolour it, then add a second one](#sora-monster-edits)
- <a id="tag-multilingual"></a>`multilingual` (4): [Bento handed over at a misty station, in Japanese](#kling-japanese-station-bento), [Joseon noblewoman and her maid](#kling-joseon-lady-and-maid), [Korean high-school rooftop at night](#kling-korean-rooftop), [Asking directions in Madrid, in halting Spanish](#kling-madrid-asking-directions)
- <a id="tag-music"></a>`music` (2): [Whip-pan from drummer to saxophonist and dancer](#omni-drummer-whip-pan), [Apartment lights switch on to the beat](#omni-lights-sync-to-music)
- <a id="tag-object-swap"></a>`object-swap` (3): [Ships to origami, astronaut to anemone, ships to stingrays](#omni-astronaut-three-swaps), [Butterfly to bee to fireflies, one change per turn](#omni-butterfly-bee-fireflies), [Edit the monster: recolour it, then add a second one](#sora-monster-edits)
- <a id="tag-orbit"></a>`orbit` (1): [Camera circles to her face, she looks up and smiles](#kling-orbit-to-smile)
- <a id="tag-period"></a>`period` (1): [Joseon noblewoman and her maid](#kling-joseon-lady-and-maid)
- <a id="tag-preview"></a>`preview` (1): [Make a small looping GIF preview for a README](#readme-preview-gif)
- <a id="tag-product"></a>`product` (1): [Keyboard made of candy](#veo-candy-keyboard)
- <a id="tag-product-ad"></a>`product-ad` (1): [Perfume ad by a Paris window](#kling-perfume-paris-ad)
- <a id="tag-qa"></a>`qa` (1): [Split a multi-shot clip into separate shots at the hard cuts](#split-shots)
- <a id="tag-reframe"></a>`reframe` (1): [Turn a 16:9 clip into a 9:16 short with a blurred background](#vertical-blur-fill)
- <a id="tag-scene-detection"></a>`scene-detection` (1): [Split a multi-shot clip into separate shots at the hard cuts](#split-shots)
- <a id="tag-sci-fi"></a>`sci-fi` (1): [Starship bridge, the fleet jumps to hyperspace](#h3-starship-hyperspace-jump)
- <a id="tag-score"></a>`score` (1): [Starship bridge, the fleet jumps to hyperspace](#h3-starship-hyperspace-jump)
- <a id="tag-sfx"></a>`sfx` (4): [Ramen in front, family dinner behind, one focus pull](#h3-ramen-focus-pull), [Starship bridge, the fleet jumps to hyperspace](#h3-starship-hyperspace-jump), [Keyboard made of candy](#veo-candy-keyboard), [Off-road rally through a river crossing](#veo-off-road-rally)
- <a id="tag-shot-reverse-shot"></a>`shot-reverse-shot` (1): [Villa terrace, a two-person summer dialogue](#kling-villa-terrace-dialogue)
- <a id="tag-spanish"></a>`spanish` (1): [Asking directions in Madrid, in halting Spanish](#kling-madrid-asking-directions)
- <a id="tag-sports"></a>`sports` (1): [Logo on a baseball bat stays sharp through the swing](#kling-baseball-bat-logo)
- <a id="tag-static-camera"></a>`static-camera` (1): [Ramen in front, family dinner behind, one focus pull](#h3-ramen-focus-pull)
- <a id="tag-stop-motion"></a>`stop-motion` (1): [Stop-motion camper and a bear with a comeback](#veo-camper-and-bear)
- <a id="tag-storyboard"></a>`storyboard` (2): [Hand it a storyboard, get the scene](#omni-storyboard-to-video), [Split a multi-shot clip into separate shots at the hard cuts](#split-shots)
- <a id="tag-structured-prompt"></a>`structured-prompt` (3): [Make the man in an existing clip speak, in a borrowed voice](#h3-pink-suit-lip-sync-edit), [Ramen in front, family dinner behind, one focus pull](#h3-ramen-focus-pull), [Starship bridge, the fleet jumps to hyperspace](#h3-starship-hyperspace-jump)
- <a id="tag-style-lock"></a>`style-lock` (1): [Quantum computing explained in risograph flat style](#omni-quantum-explainer)
- <a id="tag-style-transfer"></a>`style-transfer` (1): [One clip through crayon, pencil, glass and risograph](#omni-four-style-progression)
- <a id="tag-subtitles"></a>`subtitles` (1): [Transcribe dialogue and burn in Chinese and English subtitles](#bilingual-subtitles)
- <a id="tag-text-render"></a>`text-render` (3): [Logo on a baseball bat stays sharp through the swing](#kling-baseball-bat-logo), [Perfume ad by a Paris window](#kling-perfume-paris-ad), [Kinetic type, one word per beat](#omni-word-by-word-sizzle)
- <a id="tag-timed-cut"></a>`timed-cut` (1): [Starship bridge, the fleet jumps to hyperspace](#h3-starship-hyperspace-jump)
- <a id="tag-title-card"></a>`title-card` (1): [Cut a teaser from clips of different sizes, with title and crossfades](#teaser-montage)
- <a id="tag-tracking-shot"></a>`tracking-shot` (1): [One take follows a woman from elevator to desk](#kling-office-long-take)
- <a id="tag-vertical"></a>`vertical` (1): [Turn a 16:9 clip into a 9:16 short with a blurred background](#vertical-blur-fill)
- <a id="tag-vfx"></a>`vfx` (1): [Add cartoon motion lines to live skateboarding](#omni-skateboard-motion-fx)
- <a id="tag-voice-reference"></a>`voice-reference` (1): [Make the man in an existing clip speak, in a borrowed voice](#h3-pink-suit-lip-sync-edit)
- <a id="tag-voiceover"></a>`voiceover` (1): [Perfume ad by a Paris window](#kling-perfume-paris-ad)
- <a id="tag-whimsical"></a>`whimsical` (2): [A chubby purple monster comes out of the fridge](#sora-fridge-monster), [Keyboard made of candy](#veo-candy-keyboard)
- <a id="tag-whisper"></a>`whisper` (1): [Transcribe dialogue and burn in Chinese and English subtitles](#bilingual-subtitles)
- <a id="tag-world-building"></a>`world-building` (1): [Crystal flowers on a moon-dust plain](#veo-moon-dust-flowers)

<a id="contributing"></a>
## Contributing

1. Add one YAML file under `prompts/video/` (copy any entry as a template).
2. Link the original post or page where the prompt and its output were published, and credit the author.
3. Run `python scripts/build.py` to regenerate both READMEs, then open a pull request.
4. Entries without a visible output or a traceable source are closed. Promotional links are closed.

## Related lists by the same maintainers

- [awesome-prompts](https://github.com/ai-boost/awesome-prompts): prompts for LLMs and agents
- [awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering): building reliable agent harnesses

## License

Repository code and notes: GPL-3.0. Prompts and videos belong to their original publishers and are linked or quoted with credit.
