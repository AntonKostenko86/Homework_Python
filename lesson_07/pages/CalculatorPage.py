from selenium.webdriver.common.by import By


class CalculatorPage:

    def __init__(self, browser):
        self._driver = browser
        self._driver.get(
            "https://bonigarcia.dev/selenium"
            "-webdriver-java/slow-calculator.html"
        )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

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
