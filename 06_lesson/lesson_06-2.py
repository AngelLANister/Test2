from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

driver.find_element(By.CSS_SELECTOR, "#newButtonName").click()

send_key = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
send_key.send_keys("Skypro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
waiter = WebDriverWait(driver, 40)

waiter.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "#updatingButton")))

print(driver.find_element(
    By.CSS_SELECTOR, "#updatingButton").text)

driver.quit()
