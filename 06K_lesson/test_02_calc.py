from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_calc():

    driver = webdriver.Chrome()

    driver.get("https://bonigarcia.dev/"
               "selenium-webdriver-java/slow-calculator.html")
    driver.find_element(By.CSS_SELECTOR, "#delay").clear()
    driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")
    summ = driver.find_element(By.CLASS_NAME, "keys")
    summ.find_element(By.XPATH, "//span[text()='7']").click()
    summ.find_element(By.XPATH, "//span[text()='+']").click()
    summ.find_element(By.XPATH, "//span[text()='8']").click()
    summ.find_element(By.XPATH, "//span[text()='=']").click()

    def screen_has_number(driver):

        text = driver.find_element(By.CLASS_NAME, "screen").text.strip()
        return text.isdigit()
    WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
    summ_result = driver.find_element(By.CLASS_NAME, "screen").text
    assert "15" in summ_result, "Время вычисления истекло"

    driver.quit()
