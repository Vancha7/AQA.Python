import selenium

#Создание тестовых методов (тестов)

from selenium import webdriver
import time
class TestLogin: # Название тестового класса

    def test_open_login_page(self): # Название теста
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/login")
        assert driver.current_url == "https://demoqa.com/login", "Открыта некорректная страница"
        time.sleep(5)





                 #Пример теста на отправку формы:

from selenium import webdriver

class TestExample:

    # Locators

    USERNAME_FIELD = ("xpath", "//input[@id='userName']")
    EMAIL_FIELD = ("xpath", "//input[@id='userEmail']")
    CURRENT_ADDRESS_FIELD = ("xpath", "//textarea[@id='currentAddress']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    OUTPUT_BLOCK = ("xpath", "//div[@id='output']")

    # Тестовый метод (Тест)

    def test_valid_data(self):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/text-box")

        username = driver.find_element(*self.USERNAME_FIELD)
        username.send_keys("Alex")
        assert username.get_attribute("value") == "Alex"

        email = driver.find_element(*self.EMAIL_FIELD)
        email.send_keys("aqa@gmail.com")
        assert email.get_attribute("value") == "aqa@gmail.com"

        address = driver.find_element(*self.CURRENT_ADDRESS_FIELD)
        address.send_keys("Lenina 11")
        assert address.get_attribute("value") == "Lenina 11"

        driver.find_element(*self.SUBMIT_BUTTON).click()

        output = driver.find_element(*self.OUTPUT_BLOCK)
        assert output.is_displayed() is True
        assert ("Alex" and "aqa@gmail.com" and "Lenina 11") in output.text
        print("Выполняюсь после теста")