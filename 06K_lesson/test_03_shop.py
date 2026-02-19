from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_summary_total_label():

    driver = webdriver.Firefox()

    driver.get("https://www.saucedemo.com/")
    (driver.find_element
     (By.CSS_SELECTOR, "#user-name").send_keys("standard_user"))
    element = driver.find_element(By.CLASS_NAME, "login_password")
    txt = element.text
    lines = txt.split("\n")
    if len(lines) > 0:
        password_lines = lines[1].strip()
        password = password_lines.replace('"', '').strip()
    else:
        print("Не удалось ввести пароль")

    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    WebDriverWait(driver, 45).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".title")))
    (driver.find_element
     (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click())
    (driver.find_element
     (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click())
    (driver.find_element
     (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click())
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    WebDriverWait(driver, 45).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#checkout")))
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    WebDriverWait(driver, 45).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#first-name")))
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Андрей")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Безрук")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(660122)
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    total = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_txt = total.text
    price = total_txt.split(":")[1].strip()
    assert "$58.29" in price, "Ошибка итоговой суммы заказа"
    driver.quit()
