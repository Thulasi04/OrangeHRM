import pytest
from playwright.async_api import Page
from pages import leave_page as leave
from helper import helper_for_pages as hp
from locators import leave_locators as locate

@pytest.mark.leavefeature
def test_navigate_to_leave(page: Page):
    hp.open_website(page)
    header = leave.navigate_to_leave(page)
    hp.assert_page(header, "Leave")

@pytest.mark.leavefeature
def test_leave_apply_navigation(page: Page):
    hp.open_website(page)
    heading = leave.leave_apply_navigation(page)
    hp.assert_page(heading, "Apply Leave")

@pytest.mark.leavefeature
def test_leave_my_leave_navigation(page: Page):
    hp.open_website(page)
    heading = leave.leave_my_leave_navigation(page)
    hp.assert_page(heading, "My Leave List")

@pytest.mark.leavefeature
def test_leave_search_reset(page: Page):
    hp.open_website(page)
    reset_text = leave.leave_search_reset(page)
    hp.assert_page(reset_text, "-- Select --")