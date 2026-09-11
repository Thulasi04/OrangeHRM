import pytest
from playwright.async_api import Page
from pages import login_page as login
from helper import helper_for_pages as hp


@pytest.mark.adminfeature
def test_navigate_to_admin(page: Page):
    hp.open_website(page)
    login.login_with_admin_page(page)
    admin = page.locator(
        'a[class="oxd-main-menu-item active"]'
    ).text_content()
    hp.assert_page(admin, "Admin")


@pytest.mark.adminfeature
def test_admin_search_user(page: Page):
    hp.open_website(page)
    login.search_user_page(page)
    record_found = page.locator(
        '//span[text()="(1) Record Found"]'
    ).text_content()
    hp.assert_page(record_found, "(1) Record Found")


@pytest.mark.adminfeature
def test_add_user_role(page: Page):
    hp.open_website(page)
    login.add_user_role_page(page)
    user_role = page.locator(
        '//div[@role="rowgroup"]//div[@role="cell"]//div[text()="ESS"]'
    ).first.text_content()
    hp.assert_page(user_role, "ESS")
    page.wait_for_timeout(5000)


@pytest.mark.adminfeature
def test_reset_user_role_filter(page: Page):
    hp.open_website(page)
    reset_text = login.user_role_page(page)
    hp.assert_page(reset_text, "-- Select --")


@pytest.mark.adminfeature
def test_search_invalid_username(page: Page):
    hp.open_website(page)
    no_records_msg = login.search_invalid_username_page(page)
    hp.assert_page(no_records_msg, "No Records Found")
    page.wait_for_timeout(5000)