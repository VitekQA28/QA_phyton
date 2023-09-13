
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.AutorisationPage import Autorisation
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage
from pages.MainPage import MainPage
from pages.YourInformation import YourInformation
import allure

@allure.title("Проверка итоговой стоимости добавленного товара в корзину")
@allure.description("Добавление товара в корзину и проверка итоговой стоимости")
@allure.feature("Магазин")
@allure.severity("Critical")
def test_cart_finish_price(): #Сравнение стоимости товара и итоговой суммой в корзине
    with allure.step("Открыть браузер"):
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        with allure.step("Перейти на страницу авторизации"):
            auto_page = Autorisation(browser)
        with allure.step("Ввести данные для авторизации"):
            auto_page.get_login('standard_user', 'secret_sauce') 
    with allure.step("Перейти на главную страницу магазина"):
        main_page = MainPage(browser) 
    with allure.step("Добавить товары в корзину"):
        main_page.add_to_cart()

    with allure.step("Перейти в корзину магазина"):
        cart_page = CartPage(browser)
        cart_page.get() 

    with allure.step("Перейти на страницу для заполнения персональных данных"):
        info_page = YourInformation(browser)
    with allure.step("Заполнение персональных данных заказчика"):
        info_page.get_form('Vitek', 'Bud', '424000')

    with allure.step("Получение информации по стоимости добавленных товаров в корзину"):
        finish_price = ResultPage(browser)
        to_be = finish_price.total_price() 
    
    sleep(5)
    browser.quit()
    with allure.step("Проверка, что стоимость всех добавленных товаров в корзину соответствует ожиданию"):
    
        assert to_be == 'Total: $58.29'
        if to_be == 'Total: $58.29':
            print("Проверка пройдена успешно!")
        else:
            print("Проверка не пройдена!")

    sleep(5)
    



