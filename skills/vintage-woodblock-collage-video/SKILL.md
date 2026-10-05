---
name: vintage-woodblock-collage-video
description: >-
  Writes vintage East-Asian woodblock-print paper-collage animation shorts for MiniMax H3: silhouette-and-beauty vignettes on aged tinted xuan paper, where scene changes are paper / ink material transitions (full-screen recompositions), never camera cuts; paper tint, materials and ritual color are derived per story. Maps a story or IP (two-character encounter or folk tale; optional title, duration, ratio) onto the locked seven beats (title → encounter → ink-splash → focal gesture + beauty close-up → interior dance → brush wipe → fan-close and silent seal) and writes one complete English H3 T2VA / I2VA multi-shot prompt with a near-silent paper-rustle bed and sparse guzheng / pipa plucks on a 50 BPM grid. Use for 复古木版画拼贴 / 纸艺拼贴动画 / 剪影爱情小品 / 唐伯虎点秋香风格 / 做旧宣纸动画. Not for the voice-first timecode pipeline, live action, 3D CG, dialogue-heavy or multi-minute stories, or topic planning.
metadata:
  trigger-words: "复古木版画拼贴视频，纸艺拼贴动画，剪影爱情小品，唐伯虎点秋香风格，浮世绘拼贴风，做旧宣纸动画，水墨拼贴提示词，H3拼贴风格视频"
  kind: style-explainer
  video: vintage-woodblock
  version: "1.2.0"
  source: "G:/AI/视频分析/唐伯虎点秋香_复古版画拼贴/视频分析"
---

# 复古木版画拼贴动画视频提示词生成器

> **产线归属**：本线**不是**配音先行 / 时间码产线——不要为它调用 `h3_new_episode` / `h3_storyboard` / `h3_timecode` / `h3_align`；配音先行的写词规则（`h3-director` 写词铁律、`h3-storyboard-writing`）也不适用于本线，H3 字段语法直接按官方 `h3-prompt-writing`。这里的多镜 `[Shot N]` 写法与由 H3 生成的配乐是本线的**有意例外**（配音先行线不生成 BGM）。
>
> **在 H3-pi-agent 里出片**：整支短片写成原稿 `## 长版 · H3 分段提示词` 章下的一段 `### 第 1 段 · 标题（T2VA，15s）` + 一个代码块装整段英文提示词（超过 15 s 就按拍拆成几段）；建期、出片、交付按 `h3-director`「多镜头线出片」（模式 A，交付 `audio="segment"`）。产线只做 T2VA；I2VA 需要参考图，只用于脱离产线的单独生成。

## 主配方（哲学＝这条可复述的主线；一切细则为它服务）

> **一句话选题（两方＋一件信物＋一个小情节）→ 七拍走完（标题拼贴→两方相遇递物→泼墨强调→月下点睛与美人位工笔特写→图案化内景对场→笔刷横扫清场→信物亮题收合＋静默盖印定格）；剪影位＝行动方、美人位＝被点亮方，纸底与材料按故事世界选材（选材不选色），一切运动过真纸测试。**

配方的三个开放槽位就是扩展入口：**剪影位**（行动方——才子/农人/画师/匠人/掌柜）、**美人位**（被点亮方——人、产品、文物、节气物候皆可坐位，坐位者获得全片唯一一次工笔特写）、**信物**（可展开、可利落收合、可递出的器物——扇/鞭/笔/茶则/请柬）。题材换到任何故事世界（爱情小品/戏曲 IP/节气民俗/成语典故/非遗技艺/品牌上新/文物特展……拼贴量产基地已验证 8 个领域），配方一拍不变——故事只提供两方、信物与材料世界。每个创作决定先问「这是不是本风格会做的选择」，而不是「这个题材通常怎么做」。标杆片的"才子点秋香"只是配方在江南爱情题材上的一次取值：尘粉底、靛蓝布、朱红印是选材结果，不是规则，新故事必须重新推导。

**配方各环节的执行标准**（不与配方并列）在 `references/style-dna.md` Part A：A0 通用法则取舍表、纸底质感（A1）、配色约束（A2：低饱和统一＋唯一仪式色＋颜色数量封顶）、构图（A3）、人物画法密度（A4：剪影常态、彩绘特权）、动效语法（A5：滑/摆/贴/揭/翻/抖＋节奏双层制——永动层永不停、主事件一次一个；转场六式）、排版印章（A6）、声音（A7：近乎零拟音，重音交给拨弦，盖印静默）。"按故事分配"的**推导公式**在 Part B（纸底染色、材料包、仪式色、画法分配、信物、永动层、运动质感七问）。行业通识尺子本体在 `style-foundations` 技能。

本 Skill 生成一类高辨识度短片的 H3 提示词：**做旧手工纸上的木版画拼贴动画**（标杆为尘粉染宣纸，纸底染色按题材推导）。全片像一本会动的老画册——人物是剪纸/木版画风格的平面拼贴件，叙事主动方为全黑剪影（奶白细线勾五官），情感焦点为细腻上色的复古美人；画面元素以纸/墨材料动作衔接，**全程没有摄影机式硬切**：每次换景都是一次 0.4-0.75 秒的材料转场（纸浆雾化 / 墨液化 / 墨阵崩散 / 纸撕斜扫 / 门扇裂飞 / 粉刷横扫），且至少一个锚元素跨场存活；前三次（≈2.4 / 4.2 / 5.6 秒）是落在拨弦上的快速重组，约 9 秒后一律渐进软转场——节奏＝静→急→缓→静。以"信物亮题收合 + 无声盖下仪式色大印"收尾（标杆：开扇题字→合扇→朱红印）。配乐是单件传统弹拨乐器在恒定 50 BPM 网格上的稀疏拨弦，混音很轻。

当用户想要"复古中式/和风拼贴动画""剪影小剧场""老画册风格的故事开场"或点名"唐伯虎点秋香那种风格"时使用本 Skill。

## Step 0: 先读 H3 规范（必须）

写任何提示词之前，先读：

1. 同级技能 `h3-prompt-writing` 的 `SKILL.md` — 模式选择与工作流（Pi 会话用 `h3_get_skill name=h3-prompt-writing` 读；它与本技能装在同一技能根下）；
2. 该技能的 `references/base-en.txt` — T2VA/I2VA 的完整输出格式（三个核心字段、镜头与转场写法、运镜词表、屏幕文字规则）；
3. 若用户提供参考图/参考视频/参考音频且要求全参考模式，再读该技能的 `references/ref-en.txt`。

同时**必须**读本 Skill 的两份参考：

- `references/style-dna.md` — 锁定的视觉与听觉配方（色板、材质、人物画法、动效语法、禁忌清单）；
- `references/example-prompt.md` — 黄金范例：对标杆视频《唐伯虎点秋香》15 秒片的完整逆向 H3 提示词。

## Step 1: 收集输入并定参数

从用户输入确定（缺省值直接采用，不要追问）：

| 项目 | 缺省值 |
| --- | --- |
| 故事/IP | 用户必须提供（两方相遇/追逐/赠物类的小情节最合适；两方可以是两人，也可以一虚一实——人×产品/文物/物候） |
| 标题书法文字 | 故事名（如 "唐伯虎点秋香"），竖排或横排大字 |
| 时长 | 15.00 秒 |
| 画幅 | 16:9 横版 |
| 模式 | 无参考图 → T2VA；用户给了首帧图 → I2VA |
| 对白 | 无（本风格默认无人声；用户强烈要求时才加） |

把故事压缩成 **一句话选题：两方 + 一件信物 + 一个小情节**（标杆中：才子以扇为信物点中侍女），并分配座位：**剪影位＝行动方，美人位＝被点亮方**（人、产品、文物、节气物候皆可坐美人位，坐位者获得第 4 拍全片唯一一次工笔特写）。信物道具将贯穿全片并承担结尾动作。

## Step 2: 七拍结构规划

把情节装入以下节拍模板（标杆 15.06 秒实测拍界与占比，其他时长按占比缩放）：

| 拍 | 时间（占比） | 内容 | 固定装置（括号内为标杆样例） |
| --- | --- | --- | --- |
| 1 标题拼贴 | 0-2.40s（16%） | 全画幅静态拼贴微动：纸片、材料件、建筑线稿、彩绘角色、大字标题、小印 | 标题书法 + 仪式色小印，永动层飘落（花瓣） |
| 2 相遇递物 | 2.40-4.19s（12%） | 两方构图，剪影位向美人位递出/亮出信物道具 | 剪影角色 + 美人位坐位者，材料枝叶从画框角探入（金叶/花枝） |
| 3 泼墨强调 | 4.19-5.56s（9%） | 一个夸张动作触发墨点在巨物底盘上炸开——全片视觉最重的一击 | 浅色巨物底盘（大圆月盘）+ 黑墨飞溅 + 永动层乱飞 |
| 4 月下点睛→工笔特写（美人位） | 5.56-8.85s（22%） | 两方在巨物底盘前立定，剪影位以信物/手指做出标题动作（标杆"点"：6.50s ≈ 43% 处，全片题眼），随即推近成美人位全片唯一一次工笔特写（人：面部微笑；产品/文物：纹饰细绘同级密度），剪影角色在后景 | 人坐位：瓷白肌 + 圆形重腮红 + 仪式色点缀（红唇红发带） |
| 5 图案化对场（含门扇裂飞） | 8.85-11.30s（16%） | 换到图案化室内（格栅门窗 + 几何织物地面），两方镜像式互动（标杆：对舞）；拍末门扇如纸片裂开飞出，透出水墨远景 | 格栅 + 几何织物地 + 材料包器物（棋盘布/青花瓷） |
| 6 笔刷横扫清场 | 11.30-12.05s（5%） | 大干笔刷色块横扫，把内景"刷"回空白纸底，剪影位换位留在前景——本拍本身就是转场 | 纸底染色同族深一档的大笔触擦除（标杆：粉） |
| 7 合扇盖印定格 | 12.05-15.06s（20%） | 剪影角色侧影持信物展开（其上显影标题大字）→ 利落收合 → 右下角无声盖下仪式色大方印 → 定格 ≥1.3s（≈9% 片长） | 开扇与题字各卡一记拨弦 + 仪式色篆书大印（静默，落在网格拍位）+ 永动层落定 |

规则：

- 每一拍必须引入至少一个新视觉事件（新元素滑入、新动作、新转场）。
- 拍与拍之间**不写摄影机式硬切**：每次换景都是一次纸/墨材料转场，历时 0.4-0.75s（标杆六式：纸浆雾化 / 墨液化 / 墨阵崩散 / 纸撕斜扫 / 门扇裂飞 / 粉刷横扫，模板见 style-dna A5），且每次至少一个锚元素跨场存活（月轮/人物/信物）。前三次换景（≈2.4 / 4.2 / 5.6s）是落在拨弦上的快速重组，约 9s 之后一律渐进软转场——节奏＝静→急→缓→静。H3 里写作 `the shot transitions to` 并明确描述材料动作（本风格视为用户显式要求 wipe/dissolve）。
- 若用户的故事拍数不足，可合并拍 3 与拍 4；若时长更长，可在拍 5 后插入追逐/误会拍，但收尾必须是拍 7 的"信物亮题收合 + 静默盖印定格"。

**节奏执行标准**（标杆实测，metadata.source 目录下 `02_节奏与剪辑分析.md` §6）：

- 音乐＝单件弹拨乐器，**恒定 50 BPM（1.2s/拍）网格**贯穿全片；静段照常给拍；
- 转场跨拍间隙进行，**新场景立定压正拍**（标杆：T1 峰值 2.40s → 2.68s 拨弦上落定）；
- 事件密度均值 ≈2.7 个/s；**峰值 ≤6 个/s 且单峰 ≤1s**，每个峰后接 ≥0.8s 的呼吸谷（谷内只留永动层微动）；峰值只出现在转场群内（一次换景里多件纸片同进同出），其余时间主事件仍一次一个；
- 全片最强视觉事件（炸墨）**卡在拨弦上**（标杆 5.07s）。

## Step 3: 套用风格 DNA

先跑 `references/style-dna.md` Part B 的七个推导（纸底染色、材料包 4-6 种、仪式色、角色画法分配、信物道具、永动层、运动质感），把推导结果填进提示词。最低要求（缺一不可）：

1. `[Shot 1]` 开头声明风格：`Vintage East-Asian woodblock-print paper-collage animation`，并点明 `aged {B1 推导的染色} xuan paper` 基底与拼贴质感（标杆样例：dusty-pink）；
2. 剪影角色 = solid black paper silhouette，五官为 thin cream-colored line work，头饰/道具按题材世界取（标杆样例：Ming-style black scholar hat with a horizontal pin）；
3. 彩绘角色 = detailed painted face（porcelain skin、round rouge blush、点唇）+ 成型高发式 + 墨色袍服，衬里/发带/腰带用 B3 推导的仪式色系（标杆样例：red ribbon headband + black robe with red lining）；产品/文物坐美人位时，以同级细节密度工笔细绘其纹饰，仪式色落在其最具仪式感的部位；
4. 至少出现 B2 材料包中的 3 种材料件 + 永动层 + 信物道具（标杆样例：torn cream paper patches、checkerboard fabric swatch、gold branches、drifting petals、black-ribbed folding fan）；
5. 屏幕文字（标题书法、印章文字）用英文双引号原文保留，如 `"唐伯虎点秋香"`；
6. 动效全部是 cutout-puppet 式：肢体绕关节摆动、纸片平移滑入、轻微逐帧抖动；材料件按 B7 物性动法写（布软摆有 follow-through、瓷硬滑落定即停、墨是唯一可炸开的材料），全部通过"真纸测试"；
7. 结尾三连：信物亮相（其上题字）→ 利落收合 → 仪式色大方印盖下 → 定格 ≥1.3s（标杆样例：open fan with calligraphy → crisp snap shut → large square vermilion seal stamps down）；声音上亮相与题字各卡一记拨弦，盖印不给任何声音。

## Step 4: 写 H3 提示词

按 base-en.txt 的 T2VA（或 I2VA）格式输出英文提示词：

- `integrated_multimodal_description`：6-7 个 `[Shot N]`，首镜头无时间戳，后续 `At 00:0X.XXX` 严格递增且小于总时长；运镜以 static shot、slow push in、truck 为主，幅度小速度慢（纸片戏不适合大运镜）；
- `overall_soundscape`：只写极轻的纸张摩擦底噪（very faint dry paper rustle, almost buried under the plucks）；标杆实测几乎没有独立拟音层，不写墨溅、合扇脆响、盖印闷响——重音交给拨弦，盖印无声（静默重音落在网格拍上）；整体安静（对标积分 RMS ≈ -28 dBFS 的轻混音）；
- `non_diegetic_music`：sparse solo guzheng or pipa plucks on a steady 50 BPM grid (one pluck every 1.2 s)，高潮入口前一次约 0.5s 的轮拨加密，后半转为持续织体、重音仍落在网格上；最后一记拨弦落在信物亮题处，之后只留余韵衰减、声音先于画面结束；不要写情绪形容词，只写乐器、速度、密度变化。

对照 `references/example-prompt.md` 的黄金范例检查措辞密度与结构。

## Step 5: 质检清单

交付前逐项核对：

- [ ] Shot 1 开头有风格声明与纸底描述；
- [ ] 七拍全部落实，无摄影机式硬切措辞：每个 `the shot transitions to` 后都有纸/墨材料动作描述（0.4-0.75s），并写出跨场锚元素；
- [ ] 节奏：配乐写明 50 BPM 恒定网格；炸墨卡拨弦；新场景立定压拍；密度峰 ≤6 事件/s 且单峰 ≤1s，峰后有 ≥0.8s 呼吸谷；
- [ ] 时间戳严格递增且 ≤ 总时长；
- [ ] 标题/印章文字加英文双引号且原文未译；
- [ ] 双角色画法符合 DNA（剪影角色黑剪影+白线五官 / 彩绘角色细腻美人脸），画法密度分配正确（情感焦点才上彩）；
- [ ] 信物道具、永动层、材料包件至少各出现一次，材料包 ≥3 种；
- [ ] 动效通过"真纸测试"：无 glow；fade/morph 只以材料动作出现（纸浆雾化、墨液化），不写 digital fade / vector morph；材料件动法符合 B7 物性；同一时刻只推进一个主事件（转场群内多件纸片同进同出除外），永动层持续；
- [ ] 全片颜色可逐一回答"它是什么材料"，高饱和色仅仪式色一种且有 2-3 处同族呼应（对照 style-dna A2 五条）；
- [ ] 结尾是"信物亮题收合 + 无声仪式色大印"定格 ≥1.3s；overall_soundscape 只有极轻纸声底噪；
- [ ] 无禁忌词：photorealistic、3D render、smooth vector、neon、glow、modern objects；
- [ ] 音乐描述只含乐器/速度/密度，无情绪词。

## Step 5.5: Failure Handling（生成结果不对时：症状 → 提示词矫正）

- 动画像平滑数字动效、没有手作感 → 重写为 cutout-puppet 拍点措辞：slide in flat → light bounce → settle，加 "subtle frame-by-frame handmade jitter"；删掉 smooth/fluid/seamless 类词。
- 出现数字式淡入淡出 / 发光 / 矢量变形 → 违反真纸测试：glow 删除；fade 改 slide in 或写成材料动作（"soaks away into a mist of white paper pulp"）；morph 改为 "liquefies into black ink that reshapes into …" 或 "pieces slide apart and recompose"。
- 纸质太脏太旧（发黄、褶皱、污渍）→ 收紧做旧措辞：保留 mottled stains + fiber grain + vignetted corners，删掉 wrinkled/dirty/aged heavily；声明染色词（B1 推导结果）。
- 颜色数出来超过 7 种 / 出现第二种高饱和 → 删材料件或把新色降为做旧低饱和；重申仪式色唯一且落在 2-3 个器物上。
- 剪影角色被上了色、看清了五官 → 强化 "solid black paper silhouette, features only as thin cream line work"；彩绘特权只给情感焦点一人。
- 角色像真人/3D → 重申 "flat paper cut-out figures in woodblock-print style"，加禁忌 photorealistic/3D render。
- 转场变成摄影机式硬切 → 每个 `the shot transitions to` 后必须紧跟材料动作描述（纸浆雾化/墨液化/墨阵崩散/纸撕斜扫/门扇裂飞/粉刷横扫）并写出跨场留下的锚元素，缺一句就会切。
- 永动层消失（画面完全静止）→ 每镜写一句飘落物持续句（drifting petals continue falling softly）。
- 结尾没有盖印定格 → 收尾三连必须逐字写全：信物亮题 → 利落收合 → 大方印盖下 → hold（≥1.3s）。
- 音效抢戏 / 变成 UI 声或拟音剧 → overall_soundscape 只留极轻纸声底噪，删掉墨溅/木脆响/印闷响；non_diegetic_music 只写单件弹拨乐器与 50 BPM 网格，开扇与题字的重音交给拨弦，盖印保持无声。

## Step 6: 交付

先输出完整英文 H3 提示词，再用用户语言附一行下一步建议（例如：`下一步建议：确认后我可以用 MiniMax H3 按此提示词生成 15 秒 16:9 视频。`）。未经用户确认不要发起视频生成。
