import pytest
from playwright.async_api import Page
from pages import admin_page as admin
from helper import helper_for_pages as hp
from locators import admin_locators as locate

@pytest.mark.adminfeature
def test_navigate_to_admin(page: Page):
    hp.open_website(page)
    admin.login_with_admin_page(page)
    admin_page = page.locator(locate.admin_page_selector).text_content()
    hp.assert_page(admin_page, "Admin")

@pytest.mark.adminfeature
def test_admin_search_user(page: Page):
    hp.open_website(page)
    admin.search_user_page(page)
    record_found = page.locator(locate.record_found_selector).text_content()
    hp.assert_page(record_found, "(1) Record Found")

@pytest.mark.adminfeature
def test_add_user_role(page: Page):
    hp.open_website(page)
    admin.add_user_role_page(page)
    user_role = page.locator(locate.user_role_result_selector).first.text_content()
    hp.assert_page(user_role, "ESS")

@pytest.mark.adminfeature
def test_reset_user_role_filter(page: Page):
    hp.open_website(page)
    reset_text = admin.user_role_page(page)
    hp.assert_page(reset_text, "-- Select --")

@pytest.mark.adminfeature
def test_search_invalid_username_page(page: Page):
    hp.open_website(page)
    no_records = admin.search_invalid_username_page(page)
    hp.assert_page(no_records, "No Records Found")