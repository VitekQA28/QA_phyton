from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainCalc import Calculator
from pages.WaitCalc import Waiting
import allure 

@allure.title("Проверка результата калькулятора")
@allure.description("Проверить, что сумма чисел 7 + 8 равна 15 и это значение отобразилось через 45 секунд ожидания")
@allure.feature("Калькулятор")
@allure.severity("Critical")
def test_calculator_result():
    with allure.step("Открываем браузер Chrome"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        with allure.step("Открываем страницу сайта"):
            data_types = Calculator(browser) 
        with allure.step("Ввести на калькуляторе 7 + 8 = 15"):
            data_types.data_types()     
        waiting_calc = Waiting(browser)
    with allure.step("Сохраняем информацию полученную через 45 секунд"):
        result = waiting_calc.waiting_calc()
    with allure.step("Проверить, что сумма чисел 7 + 8 равна 15 и это значение отобразилось через 45 секунд ожидания"):
        try:
            assert result == "15"
            print("Результат соответствует числу 15")
        except TimeoutException:
            print("Результат не появился или не соответствует числу 15 после 45 секунд ожидания")
    with allure.step("Закрываем браузер"): 
        browser.quit()
    

