import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture
driver = webdriver.Edge()
def fill_field(driver, selector, value):
    driver.find_element(By.CSS_SELECTOR, selector).send_keys(value)
def test_green_after_submit(driver):
driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
fill_field(driver, "input[name='first-name']", 'Иван')
fill_field(driver, "input[name='last-name']", 'Петров')
fill_field(driver, "input[name='address']", 'Ленина, 55-3')
fill_field(driver, "input[name='zip-code']", '')
fill_field(driver, "input[name='city']", 'Москва')
fill_field(driver, "input[name='country']", 'Россия')
fill_field(driver, "input[name='e-mail']", 'test@skypro.com')
fill_field(driver, "input[name='phone']", '+7985899998787')
fill_field(driver, "input[name='job-position']", 'QA')
fill_field(driver, "input[name='company']", 'SkyPro')
driver.find_element(By.CSS_SELECTOR, [type='submit']).click()
wait = WebDriverWait(driver, 10)

border_color = value_of_css_property("border-color")
assert border_color == "badbcc"
