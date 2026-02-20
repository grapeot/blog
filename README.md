# Computing Life

This repo is the underlying files for my blog [Computing Life](http://grapeot.me/), aiming to provide a start point for a basic blog site using [Pelican](https://github.com/getpelican/pelican/), which is a static site generator.

There is a `gh-pages` branch of the repo providing a backup for the website [here](http://grapeot.github.io/blog/).

---

## 新环境配置

### 1. 克隆仓库（含 submodule）

```bash
git clone --recursive git@github.com:grapeot/blog.git
# 或如果已经 clone：
git submodule update --init --recursive
```

### 2. 创建虚拟环境

```bash
cd blog
uv venv
source .venv/bin/activate
```

### 3. 安装依赖

```bash
# 编译依赖
uv pip install -r requirements.txt

# 测试依赖
uv pip install pytest playwright pytest-playwright
playwright install chromium
```

---

## 构建

```bash
source .venv/bin/activate

# 开发模式
make html

# 生产模式（编译 + copy 到 /var/www/yage）
make publish
```

**注意**：GA4 和 Disqus 在 `pelicanconf.py` 和 `publishconf.py` 中都已启用，确保开发/测试/生产环境一致。

---

## 测试

### 运行测试

```bash
source .venv/bin/activate

# 方式一：make test（推荐）
make test

# 方式二：手动运行
make html
pytest tests/ -v
```

### 测试结果解读

```
tests/test_blog.py::TestBuild::test_index_exists PASSED           # output/index.html 存在
tests/test_blog.py::TestBuild::test_theme_files_exist PASSED      # CSS/JS 文件都存在
tests/test_blog.py::TestIntegration::test_page_loads_without_js_errors PASSED  # 页面 JS 无报错
tests/test_blog.py::TestIntegration::test_ga4_tag_present PASSED  # GA4 代码注入正确
tests/test_blog.py::TestIntegration::test_theme_toggle PASSED     # 主题切换功能正常
tests/test_blog.py::TestIntegration::test_no_console_errors PASSED  # 浏览器控制台无错误
tests/test_blog.py::TestNavigation::test_archives_page PASSED     # 归档页面正常
tests/test_blog.py::TestNavigation::test_navigation_links PASSED  # 导航链接存在
tests/test_blog.py::TestNavigation::test_click_random_article PASSED  # 随机文章可访问
tests/test_blog.py::TestNavigation::test_click_archives_then_article PASSED  # 归档→文章导航
tests/test_blog.py::TestNavigation::test_tags_page_or_sidebar PASSED  # 标签页正常
tests/test_blog.py::TestNavigation::test_disqus_scripts_present PASSED  # Disqus 脚本存在
tests/test_blog.py::TestNavigation::test_disqus_no_empty_shortname PASSED  # Disqus shortname 正确
```

**常见失败：**

| 错误 | 原因 | 解决 |
|------|------|------|
| `index.html not found` | 没有先构建 | `make publish` |
| `GA4 script not found` | 用了 `make html` | 用 `make publish` |
| `JS errors: Modernizr.load is not a function` | shim 不完整 | 检查 `modernizr-shim.js` |
| `net::ERR_NAME_NOT_RESOLVED` | 外部资源加载失败 | 正常（Disqus 等），可忽略 |

---

## 部署（手工）

```bash
# 1. 拉取最新代码
git pull --rebase
git submodule update --init

# 2. 激活环境
source .venv/bin/activate

# 3. 运行测试
pytest tests/ -v

# 4. 如果测试通过，部署
make publish
```

---

## 目录结构

```
blog/
├── .venv/                 # 虚拟环境（不提交）
├── content/               # 文章源文件
├── output/                # 构建产物（不提交）
├── pelican-plugins/       # Git submodule
├── themes/gum/            # 主题
│   ├── templates/
│   └── static/js/libs/
│       ├── jquery-3.7.1.min.js
│       ├── modernizr-shim.js
│       └── gumby.min.js
├── tests/                 # Playwright 测试
├── docs/                  # 文档
├── pelicanconf.py         # 开发配置
├── publishconf.py         # 生产配置
├── requirements.txt       # 编译依赖
└── Makefile
```

---

## 依赖清单

| 用途 | 依赖 |
|------|------|
| 编译 | pelican, markdown, pelican-render-math, pytz |
| 测试 | pytest, playwright, pytest-playwright |
| 插件 | pelican-plugins (submodule) |
