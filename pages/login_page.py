from playwright.async_api import Page
from helper import actions
from helper import locators as locate
from helper import constants_page as const

def login_with_valid(page: Page):
    actions.type_action(page,locate.username_selector, const.username_admin)
    actions.type_action(page,locate.password_selector, const.password_admin)
    actions.click_action(page,locate.submit_button_selector)

def login_with_invalid_username(page: Page):
   actions.type_action(page,locate.username_selector, const.invalid_username)
   actions.type_action(page,locate.password_selector, const.invalid_password)
   actions.click_action(page,locate.submit_button_selector)

def login_with_invalid_password(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page,locate.password_selector, const.login_invalid_password)
    actions.click_action(page, locate.submit_button_selector)

def empty_login_page(page: Page):
    actions.click_action(page, locate.submit_button_selector)

def forgot_password_page(page: Page):
    actions.click_action(page, locate.forgot_password_selector)

def login_with_admin_page(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.admin_page_selector)

def search_user_page(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.admin_page_selector)
    actions.type_action(page, locate.search_user_selector, const.username_admin )
    actions.click_action(page, locate.submit_button_selector)

def add_user_role_page(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.admin_page_selector)
    actions.click_action(page, locate.user_role_selector)
    actions.click_action(page, locate.ess_role_selector)
    actions.click_action(page, locate.search_submit_button_selector)

def user_role_page(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.admin_page_selector)
    actions.click_action(page, locate.user_role_selector)
    actions.click_action(page, locate.ess_role_selector)
    actions.click_action(page, locate.ghost_button_selector)
    return actions.get_text_action(page, locate.user_role_text_selector)

def search_invalid_username_page(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.admin_page_selector)
    actions.type_action(page,locate.username_search_selector,const.invalid_search_username)
    actions.click_action(page, locate.submit_button_selector)
    return actions.get_text_action(page, locate.no_records_found_selector)