# # Для CI/CD окружений
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
#
# # Оптимизация производительности
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-gpu")
#
# # Управление поведением
# options.add_argument("--disable-infobars")
# options.add_argument("--disable-notifications")

# # Режим инкогнито
# options.add_argument("--incognito")

# # Пример комплексной настройки:
# options.add_argument("--headless=new")                             #Без включения браузера
# options.add_argument("--incognito")                                #Режим инкогнито
# options.add_argument("--ignore-certificate-errors")                #Игнорирование отсутствия сертификата
# options.add_argument("--window-size=1920,1080")                    #Размер окна
# options.add_argument("--disable-cache")                            #Отключение кэширования
# options.add_argument("--no-sandbox")


from selenium import webdriver
import time

#Пример работы опции включения режима инкогнито в браузере.
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/upload-download")
FILE_CRED = ("xpath", "//input[@id = 'uploadFile']")                                #Объявляем переменную с расположением кнопки загрузки.
elemens_cred = driver.find_element(*FILE_CRED)                                      #Обращаемся к кнопке через переменную.
time.sleep(2)
elemens_cred.send_keys(r"C:\Users\User\PycharmProjects\AQA.Python\upload.gpeg")     #Через команду "send.keys()" загружаем файл на сайт.
time.sleep(2)