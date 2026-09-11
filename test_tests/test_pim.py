import pytest
from playwright.async_api import Page
from pages import login_page as login
from helper import helper_for_pages as hp


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