#AQA \0/ - открытие WebDriver с URL.
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(" https://demoqa.com/text-box")

element_full_name = driver.find_element("xpath", "//input[@id = 'userName']") # В переменную ложим путь до поля.
element_full_name.clear()                                                     # Элемент поля.
element_full_name.send_keys("Иван Васильченко")                               # Ввод данных в поле.
email_field = element_full_name.get_attribute("value")                        # Save данных поля в переменную.
assert "Иван Васильченко" in email_field                                      # Возвращает значение из поля, если оно есть.

time.sleep(3)

elements_email = driver.find_element("xpath", "//input[@type = 'email']")
elements_email.clear()
elements_email.send_keys("Vancha-15@mail.ru")
elements_email_as = elements_email.get_attribute("value")
assert "Vancha-15@mail.ru" in elements_email_as

time.sleep(3)

elements_current = driver.find_element("xpath", "//textarea[@id = 'currentAddress']")
elements_current.clear()
elements_current.send_keys("Краснодар, улица Московская 45/2.")
elements_current_as = elements_current.get_attribute("value")
assert "Краснодар, улица Московская 45/2." in elements_current_as

time.sleep(3)

elements_address = driver.find_element("xpath", "//textarea[@id = 'permanentAddress']")
elements_address.clear()
elements_address.send_keys("Краснодарский Край, Калининский район, Гривенская.")
elements_address_as = elements_address.get_attribute("value")
assert "Краснодарский Край, Калининский район, Гривенская." in elements_address_as

time.sleep(3)
