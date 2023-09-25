from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



class Registration:

    @allure.title("Открытие браузера")
    def __init__(self, browser):
        """
        Эта функция открывает браузер

        затем переходит на страницу по URL

        и открывает окно браузера на весь экран

        """
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.__driver = browser
        self.__driver.get('https://prostayaeda.s2.citruspro.ru/')
        self.__driver.implicitly_wait(10)
        self.__driver.maximize_window()

    @allure.step("Нажать на кнопку личного кабинета")
    def open_registration_window(self):
        self.__driver.find_element(By.XPATH, "//*[@id='header']/div[1]/div/div[2]/div[3]/a[2]").click()

    @allure.step("Регистрируем пользователя с валидными данными")
    def login_as(self, name ="Test", gender = "Мужской", phone = "9024657539", password = "Test123456")->str:
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div/div")))
        self.__driver.find_element(By.XPATH, "//*[@id='authForm_fv402gn8']/form/div[3]/div/a[2]").click()
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/main/div[2]")))
        self.__driver.find_element(By.XPATH, "//*[@id='NAME']").send_keys(name)
        self.__driver.find_element(By.XPATH, "//*[@id='registrationCKnVzT']/div/form/div[8]/div/div/label[1]").send_keys(phone)
        self.__driver.find_element(By.XPATH, "//*[@id='PERSONAL_GENDER']").send_keys(gender)
        self.__driver.find_element(By.XPATH, "//*[@id='PASSWORD']").send_keys(password)
        self.__driver.find_element(By.XPATH, "<button type='submit' class='b-btnCheck b-form_lk__btn'><i class='icon icon--tick'></i> <span>Зарегистрироваться</span></button>").click()
