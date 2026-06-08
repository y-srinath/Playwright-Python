import pytest
import re
from playwright.sync_api import Page, expect
from datetime import datetime

@pytest.mark.browser
def test_login(edge_page: Page) -> None:
    print(f"START Login Test: {datetime.now()}")
    page = edge_page
    page.goto("https://practicetestautomation.com/practice-test-login/")
    print("Navigated to Login Page")

    expect(page.get_by_role("heading", name="Test login")).to_be_visible()
    print("Login Page Loaded Successfully")

    page.get_by_role("textbox", name="Username").fill("student")
    print("Username Entered")

    page.get_by_role("textbox", name="Password").fill("Password123")
    print("Password Entered")

    page.get_by_role("button", name="Submit").click()
    print("Clicked Submit Button")

    expect(page.get_by_role("heading")).to_contain_text("Logged In Successfully")
    print("Login Successful")

    expect(page.get_by_role("strong")).to_contain_text(
        "Congratulations student. You successfully logged in!"
    )
    print("Success Message Verified")

    expect(page.get_by_role("link", name="Log out")).to_be_visible()
    print("Logout Link Displayed")

    page.get_by_role("link", name="Log out").click()
    print("Logged Out Successfully")

    print(f"END Login Test: {datetime.now()}")
