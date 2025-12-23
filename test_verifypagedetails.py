from playwright.sync_api import expect


def test_verifypagedetails(page):
    page.goto("https://www.orangehrm.com/")
    print("launch the url")

    expect(page).not_to_have_title("Human Resources Management Software | HRMS | OrangeHRM")
    print(page.title())

    page.locator("xpath=(//a[@class='navbar-brand nav-logo'])[1]").is_visible()
    print("verify logo should be there")


