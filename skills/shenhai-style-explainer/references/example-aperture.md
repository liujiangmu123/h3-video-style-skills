# Worked Example — 90s Photography Explainer: 「光圈」(Aperture)

Demonstrates the full pipeline: topic mapping → beat table → complete H3 prompts.

> **关于本例中的具体颜色**：下文所有具体色（近黑画布、荧光黄强调色及提示词内的色值）都是对「光圈」这一题材跑 `style-dna.md` Part B 推导得出的**实例结果**——画布三问：光束是"暗处的光"→ 深底；选色三问 Q1：题材世界的标志色=光本身的暖黄 → 强调色取荧光黄。**做新题材时重新推导，禁止照抄本例的颜色。**
>
> **关于本例中的运动措辞**：本例早于心电图运动哲学（style-dna A6）定稿，提示词内偶见 "smooth ease-out" 等旧措辞。写新提示词时以 A6 为准：事件是短脉冲（0.5-0.8s，包络按动词选），事件之间画布**完全冻结**（1-3s 常态、4-10s 停留是常规），任一时刻至多一个元素在动，每章仅一次 hero 级爆发。本例的节拍结构与领域锚点做法仍然有效。
>
> **关于本例提示词里的 hex 色值**（`#141414`、`#FFE600`）：本例早于"风格块不写 hex"规则（`style-dna.md` B4、SKILL.md Quality Checklist）。现行做法是把颜色写成词语（"a warm near-black canvas one step above pure black" / "a fluorescent yellow accent, the beam's own light color"），新提示词一律按现行规则；本例保留原文只为展示节拍结构。
>
> ⚠️ **本范例为旧流程（非时间码法）示例**：文中的 `<d>` 对白与秒数写法、字幕条（subtitle bar）、`(S1)` 旁白、非 N/A 的配乐（`non_diegetic_music`）、`<Picture N>` 参考图占位，**均勿照抄到时间码法产线**。时间码法写法——旁白先由 TTS 录出（`h3_plan_durations`）、旁白不进 prompt、每个事件 `At MM:SS.mmm` 绝对时间码、长动作 `finishing by MM:SS.mmm`、补偿默认 +0.2 s（渐进描画类约 −0.5 s）、首事件 ≥0.300、段 ≥2 加 0.917 s 续接头、画面字段末尾加 "No speech, no dialogue, no human voice of any kind; no people or faces appear"、`non_diegetic_music: N/A`、字幕后期烧入——一律以 `beat-templates.md` 与 `h3-storyboard-writing` 技能 §9 为准。本例仅供参考题材映射、节拍结构与领域锚点做法。
>
> **2026-09-05 帧级重读后本例已知偏差（写新例时勿照抄）**：① 字数预算按 3.3 字/秒算偏少；原片 ≈5 字/秒，但我们的 MiniMax 配音按 目标秒数 × 3.5 预算——本例 86 秒应配约 300 字（原片口径约 430 字）。② Beat 2 五句配五个动作（开大→变亮→粒子→收小→标签脉冲），原片是每 1–2 句一个动作、三到五成句子不动——应删到 2–3 个动作。③ "光圈"术语在第 8 秒就命名，原片术语卡在 12–27 秒、现象演示之后——应先让光圈开合、亮暗、虚化都发生一遍，再出名字。④ 本例通过了 B-0 四门（原子=一束光；20 秒可演=开合亮暗；骨架可叠=伦勃朗画作上的光线；手边=手机人像模式），结尾"长按点赞=光圈收缩"正是 A9.3 的"原理落到观众手边"。

## 1. Topic Mapping

| Slot | Choice |
|------|--------|
| Atomic element | a beam of light passing through an iris of aperture blades |
| Attribute pair | large aperture (bright, shallow focus) vs small aperture (dark, deep focus) |
| Case ladder | Rembrandt chiaroscuro → classic 50mm f/1.8 lens → phone portrait-mode UI |
| Concept terms | Bokeh 散景; 景深 Depth of Field |
| Interaction plant | long-press like = aperture blades contracting like a shutter |
| Aphorism | 摄影，就是用光的取舍，决定画面的主角。 |
| Canvas / accent | 画布三问 → dark (light beams are "glow in the dark") ／ 选色三问 Q1 → fluorescent yellow (the beam's own light color — borrowed from the subject) |

## 2. Beat Table

| # | Type | Dur | Narration (Chinese) | Visual event chain | Mode |
|---|------|-----|---------------------|--------------------|------|
| 1 | B1 | 8s | 这是一束光。/ 这，是一束被约束的光。/ 约束它的开口，叫做光圈。 | yellow dot → beam → six blades iris in around it | T2VA |
| 2 | B2 | 12s | 光圈越大，进光越多。/ 画面就越明亮。/ 光圈越小，进光越少。/ 画面也随之暗淡。/ 但光圈改变的，不止亮度。 | iris dilates → canvas brightens → iris contracts → dims | I2VA (from beat 1 tail) |
| 3 | B3 | 12s | 大光圈下，焦点之外的世界开始融化。/ 小光圈下，一切又重新清晰。/ 这就是景深。 | three shapes at depths blur/sharpen as iris changes | T2VA |
| 4 | B5 | 8s | 这些朦胧的光斑，被称为散景。/ 它让主体从背景中浮现。 | concept card "Bokeh" | T2VA |
| 5 | B4 | 12s | 三百年前，伦勃朗就在画布上做了同样的事。/ 用一束光，把主角从黑暗中托出来。 | painting card + accent annotation line | Ref2VA |
| 6 | B3 | 12s | 今天，手机把这一切装进了一个按钮。/ 滑动，就是在改变光圈。/ 人像模式，就是被计算出的散景。 | phone UI simulation, slider, f-number changes | T2VA |
| 7 | B6 | 8s | 所以长按点赞时，图标也会像光圈一样收缩。/ 快去试试吧。 | like icon with iris-blade contract animation | T2VA |
| 8 | B7 | 6s | 摄影，就是用光的取舍，决定画面的主角。 | all elements fade, lone beam remains, iris closes to a dot | T2VA |
| 9 | B8 | 8s | 感谢大家看到这里，更多摄影内容，欢迎关注，不要忘记一键三连，我们下期再见。 | tri-icon outro | T2VA |

Total ≈ 86s. Narration budget check (old, wrong): beat 2 = 39 chars ≈ 12s × 3.3. Corrected 2026-09-28: the production budget is ≈ target seconds × 3.5 chars with our MiniMax voice (reference films ≈5 chars/s), so a 12s beat carries ≈40 chars — this table is close for production and short by ≈35% against the reference films; when reusing it, add sentences or shorten beats.

## 3. Complete Prompts

### Beat 1 — B1 Cold Open (T2VA, 8s)

```text
integrated_multimodal_description: [Shot 1] 2D-animated minimalist motion-graphics explainer. The entire frame is a flat near-black canvas (#141414); graphics are thin white lines, white type and floating rounded-rectangle cards with faintly glowing edges, plus a single fluorescent yellow (#FFE600) accent color; a dark-grey translucent rounded subtitle bar sits at the bottom center showing bold white Chinese text; the top-right corner stays clear. Everything happens in one continuous take with no cuts: elements morph, slide, draw themselves on and scale with smooth ease-out motion and a slight elastic overshoot, while the camera holds nearly static with only a very slow small-amplitude zoom. The canvas is empty except for a single small fluorescent yellow dot glowing at center. An unseen narrator with a calm, clean young-adult male voice (S1) says in an off-screen voiceover: <d>[Chinese] 这是一束光。</d> as the subtitle bar reads "这是一束光" and the dot stretches horizontally into a soft-edged yellow beam crossing the canvas. Then six flat dark-grey aperture blades slide in from the frame edges and iris smoothly inward around the beam, choking it to a narrow shaft, while (S1) continues: <d>[Chinese] 这，是一束被约束的光。</d> and the subtitle bar swaps to "这，是一束被约束的光". A thin white circular outline draws itself around the blade opening as (S1) says: <d>[Chinese] 约束它的开口，叫做光圈。</d> with the subtitle bar reading "约束它的开口，叫做光圈", and the word "光圈" in bold white sans-serif fades in above the iris with a yellow highlighter bar sweeping under it. The composition holds for a final beat, the camera drifting in with very small amplitude at slow speed.

overall_soundscape: Near-silent room tone throughout. Sparse light interface sounds accompany each animation event: a soft whoosh as the beam stretches, a subtle mechanical slide as the blades iris in, and a gentle tick when the label lands. No other ambient sound.

non_diegetic_music: A quiet minimal lo-fi electronic bed with soft muted synth chords and a light unobtrusive beat at a moderate-slow tempo, mixed far below the narration at a constant low level.
```

### Beat 2 — B2 Concept Contrast (I2VA, 12s, chained from beat 1)

First extract the final frame of beat 1's clip as Picture 1.

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 2D-animated minimalist motion-graphics explainer continuing the exact layout of <Picture 1>: the near-black canvas (#141414), the six-blade iris around a yellow light beam, the white circular outline, the "光圈" label with its yellow underline, and the bottom subtitle bar all remain in place. The blades iris smoothly OUTWARD, widening the opening, and the beam swells brighter and broader while the whole canvas lifts slightly in brightness, as an unseen narrator with a calm, clean young-adult male voice (S1) says in an off-screen voiceover: <d>[Chinese] 光圈越大，进光越多。</d> with the subtitle bar reading "光圈越大，进光越多". (S1) continues: <d>[Chinese] 画面就越明亮。</d> as tiny yellow light particles drift outward from the beam and the subtitle bar swaps accordingly. Then the blades iris tightly INWARD, the beam thins to a sliver, and the canvas dims back down, while (S1) says: <d>[Chinese] 光圈越小，进光越少。</d> then <d>[Chinese] 画面也随之暗淡。</d> with the subtitle bar matching each sentence. Finally the iris settles at a middle opening; the "光圈" label pulses once in scale as (S1) says: <d>[Chinese] 但光圈改变的，不止亮度。</d> and the subtitle bar reads "但光圈改变的，不止亮度". The camera pushes in with very small amplitude at slow speed and the layout holds on the final frame.

overall_soundscape: Near-silent room tone throughout. A subtle mechanical slide accompanies each iris movement, a soft airy swell as the canvas brightens, and a gentle tick when the label pulses. No other ambient sound.

non_diegetic_music: A quiet minimal lo-fi electronic bed with soft muted synth chords and a light unobtrusive beat at a moderate-slow tempo, mixed far below the narration at a constant low level.
```

### Beat 4 — B5 Concept Card (T2VA, 8s)

```text
integrated_multimodal_description: [Shot 1] 2D-animated minimalist motion-graphics explainer. The entire frame is a flat near-black canvas (#141414) with a single fluorescent yellow (#FFE600) accent color and a dark-grey translucent rounded subtitle bar at the bottom center showing bold white Chinese text; the top-right corner stays clear; one continuous take with no cuts and a nearly static camera. Several soft round out-of-focus light discs in white and pale yellow float gently in the dark background. Large white serif Chinese characters "散景" fade in at the center with a subtle blur-to-sharp reveal, and a fluorescent yellow color block slides in as an underline beneath them; a thin italic English subtitle "Bokeh" fades in below. An unseen narrator with a calm, clean young-adult male voice (S1) says in an off-screen voiceover: <d>[Chinese] 这些朦胧的光斑，被称为散景。</d> while the subtitle bar reads "这些朦胧的光斑，被称为散景". The floating light discs drift slowly behind the type as (S1) continues: <d>[Chinese] 它让主体从背景中浮现。</d> with the subtitle bar swapping to match. The card holds statically for the final second while the camera pushes in with very small amplitude at slow speed.

overall_soundscape: Near-silent room tone throughout. A soft airy shimmer accompanies the drifting light discs, a subtle pop as the title sharpens, and a gentle slide as the underline lands. No other ambient sound.

non_diegetic_music: A quiet minimal lo-fi electronic bed with soft muted synth chords and a light unobtrusive beat at a moderate-slow tempo, mixed far below the narration at a constant low level.
```

### Beat 5 — B4 Case Exhibit (Ref2VA, 12s, with a Rembrandt reference image)

```text
subject_definitions:
<Subject 1> is the classical oil painting in <Picture 1>, a Rembrandt-style chiaroscuro portrait scene with a strong single light source carving the main figure out of deep shadow.

summary:
[reference generation] The target video is a minimalist motion-graphics explainer beat in which <Subject 1> appears matted inside a floating rounded-rectangle card on a near-black canvas while an off-screen narrator links painterly chiaroscuro to photographic aperture.

retention_analysis:
<Subject 1> (appears in [Shot 1]): fully_preserved - the painting's composition, warm highlight and deep shadow structure are retained inside the card.

detailed_description:
The target video is a 2D-animated minimalist motion-graphics explainer on a flat near-black canvas (#141414) with a single fluorescent yellow (#FFE600) accent color and a bottom-center dark-grey translucent rounded subtitle bar with bold white Chinese text; the top-right corner stays clear; one continuous take with no cuts and a nearly static camera.
[Shot 1] A rounded-rectangle card with a faintly glowing edge slides up into the center with a soft elastic settle, containing <Subject 1> with a thin margin, tilted about 4 degrees in gentle 3D perspective. An unseen narrator with a calm, clean young-adult male voice (S1) says in an off-screen voiceover: <d>[Chinese] 三百年前，伦勃朗就在画布上做了同样的事。</d> while the subtitle bar reads "三百年前，伦勃朗就在画布上做了同样的事". A thin fluorescent yellow annotation line draws itself from the card's edge to the painting's brightest lit area, ending in a small circle, as (S1) continues: <d>[Chinese] 用一束光，把主角从黑暗中托出来。</d> with the subtitle bar matching. The card recedes slightly and holds while the camera pulls out with very small amplitude at slow speed.

overall_soundscape: Near-silent room tone throughout. A soft whoosh as the card slides up, a faint paper settle, and a gentle tick as the annotation line lands. No other ambient sound.

non_diegetic_music: A quiet minimal lo-fi electronic bed with soft muted synth chords and a light unobtrusive beat at a moderate-slow tempo, mixed far below the narration at a constant low level.
```

### Beat 9 — B8 Fixed Outro (T2VA, 8s)

```text
integrated_multimodal_description: [Shot 1] 2D-animated minimalist motion-graphics explainer. The entire frame is a flat near-black canvas (#141414) with a single fluorescent yellow (#FFE600) accent color and a dark-grey translucent rounded subtitle bar at the bottom center showing bold white Chinese text; the top-right corner stays clear; one continuous take with no cuts and a nearly static camera. Three flat rounded icons — a thumbs-up, a coin and a five-pointed star, all in soft white with fluorescent yellow rim accents — slide up into a horizontal row at center, each landing with a small elastic bounce, staggered 0.3 seconds apart. An unseen narrator with a calm, clean young-adult male voice (S1) says in an off-screen voiceover: <d>[Chinese] 感谢大家看到这里，更多摄影内容，欢迎关注，不要忘记一键三连，我们下期再见。</d> while the subtitle bar shows the line in two successive parts, "感谢大家看到这里，更多摄影内容，欢迎关注" then "不要忘记一键三连，我们下期再见". The three icons pulse once in scale together exactly when the words "一键三连" are spoken, then hold as the frame gently settles.

overall_soundscape: Near-silent room tone throughout. Three soft pops as the icons land in sequence and one subtle unified pop on the group pulse. No other ambient sound.

non_diegetic_music: A quiet minimal lo-fi electronic bed with soft muted synth chords and a light unobtrusive beat at a moderate-slow tempo, mixed far below the narration, ending with a gentle fade in the final second.
```

## 4. Assembly Notes

1. Generate beats in order; after each generation, extract the last frame for any I2VA-chained successor.
2. Concat all clips. If music seams are audible at joins, mute the generated music layers and lay one continuous lo-fi bed over the full cut.
3. Check: subtitle bar position/size identical across beats; accent yellow consistent; no accidental cuts inside any beat; narration gaps at joins 0.2-0.5s.
4. Optional post: add the channel watermark top-right; add platform end-screen.
