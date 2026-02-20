# Blog Test Plan

## Test Strategy

静态博客的测试分为三层：

```
┌─────────────────────────────────────────────┐
│  L3: Integration (Browser)                  │  ← Playwright
│  - JS 执行无报错                              │
│  - 主题切换功能                               │
│  - GA4 tag 正确注入                          │
├─────────────────────────────────────────────┤
│  L2: Static Analysis                        │  ← linkchecker, html5validator
│  - 链接完整性                                 │
│  - HTML 有效性                               │
│  - CSS/JS 文件存在                           │
├─────────────────────────────────────────────┤
│  L1: Build                                  │  ← make html
│  - Pelican 构建成功                          │
│  - 无插件加载错误                             │
└─────────────────────────────────────────────┘
```

---

## L1: Build Tests

### 1.1 构建测试
```bash
# 在 .venv 环境中执行
source .venv/bin/activate
make html
# 期望: exit code 0, 无 ERROR 日志
```

### 1.2 插件检查
当前缺失的插件:
- `sitemap` - 生成 sitemap.xml
- `gravatar` - Gravatar 头像支持

**Action**: 修复或移除这些插件配置

---

## L2: Static Analysis Tests

### 2.1 输出文件存在性
```bash
# 检查关键文件
test -f output/index.html
test -f output/theme/gumby.css
test -f output/theme/style.css
test -f output/theme/js/libs/jquery-3.7.1.min.js
test -f output/theme/js/libs/modernizr-shim.js
test -f output/theme/js/libs/gumby.min.js
```

### 2.2 链接检查
```bash
# 使用 linkchecker
pip install linkchecker
linkchecker output/ --ignore-url=".*disqus.*" --ignore-url=".*twitter.*"
```

### 2.3 HTML 验证
```bash
# 使用 html5validator (需要 Java)
pip install html5validator
html5validator --root output/
```

---

## L3: Integration Tests (Playwright)

### 3.1 页面加载 + JS 无报错
```python
# tests/test_blog.py
from playwright.sync_api import sync_playwright

def test_page_loads_without_js_errors():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        errors = []
        page.on("pageerror", lambda e: errors.append(e))
        
        page.goto("http://localhost:8000/")
        
        assert len(errors) == 0, f"JS errors: {errors}"
        browser.close()

def test_ga4_tag_present():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8000/")
        
        # 检查 GA4 script 存在
        ga_script = page.query_selector('script[src*="googletagmanager.com/gtag/js"]')
        assert ga_script is not None
        browser.close()

def test_theme_toggle():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8000/")
        
        # 初始状态
        initial_theme = page.evaluate("document.documentElement.getAttribute('data-theme')")
        
        # 点击切换
        page.click("#theme-toggle")
        
        # 验证主题改变
        new_theme = page.evaluate("document.documentElement.getAttribute('data-theme')")
        assert initial_theme != new_theme
        browser.close()
```

### 3.2 运行测试
```bash
# 启动本地服务器
cd output && python -m http.server 8000 &

# 运行 Playwright 测试
pip install playwright pytest-playwright
playwright install chromium
pytest tests/
```

---

## CI/CD Integration

```yaml
# .github/workflows/test.yml
name: Test Blog

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install uv
        run: curl -LsSf https://astral.sh/uv/install.sh | sh
      
      - name: Create venv and install deps
        run: |
          uv venv
          source .venv/bin/activate
          uv pip install pelican markdown
      
      - name: Build
        run: |
          source .venv/bin/activate
          make html
      
      - name: Check output files
        run: |
          test -f output/index.html
          test -f output/theme/js/libs/jquery-3.7.1.min.js
      
      - name: Install Playwright
        run: |
          source .venv/bin/activate
          uv pip install playwright pytest-playwright
          playwright install chromium
      
      - name: Run integration tests
        run: |
          source .venv/bin/activate
          cd output && python -m http.server 8000 &
          sleep 2
          pytest tests/
```

---

## Priority

| 优先级 | 测试 | 工具 | 状态 |
|--------|------|------|------|
| P0 | 构建成功 | make html | 需要修复插件 |
| P1 | 文件存在性 | bash test | 待实现 |
| P1 | JS 无报错 | Playwright | 待实现 |
| P2 | GA4 注入 | Playwright | 待实现 |
| P2 | 主题切换 | Playwright | 待实现 |
| P3 | 链接检查 | linkchecker | 待实现 |
| P3 | HTML 验证 | html5validator | 待实现 |

---

## Next Steps

1. **立即**: 修复插件问题 (sitemap, gravatar)
2. **短期**: 实现 P0/P1 测试
3. **中期**: 添加 Playwright 集成测试
4. **长期**: 配置 CI/CD
