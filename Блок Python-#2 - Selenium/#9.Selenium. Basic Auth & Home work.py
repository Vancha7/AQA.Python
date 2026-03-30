#https://admin:admin@the-internet.herokuapp.com/basic_auth
#Авторизация в "Модальном окне".
# Логин и password передаются в URL.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
    }
)
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com")

USER_NAME = ("xpath", "//input[@id='user-name']")
PASSWORD = ("xpath", "//input[@id='password']")
LOGIN_BUTTON = ("xpath", "//input[@id='login-button']")

driver.find_element(*USER_NAME).send_keys("standard_user")
time.sleep(1)
driver.find_element(*PASSWORD).send_keys("secret_sauce")
time.sleep(1)
driver.find_element(*LOGIN_BUTTON).click()
time.sleep(2)
assert "https://www.saucedemo.com/inventory.html" == driver.current_url
print("Открыта страница с каталогом...")

PRICE_FILTR = ("xpath", "//select[@class='product_sort_container']")
DROP = ("xpath", "//option[text()= 'Price (high to low)']")
driver.find_element(*PRICE_FILTR).click()
print("Открыт фильтр/выпадающий список.")
time.sleep(1)
driver.find_element(*DROP).click()
print("Выбран элемент/фильтр из выпадающего списка")
time.sleep(1)

KOFTA_BUTTON = ("xpath", "(//button[text()='Add to cart'])[1]")
MAIKA_BUTTON = ("xpath", "(//button[text()='Add to cart'])[2]")
driver.find_element(*KOFTA_BUTTON).click()
print("Кофта добавлена в корзину.")
driver.find_element(*MAIKA_BUTTON).click()
print("Майка добавлена в корзину.")
time.sleep(2)

KORZINA = ("xpath", "//div[@class='shopping_cart_container']")
driver.find_element(*KORZINA).click()
assert "https://www.saucedemo.com/cart.html" == driver.current_url
print("Открыта корзина.")
time.sleep(5)

BUTTON_CHECKOUT = ("xpath", "//button[@id='checkout']")
driver.find_element(*BUTTON_CHECKOUT).click()
assert "https://www.saucedemo.com/checkout-step-one.html" == driver.current_url
print("Нажатие кнопки, переход к оформлению.")
time.sleep(2)

FIRST_NAME = ("xpath", "//input[@id='first-name']")
LAST_NAME = ("xpath", "//input[@id='last-name']")
ZIP_CODE = ("xpath", "//input[@id='postal-code']")
driver.find_element(*FIRST_NAME).send_keys("Иван")
driver.find_element(*LAST_NAME).send_keys("Васильченко")
driver.find_element(*ZIP_CODE).send_keys("353798")
print("Поля заполнены.")
time.sleep(2)
BUTTON_CONTINUE = ("xpath", "//input[@id='continue']")
driver.find_element(*BUTTON_CONTINUE).click()
assert "https://www.saucedemo.com/checkout-step-two.html" == driver.current_url
print("Открыта страница подтверждения заказа.")
time.sleep(2)

BUTTON_FINISH = ("xpath", "//button[@id='finish']")
driver.find_element(*BUTTON_FINISH).click()
print("Кнопка подтверждение заказа нажата.")
time.sleep(2)

BACK_HOME = ("xpath", "//button[text()='Back Home']")
driver.find_element(*BACK_HOME).click()
print("Возврат к домашней странице.")
time.sleep(3)