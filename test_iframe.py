from playwright.sync_api import sync_playwright, expect

def test_iframe(page):

    # Launch website
    page.goto("https://the-internet.herokuapp.com/iframe")

    # 1️⃣ Switch to iframe using frame_locator
    iframe = page.frame_locator("#mce_0_ifr")

    # 2️⃣ Clear existing content
    iframe.locator("body").click()
    page.keyboard.down("Control")
    page.keyboard.press("A")
    page.keyboard.up("Control")
    page.keyboard.press("Backspace")

    # 3️⃣ Enter text
    iframe.locator("body").type("I rule the frames!")

    # 4️⃣ Validate iframe content
    expect(iframe.locator("body")).to_have_text("I rule the frames!")

    page.wait_for_timeout(3000)

