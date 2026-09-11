import pytest
from playwright.async_api import Page
from pages import recruitment_page as recruitment
from helper import helper_for_pages as hp
from locators import recruitment_locators as locate
@pytest.mark.recruitmentfeature
def test_navigate_to_recruitment(page: Page):
    hp.open_website(page)
    header = recruitment.navigate_to_recruitment(page)
    hp.assert_page(header, "Recruitment")

@pytest.mark.recruitmentfeature
def test_navigate_to_vacancies(page: Page):
    hp.open_website(page)
    heading = recruitment.navigate_to_vacancies(page)
    hp.assert_page(heading, "Vacancies")

@pytest.mark.recruitmentfeature
def test_recruitment_add_candidate_form(page: Page):
    hp.open_website(page)
    heading = recruitment.recruitment_add_candidate_form(page)
    hp.assert_page(heading, "Add Candidate")

@pytest.mark.recruitmentfeature
def test_add_candidate_required_validation(page: Page):
    hp.open_website(page)
    required_msg = recruitment.add_candidate_required_validation(page)
    hp.assert_page(required_msg, "Required")

@pytest.mark.recruitmentfeature
def test_recruitment_reset_filter(page: Page):
    hp.open_website(page)
    reset_text = recruitment.recruitment_reset_filter(page)
    hp.assert_page(reset_text, "-- Select --")