import pytest
from selenium import webdriver
from lesson_07.AuthorizationPage import AuthorizationPage
from lesson_07.MainPage import MainPage
from lesson_07.CartPage import CartPage
from lesson_07.OrderPage import OrderPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_summ_of_purchase(driver):
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
