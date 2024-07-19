from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=800)
    page = browser.new_page()
    page.goto("https://unsplash.com")

    page.get_by_alt_text("a bright blue object in the middle of the night sky").click()

    browser.close()
