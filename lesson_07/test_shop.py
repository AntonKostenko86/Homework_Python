from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.ShopPage import ShopPage


def test_shop():
    browser = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
        )

    magazine_swag_labs = ShopPage(
        browser, "https://www.saucedemo.com/"
        )
    magazine_swag_labs.username("standard_user")
    magazine_swag_labs.password("secret_sauce")
    magazine_swag_labs.button("#login-button")

    magazine_swag_labs = ShopPage(
        browser, 'https://www.saucedemo.com/inventory.html'
        )
    magazine_swag_labs.button("#add-to-cart-sauce-labs-backpack")
    magazine_swag_labs.button("#add-to-cart-sauce-labs-bolt-t-shirt")
    magazine_swag_labs.button("#add-to-cart-sauce-labs-onesie")

    magazine_swag_labs = ShopPage(
        browser, 'https://www.saucedemo.com/cart.html'
        )
    magazine_swag_labs.button("#shopping_cart_container")
    magazine_swag_labs.button("#checkout")

    magazine_swag_labs = ShopPage(
        browser, 'https://www.saucedemo.com/checkout-step-one.html'
        )
    magazine_swag_labs.post()
    magazine_swag_labs.button("#continue")

    magazine_swag_labs = ShopPage(
        browser, "https://www.saucedemo.com/checkout-step-two.html"
        )
    summ = magazine_swag_labs.price()

    assert summ == "Total: $58.29"

    browser.quit()
