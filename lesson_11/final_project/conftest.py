import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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