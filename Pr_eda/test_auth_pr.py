from AuthPagePr import AuthPagePr
import allure
import pytest


@allure.epic("Авторизация")
def test_auth():
    main_page = AuthPagePr('browser')
    main_page.open_auth_window()
    main_page.login_as()
    actual_name = main_page.get_accautnt_info()
    current_url = main_page.get_current_url()
    with allure.step("Проверка, что URL " + current_url + "заканчивается на personal/"):
        assert "/personal" in current_url
    with allure.step("Проверка данных пользователя"):
        assert actual_name == "Budnik Viktornik"
    main_page.close()
    