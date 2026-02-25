from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open(self):
        self.driver.get(
            "https://www.saucedemo.com/checkout-step-one.html"
            )

    def order_check(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#first-name").send_keys("Андрей")
        self.driver.find_element(
            By.CSS_SELECTOR, "#last-name").send_keys("Безрук")
        self.driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys(660122)
        self.driver.find_element(
            By.CSS_SELECTOR, "#continue").click()
        total = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_txt = total.text
        price = total_txt.split(":")[1].strip()
        return price
