import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from api.BoardApi import BoardApi
#from selenium.webdriver.chrome.options import Options

@pytest.fixture()

def browser():
    with allure.step("Открыть и настроить браузер"):
    #chrome_options = Options()
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--disable-extensions")
    #chrome_options.add_argument("--disable-gpu") 
    #chrome_options.add_argument("--no-sandbox") 
    #chrome_options.add_argument("--disable-dev-shm-usage")
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.implicitly_wait(4)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()

@pytest.fixture()
def api_client()->BoardApi:
    return BoardApi("https://api.trello.com/1", "634e5e18c2571b0467a1e4a1/ATTSxiXkUOtI9qaunq65ufLDIFvBGCuZDhYCFToNQGkwCK9s8RmoDo9st5jl6opBh6YCAC89E034")


@pytest.fixture()
def api_client_no_auth()->BoardApi:
    return BoardApi("https://api.trello.com/1", "")

@pytest.fixture()
def board_id()->str:
    api = BoardApi("https://api.trello.com/1", "634e5e18c2571b0467a1e4a1/ATTSxiXkUOtI9qaunq65ufLDIFvBGCuZDhYCFToNQGkwCK9s8RmoDo9st5jl6opBh6YCAC89E034")
    resp = api.create_board("Test board to be deleted").get("id")
    return resp
    
@pytest.fixture()
def delete_board()->str:
    dictionary = {"board_id":""}
    yield dictionary

    api = BoardApi("https://api.trello.com/1", "634e5e18c2571b0467a1e4a1/ATTSxiXkUOtI9qaunq65ufLDIFvBGCuZDhYCFToNQGkwCK9s8RmoDo9st5jl6opBh6YCAC89E034")
    api.delete_board_id(dictionary.get("board_id"))