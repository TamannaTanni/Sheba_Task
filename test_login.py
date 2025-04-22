from pytest_playwright.pytest_playwright import page

LOGIN_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'


def test_login(page)-> None:

    page.goto(LOGIN_URL)

    # Interact with login form
    page.fill('input[name="username"]', "Admin")
    page.fill('input[name="password"]', "admin123")
    page.get_by_role("button", name="Login").click()

    page.wait_for_load_state("networkidle")

    assert page.url != LOGIN_URL, "Login failed or page did not redirect"
