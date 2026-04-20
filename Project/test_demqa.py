import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


@allure.feature("DemoQA")
@allure.story("Full Testing")
@allure.title("Комплексное тестирование всех разделов")
@allure.severity(allure.severity_level.CRITICAL)
class TestDemoQA:

    @allure.step("Открытие главной страницы")
    def test_full_scenario(self, driver, action_chains, wait):
        # ========== 1. ОТКРЫТИЕ САЙТА ==========
        with allure.step("Открыть сайт DemoQA"):
            driver.get("https://demoqa.com")
            time.sleep(1)
            allure.attach(driver.get_screenshot_as_png(),
                          name="main_page",
                          attachment_type=allure.attachment_type.PNG)

        # ========== 2. ПЕРЕХОД В РАЗДЕЛ ELEMENTS ==========
        with allure.step("Переход в раздел Elements"):
            ELEMENTS = (By.XPATH, "//div[@class='card-body']")
            click_element = driver.find_element(*ELEMENTS)
            click_element.click()
            time.sleep(1)

        # ========== 3. ПЕРЕХОД В ПОДРАЗДЕЛ TEXT BOX ==========
        with allure.step("Переход в подраздел Text Box"):
            TEXT_BOX = (By.XPATH, "//span[@class='text']")
            click_text = driver.find_element(*TEXT_BOX)
            click_text.click()
            time.sleep(1)

        # ========== 4. ЗАПОЛНЕНИЕ ПОЛЕЙ В TEXT BOX ==========
        with allure.step("Заполнение поля Full Name"):
            element_full_name = driver.find_element(By.XPATH, "//input[@id='userName']")
            element_full_name.clear()
            element_full_name.send_keys("Иван Васильченко")
            email_field = element_full_name.get_attribute("value")
            assert "Иван Васильченко" in email_field
            allure.attach(email_field, name="Full Name", attachment_type=allure.attachment_type.TEXT)
            time.sleep(1)

        with allure.step("Заполнение поля Email"):
            elements_email = driver.find_element(By.XPATH, "//input[@type='email']")
            elements_email.clear()
            elements_email.send_keys("Vancha-15@mail.ru")
            elements_email_as = elements_email.get_attribute("value")
            assert "Vancha-15@mail.ru" in elements_email_as
            allure.attach(elements_email_as, name="Email", attachment_type=allure.attachment_type.TEXT)
            time.sleep(1)

        with allure.step("Заполнение поля Current Address"):
            elements_current = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
            elements_current.clear()
            elements_current.send_keys("Краснодар, улица Московская 45/2.")
            elements_current_as = elements_current.get_attribute("value")
            assert "Краснодар, улица Московская 45/2." in elements_current_as
            time.sleep(1)

        with allure.step("Заполнение поля Permanent Address"):
            elements_address = driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']")
            elements_address.clear()
            elements_address.send_keys("Краснодарский Край, Калининский район, Гривенская.")
            elements_address_as = elements_address.get_attribute("value")
            assert "Краснодарский Край, Калининский район, Гривенская." in elements_address_as
            time.sleep(1)

        # ========== 5. ЗАГРУЗКА ФАЙЛОВ ==========
        with allure.step("Переход в раздел Upload and Download"):
            UPLOAD = (By.XPATH, "//span[text()='Upload and Download']")
            elements_upload = driver.find_element(*UPLOAD)
            elements_upload.click()
            time.sleep(1)

        with allure.step("Загрузка файла"):
            FILE_CRED = (By.XPATH, "//input[@id='uploadFile']")
            elemens_cred = driver.find_element(*FILE_CRED)
            time.sleep(1)
            elemens_cred.send_keys(r"C:\Users\User\PycharmProjects\AQA.Python\upload.gpeg")
            allure.attach("Файл загружен: upload.gpeg", name="File Upload", attachment_type=allure.attachment_type.TEXT)
            time.sleep(2)

        # ========== 6. ДИНАМИЧЕСКИЕ ЭЛЕМЕНТЫ ==========
        with allure.step("Переход в раздел Dynamic Properties"):
            DINAMIC_P = (By.XPATH, "//span[text()='Dynamic Properties']")
            elements_p = driver.find_element(*DINAMIC_P)
            elements_p.click()
            time.sleep(1)

        with allure.step("Ожидание активации кнопки"):
            ADD_ELEMENT_BUTTON = (By.XPATH, "//button[@id='enableAfter']")
            DELETE_BUTTON = (By.XPATH, "//button[@id='visibleAfter']")
            print("Ожидание активации кнопки...")
            wait.until(EC.element_to_be_clickable(ADD_ELEMENT_BUTTON))
            print("✓ Кнопка стала кликабельной")
            driver.find_element(*ADD_ELEMENT_BUTTON).click()
            print("✓ Клик по кнопке выполнен")

            print("Ожидание появления второй кнопки...")
            wait.until(EC.visibility_of_element_located(DELETE_BUTTON))
            print("✓ Вторая кнопка стала видимой")
            time.sleep(2)

        # ========== 7. РАБОТА С АЛЕРТАМИ ==========
        with allure.step("Открытие раздела Alerts"):
            ALLERTS_DIV = (By.XPATH, "//div[contains(@class, 'header-text') and contains(text(), 'Alerts')]")
            driver.find_element(*ALLERTS_DIV).click()
            time.sleep(1)
            print("Открыт выпадающий список Аллерт...")

        with allure.step("Переход в подраздел Alerts"):
            ALLERST_1 = (By.XPATH, "//span[text()='Alerts']")
            driver.find_element(*ALLERST_1).click()
            time.sleep(1)
            print("Открыт раздел Allerts...")

        with allure.step("Обработка простого алерта"):
            driver.find_element(By.XPATH, "//button[@id='alertButton']").click()
            time.sleep(1)
            print("Нажата кнопка Allerts...")
            alert = driver.switch_to.alert
            time.sleep(1)
            alert.accept()
            print("Allerts принят.")
            allure.attach("Простой алерт принят", name="Alert 1", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Обработка алерта с таймером"):
            ALLERST_2 = (By.XPATH, "//button[@id='timerAlertButton']")
            driver.find_element(*ALLERST_2).click()
            time.sleep(1)
            alert = wait.until(EC.alert_is_present())
            time.sleep(1)
            alert.accept()
            allure.attach("Алерт с таймером принят", name="Alert 2", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Обработка алерта с подтверждением (Отмена)"):
            ALLERST_3 = (By.XPATH, "//button[@id='confirmButton']")
            driver.find_element(*ALLERST_3).click()
            time.sleep(1)
            alert.dismiss()
            allure.attach("Алерт отклонен", name="Alert 3", attachment_type=allure.attachment_type.TEXT)
            time.sleep(1)

        with allure.step("Обработка алерта с вводом текста"):
            ALLERST_4 = (By.XPATH, "//button[@id='promtButton']")
            driver.find_element(*ALLERST_4).click()
            time.sleep(1)
            alert.send_keys("Iva.AQA")
            time.sleep(1)
            alert.accept()
            allure.attach("Введен текст: Iva.AQA", name="Alert 4", attachment_type=allure.attachment_type.TEXT)
            time.sleep(2)

        # ========== 8. РАБОТА С WIDGETS И SELECT MENU ==========
        with allure.step("Переход в раздел Widgets"):
            WIDGETS_DIV = (By.XPATH, "//div[contains(@class, 'header-text') and contains(text(), 'Widgets')]")
            driver.find_element(*WIDGETS_DIV).click()
            time.sleep(5)

        with allure.step("Переход в подраздел Select Menu"):
            SELECT_MENU = (By.XPATH, "//span[text()='Select Menu']")
            driver.find_element(*SELECT_MENU).click()
            time.sleep(1)

        with allure.step("Работа с выпадающим списком Select Value"):
            SELECT_VALUE = (By.XPATH, "//div[@class='css-19bb58m']")
            DROP1 = (By.XPATH, "//div[text()='Another root option']")
            driver.find_element(*SELECT_VALUE).click()
            time.sleep(1)
            driver.find_element(*DROP1).click()
            time.sleep(2)

        with allure.step("Работа с Old Style Select Menu"):
            OLD_STYLE = (By.XPATH, "//select[@id='oldSelectMenu']")
            DROPDOWN = Select(driver.find_element(*OLD_STYLE))
            DROPDOWN.select_by_visible_text("Black")
            allure.attach("Выбран Black", name="Select Menu", attachment_type=allure.attachment_type.TEXT)
            time.sleep(2)

        with allure.step("Работа с Multi Select"):
            MULTISELECT = (By.XPATH, "//input[@id='react-select-4-input']")
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

            END_ESC = (By.XPATH, "//div[@class='css-v7duua']")
            driver.find_element(*END_ESC).click()

        with allure.step("Работа со Standard Select"):
            STANDARD_SELECT = (By.XPATH, "//select[@id='cars']")
            DROPDOWN2 = Select(driver.find_element(*STANDARD_SELECT))
            DROPDOWN2.select_by_index(3)
            allure.attach("Выбран элемент по индексу 3", name="Standard Select",
                          attachment_type=allure.attachment_type.TEXT)
            time.sleep(5)

        # ========== 9. ВЗАИМОДЕЙСТВИЕ С МЫШЬЮ ==========
        with allure.step("Взаимодействие с мышью - кнопки"):
            SELECT_MENU_BUTTONS = (By.XPATH, "//span[text()='Buttons']")
            B_BUTTON_LOCATOR = (By.XPATH, "//button[@id='doubleClickBtn']")
            RIGHT_CLICK_BUTTON = (By.XPATH, "//button[@id='rightClickBtn']")
            ELEMENTS_MAIN = (By.XPATH, "(//div[@class='header-text'])[1]")
            CLICK_ME = (By.XPATH, "//button[text()='Click Me']")
            time.sleep(2)

            driver.find_element(*ELEMENTS_MAIN).click()
            time.sleep(1)
            driver.find_element(*SELECT_MENU_BUTTONS).click()
            time.sleep(2)

            with allure.step("Двойной клик"):
                BUTTON = driver.find_element(*B_BUTTON_LOCATOR)
                action_chains.double_click(BUTTON).perform()
                allure.attach("Выполнен двойной клик", name="Mouse Action", attachment_type=allure.attachment_type.TEXT)
                time.sleep(2)

            with allure.step("Клик правой кнопкой"):
                BUTTON = driver.find_element(*RIGHT_CLICK_BUTTON)
                time.sleep(2)
                action_chains.context_click(BUTTON).perform()
                allure.attach("Выполнен клик правой кнопкой", name="Mouse Action",
                              attachment_type=allure.attachment_type.TEXT)
                time.sleep(2)

            with allure.step("Одинарный клик"):
                element = driver.find_element(*CLICK_ME)
                action_chains.click(element).perform()
                allure.attach("Выполнен одинарный клик", name="Mouse Action",
                              attachment_type=allure.attachment_type.TEXT)
                print("Раздел по взаимодействию с мышью успешно пройден ✓.")

        # Финальный скриншот
        with allure.step("Финальный скриншот"):
            allure.attach(driver.get_screenshot_as_png(),
                          name="final_state",
                          attachment_type=allure.attachment_type.PNG)

        allure.attach("Все тесты успешно завершены!", name="Test Result", attachment_type=allure.attachment_type.TEXT)