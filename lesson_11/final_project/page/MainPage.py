from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    def __init__ (self, driver: WebDriver) ->None:
        self.__driver = driver

    def get_current_url(self)->str:
        return self.__driver.current_url

    def open_menu(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=header-member-menu-button]").click()

    def get_accautnt_info(self)->list[str]:
        name = self.__driver.find_element(By.XPATH, "/html/body/div[3]/div/section/div/div/div/div[1]/div/div[2]/div[1]").text
        email = self.__driver.find_element(By.XPATH, "/html/body/div[3]/div/section/div/div/div/div[1]/div/div[2]/div[2]").text
        return [name, email]
    
    
