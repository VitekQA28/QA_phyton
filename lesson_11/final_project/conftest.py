import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxServise
from webdriver_manager.chrome import ChromeDriverManager
from api.BoardApi import BoardApi
from configuration.ConfigProvider import ConfigProvider
from webdriver_manager.firefox import GeckoDriverManager
#from selenium.webdriver.chrome.options import Options

@pytest.fixture()

def browser():
    with allure.step("Открыть и настроить браузер"):
        timeout = ConfigProvider().getint("ui", "timeout")
        browser_name = ConfigProvider().get("ui", "browser_name")

        if browser_name == 'chrome':
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        else:    
            browser = webdriver.Firefox(service=FirefoxServise(GeckoDriverManager().install()))

        browser.implicitly_wait(timeout)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()

@pytest.fixture()
def api_client()->BoardApi:
    url = ConfigProvider().get("api", "base_url")
    return BoardApi(url, "634e5e18c2571b0467a1e4a1/ATTSxiXkUOtI9qaunq65ufLDIFvBGCuZDhYCFToNQGkwCK9s8RmoDo9st5jl6opBh6YCAC89E034")


@pytest.fixture()
def api_client_no_auth()->BoardApi:
    return BoardApi(ConfigProvider().get("api", "base_url"), "")

@pytest.fixture()
def board_id()->str:
    api = BoardApi(ConfigProvider().get("api", "base_url"), "634e5e18c2571b0467a1e4a1/ATTSxiXkUOtI9qaunq65ufLDIFvBGCuZDhYCFToNQGkwCK9s8RmoDo9st5jl6opBh6YCAC89E034")
    resp = api.create_board("Test board to be deleted").get("id")
    return resp
    
@pytest.fixture()
def delete_board()->str:
    dictionary = {"board_id":""}
    yield dictionary

    api = BoardApi(ConfigProvider().get("api", "base_url"), "634e5e18c2571b0467a1e4a1/ATTSxiXkUOtI9qaunq65ufLDIFvBGCuZDhYCFToNQGkwCK9s8RmoDo9st5jl6opBh6YCAC89E034")
    api.delete_board_id(dictionary.get("board_id"))