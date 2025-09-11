import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    return driver


def test_form(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    driver.find_element(
        By.CSS_SELECTOR, "[name='first-name']"
        ).send_keys("Иван")
    driver.find_element(
        By.CSS_SELECTOR, "[name='last-name']"
        ).send_keys("Петров")
    driver.find_element(
        By.CSS_SELECTOR, "[name='address']"
        ).send_keys("Ленина, 55-3")
    driver.find_element(
        By.CSS_SELECTOR, "[name='e-mail']"
        ).send_keys("test@skypro.com")
    driver.find_element(
        By.CSS_SELECTOR, "[name='phone']"
        ).send_keys("+7985899998787")
    driver.find_element(
        By.CSS_SELECTOR, "[name='zip-code']"
        ).send_keys("")
    driver.find_element(
        By.CSS_SELECTOR, "[name='city']"
        ).send_keys("Москва")
    driver.find_element(
        By.CSS_SELECTOR, "[name='country']"
        ).send_keys("Россия")
    driver.find_element(
        By.CSS_SELECTOR, "[name='job-position']"
        ).send_keys("QA")
    driver.find_element(
        By.CSS_SELECTOR, "[name='company']"
        ).send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button").click()

    zipcode = driver.find_element(
        By.CSS_SELECTOR, "#zip-code"
        ).get_attribute("class")
    assert zipcode == "alert py-2 alert-danger"

    fields = ["#first-name", "#last-name", "#address", "#e-mail", "#phone",
              "#city", "#country", "#job-position", "#company"]

    for field in fields:
        green = driver.find_element(
            By.CSS_SELECTOR, field
            ).get_attribute("class")
        assert green == "alert py-2 alert-success"

    driver.quit()
