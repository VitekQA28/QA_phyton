from page.AuthPage import AuthPage
from page.MainPage import MainPage
import time
import allure
import pytest


@pytest.mark.skip
def test_auth(browser):
    email = "another.yola@gmail.com"
    password = "Vitechkin90"
    username = "Viktor Budnik"
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_accautnt_info()

    time.sleep(1)
    current_url = main_page.get_current_url()
    with allure.step("Проверка, что URL " + current_url + "заканчивается на viktorbudnik/boards"):
        assert current_url.endswith("viktorbudnik/boards")
    with allure.step("Проверка данных пользователя"):
        with allure.step("Имя пользователя должно быть "+username):
            assert info[0] == username
        with allure.step("Почта пользователя должна быть "+email):
            assert info[1] == email
   


