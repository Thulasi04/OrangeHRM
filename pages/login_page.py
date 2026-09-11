from playwright.async_api import Page
from helper import actions_for_pages
from helper import constants_for_pages as const
from locators import login_locators as locate


def login_with_valid(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)

def login_with_multiple_users(page: Page, username, password):
    actions_for_pages.type_action(page, locate.username_selector, username)
    actions_for_pages.type_action(page, locate.password_selector, password)
    actions_for_pages.click_action(page, locate.submit_button_selector)

def login_with_invalid_username(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.invalid_username)
    actions_for_pages.type_action(page, locate.password_selector, const.invalid_password)
    actions_for_pages.click_action(page, locate.submit_button_selector)

def login_with_invalid_password(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.login_invalid_password)
    actions_for_pages.click_action(page, locate.submit_button_selector)

def empty_login_page(page: Page):
    actions_for_pages.click_action(page, locate.submit_button_selector)

def forgot_password_page(page: Page):
    actions_for_pages.click_action(page, locate.forgot_password_selector)

