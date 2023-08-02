from time import sleep
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait 



# Используем драйвер Chrome
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Открыть сайт
chrome_driver.get('http://uitestingplayground.com/classattr')

#Кликнуть на синюю кнопку без ID и потом кликнуть нажать Enter. Повторить процедуру 3 раза.
blue_button_locator = 'btn-primary'
for _ in range(3):
    try:
        button_click = chrome_driver.find_element(By.CLASS_NAME, blue_button_locator)
        button_click.click()
        wait = WebDriverWait(chrome_driver, 5)
        button_click.send_keys(Keys.RETURN)
        try:
            alert = chrome_driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass
    except UnexpectedAlertPresentException:
        pass


# Используем драйвер Gecko (Firefox)
gecko_driver = webdriver.Firefox(service=GeckoService(executable_path=GeckoDriverManager().install()))

#Открыть сайт
gecko_driver.get('http://uitestingplayground.com/classattr')

#Кликнуть на синюю кнопку без ID
blue_button_locator = 'btn-primary'
for _ in range(3):
    try:
        button_click = gecko_driver.find_element(By.CLASS_NAME, blue_button_locator)
        button_click.click()
        wait = WebDriverWait(gecko_driver, 5)
        button_click.send_keys(Keys.RETURN)
        try:
            alert = gecko_driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass
    except UnexpectedAlertPresentException:
        pass
gecko_driver.quit()