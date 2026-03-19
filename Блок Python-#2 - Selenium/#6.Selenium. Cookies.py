#import json                   # Для работы с куками.
# driver.get_cookie("name")     # Вернет куку name или любую другую указанную в качестве аргумента
# driver.get_cookies()          # Вернет список словарей, все куки

#1. Получаем куки и сохраняем их в файл.
import json
from selenium import webdriver
import time

driver = webdriver.Chrome()
LOGIN_FIELD = ("xpath", "//input[@id = 'login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id = 'password']")
SUBMIT_BUTTON = ("xpath", "//button[@title= 'Отправить']")

# Логинимся в аккаунт
driver.get("https://www.freeconferencecall.com/ru/ru/login")
driver.find_element(*LOGIN_FIELD).send_keys("Iva.Vasilchenko@x5.ru")
driver.find_element(*PASSWORD_FIELD).send_keys("Nfyrb2003")
driver.find_element(*SUBMIT_BUTTON).click()
# Получаем cookies
cookies = driver.get_cookies()
# Сохраняем в файл
with open("../Практика/cookies.json", "w") as file:
    json.dump(cookies, file, indent=4)


#№2.Чтение Сookies из файла.
import json
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.freeconferencecall.com/ru/ru/login")       # Важно: перейти на домен перед add_cookie
driver.delete_all_cookies()                            # Чистит все куки на странице, чтобы не было наложения.
# Загружаем cookies из файла
with open("../Практика/cookies.json", "r") as file:
    cookies = json.load(file)
# Добавляем каждую куку по отдельности
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()

#№3.Создание класса CookieManager.
import json
from selenium.webdriver.chrome.webdriver import WebDriver
class CookieManager:
    def __init__(self,driver, file_path="cookies.json"):
        self.driver: WebDriver = driver
        self.file_path = file_path
    def save(self):
        cookies = self.driver.get_cookies()
        with open(self.file_path, "w") as file:
            json.dump(cookies, file, indent=4)
    def load(self):
        self.driver.delete_all_cookies()
        with open(self.file_path, "r") as file:
            cookies = json.load(file)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
                     #I
                     #I
#Пример использования:
import time
import os.path
from selenium import webdriver
from cookies_manager import CookieManager
LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")
driver = webdriver.Chrome()
driver.get("https://www.freeconferencecall.com/ru/ru/login")
cookie_manager = CookieManager(driver)
if os.path.exists("../Практика/cookies.json"):
    cookie_manager.load()
else:
    driver.find_element(*LOGIN_FIELD).send_keys("Ваш логин")
    driver.find_element(*PASSWORD_FIELD).send_keys("Ваш пароль")
    driver.find_element(*SUBMIT_BUTTON).click()
    cookie_manager.save()
time.sleep(5)