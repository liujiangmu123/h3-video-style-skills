---
name: codegen-showcase-series-planner
description: "Plan 代码生成视频·N种风格 series topics — the topic skill (选题 skill) for the 'one frame, N different cores' showcase format: decide what goes into the frame (one everyday thing × N styles / one dot's life act by act / a style telling its own story), pick the N cores from the 15 style cards by engine (H3-led or hybrid first; code-led cores wait for the engines), rate directions with the format's gates (comparable / grows from one unit / lands as a finished piece / name = technique), five fit questions, H3 producibility and pool depth, keep the ledger and the overlap rules with 望海潮 / 唐伯虎 / 深海 / 01 / 06, the copyright rules (never remake the reel's 15 works, names or wordmarks), and write task messages for codegen-style-showcase. Use when the user asks 代码生成视频·N种风格 / 一物N画 / 风格盘点 做什么选题 / 方向 / 路线图 / 任务消息, or whether a topic fits. Not for writing cards or H3 prompts (that is codegen-style-showcase)."
metadata:
  kind: style-planner
  version: "1.0.0"
  video: codegen-showcase
  pair: codegen-style-showcase
  source: "G:/AI/视频分析/一些最近的想法/04/代码生成视频_15种风格"
---

# 代码生成视频 · N 种风格 · 选题 skill（series-planner）

研发线用：由 `h3-research-director` 第 ④ 步调用。本技能只决定"做什么"（框里放什么、选哪 N 个芯、怎么排季），不写说明卡、不写提示词（那是风格 skill `codegen-style-showcase`）。判断一个题合不合适，用的是风格 skill 的哲学：**用同一个框装 N 种完全不同的芯，每一种都从一个点长成一个能用的成品，让观众自己去比。**

## 方法

六阶流程、三个一票否决、爆火六力、星级判定树、每期字段、撞题、任务消息骨架、合规红线按 `h3-research-director` 的 planning-method 走；完整实例看 `shenhai-series-planner`。本技能只存这条线专有的判据、规则、数据和台账。

## 三元组（每期必须写得出）

**题（放进同一个框的那一个东西 / 故事 / 风格）× N 个芯（每个芯写得出：最小单位 → 约 63% 的最大变化 → 成品落版）× 引擎分工（每个芯标 H3 / 代码 / 混合；H3 为主和混合的要占多数）**。写不全的不进库。

例：一只橘子 · 9 个芯（03 扁平：一颗橙色圆点 → 切开成一轮太阳 → 一张果汁海报；14 液态：一滴橙汁 → 三滴融成一团 → 立着的橙色水滴；……）· 9 个全是 H3 为主或混合 →《一只橘子，九种画法》。

芯从 15 张风格卡里挑：`风格量产\风格卡\NN_*.md`（每张有 H3 风格块、10 秒节拍、试片词、引擎分工）；总表与"H3 / 代码 / 混合"判定在 `风格量产\01_风格块与引擎分工.md`；古风化的风格块 G1–G5 在 `风格量产\_风格创新_变体卡.md`。

## 方向轴与来源

一期的单位看方向（planning-method 第五节）：

| 方向 | 一期的单位 | 轴 | 池深线 |
|---|---|---|---|
| 方向01 一物 N 画 | 一个日常的东西 × N 种画风 | 题材轴 | ≥50 |
| 方向02 一颗点的一生 | 一个故事 × 每一幕一种画风，一颗点贯穿 | 叙事轴 | ≥100 |
| 方向03 用风格讲风格 | 一种风格用自己的样子讲自己 | 题材轴（风格数有限） | ≥50，在线附近 |

候选来源：B 站"不同画风的 X，你最喜欢哪一个"一类（取证 §3，同一 UP 主多条 95–181 万）；logo 演绎、MG 合集（§4）；风格美学混剪与风格史（§5）；古风化需求（§7）。证据全在风格线 `视频分析\分析素材\联网取证_2026-09-30.md`。

## 规则（专有，优先于评分）

1. **不复刻 V01**：不用它的 15 支作品、作品名、字标、口号、说明卡原文（ISOPOLIS、popwise、ATELIER LINEA、NOGGIN、Aurora、NEON DRIVE、PIXEL QUEST、drop 等）；不做"H3 能做到商用水准的 N 种风格"这种照搬盘点（F07 出局）。只学格式和风格做法；风格本身（包豪斯、Synthwave、像素……）可以用。
2. **不借产品名**："Opus 5.5""Claude"不进标题，不暗示官方；本库的片是 H3 做的，不说"由 Opus 做"。
3. **先挑 H3 能做的芯**：代码为主的 6 种（02、04、07、10、11、13）要等 HyperFrames / Remotion 安装（要联网、要用户同意）。在那之前每期只用 H3 为主（05、06、09、12、14）和混合（01、03、08、15）的芯，外框、编号、说明卡、落版字标用 ffmpeg 叠（不等代码引擎）。
4. **不画 IP 和真人**：不画在世名人、他人 IP 角色（例：湘灵手绘画过的游戏角色那类）；综艺花字不用真人和明星素材；HUD 不锁定真实地点、坐标、军事设施。
5. **撞题让位**：子题碰到城市、诗词让望海潮，节日、老字号让唐伯虎；一首歌 N 种画风让 01 线；界面史、颜色史、形变单风格让深海；拼贴单风格让唐伯虎；每个知识点配画风让 06 线。

## 风格契合判据

选题门、契合题、H3 可生产性、六力改写、专有否决、已判不做的方向在 `references/fit-criteria.md`。

## 领域套件

每个方向的题怎么选、芯池、排序、落版、比较轴与风险在 `references/domain-kits.md`（不写 hex）。

## 台账

| 方向 | 星级 | 状态 | 已产期数 | 资料位置（风格线 `风格量产\`） | 顺序 |
|---|---|---|---|---|---|
| 方向01 一物 N 画 | ★★★★★（有条件：每期只用 H3 为主 / 混合的 6–9 种芯） | 路线图 12 期；样稿 001《一只橘子，九种画法》（B 线 9 段试片词，过 `h3_lint`） | 0（未出片） | `方向01_一物N画\` | 1 |
| 方向02 一颗点的一生 | ★★★★☆（F1 3：每幕不在同一个框里；F3 3：中间幕不落成成品） | 路线图 6 期种子 | 0 | `方向02_一颗点的一生\` | 2 |
| 方向03 用风格讲风格 | ★★★★（池深 40–60 种常用风格，在线附近；做客串） | 路线图 6 期种子 | 0 | `方向03_用风格讲风格\` | 3（客串） |
| 十秒品牌片（F04） | ★★★ | 不建文件夹，接单作品集 | — | — | 用户要接单时 |

评级明细与否决清单在风格线 `风格量产\00_领域总览.md`。池深：方向01 题材不限（已列 14 个起），方向02 估 ≥100，方向03 约 40–60——**都是估算**，开工种子包要逐方向枚举。

**撞题分工**：本线是"比"的格式，不讲知识、不讲故事情节（方向02 例外：故事只是一条线，靠画风换幕）。与 02 网文线方向的"一生"分工：02 是说书旁白 + 一种画面，本线无旁白、每幕换风格。15 个风格块同时是全库的画面候选库，别的线 ③ 配画面时借用不算撞题。

## 创新档与母题库

每期标创新档 A / B / C；执行写法在 `codegen-style-showcase`「创新档怎么执行」。

- B 档母题库（母题 | 适合的方向 / 期 | 用过的期号 | 效果）：
  - 猜风格（总览格前最后一题：先出一段不给说明卡，让观众猜是几号的风格）| 方向01 | — | 未出片（原 F25 并入）
  - 风格反串（用一种风格讲一个和它气质相反的题）| 方向03 客串期 | — | 未出片（原 F27 并入）
  - 同一颗点走完全片（片头那颗点就是第 1 号的最小单位，片尾回到它）| 方向01 / 02 | — | 未出片
- 变体与杂交登记（名称 | 程度 | 结论 | 理由 | 立了的 skill 名）：
  - V1 加一个讲解员（A 线）| 2 | 降为期级 | 作品集的克制没了一半；五问第 4 问没有方向因此升五星；方向03 客串期可试一句讲解 | —
  - V2 古风外框（做旧纸面 + 竖排说明卡 + 古风化芯）| 2 | 暂不立 | 撞望海潮 / 唐伯虎的子题；五问第 3 问 G 系列风格块未上 H3 | —
  - G1–G5 古风化风格块 | — | 不是本格式的变体，是风格块的派生 | 给 01 / 02 / 05 / 06 线 ③ 配画面用 | —
  - 卡片在风格线 `风格量产\_风格创新_变体卡.md`。

## 查证

爆款实证与事实查证要联网：Pi 没有联网搜索，这一步在 Kiro / Cursor 里做，结论写回路线图"注记"。每期写稿前查：题有没有 IP / 商标（画一个品牌的标志性产品不行）；同题的"不同画风"视频有没有人做过（做过就换题或换芯）；落版要叠的字标名字是不是别人的商标。

## 任务消息

本风格专有部分与可粘贴的模板在 `references/output-templates.md`；通用骨架见方法文件第八节。
