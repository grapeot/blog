# 工作记录

## Changelog

### 2026-02-20 - 高优先级技术债务修复
**Commits:**
1. `086b595` - 升级主题：GA4、jQuery 3.7.1、删除 Google+、合并官方 2025 功能
2. `de71b1f` - 用 3 行 shim 替换 16KB Modernizr 2.6.2
3. `2f9cf66` - 添加测试计划、初始化 pelican-plugins submodule
4. `待提交` - 添加 Playwright 集成测试

**改动：**
- **Google Analytics**: ga.js → GA4 gtag.js，ID 改为 `G-03MXLX12W1`
- **jQuery**: 1.9.1 (2013, 有 XSS 漏洞) → 3.7.1
- **Modernizr**: 16KB → 3 行 shim
- **Google+**: 删除（2019 年关闭）
- **主题**: 合入官方 2025 功能（`CUSTOM_CSS_*`、`CUSTOM_JS_*`、`extra_footer.html`）

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
- `make html` 用 `pelicanconf.py`（开发），`make publish` 用 `publishconf.py`（生产）
- GA4 ID 只在 publish 模式注入

### 测试
- Playwright 可以检测 JS 错误、GA4 注入、主题切换功能
- 测试需要用 `make publish` 的输出（不是 `make html`）

---

## 待办

- [ ] 夜间模式配色统一（Gruvbox + Monokai 打架）
- [ ] Disqus 更新或迁移
- [ ] 清理 IE7/IE9 兼容代码
- [ ] CI/CD 部署方案
