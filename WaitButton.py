import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from func import func_click_reg

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    message = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
        )

    button = browser.find_element(By.ID, "book")
    button.click()

    func_click_reg(browser)

    alert = browser.switch_to.alert
    print(alert.text)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()