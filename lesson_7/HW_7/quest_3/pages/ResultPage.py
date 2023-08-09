from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultPage:
    def __init__(self, browser):
        self._driver = browser

    
    def total_price(self):
        total_price = WebDriverWait(self._driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
    ).text
        return total_price
