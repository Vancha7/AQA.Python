import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")
MULTISELECT = ("xpath", "//input[@id='react-select-4-input']")
select = driver.find_element(*MULTISELECT)
select.send_keys("Green")
assert select.get_attribute("value") == "Green", "Error in value Green"
select.send_keys(Keys.ENTER)
time.sleep(3)
