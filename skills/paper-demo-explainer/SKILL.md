---
name: paper-demo-explainer
description: "经典论文科普（Paper-demo explainer）风格 skill：每期拿一篇经典论文（香农 1948、图灵 1950、感知机、反向传播、Attention、PageRank、Diffie-Hellman、Nash、DNA 双螺旋等），讲'论文里有什么'——一个反常结果 + 一个被逼出来的公式——再做出一个观众能亲手复现的可演示物（≤30 行代码、纸笔实验、小游戏，先运行再写稿），用参与式引导先让观众做再命名，结尾留三道题并把开头空格交还。黑底、每个量一种固定颜色、一个可拖动的旋钮。Use when the user wants 论文科普 / 经典论文科普 / 压缩即智能 / 看看论文有什么再做出有趣的东西 / 把一篇论文做成可演示的短视频. Not for the general participation devices (see participation-design) or knowledge-ladder episodes that climb from a high-school tool (see knowledge-ladder-explainer)."
metadata:
  kind: style-explainer
  version: "1.1.0"
  video: paper-demo
  pair: paper-demo-series-planner
  source: "G:/AI/视频分析/一些最近的想法/09/论文科普_压缩即智能"
---

# 经典论文科普 · 风格 skill

参考片：《压缩即智能 P2：交叉熵》（3Blue1Brown，33.8 min，2026-10 分析）。只一支样片；读数与目标值见 `references/style-dna.md`。参与层用通用 skill `participation-design`，本 skill 只规定在哪里放、放几个。

## 哲学
> 一篇论文 = 一个反常结果 + 一个被逼出来的公式 + 一件你今天就能亲手做的事。

## 主配方（纲）
> 反常结果钩子（论文凭证 ≤3 s）→ 让你先猜/先做 → 降到一个旋钮 → 公式逐项点亮、讲成"被逼的" → 回到论文看它怎么用 → 今天的影子 → 你亲手做出一个东西 → 翻转 → 三道题 + 交还开头空格。

细则与配方冲突时配方赢。

## 执行标准（目）
- 钩子 ≤8 s，给结果不给题目；冷开场两个同构小实验：一个必中、一个必不中。
- 每段：让你做 → 画出你的状态（剩余可能 / 仪表）→ 揭晓变金 → 才命名 → 推到生活；段末一句是下一段的问题。
- 画面：黑底；颜色身份全线固定（白对象 / 金答案 / 青猜测 / 红超标 / 绿极限）；彩色 ≤1/6；一屏 ≤4 色；全期一个旋钮。
- 必然性一处，模板：需求 → 形状 → 无数候选 → 加一条愿望 → 只剩一个。
- 关键句一句，开头命名 + 结尾各一次。
- 可演示物先写、先运行；片中所有数字来自运行输出，并在稿末附实测表；代码评论区置顶。
- 约 70–75% 处一次翻转（推翻观众刚建立的判断）。
- 收尾三题：简单 / 动手 / 开放；最后一镜交还开头物件。
- 节奏：8 段、4–5 min、≥14 事件/分、静止 ≈1/3。

## 工作流
1. 从选题库/方向路线图取一篇，写"论文里有什么"备忘：反常结果、被逼的公式、今天的影子（不上屏）。
2. 写并运行可演示物，拿到数字。
3. 用 `participation-design` 排参与 beat（回扣物、仪表、留白秒）。
4. 按总指导 §4.3 写 ② 章；中文画面守 `h3-storyboard-writing` §0；精确文字/数字/公式交代码层。
5. ③ 章：风格块用 `references/style-dna.md` Part B 的颜色；visual_en 按 `h3-storyboard-writing` §2；新手法按 `h3-prompt-writing`。
6. 跑样稿末尾自检清单。

## 资料
- 分析：`../../视频分析/01–04`
- 读数与目标值：`references/style-dna.md`
- 选题库 45 篇：`../../风格量产/01_经典论文选题库.md`
- 方向：`../../风格量产/方向1_AI的祖宗们/`、`方向2_互联网的地基/`、`方向3_一页纸改变世界/`（各含 `_选题路线图.md`）
- 满配样稿：`../../风格量产/03_样稿_香农1948_猜下一个字.md`；配套代码 `../../风格量产/方向1_AI的祖宗们/03_样稿配套_shannon_guess.py`
