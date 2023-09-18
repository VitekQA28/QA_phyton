import requests

class BoardApi:

    base_url = "https://api.trello.com/1"

    def __init__(self) -> None:
        pass

    def get_all_boards_by_org_id(self, org_id: str):
        
        path = "{trello}/organizations/{id}?boards".format(trello = self.base_url, id = org_id )
        cookie = {"token" : "634e5e18c2571b0467a1e4a1/ATTSxiXkUOtI9qaunq65ufLDIFvBGCuZDhYCFToNQGkwCK9s8RmoDo9st5jl6opBh6YCAC89E034"}
        resp = requests.get(path, cookies = cookie)

        return resp.json()