from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class AuthorizationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open(self):
        self.driver.get(
            "https://www.saucedemo.com/"
            )

    def login_standart_user(self):
        (self.driver.find_element
         (By.CSS_SELECTOR, "#user-name").send_keys("standard_user"))
        element = self.driver.find_element(By.CLASS_NAME, "login_password")
        txt = element.text
        lines = txt.split("\n")
        print(element)
        if len(lines) > 0:
            password_lines = lines[1].strip()
            password = password_lines.replace('"', '').strip()
        else:
            print("Не удалось ввести пароль")
        (self.driver.find_element(By.CSS_SELECTOR, "#password").
         send_keys(password))
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".title")))
