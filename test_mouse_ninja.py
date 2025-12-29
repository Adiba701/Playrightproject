from playwright.sync_api import Page


def test_double_click(page: Page):
    page.goto("https://demoqa.com/buttons")

    # Double Click
    page.locator("#doubleClickBtn").dblclick()

    # Validate message
    msg = page.locator("#doubleClickMessage").text_content()
    assert "You have done a double click" in msg

def test_right_click(page: Page):
        page.goto("https://demoqa.com/buttons")

        # Right Click (Context Click)
        page.locator("#rightClickBtn").click(button="right")

        # Validate message
        msg = page.locator("#rightClickMessage").text_content()
        assert "You have done a right click" in msg
