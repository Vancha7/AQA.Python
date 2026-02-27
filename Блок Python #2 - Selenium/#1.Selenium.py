#AQA \0/ - открытие WebDriver с URL.
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
time.sleep(5)
print(driver.title)
