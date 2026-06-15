# Blog Redesign Implementation Plan：把 Signal handoff 落到 Pelican 博客

这份文档回答一个工程问题：`~/Downloads/design_handoff_blog_redesign/` 里的 **Signal** 设计能不能安全合进 `contexts/blog`，以及合进去前哪些约束必须先定死。结论是可以做，但它不是纯 CSS 替换，而是一次小型主题重构。

## 一屏结论

| 判断 | 结论 |
|---|---|
| 是否采用 Downloads handoff | 采用。`README.md`、`tokens.css`、`reference/theme.css` 是当前 source of truth |
| 旧 `design_review_assets/final_v1_*` | 只保留为探索记录，不再作为实现目标 |
| 最大工程风险 | 真实文章内容、双语 correspondence、中文 Kit、移动端降级 |
| 不做什么 | 不写回双向 `Translation` 字段，不做客户端 in-place 语言切换，不新增英文 newsletter，不把 Gumby 测试 contract 保留下来 |
| 推荐推进方式 | 先做数据/测试 contract，再换 shell/template，最后做真实截图 QA |

## 四个必须守住的 Gate

| Gate | 必须成立的条件 | 失败症状 | 验收方式 |
|---|---|---|---|
| 真实内容 | 长标题、图片、表格、代码、公式、inline HTML 都不撑破版面 | prototype 很好看，老文章横向溢出 | 抽样 7 类真实页面截图 |
| 双语关系 | 只用派生 index 查 pair，不反写 content 或 article metadata | Pelican 把自定义字段当 translation 逻辑处理，构建异常 | 中英文双方都有链接和 `hreflang` |
| Newsletter | Kit 仍只出现在中文文章正文末尾 | 英文页或 footer 出现订阅入口 | 中文页有 Kit，英文页无 CTA |
| 移动端 | 首页、文章、归档、masthead 都有小屏布局 | 桌面网格硬缩，阅读需要横向缩放 | 375/390/430/768px 截图无横滚 |

## 实现路径

| 顺序 | 工作 | 目的 | 主要文件 |
|---|---|---|---|
| 1 | 建立 bilingual index 和测试 contract | 先把行为边界固定，避免视觉重构时混入数据问题 | `pelicanconf.py` / theme helper、`tests/test_blog.py` |
| 2 | 重写 site shell | 换掉 Gumby-era masthead/footer/script shell | `themes/gum/templates/base.html`、`theme-toggle.js` |
| 3 | 重写页面模板 | 让首页、文章、归档、tag/category 都进入 Signal 结构 | `index.html`、`article.html`、`archives.html`、`tag.html`、`category.html` |
| 4 | 替换 CSS | 使用 frozen tokens 和 Signal component CSS，同时补真实内容 guardrails | `themes/gum/static/style.css` |
| 5 | 做截图 QA | 用真实内容验证设计，而不是只比对 prototype | `output/` + Playwright 截图 |

```text
先固定行为 contract
        ↓
换 base shell：fonts / masthead / footer / scripts
        ↓
换页面模板：index / article / archive / tags
        ↓
换 CSS tokens + components
        ↓
真实文章截图 QA，再修移动端和 edge cases
```

## 现有代码事实

| 事实 | 证据 | 对实现的影响 |
|---|---|---|
| 当前还是 Gumby shell | `themes/gum/templates/base.html` 引入 `gumby.css`、jQuery、Gumby JS，并使用 `#banner` / `#navigation` | redesign 应移除 Gumby 依赖，测试也要更新 |
| 首页和文章页依赖 sidebar | `index.html` / `article.html` 使用 `eleven columns` + `sidebar.html` | Signal 方案要删除 sidebar include points |
| 归档/tag/category 仍是默认列表 | `archives.html`、`tags.html`、`categories.html` 内容很薄 | 需要统一成 archive/list surface |
| 语言信息已经存在 | `docs/tag_system.md` 要求 `Chinese` / `English` tag；`AGENTS.md` 规定英文页 `Translation: chinese-slug.html` | 列表过滤可用 tag，文章 pair 需要派生 index |
| Newsletter 是内容层行为 | 中文文章末尾手工加 Kit 脚本，英文版不加 | 主题不要新增全站 subscribe card |
| 测试目前锁住旧结构 | `tests/test_blog.py` 查 `#navigation`、`#post-list`、`gumby.css`、jQuery、Gumby JS | Gumby 删除前必须先改测试 contract |

## 设计基准

Signal handoff 的可执行部分如下。实现时优先匹配这些，不再回到旧 mockup 做取舍。

| 维度 | 采用 |
|---|---|
| 字体 | `IBM Plex Sans`、`IBM Plex Mono`、`Noto Sans SC` |
| 颜色 | cool near-white / carbon dark + cobalt accent |
| 布局 | site max `1140px`，article column `680px` |
| Masthead | sticky、blurred background、monogram tile、mono nav |
| 首页 | lede + numbered post rows，`32px | 132px | 1fr` desktop grid |
| 文章页 | reading column、breadcrumb、byline、optional bilingual row、right rail TOC；不做首字母下沉 |
| 归档页 | year groups + dense rows，按日期和类别快速扫读 |
| Dark mode | 只切 `data-theme="dark"`，不引入其它 runtime visual toggles |

不采用的 prototype 部分：React state、客户端 in-place 语言切换、fake newsletter form、warm temperature toggle、sample-only figure placeholder、首字母下沉。

## Gate 1：真实文章兼容

真实内容的风险来自边界形态，不是普通段落。需要按下面这张表做 CSS 和模板 contract。

| 内容类型 | Contract |
|---|---|
| 正文 | 统一进入 `.prose-body`，正文列宽 `--maxw-prose: 680px` |
| 中文正文 | `lang="zh"` 或 `.prose-body.cjk`，line-height 比英文更松 |
| 长标题 | 允许换行，不截断，不用 fixed height |
| Summary | 首页最大宽度约 `66ch`，移动端自然换行 |
| 图片 / video / iframe | `max-width: 100%`，不能撑破 reading column |
| 表格 | 外层横向滚动，整页不能横滚 |
| 代码块 | `overflow-x: auto`，inline code 允许断行或局部滚动 |
| 数学公式 | 不被 line-height 或 overflow 破坏 |
| tag chips | 领域 tag 可展示；`Chinese` / `English` 不作为普通 chip 抢视觉主位 |

页面覆盖范围：`base.html`、`index.html`、`article.html`、`archives.html`、`tags.html`、`categories.html`、`tag.html`、`category.html`、`pagination.html`、`content/pages/*`、Disqus include、footer include。

`/search/` 目前没有对应 theme template。第一版可以让 search icon 跳转 `/search/` 或做轻量入口；完整 overlay 需要先确认 search index 的生成方式。

## Gate 2：双语 correspondence 只做派生 index

语言能力分两层，不能混在一起处理。

| 层级 | 用途 | 数据来源 | UI 行为 |
|---|---|---|---|
| 列表语言过滤 | 看中文列表或英文列表 | `Chinese` / `English` tag | 首页/归档 EN/中 filter 或链接 |
| 文章 pair 切换 | 当前文章跳到对应翻译 | 英文页 `Translation` + slug fallback 的派生 index | 文章页 bilingual row 普通链接 |

实现 bilingual index 的约束要写死：读英文文章的 `Translation` 字段，生成 `english_url -> chinese_url` 和 `chinese_url -> english_url` 查找表；用 slug fallback 处理 `foo-en.md`、`foo_en.md` 这类历史命名；查找表只供模板使用，不写回中文 frontmatter，不给 article 注入 `translation_url`、`is_bilingual` 这类 metadata 字段。

这样做的原因是 Pelican 自己有 translation 语义。把双向关系写成 frontmatter 或 article metadata，容易让编译阶段误判 translation 状态。我们要的是渲染期链接，不是改变 Pelican 的内容模型。

SEO 同步用这个 index 生成 `hreflang`。英文页现有 `article.translation` 可以继续用；中文页通过派生 index 补出英文 alternate。没有 pair 的文章不显示 bilingual switch，也不输出虚假的 alternate。

## Gate 3：Newsletter 保持中文 Kit 弹窗

| 页面/语言 | 行为 |
|---|---|
| 中文文章 | 保留正文末尾已有 Kit 脚本 |
| 英文文章 | 不显示 Kit，不显示 newsletter CTA |
| 首页/归档/tag/category | 不新增 newsletter 模块 |
| Footer | 不放 Newsletter 链接，除非以后有独立中文订阅页 |

文章 footer 的顺序建议是：正文结束后输出文章 tag chips；已有 Kit 脚本自然渲染；再输出 prev/next；最后输出 Disqus。不要把 Kit 包进 prototype 的 `.subscribe` 假表单里。CSS 只给 Kit 注入内容留出 margin 和宽度保护。

## Gate 4：移动端按阅读任务重新设计

移动端 primary task 是阅读和找文章。Signal 桌面网格要降级，而不是硬缩。

| 区域 | 小屏规则 |
|---|---|
| Masthead | 保留 brand、search/RSS、theme、menu；文字 nav 进 drawer 或下拉 |
| Touch target | 交互目标不低于 44px，不能只按 36px 图标按钮实现 |
| 首页 feed | `max-width: 760px` 下单列；隐藏 index；日期/category 横排 |
| Archive | year 从 sticky side column 变成 section title；row 允许换行 |
| Article TOC | 小屏隐藏右 rail；可选用标题后 `<details>`，第一版可不做 |
| Reading progress | 可保留，但不能遮住 iOS Safari 顶部安全区 |
| Drop cap | 全站关闭，不实现首字母下沉 |
| 宽内容 | 表格和代码块内部滚动，整页不横滚 |

移动端验收视口：375px、390px、430px、768px。每个视口至少看首页、中文文章、英文文章、归档页。

## 验收清单

| 类别 | 必须通过 |
|---|---|
| Build | `make html` 成功；`pytest tests/ -v` 成功；feeds、sitemap、theme assets 存在 |
| 功能 | GA4、Disqus、RSS/Atom、theme toggle、pygment light/dark 都仍可用 |
| 双语 | 英文页链接中文页；中文页链接英文页；无 pair 文章不显示 switch；双方 `hreflang` 成立 |
| Newsletter | 中文文章有 Kit；英文文章没有 Kit 或 newsletter CTA；footer 没有新增订阅入口 |
| 移动端 | 四档视口无整页横滚；masthead 可操作；正文、tag、archive row 自然换行 |
| 设计 | 匹配 Signal：Plex 字体、cobalt accent、mono metadata、细 rule、小 radius、monogram tile；不实现首字母下沉 |

## 第一版暂不做

| 暂不做 | 原因 |
|---|---|
| 真正的客户端全文 search overlay | 当前 search index 机制还没确认，先不要把搜索变成 redesign 阻塞项 |
| 双向 frontmatter | 会干扰 Pelican translation 编译逻辑 |
| 删除 `Chinese` / `English` tag | 它们仍是现有语言过滤口径 |
| 英文 newsletter 或全站订阅入口 | 当前 newsletter 只服务中文用户 |
| 首字母下沉 | 不符合这次本站落地偏好，直接从设计里移除 |
| 所有旧文章 pixel-perfect | 第一版先保证阅读可靠、无 overflow、核心页面符合 Signal |

<details>
<summary>实现文件索引</summary>

| 文件 | 计划 |
|---|---|
| `themes/gum/templates/base.html` | 重写 head font links、masthead、footer、script includes |
| `themes/gum/templates/index.html` | 改成 lede + numbered post feed + Signal pagination |
| `themes/gum/templates/article.html` | 改成 reading layout、bilingual row、tags、prev/next、Disqus |
| `themes/gum/templates/archives.html` | 改成年份分组 archive surface |
| `themes/gum/templates/tags.html` | 改成 tag index surface |
| `themes/gum/templates/categories.html` | 改成 category index surface |
| `themes/gum/templates/tag.html` | 复用 archive/list row，当前 tag preselected |
| `themes/gum/templates/category.html` | 复用 archive/list row，当前 category preselected |
| `themes/gum/templates/pagination.html` | 改成 `.pager` |
| `themes/gum/templates/sidebar.html` | 不再引用，可保留文件 |
| `themes/gum/static/style.css` | 用 `tokens.css` + Signal component CSS 重写，并补真实内容 guardrails |
| `themes/gum/static/js/theme-toggle.js` | 保留逻辑，适配新 button 和可访问 icon |
| `tests/test_blog.py` | 把旧 Gumby contract 改成 Signal contract |

</details>

<details>
<summary>截图 QA 抽样页</summary>

| 页面 | 要看什么 |
|---|---|
| 首页第一页 | post row、tag chips、pagination、mobile collapse |
| 中文 AI 长文 | 中文 line-height、Kit、Disqus、无首字母下沉 |
| 英文翻译页 | bilingual row、无 newsletter、英文行距 |
| 老中文图文页 | 图片和 inline HTML 是否撑破正文列 |
| 代码/表格页 | `pre`、table、inline code 是否局部滚动 |
| Archives | year grouping、dense rows、mobile one-column |
| Tag page | filter/list 行为和首页区分开 |
| About page | static page 是否也被新 shell 正常包住 |
| Dark mode | pygment、Kit、Disqus 周边、chips、nav 对比度 |

</details>

## 下一步

实现入口是 `themes/gum/templates/base.html`、`themes/gum/static/style.css` 和 bilingual index。建议第一步只提交数据/helper + 测试 contract；第二步再提交模板和 CSS。这样视觉迁移出问题时，行为边界仍然清楚。
