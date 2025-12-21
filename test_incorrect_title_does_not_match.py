from playwright.sync_api import expect


def test_incorrect_title_does_not_match(page):
    page.goto("https://www.orangehrm.com/")

    # Verify incorrect title does NOT match actual title
    expect(page).not_to_have_title("swaglabs")
    print("tittle does not match")
