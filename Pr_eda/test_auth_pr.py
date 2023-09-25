from AuthPagePr import AuthPagePr
import allure
import pytest

@allure.severity("critical")
@allure.epic("Авторизация")
def test_auth():
    with allure.step("Отрываем и настраиваем браузер"):
        main_page = AuthPagePr('browser')
    with allure.step("Отрываем страницу авторизации"):
        main_page.open_auth_window()
    with allure.step("Водим валидные данные"):
        main_page.login_as()
    with allure.step("Проводим проверку данных"):
        actual_name = main_page.get_accautnt_info()
        current_url = main_page.get_current_url()
        with allure.step("Проверка, что URL " + current_url + "заканчивается на personal/"):
            assert "/personal" in current_url
        with allure.step("Проверка данных пользователя"):
            assert actual_name == "Budnik Viktornik"
    main_page.close()
    