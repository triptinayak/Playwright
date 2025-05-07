
from playwright.sync_api import sync_playwright

def test_mobile_emulation():
    with sync_playwright() as p:
        iphone_12 = p.devices['iPhone 12']
        browser = p.webkit.launch(headless=False)
        context = browser.new_context(**iphone_12)
        page = context.new_page()
        page.goto("https://rahulshettyacademy.com/client")
        page.locator("#userEmail").fill("tripti_5@yahoo.com")
        page.locator("#userPassword").fill("1008Chancery")
        page.get_by_role("button", name="Login").click()
        browser.close()