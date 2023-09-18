from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.suite("Работа с ожиданием")
class Waiting:
    @allure.title("Открытие браузера")
    def __init__(self, browser)->None:
        """
        Эта функция открывает браузер

        """
        self._driver = browser

    @allure.title("Ожидание результата")
    def waiting_calc(self) ->str:
        """
        Эта функция устанавливает ожидание операции на время N секунд

        затем забирает информцию из поля по селектору

        и возвращает результат в текстовом формате

        """ # Ожидаем 45 секунд и вытаскиваем информацию из поля результат, который должен равняться 15
        WebDriverWait(self._driver, 46).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        result = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result