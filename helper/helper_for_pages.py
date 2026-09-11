def open_website(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

def assert_page(actual, expected):
    assert actual == expected
