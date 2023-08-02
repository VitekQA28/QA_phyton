
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
gecko_driver = webdriver.Firefox(service=GeckoService(executable_path=GeckoDriverManager().install()))
# Открытие страницы
chrome_driver.get('http://the-internet.herokuapp.com/inputs')
gecko_driver.get('http://the-internet.herokuapp.com/inputs')
#Ввести в поле текст 1000
num_locator = 'input[type="number"]'
num_input = chrome_driver.find_element(By.CSS_SELECTOR, num_locator)
num_input.send_keys('1000')
sleep(3)
#Очистить поле от значения методом Clear
num_input.clear()
#Ввод значения 999
sleep(3)
num_input = chrome_driver.find_element(By.CSS_SELECTOR, num_locator)
num_input.send_keys('999')

#Ввести в поле текст 1000
num_locator = 'input[type="number"]'
num_input = gecko_driver.find_element(By.CSS_SELECTOR, num_locator)
num_input.send_keys('1000')
sleep(3)
#Очистить поле от значения методом Clear
num_input.clear()
#Ввод значения 999
sleep(3)
num_input = gecko_driver.find_element(By.CSS_SELECTOR, num_locator)
num_input.send_keys('999')

# Закрытие браузера
chrome_driver.quit()
gecko_driver.quit()