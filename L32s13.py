from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


def assertEqual(welcome_text_elt, welcome_text, param):
    pass


class TestAbs(unittest.TestCase):
    def test_1(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get("http://suninjuly.github.io/registration1.html")
        elem = driver.find_element(By.CSS_SELECTOR, ".first_block .first")
        elem.send_keys("Ivan")
        elem2 = driver.find_element(By.CSS_SELECTOR, ".first_block > .form-group.second_class > .form-control.second")
        elem2.send_keys("Petrov")
        elem3 = driver.find_element(By.CLASS_NAME, "form-control.third")
        elem3.send_keys("petrov@gmail.com")
        elem4 = driver.find_element(By.XPATH, '//button[text()="Submit"]')
        elem4.click()
        time.sleep(1)
        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        message: str = "Congratulations! You have successfully registered!"
        assertEqual(welcome_text_elt, welcome_text, "Congratulations! You have successfully registered!")

    def test2(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get("http://suninjuly.github.io/registration2.html")
        elem = driver.find_element(By.CSS_SELECTOR, ".first_block .first")
        elem.send_keys("Ivan")
        elem2 = driver.find_element(By.CSS_SELECTOR, ".first_block > .form-group.second_class > .form-control.second")
        elem2.send_keys("Petrov")
        elem3 = driver.find_element(By.CLASS_NAME, "form-control.third")
        elem3.send_keys("petrov@gmail.com")
        elem4 = driver.find_element(By.XPATH, '//button[text()="Submit"]')
        elem4.click()
        time.sleep(1)
        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        message: str = "Congratulations! You have successfully registered!"
        assertEqual(welcome_text_elt, welcome_text, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()