from selenium.webdriver.common.by import By
import allure 

@allure.suite("Работа со Страницей корзины")
class CartPage:
    @allure.title("Открытие браузера")
    def __init__(self, browser)->None:
        """
        Эта функция открывает браузер
        """
        self._driver = browser

    @allure.title("Открываем страницу по URL")
    def get(self)->None:
        """
        Переходит на страницу по URL
        """
        self._driver.get('https://www.saucedemo.com/cart.html') 

    @allure.title("Переход к заполнению персональных данных ")
    def go_to_checkout(self)->None:
        """
        Нажимает на кнопку по селектору #checkout
        """
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    
    