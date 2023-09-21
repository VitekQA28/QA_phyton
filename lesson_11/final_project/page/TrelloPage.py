from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider
from selenium.common.exceptions import NoSuchElementException
import allure

class TrelloPage:

    def __init__ (self, driver: WebDriver) ->None:

        url = ConfigProvider().get("ui", "base_url")
        self.__url = url+"/login?returnUrl=%2Fu%2Fviktorbudnik%2Fboards"
        self.__driver = driver

    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    @allure.step("Перейти на страницу авторизации и создать доску")
    def go_and_create_board(self, email: str, password: str, board_name: str):
        self.__driver.get(self.__url)
        self.__driver.find_element(By.CSS_SELECTOR, "#user").send_keys(email)
        self.__driver.find_element(By.CSS_SELECTOR, "#login").click()
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "svg[role=presentation]")))
        self.__driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()
        
        self.open_create_form()
        self.choose_option()
        self.fill_name(board_name)
        self.click_save_button()


    @allure.step("Нажать кнопку Создать в шапке")
    def open_create_form(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=header-create-menu-button]").click()
        
    @allure.step("Выбрать {number} элемент")
    def choose_option(self, number=1):
        popover = self.__driver.find_element(By.CSS_SELECTOR, "section[data-testid=header-create-menu-popover]")
        lis = popover.find_elements(By.CSS_SELECTOR, "li")
        lis[number-1].click()

    @allure.step("Указать имя новой доски = {board_name}")
    def fill_name(self, board_name:str):
        self.__driver.find_element(By.CSS_SELECTOR, "input[data-testid=create-board-title-input]").send_keys(board_name)

    @allure.step("Нажать кнопку Создать")
    def click_save_button(self):
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/section/div/form/button")))
        self.__driver.find_element(By.XPATH, "/html/body/div[3]/div/section/div/form/button").click()

    @allure.step("Проверка, что доска создалась c названием {board_name}")
    def is_board_created(self, board_name: str) -> bool:
        try:
            # Дожидаемся, пока страница полностью обновится
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".board-tile-details-name")))
            board_tiles = self.__driver.find_elements(By.CSS_SELECTOR, ".board-tile-details-name")
            for tile in board_tiles:
                if tile.text == board_name:
                    return True
            return False
        except NoSuchElementException:
            return False
