---
name: xuezhong-style-writing
description: "Write original ancient-setting short stories in the 雪中悍刀行 web-novel brush (雪中写法) — the style skill (风格 skill) for this line: open on a long worldly / weather / place sentence with the callback object shown once, two people trade dialogue with one real laugh, a bystander's silence at 65–75%, then the climax as one line or gesture of someone LEAVING (not winning), one line of everyday life, 3–5 closing sentences of ≤10 characters, and the last line is the title. Storyteller voice: declarative, laughing, an occasional '其实', emotions as actions, no questions, no emotion adjectives. Writes the full short story (800–1500 字 图文版) first, then compresses it into a 250–650 字 A-line narration with H3 pictures. Use for 雪中风格 / 网文写法 / 说书人口吻古风短篇 / 先笑后走的故事, or the story layer of 古风歌曲一歌一故事. Topics: xuezhong-series-planner. Never uses the novel's characters, places or sentences."
metadata:
  kind: style-explainer
  version: "1.0.1"
  video: xuezhong
  pair: xuezhong-series-planner
  source: "G:/AI/视频分析/一些最近的想法/02/网文写法_雪中悍刀行"
---

# 雪中悍刀行写法 · 风格 skill

从《雪中悍刀行》全书文本统计 + 名场面精读学来的**写法**（2026-09-30 分析）。产出是原创人物的古风短篇，再配 H3 画面。这条线**纯写作**：画面、节奏、声音由研发线 ③ 配。读数与证据在 `references/style-dna.md`，原报告 `..\..\视频分析\04_风格解构.md`。

## 主配方（一切细则为它服务）

> **世情 / 天气长句铺场（回扣物露一次）→ 两人对白往来、带一个笑点 → 65%–75% 一次静后落高潮（一句台词或一个动作）→ 回一句日常 → 最后 3–5 句每句 ≤10 字单独成句（物件、评语）→ 最后一句说出标题。**

硬指标：段长 / 句长单调变短不回升；高潮在 65–75%，前一句是旁观者的静；结尾短句 3–5 句、每句 ≤10 字，视频版每句后停 ≥1 s；标题 = 最后一句（或其中的词）；叙述问号 ≤1；情绪形容词 0。

## 一、动笔前：过四道门 + 定五个变量

| 门 | 问 | 不过就 |
|---|---|---|
| 离场 | 有没有一个人要"走"（离开、放下、老去、死）？ | 不做 |
| 小物 | 有没有一件便宜、旧、拿得住的东西扛住结局？ | 不做 |
| 先笑 | 前半段能放一个真笑点吗？ | 改题 |
| 一句 | 最后一句能 ≤10 字又能当标题吗？ | 改结尾 |

变量（每期自选）：谁走、什么物件、开头用哪种（地方 / 天气 / 世情）、笑点是什么、最后那句是台词还是叙述。只写古代：驿卒、镖师、戏班、窑工、军伍、市井、父子师徒都行。

## 二、按比例写（结构）

| 段 | 比例 | 视频 90 s | 写法 |
|---|---|---|---|
| 铺场 | 0–20% | 0–18 s | 1–2 句长句，不问不喊；回扣物露一次 |
| 往来 | 20–65% | 18–58 s | 对白 + 叙述者插一句"其实"+ 笑点 |
| 高潮 | 65–75% | 58–68 s | 前一句静；一句台词或一个动作；写"走"不写"赢" |
| 回落 | 75–85% | 68–76 s | 一句日常 |
| 余味 | 85–100% | 76–90 s | 3–5 句 ≤10 字，最后一句 = 标题 |

长版（180 s / 600–700 字）同比例放大，不加第二个高潮。

## 三、句子层（口吻）

- 说书人可以站出来评一句，但不下断言：多用"似乎 / 大概 / 其实"，"只是 / 不过"口癖。
- 情绪写动作：不写"他很伤心"，写他把酒坛往怀里拢了拢。
- 叙述不问不喊；问号留给对白。
- 文白混搭，官职、地名、数字写实（借真实朝代制度做底），给虚构世界分量。
- 字里的声音少而准（"猎猎作响"），可直接转 sfx。
- 名字是承诺：标题和关键称呼留到最后才说出。

## 四、先写小说，再压视频

1. 先写完整短篇（图文版 800–1500 字，就是 3 张长图的原文）。
2. 再压成视频旁白：90 s ≈ 315 字、150 s ≈ 525 字（秒数 × 3.5）；保留铺场长句、笑点、静、高潮、短句收，删往来里的枝节。
3. 视频走 A 线配音先行：每句一个画面，按句钉时间码。逐句中文画面 → 英文分镜用 `h3-storyboard-writing`（`G:\AI\视频分析\skill\5_逐句分镜写法_h3-storyboard-writing\`），H3 语法用 `h3-prompt-writing`（`G:\AI\视频分析\skill\4_H3提示词语法_h3-prompt-writing\`），画面发明用 `creative-animation-treatment`（`G:\AI\视频分析\skill\2_动画创意_creative-animation-treatment\`）。
4. 画面默认借望海潮"画面"行（雾、逆光、小人物、背影、远—近—物），不借它的节奏；轻喜剧期借唐伯虎纸艺材质。一场一种强调色，写背影和旁观者的脸，不写主角哭的正脸；越往后镜头越短，最后几句一句一镜。
5. 产线参数（建期后、写英文拍前设）：
   - 风格块按 `h3-storyboard-writing` §6 写有世界的档位（满配八槽见 `h3-prompt-writing` creative-compile §7），**不用默认深海块**（米白底 + 图标）；人物只登记背影、手、侧影，`no_voice_en` 照改。
   - 节奏目标（暂定）：`target_events_per_min` 9（按主配方推：一句一事件、静止句约 1/4），`target_motion_share` 与 `max_still_p50_s` 先设 0（不查）。参考源是小说，没有可量的成片节奏；"越往后越短"用自检第 3 问查。首期两段草稿后按 `h3_align` 成片读数回写这里。
   - 结尾短句后的停（≥1 s）、高潮前的静：句末写 MiniMax 停顿 `<#1#>`。⚠ 现在配音层剪首尾静音会把句末停顿剪掉，修好前看 `G:\AI\H3动画量产_AI总指导.md` §13 第 10 条。
   - 抖音版用一句江湖写法（约 30 s、6 句，最后 3 句每句 ≤6 字），和长版是同一个栏目。

## 创新档怎么执行（允许的偏离）

- A：按主配方直走。
- B 母题创新：用选题 skill 母题库里的一个母题（季末回扣季初、父子 / 家书、不出手）撑整篇；主配方和硬指标不动。
- C 形式即内容：调 `creative-animation-treatment` 整片模式，把哲学 P1–P6 和三层表本质当不可打破的规则交给它；只接受改每期自由、作者默认最多偏离 1–2 条的方案。

B、C 写完都过「七、写完自检」。允许的偏离（偏离哪条作者默认 | 改成什么 | 什么题材用 | 出处）：
- 雪、酒、剑、马 | 换成这期的日用物（算盘、豆腐、梆子、醒木） | 所有方向 | 三篇样稿
- 望海潮画面行 | 唐伯虎纸艺材质 | 市井轻喜剧期 | 方向03 第 001 期 ④ 两版对照

## 五、和 01 线的接口

01 古风歌曲线的故事按本主配方写；01 的揭示点（金句起唱）= 本线高潮点（65–75%）。01 额外要求故事贴歌、分"那时 / 现在"两层，见 `gufeng-song-story`。

## 六、红线

不写原著人物、不用原著地名作主舞台、不抄原句；不用"大家好 / 今天讲"；结尾不讲道理不喊口号；不用情绪形容词代替动作；不开头上高潮、不一期两个高潮；标题不在开头解释；只写古代；一篇一个完整故事，不写连载、不"下回分解"。

## 七、写完自检

1. 这期是谁走？留下了什么？
2. 回扣物开头结尾各出现一次了吗？
3. 句子越往后越短吗？高潮在 65–75% 吗？
4. 叙述里有问号吗？有情绪形容词吗？最后一句是标题、是不是最短？
5. 最重那句前有静吗？
