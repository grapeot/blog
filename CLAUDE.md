# Blog 写作与发布规范

## 博客引擎

Pelican 静态站点生成器。内容在 `content/` 目录，Markdown 格式。

## 文章 Frontmatter

### 中文文章

```markdown
---
Title: 文章标题
Date: 2026-03-30 22:00
Category: Computing
Tags: Chinese, Frontend, System Design
Slug: my-article-slug
Summary: 一两句话的中文摘要，150-200 字符。
---
```

末尾加 Kit 订阅脚本：
```html
<script async data-uid="65448d4615" src="https://yage.kit.com/65448d4615/index.js"></script>
```

### 英文翻译版

文件名加 `-en` 后缀（如 `my-article-en.md`）。

```markdown
---
Title: English Title
Date: 2026-03-30 21:00
Category: Computing
Tags: English, Frontend, System Design
Slug: my-article-slug-en
Translation: my-article-slug.html
Summary: English summary, ~160 chars.
---
```

和中文版的区别：
- `Tags` 里 `Chinese` 改成 `English`
- `Slug` 加 `-en` 后缀
- `Date` 比中文版早 1 小时
- 加 `Translation` 字段，值是中文版的 `.html` 文件名（slug + .html）
- 末尾不加 Kit 订阅脚本
- 中文版不需要 `Translation` 字段（只有英文版指向中文版）

## 文章内链接

站内链接用 Pelican 的相对路径格式。中文文章内链接中文版，英文文章内链接英文版：
- 中文：`[文章名](/article-slug.html)`
- 英文：`[Article Name](/article-slug-en.html)`

## 工作记录

Changelog 和经验教训记录在 `docs/working.md`。
