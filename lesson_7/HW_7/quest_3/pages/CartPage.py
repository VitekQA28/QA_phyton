from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, browser):
        self._driver = browser

    def get(self):
        self._driver.get('https://www.saucedemo.com/cart.html')    

    def go_to_checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    
    