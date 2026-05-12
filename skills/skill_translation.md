# Blog 文章英译 Skill

## 元数据

- **类型**: Workflow
- **适用场景**: 将博客 `content/` 下的中文 markdown 文章翻译为英文版
- **创建日期**: 2026-05-11
- **更新日期**: 2026-05-11

## 目标

将一篇中文博客文章以意义翻译（而非逐字逐句翻译）的方式转换为英文版，产出具有英语母语阅读体验的翻译，并遵循本博客已有英文版文章的 front matter 规则。

## 验收标准

- 英文版文件已保存到 `content/` 目录，文件名为 `<slug>-en.md`（如 `ai-sleep-en.md`）
- 英文版 front matter 按本 skill 的输出规格设置
- 中文版文章内的站内链接（指向其他博客文章）在英文版中指向对应的英文版 slug（slug 加 `-en`）
- 英文版不包含 Kit 订阅脚本
- 翻译以意义为单位，不以句子为单位——英文读起来像母语者写的，不是翻过来的
- 中文特色表达（如"拍脑袋"、"瞎猫撞上死耗子"）找英文对应惯用语，不直译

## 可用资源

- `content/` 目录下的已发表英文版文章（`*-en.md`），作为 front matter 格式和文风参考
- 中文版原文文件

## 输出规格

### 文件名

`<cn-slug>-en.md`，与中文版文件放在同一目录。

### Front matter 规则

从中文版 front matter 照此规则翻译：

| 字段 | 中文版 | 英文版 |
|------|--------|--------|
| Title | 中文标题 | 自然英文翻译，不逐字 |
| Date | `YYYY-MM-DD HH:MM` | 同一天，但比中文版早 1 小时 |
| Category | 保留原值 | 保留原值 |
| Tags | `Chinese, ...` | `English, ...`（把 `Chinese` 替换为 `English`，其他不变） |
| Slug | `my-slug` | `my-slug-en` |
| Translation | (无此字段) | `my-slug.html`（指向中文版 .html 文件） |
| Summary | 中文摘要 | 英文摘要，约 160 字符 |

**注意**：只有英文版需要 `Translation` 字段，中文版不需要。

### Kit 订阅脚本

中文版末尾有：
```html
<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>
```
英文版**不要**加这行。

### 站内链接

中文版文章中的站内链接（`[文字](/some-article.html)` 格式）在英文版中需指向对应的英文版页面：
- 如果链接目标有对应的英文版（`some-article-en.md`），改为 `/some-article-en.html`
- 如果链接目标没有英文版，保持原链接
- 链接文字本身也要翻译为英文

### 文章末尾

英文版末尾不加 Kit 脚本，也不留多余空行。

## 方法论建议

**意义翻译。** 不逐句对译。把中文段落整体理解后，用英语母语者自然的方式重新表达。允许：
- 调整段落内句子顺序以适应英文叙事节奏
- 合并或拆分中文的短句
- 把中文的多层嵌套从句解构成英文的清晰主谓结构
- 在保留原意的前提下适当压缩或展开

**术语处理。** 中文特有的概念（如"comfort level"本身已是英文的保留原样；"拍脑袋"、"车轮战"、"体力活"等找到英文对应表达）。

**技术名称。** HealthKit、iOS、Apple Watch、AA 电池等专有名词保留原文。多变量回归分析、AST 解析等技术术语保留标准英文术语。

**文化适配。** "瞎猫撞上死耗子" → "a broken clock is right twice a day" 或类似英语谚语。"没头苍蝇一样的尝试" → "random trial and error"。不要直译中文俗语。

## 已知陷阱

| 陷阱 | 表现 | 应对 |
|------|------|------|
| 外部链接（yage.ai 域）指向中文版 | 中文版引用同博客其他文章时用了完整 URL（`https://yage.ai/some-article.html`），翻译后指向仍是中文版 | 将这些完整 URL 也改为对应的英文版链接（在 slug 后加 `-en`）。检查所有以 `yage.ai` 为域名的站内链接 |
| 中文俗语直译 | "拍脑袋"译成 "pat the head"、"瞎猫撞上死耗子"译成 "blind cat finds dead mouse"，英文读者无法理解 | 改用英文对应成语或惯用语：拍脑袋 → wild guess / gut feeling；瞎猫撞上死耗子 → random trial and error / a broken clock is right twice a day；没头苍蝇 → random flailing；车轮战 → tag-team / in rapid succession |
| 中文文章内嵌的英文术语 | 中文文章常直接夹用英文词（如 comfort level、app、bug、log、debug），翻译时需要判断保留还是改写 | 优先保留原文中的英文技术术语（HealthKit、Python、iOS、REM、AST），但需要调整周围语法使其在英文中自然。例如中文写"comfort level 的变化"，英文直接写 "changes in comfort level" |
| Kit 脚本遗漏 | 将中文版整段复制后容易把 Kit 订阅脚本也带进英文版 | 英文版末尾**必须删除** Kit 脚本。策略：以中文版 final front matter 之后、Kit 脚本之前的正文部分为翻译源 |
| 中文标点和表达习惯残留 | 中文版有"啊。。"（双句号表达语气）、"😂"等标点和 emoji，直翻到英文版不合适 | 双句号改为正常句号或根据语气转为其他表达。emoji 根据英文文章风格决定是否保留（通常删除） |
| 外链文字未翻译 | 中文版链接文字是中文（如`[成本结构决定最优策略]`），翻译后链接文字仍为中文 | 链接文字也要翻译，如`[cost structure determines optimal strategy]`。同时检查链接目标是否有对应英文版 |
| 中文版中间某个 heading 的文字没带空格 | 中文版可能写了 `##非主流的失眠诊断`（`##` 后无空格）。英文版要注意写 `## `（`##` 后有空格） | 翻译时直接按标准 Markdown 写，`## ` 后加空格 |
| 漏翻中文片段 | 中文段落中间夹了中文词未被翻译，如"高强度"留在英文句子里 | 翻译完成后全文 grep 检查是否还有 CJK 字符残留。快速验证：`rg -n '[\u4e00-\u9fff]' content/<file>-en.md` |
