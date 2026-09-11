from playwright.async_api import Page
from helper import actions
from helper import locators as locate
from helper import constants_page as const

def login_with_valid(page: Page):
    actions.type_action(page,locate.username_selector, const.username_admin)
    actions.type_action(page,locate.password_selector, const.password_admin)
    actions.click_action(page,locate.submit_button_selector)

def login_with_multiple_users(page,username,password):
    actions.type_action(page, locate.username_selector, username)
    actions.type_action(page, locate.password_selector, password)
    actions.click_action(page, locate.submit_button_selector)


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

def navigate_to_pim(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.pim_user_selector)
    return actions.get_text_action(page, locate.pim_header_selector)

def search_emp_id_page(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.pim_user_selector)

def navigate_to_add_employee(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.pim_user_selector)
    actions.click_action(page, locate.add_employee_selector)
    return actions.get_text_action(page, locate.add_employee_header_selector)

def add_employee_required_fields(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.pim_user_selector)
    actions.click_action(page, locate.add_employee_selector)
    actions.click_action(page, locate.submit_button_selector)
    return page.locator(locate.required_selector).first.text_content()

def pim_reset_search_filter(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.pim_user_selector)
    actions.type_action(page, locate.employee_id_selector, const.employee_id)
    actions.click_action(page, locate.ghost_button_selector)
    return page.locator(locate.employee_id_selector).input_value()

def navigate_to_leave(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.leave_page_selector)
    return actions.get_text_action(page, locate.leave_header_selector)

def leave_apply_navigation(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.leave_page_selector)
    actions.click_action(page, locate.apply_leave_selector)
    return actions.get_text_action(page, locate.apply_leave_header_selector)

def leave_my_leave_navigation(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.leave_page_selector)
    actions.click_action(page, locate.my_leave_selector)
    return actions.get_text_action(page, locate.my_leave_header_selector)

def leave_search_reset(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.leave_page_selector)
    actions.click_action(page, locate.sub_unit_selector)
    actions.click_action(page, locate.engineering_selector)
    actions.click_action(page, locate.ghost_button_selector)
    return actions.get_text_action(page, locate.sub_unit_text_selector)

def navigate_to_recruitment(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.recruitment_page_selector)
    return actions.get_text_action(page, locate.recruitment_header_selector)

def navigate_to_vacancies(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.recruitment_page_selector)
    actions.click_action(page, locate.vacancies_selector)
    return actions.get_text_action(page, locate.vacancies_header_selector)

def recruitment_add_candidate_form(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.recruitment_page_selector)
    actions.click_action(page, locate.add_button_selector)
    return actions.get_text_action(page, locate.add_candidate_header_selector)

def add_candidate_required_validation(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.recruitment_page_selector)
    actions.click_action(page, locate.add_button_selector)
    actions.click_action(page, locate.submit_button_selector)
    return page.locator(locate.required_selector).first.text_content()

def recruitment_reset_filter(page: Page):
    actions.type_action(page, locate.username_selector, const.username_admin)
    actions.type_action(page, locate.password_selector, const.password_admin)
    actions.click_action(page, locate.submit_button_selector)
    actions.click_action(page, locate.recruitment_page_selector)
    actions.click_action(page, locate.job_title_selector)
    actions.click_action(page, locate.automation_tester_selector)
    actions.click_action(page, locate.ghost_button_selector)
    return actions.get_text_action(page, locate.job_title_text_selector)

