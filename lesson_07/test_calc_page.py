import pytest
from selenium import webdriver
from lesson_07.CalcPage import CalcPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calc(driver):
    calcPage = CalcPage(driver)
    calcPage.open()
    calcPage.delay_send_key()
    calcPage.find_summ()
    calcPage.screen_has_number()
    calcPage.screen_has_15()
    results = calcPage.screen_has_15()

    assert results == 15
