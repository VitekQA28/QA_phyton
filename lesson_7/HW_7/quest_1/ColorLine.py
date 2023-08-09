from selenium.webdriver.common.by import By

class ColorLine:
    def __init__(self, browser):
        self._driver = browser
    
    def empty_line_color(self): #проверка цвета незаполненых полей
        self._driver.implicitly_wait(5)
        red = self._driver.find_element(By.CSS_SELECTOR, '.alert.py-2.alert-danger').value_of_css_property('background-color')
        color_red = red
        return color_red
    
    def color_of_filled_lines(self): #проверка цвета заполненых полей
        self._driver.implicitly_wait(5)
        green = self._driver.find_element(By.CSS_SELECTOR, '.alert.py-2.alert-success').value_of_css_property('background-color')
        color_green = green
        return color_green