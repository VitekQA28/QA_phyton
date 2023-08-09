from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from DataTypes import DataTypes
from ColorLine import ColorLine


def test_practice_site():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    data_types = DataTypes(browser) #Открыть сайт
    data_types.data_types() #Заполнить поля данными

    color_line = ColorLine(browser)
    color_line.empty_line_color() #Определить цвет пустого поля
    color_line.color_of_filled_lines() #Определить цвет заполненных полей
    color_red = color_line.empty_line_color() #Переопределили переменную для красного цвета
    color_green = color_line.color_of_filled_lines() #Переопределили переменную для зеленого цвета

    assert color_red == 'rgba(248, 215, 218, 1)' # проверка, что цвет подсвеченного поля равен красному
    assert color_green == 'rgba(209, 231, 221, 1)' # проверка, что цвет подсвеченного поля равен зеленому
    
    browser.quit()
    
