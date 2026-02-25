from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open(self):
        self.driver.get(
            "https://www.saucedemo.com/inventory.html"
            )

    def add_lots(self):
        (self.driver.find_element
         (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click())
        (self.driver.find_element
         (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click())
        (self.driver.find_element
         (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click())
        self.driver.find_element(
          By.CSS_SELECTOR, ".shopping_cart_link").click()
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#checkout")))
