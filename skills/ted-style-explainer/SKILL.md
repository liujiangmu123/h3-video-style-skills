---
name: ted-style-explainer
description: "Generate TED演讲·技术科普 style episodes with MiniMax H3 — the style skill (风格 skill): one talk, one idea, one checkable fact. Opens on a concrete first-person dilemma with the object in one warm spotlight; the object makes one small decision; a 'not A but B' flip at 45–65%; the idea named only after the demo; a three-step number ladder from the original research; one concession; the choice handed back ('the step you can take' + an honest either-or question); a static source card (speaker · event · year). Dark stage, faceless wooden figure as 'you', no speaker likeness, no TED logos, no applause or inspirational music. A-line (voice-first timecode). Use when the user wants TED风格 / 演讲观点科普 / 一个观点一个数字 / turning a talk into this format, or asks how this line writes narration, picture lines or H3 prompts. Topics: ted-series-planner."
metadata:
  kind: style-explainer
  version: "1.0.1"
  video: ted
  pair: ted-series-planner
  source: "G:/AI/视频分析/一些最近的想法/03/TED演讲_技术科普"
---

# TED 演讲 · 技术科普 · 风格 skill

学的是两层叠起来的东西：图文作者"靓女落泪我心碎"从 17 分钟演讲里挑 25 句的编辑手法 + TED 讲法本身（Duneier 场为样本，Anderson、Duarte 两场做尺子）。画面、画面节奏、声音是本线 ③ 配的（原作只有截图），数值是目标值。读数在 `references/style-dna.md`，原报告 `..\..\视频分析\04_风格解构.md`，画面配对见 `..\..\风格量产\01_画面配对与产线.md`。

## 主配方（一切细则为它服务）

> **困境一句（我 / 你，一个具体时刻，那件东西已经在光里）→ 转机一句 → 演示：那件东西做一个小决定（一次只动一件）→ 翻转金句（不是 A，而是 B）→ 命名观点 → 三级证据（能核的数字阶梯）→ 让步一句 → 交回：你能做的那一步 + 二选一问题 → 出处卡（讲者 · 场次 · 年份）。**

硬指标：观点 1 个；物件 ≤3 件 + 一个代表"你"的小人；证据 3 级每级一句；问号 ≤2（中段最多一个设问 + 结尾一个二选一，前两句没有）；翻转句在 45–65%；出处每期必出；长版 5 段约 150 s 约 500 字，抖音版 3 段约 60 s 约 200 字；句长 8–15 字，3.5 字/秒。

每期换：困境时刻、物件、翻转的两个词、数字、问题的两边、讲者与场次。不换：段序、证据三级、出处卡、口吻、光。

## 一、选题门

1. 一句话：能压成"不是 A，而是 B"吗？
2. 手边：观点能落到观众手边的一个时刻、一件物、一个小动作上吗？
3. 可核：有没有一个能联网核实的数字、研究或事实（回原始研究，不只取自演讲）？
4. 自己说：不照搬演讲故事顺序和原话，用原始资料和自己的例子能讲清吗？

## 二、旁白写法

| 段（长版） | 占比 | 句数 | 写法 |
|---|---|---|---|
| 1 困境 | 15% | 2–3 | 陈述句 8–15 字，"我 / 你"开头，一个具体时刻 + 转机 |
| 2 演示 | 25% | 3–4 | 那件东西做一个小决定，旁白给方法；动作链句式 |
| 3 翻转 + 命名 | 15% | 2–3 | 不是 A 而是 B；观点在演示之后才说出 |
| 4 证据 | 25% | 3–4 | 三级数字 + 让步"不是说容易" |
| 5 交回 + 出处 | 20% | 2–3 | 你的那一步、二选一、"这是 X，在某年 Y 讲的。" |

抖音版：困境 + 翻转 / 证据三级 / 交回 + 出处。
口吻：谦逊，"也许 / 可能"；人称"我 → 你 → 他 → 每个人"；不命令、不夸讲者、承认限制。不说"大家好""今天分享一个 TED""关注我""感谢观看"。讲者个人故事最多两句。

## 三、画面、节奏、声音（③ 配）

- 画面：暗场 + 一束暖色追光，被光照到的才存在；观点由手边物件演（手机、沙发、闹钟、AI 对话框）；一个无脸木质小人代表"你"；桌面微缩尺度、真材质（木、布、纸）；数字写在背板上；底部 1/5 留空给字幕；一次只有一件东西在变。
- 节奏：困境句画面静；观点落在一个决定性动作上；证据一级一级亮；静止句 ≥1/3；每段 2–4 个事件；最长静止在交回问题之前。
- 声音：物件发自己的材质声；翻转前一拍静；只有房间底噪；证据声逐级升一点；无掌声、笑声、励志配乐。
- 出片：A 线配音先行时间码。逐句中文画面 → 英文分镜用 `h3-storyboard-writing`（`G:\AI\视频分析\skill\5_逐句分镜写法_h3-storyboard-writing\`）；H3 提示词结构用 `h3-prompt-writing`（`G:\AI\视频分析\skill\4_H3提示词语法_h3-prompt-writing\`）；钩子帧、演示动作要有创意时用 `creative-animation-treatment`（`G:\AI\视频分析\skill\2_动画创意_creative-animation-treatment\`）。

## 四、红线

1. 不截取、转载、配音、翻译任何 TED / TEDx 视频、音频、字幕、文字稿。
2. 不出现 TED / TEDx 字标、红圆地毯 + 红大字舞台、片头片尾。
3. 不生成讲者肖像或声音。
4. 不把"TED"当品牌用；出处卡写"观点来自 X 在 Y（场次，年份）的演讲"可以。
5. 不照演讲故事顺序复述。
6. 不命令、不骂观众、不夸讲者。
7. 医疗、心理、理财、育儿只讲研究结论，不给个人建议，不承诺效果。
8. 陈词黑名单：灯泡、火箭、台阶山峰（字面爬山除外）、拼图、发光大脑、网络节点、漂浮粒子、矩阵数字雨。

## 五、写完自检（作者感觉）

1. 只有一个观点吗？站在一个能核的事实上吗？
2. 画面是观众手边的东西吗？只有一件在变吗？讲者和商标出现了吗？
3. 困境句停了吗？观点落在一个动作上吗？证据一级一级来吗？
4. 第一句是具体时刻吗？有一句翻转吗？结尾交回了吗？出处说了吗？
5. 有掌声、笑声、配乐吗？翻转前有静吗？
