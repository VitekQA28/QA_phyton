from page.AuthPage import AuthPage
from page.MainPage import MainPage
import time
import allure
import pytest
from page.TrelloPage import TrelloPage



@pytest.mark.skip
@pytest.mark.ui_test
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


@pytest.mark.ui_test
@pytest.mark.parametrize("board_name", ["Test Board 1"])
def test_create_board(browser, board_name, test_data: dict):
    base_url = test_data.get("base_url") 
    token = test_data.get("token") 
    trello_page = TrelloPage(browser, base_url, token)

    with allure.step("Перейти на страницу авторизации и создать доску"):
        trello_page.go_and_create_board(board_name)

    with allure.step("Проверить, что доска успешно создана"):
        assert trello_page.is_board_created(board_name)

    with allure.step("Добавляем новую карточку"):
        trello_page.add_new_card()
    with allure.step("Меняем название карточки"):    
        trello_page.update_name()
    with allure.step("Перемещаем карточку"):  
        trello_page.move_card_to_list()



    time.sleep(100)