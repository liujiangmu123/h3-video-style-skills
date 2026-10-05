---
name: codegen-style-showcase
description: "Make 代码生成视频·N种风格 showcase episodes — the style skill (风格 skill) for the 'one frame, N different cores' format learned from the Opus 5.5 fifteen-styles reel: a title giving the count and the bar, then N identical ~10.8 s segments where a caption card lights first (number · name · three restrained lines · two tech tags), one smallest unit (dot, drop, square, line) grows into a finished piece (wordmark / cover / poster), the biggest change lands at ~63%, it settles, then silence + one dot bridges to the next; ends on an N-cell overview + title callback + a three-beat line. No narration, no CTA, no hard cuts between segments. Hybrid production: code for frame, cards and type; H3 for the cores it does well. Use for N种风格盘点 / 同题多风格对比 / 一物N画 / 代码动画风格库, or how this format writes cards, segments or H3 prompts. Topics: codegen-showcase-series-planner."
metadata:
  kind: style-explainer
  version: "1.0.1"
  video: codegen-showcase
  pair: codegen-showcase-series-planner
  source: "G:/AI/视频分析/一些最近的想法/04/代码生成视频_15种风格"
---

# 代码生成视频 · N 种风格 · 风格 skill

从 V01（Opus 5.5 十五种风格盘点，2026-09-30 分析）学来的**盘点格式**。这支片有两样东西：格式（本 skill）和它展示的 15 个风格块（`..\..\风格量产\01_风格块与引擎分工.md`，按块查能否用 H3）。读数在 `references/style-dna.md`，原报告 `..\..\视频分析\04_风格解构.md`。

## 主配方（一切细则为它服务）

> **标题给数目和门槛 → [说明卡先亮（编号 · 名称 · 三行 · 标签）→ 一个最小单位 → 生长 → 约 63% 处一次最大的变化 → 落版静住 → 静音 + 一颗点过桥] × N → N 格总览 → 标题回扣 + 三段式金句。**

硬指标：每段 10.1–12.6 s（作品 10 s + 过桥约 0.8 s）；最大变化在段内 58–72%；段间 0 硬切、短静 −42 ~ −52 dB；每段 2–3 种颜色；说明卡 3 行、每行 ≤19 字、0 问号 0 叹号 0 第一人称。
变量：N、选哪几种风格、每支作品的题材和品牌名、音乐。

## 一、选题门

1. 可比：这 N 个能放进同一个框比吗（同题、同时长、同版式）？
2. 一点：每一个能从一个最小单位（点、滴、方块、一句话、一只手）长出来吗？
3. 成品：每一个结尾能落成"能用"的东西（字标、封面、海报、口号）吗？
4. 自证：作品名能就是它的技法吗（一笔画、一形万象、万物始于一滴）？

题例："同一场雨的 9 种画法"、"同一个字标的 12 种动效"、"同一条公式的 6 种可视化"。

## 二、每段怎么写（段卡模板）

```
#编号  作品名（= 技法）
行1 零件：用了什么（例：一根线、一种笔刷）
行2 判断：好在哪（书面克制，无问号叹号）
行3 动作链：发生了什么（A → B → C）
标签：#技术1 #技术2
画面：起点（最小单位）→ 生长 → 63% 最大变化 → 落版（字标 / 封面）静 ≥1 s
颜色：主色 + 1–2 色；编号 / 短横 / 进度条当前格 = 主色
音乐：像这个风格的一首；本段帧率：__ fps
过桥：静音 + 一颗点滑到另一侧
```

外框固定：暗底；说明栏 + 作品屏两栏，每段左右交替；底部进度条 N 格。片头一颗火星 → 大标题（数目 + 门槛）→ 碎成一颗点（约 4.5 s）；片尾全部作品缩成总览格 → 回到标题 + 三段式金句（约 8 s），只在这里说一句"怎么做的"。

## 三、出片（引用通用 skill，不在此复制）

- 推荐混合：外框、说明卡、字标、HUD、包豪斯、像素、花字这类"字和几何"用代码渲染（`G:\AI\montage\h3-agent` 的 HyperFrames / Remotion 技能；Node 依赖未装，装要用户同意），外框做一次 N 段复用；H3 只出它擅长的芯，装配合成。
- H3 芯：每段一条 10–12 s 的 T2VA，B 线多镜头模式 A，无旁白，音乐装配时加。提示词结构按 `h3-prompt-writing`（`G:\AI\视频分析\skill\4_H3提示词语法_h3-prompt-writing\`）。
- 每段的"从一点生长"和最大变化怎么设计得不像 AI：`creative-animation-treatment`（`G:\AI\视频分析\skill\2_动画创意_creative-animation-treatment\`）。
- 变体"加一个讲解员"才走 A 线，此时逐句分镜用 `h3-storyboard-writing`（`G:\AI\视频分析\skill\5_逐句分镜写法_h3-storyboard-writing\`）。
- **段间续接（一期 N 段走 B 线时）**：段 ≥2 的开头 0.917 s 是上一段末尾的重放（`h3-director`「多镜头线出片」）。本格式的过桥点正好拿来续接：每段最后约 1.3 s 让整幅缩成一颗点、落在近黑底上；下一段 `[Shot 1]` 写"这颗点还在"，新风格从 `00:01.217` 长出来。段 1 写 10 s，段 ≥2 写 11 s（吸附 11.542 s，去掉续接头后 10.625 s）。没出过片：先只跑两段草稿（样稿 `..\..\风格量产\方向01_一物N画\样稿_第001期_一只橘子九种画法.md` 方案甲）；不稳就每个芯单建一期、过桥点在代码层拼（方案乙）。
- **竖屏芯**（花字一类）：一期画幅是 16:9，H3 画不出框中框；块里写"主体留在中间三分之一"，装配时裁出 9:16、两侧模糊垫底（风格卡 15 第 8 节）。
- 芯从风格卡挑：`..\..\风格量产\风格卡\NN_*.md`（15 张，示例题统一是一盏灯笼）；古风化的块 G1–G5 在 `..\..\风格量产\_风格创新_变体卡.md`。

## 创新档怎么执行（允许的偏离）

- A：按主配方直走。
- B 母题创新：一个母题撑全片（同一颗点走完全片、猜风格、风格反串），从 `codegen-showcase-series-planner` 的母题库挑；主配方和硬指标不动。
- C 形式即内容：调 `creative-animation-treatment` 整片模式，把哲学 P1–P6 和三层表本质当不可打破的规则交给它；只接受改每期自由、作者默认最多偏离 1–2 条的方案。

B、C 写完都过「五、写完自检」。允许的偏离（偏离哪条作者默认 | 改成什么 | 什么题材用 | 出处）：
- 无旁白 | 片尾一句讲解 | 方向03 用风格讲风格的客串期 | 变体卡 V1（降为期级）
- 暗底外框 | 做旧纸面 + 竖排说明卡 | 古风子题 | 变体卡 V2（暂不立，先当期级试）
- 每段 10 s | 段 ≥2 写 11 s（含 0.917 s 续接头） | B 线一期多段 | 样稿 001

## 四、红线

段间不硬切；说明卡不用问号、叹号、第一人称；每段不超过一支作品；正片不讲"AI 怎么做的"（只片尾一句）；HUD、军事感风格不锁定任何真实地点；不说"关注 / 评论你喜欢哪种"（编号与总览格自然引出"我选 9 号"）。

## 五、写完自检（作者感觉）

1. 这 N 个能放进同一个框比吗？每个都落成成品了吗？
2. 每个都从一个最小单位起吗？一屏几种颜色？
3. 最大的一下在段内哪里？段间有硬切吗？
4. 每张卡是不是"零件 / 判断 / 动作链"？有问号叹号吗？
5. 每段各有一首音乐吗？段间有一次静吗？
