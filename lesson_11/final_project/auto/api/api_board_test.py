from api.BoardApi import BoardApi
import pytest


def test_create_board(api_client: BoardApi, delete_board: dict):
    board_list_before = api_client.get_all_boards_by_org_id("634e5f7f96fd490099b28bf9")
    resp = api_client.create_board("Test board VB")
    delete_board["board_id"] = resp.get("id")
    board_list_after = api_client.get_all_boards_by_org_id("634e5f7f96fd490099b28bf9")
    assert len(board_list_before) < len(board_list_after)


def test_delete_board(api_client: BoardApi, board_id: str ):
    """
    Эта функция удаляет доску
    """
    board_list_before = api_client.get_all_boards_by_org_id("634e5f7f96fd490099b28bf9")
    api_client.delete_board_id(board_id)
    board_list_after = api_client.get_all_boards_by_org_id("634e5f7f96fd490099b28bf9")
    assert len(board_list_before) - len(board_list_after) == 1