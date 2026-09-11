from playwright.sync_api import Page
from helper import actions_for_pages
from helper import leave_locators as locate
from helper import constants_for_pages as const


def navigate_to_leave(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.leave_page_selector)
    return actions_for_pages.get_text_action(page, locate.leave_header_selector)

def leave_apply_navigation(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.leave_page_selector)
    actions_for_pages.click_action(page, locate.apply_leave_selector)
    return actions_for_pages.get_text_action(page, locate.apply_leave_header_selector)

def leave_my_leave_navigation(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.leave_page_selector)
    actions_for_pages.click_action(page, locate.my_leave_selector)
    return actions_for_pages.get_text_action(page, locate.my_leave_header_selector)

def leave_search_reset(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.leave_page_selector)
    actions_for_pages.click_action(page, locate.sub_unit_selector)
    actions_for_pages.click_action(page, locate.engineering_selector)
    actions_for_pages.click_action(page, locate.ghost_button_selector)
    return actions_for_pages.get_text_action(page, locate.sub_unit_text_selector)