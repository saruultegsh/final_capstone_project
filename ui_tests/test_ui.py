from playwright.sync_api import sync_playwright
from pages.home_page import HomePage

def test_open_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        home = HomePage(page)
        home.open()

        assert "Example" in home.get_title()

        browser.close()

def test_heading():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://example.com")

        assert page.locator("h1").inner_text() == "Example Domain"

        browser.close()

def test_url():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://example.com")

        assert "example.com" in page.url

        browser.close()

def test_title():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://example.com")

        assert page.title() == "Example Domain"

        browser.close()