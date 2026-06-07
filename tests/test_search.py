import pytest, re
from playwright.sync_api import Page, expect

def test_search(page: Page):
    page.goto("https://www.duckduckgo.com/")

    search_input = page.get_by_role("combobox", name="Search with DuckDuckGo")
    search_input.fill("Playwright Python")
    search_input.press("Enter")

    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))