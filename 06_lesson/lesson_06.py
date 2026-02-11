from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

waiter= WebDriverWait(driver, 40)

waiter.until(ЕC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success")))

# print()

driver.quit()