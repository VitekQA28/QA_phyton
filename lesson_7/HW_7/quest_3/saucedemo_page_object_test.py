
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.AutorisationPage import Autorisation
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage
from pages.MainPage import MainPage
from pages.YourInformation import YourInformation

def test_cart_finish_price():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    auto_page = Autorisation(browser)
    auto_page.get_login('standard_user', 'secret_sauce')

    main_page = MainPage(browser)
    main_page.add_to_cart()

    cart_page = CartPage(browser)
    cart_page.get()

    info_page = YourInformation(browser)
    info_page.get_form('Vitek', 'Bud', '424000')

    finish_price = ResultPage(browser)
    to_be = finish_price.total_price()
    
    sleep(5)
    browser.quit()

    assert to_be == 'Total: $58.29'
    if to_be == 'Total: $58.29':
        print("Проверка пройдена успешно!")
    else:
        print("Проверка не пройдена!")

    sleep(5)
    



