from playwright.async_api import Page
from helper import actions_for_pages
from helper import constants_for_pages as const
from locators import pim_locators as locate

def navigate_to_pim(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.pim_user_selector)

def search_emp_id_page(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.pim_user_selector)

def navigate_to_add_employee(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.pim_user_selector)
    actions_for_pages.click_action(page, locate.add_employee_selector)
    return page.locator(locate.add_employee_header_selector).text_content()

def add_employee_required_fields(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.pim_user_selector)
    actions_for_pages.click_action(page, locate.add_employee_selector)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    return page.locator(locate.required_selector).first.text_content()

def pim_reset_search_filter(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.pim_user_selector)
    actions_for_pages.type_action(page, locate.employee_id_selector, const.employee_id)
    actions_for_pages.click_action(page, locate.ghost_button_selector)
    return page.locator(locate.employee_id_selector).input_value()