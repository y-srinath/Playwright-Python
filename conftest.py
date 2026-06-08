import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def chrome_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=False,
            slow_mo=2000
        )

        page = browser.new_page()
        page.set_default_timeout(7000)

        yield page

        page.close()
        browser.close()

@pytest.fixture
def edge_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="msedge",
            headless=False,
            slow_mo=2000
        )

        page = browser.new_page()
        page.set_default_timeout(7000)

        yield page

        page.close()
        browser.close()