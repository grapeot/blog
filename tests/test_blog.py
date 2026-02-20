import subprocess
import time
import socket
import pytest
import random
from playwright.sync_api import sync_playwright, Page


def get_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]


@pytest.fixture(scope="module")
def server():
    port = get_free_port()
    proc = subprocess.Popen(
        ["python", "-m", "http.server", str(port)],
        cwd="output",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(1)
    yield f"http://localhost:{port}"
    proc.terminate()
    proc.wait()


class TestBuild:
    def test_index_exists(self):
        import os
        assert os.path.exists("output/index.html"), "index.html not found"
    
    def test_theme_files_exist(self):
        import os
        files = [
            "output/theme/gumby.css",
            "output/theme/style.css",
            "output/theme/pygment.css",
            "output/theme/pygment-dark.css",
            "output/theme/js/libs/jquery-3.7.1.min.js",
            "output/theme/js/libs/modernizr-shim.js",
            "output/theme/js/libs/gumby.min.js",
            "output/theme/js/theme-toggle.js",
        ]
        for f in files:
            assert os.path.exists(f), f"{f} not found"


class TestIntegration:
    def test_page_loads_without_js_errors(self, server):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            
            page.goto(server + "/")
            page.wait_for_load_state("networkidle")
            
            browser.close()
            
            assert len(errors) == 0, f"JS errors found: {errors}"
    
    def test_ga4_tag_present(self, server):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(server + "/")
            
            ga_script = page.query_selector('script[src*="googletagmanager.com/gtag/js"]')
            assert ga_script is not None, "GA4 script not found"
            
            content = page.content()
            assert "G-03MXLX12W1" in content, "GA4 measurement ID not found"
            
            browser.close()
    
    def test_theme_toggle(self, server):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(server + "/")
            
            initial = page.evaluate("document.documentElement.getAttribute('data-theme')")
            
            toggle = page.query_selector("#theme-toggle")
            assert toggle is not None, "Theme toggle button not found"
            
            toggle.click()
            page.wait_for_timeout(100)
            
            new = page.evaluate("document.documentElement.getAttribute('data-theme')")
            
            assert initial != new, "Theme did not change after toggle"
            
            browser.close()
    
    def test_no_console_errors(self, server):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            console_messages = []
            page.on("console", lambda msg: console_messages.append(msg))
            
            page.goto(server + "/")
            page.wait_for_load_state("networkidle")
            
            browser.close()
            
            errors = [m for m in console_messages if m.type == "error"]
            allowed_patterns = ["disqus", "ERR_NAME_NOT_RESOLVED", "ERR_CONNECTION_REFUSED"]
            real_errors = [e for e in errors if not any(p in e.text.lower() for p in allowed_patterns)]
            assert len(real_errors) == 0, f"Console errors: {[e.text for e in real_errors]}"


class TestNavigation:
    def test_archives_page(self, server):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            
            page.goto(server + "/archives.html")
            page.wait_for_load_state("networkidle")
            
            assert len(errors) == 0, f"JS errors on archives: {errors}"
            assert "Archives" in page.title() or page.query_selector("h1, h2"), "Archives page content missing"
            
            browser.close()
    
    def test_navigation_links(self, server):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(server + "/")
            
            nav_links = page.query_selector_all("#navigation a")
            assert len(nav_links) >= 3, f"Expected at least 3 nav links, found {len(nav_links)}"
            
            browser.close()
    
    def test_click_random_article(self, server):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(server + "/")
            
            article_links = page.query_selector_all("#post-list a")
            if len(article_links) == 0:
                pytest.skip("No articles found on homepage")
            
            random_link = random.choice(article_links)
            href = random_link.get_attribute("href")
            
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            
            random_link.click()
            page.wait_for_load_state("networkidle")
            
            assert len(errors) == 0, f"JS errors on article page: {errors}"
            
            browser.close()
    
    def test_click_archives_then_article(self, server):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            
            page.goto(server + "/archives.html")
            page.wait_for_load_state("networkidle")
            
            archive_links = page.query_selector_all("a[href$='.html']")
            internal_links = [a for a in archive_links if not (a.get_attribute("href") or "").startswith("http")]
            
            if len(internal_links) > 0:
                random_link = random.choice(internal_links[:10])
                random_link.click()
                page.wait_for_load_state("networkidle")
            
            assert len(errors) == 0, f"JS errors during navigation: {errors}"
            
            browser.close()
    
    def test_tags_page_or_sidebar(self, server):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            
            page.goto(server + "/")
            
            tag_links = page.query_selector_all(".sidebar-tags a, .tag a, a[href*='tag']")
            if len(tag_links) > 0:
                random_tag = random.choice(tag_links[:5])
                random_tag.click()
                page.wait_for_load_state("networkidle")
            
            assert len(errors) == 0, f"JS errors on tag page: {errors}"
            
            browser.close()
