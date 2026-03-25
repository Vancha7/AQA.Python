import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1) # Создаем обьект ожиданий
action = ActionChains(driver)   # Создаем обьект action

driver.get("https://demoqa.com/buttons")
DB_BUTTON_LOCATOR = ("xpath", "//button[@id='doubleClickBtn']")
BUTTON = driver.find_element(*DB_BUTTON_LOCATOR)
time.sleep(2)
action.double_click(BUTTON).perform() #Двойной клик по кнопке
time.sleep(2)

driver.get("https://demoqa.com/buttons")
RIGHT_CLICK_BUTTON = ("xpath", "//button[@id='rightClickBtn']")
BUTTON = driver.find_element(*RIGHT_CLICK_BUTTON)
time.sleep(2)
action.context_click(BUTTON).perform() #Клик правой кнопкой мыши
time.sleep(2)

element = driver.find_element(...)
action.click(element).preform() #Одинарный клик левой кнопкой мыши