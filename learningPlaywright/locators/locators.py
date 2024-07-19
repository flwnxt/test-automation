"""
Learning locators

"""

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")

    # # get_by_role
    btn = page.get_by_role("button", name="Default button")
    heading = page.get_by_role("heading", name="Heading 2")
    radio_btn = page.get_by_role("radio", name="Option two can be something else and selecting it will deselect "
                                               "option one")
    checkbox_btn = page.get_by_role("checkbox", name="Default checkbox")
    checkbox_btn.check()

    # # get by_label method
    email_field = page.get_by_label("Email address")

    # # get by_placeholder
    pwd_field = page.get_by_placeholder("Password")

    # # get by_text
    # possible arguments: exact=False ; exact=True
    get_text = page.get_by_text("with faded secondary text")
    get_partial_text = page.get_by_text("showing and hiding")

    # # get by title
    get_by_title = page.get_by_title("attribute")

    # # get by CSS locator
    # h1 tag
    heading_tag = page.locator("css=h1")  # css tag is optional

    # button with specific class name
    get_by_locator_class = page.locator("button.btn-outline-success")

    # button with specific ID
    get_by_locator_id = page.locator("button#btnGroupDrop1")

    # field with specific attribute
    get_by_locator_attribute = page.locator("input[readonly]")

    # field with specific value
    get_by_locator_value = page.locator("input[value='correct value']")

    # # CSS hierarchy
    # from nav select the anchor which has 2 classes (nav-link & active)
    get_by_specific_locator = page.locator("nav.bg-dark a.nav-link.active")

    # also, get the direct child of a parent direct child selector by searching for div.bs-component > ul.list-group
    get_by_specific_locator_first_child = page.locator("div.bs-component > ul.list-group")

    # # Pseudo Classes
    # get the h1 tag which contains the text "navbars", but all the h1 tags which contains "nav" will be returned
    get_by_pseudoclass = page.locator("h1:text('Navbars')")

    # get the h1 tag which contains the text "nav", but all the h1 tags which contains "nav" will be returned
    get_by_pseudoclass_all_nav = page.locator("h1:text('Nav')")

    # get the h1 tag which contains the exactly specified text
    get_by_specific_pseudoclass = page.locator("h1:text-is('Navs')")

    # get the element which is visible using :visibile pseudoclass. This will not return anything because this div
    # is not visibile
    get_by_pseudoclass_visible = page.locator("div.dropdown-menu:visibile")

    # get the 5th element found on page
    get_by_pseudoclass_the_5th_element = page.locator(":nth-match(button.btn-primary, 5)")

    # get the 1st element found on page having the "primary" text
    get_by_pseudoclass_having_specific_text = page.locator(":nth-match(button:text('Primary'), 1)")

    # # xpath
    # /html/head/title - this is the absolute path
    # // - two slashes, means to search anywhere into the document (relative paths)
    get_by_xpath = page.locator("xpath=//h1")

    # get by xpath with specific ID
    get_by_xpath_specific_id = page.locator("xpath=//h1[@id='navbars']")

    # # get first element (when multiple elements with the same attribute are returned) using specific field attribute
    readonly_input = page.locator("//input[@readonly]")

    # getting the first element having the "readonly" selector
    first_readonly_input = readonly_input.first

    # # get an element by specific value
    get_by_specific_value = page.locator("//input[@value='wrong value']")

    # # other locators
    # get first element by role and name of the element
    page.get_by_role("button", name="Primary").locator("nth=0")

    # # get the 18th element
    page.locator("button").locator("nth=18")

    # # get the parent component of an element
    page.get_by_label("Email address").locator("..")

    # get by id
    page.locator("id=btnGroupDrop1")

    # get specific heading with specific text
    page.get_by_role("heading").filter(has_text="Heading").highlight()

    # locate the dropdown menu which is visible
    page.locator("div.dropdown-menu").locator("visible=true")



    print("Page Link:", page.url)
    browser.close()
