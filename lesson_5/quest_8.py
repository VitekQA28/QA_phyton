from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера Chrome
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Открытие страницы
chrome_driver.get('http://the-internet.herokuapp.com/login')
#В поле username введите значение tomsmith
username_locator = '#username'
name_input = chrome_driver.find_element(By.CSS_SELECTOR, username_locator)
name_input.send_keys('tomsmith')
#В поле password введите значение SuperSecretPassword!
pas_locator = '#password'
pas_input = chrome_driver.find_element(By.CSS_SELECTOR, pas_locator)
pas_input.send_keys('SuperSecretPassword!')
#Нажмите кнопку Login
login_locator = 'button[type="submit"]'
login_input = chrome_driver.find_element(By.CSS_SELECTOR, login_locator)
login_input.click()


# Инициализация драйвера Gecko
gecko_driver = webdriver.Firefox(service=GeckoService(executable_path=GeckoDriverManager().install()))
# Открытие страницы
gecko_driver.get('http://the-internet.herokuapp.com/login')
#В поле username введите значение tomsmith
username_locator = '#username'
name_input = gecko_driver.find_element(By.CSS_SELECTOR, username_locator)
name_input.send_keys('tomsmith')
#В поле password введите значение SuperSecretPassword!
pas_locator = '#password'
pas_input = gecko_driver.find_element(By.CSS_SELECTOR, pas_locator)
pas_input.send_keys('SuperSecretPassword!')
#Нажмите кнопку Login
login_locator = 'button[type="submit"]'
login_input = gecko_driver.find_element(By.CSS_SELECTOR, login_locator)
login_input.click()

sleep(5)

# Закрытие браузера
chrome_driver.quit()
gecko_driver.quit()