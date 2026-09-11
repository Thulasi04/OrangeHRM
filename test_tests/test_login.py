import pytest
from playwright.async_api import Page
from pages import login_page as login
from helper import helper_for_pages as hp
from locators import login_locators as locate

@pytest.mark.regression
def test_navigate_to_login(page: Page):
    hp.open_website(page)
    title = page.title()
    hp.assert_page(title, "OrangeHRM")

@pytest.mark.regression
def test_valid_login(page: Page):
    hp.open_website(page)
    login.login_with_valid(page)
    header = page.locator(locate.dashboard_header_selector).text_content()
    hp.assert_page(header, "Dashboard")

@pytest.mark.regression
def test_invalid_username(page: Page):
    hp.open_website(page)
    login.login_with_invalid_username(page)
    invalid = page.locator(locate.invalid_credentials_selector ).text_content()
    hp.assert_page(invalid, "Invalid credentials")

@pytest.mark.regression
def test_invalid_password(page: Page):
    hp.open_website(page)
    login.login_with_invalid_password(page)
    invalid = page.locator(locate.invalid_credentials_selector).text_content()
    hp.assert_page(invalid, "Invalid credentials")

@pytest.mark.regression
def test_empty_fields(page: Page):
    hp.open_website(page)
    login.empty_login_page(page)
    required = page.locator(locate.required_selector).first.text_content()
    hp.assert_page(required, "Required")

@pytest.mark.regression
def test_forgot_password(page: Page):
    hp.open_website(page)
    login.forgot_password_page(page)
    reset_header = page.locator(locate.reset_password_header_selector).text_content()
    hp.assert_page(reset_header, "Reset Password")