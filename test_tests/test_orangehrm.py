import pytest
from playwright.async_api import Page
from pages import login_page as login
from helper import helper_for_pages as hp

@pytest.mark.regression
def test_navigate_to_login(page: Page):
    hp.open_website(page)
    title = page.title()
    hp.assert_page(title,"OrangeHRM")

@pytest.mark.regression
def test_valid_login(page: Page):
    hp.open_website(page)
    login.login_with_valid(page)
    header = page.locator('//h6[text()="Dashboard"]').text_content()
    hp.assert_page(header,"Dashboard")

@pytest.mark.regression
def test_invalid_username(page: Page):
    hp.open_website(page)
    login.login_with_invalid_username(page)
    invalid = page.locator('[class="oxd-text oxd-text--p oxd-alert-content-text"]').text_content()
    hp.assert_page(invalid ,"Invalid credentials")

@pytest.mark.regression
def test_invalid_password(page: Page):
    hp.open_website(page)
    login.login_with_invalid_password(page)
    invalid = page.locator('[class="oxd-text oxd-text--p oxd-alert-content-text"]').text_content()
    hp.assert_page(invalid ,"Invalid credentials")

@pytest.mark.regression
def test_empty_fields(page: Page):
    hp.open_website(page)
    login.empty_login_page(page)
    required = page.locator("//span[text()='Required']").first.text_content()
    hp.assert_page(required,"Required")

@pytest.mark.regression
def test_forgot_password(page: Page):
    hp.open_website(page)
    login.forgot_password_page(page)
    reset_header = page.locator('h6[class="oxd-text oxd-text--h6 orangehrm-forgot-password-title"]').text_content()
    hp.assert_page(reset_header,"Reset Password")
    page.wait_for_timeout(5000)

@pytest.mark.adminfeature
def test_navigate_to_admin(page: Page):
    hp.open_website(page)
    login.login_with_admin_page(page)
    admin = page.locator('a[class="oxd-main-menu-item active"]').text_content()
    hp.assert_page(admin,"Admin")

@pytest.mark.adminfeature
def test_admin_search_user(page: Page):
    hp.open_website(page)
    login.search_user_page(page)
    record_found = page.locator('//span[text()="(1) Record Found"]').text_content()
    hp.assert_page(record_found, "(1) Record Found")

@pytest.mark.adminfeature
def test_add_user_role(page: Page):
    hp.open_website(page)
    login.add_user_role_page(page)
    user_role = page.locator('//div[@role="rowgroup"]//div[@role="cell"]//div[text()="ESS"]').first.text_content()
    hp.assert_page(user_role,"ESS")
    page.wait_for_timeout(5000)

@pytest.mark.adminfeature
def test_reset_user_role_filter(page: Page):
    hp.open_website(page)
    reset_text =  login.user_role_page(page)
    hp.assert_page(reset_text,"-- Select --")

@pytest.mark.adminfeature
def test_search_invalid_username(page: Page):
    hp.open_website(page)
    no_records_msg = login.search_invalid_username_page(page)
    hp.assert_page(no_records_msg, "No Records Found")
    page.wait_for_timeout(5000)

@pytest.mark.pimfeature
def test_navigate_to_pim(page: Page):
    hp.open_website(page)
    pim_header = login.navigate_to_pim(page)
    hp.assert_page(pim_header, "PIM")

@pytest.mark.pimfeature
def test_search_emp_id(page: Page):
    hp.open_website(page)
    login.search_emp_id_page(page)

@pytest.mark.pimfeature
def test_navigate_to_add_employee(page: Page):
    hp.open_website(page)
    heading = login.navigate_to_add_employee(page)
    hp.assert_page(heading, "Add Employee")

@pytest.mark.pimfeature
def test_add_employee_required_fields(page: Page):
    hp.open_website(page)
    required = login.add_employee_required_fields(page)
    hp.assert_page(required, "Required")

@pytest.mark.pimfeature
def test_pim_reset_search_filter(page: Page):
    hp.open_website(page)
    emp_id_val = login.pim_reset_search_filter(page)
    hp.assert_page(emp_id_val, "")

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
def test_apply_leave_required_validation(page: Page):
    hp.open_website(page)
    required_msg = login.apply_leave_required_validation(page)
    hp.assert_page(required_msg, "Required")

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

@pytest.mark.recruitmentfeature
def test_navigate_to_recruitment(page: Page):
    hp.open_website(page)
    header = login.navigate_to_recruitment(page)
    hp.assert_page(header, "Recruitment")

@pytest.mark.recruitmentfeature
def test_navigate_to_vacancies(page: Page):
    hp.open_website(page)
    heading = login.navigate_to_vacancies(page)
    hp.assert_page(heading, "Vacancies")

@pytest.mark.recruitmentfeature
def test_recruitment_add_candidate_form(page: Page):
    hp.open_website(page)
    heading = login.recruitment_add_candidate_form(page)
    hp.assert_page(heading, "Add Candidate")

@pytest.mark.recruitmentfeature
def test_add_candidate_required_validation(page: Page):
    hp.open_website(page)
    required_msg = login.add_candidate_required_validation(page)
    hp.assert_page(required_msg, "Required")

@pytest.mark.recruitmentfeature
def test_recruitment_reset_filter(page: Page):
    hp.open_website(page)
    reset_text = login.recruitment_reset_filter(page)
    hp.assert_page(reset_text, "-- Select --")
