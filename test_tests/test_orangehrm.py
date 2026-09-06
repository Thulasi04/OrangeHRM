from playwright.async_api import Page
from pages import login_page as login
from helper import helper_for_pages as hp

def test_navigate_to_login(page: Page):
    hp.open_website(page)
    title = page.title()
    hp.assert_page(title,"OrangeHRM")

#testcase1
def test_valid_login(page: Page):
    hp.open_website(page)
    login.login_with_valid(page)
    header = page.locator('//h6[text()="Dashboard"]').text_content()
    hp.assert_page(header,"Dashboard")

#testcase2
def test_invalid_username(page: Page):
    hp.open_website(page)
    login.login_with_invalid_username(page)
    invalid = page.locator('[class="oxd-text oxd-text--p oxd-alert-content-text"]').text_content()
    hp.assert_page(invalid ,"Invalid credentials")

#testcase3
def test_invalid_password(page: Page):
    hp.open_website(page)
    login.login_with_invalid_password(page)
    invalid = page.locator('[class="oxd-text oxd-text--p oxd-alert-content-text"]').text_content()
    hp.assert_page(invalid ,"Invalid credentials")

#testcase4
def test_empty_fields(page: Page):
    hp.open_website(page)
    login.empty_login_page(page)
    required = page.locator("//span[text()='Required']").first.text_content()
    hp.assert_page(required,"Required")

#testcase5
def test_forgot_password(page: Page):
    hp.open_website(page)
    login.forgot_password_page(page)
    reset_header = page.locator('h6[class="oxd-text oxd-text--h6 orangehrm-forgot-password-title"]').text_content()
    hp.assert_page(reset_header,"Reset Password")
    page.wait_for_timeout(5000)

#testcase6
def test_navigate_to_admin(page: Page):
    hp.open_website(page)
    login.login_with_admin_page(page)
    admin = page.locator('a[class="oxd-main-menu-item active"]').text_content()
    hp.assert_page(admin,"Admin")

#testcase7
def test_admin_search_user(page: Page):
    hp.open_website(page)
    login.search_user_page(page)
    record_found = page.locator('//span[text()="(1) Record Found"]').text_content()
    hp.assert_page(record_found, "(1) Record Found")

#testcase8
def test_add_user_role(page: Page):
    hp.open_website(page)
    login.add_user_role_page(page)
    user_role = page.locator('//div[@role="rowgroup"]//div[@role="cell"]//div[text()="ESS"]').first.text_content()
    hp.assert_page(user_role,"ESS")
    page.wait_for_timeout(5000)

#testcase9
def test_reset_user_role_filter(page: Page):
    hp.open_website(page)
    reset_text =  login.user_role_page(page)
    hp.assert_page(reset_text,"-- Select --")

#testcase10
def test_search_invalid_username(page: Page):
    hp.open_website(page)
    no_records_msg = login.search_invalid_username_page(page)
    hp.assert_page(no_records_msg, "No Records Found")
    page.wait_for_timeout(5000)

#testcase11
def test_navigate_to_pim(page: Page):
    hp.open_website(page)
    page.locator("input[name='username']").type("Admin")
    page.locator("input[name='password']").type("admin123")
    page.locator("button[type='submit']").click()
    page.locator('//span[text()="PIM"]').click()
    header = page.locator('//h6[text()="PIM"]').text_content()
    assert header == "PIM"
    page.wait_for_timeout(5000)

#testcase12
def test_search_emp_id(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/")
    page.locator("input[name='username']").type("Admin")
    page.locator("input[name='password']").type("admin123")
    page.locator("button[type='submit']").click()
    page.locator('//span[text()="PIM"]').click()
