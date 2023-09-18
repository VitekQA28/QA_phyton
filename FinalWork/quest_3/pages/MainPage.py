
from selenium.webdriver.common.by import By
import allure

@allure.suite("Работа с главной страницей сайта")
class MainPage:
    
    @allure.title("Открытие браузера")
    def __init__(self, driver)->None:
        """
        Эта функция открывает браузер

        затем переходит на страницу по URL

        и открывает окно браузера на весь экран

        """
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/inventory.html')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    @allure.title("Добавляем товары в корзину")
    def add_to_cart(self)->None:
        """
        Эта функция кликает на кнопку "Корзину" по селектору

        """
        self._driver.find_element(By.CSS_SELECTOR, ('button[name="add-to-cart-sauce-labs-backpack"]')).click()
        self._driver.find_element(By.CSS_SELECTOR, ('button[name="add-to-cart-sauce-labs-bolt-t-shirt"]')).click()
        self._driver.find_element(By.CSS_SELECTOR, ('button[name="add-to-cart-sauce-labs-onesie"]')).click()