from api.BoardApi import BoardApi
import allure
import pytest

@pytest.mark.api
def test_create_board(api_client: BoardApi, delete_board: dict, test_data: dict):
    org_id = test_data.get("org_id")
    board_list_before = api_client.get_all_boards_by_org_id(org_id)
    resp = api_client.create_board("Test board VB")
    delete_board["board_id"] = resp.get("id")
    board_list_after = api_client.get_all_boards_by_org_id(org_id)
    with allure.step("Проверить, колличество досок стало на больше на 1"):
        assert len(board_list_after) - len(board_list_before) == 1 

@pytest.mark.api
def test_delete_board(api_client: BoardApi, board_id: str, test_data: dict ):
    """
    Эта функция удаляет доску
    """
    org_id = test_data.get("org_id")
    board_list_before = api_client.get_all_boards_by_org_id(org_id)
    api_client.delete_board_id(board_id)
    board_list_after = api_client.get_all_boards_by_org_id(org_id)
    with allure.step("Проверить, колличество досок стало меньше на 1"):
        assert len(board_list_before) - len(board_list_after) == 1