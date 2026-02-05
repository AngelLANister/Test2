from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
search_username_locator = "[name='username']"
search_input = driver.find_element(By.CSS_SELECTOR, search_username_locator)
search_input.send_keys("tomsmith")
search_password_locator = "[name='password']"
search_input = driver.find_element(By.CSS_SELECTOR, search_password_locator)
search_input.send_keys("SuperSecretPassword!")
search_input.send_keys(Keys.RETURN)
wait = WebDriverWait(driver, 10)
login_message = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#flash")))
print(login_message.text)
driver.quit()
