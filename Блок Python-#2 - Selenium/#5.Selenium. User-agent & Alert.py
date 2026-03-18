#Агент.
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")       # отключает некоторые автоматические функции,
                                                                            # которые могут выдавать использование автоматизации.



options.add_experimental_option("excludeSwitches", ["enable-automation"])   # Эти параметры исключают автоматизацию расширений и отключают уведомление
                                                                            # об использовании автоматизации.



options.add_experimental_option('useAutomationExtension', False)            # отключает использование расширения для автоматизации браузера (Automation Extension),
                                                                            # которое обычно используется для управления браузером через WebDriver.

options.add_argument("--user-agent=Ваш кастомный или заранее выбранный юзер-агент") #Сюда прописать user-agent.


driver = webdriver.Chrome(options=options)
driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
time.sleep(3)


#Allert.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создание экземпляра веб-драйвера
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10, poll_frequency=1)

# Переход на веб-страницу
driver.get("https://demoqa.com/alerts")
driver.find_element("xpath", "//button[@id='alertButton']").click()
time.sleep(2)

# Ожидание появления alert и запись элемента Alert в переменную
alert = driver.switch_to.alert

# Ожидание появления alert и запись элемента Alert в переменную
alert = wait.until(EC.alert_is_present())

# Принимаем алерт - alert.accept()
# Отклоняем алерт - alert.dismiss()
# Ввод данных в alert - alert.send_keys("Alex")
