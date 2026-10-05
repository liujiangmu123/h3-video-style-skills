# H3 视频风格与选题技能

从视频、文章和创作方法研究中形成的 **22 项专用 skill**，覆盖 **12 个创作方向**。本项目提供技能原文、参考文件和可供 H3-pi-agent 安装的独立技能包。它与 [8 项通用生产技能](https://github.com/liujiangmu123/h3-production-skills) 配合使用。

整理日期：2026-10-05。各技能版本和内容保持原样；这次只做分类、导出和打包。这里的“专用技能”不表示专利权或官方认证。

## 按类别选择

### 知识讲解

| 方向 | 风格与写作 | 选题与栏目 |
|---|---|---|
| 深海极简演示 | [shenhai-style-explainer](skills/shenhai-style-explainer/SKILL.md) | [shenhai-series-planner](skills/shenhai-series-planner/SKILL.md) |
| 电子智人参与式科普 | [dianzi-style-explainer](skills/dianzi-style-explainer/SKILL.md) | [dianzi-series-planner](skills/dianzi-series-planner/SKILL.md) |
| TED 观点与技术科普 | [ted-style-explainer](skills/ted-style-explainer/SKILL.md) | [ted-series-planner](skills/ted-series-planner/SKILL.md) |
| 知识溯源阶梯 | [knowledge-ladder-explainer](skills/knowledge-ladder-explainer/SKILL.md) | [knowledge-ladder-series-planner](skills/knowledge-ladder-series-planner/SKILL.md) |
| 经典论文与演示 | [paper-demo-explainer](skills/paper-demo-explainer/SKILL.md) | [paper-demo-series-planner](skills/paper-demo-series-planner/SKILL.md)（待补全） |

### 故事叙事

| 方向 | 风格与写作 | 选题与栏目 |
|---|---|---|
| 雪中笔法古风短篇 | [xuezhong-style-writing](skills/xuezhong-style-writing/SKILL.md) | [xuezhong-series-planner](skills/xuezhong-series-planner/SKILL.md) |
| 古风歌曲一歌一故事 | [gufeng-song-story](skills/gufeng-song-story/SKILL.md) | [gufeng-song-story-series-planner](skills/gufeng-song-story-series-planner/SKILL.md) |
| 人物传记档案蒙太奇 | [biography-montage-style-explainer](skills/biography-montage-style-explainer/SKILL.md) | [biography-montage-series-planner](skills/biography-montage-series-planner/SKILL.md)（待补全） |
| 历史原创重演 | [history-reenact-explainer](skills/history-reenact-explainer/SKILL.md) | [history-reenact-series-planner](skills/history-reenact-series-planner/SKILL.md)（待补全） |

### 动画制作实验

| 方向 | 风格与制作 | 选题与栏目 |
|---|---|---|
| 代码生成视频与多风格展示 | [codegen-style-showcase](skills/codegen-style-showcase/SKILL.md) | [codegen-showcase-series-planner](skills/codegen-showcase-series-planner/SKILL.md) |

此方向涉及同框多种制作语言、代码与 H3 混合、由最小视觉单元发展成作品。具体引擎和技术路线仍以实际接入情况为准。

### 诗词与纸艺

| 方向 | 技能 | 当前选题配对 |
|---|---|---|
| 电影感诗词长卷 | [cinematic-poem-scroll-video](skills/cinematic-poem-scroll-video/SKILL.md) | 尚无独立 planner |
| 复古木版画拼贴 | [vintage-woodblock-collage-video](skills/vintage-woodblock-collage-video/SKILL.md) | 尚无独立 planner |

## 怎样使用

**找方向或做题库**：读取所选方向的 `series-planner`，同时读取配对风格的哲学与本质。**写一期作品**：读取风格技能，再由通用动画创意、分镜、提示词和生产导演承接。**分析新类别并形成新技能**：使用通用库的 `h3-research-director` 与 `style-foundations`；本库提供已经沉淀的类别方法。

在你现有的 Pi 环境里，这 22 项已经安装。可以直接提出任务，例如：

```text
请用 h3_get_skill 读取 codegen-style-showcase 和 codegen-showcase-series-planner。
按这个系列的方法研究新方向，给我选题与制作方案，并标出实际可执行和待试验的部分。
```

或者：

```text
读取 xuezhong-series-planner，提出适合这一写法的故事选题；
选定后用 xuezhong-style-writing 写稿，再交 h3-director 制作。
```

在其他电脑可克隆两个公共项目：

```powershell
git clone https://github.com/liujiangmu123/h3-production-skills.git
git clone https://github.com/liujiangmu123/h3-video-style-skills.git
```

通用读取型 Agent 可以按任务打开 `skills/<name>/SKILL.md` 和其引用的参考文件。H3-pi-agent 用户在 [安装包目录](packages/README.md) 下载对应 `.skill.zip`，通过现有 `h3_skill install` 安装。使用明确的包路径；替换已有版本时查看工具报告的覆盖范围。风格和选题技能按需读取即可。

技能库提供方法与制作约定；实际生成仍依赖用户已配置的 H3-pi-agent、ComfyUI、模型及工作流。技能原文保留的 G:/AI、D:/AI 路径是原工作站的工程或证据位置，迁移时映射到实际路径，原视频与完整研究档案没有随库分发。

## 文件和验证

- `skills/`：22 个完整技能目录，79 个原始文件。
- `packages/`：22 个独立 `.skill.zip`，包内带逐文件校验清单。
- [catalog.json](catalog.json)：类别、版本、配对、来源、文件哈希和当前状态。
- [校验结果](docs/verification.json)：22 项检查，0 error、6 warning。

3 个选题技能仍含“待填”条目，已在目录标注；诗词长卷和木版画拼贴缺独立选题配对，另有一个长度提醒。保留这些原始状态，不把格式通过写成创意或成片质量认证。

校验当前快照和安装包：

```powershell
python scripts/verify_bundle.py
```

研究来源与使用边界见 [来源说明](THIRD_PARTY_NOTICES.md)。本项目没有模型权重、软件环境、原始视频和音乐素材。
