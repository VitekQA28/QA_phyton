from selenium.webdriver.common.by import By
import allure 



@allure.suite("Работа с цветом ячеек в таблице")
class DataTypes:
    @allure.title("Открытие браузера")
    def __init__(self, browser):
        """
        Эта функция открывает браузер

        затем переходит на страницу по URL

        и открывает окно браузера на весь экран

        """
        self._driver = browser
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    @allure.title("Получение новой организации по ID")
    def data_types(self) ->str:
        """
        Эта функция содержит в себе список массив данных

        эти данные подставляются в таблицу по селектору

        данные передаются в формате str

        """
        self._driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys('Иван')
        self._driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys('Петров')
        self._driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys('Ленина, 55-3')
        self._driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys('test@skypro.com')
        self._driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys('QA')
        self._driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys()
        self._driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys('Москва')
        self._driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys('Россия')
        self._driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys('+7985899998787')
        self._driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys('SkyPro')
        self._driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()    