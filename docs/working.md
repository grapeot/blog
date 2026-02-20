# 工作记录

## Changelog

### 2026-02-20 - 高优先级技术债务修复
**Commits:**
1. `086b595` - 升级主题：GA4、jQuery 3.7.1、删除 Google+、合并官方 2025 功能
2. `de71b1f` - 用 3 行 shim 替换 16KB Modernizr 2.6.2
3. `2f9cf66` - 添加测试计划、初始化 pelican-plugins submodule
4. `3c7d251` - 添加 Playwright 测试、修复 Modernizr.load shim
5. `7d225ad` - 更新 README 环境/测试指南、补充 pytz 依赖
6. `1fab1ec` - 更新 working.md
7. `8f610a2` - 夜间模式统一 Gruvbox、清理 IE CSS、扩展测试
8. `c27810c` - 修复 Disqus 空短名称问题、添加 Disqus 测试
9. `待提交` - 统一 pelicanconf/publishconf 配置、添加 make test

**改动：**
- **Google Analytics**: ga.js → GA4 gtag.js，ID 改为 `G-03MXLX12W1`
- **jQuery**: 1.9.1 (2013, 有 XSS 漏洞) → 3.7.1
- **Modernizr**: 16KB → 5 行 shim（含 load 方法）
- **Google+**: 删除（2019 年关闭）
- **主题**: 合入官方 2025 功能（`CUSTOM_CSS_*`、`CUSTOM_JS_*`、`extra_footer.html`）
- **夜间模式**: Monokai → Gruvbox Dark（配色统一）
- **Disqus**: 更新到最新嵌入代码
- **IE 兼容**: 删除 .ie7/.ie8/.ie9 CSS 代码
- **测试**: 扩展到 11 个 Playwright 测试（含导航测试）

**JS 体积优化:** ~109KB → ~88KB（-21KB）

### 2026-02-20 - 项目启动
- 从 GitHub 拉取最新内容
- 并行 Agent 调研识别技术债务

---

## 经验教训

### Google Analytics 迁移
- Universal Analytics (UA-XXXXX-X) 在 2023/7/1 停止处理，2024/7/1 完全关闭
- GA4 Measurement ID 格式是 `G-XXXXXXXXXX`
- 实现用 gtag.js，不是 ga.js 或 analytics.js

### Pelican 主题维护
- 官方 gum 主题在 `getpelican/pelican-themes` 仓库里（不是独立仓库）
- 2025 年新增 `CUSTOM_CSS_FILES` 等配置
- 2024 年新增 `extra_footer.html` 模板覆盖

### JavaScript 库
- jQuery 1.9.1 有 XSS 漏洞，必须升级到 3.7.x
- Modernizr 如果只用 touch 检测，可以用 shim 替代
- `gumby.min.js` 内嵌 `Modernizr.load()` 调用，shim 需要实现这个方法
- Gumby Framework (2014) 已停止维护，未来考虑迁移

### 构建流程
- `pelican-plugins` 是 git submodule，需要 `git submodule update --init`
- `sitemap` 插件需要 `pytz` 依赖
- `make html` 用 `pelicanconf.py`，`make publish` 用 `publishconf.py`
- **GA4/Disqus 统一在两个配置中启用**，确保开发/测试/生产一致
- `make test` = `make html` + `pytest tests/ -v`

### 夜间模式
- 主 UI 用 Gruvbox，代码高亮也要用 Gruvbox Dark 保持一致
- Pygments 语法高亮配色需要单独定义（`pygment-dark.css`）

### 测试
- Playwright 可以检测 JS 错误、GA4 注入、主题切换功能
- 测试需要用 `make publish` 的输出（不是 `make html`）
- 导航测试可以覆盖 archives、随机文章、tags 等页面
- 外部资源加载失败（Disqus 等）需要过滤掉，不算测试失败

---

## 待办

- [x] ~~夜间模式配色统一（Gruvbox + Monokai 打架）~~ → 已改用 Gruvbox Dark
- [x] ~~Disqus 更新或迁移~~ → 已更新到最新嵌入代码
- [x] ~~清理 IE7/IE9 兼容代码~~ → 已删除
- [ ] CI/CD 部署方案（手工部署足够，暂不实施）
