from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
import time


options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://demoqa.com")                                               #Открываем сайт
time.sleep(1)
ELEMENTS = ("xpath", "//div[@class= 'card-body']")
click_element = driver.find_element(*ELEMENTS)                                 #Переходим в раздел "Elements"
click_element.click()
time.sleep(1)
TEXT_BOX = ("xpath", "//span[@class = 'text']")
click_text = driver.find_element(*TEXT_BOX)                                    #Переходим в подраздел "Text Box"
click_text.click()
time.sleep(1)

#Переходим к разделу заполнения полей.

element_full_name = driver.find_element("xpath", "//input[@id = 'userName']")   # В переменную ложим путь до поля.
element_full_name.clear()                                                       # Элемент поля.
element_full_name.send_keys("Иван Васильченко")                                 # Ввод данных в поле.
email_field = element_full_name.get_attribute("value")                          # Save данных поля в переменную.
assert "Иван Васильченко" in email_field                                        # Возвращает значение из поля, если оно есть.
time.sleep(1)

elements_email = driver.find_element("xpath", "//input[@type = 'email']")
elements_email.clear()
elements_email.send_keys("Vancha-15@mail.ru")
elements_email_as = elements_email.get_attribute("value")
assert "Vancha-15@mail.ru" in elements_email_as
time.sleep(1)

elements_current = driver.find_element("xpath", "//textarea[@id = 'currentAddress']")
elements_current.clear()
elements_current.send_keys("Краснодар, улица Московская 45/2.")
elements_current_as = elements_current.get_attribute("value")
assert "Краснодар, улица Московская 45/2." in elements_current_as
time.sleep(1)

elements_address = driver.find_element("xpath", "//textarea[@id = 'permanentAddress']")
elements_address.clear()
elements_address.send_keys("Краснодарский Край, Калининский район, Гривенская.")
elements_address_as = elements_address.get_attribute("value")
assert "Краснодарский Край, Калининский район, Гривенская." in elements_address_as
time.sleep(1)

#Переход к разделу по загрузке файлов.
UPPLOAD = ("xpath", "//span[text()= 'Upload and Download']")
elements_upload = driver.find_element(*UPPLOAD)
elements_upload.click()
time.sleep(1)

FILE_CRED = ("xpath", "//input[@id = 'uploadFile']")                                #Объявляем переменную с расположением кнопки загрузки.
elemens_cred = driver.find_element(*FILE_CRED)                                      #Обращаемся к кнопке через переменную.
time.sleep(1)
elemens_cred.send_keys(r"C:\Users\User\PycharmProjects\AQA.Python\upload.gpeg")     #Через команду "send.keys()" загружаем файл на сайт.
time.sleep(2)

#Переход к разделу по динамическим элементам.
DINAMIC_P = ("xpath", "//span[text()= 'Dynamic Properties']")
elements_p = driver.find_element(*DINAMIC_P)
elements_p.click()

time.sleep(1)
wait = WebDriverWait(driver, 30, poll_frequency=1)
ADD_ELEMENT_BUTTON = ("xpath", "//button[@id='enableAfter']")
DELETE_BUTTON = ("xpath", "//button[@id='visibleAfter']")
print("Ожидание активации кнопки...")
wait.until(EC.element_to_be_clickable(ADD_ELEMENT_BUTTON))                            # Ждем пока кнопка станет кликабельной
print("✓ Кнопка стала кликабельной")
driver.find_element(*ADD_ELEMENT_BUTTON).click()
print("✓ Клик по кнопке выполнен")
print("Ожидание появления второй кнопки...")
wait.until(EC.visibility_of_element_located(DELETE_BUTTON))                           # Ждем пока элемент станет видимым
print("✓ Вторая кнопка стала видимой")
time.sleep(2)

#Аллерт.
ALLERTS_DIV = ("xpath", "//div[contains(@class, 'header-text') and contains(text(), 'Alerts')]")
driver.find_element(*ALLERTS_DIV).click()
time.sleep(1)
print("Открыт выпадающий список Аллерт...")

#Аллерт: Да.
ALLERST_1 = ("xpath", "//span[text() = 'Alerts']")
driver.find_element(*ALLERST_1).click()
time.sleep(1)
print("Открыт раздел Allerts...")
driver.find_element("xpath", "//button[@id='alertButton']").click()
time.sleep(1)
print("Нажата кнопка Allerts...")
alert = driver.switch_to.alert
time.sleep(1)
alert.accept()
print("Allerts принят.")

#Аллерт с тайматом после нажатия кнопки 5 сек.
ALLERST_2 = ("xpath", "//button[@id = 'timerAlertButton']")
driver.find_element(*ALLERST_2).click()
time.sleep(1)
alert = wait.until(EC.alert_is_present())            #Ожидание появления аллерта.
time.sleep(1)
alert.accept()

#Аллерт: Да - Отмена.
ALLERST_3 = ("xpath", "//button[@id = 'confirmButton']")
driver.find_element(*ALLERST_3).click()
time.sleep(1)
alert.dismiss()                                      #Отклоняем аллерт.
time.sleep(1)

#Аллерт с вводом текста.
ALLERST_4 = ("xpath", "//button[@id = 'promtButton']")
driver.find_element(*ALLERST_4).click()
time.sleep(1)
alert.send_keys("Iva.AQA")
time.sleep(1)
alert.accept()
time.sleep(2)

WIDGETS_DIV = ("xpath", "//div[contains(@class, 'header-text') and contains(text(), 'Widgets')]")            #Переходим в раздел "Elements"
driver.find_element(*WIDGETS_DIV).click()
time.sleep(5)
SELECT_MENU = ("xpath", "//span[text() = 'Select Menu']")                                                    #Переходим в подраздел "Text Box
driver.find_element(*SELECT_MENU).click()
time.sleep(1)


SELECT_VALUE = ("xpath", "//div[@class = 'css-19bb58m']")
DROP1 = ("xpath", "//div[text()= 'Another root option']")
SELECT_ONE = ("xpath", "//div[@class = 'css-hlgwow']")
DROP2 = ("xpath", "//div[text()= 'Mr.']")
OLD_STYLE = ("xpath", "//select[@id= 'oldSelectMenu']")
MULTISELECT = ("xpath", "//input[@id='react-select-4-input']")
STANDARD_SELECT = ("xpath", "//select[@id= 'cars']")

driver.find_element(*SELECT_VALUE).click()                                                                  #Кликаем по выпадающему списку
time.sleep(1)                                                                                               #Кликаем по элементу из выпадающего списка
driver.find_element(*DROP1).click()
time.sleep(2)


DROPDOWN = Select(driver.find_element(*OLD_STYLE))                                                          #Обращаемся к элементам выпадающего списка
DROPDOWN.select_by_visible_text("Black")                                                                    #Выбираем элемент по тексту "Black"
time.sleep(2)


select = driver.find_element(*MULTISELECT)
select.send_keys("Green")
assert select.get_attribute("value") == "Green", "Error in value Green"
select.send_keys(Keys.ENTER)
select.send_keys(Keys.ESCAPE)
time.sleep(2)

select.send_keys("Blue")
assert select.get_attribute("value") == "Blue", "Error in value Blue"
select.send_keys(Keys.ENTER)
time.sleep(1)
select.send_keys(Keys.ESCAPE)
time.sleep(1)
select.send_keys("Blue")
time.sleep(1)
END_ESC = ("xpath", "//div[@class = 'css-v7duua']")
driver.find_element(*END_ESC).click()                                                         #Удаляем элемент по клику на "Х" в выпадающем списке


DROPDOWN2 = Select(driver.find_element(*STANDARD_SELECT))                                     #Обращаемся к элементам выпадающего списка
DROPDOWN2.select_by_index(3)                                                                  #Выбираем элемент по индексу
time.sleep(5)

#Взаимодействие с мышью.
SELECT_MENU = ("xpath", "//span[text() = 'Buttons']")
B_BUTTON_LOCATOR = ("xpath", "//button[@id='doubleClickBtn']")
RIGHT_CLICK_BUTTON = ("xpath", "//button[@id='rightClickBtn']")
ELEMENTS = ("xpath", "(//div[@class='header-text'])[1]")
CLICK_ME = ("xpath", "//button[text() = 'Click Me']")
time.sleep(2)
driver.find_element(*ELEMENTS).click()                                                        #Открываем раздел Elements
time.sleep(1)
driver.find_element(*SELECT_MENU).click()                                                     #Переходим в подраздел.
time.sleep(2)
BUTTON = driver.find_element(*B_BUTTON_LOCATOR)
action.double_click(BUTTON).perform()                                                         #Двойной клик по кнопке
time.sleep(2)
BUTTON = driver.find_element(*RIGHT_CLICK_BUTTON)
time.sleep(2)
action.context_click(BUTTON).perform()                                                        #Клик правой кнопкой мыши
time.sleep(2)
element = driver.find_element(*CLICK_ME)
action.click(element).perform()                                                               #Одинарный клик левой кнопкой мыши
print("Раздел по взаимодействию с мышью успешно пройден ✓." )