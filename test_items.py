import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_submit_button(browser):
    browser.get(link)
    #time.sleep(30)

    #but = browser.find_element_by_css_selector("button.btn-add-to-basket")#("button.btn")
    assert None !=  browser.find_element_by_css_selector("button.btn-add-to-basket"), "Button is not found"
