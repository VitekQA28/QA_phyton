from selenium.webdriver.common.by import By
import allure 

@allure.suite("Работа с калькулятором")
class Calculator:
    @allure.title("Проверка цвета незаполненых полей")
    def __init__(self, browser)->None:
        """
        Эта функция открывает браузер

        затем переходит на страницу по URL

        и открывает окно браузера на весь экран

        """
        with allure.step("Открываем окно браузера и разворачиваем на весь экран"): 
            self._driver = browser
            self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
            self._driver.maximize_window()

    @allure.title("Устанавливаем таймер 45 секунд и вводим данные на калькуляторе")
    def data_types(self)->str:
        """
        Эта функция устанавливает время на таймере
        
        Вводит данные на калькуляторе
        """
        with allure.step("Очищием поле ввода"):
            self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        with allure.step("Устанавливаем таймер 45 секунд"):
            self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys('45')
        with allure.step("Вводим данные на калькуляторе по селектору"):
            self._driver.find_element(By.XPATH, "//span[contains(text(),'7')]").click()
            self._driver.find_element(By.XPATH, "//span[contains(text(),'+')]").click()
            self._driver.find_element(By.XPATH, "//span[contains(text(),'8')]").click()
            self._driver.find_element(By.XPATH, "//span[contains(text(),'=')]").click()