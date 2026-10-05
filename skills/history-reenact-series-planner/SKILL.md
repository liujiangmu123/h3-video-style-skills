---
name: history-reenact-series-planner
description: "Plan 历史影视解说·H3原创重演 style series topics — the topic skill (选题 skill): find directions, rate candidates, build topic pools and roadmaps, and hand each episode to the style skill history-reenact-explainer as a task message. Use when the user asks 历史影视解说·H3原创重演风格做什么选题 / 方向 / 选题池 / 路线图, or asks whether a topic fits this style. Not for writing narration or H3 prompts (that is history-reenact-explainer)."
metadata:
  kind: style-planner
  version: "0.1.0"
  video: history-reenact
  pair: history-reenact-explainer
  source: "G:/AI/视频分析/一些最近的想法/05/历史影视剪辑_解说"
---

# 历史影视解说·H3原创重演 · 选题 skill（series-planner）

研发线用：由 `h3-research-director` 第 ④ 步调用。本技能只决定"做什么"（方向、选题、路线），不决定"长什么样"，不写旁白、不写提示词（那是风格 skill history-reenact-explainer，生产线用）。判断一个题材合不合适，用的是风格 skill 里的哲学和本质。

## 方法

六阶流程、三个一票否决、爆火六力、星级、每期字段、撞题、任务消息骨架、合规红线**不在这里重写**，按 `h3-research-director/references/planning-method.md` 走。完整实例看 `shenhai-series-planner`。本技能只存这个风格专有的东西：

## 风格契合判据

从风格 skill 的哲学导出的选题门、三层表"本质"逐条改写成的 1–5 分问题，以及本风格专有的否决项，在 `references/fit-criteria.md`。

## 三元组

待填：本风格每一期必须写得出的三样东西（深海是 原理 × 证物 × 手边物），写不出的选题不进库。

## 方向轴与来源

待填：本风格适合的方向轴（学科轴 / 叙事单元轴，或本风格自己的轴；按"一期的单位"判，见方法文件第五节）、池深线，以及本风格特有的候选来源。

## 领域套件

每个立项方向的锚点与素材套件（不写 hex）在 `references/domain-kits.md`。

## 台账

待填：已立项方向的编号 / 星级 / 状态 / 已产期数 / 资料位置（新方向立项前先查，避免重复）。

## 创新档与母题库

每期标创新档 A / B / C（定义见方法文件第六节）；执行写法在 history-reenact-explainer「创新档怎么执行」。
- B 档母题库：（暂无。每条一行：母题 | 适合的方向 / 期 | 用过的期号 | 效果）
- 变体与杂交登记：（暂无。研发线 ⑤ 评过的每个候选一行：名称 | 程度 1/2/3 | 结论 立 / 暂不立 / 降为期级 | 理由 | 立了的 skill 名）

## 查证

爆款实证与事实查证要联网：Pi 没有联网搜索，这一步在 Kiro / Cursor 里做，结论写回种子包的"查证要点"。

## 任务消息

交给 history-reenact-explainer 的任务消息里本风格专有的部分（必读文件、锁定参数、字数口径、特殊红线）在 `references/output-templates.md`；通用骨架见方法文件第八节。
