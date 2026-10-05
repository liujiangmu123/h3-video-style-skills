# Beat Templates B1-B8 — Full H3 Prompt Patterns (timecode form)

Every template below is a complete H3 prompt skeleton. Replace `{...}` placeholders. `{STYLE_BLOCK}` = the light or dark canvas block from `style-dna.md` Part B4, with `{ACCENT}` filled by the 选色三问 derivation result (a plain-language color phrase — never a hex code). `{NO_VOICE}` = the closing sentence from B4: `No speech, no dialogue, no human voice of any kind; no people or faces appear; no on-screen text other than the labels described.`

**Production motion rule.** In the pipeline `{STYLE_BLOCK}` = the storyboard's `visual_prefix` (B4's canvas + accent sentences) followed by the default `motion_rule`: `One continuous shot with a perfectly locked camera: no zoom, no pan, no camera drift. Every timed event is a single crisp change completed within a quarter second, followed by absolute stillness until the next timed event. There is no swinging or elastic bouncing.` It replaces B4's camera clause ("apart from an occasional zoom") and its "envelope follows its verb" clause — those describe the originals (glides 0.5-0.8 s, staggers 0.2-0.4 s, rare slow zooms). The templates below are written in that default. A declared gradual style (draw-on / elastic settle written into a rewritten motion_rule) sets `compensation_s` ≈ −0.5 and is re-measured with `h3_align` before production.

**The narration is NOT in the prompt.** It is recorded first by TTS (`h3_plan_durations`); each sentence's start time inside the segment becomes the timecode of the event it triggers. In the tool pipeline `h3_timecode` assembles these prompts from `分镜_长版.json` (one English `visual_en` + optional `sfx_en` per sentence, or several `beats` with `at` ratios) and `timing.json`; the templates here show what that output should look like when written by hand, and what wording to put into `visual_en`. The external narration is quoted beside each template only so the writer can see which sentence each timecode belongs to.

Rules that apply to ALL beats (format authority: field names and order from the official `h3-prompt-writing` skill — `references/base-en.txt` for T2VA / I2VA / FL2VA, `references/ref-en.txt` for Ref2VA; the timecode line's own conventions from `h3-storyboard-writing` §9. When this file disagrees with them on field names, order or fixed phrases, they win):

- **Field order is fixed**: `integrated_multimodal_description:` → blank line → `overall_soundscape:` → blank line → `non_diegetic_music:`. T2VA starts directly with the first field. The production line is T2VA in every beat, chained by latent continuation (segment N+1 starts from segment N's tail). **Standalone use only** (no pipeline, frames extracted by hand) may take I2VA / FL2VA; those prompts start with the guide's instruction line **verbatim**, then one blank line:
  - I2VA: `For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.`
  - FL2VA: `How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the S.SS-second mark of the target video.` (S.SS = beat duration, two decimals)
  - Ref2VA (B4 with user-supplied real assets, standalone only) uses the six-section format instead: `subject_definitions` → `summary` → `retention_analysis` → `detailed_description` → `overall_soundscape` → `non_diegetic_music`; style sentence goes *before* `[Shot 1]` in `detailed_description`. `<Picture N>` never appears in a production-line prompt (the quality gate rejects it).
- Single `[Shot 1]`, never a `[Shot 2]`; no timestamp on Shot 1. `[Shot 1]` opens with the style block, whose first words are the official style word `2D-animated`.
- **No `<d>…</d>`, no narrator / voiceover / (S1) / "says", no subtitle bar, no quoted narration text.** The voice track is added at assembly and subtitles are made by the user in post; H3 never hears the audio. The style block keeps the lower fifth of the frame empty for the subtitles; `{NO_VOICE}` closes every picture field and carries the people policy (R1–R2: no people or faces; R3–R4 with a cast: the register sentence in `style-dna.md` B4).
- **Register (`style-dna.md` B6).** The templates below are written in R1 (signs on a lit canvas). At R2–R4 `{STYLE_BLOCK}` is the episode's register block (B4), the freeze phrase is the register's `hold_en` / `closing_en`, and each event is written as **anchor + envelope + reaction + hold** in one clause (`h3-prompt-writing` creative-compile §7.2), e.g. B2 at R3: `the picture inside the lower screen instantly changes into a close shot of the same seated figure, her shoulders filling the frame; the screen border, the table and the other screen remain exactly unchanged`. Beat types, timecode rules and event budgets do not change with the register.
- **One event ↔ one absolute timecode**: `At {tc}, {element} {action} with {sound}, then the canvas freezes.` `{tc}` = `MM:SS.mmm` = the triggering sentence's start within the segment + `compensation_s` (default +0.2 s with the locked-camera / instant-appearance motion rule; about −0.5 s only for gradual draw-on styles), + 0.917 s continuation head for segments ≥2, and never earlier than 0.300 (segment 1) / 1.217 (segments ≥2) for the segment's first event. Long actions (stroke-by-stroke drawing, gradual reveals) add `, finishing by {tc}` so H3 has a hard end and does not push later events back. Several sub-events of one sentence are joined with `; at {tc}, …` and share one trailing freeze (keep them ≳1.2 s apart, or H3 merges them into one). Timecodes strictly increase; ≤6 per segment; the last one ≥0.5 s before the segment end.
- The last event of the beat ends with `and everything holds completely still until the end.` instead of a freeze, so the next segment continues from a still frame.
- Camera: perfectly locked (the default motion_rule already says so; a hand-written prompt may add `the camera holds a static shot`). The guide's `zooms in / pulls out with small amplitude at slow speed` matches the originals' rare breathing zoom but is **not written in the timecode line** — `h3_align`'s frame diff reads camera motion as whole-frame motion and loses the event onsets. Never `drifts`, `floats`, `orbits`, `pans`, `dollies`.
- **At most one animation event per narration sentence, and roughly one event per 1-2 sentences** (frame-level re-read 2026-09-05: 0.5-1.1 events per sentence, a third to a half of sentences with no motion). A 12s beat carrying 3-4 sentences should have 2-3 timecodes — a sentence that triggers nothing is written `→ 视觉：（静止）` (storyboard `still`) and gets no `At` clause. **ECG rhythm**: the event is a short crisp pulse (the originals glide ≈0.5-0.8s with a verb-specific envelope; production writes a single crisp change completed within a quarter second, and envelopes — slide = fast attack + elastic settle, draw-on = accelerate and stop dead — only in a declared gradual style, see above); until the next timecode the canvas freezes completely — always write the freeze. Place events on a sentence's first syllable or on its key noun (the cue you take from `timing.json` is the sentence start; a key-noun placement is a `beats` entry with an `at` ratio). At most one element moves at any moment; a grouped entry is **ONE timed event** whose clause says the items enter one after another, the last a hair late (`three cards snap in one after another, the last a hair late`) — never separate timecodes 0.2-0.4 s apart (the originals' stagger), because H3 merges two small actions written ≲1.2 s apart; never a metronomic cascade.
- **Feel layer** (`style-dna.md` B5.4 → `creative-animation-treatment/references/feel.md`): each event is written with what precedes it (by default the dead hold *is* the preparation — no wind-up; a visible wind-up is a tier-2 device reserved for a hero move whose material is one), its speed shape and its ending — the ending names the material (paper snaps and stops dead; a card is the heaviest thing and sinks once without rebounding; a line accelerates and stops the instant it completes). The longest freeze of the beat sits *before* its key event, not after. Each beat carries exactly one deliberate irregularity: by default **temporal** (one label arrives a hair late; one overshoot is a touch larger) because the author's world is exact vector; **geometric** (a flaring stroke end, a wavering line) only when hand-made is the material. Never random jitter. When a beat departs from an author default (B-0 tier 2), the beat table names the departure and its reason. A vague verb ("slides in / fades in / moves") is a placeholder to be replaced before delivery: `instantly pops in / snaps into place / changes into / flips to` (`h3-storyboard-writing` §2), every morph written with its start and end form.
- Narration budget per beat ≈ beat_seconds × 3.5 characters with our MiniMax voice (a 12s beat ≈ 40 characters in 3-4 sentences; the reference films' ×5 renders ≈30% long); pauses between sentences stay under 1s — never stop the voice to let the picture breathe. The beat's duration itself is **derived** from the recording (`grid(speech + gapSegment)`), never chosen first.
- End every visual description with the state the NEXT beat will start from (the final "holds completely still until the end").
- Every beat shows at least one item from the topic's domain anchor kit (`style-dna.md` A4.9): a domain container framing the demo, domain notation on the demo, or a domain tool in frame. Abstract atoms get captured inside a domain container within their first beat.
- `overall_soundscape` lists the same sounds by timecode and ends with `Quiet room tone underneath; no voices.`; `non_diegetic_music: N/A` in every beat (no BGM is generated; the user adds any in post).

Timecode placeholders below (`{tc1}`, `{tc2}` …) are illustrative: real values come from `timing.json`.

---

## B1 Cold Open — "这是X" (T2VA, 6-10s)

Purpose: define the topic's atomic element, alone on the canvas. Narration (external): `这是{X}。` / `这是{Y}。` / `{把元素与领域绑定的句子}`.

```text
integrated_multimodal_description: [Shot 1] {STYLE_BLOCK} At {tc1}, {atomic element, e.g. "a single thick vertical black bar"} instantly pops in slightly left of center with a soft brush-on-paper stroke, then the canvas freezes. At {tc2}, the element {first morph, e.g. "snaps from upright to a 30-degree clockwise tilt around its center in one crisp change"} with a soft whoosh, then the canvas freezes. At {tc3}, {domain anchor lands, e.g. four black corner brackets snap in around the element one after another forming a viewfinder frame, and a small exposure readout "1/125 · f/2.8" pops in along the bottom inside edge, the readout landing a hair late} with a gentle tick, and everything holds completely still until the end. {NO_VOICE}

overall_soundscape: A soft brush-on-paper stroke at {tc1}; a soft whoosh at {tc2}; a gentle tick at {tc3}. Quiet room tone underneath; no voices.

non_diegetic_music: N/A
```

## B2 Concept Contrast — paired attributes (T2VA, 10-15s)

Purpose: show the two poles of an attribute via morph or side-by-side. Narration: `{A的属性句，如：横平竖直的线条}` / `{A的效果句，如：让画面沉静、稳定}` / `{B的属性句}` / `{B的效果句，如：立刻呈现出动感与张力}`. Four sentences, three or four events — let one pass with nothing moving.

```text
integrated_multimodal_description: [Shot 1] {STYLE_BLOCK} The frame opens on {state A, continuing from the previous beat}. At {tc1}, {elements arrange into pattern A, e.g. "three vertical bars snap into a calm grid"} with a soft whoosh, then the canvas freezes. At {tc2}, {a small accent-color check or underline confirms the state} with a gentle tick, then the canvas freezes. At {tc3}, every element {changes to pole B in one timed event, e.g. "the upright bars snap into a 30-degree slant one after another, the last one a hair late"} with three soft whooshes, then the canvas freezes. At {tc4}, {accent-color motion lines snap in outward from the bars} with a faint swish, and everything holds completely still until the end. {NO_VOICE}

overall_soundscape: A soft whoosh at {tc1}; a gentle tick at {tc2}; three staggered soft whooshes at {tc3}; a faint swish at {tc4}. Quiet room tone underneath; no voices.

non_diegetic_music: N/A
```

Standalone FL2VA variant: render pole A as Picture 1 and pole B as Picture 2, use the FL2VA alignment instruction and describe only the morph path between them — still with timecodes, still `{NO_VOICE}`, still `N/A`.

## B3 Morph Chain Demo — knowledge ladder (T2VA, 10-15s)

Purpose: 2-4 linked transformations that each illustrate one sentence.

```text
integrated_multimodal_description: [Shot 1] {STYLE_BLOCK} It begins with {element 1}. At {tc1}, {morph 1: "the complete loose outline of {element 2} snaps in around it"} with a soft brush stroke, then the canvas freezes. At {tc2}, {morph 2: "the loose outline changes into a solid black silhouette"} with a low soft thud, then the canvas freezes. At {tc3}, {morph 3: "the detailed silhouette changes into its simplified iconic shape, the redundant limbs gone"} with a faint hush; at {tc4}, the final form instantly turns {ACCENT} with a gentle tick, and everything holds completely still until the end. Each transformation is a single crisp change from the stated start form to the stated end form. {NO_VOICE}

overall_soundscape: A soft brush stroke at {tc1}; a low soft thud at {tc2}; a faint hush at {tc3}; a gentle tick at {tc4}. Quiet room tone underneath; no voices.

non_diegetic_music: N/A
```

Declared gradual style only (motion_rule rewritten, `compensation_s` ≈ −0.5, re-measured with `h3_align`): morph 1 may become a draw-on — `the outline draws itself stroke by stroke, the line accelerating and stopping dead the instant it completes, finishing by {tc1_end}` — with `soft brush strokes from {tc1} to {tc1_end}` in the soundscape.

## B4 Case Exhibit — real assets in cards (T2VA, 10-15s)

Purpose: quote paintings / logos / product photos / UI screenshots as floating matted cards.

The production pipeline runs T2VA with latent continuation (no `<Picture N>` references — they are rejected by the quality gate), so describe the asset as a **flat vector redraw**:

```text
integrated_multimodal_description: [Shot 1] {STYLE_BLOCK} At {tc1}, a rounded-rectangle card snaps into place at the center and lands heavy with no rebound, with a faint paper slide, containing a flat vector redraw in uniform black strokes of {famous work / product} with a thin margin, tilted about 4 degrees in gentle 3D perspective, then the canvas freezes. At {tc2}, a bold {ACCENT} annotation arrow instantly pops in across the card pointing at {detail}, with a gentle tick, then the canvas freezes. {Optional: At {tc3}, a second smaller card snaps in beside it for comparison with a soft whoosh, then the canvas freezes.} At {tc4}, the card instantly shrinks to two-thirds of its size with a faint hush, and everything holds completely still until the end. {NO_VOICE}

overall_soundscape: A faint paper slide at {tc1}; a gentle tick at {tc2}; a soft whoosh at {tc3}; a faint hush at {tc4}. Quiet room tone underneath; no voices.

non_diegetic_music: N/A
```

Standalone use with user-supplied reference images may still take the Ref2VA six-section format from the `h3-prompt-writing` skill (`<Subject 1> is the artwork in <Picture 1>` …); keep the same timecode / `{NO_VOICE}` / `N/A` rules inside `detailed_description`, and write the canvas sentence there without any subtitle bar.

## B5 Concept Card — bilingual term (T2VA, 6-10s)

Purpose: chapter-turn typography card. Two locked layouts. The card text IS content text, so it stays in the prompt in exact quotes. Narration: `{这被称为TERM}` / `{一句解释}`.

Light canvas:

```text
integrated_multimodal_description: [Shot 1] {STYLE_BLOCK-light} The canvas clears to empty. At {tc1}, huge black bold sans-serif words "{TERM IN ENGLISH}" instantly pop in at the center with a subtle pop, and a bright {ACCENT} highlighter bar snaps in under the full width of the text with a soft marker swish, then the canvas freezes. At {tc2}, a small Chinese annotation "{中文注释}" pops in below the headline with a gentle tick, and everything holds completely still until the end. {NO_VOICE}

overall_soundscape: A subtle pop and a soft marker swish at {tc1}; a gentle tick at {tc2}. Quiet room tone underneath; no voices.

non_diegetic_music: N/A
```

Dark canvas:

```text
integrated_multimodal_description: [Shot 1] {STYLE_BLOCK-dark} The canvas is empty near-black. At {tc1}, large white serif Chinese characters "{术语}" instantly appear at the center with a faint hush, then the canvas freezes. At {tc2}, "{KEY FIGURE like √2:1}" in white serif appears below with a {ACCENT} color block snapping in as its underline with a soft whoosh, then the canvas freezes. At {tc3}, a thin italic English line "{English term}" pops in beneath with a gentle tick, and everything holds completely still until the end. {NO_VOICE}

overall_soundscape: A faint hush at {tc1}; a soft whoosh at {tc2}; a gentle tick at {tc3}. Quiet room tone underneath; no voices.

non_diegetic_music: N/A
```

## B6 Interaction Plant — platform button as example (T2VA, 6-10s)

Purpose: make the like/subscribe UI itself demonstrate the current lesson. Narration: `{把课程知识点绑定到按钮的句子}` / `快去试试吧。`

```text
integrated_multimodal_description: [Shot 1] {STYLE_BLOCK} A large flat white thumbs-up "like" icon sits center canvas. At {tc1}, the icon demonstrates the lesson: {e.g. "it snaps from upright to a 15-degree tilt to the left" / "thick accent-color lines burst from its top edge in one crisp change" / "its solid face changes into an outline drawing"} with {matching UI sound}, then the canvas freezes. At {tc2}, the icon instantly turns {ACCENT} with a subtle pop, and everything holds completely still until the end. {NO_VOICE}

overall_soundscape: {matching UI sound} at {tc1}; a subtle pop at {tc2}. Quiet room tone underneath; no voices.

non_diegetic_music: N/A
```

## B7 Aphorism — closing truth (T2VA, 5-8s)

Narration (external, slightly slower): `{金句，如：设计，就是在不同的形式间做出最准确的表达。}`

```text
integrated_multimodal_description: [Shot 1] {STYLE_BLOCK} At {tc1}, all case elements vanish one after another in one quick exit, the last a hair late, with a faint hush, leaving {the original atomic element from B1} alone at center, then the canvas freezes. At {tc2}, the element changes into {its final form, echoing the video's theme} in one last crisp change with a soft brush stroke, and everything holds completely still until the end. {NO_VOICE}

overall_soundscape: A faint hush at {tc1}; a soft brush stroke at {tc2}. Quiet room tone underneath; no voices.

non_diegetic_music: N/A
```

## B8 Fixed Outro — tri-icon (T2VA, 5-6s)

Narration (external): `感谢大家看到这里，更多{领域}内容，欢迎关注{频道名}，不要忘记一键三连，我们下期再见。` — the `{tc2}` pulse sits on "一键三连" (a `beats` entry with an `at` ratio inside the sentence).

```text
integrated_multimodal_description: [Shot 1] {STYLE_BLOCK} At {tc1}, three flat rounded white icons — a thumbs-up, a coin, a five-pointed star — snap into a horizontal row at center one after another, each with a subtle pop, the star a hair late, then the canvas freezes. At {tc2}, the three icons instantly turn {ACCENT} together with a gentle tick, and everything holds completely still until the end. {NO_VOICE}

overall_soundscape: Three staggered subtle pops from {tc1}; a gentle tick at {tc2}. Quiet room tone underneath; no voices.

non_diegetic_music: N/A
```

---

## Beat Table Format (deliverable)

Durations are **derived, not chosen**: after `h3_plan_durations` each row's Dur = `grid(speech + gapSegment)`. Fill the narration and event columns first with no seconds; let the tool fill Dur and the timecodes. Rows whose sentence triggers nothing carry （静止） in the event column (in the MD: `→ 视觉：（静止）`; the storyboard marks it `still` and writes no timecode).

The table opens with one line: `Register R? · reason · style block = B4 {block name}`.

| # | Type | Dur (derived) | Narration (Chinese, external) | Visual event chain (one `visual_en` per sentence, or （静止）) | Sounds | Tier-2 departure (if any) + reason |
|---|------|---------------|-------------------------------|---------------------------------------------------|--------|------------------------------------|
| 1 | B1 | 10.833s | 这是光。/ 这是一束被约束的光。/ 约束它的开口，叫做光圈。 | dot instantly pops in → （静止） → six blades snap in around it one after another | brush stroke / — / soft whoosh | — |
| 2 | B2 | — | ... | ... | ... | ... |

Assembly notes to include with every delivery: `h3_deliver tier=2k` (narration only on the delivered track; rough cuts use `h3_assemble mode=rough audio=mix` = narration + H3 event sounds peak-normalized and ducked). No subtitles are burned and no BGM is laid — the empty lower band and any music are the user's post work; verify with `h3_align` before finalizing. Acceptance grades: **pass** = every written timecode matched to a detected motion onset AND median offset ≤ 0.2 s AND max offset ≤ 0.3 s; **check** = every timecode matched AND median offset ≤ 0.35 s (max may exceed 0.3 s — inspect the outliers by eye); anything else (any unmatched timecode, or median > 0.35 s) = **fail** → adjust `compensation_s` / rewrite the weak event and re-run. Standalone deliveries (no pipeline) note instead: concat order, which boundaries use I2VA / FL2VA and which frame to extract, and that per-beat music is muted in favour of one continuous bed.
