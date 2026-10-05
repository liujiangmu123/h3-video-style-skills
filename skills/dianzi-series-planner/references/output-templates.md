# 任务消息（本风格专有部分）

通用骨架见 `h3-research-director/references/planning-method.md` 第八节。这里补：

- 必读文件：`dianzi-style-explainer` 全文与 references（它的 SKILL.md「哲学」「主配方」「作者感觉」「产线路线」「交付格式」必读；`dianzi-style-explainer/references/narration.md`、`dianzi-style-explainer/references/beat-templates.md`、`dianzi-style-explainer/references/style-dna.md` A′ 必读）；`h3-storyboard-writing`（写中文画面时守 §0）；参与装置的通用写法 `participation-design`。
- 锁定参数：A 线；长版 120–240 s（3–5 章）、16:9；抖音版 55–70 s、9:16；字幕版为默认（配音只当时钟，交付 `h3_deliver tier="2k" audio="segment" subtitles="burn"`）；字数口径：句数由章模板定，每句 13–20 字，句末停顿 `<#秒#>` 按风格 skill narration.md §9 公式补到目标在屏时长（这个写法现在有已知缺陷：句末停顿会被配音层剪掉、标记会烧进字幕，见总指导 §13 第 10 条——原稿照写，修好前别真跑配音）；风格块用风格 skill style-dna A′2 并覆盖节奏目标三项。
- 每期条目必带：三元组（开场两个实验 + 每章入口实验 / 仪表 / 交还动作）、回扣物、翻转点、代码层要出的字（大致）、创新档、查证要点（论文或数据出处）。
- 特殊红线：不在体验前给术语；不问考试题；无人物、无 logo；会被读的长字一律代码层；不做诊断式自测、不给投资建议。

## 任务消息模板（本风格）

```text
【任务】按 dianzi-style-explainer 写 {方向} 第{NNN}期《{标题}》原稿（长版 + 抖音版），A 线 §4.3 格式，字幕版。
【先读】dianzi-style-explainer（SKILL.md 全文 + references 全部）；h3-storyboard-writing §0；participation-design；G:\AI\H3动画量产_AI总指导.md §4.3；本方向 _选题路线图.md 第{NNN}行；本方向 001 样稿与 风格量产\_盲测报告.md（格式与已知偏差）。
【本期】产线：{H3/代码/混合}；声音母题：{…}；开场两个实验：{必中} / {必不中}（孪生会剧透时注明"挪 2/3"）；仪表：{…}；每章入口实验：{…}；翻转：{…}；交还：{…}；回扣物：{…}；创新档：{A/B/C}；查证：{出处}。
【交付】一份 MD：① 选题信息与查证（含代码层清单）→ ② 长版旁白时间轴 → ④ 抖音版旁白时间轴 → ⑥ 自检（按风格 skill 自检表 + 作者感觉对照）。确认能解析：Pi 里临时系列 `h3_new_episode md_path=<原稿> storyboard=true` 看句数和（静止）句对不对；Kiro / Cursor 里在 G:\AI\h3-pi-agent\bridge 下用 G:\AI\envs\minimax-h3\python.exe 调 `h3_storyboard.parse_md(原稿全文)`。
```
