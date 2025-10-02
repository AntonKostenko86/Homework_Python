from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from ShopPage import ShopPage
import allure


@allure.title("Тестирование интернет-магазина")
@allure.description("Тест проверяет авторизацию, "
                    "нажатие кнопок, "
                    "добавление товаров в корзину, "
                    "переход в корзину, "
                    "заполнение формы данными, "
                    "итоговую стоимость "
                    )
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    """
        Тест проверяет корректность оформления заказа в интернет-магазине
    """
    with allure.step("Инициализация работы браузера"):
        browser = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
            )
    with allure.step("Открытие страницы интернет-магазина"):
        magazine_swag_labs = ShopPage(
            browser, "https://www.saucedemo.com/"
            )
    with allure.step("Авторизация на сайте"):
        magazine_swag_labs.username("standard_user")
        magazine_swag_labs.password("secret_sauce")
        magazine_swag_labs.button("#login-button")
    with allure.step("Добавить в корзину товары"):
        magazine_swag_labs.button("#add-to-cart-sauce-labs-backpack")
        magazine_swag_labs.button("#add-to-cart-sauce-labs-bolt-t-shirt")
        magazine_swag_labs.button("#add-to-cart-sauce-labs-onesie")
    with allure.step("Перейти в корзину"):
        magazine_swag_labs.button("#shopping_cart_container")
    with allure.step("Оформить заказ"):
        magazine_swag_labs.button("#checkout")
    with allure.step("Заполнить форму данными"):
        magazine_swag_labs.post()
        magazine_swag_labs.button("#continue")
    with allure.step("Прочитать со страницы итоговую стоимость"):
        summ = magazine_swag_labs.price()
    with allure.step("Проверить итоговую стоимость"):
        assert summ == "Total: $58.29"
    with allure.step("Завершение работы браузера"):
        browser.quit()
