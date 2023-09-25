from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



class AuthPagePr:

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
    def open_auth_window(self):
        self.__driver.find_element(By.XPATH, "//*[@id='header']/div[1]/div/div[2]/div[3]/a[2]").click()

    @allure.step("Авторизоваться под {phone}:{password}")
    def login_as(self, phone = "9024657539", password = "Vitek727217")->str:
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div/div")))
        self.__driver.find_element(By.CSS_SELECTOR, "#USER_LOGIN").send_keys(phone)
        self.__driver.find_element(By.CSS_SELECTOR, "#USER_PASSWORD").send_keys(password)
        self.__driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/div/form/div[3]/button").send_keys(Keys.ENTER)
        
    @allure.step("Получаем актуальный URL")
    def get_current_url(self):
        return self.__driver.current_url
        

    @allure.step("Получаем данные о пользователе")
    def get_accautnt_info(self) -> str:
        # Открываем страницу личного кабинета
        self.__driver.get("https://prostayaeda.s2.citruspro.ru/personal")
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/main/div[2]")))
        # Находим нужные элементы на странице
        name = self.__driver.find_element(By.XPATH, "//*[@id='citrusFormsIblockElement_b7580068da00bffc99fa526470b7d50e']/div[1]/div[1]/h2").text       
        # Возвращаем значение
        return name
    
    @allure.step("Выходим из аккаунта")
    def exit_accautnt(self):
        self.__driver.find_element(By.XPATH, "/html/body/div[4]/main/div[1]/nav/ul/li[3]/a").click()
    
        
    @allure.step("Закрываем браузер")
    def close(self):
        self.__driver.quit()
        
