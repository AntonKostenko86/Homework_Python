from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
import allure


class ShopPage:

    @allure.step("Открытие страницы интернет-магазина")
    def __init__(self, browser: WebDriver, url: str) -> None:
        """
            Конструктор класса ShopPage.
            WebDriver — объект драйвера Selenium.
            Открывает страницу интернет-магазина.
        """
        self._driver = browser
        self._driver.get(url)

    @allure.step("Ввод имени пользователя для авторизации")
    def username(self, username: str) -> None:
        """
            Вводит данные с именем пользователя в поле {Username}.
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "#user-name"
            ).send_keys(username)

    @allure.step("Ввод пароля для авторизации")
    def password(self, password: str) -> None:
        """
            Вводит данные с паролем в поле {Password}.
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "#password"
            ).send_keys(password)

    @allure.step("Нажатие на кнопку")
    def button(self, locator) -> None:
        """
            Нажимает на кнопку.
        """
        self._driver.find_element(
            By.CSS_SELECTOR, locator
            ).click()

    @allure.step("Заполнение формы данными")
    def post(self) -> None:
        """
            Вводит данные с именем пользователя в поле {First Name}.
            Вводит данные с фамилией пользователя в поле {Last Name}.
            Вводит данные с почтовым индексом пользователя
            в поле {Zip/Postal Code}.
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "#first-name"
            ).send_keys("Антон")
        self._driver.find_element(
            By.CSS_SELECTOR, "#last-name"
            ).send_keys("Костенко")
        self._driver.find_element(
            By.CSS_SELECTOR, "#postal-code"
            ).send_keys("248000")

    @allure.step("Проверка итоговой стоимости")
    def price(self) -> str:
        """
            Прочитать со страницы итоговую стоимость {Total:}.
        """
        txt = self._driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label"
            ).text
        return txt
