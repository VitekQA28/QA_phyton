from selenium.webdriver.common.by import By

class YourInformation:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/checkout-step-one.html')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()
   

    def get_form(self, first_name, last_name, code):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(code)
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()