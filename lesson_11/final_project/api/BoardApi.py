import requests
import allure

class BoardApi:

    @allure.step("URL: {base_url}, token авторизации {token}")
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    @allure.step("Запросить список всех досок для организации {org_id}")
    def get_all_boards_by_org_id(self, org_id: str)->list:
        path = "{trello}/organizations/{id}?boards=open&board_fields=all&fields=boards".format(trello = self.base_url, id = org_id )
        cookie = {"token" : self.token}
        resp = requests.get(path, cookies = cookie)
        return resp.json().get("boards")
    
    @allure.step("Создать доску {name}")
    def create_board(self, name: str , default_lists = True)->dict:
        body = {
            'defaultLists': default_lists,
            'name': name,
            'token': self.token
            }
        cookie = {"token" : self.token}        
        path = "{trello}/boards/".format(trello = self.base_url)
        resp = requests.post(path, json=body, cookies=cookie)
        return resp.json()
    
    @allure.step("Получить список колонок на доске {board_id}")
    def get_board_lists(self, board_id: str) -> dict:
        cookie = {"token": self.token}
        path = f"{self.base_url}/boards/{board_id}/lists"
        resp = requests.get(path, cookies=cookie)
        return resp.json()

    
    @allure.step("Добавить карточку в первую колонку на доске {board_id}")
    def add_card_to_first_list(self, board_id: str, card_name: str) -> dict:
        lists = self.get_board_lists(board_id)
        if len(lists) > 0:
            first_list_id = lists[0]['id']
            body = {
                'idList': first_list_id,
                'name': card_name,
                'token': self.token
            }
            cookie = {"token": self.token}
            path = f"{self.base_url}/cards"
            resp = requests.post(path, json=body, cookies=cookie)
            return resp.json()
        else:
            raise Exception("No lists found on the board")


    @allure.step("Удалить доску {id}")
    def delete_board_id(self, id: str):
        cookie = {"token" : self.token}        
        path = "{trello}/boards/{board_id}".format(trello = self.base_url, board_id = id)
        resp = requests.delete(path, json=cookie, cookies=cookie)
        return resp.json()