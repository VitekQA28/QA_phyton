from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainCalc import Calculator
from pages.WaitCalc import Waiting


def test_calculator_result():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    data_types = Calculator(browser) #Открыть сайт
    data_types.data_types() 
    waiting_calc = Waiting(browser)
    result = waiting_calc.waiting_calc()
    

    try:
        assert result == "15"
        print("Результат соответствует числу 15")
    except TimeoutException:
        print("Результат не появился или не соответствует числу 15 после 45 секунд ожидания")
    browser.quit()
    

