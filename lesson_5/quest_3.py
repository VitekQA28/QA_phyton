from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.firefox import GeckoDriverManager

chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
gecko_driver = webdriver.Firefox(service=GeckoService(executable_path=GeckoDriverManager().install()))

#Открыть сайт
chrome_driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

# 5 раз кликнуть на кнопку "Добавить эллемент"
button_locator = 'button[onclick="addElement()"]'
for _ in range(5):
    button_click = chrome_driver.find_element(By.CSS_SELECTOR, button_locator)
    button_click.click()

# Вывести кол-во добавленных элементов
delete_locator = "button.added-manually"
delete = chrome_driver.find_elements(By.CSS_SELECTOR, delete_locator)
print("Chrome Количество кнопок Delete = " + str(len(delete)))

#Открыть сайт
gecko_driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

# 5 раз кликнуть на кнопку "Добавить эллемент"
button_locator = 'button[onclick="addElement()"]'
for _ in range(5):
    button_click = gecko_driver.find_element(By.CSS_SELECTOR, button_locator)
    button_click.click()

# Вывести кол-во добавленных элементов
delete_locator = "button.added-manually"
delete = gecko_driver.find_elements(By.CSS_SELECTOR, delete_locator)
print("Firefox Количество кнопок Delete = " + str(len(delete)))
gecko_driver.quit()
