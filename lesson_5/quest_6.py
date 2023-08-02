
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
chrome_driver.get('http://the-internet.herokuapp.com/entry_ad')
gecko_driver.get('http://the-internet.herokuapp.com/entry_ad')
# Ожидание появления модального окна
wait = WebDriverWait(chrome_driver, 4)
close_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='modal']//p[text()='Close']")))
close_button.click() # Нажатие на кнопку Close
wait = WebDriverWait(gecko_driver, 4)
close_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='modal']//p[text()='Close']")))
close_button.click() # Нажатие на кнопку Close

# Закрытие браузера
chrome_driver.quit()
gecko_driver.quit()