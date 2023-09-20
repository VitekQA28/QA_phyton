from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configuration.ConfigProvider import ConfigProvider
import allure

class MainPage:

    def __init__ (self, driver: WebDriver) ->None:
        self.__driver = driver
        self.url = ConfigProvider().get("ui", "base_url")
        self.__url = self.url+"/u/viktorbudnik/boards"

    @allure.step("Перейти на страницу авторизации")
    def go(self):
        self.__driver.get(self.__url)


    @allure.step("Получить текущий URL")
    def get_current_url(self)->str:
        return self.__driver.current_url

    @allure.step("Открыть боковое меню")
    def open_menu(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=header-member-menu-button]").click()

    @allure.step("Прочитать информацию о пользователе")
    def get_accautnt_info(self)->list[str]:
        name = self.__driver.find_element(By.XPATH, "/html/body/div[3]/div/section/div/div/div/div[1]/div/div[2]/div[1]").text
        email = self.__driver.find_element(By.XPATH, "/html/body/div[3]/div/section/div/div/div/div[1]/div/div[2]/div[2]").text
        return [name, email]
    
    @allure.step("Прочитать информацию о пользователе")
    def add_cookie(self):
        cookie = {
            "name":"token",
            "value":"634e5e18c2571b0467a1e4a1/ATTSxiXkUOtI9qaunq65ufLDIFvBGCuZDhYCFToNQGkwCK9s8RmoDo9st5jl6opBh6YCAC89E034"
        }
        self.__driver.add_cookie(cookie)

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

    @allure.step("Нажать сохранить")
    def click_save_button(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=create-board-sumbit-button]").click()
        WebDriverWait(self.__driver, 10).until(EC.url_contains(self.url+"/b/"))