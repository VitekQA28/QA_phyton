from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from configuration.ConfigProvider import ConfigProvider
from selenium.webdriver.support import expected_conditions as EC
import allure

class AuthPage:

    def __init__ (self, driver: WebDriver) ->None:

        url = ConfigProvider().get("ui", "base_url")
        self.__url = url+"/login?returnUrl=%2Fu%2Fviktorbudnik%2Fboards"
        self.__driver = driver

    @allure.step("Перейти на страницу авторизации")
    def go(self):
        self.__driver.get(self.__url)

    @allure.step("Авторизоваться под {email}:{password}")
    def login_as(self, email: str, password: str)->str:
        self.__driver.find_element(By.CSS_SELECTOR, "#user").send_keys(email)
        self.__driver.find_element(By.CSS_SELECTOR, "#login").click()
        #Дожидаемся когда отобразиться окно "password"
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "svg[role=presentation]")))
        self.__driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()

    def get_current_url(self):
        return self.__driver.current_url

