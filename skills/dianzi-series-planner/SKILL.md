---
name: dianzi-series-planner
description: "Plan 电子智人参与式科普 (Dianzi participatory explainer) series topics — the topic skill (选题 skill): finds directions on the experience axis (one episode = one phenomenon the viewer can live through on themselves: a blank they can or cannot fill, a number they guess, a scrambled line they still read, a vote that turns out wrong), rates candidates with the style's four gates (do it first / form is content / shared everyday experience / hand it back), the viral six forces and pool depth, writes per-episode triples (self-experiment × meter × hand-back action), roadmaps and task messages for the style skill dianzi-style-explainer. Use when the user asks 电子智人风格 / 参与式科普 做什么选题 / 方向 / 选题池 / 路线图, or whether a topic fits this guided-participation format. Not for writing captions, narration or H3 prompts (that is dianzi-style-explainer)."
metadata:
  kind: style-planner
  version: "1.1.1"
  video: dianzi
  pair: dianzi-style-explainer
  source: "G:/AI/视频分析/一些最近的想法/15/电子智人_无旁白参与式科普"
---

# 电子智人参与式科普 · 选题 skill（series-planner）

研发线用：由 `h3-research-director` 第 ④ 步调用。本技能只决定"做什么"（方向、选题、路线），不决定"长什么样"，不写旁白、不写提示词（那是风格 skill `dianzi-style-explainer`）。判断题材合不合适，用的是风格 skill 的哲学与三层表本质。

## 方法

六阶流程、三个一票否决、爆火六力、星级、每期字段、撞题、任务消息骨架、合规红线按 `h3-research-director/references/planning-method.md` 走；完整实例看 `shenhai-series-planner`。本技能只存这个风格专有的判据、数据和台账。

## 风格契合判据

选题门 G1–G4、本质改写的契合题、专有否决在 `references/fit-criteria.md`。一句话：**找不到观众能在自己身上当场经历一次的入口，就不是这个风格的题。**

## 三元组

每期条目另带两项（⑦ 盲测后加）：**产线**（H3 / 代码 / 混合——错觉材料、模拟计数这类必须一像素不差的题标"代码"或"混合"，判据见风格 skill「代码动画线分支」）与**声音母题**（观众出力那一刻的音）。孪生实验会剧透答案时（如三扇门 / 一百扇门），在条目里注明"孪生实验挪 2/3"，风格 skill 已列为允许的偏离。参与装置的通用判据引用共享技能 `participation-design`，本技能不复制。

每期必须写得出：**亲身实验 × 仪表 × 交还动作**。
- 亲身实验：两个同构的小实验最好（一个必中、一个必不中）；每章再有一个入口实验。
- 仪表：把观众脑子里的状态画成看得见的东西（剩余可能、惊奇 bits、置信度条、你的票 vs 真相、记忆格子）。
- 交还动作：结尾留给观众自己完成的一件事。
写不出亲身实验的不进库；写不出交还动作的可进库，标"无交还"。

## 方向轴与来源

**体验轴**：一期的单位 = 一个观众能当场经历的现象；学科只决定例子。池深线 ≥40 期。

候选来源：认知心理学经典实验（知觉、记忆、注意、决策偏差）；概率与统计悖论清单；信息论 / 算法 / 密码入门教材的"课堂小游戏"；语言学与汉字现象；诗词炼字；AI / 大模型原理（填空、温度、注意力、幻觉）；电影剪辑的观众实验（库里肖夫）；平台上"测一测 / 你能看出来吗"类爆款话题（只借入口，不借结论）。

## 领域套件

每个立项方向的舞台物、仪表、共同经验、合规点在 `references/domain-kits.md`（不写 hex）。

## 台账

| 编号 | 方向 | 星级 | 状态 | 已产 | 资料位置 |
|---|---|---|---|---|---|
| A | AI 只做一件事（大模型原理） | ★★★★★（待实证） | 路线图 12 期，001 样稿已过 parse_md、盲测 90/120 | 样稿 1 | 风格线 `风格量产\方向A_AI只做一件事\` |
| B | 你的大脑被骗了（知觉记忆注意偏差） | ★★★★★（待实证） | 路线图 12 期，001 盲测样稿 93/120；产线宜"混合"或代码线 | 样稿 1 | `风格量产\方向B_你的大脑被骗了\` |
| C | 直觉投票站（概率统计悖论） | ★★★★★（待实证） | 路线图 12 期，001 盲测样稿 92/120；产线宜"混合" | 样稿 1 | `风格量产\方向C_直觉投票站\` |
| — | 信息与压缩 / 诗词炼字 / 一个算法一个游戏 / 行为经济学 / 密码 / 语言直觉 | ★★★★–★★★★☆ | 作穿插单期 | 0 | `风格量产\00_领域总览.md` |

撞题分工：A 与深海 28 机器学习原理、09 论文科普线；B 与深海 43 心理学实验档案、04 电影视听语言（库里肖夫只做 1 期）；C 与深海 30 统计学与统计陷阱。本线只讲"观众亲身经历的那一下"，不讲推导、论文、故事；片尾互导。

## 创新档与母题库

每期标创新档 A / B / C（定义见方法文件第六节）；执行写法在 `dianzi-style-explainer`「创新档怎么执行」。

- B 档母题库：
  - 贯穿残句 | 方向 A 全系列 | — | 同一行残句每期换一个空
  - 你的票 vs 真相 | 方向 C 全系列 | — | 投票槽与模拟计数
  - 注意力光圈 | 方向 B 003、009 | — | 光圈之外的东西被"看不见"
  - 同一行字链 | 方向 A 003 | — | 字链越来越长，开头逐渐变暗
- 变体与杂交登记（研发线 ⑤，详见风格线 `风格量产\_风格创新_变体卡.md`）：
  - V1 配音参与版 | 程度 1 | 降为期级（已写进风格 skill 允许的偏离） | 只换声音层 | —
  - V2 纸墨参与版（米白纸面 + 墨线） | 程度 2 | 暂不立 | 题材是纸、书法、印刷时才有意义，先做 1 期期级 | —
  - V3 深海 × 参与（深海画布 + 一问一停） | 程度 3（杂交） | 暂不立 | 动了深海本质"≤1 问号、冷开场陈述句"；先在深海 04 优化版试陈述句版参与装置 | —

## 查证

爆款实证与事实查证要联网：Pi 没有联网搜索，这一步在 Kiro / Cursor 里做，结论写回路线图的"查证要点"。本轮三个方向的五星都是"待实证"：立项前每方向补 ≥15 条带平台、账号、播放量级的实证（重点搜：抖音"Vibe 知识大赏"、B 站"你能看出来吗 / 测一测"类、3Blue1Brown 与 Veritasium 中文搬运、"大模型原理 科普"）。

## 任务消息

本风格专有部分（必读文件、锁定参数、字数口径、特殊红线）在 `references/output-templates.md`；通用骨架见方法文件第八节。
