from playwright.async_api import Page
from helper import actions_for_pages
from helper import constants_for_pages as const
from locators import admin_locators as locate

def login_with_admin_page(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.admin_page_selector)

def search_user_page(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.admin_page_selector)
    actions_for_pages.type_action(page, locate.search_user_selector, const.username_admin)
    actions_for_pages.click_action(page, locate.search_submit_button_selector)

def add_user_role_page(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.admin_page_selector)
    actions_for_pages.click_action(page, locate.user_role_selector)
    actions_for_pages.click_action(page, locate.ess_role_selector)
    actions_for_pages.click_action(page, locate.search_submit_button_selector)

def user_role_page(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.admin_page_selector)
    actions_for_pages.click_action(page, locate.user_role_selector)
    actions_for_pages.click_action(page, locate.ess_role_selector)
    actions_for_pages.click_action(page, locate.ghost_button_selector)
    return page.locator(locate.user_role_text_selector).text_content()

def search_invalid_username_page(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.admin_page_selector)
    actions_for_pages.type_action(page, locate.username_search_selector, const.invalid_search_username)
    actions_for_pages.click_action(page, locate.search_submit_button_selector)
    return page.locator(locate.no_records_found_selector).text_content()