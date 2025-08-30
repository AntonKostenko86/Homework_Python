from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")

username_input = driver.find_element(By.CSS_SELECTOR, "#username")
username_input.send_keys("tomsmith")

sleep(3)

password_input = driver.find_element(By.CSS_SELECTOR, "#password")
password_input.send_keys("SuperSecretPassword!")

sleep(3)

press_btn = driver.find_element(By.CSS_SELECTOR, "button")
press_btn.click()

sleep(3)

message = driver.find_element(By.CSS_SELECTOR, "#flash").text

print(message)

driver.quit()
