# 黄金范例：《唐伯虎点秋香》15 秒拼贴片的完整 H3 提示词

本范例是对标杆视频的逐镜头逆向重写（T2VA 模式，15.00s，16:9）。新任务请替换故事、角色与标题文字，但保留节拍结构、转场方式与声音设计的写法密度。

> **关于本例中的具体颜色**：粉纸底、靛蓝布、金枝、朱红印等都是"江南才子佳人"题材跑 `style-dna.md` Part B 六个推导得出的**选材结果**（纸底染色=春日喜事→尘粉；仪式色=文人印信→印泥朱红…）。**新题材必须重新推导选材，禁止照抄本例的颜色。**

## 节拍对照

时间为原片实测拍界（SKILL.md metadata.source 目录下 `02_节奏与剪辑分析.md` §1，原片 15.06s；提示词按 15.00s 生成，末拍相应略短）：

| Shot | 时间（占比） | 对应七拍 | 原片内容 |
| --- | --- | --- | --- |
| 1 | 0.000-2.400（16%） | 标题拼贴 | 粉纸底全幅拼贴 + 书法标题 + 美人侧影持扇，全拍静置 |
| 2 | 2.400-4.190（12%） | 相遇 | 纸浆雾化换景 → 黑剪影才子向美人甩开大折扇，隔扇对望 |
| 3 | 4.190-5.560（9%） | 泼墨强调 | 月轮胀大、才子液化为墨成执笔巨手，墨点在大圆月上炸开（卡拨弦） |
| 4 | 5.560-8.850（22%） | 月下点睛 → 美人特写 | 墨阵崩散、二人月下立定，"点秋香"手势（6.50s ≈43%，全片题眼）→ 推近成女主回眸特写，男主剪影后景 |
| 5 | 8.850-12.050（16%+5%） | 厅堂对舞（含门扇裂飞）+ 笔刷横扫清场 | 纸撕斜扫入格栅厅堂镜像舞步 → 门扇裂飞露水墨远村 → 粉笔刷横扫清场 |
| 6 | 12.050-15.000（20%） | 合扇盖印定格 | 扇面题字（卡拨弦）→ 合扇 → 无声盖朱红大印 → 定格 ≥1.3s |

## 完整提示词

```text
integrated_multimodal_description: [Shot 1] Vintage East-Asian woodblock-print paper-collage animation, a full-frame title collage sits on aged dusty-pink xuan paper with mottled stains, visible fiber grain, and softly vignetted corners. Layered torn cream paper patches carry an ink-line drawing of upturned pavilion roofs at the upper left, a black-and-white checkerboard fabric swatch and an indigo cloth patch with a white circular emblem and visible stitch marks at the lower left. On the right, a woman rendered as a flat woodblock-print figure stands in profile: porcelain-white face with a heavy round rouge blush, glossy black voluminous updo with hairpins, dark robe, holding a large black-ribbed folding fan spread below her; pink plum-blossom branches arch around her and loose pink petals drift slowly down the frame. Large black calligraphy reading "唐伯虎点秋香" sits across the lower left on a torn paper strip, accompanied by two small vermilion seal stamps. The camera holds a static shot while the paper layers breathe with a subtle frame-by-frame handmade jitter. [Shot 2] At 00:02.400, a mist of white paper pulp spreads from the woman's card and the title collage soaks away into the paper while new cutout pieces slide in flat from the corners, recomposing into a two-figure encounter on the same pink paper: a scholar rendered as a solid black paper silhouette, his single-line eye and sly smile drawn in thin cream lines, wearing a black scholar hat with a long horizontal pin, extends a large black-ribbed folding fan flat toward a maiden on the right; she has a porcelain-white painted face with round rouge blush and small red lips, a glossy black updo bound with a red ribbon, and a black robe with red lining, holding her own small fan at her chest. Golden-leaf branches reach in from the top corners and checkerboard patches anchor the frame edges as petals keep drifting. Their cutout arms pivot at the joints like paper puppets. [Shot 3] At 00:04.190, the shot transitions as a small pale cream moon behind them swells into a huge disc filling the background while the scholar's sleeve and fan liquefy into black ink that reshapes into a giant black silhouette hand gripping an oversized ink brush; the brush flicks and a burst of black ink splatter blooms across the moon, scattering dots of ink while pink petals whirl through the splash. The camera pushes in with small amplitude at slow speed toward the ink bloom. [Shot 4] At 00:05.560, the ink burst shatters into a curtain of ink dots that scatters apart across the moon, and the shot transitions to the two figures standing beneath the pale moon: the black-silhouette scholar raises his sleeve and points one fingertip toward the maiden's cheek as a pink petal touches her lips; the camera then pushes in with small amplitude at slow speed into a close-up two-shot: the maiden's finely painted face turns over her shoulder into frame, smiling with heavy round blush and red lips, petals caught in her black updo and red ribbon, while the scholar's solid black silhouette face with cream-line features leans in behind her against the pale moon halo. The close-up settles and holds as a single petal lands on her hair. [Shot 5] At 00:08.850, a lattice-hall background seeps in behind the close-up and diagonal torn-paper strips sweep across the foreground, peeling the close-up away to reveal a patterned interior: teal lattice-window doors line the background, the floor is a black-and-white checkerboard, a gold-leaf branch enters from the upper left and pink blossoms with a blue-and-white porcelain planter stand at the right. The black-silhouette scholar on the left and the maiden in her black robe with red sash on the right mirror each other in a courtly cutout dance, sleeves swinging in flat pivoting arcs as they step apart and back. Near the end of the shot the lattice doors split apart and fly outward as flat paper pieces, opening a V-shaped gap onto a faint ink-wash village skyline; then a broad dry-brush stroke of dusty pink paint surges in from the lower right and sweeps across the frame, brushing the hall back to blank pink paper while the scholar stays in the foreground. [Shot 6] At 00:12.050, the pink brush stroke wipes clear to the final card on plain aged pink paper: the scholar stands in black silhouette profile, his cream-line eye and smile visible, holding the folding fan fully open with large black calligraphy reading "唐伯虎点秋香" across the top of the frame and a small vermilion seal beside it; a single pink petal rests on his sleeve. He snaps the fan shut into a thin stick with a crisp motion, the tassel swinging once, and a large square vermilion seal with seal-script characters stamps down onto the paper at the lower right. The petals settle and the image holds as a still collage until the end.

overall_soundscape: Only a very faint dry paper rustle sits under the collage movements, almost buried beneath the plucks; there is no separate spatter, snap, or stamp sound, and the seal lands in complete silence. The whole mix stays quiet and intimate with long silences.

non_diegetic_music: Sparse solo guzheng plucks on a steady 50 BPM pulse, one pluck every 1.2 seconds with long decays between single notes, the ink burst landing on a pluck; a single brief tremolo flurry just before the midpoint, then a soft sustained pipa texture whose accents still fall on the same 1.2-second grid through the dance; accented plucks mark the fan opening and the calligraphy appearing, after which no new note sounds and the last pluck simply decays into silence before the image ends.
```

## I2VA 变体要点

若用户提供首帧图（通常是标题拼贴帧），按 base-en.txt 在最前面加一行：

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.
```

然后 Shot 1 改写为"锚定图中已有的纸底、拼贴件、人物与标题 → 花瓣开始飘落、纸层开始呼吸"，后续节拍不变。
