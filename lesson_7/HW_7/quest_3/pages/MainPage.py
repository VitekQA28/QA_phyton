
from selenium.webdriver.common.by import By

class MainPage:
    

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/inventory.html')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def add_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, ('button[name="add-to-cart-sauce-labs-backpack"]')).click()
        self._driver.find_element(By.CSS_SELECTOR, ('button[name="add-to-cart-sauce-labs-bolt-t-shirt"]')).click()
        self._driver.find_element(By.CSS_SELECTOR, ('button[name="add-to-cart-sauce-labs-onesie"]')).click()