from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.suite("Работа с результатом покупки")
class ResultPage:
    @allure.title("Открытие браузера")
    def __init__(self, browser)->None:
        """
        Эта функция открывает браузер
        """
        self._driver = browser

    @allure.title("Получаем итоговую стоимость товара в корзине")
    def total_price(self)->str:
        """
        Эта функция по слектору "summary_total_label" считывает сумму покупки

        """
        total_price = WebDriverWait(self._driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
    ).text
        return total_price
