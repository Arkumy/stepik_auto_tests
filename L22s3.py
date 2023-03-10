from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    y_element = browser.find_element(By.ID, "num2")
    x = x_element.text
    y = y_element.text

    m = str(int(x)+int(y))


    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(m))

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:

    time.sleep(10)
    browser.quit()
