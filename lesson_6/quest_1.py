#from time import sleep
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.firefox import GeckoDriverManager

# Проверка, что после нажатия кнопки - текст "Data loaded with AJAX get request" выйдет через 16 секунд.

driver = webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()))
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://uitestingplayground.com/ajax')

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

waiter = WebDriverWait(driver, 16, 0.1)
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#content"), "Data loaded with AJAX get request" )
)
print(driver.find_element(By.CSS_SELECTOR, '.bg-success').text)

driver.quit()