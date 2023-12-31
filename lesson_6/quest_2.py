#from time import sleep
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.firefox import GeckoDriverManager

'''
**Задание 2. Переименовать кнопку**

Напишите скрипт. 

Шаги:

1. Перейдите на сайт: http://uitestingplayground.com/textinput.
2. Укажите в поле ввода текст SkyPro.
3. Нажмите на синюю кнопку.
4. Получите текст кнопки и выведите в консоль *(“SkyPro”).*
''' 

driver = webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()))
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://uitestingplayground.com/textinput')

driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys('SkyPro')
waiter = WebDriverWait(driver, 4)
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
waiter = WebDriverWait(driver, 4)
txt = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
print(txt)


driver.quit()