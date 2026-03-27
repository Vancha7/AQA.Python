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



#Для наведения на элемент, action использует метод move_to_element(),
#Где в качестве аргумента принимает веб-элемент для наведения.
#
# STEP_1_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
# STEP_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
# STEP_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")
# STEP_1 = driver.find_element(*STEP_1_LOCATOR)
# STEP_2 = driver.find_element(*STEP_2_LOCATOR)
# STEP_3 = driver.find_element(*STEP_3_LOCATOR)
#action.move_to_element(STEP_1).move_to_element(STEP_2).move_to_element(STEP_3).perform()
#
# Если нужна пауза между цепочками, то можем написать так:
# action.move_to_element(STEP_1).pause(3).move_to_element(STEP_2).pause(3).move_to_element(STEP_3).pause(3).perform()

# Перетаскивание элементов (drag and drop)
# Нам нужно указать элемент, который мы будем перетаскивать и область в которую будем его перетаскивать.
# Как правило:
# source - это то, что мы перетягиваем.
# target - это то, куда мы перетягиваем.
#
#driver.get("https://demoqa.com/droppable")
# SOURCE_LOCATOR = ("xpath", "//div[@id='draggable']")
# TARGET_LOCATOR = ("xpath", "//div[@id='droppable']")
# SOURCE = driver.find_element(*SOURCE_LOCATOR)
# TARGET = driver.find_element(*TARGET_LOCATOR)
# action.drag_and_drop(SOURCE, TARGET).perform()  # Перетаскивание
...