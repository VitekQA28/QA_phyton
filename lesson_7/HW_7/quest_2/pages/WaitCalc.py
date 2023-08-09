from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Waiting:
    def __init__(self, browser):
        self._driver = browser


    def waiting_calc(self):
        WebDriverWait(self._driver, 46).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        result = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result