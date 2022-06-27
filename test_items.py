import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_searching_button_link(browser):
    browser.get(link)
    time.sleep(30)
    button = len(browser.find_elements(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket"))
    assert button > 0, 'кнопку сляvздили, купить нельзя'