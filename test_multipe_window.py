import time
from playwright.sync_api import Playwright, Page, expect

def test_MultipleWindow(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    #firefoxBrowser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    #page = firefoxBrowser.new_page()

    page.goto("https://www.orangehrm.com/")

    with page.expect_popup() as newPage_info:
        page.locator("xpath=(//a[@href='https://www.orangehrm.com/en/company/about-us'])[1]").click()
        childPage = newPage_info.value

        # All lines inside 'with' block must be indented the same
        expect(childPage.locator("xpath=//div[@class='page-title']")).to_be_visible()
        page.bring_to_front()
        page.locator("xpath=(//a[@href='https://www.orangehrm.com/en/resources/e-books'])[2]").click()
        childPage = newPage_info.value
        #expect(childPage.locator("xpath=//div[@class='page-title']")).to_be_visible()
        page.bring_to_front()
        #childPage.close()

        time.sleep(5)
