
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.AutorisationPage import Autorisation
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage
from pages.MainPage import MainPage
from pages.YourInformation import YourInformation

def test_cart_finish_price(): #Сравнение стоимости товара и итоговой суммой в корзине
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    auto_page = Autorisation(browser)
    auto_page.get_login('standard_user', 'secret_sauce') # Авторизация пользователя

    main_page = MainPage(browser) 
    main_page.add_to_cart() #Добавление товара в корзину

    cart_page = CartPage(browser)
    cart_page.get() # Переход на страницу корзины

    info_page = YourInformation(browser)
    info_page.get_form('Vitek', 'Bud', '424000') # Заполнение персональных данных заказчика

    finish_price = ResultPage(browser)
    to_be = finish_price.total_price() # Получение информации по стоимости добавленных товаров в корзину
    
    sleep(5)
    browser.quit()
    # Проверка, что стоимость всех добавленных товаров в корзину соответствует ожиданию.
    assert to_be == 'Total: $58.29'
    if to_be == 'Total: $58.29':
        print("Проверка пройдена успешно!")
    else:
        print("Проверка не пройдена!")

    sleep(5)
    



