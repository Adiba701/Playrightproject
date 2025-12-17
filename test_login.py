from pydoc import browse

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def setup():
    with sync_playwright() as playwright:
        # Launch the browser
      browse =  playwright.chromium.launch(headless=False ,slow_mode=500)
        print("Browser setup")
        yield
        browse.close()
        print("Browser teardown")



