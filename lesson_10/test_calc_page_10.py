import allure
import pytest
from selenium import webdriver
from CalcPage import CalcPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Проверка вычисления суммы с задержкой")
@allure.description("Сумма чисел 7 и 8")
@allure.feature("SUMMARY")
@allure.severity("blocker")
def test_calc(driver):
    with allure.step("Вычисления суммы"):
        calcPage = CalcPage(driver)
        calcPage.open()
        calcPage.delay_send_key()
        calcPage.find_summ()
        calcPage.screen_has_15()
        results = calcPage.screen_has_15()

        assert results == 15
