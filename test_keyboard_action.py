from playwright.sync_api import sync_playwright
from pytest_playwright.pytest_playwright import page


def test_keyboard_action(page):

  page.goto("https://www.selenium.dev/selenium/web/web-form.html")

# Click first input to focus (allowed once)
page.click("input[name='my-text']")

# Type text using keyboard
page.keyboard.type("Hello Playwright")

# Clear text using CTRL + A + Backspace
page.keyboard.down("Control")
page.keyboard.press("A")
page.keyboard.up("Control")
page.keyboard.press("Backspace")

# Type again
page.keyboard.type("Keyboard Automation")

# Navigate using TAB key
page.keyboard.press("Tab")   # Move to Password
page.keyboard.type("password123")

page.keyboard.press("Tab")   # Move to Textarea
page.keyboard.type("This form is automated using keyboard")

    # Keep pressing TAB until Submit button
for _ in range(5):
    page.keyboard.press("Tab")

    # Submit form using ENTER key
page.keyboard.press("Enter")

page.wait_for_timeout(3000)



