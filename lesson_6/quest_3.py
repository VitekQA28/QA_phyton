#from time import sleep
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.firefox import GeckoDriverManager


# Дождаться появления картинок

driver = webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()))
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

# Дождаться появления картинок
waiter = WebDriverWait(driver, 40)
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), "Done!" )) 

# Получение значения атрибута src у третьей картинки (индекс 2, так как индексация начинается с 0)
images = driver.find_elements(By.TAG_NAME, "img")
src = images[2].get_attribute("src")
print(src)

driver.quit()


