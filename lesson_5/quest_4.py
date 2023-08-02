from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.firefox import GeckoDriverManager

# Используем драйвер Chrome
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Открыть сайт
chrome_driver.get('http://uitestingplayground.com/dynamicid')

#Кликнуть на синюю кнопку без ID
button_locator = 'button.btn.btn-primary'
for _ in range(3):
    button_click = chrome_driver.find_element(By.CSS_SELECTOR, button_locator)
    button_click.click()


# Используем драйвер Gecko (Firefox)
gecko_driver = webdriver.Firefox(service=GeckoService(executable_path=GeckoDriverManager().install()))

#Открыть сайт
gecko_driver.get('http://uitestingplayground.com/dynamicid')

#Кликнуть на синюю кнопку без ID
button_locator = 'button.btn.btn-primary'
for _ in range(3):
    button_click = gecko_driver.find_element(By.CSS_SELECTOR, button_locator)
    button_click.click()

gecko_driver.quit()
