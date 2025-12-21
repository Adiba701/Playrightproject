

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def test_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        print("launch browser")
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
        print("close browser")




