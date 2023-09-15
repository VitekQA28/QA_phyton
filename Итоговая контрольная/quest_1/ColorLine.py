from selenium.webdriver.common.by import By
import allure 

@allure.suite("Работа с цветом ячеек в таблице")
class ColorLine:
    def __init__(self, browser):
        self._driver = browser
    
    @allure.title("Проверка цвета незаполненых полей")
    def empty_line_color(self)->str: #проверка цвета незаполненых полей
        """
        Эта функция проверяет наличие пустых ячеек в таблице

        по селектору '.alert.py-2.alert-danger' 

        и возвращает код цвета в виде текста 'rgba(000, 000, 000, 0)'

        """
        self._driver.implicitly_wait(5)
        red = self._driver.find_element(By.CSS_SELECTOR, '.alert.py-2.alert-danger').value_of_css_property('background-color')
        color_red = red
        return color_red
    
    @allure.title("Проверка цвета заполненых полей")
    def color_of_filled_lines(self) ->str:
        """
        Эта функция проверяет наличие заполненных ячеек в таблице

        по селектору '.alert.py-2.alert-success' 

        и возвращает код цвета в виде текста 'rgba(000, 000, 000, 0)'

        """
        self._driver.implicitly_wait(5)
        green = self._driver.find_element(By.CSS_SELECTOR, '.alert.py-2.alert-success').value_of_css_property('background-color')
        color_green = green
        return color_green