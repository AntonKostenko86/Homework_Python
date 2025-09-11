from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.CalculatorPage import CalculatorPage


def test_calculator():

    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
        )
    calculator_page = CalculatorPage(browser)
    calculator_page.delay('45')
    calculator_page.button()
    calculator_page.result()

    WebDriverWait(browser, 46).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), '15')
        )

    result = calculator_page.result()
    assert result == "15"
    browser.quit()
