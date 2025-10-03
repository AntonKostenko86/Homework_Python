from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CalculatorPage import CalculatorPage
import allure


@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректность работы калькулятора")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    """
        Тест проверяет работу калькулятора на сложение.
    """
    with allure.step("Инициализация работы браузера"):
        browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
            )
        calculator_page = CalculatorPage(browser)
    with allure.step("Открытие страницы калькулятора"):
        calculator_page.open()
    with allure.step("Установка задержки для выполнения операции в секундах"):
        calculator_page.delay('45')
    with allure.step("Нажатие кнопок калькулятора по очереди"):
        calculator_page.button()
    with allure.step("Ожидание результата"):
        calculator_page.result()
        WebDriverWait(browser, 46).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), '15'
            )
        )
    with allure.step("Получение результата"):
        result = calculator_page.result()
    with allure.step("Проверка результата"):
        assert result == "15"
    with allure.step("Завершение работы браузера"):
        browser.quit()
