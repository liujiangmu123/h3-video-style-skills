# Shenhai Style DNA — Two-Column Vocabulary (Constants / Derivation Rules)

Derived from frame-level analysis of 13 originals (45 min, ~2700 sampled frames, cut detection, audio onset/loudness analysis, full transcripts), plus four dedicated probes run on the originals: color_probe (frame-level color/light fields), color_timeline (per-second color share across 11 films), motion_probe (frame-difference energy pulses on 4 pure-animation films), composition_probe (24 keyframes quantified). Probe data lives in `设计师深海视频分析/风格分析工作区/深度研究_2026-08-25/`.

**2026-09-05 frame-level re-read** (`深度研究_2026-09-05/frame_rhythm_report.md`, `canvas_report.md`; summary in `设计师深海_白底极简科普/设计师深海视频分析/逐帧核心提炼_2026-09-05.md`): every frame of all 13 films scored with the subtitle band cropped out (the earlier probes counted subtitle swaps as motion), narration pauses measured from audio RMS, contact sheets viewed shot by shot. Numbers below marked **[09-05]** supersede older values; the biggest corrections are narration speed (≈5 chars/s, not 3.3), motion share (12-29%, not 33-68%) and the "one sentence = one event" law (one event per 1-2 sentences; a third to a half of sentences have no motion at all).

**Structure of this file**: Part A holds the CONSTANTS — philosophy rules and quantified constraints that never change across topics. Part B holds the DERIVATION RULES — formulas for re-deriving every variable (canvas, register, accent color, motion texture, anchors) per topic. **No fixed color values live in the rules**: colors observed in the originals were the author's per-episode derivation RESULTS, not the style. Copy the reasoning, never the swatch.

---

# 主配方 THE FORMULA（全文件的纲；哲学＝这条可复述的主线）

> **领域锚点容器 1 秒内落位 → 领域实物演示一个核心知识点 → 参数/记号驱动连续变形 → 一句一事件；画布、画面档位与强调色按领域特性分配，符合观看者心理。**

Part A 各节是这条配方各环节的**执行标准**（量化验收值）；Part B 是"按领域分配"的**推导公式**。任何一节都不得凌驾于配方之上——细则为配方服务，配方指导一切新领域开工。

---

# PART A — 常量栏 Constants (execution standards for the formula: rules + constraint values)

## A0. Convention Ledger — 通用法则取舍表 (readings on the industry rulers; the rulers themselves live in the `style-foundations` skill)

Style = a specific set of readings and refusals on universal rulers. What this author REFUSES is his strongest signature. This table records what the author *did* across 13 films; which of these readings are the style's essence and which are habits an episode may depart from with a reason is decided in B-0's three-tier table — read A0 as evidence, B-0 as policy:

| Industry convention (ruler) | Stance | This style's form |
| --- | --- | --- |
| Staging (Disney #3) | Radicalized | One Event law: at most one element moves at any moment (A6) |
| Secondary action (Disney #8) | **Refused** | Total Freeze compensates: zero pixels move between events; stillness itself is the weapon (A6) |
| Slow in & slow out (Disney #6) | Adapted per verb | No single easing signature **[09-05]**: fast-in/slow-out, symmetric and slow-in/fast-stop each ≈1/3 of glides; the verb decides (draw-on accelerates and stops dead, slide-in fires and settles) (A6) |
| Follow-through (Disney #5) | Absorbed | The only residual motion is the landing overshoot; no other overlapping action |
| Squash & stretch (Disney #1) | N/A → overshoot only | Elements are rigid vector pieces; deformation lives only inside morph events |
| Anticipation (Disney #2) | Refused | No wind-up; the preceding dead silence stores the energy |
| Timing (Disney #9) | Adopted & quantified | Three force tiers, 10-22× dynamic range, one hero event per chapter (A6) |
| Rule of thirds | Refused | Axis gravity: content centroid locks to x 0.47-0.52 (A3) |
| 60-30-10 color budget | Adapted | Radicalized to 95-4-1 with tiered measured budgets (A2) |
| "Never let the frame stop" | **Refused** | ECG rhythm **[09-05]**: canvas still 71-88% of runtime; still gaps median 0.9-2.7s, p90 3.6-8s, every film holds 6-30s at least once — while the narration never pauses >1s (A6) |
| Canvas three states | Lit place | Canvas standard (A1) |

Inventions (devices with no industry counterpart — the author's own): the ECG rhythm model with its quantified bands, delayed first color as a narrative event owed to the audience, domain anchor containers, the 创意五问 brief.

## A1. 画布执行标准 Canvas Standard（配方"画布按领域分配"环节的质感验收；the canvas is a place, not a background）

1. **场所律 Place**: the canvas is the physical place the topic lives in, not a layout surface. Silent-frame test: an empty frame must still answer "where is this". Originals built, per episode: a deep-night phone screen, a xuan-paper wall of historical text, a print mounted inside a dark frame, a night sky, a black-gold luxury surface, a design tool's own mid-grey canvas. Derive the place per topic with B1 (画布三问); "paper" (light) and "blackboard/darkroom" (dark) are the two tonal families, with the tool-canvas mid-grey as a documented third base for UI/software topics.
2. **有光律 Light**: the canvas must carry light — dead-flat fills are forbidden. Dark canvases: a soft central light pool falling off into darker corners (measured vignette falloff 45-89%), and the black is WARM (the darkest tones lean warm, never pure black). Light canvases: a paper-grey base one perceptible step below pure white with a faint warm lean; whites are layered — card surfaces and highlights sit a step brighter than the base (2-3 distinct whites per frame). Every canvas carries a barely visible micro-noise grain. "White not pure, black not black" is the essence: light leaves time and place on every tone.
3. **层次律 Greys**: grey levels are space. Rich frames run 10-31 grey levels (base / texture / plane / line / shadow); 2-3 greys reads as a chart, 10+ reads as a world. Text-walls, floating cards and ghost outlines are the middle layers between canvas and subject.
4. **舞台律 Stage**: the light pool is stage lighting — place the subject where the light is; the vignette is a spotlight, not a filter. **Switching canvas base mid-video is a chapter accent**: 6 of 11 originals switch light↔dark exactly at chapter turns (light canvas teaches concepts; dark canvas hosts glowing demos and card streams). Switch only at a concept-card chapter turn or a case-block turn (the tilt episode puts its own construction on light and each brand logo back on that brand's dark ground), never inside a demo.
5. **底色频率 Base frequency [09-05]**: frame-weighted across the 13 originals the canvas is dark 50% / light 28% (the rest is quoted footage or mid-grey cards); excluding the two footage-heavy films, dark 52% / light 36%. Dark is at least as "default" as light — the skill's nickname "白底" is a misnomer. Derive per topic with B1; never assume light.

Constraints: never pure white, never pure black (one perceptible step off the extreme); never texture-less dead-flat color. Watermark zone: top-right corner stays clear. Aspect: 16:9 default; one original used 4:3 inside a black pillarbox for a "classic art" episode — allowed as a deliberate framing card.

## A2. 色彩执行标准 Color Standard（配方"强调色按领域分配"环节的预算验收；color is an event, not decoration）

- **Monochrome discipline**: ink-black (near-black, warm, not pure), layered whites, and 2-3 greys are the absolute body of every frame. Color is scarce on purpose — scarcity is what makes the accent legible. Working ratio ≈ **95-4-1**: ~95% achromatic canvas, ~4% grey structure, ~1% accent.
- *Register note (B6)*: the numbers above are the R1 reading. At R3–R4 the body may be one low-saturation tonal family that leans the canvas temperature instead of strict greys; keep it clearly below the accent (HSV saturation under ≈0.35, which is also where `h3_align`'s color-area reading starts counting) so the accent stays the only color the eye and the meter see.
- **One accent color per video, start to finish** — or one cool-vs-warm pair when the episode is a two-sided comparison (B2-Q2: blue bull vs red bull, red wrong vs green right). Never a third working color, never mid-video swaps. Frame-level check **[09-05]**: 1-2 hue buckets per frame at the median, never more than 4; 15-74% of frames carry no color at all. The accent's job is attention direction: highlight bars under key words, the top face of 3D shapes, ground-line strips, key element fills, annotation lines. If everything is colored, nothing is emphasized.
- **Color budget tiers** (measured colored-pixel share): restrained 3-7% (color only on emphasis seconds), single-accent standard 8-17%, content-color 23-36% ONLY when quoted assets (paintings, memes, footage) bring their own color. Baseline discipline ≤10%.
- **Delayed entrance**: decorative accents open in pure monochrome and hold 13-42 seconds, landing the first color exactly on the first knowledge point — the first color is a narrative event the audience has been "owed". Content-type color (quoted assets) may appear from second 1.
- **Full-saturation law**: when the accent appears it is fully saturated (measured p90 saturation 0.9-1.0) — either zero color or full color. Restraint lives in area and timing, never in purity; no muted-morandi hedging.
- **One lamp**: every tone from the darkest black to the brightest white leans the same temperature direction, as if lit by a single lamp. Check: dark / mid / highlight samples must share the same warm-or-cool bias.
- **Greyscale skeleton**: a fully de-saturated frame must still work — hierarchy lives in value structure; hue only names things.
- **Hue signature** (channel-level taste constant observed across all originals): the palette lives in three hue regions — warm orange-yellow, cool blue-violet, magenta-rose; the green band is systematically absent except as the semantic check-mark. A 选色三问-Q1 borrowed color or a strong material reason (terminal green for a hacking episode) may override it.
- **Accent quality constraints** (values, not hues): high saturation; must contrast strongly against both the canvas and black/white/grey; reads as "marker pen on paper" (light canvas) or "glow in the dark" (dark canvas).
- **Semantic constants** (universal semantics, not aesthetic choices): red = wrong/legacy/warning, green = correct; a blue-vs-red (cool-vs-warm) pair = the two sides of any comparison.
- **Sanctioned polychrome exception**: capsule pointillism — colorful rounded dots/capsules assembling into an image on the dark canvas (city lights, Eiffel tower). This is the one device allowed to be multicolor, because the dots depict light sources themselves.

## A3. 构图执行标准 Composition Standard（"实物演示知识点"的画面布局验收；quantified on 24 keyframes）

1. **中轴引力 Axis gravity**: the content centroid locks to the vertical axis — x within 0.47-0.52 in 22/24 measured frames, left/right margins differing ≤0.04 of frame width. Center is home; off-axis placement must be a deliberate statement.
2. **墨量预算 Ink budget**: single-focus teaching frames put content at only **2-15% of frame area** (openings go as low as ~2%), leaving 85-98% empty canvas; case-exhibit frames rise to 30-65%; full-bleed is reserved for deliberate texture beats (card streams, text walls). Emptiness is what makes the subject loud. *Register note (B6):* this is the R1 reading. At R3–R4 the place fills the frame and emptiness moves from blank canvas to value — the focal plane holds the only strong contrast, everything else sits in close grey steps; the production reading `target_ink` is a floor, not a ceiling.
3. **对称默认，不对称是事件 Symmetry default**: horizontal mirror overlap is high by default (IoU 0.7-0.97). Break symmetry ONLY when the asymmetry itself teaches the point — the "tilt" episode opened with a deliberately off-axis line, the single IoU=0 frame in the whole library.
4. **重心微偏下 Slightly-low centroid**: content centroid y sits at 0.55-0.62 — a touch below center with air kept at the top, like gallery-hung art; grounded scenes may sink lower.

## A4. Graphic Language (pick per beat, never mix more than 2 in one beat)

1. **Flat vector line art** — uniform-weight black strokes, no gradient, no shadow; strokes can "draw themselves on"
2. **Solid silhouette / positive-negative shapes** — bold black (or white-on-dark) animal/object silhouettes with clever negative space
3. **Geometric construction** — thin white frame lines on dark canvas + accent-colored auxiliary lines (diagonals, arcs) + serif numerals like "1", "√2"; math-blackboard feel
4. **Silhouette cast** — a tiny line person for scale, or (R3–R4, B6) a fixed cast of 1–3 featureless flat silhouettes whose outline of nose and chin shows which way they face; poses change by snapping, never by walking; no eyes, no mouth, no fingers. Domain material wherever the field's knowledge lives in bodies, gaze or position (film, sport, psychology, fashion…)
5. **Rounded-rectangle cards** — all quoted assets (paintings, photos, memes, UI screenshots) are matted inside floating rounded cards with slight 3D tilt; on dark canvas card edges glow faintly
6. **Text-wall texture** — large light-grey characters tiling the background as historical context, main subject in a circular crop in front
7. **Capsule pointillism** — see A2 polychrome exception
8. **Design-tool simulation** — selection boxes, px spec labels, frosted-glass nav bars, as if screen-recording a design app; selection-box tint = the accent color (or the simulated tool's own signature UI tint, which then usually IS the episode accent — see B2)
9. **Domain containers & anchors** — mandatory when the topic is NOT graphic design itself (Shenhai's abstraction reads as content only because his field is graphics). Wrap abstract demos inside domain-native frames so every beat visually names the field: photography → viewfinder corner brackets with a small exposure readout ("1/125 · f/2.8 · ISO 100"), white-bordered photo prints, flat vector camera/lens; music → staff lines and note heads; physics → blackboard axes, formulas, vector arrows; economics → axis charts, candlesticks, coins; cooking → cutting board, pan outlines. Anchors use the episode's register language (B6) and never break the tonal body + single accent rule. A container is not a demonstration: the knowledge is shown on what lives inside it.
10. **Register languages R2–R4** — cutaway diagram, tonal stage with a silhouette cast, cut-paper diorama (B6; blocks in B4). One register per episode, used throughout; anything from items 1–9 that appears inside it is drawn in that register.

## A5. Typography (three tiers)

1. **Subtitle band** (every second of every video): bottom-center, one sentence of 5-15 characters, swaps with each narration sentence (the originals draw it as a dark-grey translucent rounded bar with bold white sans-serif Chinese). In production the pipeline delivers **without subtitles** (`subtitles=none`); the user adds the band in post via speech-to-text. It is never described in the H3 prompt. The prompt only reserves the space: "the lower fifth of the frame stays completely empty at all times".
2. **Concept cards** (chapter turns, 5-10s):
   - Light-canvas version: huge black bold sans-serif (Helvetica-like) headline + **accent-color highlighter bar sweeping under the text** + small Chinese annotation line
   - Dark-canvas version: large white SERIF (Songti/Ming) Chinese headline + accent color block underline on the key figure + italic thin English subtitle below
3. **Accent lettering** (sparingly): sticker-style bold white characters with extra-thick black outline; calligraphy art-characters for rotation/flip demos; outlined hollow display type over footage.

## A6. 「一句一事件」执行标准 — 心电图节奏模型（配方最后一环的节奏验收；pulse — dead silence — pulse）

The originals' rhythm is an ECG, not a conveyor belt: at frame level (subtitle band excluded) motion occupies only **12-29% of runtime** in the animation-led films **[09-05]** (the older 33-68% figure came from 1-second granularity, where any second containing motion counted as moving); everything else is true stillness. Build → Breathe → Resolve — stillness is the strongest weapon: no true stillness, no true burst.

- **Motion verbs** (copy these): zero-cut morph flow — element A transforms into element B ("the line rotates and thickens into a rectangle", "strokes reassemble into the flipped character", "the horizontal lines break into dashes and become sea sparkle"); enter = slide in / fade in / scale up; draw-on = line art draws itself stroke by stroke; exit = shrink and fade, or pushed off-canvas by the next element; emphasis = scale pulse, color flash to accent, highlighter bar sweep, red cross / green check stamping in.
- **事件密度 Event density [09-05]**: 14-33 motion events per minute (median ≈20) — **one event every 2-4 seconds**, not one per second. Four measured event tiers by duration: snap <0.3s (26-50% of events), glide 0.3-1.0s (33-69%), sustain >1s (2-14%), single-frame pop (0-8%; up to 17% in the UI-spec episode where labels pop in). Glides: median 0.47-0.77s, p90 0.75-1.5s.
- **脉冲律 Pulse**: a single motion event is short and crisp — glide median **0.5-0.8s**, p90 ≤1.5s. The event is a short pulse; the canvas holds still before and after it. (The old "every event 2-3s, fill the duration" reading is wrong and produces the conveyor-belt feel.)
- **「一句一事件」的真实含义 [09-05]**: *at most* one event per sentence — NOT one event for every sentence. Measured 0.5-1.1 events per narration sentence (median 0-1); **38-65% of sentences have no motion at all** (small label pops may be under-counted, so plan on "at least a third of sentences stay frozen"). Event onsets land 24-52% at a sentence's first syllable (±0.3s), 35-65% mid-sentence on the key noun, 6-17% inside a breath pause. Picture and voice are effectively synchronous (median offset −0.01 to −0.22s, picture a hair early). Practical rule: **one event per 1-2 sentences, placed on the sentence onset or the key noun; let whole sentences pass with nothing moving.**
- **死寂律 Total Freeze**: between events the canvas truly freezes — **zero pixels moving**, no idle loops, no ambient drift, no secondary action. Measured still gaps **[09-05]**: median 0.9-2.7s, p90 3.6-8s; every film has 7-26 holds ≥3s and one longest hold of 6-31s (the one-stroke episode holds 30.8s on a finished drawing while the narration keeps going). Long holds are routine, not chapter-only. Never fear stillness; fear filling it. *Register note (B6):* the originals are R1, where everything on screen carries information. At R3–R4 everything that carries information still freezes; one constant, information-free life layer is the only thing allowed to stay alive (待测).
- **声画反相 Voice-picture inversion [09-05]**: the narration never rests (pauses median 0.35-0.5s, p90 <0.9s, ≥1s at most 1-2 times per film) while the picture rests 71-88% of the time. The ear is led continuously; the eye is allowed to rest. This inversion — not the stillness alone — is why a 2-4 minute film does not tire. Never write a script that pauses the voice to "let the picture breathe": the picture breathes under a talking voice.
- **单事件律 One Event**: at any moment at most ONE motion event; everything else is frozen. Disney-style secondary action is deliberately banned — the goal is eye control, not visual richness: 100% of attention lands on the one changing element. Grouped entries are a chain of single events staggered 0.2-0.4s apart (not parallel motion); parented elements (a grid carrying its labels/annotations along) count as one event. *Production:* H3 merges two small moves ≲1.2 s apart into one, so a grouped entry is written as **one** timecoded event with the order in the clause ("three cards snap in one after another, the last a hair late"); unrelated moves go to different sentences ≥1.2 s apart (SKILL.md).
- **三档力度 Force tiers**: micro (hairline annotation, feather-level energy) / normal / hero (full-canvas burst). Measured peak dynamic range between gentlest and strongest event: **10-22×**. Exactly **one hero event per chapter**; if everything is loud, nothing is loud — the slowest element must read 3×+ slower than the fastest or nothing has weight.
- **包络随动词 Envelope follows the verb [09-05]**: measured glide envelopes split roughly evenly — fast-attack/long-settle ≈1/3, symmetric ≈1/3, slow-in/dead-stop ≈1/3 — so there is no single easing signature. Slide/scale entries fire fast and settle with a slight elastic overshoot (attack 0.1-0.5s, release 1.4-1.6×); draw-on strokes accelerate and stop dead the instant the line completes; morphs are near-symmetric. Choose the envelope from the verb (B5); applying one easing to everything — whether uniform ease-out or uniform overshoot — is the violation. *Production:* these envelopes describe the originals. The timecode line's default `motion_rule` writes every event as a single crisp change completed within a quarter second (best measured alignment, `compensation_s` +0.2, 2026-09-27); named envelopes are written only in a declared gradual style (rewrite `motion_rule`, `compensation_s` ≈ −0.5, re-measure with `h3_align`).
- **长高潮变形链 Climax morph**: at most once per video, a 10-30s continuous transformation chain serves as the visual climax (originals ran 21s and 33s morphs) — the sanctioned exception to short pulses; still one event, still zero cuts.
- **物性运动 Material motion**: motion texture obeys the topic's material — a stone topic moves heavy and blunt, a light/electric topic moves fast and sharp, a paper topic snaps and folds crisply. Derive verbs and easing weights per topic via B5.
- **Pseudo-camera (originals only)**: the originals let the whole canvas slowly zoom or pan with small amplitude (breathing feel), pushing in slightly on key moments and pulling out at section turns; no real cuts. **Production locks the camera** (default `motion_rule`: no zoom, no pan, no camera drift) and never writes this breathing into the timecode line — `h3_align`'s frame diff reads camera motion as whole-frame motion and loses the event onsets.

## A7. Audio Spec

- **Narrator**: one young-adult Chinese male voice, calm, clean, friendly-neutral, brisk and even — **[09-05] ≈5 characters/sec over the whole runtime (4.4-5.6 across 13 films), 6-7 characters/sec while actually voicing (median 6.3)**; the older "3.3 chars/sec" figure is wrong by half and produces sluggish, half-empty narration. Clear stress on key words. Breath pauses median 0.35-0.5s, p90 <0.9s; a pause ≥1s occurs at most once or twice per film, only at a chapter turn. Voiced share 74-88% of runtime. First sentence lands at 0.14-0.30s (12 of 13 films) — no music intro, no title, no greeting; fixed outro line at end. **Recorded externally by TTS before any picture exists** (`h3_plan_durations`); its sentence cues (`timing.json`) become the prompt timecodes. It is never written into the prompt — no `<d>`, no `(S1)`, no "narrator"/"voiceover"; the prompt instead ends the picture field with "No speech, no dialogue, no human voice of any kind; no people or faces appear; no on-screen text other than the labels described."
- **Soundscape**: near-silent room tone; sparse light UI sounds tied to animation events only — soft whoosh (slide in), subtle pop (element appears), gentle tick/click (annotation lands), faint paper slide (card flip). Never continuous. Material-flavored event sounds (a stone thud, a paper snap) are allowed when B5 motion derivation calls for them, still sparse and event-tied. In the prompt each sound sits inline with its action ("… pops in with a gentle tick") and is listed again by timecode in `overall_soundscape`, ending "Quiet room tone underneath; no voices." At assembly H3's sound track is peak-normalized and ducked under the narration.
- **Music**: quiet minimal lo-fi electronic bed — soft muted synth chords with a light unobtrusive beat at moderate-slow tempo, mixed far below the narration, no melodic hook, constant level. RMS target ≈ -22 dB overall. **Never generated per beat, and the assembler lays no BGM**: every prompt's `non_diegetic_music` is `N/A`; any bed is added by the user in post.

## A8. Narration Writing Rules (Chinese)

- Sentence length 5-15 characters (measured whisper segments 9-12 chars, culture-history episode 16.6); reference films carry ≈ duration_seconds × 5 **[09-05]** (a 150s original ≈750 characters). **Production budget = target seconds × 3.5**: our MiniMax voice (speed 0.96, gapSentence 0.24, gapSegment 0.9, grid snapping) speaks ≈4.4 chars/s inside a sentence and ≈3-3.7 over the runtime, so ×5 renders ≈30% long (150 s ≈ 550 characters). The recording always decides the final length.
- Cold open formula: `这是X` / `这，是一个X` — paired, contrastive, no greeting; the first sentence must land within 0.3s of frame one. Six of 13 films open exactly this way (这是一条线 / 这是直的线 / 这，是一个点 / 这，是二维平面中的方块 / 这，是一张空白画布).
- Attribute pairs: `X会让画面…` / `而Y则会…`; connectives 而/则/就/如果…就.
- Case intro: `比如…` `例如…, 例如苹果、推特等` `设计大师保罗·兰德…`.
- Plant humor sparingly: one meme-tier aside per video max (e.g. `认识这个品牌的同学请扣1`).
- Interaction plant pattern: tie the platform button to the lesson (`所以长按点赞时，图标也会不停地左右倾斜，快去试试吧`).
- Aphorism pattern: `X，就是…最…的…` one abstract closing truth.
- Fixed outro (verbatim): `感谢大家看到这里，更多内容，欢迎关注，不要忘记一键三连，我们下期再见` (adapt channel name).
- **A8.9 声音的感觉 — the voice, beyond the numbers** (the reading of B-0.7 "do not perform" at sentence level): the narrator states, he does not ask, greet, tease or exclaim — the long version's first sentence and every chapter opener are statements; a question mark appears at most once per film and never in the first two sentences. No performance vocabulary: no 大家好 / 今天我们来聊 / 你知道吗 / 其实 / 那么 / 没错 / 划重点, no 太…了 praise adjectives, no exclamation marks. Sentences are short, paired and end on the noun or the verb that the picture is about to move (the picture answers the sentence's last word). Authority comes from the evidence on screen, so the voice never insists — "这是" and "而" carry the argument, not "一定" or "其实". Warmth is allowed exactly twice: the one meme-tier aside, and the interaction plant. Everything else is a calm teacher who assumes the viewer is intelligent.

## A9. 结构执行标准 Structure Standard [09-05]（配方"实物演示知识点"的时间顺序验收）

1. **演示先于命名 Show before naming**: the phenomenon is built on screen first; the term card arrives only after the viewer has already seen it work — measured 12s (silver ratio), 20s (Ambigram), 27s (相似·连续, whose title is itself drawn out of the lines it names); the UI episode builds silently for 20s and only then asks its question. A concept card in the first 10 seconds is a style violation.
2. **三层弧线 Three-tier arc**: abstract principle (construction lines, geometry) → real-world evidence (actual brand logos, paintings, photographs, shown with the principle's skeleton drawn over them — dashed guide lines on F1/7UP/BOAC, the 28° annotation on the NeXT cube) → **the viewer's own hand** (the platform's like button tilting, a "点赞" ambigram, color bars spelling PLEASE DIAN ZAN). Authority comes from the evidence, not from the narrator's tone.
3. **互动即最后一例 The plant is the last example**: the like/subscribe beat is not an appended CTA; it is the final proof that the principle is everywhere, including under the viewer's thumb. It may sit at 60% of runtime (the line-vs-plane episode) or at the very end.
4. **一集一母题 One motif per episode**: each film has exactly one graphic device that carries the whole argument — skeleton lines over logos / strokes drawing themselves / line-vs-plane silhouettes / the screen flipping / cyan px annotations. Cases are evidence for the motif, never decoration beside it.
5. **唯一破规 One deliberate break**: at most one moment per film breaks the monochrome discipline for effect (the Y2K collage burst in the tilt episode, the SMPTE color bars in the line-vs-plane episode) — never two.
6. **转场签名 Transition signature**: page-corner peel / diagonal triangle wipe between case blocks (seen in four films); black chapter cards (numbered 01-10, "与此同时，另外一边…", term cards) for chapter turns. Zero hard cuts otherwise in animation-led films (0-5 per film; the listicle's 13 are all chapter numbers).
7. **商单结构 Sponsored structure**: 6 of 13 films are sponsored and all use the same shape — the first half is a pure principle demonstration indistinguishable in numbers from the non-sponsored films; the product enters in the second half as the principle's newest instance. The principle half is never shortened for the sponsor.

---

# PART B — 生成规则栏 Derivation Rules (re-derive per topic; never copy sample values)

## B-0. 哲学与选题四门 Philosophy & the Four Gates [09-05]（跑创意五问之前先过这里）

**The philosophy, as read from the frames (not from the formula line):**

1. **Teach one principle, and perform it with the principle's own material.** The episode about lines draws its seascape and its title out of lines; the episode about light builds the Eiffel Tower from light dots; the ambigram episode flips the screen itself; the tilt episode ends by tilting the like button. Form-is-content is the single source of the "wow"; everything else is discipline.
2. **Let them see it before you name it.** Terms are names for phenomena the viewer has already watched happen (A9.1).
3. **Grow the world from one atom.** "这是一条线 / 这是一个点 / 这是一张空白画布" is not a hook — it is the atom the whole film is built from by arranging, tilting, thickening, flipping it.
4. **Prove it with the real world, skeleton drawn on.** Real logos, real paintings, real photos, with the principle's construction lines overlaid (A9.2).
5. **Restraint is attention design, not taste.** Picture still 3/4 of the time, one moving thing, one accent, no cuts — so the one moving thing receives 100% of attention; voice continuous so the ear is never released (A6 声画反相).
6. **Bring the principle back to the viewer's hand** (A9.3).
7. **Do not perform.** No opening question, no music intro, no face, no "你知道吗"; a statement at 0.3s. A teacher's confidence, not a creator's anxiety.

One line: **用一个原理自己的材料，从一个原子开始，演到看懂了再给名字，用真东西作证，最后落到观众手边——全程只动一件东西，旁白不停、画面常停。**

**The Four Gates — a topic fits this style only if all four pass** (run before 创意五问; the alphabet test in the five-step transplant below checks whether the field has drawable material, these check the philosophy):

| Gate | Question | Pass example | Fail example |
| --- | --- | --- | --- |
| 1 原子 Atom | Is there a drawable smallest unit? | light → one beam; music → one note; economics → one coin; geography → one contour line | "workplace communication skills" — no atom |
| 2 可演 Demonstrable | Can the principle be shown in 20s with no words? | fast/slow shutter → the same ball frozen vs smeared; compound interest → a circle growing a ring each tick | a principle that can only be stated |
| 3 骨架可叠 Skeleton-on-evidence | Is there a real object the principle's lines can be drawn over? | a famous photo with thirds/exposure readout; a building photo with force lines; a hit song's waveform with beat grid | evidence that must be filmed to be believed |
| 4 手边 In the viewer's hand | Does the viewer own an instance? | phone camera portrait mode; music player progress bar; payment screen; own floor plan | nothing closer than a museum |

Photography, music theory, hanzi/typography, economics basics and architecture pass all four. A topic passing 1-3 but not 4 can still be an episode but loses the A9.3 ending; a topic failing 1 or 2 is not a Shenhai topic regardless of alphabet.

**Three tiers of constraint — essence, author defaults, free** (this is how 13 visibly different films still read as one author, and how a new episode can be more imaginative than any of the 13 without stopping being 深海). Part A records what the author *did*; not everything he did is what makes the style *his*. Sort every Part A value into one of three tiers before deciding what an episode may change:

| Tier | What it is | Rule | Contents |
| --- | --- | --- | --- |
| **1 · Essence 本质** | The handful of things a viewer recognizes the channel by; break one and the film is a different channel | **Never varies.** Not negotiable for any idea, any tier, any client | **Attention design**: at most one element changes at any moment; between events nothing that carries information moves (zero pixels on it — stillness is the weapon) and the picture is still most of the time while the voice never rests (A6 声画反相); one hero per chapter. At R1–R2 the whole canvas stops; at R3–R4 one constant, information-free life layer may stay alive (B6, 待测, default none). **One canvas, zero cuts**: continuity by morph, not by edit. **Color is an event**: a monochrome body (at R3–R4 one low-saturation tonal family, B6), one accent (or one comparison pair) at full saturation, arriving late on the first knowledge point, at most one break per film (A2, A9.5). **A made world on a lit canvas, sized to the knowledge**: everything is designed and drawn or cut — flat vector, silhouette, construction line, cutaway, cut paper — in one register per episode chosen by B6 (R1 glyph → R4 tactile); no live-action or photoreal look, no realistic person, no facial features, no fingers; featureless silhouette casts are domain material wherever the knowledge lives in bodies, gaze or position (A1, A4, B4, B6). **Teaching order**: show before name, grow from one atom, real evidence with the skeleton drawn on, back to the viewer's hand (A9, B-0). **Voice**: a calm teacher who states; brisk (≈5 chars/s), pauses <1s, first sentence at 0.3s, subtitle band every second (added by the user in post, A5), fixed outro (A7, A8) |
| **2 · Author defaults 作者默认** | How the author habitually executed the essence — the measured base every episode starts from | **The base, not a cage.** An episode starts here and **may depart when the topic's material, a demonstration, or a mechanism asks for it** — written as a sentence with its reason, staying inside tier 1. A departure is a device; if the same departure shows up in every beat it has become a new habit and must be either promoted into this file after review or removed | No wind-up before a move (A0 — the silence stores the energy); glide 0.5-0.8s, density 14-33/min, still share 71-88% (A6 bands); the three measured envelope families; grouped entries 0.2-0.4s apart; elements cast no shadow and carry no gradient (A4.1; the R1 reading — B6 sets light and shadow per register); lines uniform-weight and exact; imperfection expressed in time rather than in geometry; camera locked in production (the originals' rare small slow zoom is not written, A6); centered axis with 2-15% ink budget (A3; R1 reading, B6); hue signature regions (A2); "这是X" cold open; card tilt, page-peel and chapter-card transitions; the seven-part skeleton in its usual order |
| **3 · Free 每期自由** | Everything derived per episode with B1-B6 | Invent freely | The register inside the field's range (B6), the place and its depth planes, the inhabitant bible, the life layer (if any), canvas place and base (dark/light), the accent or pair, *when* color first lands and on which word, the one graphic motif, the native verbs and their envelopes, which move is the hero, where the longest hold sits, which element arrives late, the one sanctioned break (what and where), the case ladder, the domain anchor kit, the aphorism, the hook pattern |

**Examples of legal tier-2 departures**: a bow episode lets the string draw back before it fires — the one wind-up in the film, because the material *is* a wind-up; a calligraphy episode writes with a real brush envelope whose stroke ends flare and waver, because hand-made is the material (the horse episode already did this); a light-and-shadow episode lets the one object cast the one shadow, because the shadow is the lesson; a hero morph runs 20 s (A6 climax morph); a travel happens once because the canvas is a scroll and the travel *is* the reading (in production write it as the content sliding past a locked camera, in its own segment). **Examples of tier-1 violations dressed as creativity**: two things moving "for richness"; ambient drift "so it doesn't feel dead" (at R1–R2 always; at R3–R4 the one life layer of B6, declared once in the style block, is the only legal form — never added beat by beat); a second accent "for the comparison" when the topic is not a comparison; a cut "for pace"; a hand entering frame "for warmth" (a silhouette hand that *is* the lesson — Burch's half-in-frame limb in a film episode — is domain material, not warmth); a question opener "for the hook" in the long version.

Per-episode originality lives in tiers 2 and 3. **Tier 1 is the constraint set handed to `creative-animation-treatment` for tier C**; tier 2 is handed to it as *the base it departs from with reasons*, not as a second wall; B6 hands it the legal register range. A treatment that keeps the rhythm numbers but proposes a second color, a photoreal medium or a realistic face has left the style just as surely as one that adds a cut; a treatment that lets a bowstring wind up, or a brushstroke waver, has not.

**Five-step transplant — deriving a domain anchor kit when none is supplied.** Shenhai style = fixed animation grammar × the field's own visual alphabet; the grammar never changes, only the alphabet is swapped. Normally the kit arrives with the 任务消息 / 开工种子包 (planning-layer data). When this skill is used standalone, derive one in this order and treat it as the topic's fixed anchor set for every beat:

1. **Find the alphabet** — what are this field's "dots / lines / planes"? (a brushstroke, a beam, a coin, a contour line). Rule of thumb: knowledge explainable on a blackboard fits; knowledge that must be filmed to be believed does not.
2. **Fix the anchor kit and the register** — 3–5 instantly recognizable containers / notations / tools, described as geometry (H3 needs shapes, not names), one present in every beat; then the inhabitants that live inside them when the knowledge lives there (people, objects, works), and the field's main register and range (B6). A container alone is not a demonstration.
3. **Pick morph chains** — prefer evolution / growth / contrast knowledge points; each chain named by its start and end form.
4. **Build the case ladder** — historic masterpiece → classic application → modern product / app, every rung a real object the skeleton can be drawn over (gate 3).
5. **Apply the seven-part skeleton** — paired cold open → attribute contrast → cases → concept cards → interaction plant → aphorism → tri-icon outro.

Anti-fit regardless of alphabet: food review, travel scenery, emotional interviews, breaking news, physical-skill micro-teaching (principle episodes fine, tutorial episodes not).

## B0. 创意五问 — per-episode creative brief (run BEFORE writing any beat)

Answer question 0, then five questions from inside the topic's physical world; they feed every other derivation:

0. **Where does this knowledge live, and how much world does the frame need to show it?** → the register (B6). Swap the inhabitants for dots: if the lesson survives, it is R1 and the author's own minimalism applies; if it dies (who stands where, who looks at whom, what the light does, what the material does), the frame must hold the inhabitants. The register normally arrives in the brief; check it against this episode's evidence.
1. **What physical space does this topic live in?** → canvas material and place (B1). A character lives on paper; a star lives in deep space; code lives in a terminal.
2. **What in its world already owns a color?** → accent color (B2). Seal paste is red; a safelight is amber; blueprint paper is cyan.
3. **How does it naturally move?** → motion verbs and easing weights (B5). A character is written stroke by stroke; a wave propagates; a crystal grows.
4. **Can the form BE the content?** → the single biggest source of the "wow" feel: draw the sea out of the very line the episode is about; let light itself tell the story of light; make the like-button demonstrate the tilt.
5. **Can the platform interaction plant become a subject-matter example?** → interaction beat design (SKILL.md structure part 5).

## B1. Canvas — 画布三问

Ask three questions in order; they produce the canvas place, tonal base and mode:

1. **What physical place does the topic live in?** → the canvas material metaphor (xuan paper / blackboard / night sky / picture-frame mounting / phone screen / design-tool canvas). The canvas is that place, not a colored rectangle.
2. **Is that place light or dark by nature?** Diagrams, typography, silhouettes, knowledge told in ink → paper family (light). Light sources, glowing dots, luminous beams, screens in the dark → darkroom family (dark). UI/software topics may take the tool's own mid-grey canvas (documented third base).
3. **Does any core demo NEED darkness to read?** Card streams (glowing card edges), math construction (blackboard feel), any beat where the subject emits light → dark canvas wins even if the rest feels papery.

Then dress the canvas per A1: light pool or layered whites, warm black, micro grain — never dead-flat. Evidence from originals: graphic/typography/knowledge episodes ran light; card-stream, math-construction and glowing-subject episodes ran dark; the UI episode ran the tool's mid-grey. Neither value is "the default" — the topic's physicality decides.

At R3–R4 (B6) question 1's place stops being a metaphor for a surface and becomes the literal set: a screening room, a back alley, a layered paper landscape. Questions 2–3 still decide the light or dark base; A1's light pool becomes a named key light with a direction, and the "white not pure, black not black" rule holds for every tone in the set.

## B2. Accent Color — 选色三问

Ask three questions in order; stop at the first hit:

1. **Does the topic's own world already own an iconic color?** Brand color, tool color, cultural color, physical color — borrow it. Evidence: the phone-brand episode borrowed that brand's blue-violet; the game episode borrowed the game's signature yellow; the UI-annotation episode borrowed the design tool's selection-box tint; the calligraphy episode borrowed rubbing-and-seal red/ink contrast. The accent is stolen from the subject, so the color itself teaches.
2. **Is this episode a two-sided comparison at heart?** Then use the semantic cool-vs-warm pair (blue vs red) as the working colors instead of a single accent — the comparison IS the palette.
3. **Neither?** Pick one high-saturation, high-visibility color that maximizes contrast against black/white/grey on the chosen canvas — a "marker pen" color. Prefer the A2 hue-signature regions (warm orange-yellow / cool blue-violet / magenta-rose). (The original author's channel default was a fluorescent yellow; that was HIS answer to this question, not a rule. Your channel may standardize its own answer once and reuse it as a brand.)

Constraints from A2 always apply: single accent, full-video lock, full saturation, strong contrast, delayed entrance landing on the first knowledge point.

## B3. Anchor Colors

Domain anchors stay monochrome (at R3–R4 the episode's tonal body) + accent (A4.9). When a domain's real-world material has an iconic tint (blueprint paper, seal paste, laser red), do not ADD it as an extra color — either let it become the episode accent via B2-Q1, or draw the anchor in monochrome.

## B4. Copy-Paste Style Block (hex-free)

Embed one of these (with `{ACCENT}` filled with the B2 derivation result, described in words) at the start of `[Shot 1]` in every beat prompt. Neither block mentions a subtitle bar or a narrator: subtitles are added by the user in post (A5) and the voice is external (A7), so the block reserves the lower fifth of the frame and times the pulses to events, not to sentences. **The two blocks below are the R1 register** (the originals' world: signs on a lit canvas). Episodes at R2–R4 use the register blocks further down (B6 decides which); every block keeps the people policy in the closing sentence (`no_voice_en`), not in the canvas sentence.

**Light canvas ("paper"):**

```text
2D-animated minimalist motion-graphics explainer. The entire frame is a soft matte paper-grey canvas, one perceptible step below pure white with a faint warm lean and a barely visible paper grain; card surfaces and highlights sit a step brighter than the canvas base, and generous empty margins surround a single focal point; all graphics are flat vector shapes in warm ink-black, layered whites and a few greys with a single {ACCENT} accent color; the lower fifth of the frame stays completely empty at all times and the top-right corner stays clear. Everything happens in one continuous take with no cuts and a perfectly locked camera: at each timed event exactly one element changes in a single crisp change — it morphs, snaps into place, draws itself on or scales — then the canvas freezes completely until the next timed event.
```

**Dark canvas ("blackboard/darkroom"):**

```text
2D-animated minimalist motion-graphics explainer. The entire frame is a warm near-black canvas, one perceptible step above pure black, with a soft, perfectly steady pool of light in the middle that falls off into darker corners and a barely visible fine grain; graphics are thin white lines, white type and floating rounded-rectangle cards with a thin pale rim along their edges, plus a single {ACCENT} accent color; the lower fifth of the frame stays completely empty at all times and the top-right corner stays clear. Everything happens in one continuous take with no cuts and a perfectly locked camera: at each timed event exactly one element changes in a single crisp change — it morphs, snaps into place, draws itself on or scales — then the canvas freezes completely until the next timed event.
```

(2026-10-01: the dark block used to say the pool fell off "like a single lamp aimed at the middle of a wall" and that cards had "faintly glowing edges"; H3 drew the lamp and lit the edges as light — `h3-production-lessons` P-002, P-013. The sentences above describe the light itself.)

**Register blocks R2–R4** (B6; written as the storyboard `style` keys the pipeline uses; fill every `{…}`, delete the brackets; full-density slot list in `h3-prompt-writing` creative-compile §7):

R2 · cutaway diagram (light paper shown; the dark base swaps the canvas sentence for the dark one above):

```text
visual_prefix: 2D-animated technical-illustration explainer. The entire frame is a soft matte paper-grey sheet, one perceptible step below pure white with a faint warm lean and a barely visible paper grain, a touch brighter in the middle than at the corners. {The subject} is drawn as a clean cutaway at correct proportions in uniform warm ink-black outlines with two or three flat grey planes that give it volume: {parts, at most five, each named by its shape and position}. One soft light from {the upper left} lays a single short flat grey contact shadow under it toward {the lower right}. A single {ACCENT} accent is used only where described. The lower fifth of the frame stays completely empty at all times and the top-right corner stays clear.
motion_rule: (the mixed rule in h3-storyboard-writing §6, with the fixed parts named)
no_voice_en / hold_en / closing_en / sound_suffix: R1 defaults
```

R3 · tonal stage with a silhouette cast (dark base shown; light base = paper-grey ground with the darkest step as ink):

```text
visual_prefix: 2D-animated flat-graphic stage explainer. The entire frame is one place, {the place}, built from flat matte shapes in three or four close warm grey steps on a warm near-black ground, with a barely visible fine grain: {foreground occluder} in the darkest step along {edge}; {subject plane} in the middle; {background}; {far plane}. The recurring figures are featureless flat silhouettes — {cast bible: one sentence per figure, its outline and one trait only it has} — and only the outline of nose and chin shows which way each one faces. One key light comes from {direction}; every figure and object lays one flat, crisp-edged shadow shape toward {direction}, one grey step darker than the ground it falls on. A single {ACCENT} accent is used only where described; until its first arrival nothing in the frame carries it. The lower fifth of the frame is a plain, even strip of the darkest grey with nothing on it, and the top-right corner holds only {background element}.
motion_rule: One continuous shot with a perfectly locked camera: no zoom, no pan, no camera drift. Each timed event has exactly one main change, and at most one smaller reaction that belongs to it. A change with no finishing time is a single crisp change completed within a quarter second; a change with a finishing time moves steadily and stops dead exactly at that time. A figure never walks or gestures on its own; it changes pose only by snapping into the new pose. Between events every figure, every set piece and every frame holds perfectly still. {The fixed set pieces} are fixed flat cut-outs that never move, resize or drift. Everything already in the frame keeps its exact shape, size, position and brightness unless a timed event changes it; nothing fades, flickers or sheds fragments on its own.
no_voice_en: No speech, no dialogue, no human voice of any kind; no realistic people or faces — the only figures are the flat featureless silhouettes described, with their mouths closed; no on-screen text other than the labels described.
hold_en: then the figures and the set hold still in their new positions
closing_en: and the figures and the set hold still in place until the end
sound_suffix: {the bed of this place: one or two low, steady sounds, no melody}; no voices.
```

R4 · cut-paper diorama:

```text
visual_prefix: Paper-craft stop-motion diorama explainer photographed in macro, seen straight on. Every element is cut from matte paper and card with visible thickness, clean cut edges and a fine fibre texture, in {three or four tones of one paper family}: {far plane}; {background}; {subject plane}; {foreground occluder}. One soft key light from {direction} lays a short, real contact shadow behind every layer, so each plane stands visibly in front of the one behind it; the depth of field is shallow and only the {subject plane} is sharp. {Inhabitant bible, in paper}. A single {ACCENT} paper is used only where described; until its first arrival no piece is that color. The lower fifth of the frame is a plain strip of {ground paper} with nothing on it, and the top-right corner holds only {far plane}.
motion_rule: One continuous shot with a perfectly locked camera: no zoom, no pan, no camera drift. Each timed event moves exactly one paper piece or one group, in stop-motion steps: it slides or pops into place and presses flat. A change with no finishing time completes within a quarter second; a change with a finishing time moves steadily and stops dead exactly at that time. Between events every paper piece holds perfectly still. {The fixed planes} are glued in place and never move, curl or drift. Everything already in the frame keeps its exact shape, size, position and brightness unless a timed event changes it; nothing fades, flickers or sheds fragments on its own.
no_voice_en: R1 default when there are no figures; with paper figures: No speech, no dialogue, no human voice of any kind; no realistic people or faces — the only figures are the flat paper cut-out figures described, with no facial features; no on-screen text other than the labels described.
hold_en: then every paper piece holds still in its new place
closing_en: and every paper piece holds still in place until the end
sound_suffix: {the bed of this place: low and steady}; no voices.  (per-event foley: paper slide, card tap, a soft press)
```

A life layer (R3–R4 only, 待测, default none) is one sentence added to `motion_rule`, written as in `h3-storyboard-writing` §6 (living mode), with the area budget there.

In the tool pipeline this block is split into the storyboard `style` fields `visual_prefix` (canvas / color / empty-band sentence) and `motion_rule` (continuous-take / locked camera / crisp change / freeze sentence); `h3_storyboard action=style` overrides them per episode. Normally only `visual_prefix` is replaced and the default `motion_rule` ("One continuous shot with a perfectly locked camera: no zoom, no pan, no camera drift. Every timed event is a single crisp change completed within a quarter second, followed by absolute stillness until the next timed event. There is no swinging or elastic bouncing.") stays, because `compensation_s` +0.2 was measured with it. The pipeline's reference `DEFAULT_STYLE` (`bridge/h3_storyboard.py` in h3-pi-agent) is the 001-期 seal-red paper variant and does carry hex values because it was measured from the rendered test; hand-written blocks stay hex-free.

**Closing sentence** (identical in every beat, ends the picture field; R1–R2, and R4 without figures — R3 and R4 with figures use the register `no_voice_en` above):

```text
No speech, no dialogue, no human voice of any kind; no people or faces appear; no on-screen text other than the labels described.
```

**Shared audio blocks** (identical structure in every beat; the sound list follows the beat's timecodes):

```text
overall_soundscape: A thin paper-scratch tick at 00:00.300; a gentle tick at 00:02.144; … . Quiet room tone underneath; no voices.

non_diegetic_music: N/A
```

`{ACCENT}` is filled with a plain-language color phrase (e.g. "fluorescent yellow", "electric violet-blue", "vivid seal-red") — the phrase your B2 derivation produced for THIS topic. State it identically in every beat of the video.

## B5. Motion Texture — 运动质感推导 (material → verbs, weights, sounds)

Ask: **what is the topic's material, and how heavy / how sharp is it?** Then derive:

1. **Verbs from the material's world** (创意五问-Q3): a character is written stroke by stroke; a wave propagates outward; a crystal grows facet by facet; a shutter blinks; a coin flips. Do not default to generic slide/fade when the material offers a native verb.
2. **Easing weight from the material's mass**: heavy materials (stone, metal, architecture) move with slower attacks, longer settles and blunter overshoot; sharp/light materials (light beams, electricity, UI) fire with fast attacks and tight settles; paper/fabric snaps and folds crisply. All weights stay inside the A6 constraint band (attack 0.1-0.5s, release 1.4-1.6×) — the material shifts WHERE in the band each event sits. In the default timecode line (crisp change within a quarter second) mass is carried by the verb, the sound and the size of the change — a stone *lands* with a low thud, a beam *flicks on* — not by a longer move.
3. **Event sounds from the material** (optional, within A7 limits): a stone lands with a low thud, paper snaps, a light flicks on with a soft click — still sparse, still event-tied, never continuous.

Benchmark samples (results, not rules): the horse episode wrote strokes on and morphed them (writing = the material's motion); the light episode swept beams and bloomed dots (light moves fast and sharp).

4. **The feel layer.** The invisible details that make a move feel authored — anticipation, how it settles, uneven offsets inside a group, where the eye is when the next thing changes, the one deliberate imperfection, color arriving as an event — are written up once for all styles in `creative-animation-treatment/references/feel.md` (§一 motion, §二 color, §四 the mediocre-defaults delete list, §六 six self-tests). Run its questions on every beat. The author's frames already answer several of them; sort those answers by the three tiers in B-0 — some are the essence and hold always, most are the **base** the episode starts from and may leave with a reason:

   **Essence (tier 1) — feel.md never overrides these:**
   - **The hold (§一 6)** is a *dead* hold on everything that carries information: zero pixels, no moving hold, no secondary life (A6). feel.md's "moving hold vs dead hold — decide once" is decided: dead. The only exception is the one constant life layer an R3–R4 episode may carry (B6, 待测, default none) — it never carries information and never changes at an event. The part that applies in full is *placement* — the hold before the beat's key event is the longest one.
   - **One thing moves (§一 10 dynamics)**: at most one element changes; a reaction the event itself causes (the sparrow that flinches when the shadow lands) counts as part of that event, as parented elements do in A6, and is always a tier smaller; one hero per chapter within a 10–22× range. Richness never justifies a second, independent mover.
   - **Color as event (§二 1–9)**: one accent (or one pair) derived by B2, arriving late on the first knowledge point at full saturation, at most one break per film (A2, A9.5). The treatment may decide *when* and *on what* color lands, never *which hue* — hue is B2's job.

   **Author defaults (tier 2) — the base; depart when the material, the demonstration or a mechanism asks for it, as a written device, never as a habit:**
   - **Anticipation (§一 1)**: the base is no wind-up — the preceding silence is the preparation; write "the canvas holds perfectly still, then X snaps…". A visible wind-up is allowed when the material *is* one (a bowstring drawn, a spring compressed, a brush lifting before the stroke) and is spent on the beat's hero move; two wind-ups in a film means the base has been abandoned.
   - **Envelope (§一 2–3)**: base is the three measured families (slide fires and settles with a slight overshoot; draw-on accelerates and stops dead; morph is even) — never one easing for all. A new envelope is welcome when the material brings it (a pendulum's symmetric swing, a heavy stone's long settle, ink's slow bleed-stop). *Production:* envelopes are for a declared gradual style only (A6); the default timecode line expresses weight through the size and contrast of the crisp change, not its duration.
   - **Offset (§一 5)**: base 0.2–0.4 s between grouped entries, never metronomic — vary the gaps, let the last one land a hair late. Wider or tighter spacing when the material's rhythm (a heartbeat, a metronome that is the topic) demands it. *Production:* the offset lives inside one event's clause ("one after another, the last a hair late"); never one timecode per item (A6 One Event).
   - **Imperfection (§一 11)**: base is *temporal* — one element late, one overshoot a touch larger, one hold longer than expected — because the author's world is exact vector (A4.1). *Geometric* imperfection (a stroke end that flares, a line that wavers) is legal exactly when hand-made is the material — calligraphy, sketching, carving (the horse episode's brush strokes are the precedent). Otherwise a wobble reads as generator noise, not as craft.
   - **Light and shadow (§二 5, Step 7 "contact shadow")**: base at R1 is a lit canvas (A1 light pool, warm black, grain) with elements that cast no shadow and carry no gradient (A4.1); depth lives in grey levels. The one shadow is legal when the shadow is the lesson (light, sundials, perspective, photography) — and then it belongs to the one object the lesson is about. The register moves the base (B6): R2 gives the subject one short flat contact shadow, R3 gives every figure and set piece one flat crisp-edged shadow shape from one named key light, R4 gives real contact shadows between paper layers. Shadows stay shapes, never gradients or glow.
   - **Camera**: locked in production (B4, default `motion_rule`); the originals' small slow zoom is not written. When travel *is* the reading (a scroll unrolling, a timeline that must be travelled), write the content sliding past the locked camera as one event in its own segment; that is the film's sanctioned break and nothing else may break. A real camera move needs a rewritten `motion_rule` for that segment and an `h3_align` re-check.

   Everything feel.md asks that Part A leaves silent — how each material stops, which element is the late one, which sentence the accent lands on, which move is the chapter's hero, where the longest hold sits, what the one invisible detail is — is decided here, per episode, and written into the beat as a sentence. When a tier-2 departure is used, the beat table says so and says why; the six self-tests in feel.md §六 still apply.

## B6. 画面档位 Register — 世界有多满（方向定主档与范围，每期再判一次）

**Why this exists.** The 13 originals are all R1 — signs on a lit canvas — because the author's subject is graphic design: dots, lines and planes *are* his knowledge (A4.9 says so). That minimalism is his derivation for his subject, not the style. B-0 rule 1 is the real constant: *perform the principle with the principle's own material*. For a field whose material is people, places, light or matter, flat glyphs break rule 1 harder than a fuller world breaks the habit of emptiness. 2026-10-01 evidence: a film-language episode drawn at R1 (one wire, two clip-art birds, a frame, one yellow fill on cream paper) passed alignment and read as "元素极其简单、动画中等" to the user; the knowledge (who is in frame, who is outside it, where the light falls) had nowhere to live (`h3-production-lessons` F-007).

**How to decide.** Run the five register questions in `creative-animation-treatment/references/world-class.md` §一 (where the knowledge lives / replace-with-dots test / texture / emotion / evidence) — the shared tool holds the ruler; this section holds the author's readings. The register normally arrives with the brief (任务消息 / 种子包 carry the field's main register and range); standalone, derive it with those questions and B0 question 0.

**Legal range for this style: R1–R4.** R5 (cinematic 3D, atmospheric perspective, real camera moves) leaves tier 1 (a made, drawn or cut world on one locked canvas) and is a style variant → `h3-research-director` ⑤.

| 档 | 在深海里长什么样 | 住户 | 光与影 | 活层 | 读数口径 | 典型领域（初分，以种子包为准） |
| --- | --- | --- | --- | --- | --- | --- |
| R1 符号 | 原片：点线面、记号、字形、构造线、卡片，在有光的纸或暗室上（B4 两块） | 记号本身 | 画布光池，元素不投影 | 无 | A2 / A3 原读数 | 汉字字体、乐理、数学、拓扑、数据可视化、密码、信号 |
| R2 图解 | 剖面、爆炸图、装置线稿，比例正确，零件 ≤5、数量写死；扁平矢量加两三档灰的体积面 | 器物、装置、机构 | 一盏方向光，主体一块扁平接触影 | 无 | 墨量可到 10–30%；色面守 A2 | 机械、工程力学、物理与化学实验、汽车、家电、建筑结构 |
| R3 舞台 | 一个扁平的地点：三四档灰的布景分前景遮挡 / 中景 / 背景 / 远景；固定的无五官剪影演员或设计过的动物剪影；骨架线可叠在上面（A9.2） | 剪影演员 1–3 位、布景 ≤8 件，每件一句定稿外形 | 一盏有方向的主光，每件东西一块扁平硬边影；光块挪位可以就是演示 | 可选一层（待测），默认无 | 墨量 20–60%（`target_ink` 只是下限）；色面守 A2，底色族饱和度低于 0.35 | 电影视听、心理实验、宠物行为、穿搭、行为经济与生活经济、公司与货币史的情景、法医现场俯视 |
| R4 纸艺 | 纸面画布字面化：分层剪纸 / 立体书，纸有厚度、切边、纤维，层间真实接触阴影，微距浅景深 | 纸剪的地形、器物、生物、人形（无五官） | 一盏主光，层间接触阴影 | 可选一层（待测），默认无 | 墨量不限；色面守 A2，纸色族饱和度低于 0.35 | 地理、地质、天气、古生物、生物的生命过程、传统手艺与纹样的来历 |

**What never changes across registers** (tier 1 read in register terms): at most one change at a time (its own reaction included, B5.4); nothing that carries information moves between events; one accent at full saturation, arriving late on the first knowledge point; a calm stating voice that never pauses; show before name, one atom, real evidence with the skeleton drawn on, back to the viewer's hand; one canvas, zero cuts — a cut happens only inside a frame on screen (a screen's picture changes, the screen stays); locked camera in production; a made world (no live action, no photoreal, no realistic face, no fingers); the lower fifth reserved for subtitles.

**What the register moves** (tier-2 bases that each register replaces, written once in the episode's style block, not as per-beat departures): how much of the frame is world (A3 ink budget), shadows (B5.4 light and shadow), the tonal body (A2 note), inhabitants (A4.4 silhouette cast), the life layer (A6 note), the canvas as literal set (B1 note).

**Discipline.**

- One register per episode. R1 skeleton lines and notations laid over an R2–R4 world are not a switch — they are A9.2 (evidence with the skeleton drawn on) and the strongest form of it.
- A register switch is allowed only at a concept-card chapter turn, at most once per film, through a full-canvas hinge (the same rule as A1.4's light↔dark switch).
- An episode may move one step inside the field's range when its evidence or demonstration asks (a film episode about an aspect-ratio number may drop to R1; a typography episode about a carved stele may rise to R4); write the reason in ①.
- Register up does not mean more events: the world lives in the style block (B4 register blocks; `h3-prompt-writing` creative-compile §7), the beats keep A6's budget.
- Readings stay floors: `target_ink` / `target_color_area` in the episode style still guard against empty frames and a thin accent; at R3–R4 the accent must still become a surface at least once per chapter.

**作者感觉对照 for a register change** (the check, `style-foundations`「作者感觉」): *Would he do it this way?* — He makes every film out of its subject's own material (B-0.1); for film the material is a screen with people and light in it, so a tonal stage with a silhouette cast is his move, dots are not. He keeps one thing changing and the rest dead still, one late accent, a voice that states — all unchanged. He would not add a second color, a camera move, a face or a cut; none of those comes with the register.
