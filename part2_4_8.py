from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
   )

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer").send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    time.sleep(15)
    browser.quit()