from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure


class CalculatorPage:

    def __init__(self, browser: WebDriver):
        """
            Конструктор класса CalculatorPage.
            WebDriver — объект драйвера Selenium.
        """
        self._driver = browser

    @allure.step("Открытие страницы калькулятора")
    def open(self) -> None:
        """
            Открывает страницу калькулятора.
            Устанавливает фиксированный тайм-аут
            для неявного ожидания завершения команды.
            Увеличивает текущее окно, используемое веб-драйвером.
        """
        self._driver.get(
            "https://bonigarcia.dev/selenium"
            "-webdriver-java/slow-calculator.html"
        )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Установка задержки в секундах")
    def delay(self, time: str) -> None:
        """
            Очищает поле задержки.
            Устанавливает задержку для выполнения операций на калькуляторе.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(time)

    @allure.step("Нажатие кнопок калькулятора")
    def button(self) -> None:
        """
            Нажимает на несколько кнопок калькулятора по очереди.
        """
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()

    @allure.step("Получение результата с экрана калькулятора")
    def result(self) -> str:
        """
            Возвращает текущий результат с экрана калькулятора.
        """
        end_result = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        return end_result
