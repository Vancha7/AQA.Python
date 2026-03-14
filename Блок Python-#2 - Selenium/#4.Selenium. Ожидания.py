#Неявные ожидания - Implicit Waits
#driver.implicitly_wait(10)                    #Ждем до 10 секунд


#Неявные ожидания
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")
driver.implicitly_wait(5)
VISIBLE_AFTER_5_SECOND_BUTTON = ("xpath", "//button[@id='visibleAfter']")
driver.find_element(*VISIBLE_AFTER_5_SECOND_BUTTON).click()

#Явные ожидания
# Для начала работы необходимо импортировать 2 модуля:
#
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

#WebDriverWait - нужен для того, чтобы мы могли указать общее время ожидания для всех условий в будущем.
#expected_conditions - в дальнейшем EC, так и переводиться “ожидаемые условия”,
#то есть данный модуль поможет нам выбрать необходимое условие выполнения, которого мы будем ожидать.

#Пример кода, где создается объект wait:
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#driver = webdriver.Chrome(options=options)
#wait = WebDriverWait(driver, 30, poll_frequency=1)
#driver - будет ждать условий далее
#30 (любое число) - это количество секунд
#poll_frequency=1 - определяет то, как часто делать новый запрос на проверку выполнения ожидаемого условия.
#В данном случае 1 секунда.


#Задача - 1.
#Ожидаемое условие: element_to_be_clickable
#Функционал: Кнопка ADD_ELEMENT_BUTTON становится кликабельной только через 5 секунд
#Задача: Дождаться того, чтобы кнопка стала кликабельной
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 30, poll_frequency=1)
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

ADD_ELEMENT_BUTTON = ("xpath", "//button[@id='sbm']")

wait.until(EC.element_to_be_clickable(ADD_ELEMENT_BUTTON))         # Ждем пока кнопка станет кликабельной
driver.find_element(*ADD_ELEMENT_BUTTON).click()

#Задача - 2.
#Ожидаемое условие: visibility_of_element_located
#Функционал: После нажатия на кнопку ADD_ELEMENT появляется элемент DELETE_BUTTON
#Задача: После клика, дождаться появления элемента DELETE_BUTTON
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 30, poll_frequency=1)

driver.get("https://demoqa.com/dynamic-properties")

ADD_ELEMENT = ("xpath", "//button[@onclick='addElement()'")
DELETE_BUTTON = ("xpath", "//button[@onclick='deleteElement()']")

wait.until(EC.element_to_be_clickable(ADD_ELEMENT))               # Ждем пока кнопка станет кликабельной
driver.find_element(*ADD_ELEMENT).click()                         # Кликаем на кнопку

wait.until(EC.visibility_of_element_located(DELETE_BUTTON))       # Ждем пока элемент станет видимым