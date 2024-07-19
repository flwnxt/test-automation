from playwright.sync_api import sync_playwright

# playwright = sync_playwright().start()

with sync_playwright() as playwright:

    # Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)

    # Create a new page
    page = browser.new_page()

    # Go to the playwright page
    page.goto("https://playwright.dev/python")

    # Locate a link element with "Docs" text and click on it
    docs_button = page.get_by_role('link', name='Docs')
    docs_button.click()

    #  Get the url and print it
    print("Link:", page.url)

    browser.close()
