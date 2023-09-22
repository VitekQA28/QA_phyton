from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import allure


class TrelloPage:

    def __init__ (self, driver: WebDriver, base_url: str, token: str) ->None:
        self.__driver = driver
        self.__url = base_url+"/login?returnUrl=%2Fu%2Fviktorbudnik%2Fboards"
        self.token = token


    @allure.step("Перейти на страницу авторизации и создать доску")
    def go_and_create_board(self, board_name: str):
        self.__driver.get(self.__url)
        cookie = {
            "name" : "token",
            "value" : self.token
            }
        WebDriverWait(self.__driver, 10)
        self.__driver.add_cookie(cookie)
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
        WebDriverWait(self.__driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/section/div/form/button")))
        self.__driver.find_element(By.XPATH, "/html/body/div[3]/div/section/div/form/button").click()
    
    @allure.step("Проверка, что доска создалась c названием {board_name}")
    def is_board_created(self, board_name: str) -> bool:
        try:
            # Дожидаемся, пока страница полностью обновится
            WebDriverWait(self.__driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div/div[1]/div[1]/div/div/span[1]/div[1]/h1")))
            board_tiles = self.__driver.find_elements(By.XPATH, "//*[@id='content']/div/div[1]/div[1]/div/div/span[1]/div[1]/h1")
            for tile in board_tiles:
                if tile.text == board_name:
                    return True
            return False
        except NoSuchElementException:
            return False
        
    @allure.step("Создать новую карточку в первом листе")    
    def add_new_card(self):
        with allure.step("В поле вводим название карточки Test_card 1"):
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='board']/div[1]/div/div[2]/div/div[1]/div/textarea")))
            self.__driver.find_element(By.XPATH, "//*[@id='board']/div[1]/div/div[2]/div/div[1]/div/textarea").send_keys("Test_card 1")
        
        with allure.step("Нажимаем на кнопку добавить карточку"):
            WebDriverWait(self.__driver, 10)
            self.__driver.find_element(By.XPATH, "//*[@id='board']/div[1]/div/div[2]/div/div[2]/div/input").click()

    @allure.step("Именяем название карточки")      
    def update_name(self):
        with allure.step("Нажимаем на редактироваие карточки"):
            card_title = self.__driver.find_element(By.XPATH, "//*[@id='board']/div[1]/div/div[2]/a/div[3]")
            card_title.click()
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='chrome-container']/div[3]/div/div/div/div[3]/div[1]/textarea")))
        with allure.step("Нажимаем на название карточки"):
            card_title_field = self.__driver.find_element(By.XPATH, "//*[@id='chrome-container']/div[3]/div/div/div/div[3]/div[1]/textarea")
            card_title_field.click()
        time.sleep(2)
        with allure.step("Очищаем содержимое поля"):
            card_title_field.clear()
        time.sleep(2)
        with allure.step("Вводим новое название New Card Title"):
            card_title_field.send_keys("New Card Title")
            with allure.step("Нажимаем Enter"):
                card_title_field.send_keys(Keys.RETURN)
        with allure.step("Закрываем окно редактирования"):
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='chrome-container']/div[3]/div/div/a")))
            self.__driver.find_element(By.XPATH, "//*[@id='chrome-container']/div[3]/div/div/a").click()
    

    @allure.step("Перечещаем карточку на другой лист")
    def move_card_to_list(self):
        WebDriverWait(self.__driver, 10)
        with allure.step("Находим первый список"):
            self.__driver.find_element(By.XPATH, "//*[@id='board']/div[1]")
        with allure.step("Находим карточку в первом списке"):
            card = self.__driver.find_element(By.XPATH, "//*[@id='board']/div[1]/div/div[2]/a/div[3]")
        with allure.step("Находим второй список"):
            target_list = self.__driver.find_element(By.XPATH, "//*[@id='board']/div[2]")
        with allure.step(" Перемещаем карточку из первого списка во второй список"):
            actions = ActionChains(self.__driver)
            actions.drag_and_drop(card, target_list)
            actions.perform()

    @allure.step("Удаляем карточку")
    def delete_card(self):
        WebDriverWait(self.__driver, 10)
        with allure.step("Нажимаем на карточку"):
            card_title = self.__driver.find_element(By.XPATH, "//*[@id='board']/div[2]/div/div[2]/a/div[3]")
            card_title.click()
        with allure.step("В открывшемся меню нажимем на Архивировать"):
            self.__driver.find_element(By.XPATH, "//*[@id='chrome-container']/div[3]/div/div/div/div[5]/div[5]/div[1]/a[4]").click()
            WebDriverWait(self.__driver, 10)
            with allure.step("В открывшемся меню нажимем на Удалить"):
                self.__driver.find_element(By.XPATH, "//*[@id='chrome-container']/div[3]/div/div/div/div[5]/div[5]/div[1]/a[6]").click()
        WebDriverWait(self.__driver, 10)
        with allure.step("Закрываем окно редактирования карточки"):
            self.__driver.find_element(By.XPATH, "//*[@id='chrome-container']/div[3]/div/div/a").click()
            time.sleep(2)

    @allure.step("Удаляем доску")
    def delete_board(self):
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, "//*[@id='content']/div/div[1]/div[1]/div/div/span[2]/button[2]/span/span")))
        with allure.step("Нажимаем на кнопку Меню в шапке сайта"):
            self.__driver.find_element(By.XPATH, "//*[@id='content']/div/div[1]/div[1]/div/div/span[2]/button[2]/span/span").click()
        with allure.step("Нажимаем кнопку закрыть доску"):   
            self.__driver.find_element(By.XPATH, "//*[@id='content']/div/div[2]/div/div/div[2]/div/ul/li[16]/a").click()
        with allure.step("Нажимаем кнопку закрыть доску"):   
            self.__driver.find_element(By.XPATH, "//*[@id='chrome-container']/div[4]/div/div[2]/div/div/div/input").click()
            WebDriverWait(self.__driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, "//*[@id='content']/div/div/div/div/div/div[2]/button")))
            with allure.step("Нажимаем кнопку Закрыть"):
                self.__driver.find_element(By.XPATH, "//*[@id='content']/div/div/div/div/div/div[2]/button").click()
        with allure.step("Возвращаемся к списку досок"):
            self.__driver.get("https://trello.com/u/viktorbudnik/boards")

    @allure.step("Проверяем, что список досок пустой")
    def check_empty_board_list(self):
    # Находим все элементы, представляющие доски
        board_elements = self.__driver.find_elements(By.XPATH, "//div[@class='board-tile']")
    
    # Проверяем, что количество элементов равно 0
        assert len(board_elements) == 0, "Список досок не пустой"