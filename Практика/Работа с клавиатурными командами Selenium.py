from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/key_presses")

elements = driver.find_element("xpath", "//input[@id = 'target']")
elements.send_keys("Иван Петрович")
time.sleep(1)
elements.send_keys(Keys.CONTROL + "A")
time.sleep(1)
elements.send_keys(Keys.BACKSPACE)
time.sleep(1)
elements.send_keys("Василий Федорович")

time.sleep(1)

elements.send_keys(Keys.CONTROL + "A")
time.sleep(1)
elements.send_keys(Keys.BACKSPACE)