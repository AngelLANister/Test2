import allure
import pytest
from selenium import webdriver
from AuthorizationPage import AuthorizationPage
from MainPage import MainPage
from CartPage import CartPage
from OrderPage import OrderPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@allure.title("Проверка итоговой суммы заказа")
@allure.description("Ожидаемая сумма заказа $58.29")
@allure.feature("SUMMARY")
@allure.severity("blocker")
def test_summ_of_purchase(driver):
    with allure.step("Проверка суммы заказа"):
        authorizationPage = AuthorizationPage(driver)
        authorizationPage.open()
        authorizationPage.login_standart_user()

        mainPage = MainPage(driver)
        mainPage.open()
        mainPage.add_lots()

        cartPage = CartPage(driver)
        cartPage.open()
        cartPage.order_check()

        orderPage = OrderPage(driver)
        orderPage.open()
        result = orderPage.order_check()

        expected_price = "$58.29"
        assert result == expected_price
