import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxServise
from webdriver_manager.chrome import ChromeDriverManager
from api.BoardApi import BoardApi
from configuration.ConfigProvider import ConfigProvider
from webdriver_manager.firefox import GeckoDriverManager
from testdata.DataProvider import DataProvider


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
def test_data():
    return DataProvider()

@pytest.fixture()
def api_client()->BoardApi:
    DataProvider().get_token()
    return BoardApi(ConfigProvider().get("api", "base_url"), DataProvider().get_token())


@pytest.fixture()
def api_client_no_auth()->BoardApi:
    return BoardApi(ConfigProvider().get("api", "base_url"), "")

@pytest.fixture()
def board_id()->str:
    api = BoardApi(ConfigProvider().get("api", "base_url"), DataProvider().get_token())
    with allure.step("Предварительно создать доску"):
        resp = api.create_board("Test board to be deleted").get("id")
    return resp
    
@pytest.fixture()
def delete_board()->str:
    dictionary = {"board_id":""}
    yield dictionary
    with allure.step("Удалить доску"):
        api = BoardApi(ConfigProvider().get("api", "base_url"), DataProvider().get_token())
        api.delete_board_id(dictionary.get("board_id"))
