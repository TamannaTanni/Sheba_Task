from pytest_playwright.pytest_playwright import page
from datetime import datetime

LEAVE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/leave/applyLeave"

def login(page):
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page.fill('input[name="username"]', "Admin")
    page.fill('input[name="password"]', "admin123")
    page.click('button[type="submit"]')
    page.wait_for_load_state("networkidle")

def test_apply_leave(page):

    login(page)

    page.goto(LEAVE_URL)
    page.wait_for_load_state("networkidle")

    page.click('div.oxd-select-text')  # Open dropdown
    page.get_by_text("CAN - FMLA", exact=True).click()  # Select option

    page.locator('input[placeholder="yyyy-dd-mm"]').nth(0).fill(datetime.today().strftime('%Y-%d-%m'))

    # page.locator('input[placeholder="yyyy-dd-mm"]').nth(1).fill("2025-25-04")
    page.locator('input[placeholder="yyyy-dd-mm"]').nth(1).click()

    # page.wait_for_selector('label.oxd-label:text("Duration")', timeout=10000)

    page.get_by_role("button", name="Apply").click()

    assert page.locator('text=Successfully Saved').is_visible()
