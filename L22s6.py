from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)


    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.NAME, "ruler")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    option3 = browser.find_element(By.ID, "robotsRule")
    option3.click()

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()


finally:

    time.sleep(10)
    browser.quit()