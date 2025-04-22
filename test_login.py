import pytest
from pytest_playwright.pytest_playwright import browser


def test_login(browser_context_with_trace)-> None:
    page = browser_context_with_trace.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    # Interact with login form
    page.get_by_label("Email Address / Username").fill("Admin")
    page.get_by_label("Password", exact=True).fill("admin123")
    page.get_by_role("button", name="Login").click()
    assert "Login Successful!" in page.get_by_role("status").inner_text()
