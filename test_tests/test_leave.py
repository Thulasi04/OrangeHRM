import pytest
from playwright.async_api import Page
from pages import login_page as login
from helper import helper_for_pages as hp


@pytest.mark.leavefeature
def test_navigate_to_leave(page: Page):
    hp.open_website(page)
    header = login.navigate_to_leave(page)
    hp.assert_page(header, "Leave")


@pytest.mark.leavefeature
def test_leave_apply_navigation(page: Page):
    hp.open_website(page)
    heading = login.leave_apply_navigation(page)
    hp.assert_page(heading, "Apply Leave")


@pytest.mark.leavefeature
def test_leave_my_leave_navigation(page: Page):
    hp.open_website(page)
    heading = login.leave_my_leave_navigation(page)
    hp.assert_page(heading, "My Leave List")


@pytest.mark.leavefeature
def test_leave_search_reset(page: Page):
    hp.open_website(page)
    reset_text = login.leave_search_reset(page)
    hp.assert_page(reset_text, "-- Select --")