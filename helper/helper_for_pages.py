from playwright.async_api import Page

def open_website(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

def assert_page(actual, expected):
    assert actual == expected
