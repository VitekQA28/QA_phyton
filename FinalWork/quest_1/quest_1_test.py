from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from DataTypes import DataTypes
from ColorLine import ColorLine
import allure 


@allure.title("Заполнение таблицы данными")
@allure.description("Заполнение таблицы данными и проверка подсветки ячеек таблицы")
@allure.feature("Таблица")
@allure.severity("Critical")
def test_practice_site():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Открыть сайт"):
        data_types = DataTypes(browser) 
    with allure.step("Заполнить поля данными"):
        data_types.data_types()
    with allure.step("Получаем данные со страницы браузера"):
        color_line = ColorLine(browser)
        with allure.step("Определить цвет пустого поля"):
            color_line.empty_line_color() 
        with allure.step("Определить цвет заполненных полей"):    
            color_line.color_of_filled_lines()
    with allure.step("Переопределили переменную для красного цвета"):
        color_red = color_line.empty_line_color()
    with allure.step("Переопределили переменную для зеленого цвета"):    
        color_green = color_line.color_of_filled_lines() 
    with allure.step("Проверка, что цвет пустого поля равен красному"):
        assert color_red == 'rgba(248, 215, 218, 1)' 
    with allure.step("Проверка, что цвет заполненого поля равен зеленому"):
        assert color_green == 'rgba(209, 231, 221, 1)'
    with allure.step("Закрываем браузер"):
        browser.quit()
    
