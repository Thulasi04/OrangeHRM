def type_action(page,selector,value):
    page.locator(selector).type(value)

def click_action(page,selector):
    page.locator(selector).click()

def get_text_action(page, selector):
    return page.locator(selector).text_content()