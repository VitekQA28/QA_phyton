from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainCalc import Calculator
from pages.WaitCalc import Waiting


def test_calculator_result():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    data_types = Calculator(browser) #Открыть сайт
    data_types.data_types() # ввести на калькуляторе 7 + 8 = 15 (ответ должен отобразиться через 45 секунд)
    waiting_calc = Waiting(browser)
    result = waiting_calc.waiting_calc() #вытащить информацию из поля результат, через 45 секунд.
    
    # Проверить, что сумма чисел 7 + 8 равна 15 и это значение отобразилось через 45 секунд ожидания.
    try:
        assert result == "15"
        print("Результат соответствует числу 15")
    except TimeoutException:
        print("Результат не появился или не соответствует числу 15 после 45 секунд ожидания")
    browser.quit()
    

