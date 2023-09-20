from page.AuthPage import AuthPage
from page.MainPage import MainPage
import time
import allure
import pytest

@pytest.mark.ui
def test_auth(browser, test_data:dict):
    email = test_data.get("email")
    password = test_data.get("password")
    username = test_data.get("username")
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
   


