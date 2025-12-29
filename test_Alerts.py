import time
from tkinter import dialog
import pytest
from playwright.sync_api import expect, Page


def test_Accept_JavaScript_Alert(page : Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    print("URL launched")

    page.on("dialog", lambda dialog: dialog.accept())
    page.locator("xpath=//button[text()='Click for JS Alert']").click()

    result_text = page.locator("#result").text_content()
    print("Result:", result_text)

    assert "You successfully clicked an alert" in result_text

    time.sleep(5)

def test_Alert_Dismiss(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    accept = False

    def handle_dialog(dialog):
        if accept:
            dialog.accept()
        else:
            dialog.dismiss()

    # dialog handler register
    page.on("dialog", handle_dialog)

    # Click JS Confirm button
    page.locator("//button[text()='Click for JS Confirm']").click()

    page.wait_for_timeout(3000)

    # Verify result text
    result = page.locator("#result").text_content()
    assert "You clicked: Cancel" in result
    print("Result:", result)


def test_enter_text_and_acept(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    def handle_dialog(dialog):
        print("Prompt text:", dialog.message)
        dialog.accept("Playwright Hero")

    page.on("dialog", handle_dialog)

    # Click JS Prompt button
    page.locator("//button[text()='Click for JS Prompt']").click()

    page.wait_for_timeout(3000)

    # Verify result
    result = page.locator("#result").text_content()
    print("Result:", result)

    assert "Playwright Hero" in result