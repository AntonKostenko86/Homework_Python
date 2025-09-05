from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium"
            "-webdriver-java/slow-calculator.html"
            )

    def delay(self, time: str):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(time)

    def button(self):
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()

    def result(self):
        end_result = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        return end_result


def test_check_calculator_result():
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
        )
    calculator = Calculator(browser)
    calculator.delay("45")
    calculator.button()

    WebDriverWait(browser, 46).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), '15')
    )

    result = calculator.result()
    assert result == "15"
    browser.quit()
