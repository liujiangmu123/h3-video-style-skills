---
name: knowledge-ladder-explainer
description: "知识溯源科普（Knowledge-ladder explainer）风格 skill：从一个高中就会的工具（斜率、对数、平均数、三角函数）出发，按五级阶梯 直觉 → 工具 → 困难 → 推广 → 做出东西 爬到一个高级概念（泰勒展开、傅里叶、梯度下降、贝叶斯、信息熵、控制论），历史溯源每处一句（莱布尼茨、维纳、香农），最后让观众做出一个可复现的小项目解决开头的真问题（自制 sin 计算器、修镜头畸变、调音器）。Use when the user wants 知识溯源 / 从斜率到泰勒 / 从高中知识讲起 / 对人有用的科普 / 从见到到困难到做出东西 / AI 的设想来源. Not for single-paper explainers (see paper-demo-explainer)."
metadata:
  kind: style-explainer
  version: "1.1.0"
  video: knowledge-ladder
  pair: knowledge-ladder-series-planner
  source: "G:/AI/视频分析/一些最近的想法/06/知识溯源科普_从斜率到泰勒"
---

# 知识溯源科普 · 风格 skill

无参考视频，方法论来自用户第 6 条想法 + 卡兹克访谈摘录（"看一百个教程，不如被一个真问题逼着打一仗"）。

## 哲学
> 科普要对人有用：从见到，到困难，最后做出一个东西解决一个问题。

## 主配方（纲）
> 真问题开场（"计算器只会加减乘除，怎么算 sin？"）→ 直觉 → 高中工具 → 工具失败（困难）→ 推广出新概念（此时才命名 + 一句溯源）→ 亲手做出东西解决开场问题 → 回看阶梯 + 三道题。

## 执行标准（目）
- 困难先于概念：新名词只在旧工具失败后出现。
- 每级只跨一步，画面保留上一级的影子。
- 溯源只一句，服务"为什么有人会想到"。
- 第 5 级成果 10 分钟内可复现（≤40 行代码 / 在线工具 / 纸笔），评论区置顶。
- 至少一个可拖动参数（项数 N、畸变系数 k₁、学习率）。
- 可与 15 线 `dianzi-style-explainer` 的参与装置组合（先猜后揭晓）。

## 资料
- 方法论：`../../视频分析/01_方法论_知识阶梯.md`
- 样稿：`../../风格量产/01_样稿_从斜率到泰勒.md`
- 选题：`../../风格量产/02_溯源阶梯选题库.md`
- 路线：`../../风格量产/03_方向路线图.md`
- 配套代码（已运行，误差表在样稿）：`../../风格量产/01_样稿配套_taylor_sin.py`
- `references/ladder-template.md` — 选题卡、时长预算、颜色身份、句式库（写稿先填）
- `references/self-check.md` — 14 条自检
- `references/reference-cases.md` — 3B1B / Veritasium 核实案例与未核实事项

## 工作流
1. 从选题库取一条，填 `references/ladder-template.md` 选题卡。
2. 先写并运行第 5 级代码，拿到实测数字——片中数字只能来自运行输出。
3. 按五级写 ② 章（总指导 §4.3 格式），参与层用通用 skill `participation-design`。
4. 中文画面按 `h3-storyboard-writing` §0 写；精确曲线/数字/滑块交代码层。
5. 跑 `references/self-check.md`。
