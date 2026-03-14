from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.devtools.v143.fed_cm import click_dialog_button

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com")                                               #Открываем сайт
time.sleep(1)
ELEMENTS = ("xpath", "//div[@class= 'card-body']")
click_element = driver.find_element(*ELEMENTS)                                 #Переходим в раздел "Elements"
click_element.click()
time.sleep(1)
TEXT_BOX = ("xpath", "//span[@class = 'text']")
click_text = driver.find_element(*TEXT_BOX)                                    #Переходим в раздел "Text Box"
click_text.click()
time.sleep(1)

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

UPPLOAD = ("xpath", "//span[text()= 'Upload and Download']")
elements_upload = driver.find_element(*UPPLOAD)
elements_upload.click()
time.sleep(1)

FILE_CRED = ("xpath", "//input[@id = 'uploadFile']")                                #Объявляем переменную с расположением кнопки загрузки.
elemens_cred = driver.find_element(*FILE_CRED)                                      #Обращаемся к кнопке через переменную.
time.sleep(1)
elemens_cred.send_keys(r"C:\Users\User\PycharmProjects\AQA.Python\upload.gpeg")     #Через команду "send.keys()" загружаем файл на сайт.
time.sleep(2)

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
time.sleep(5)
