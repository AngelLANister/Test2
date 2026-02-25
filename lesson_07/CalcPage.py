from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
            )

    def delay_send_key(self):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    def find_summ(self):
        summ = self.driver.find_element(By.CLASS_NAME, "keys")
        summ.find_element(By.XPATH, "//span[text()='7']").click()
        summ.find_element(By.XPATH, "//span[text()='+']").click()
        summ.find_element(By.XPATH, "//span[text()='8']").click()
        summ.find_element(By.XPATH, "//span[text()='=']").click()

    def screen_has_number(self):
        text = self.driver.find_element(By.CLASS_NAME, "screen").text.strip()
        return text.isdigit()

    def screen_has_15(self):
        self.wait.until(
        EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "screen"), "15")
        )
        summ_result = self.driver.find_element(By.CLASS_NAME, "screen").text
        return int(summ_result)
