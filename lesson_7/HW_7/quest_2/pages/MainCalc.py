from selenium.webdriver.common.by import By

class Calculator:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.maximize_window()

    def data_types(self):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys('45')
        self._driver.find_element(By.XPATH, "//span[contains(text(),'7')]").click()
        self._driver.find_element(By.XPATH, "//span[contains(text(),'+')]").click()
        self._driver.find_element(By.XPATH, "//span[contains(text(),'8')]").click()
        self._driver.find_element(By.XPATH, "//span[contains(text(),'=')]").click()