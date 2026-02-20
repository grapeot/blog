# Blog Tag System

> 更新时间：2025-02-20
> 
> 总文章数：363 | 总标签数：27

---

## Tag 索引（按文章数排序）

| Tag | 文章数 | 说明 |
|-----|--------|------|
| Chinese | 225 | 中文文章 |
| English | 138 | 英文文章 |
| AI | 76 | AI 通用（不适合归入子类） |
| Tutorial | 58 | 教程 |
| Reflection | 52 | 反思、随想 |
| Agentic AI | 46 | Agent、Cursor、Devin、自主执行 |
| Photography | 42 | 普通摄影 |
| Review | 34 | 评测 |
| Astrophotography | 34 | 天文摄影 |
| DIY | 30 | 自己动手 |
| Career | 21 | 职业、面试 |
| AI Technique | 21 | Prompt、微调 |
| Hardware | 17 | 硬件评测、3D打印 |
| Research | 17 | 学术研究 |
| AI Coding | 12 | AI 辅助编程 |
| AI Product | 12 | AI 产品分析 |
| Audio | 12 | 音频、HiFi |
| Smart Home | 10 | 智能家居 |
| Image Processing | 8 | 图像处理 |
| Linux | 7 | Linux |
| Time Management | 7 | 时间管理 |
| Aviation | 6 | 航空 |
| AI Management | 6 | 管理 AI |
| Travel | 6 | 旅行 |
| Finance | 5 | 金融 |
| Coffee | 4 | 咖啡 |
| Health | 4 | 健康 |

---

## 设计原则

### 规则

1. **语言标签（必须有）**：每篇文章有且仅有一个语言标签（Chinese 或 English）
2. **领域标签（1-3个）**：根据文章内容选择，明确属于子类时不用父类
3. **中英文一致**：翻译版本应该有相同的领域标签

### Tag 分类

**语言：**
- Chinese, English

**AI 领域：**
- AI（通用兜底）
- Agentic AI（Agent、Cursor、Devin）
- AI Coding（AI 辅助编程）
- AI Management（管理 AI）
- AI Product（AI 产品分析）
- AI Technique（Prompt、微调）

**摄影：**
- Astrophotography（天文摄影）
- Photography（普通摄影）

**其他领域：**
- Audio, Coffee, Career, Smart Home, Hardware, Health, Finance

**内容形式：**
- Tutorial, Review, Reflection, Research, DIY

**工具/系统：**
- Time Management, Image Processing, Linux, Travel, Aviation

---

## 问题诊断

### 迁移前的问题

1. **粒度不统一**：AI 太大（139篇），OpenClaw 太小（2篇）
2. **语言标记污染**：Chinese/English 占据 tag 榜单前列
3. **大小写混乱**：astrophotography/Astrophotography，gpt/GPT
4. **同类项未合并**：Agentic AI / AI Centric / AI Native 本质相同

### 解决方案

- 合并同类项（Agentic AI / AI Centric / AI Native → Agentic AI）
- 统一大小写（astrophotography → Astrophotography）
- 保留语言标签（用户需求：一键看所有中文/英文）
- 精简到 27 个核心标签

---

## 实施记录

2025-02-20：
- 分析 363 篇文章，设计新的 tag taxonomy
- 使用 8 个 sub-agent 并行分析文章内容
- 生成 tag_proposal.json 作为迁移计划
- 批量更新所有文章的 Tags 字段
- 验证：361 篇替换成功，2 篇新增 Tags 行

---

## 设计决策

### Q: 为什么保留 AI 通用标签？

**A:** 用于不适合归入具体子类的文章。如 `ai-eternity`（赛博长生哲学）、`ai-society`（后智慧时代社会思考）等。

### Q: 为什么保留 Chinese/English 作为 Tag？

**A:** 用户有"一键看所有中文/英文"的需求，目前没有其他机制实现这个功能。

### Q: 为什么不用太多工具名作为 Tag？

**A:** 工具会过时。Cursor 今天火，明年可能就换别的。文章的核心价值是方法论，不是工具本身。
