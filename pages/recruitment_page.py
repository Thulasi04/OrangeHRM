from playwright.sync_api import Page
from helper import actions_for_pages
from helper import recruitment_locators as locate
from helper import constants_for_pages as const


def navigate_to_recruitment(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.recruitment_page_selector)
    return actions_for_pages.get_text_action(page, locate.recruitment_header_selector)

def navigate_to_vacancies(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.recruitment_page_selector)
    actions_for_pages.click_action(page, locate.vacancies_selector)
    return actions_for_pages.get_text_action(page, locate.vacancies_header_selector)

def recruitment_add_candidate_form(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.recruitment_page_selector)
    actions_for_pages.click_action(page, locate.add_button_selector)
    return actions_for_pages.get_text_action(page, locate.add_candidate_header_selector)

def add_candidate_required_validation(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.recruitment_page_selector)
    actions_for_pages.click_action(page, locate.add_button_selector)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    return page.locator(locate.required_selector).first.text_content()

def recruitment_reset_filter(page: Page):
    actions_for_pages.type_action(page, locate.username_selector, const.username_admin)
    actions_for_pages.type_action(page, locate.password_selector, const.password_admin)
    actions_for_pages.click_action(page, locate.submit_button_selector)
    actions_for_pages.click_action(page, locate.recruitment_page_selector)
    actions_for_pages.click_action(page, locate.job_title_selector)
    actions_for_pages.click_action(page, locate.automation_tester_selector)
    actions_for_pages.click_action(page, locate.ghost_button_selector)
    return actions_for_pages.get_text_action(page, locate.job_title_text_selector)