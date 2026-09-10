import pytest
from playwright.async_api import Page

@pytest.mark.skip
def test_search_emp_id(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/")
    page.locator("input[name='username']").type("Admin")
    page.locator("input[name='password']").type("admin12")
    page.locator("button[type='submit']").click()
    page.locator('//span[text()="PIM"]').click()
