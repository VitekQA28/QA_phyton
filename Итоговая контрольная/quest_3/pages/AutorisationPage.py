from selenium.webdriver.common.by import By
import allure 

@allure.suite("Работа со Страницей авторизации")
class Autorisation:
    @allure.title("Открытие браузера")
    def __init__(self, driver)->None:
        """
        Эта функция открывает браузер

        затем переходит на страницу по URL

        и открывает окно браузера на весь экран

        """
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()
   
    @allure.title("Заполнение полей авторизции {name} / {password}")
    def get_login(self, name, password)->str:
        """
        Эта функция заполняет по локатору поля данными авторизации

        и кликает на кнопку входа.

        """
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(name)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()