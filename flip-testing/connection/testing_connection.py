"""
Connect to the testing environment on Flip
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=700)

    page = browser.new_page()

    page.goto("https://flip:flippass@testing.flip.ro")

    print("Link:", page.url)



    browser.close()


