import pytest, re
from playwright.sync_api import Page, expect

@pytest.mark.browser
def test_amazon_search(chrome_page: Page):
    page = chrome_page
    page.goto("https://www.amazon.com/")
    #page.wait_for_timeout(9000)
    try:
        page.get_by_role("button", name="Continue shopping").click(timeout=3000)
    except:
        print("Continue shopping page not shown")

    search_box = page.locator("#twotabsearchtextbox")
    print("Navigated to:", page.url)
    search_box.fill("Protein Powder")
    search_box.press("Enter")
    expect(page).to_have_title(re.compile("Protein Powder", re.IGNORECASE))
    print("Page title >>>", page.title())
    expect(page.locator("[data-component-type='s-search-result']").first).to_be_visible()
    print("Search results are displayed")

# def test_amazon_search(page: Page):
#     page.goto("https://www.amazon.com/")
#     page.get_by_placeholder("Search Amazon").fill("Protein Powder")
#     page.get_by_placeholder("Search Amazon").press("Enter")
#     expect(page).to_have_title(re.compile("Protein Powder", re.IGNORECASE))


