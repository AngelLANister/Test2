from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open(self):
        self.driver.get(
            "https://www.saucedemo.com/cart.html"
            )

    def order_check(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#first-name")))
