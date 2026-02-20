import subprocess
import time
import socket
import pytest
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
            assert len(errors) == 0, f"Console errors: {[e.text for e in errors]}"
