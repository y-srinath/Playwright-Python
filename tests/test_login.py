import pytest, re
from playwright.sync_api import Page, expect
from pages.ohrm_login_page import LoginPage
from pages.ohrm_home_page import HomePage

@pytest.mark.parametrize("username, password", [
    ("Admin", "admin123"),
    ("John", "password123")
])

def test_example(page: Page, username: str, password: str) -> None:
    # page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # page.get_by_role("textbox", name="Username").click()
    # page.get_by_role("textbox", name="Username").fill("Admin")
    # page.get_by_role("textbox", name="Password").click()
    # page.get_by_role("textbox", name="Password").fill("admin123")
    # page.get_by_role("button", name="Login").click()
    # expect(page.get_by_role("button", name="Upgrade")).to_be_visible()

    login_page = LoginPage(page)
    home_page = HomePage(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.login(username, password)
    home_page.is_upgrade_visible()
    home_page.click_performance()
    home_page.click_dashboard()