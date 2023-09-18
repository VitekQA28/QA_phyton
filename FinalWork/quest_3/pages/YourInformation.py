from selenium.webdriver.common.by import By
import allure


@allure.suite("Работа со Страницей корзины")
class YourInformation:
    @allure.title("Открытие браузера")
    def __init__(self, driver):
        """
        Эта функция открывает браузер

        затем переходит на страницу по URL

        и открывает окно браузера на весь экран

        """
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/checkout-step-one.html')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()
   
    @allure.title("Заполняем поля {first_name} , {last_name} персональными данными и вводим {code} ")
    def get_form(self, first_name: str, last_name: str, code: str)->str:
        """
        Эта функция передает в форму данные

        """
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(code)
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()