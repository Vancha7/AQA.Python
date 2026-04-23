import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
import time
from locators import DemoQALocators as L

def take_screenshot(driver, name):
    """Функция для создания скриншота и добавления в Allure отчёт"""
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)


@allure.feature("DemoQA")
class TestDemoQA:

    @allure.story("Elements")
    @allure.title("Тест Text Box")
    @pytest.mark.smoke
    @pytest.mark.elements
    @pytest.mark.critical
    def test_text_box(self, driver):
        driver.get("https://demoqa.com/elements")

        time.sleep(3)
        take_screenshot(driver, "Открыта страница Elements")

        driver.find_element(*L.TEXT_BOX).click()
        take_screenshot(driver, "Открыта форма Text Box")

        # Заполнение полей
        element_full_name = driver.find_element(*L.FULL_NAME)
        element_full_name.clear()
        element_full_name.send_keys("Иван Васильченко")
        assert "Иван Васильченко" in element_full_name.get_attribute("value")

        elements_email = driver.find_element(*L.EMAIL)
        elements_email.clear()
        elements_email.send_keys("Vancha-15@mail.ru")
        assert "Vancha-15@mail.ru" in elements_email.get_attribute("value")

        elements_current = driver.find_element(*L.CURRENT_ADDRESS)
        elements_current.clear()
        elements_current.send_keys("Краснодар, улица Московская 45/2.")

        elements_address = driver.find_element(*L.PERMANENT_ADDRESS)
        elements_address.clear()
        elements_address.send_keys("Краснодарский Край, Калининский район, Гривенская.")
        
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Text page",
            attachment_type=allure.attachment_type.PNG
        )
        time.sleep(1)

    @allure.story("Elements")
    @allure.title("Тест Upload and Download")
    @pytest.mark.upload
    @pytest.mark.elements
    def test_upload_file(self, driver):
        driver.get("https://demoqa.com/elements")
        time.sleep(3)

        UPLOAD = (By.XPATH, "//span[text()='Upload and Download']")
        driver.find_element(*UPLOAD).click()
        time.sleep(1)

        upload_element = driver.find_element(*L.UPLOAD_FILE)
        upload_element.send_keys(r"C:\Users\User\PycharmProjects\AQA.Python\upload.gpeg")
        allure.attach("Файл загружен: upload.gpeg", name="File Upload", attachment_type=allure.attachment_type.TEXT)
        take_screenshot(driver, "Результат загрузки файла")
        time.sleep(2)

    @allure.story("Elements")
    @allure.title("Тест Dynamic Properties")
    @pytest.mark.dynamic
    @pytest.mark.elements
    def test_dynamic_properties(self, driver, wait):
        driver.get("https://demoqa.com/elements")
        time.sleep(3)
        DINAMIC_P = (By.XPATH, "//span[text()='Dynamic Properties']")
        driver.find_element(*DINAMIC_P).click()
        time.sleep(1)

        print("Ожидание активации кнопки...")
        wait.until(EC.element_to_be_clickable(L.ENABLE_AFTER))
        print("✓ Кнопка стала кликабельной")
        driver.find_element(*L.VISIBLE_AFTER).click()
        print("✓ Клик по кнопке выполнен")
        print("Ожидание появления второй кнопки...")
        wait.until(EC.visibility_of_element_located(L.ENABLE_AFTER))
        print("✓ Вторая кнопка стала видимой")
        time.sleep(2)

    @allure.story("Alerts")
    @allure.title("Тест всех алертов")
    @pytest.mark.alerts
    @pytest.mark.critical
    @pytest.mark.smoke
    def test_alerts(self, driver, wait):
        driver.get("https://demoqa.com/elements")
        driver.find_element(*L.ALERTS_DIV).click()
        time.sleep(1)
        driver.find_element(*L.ALERTS_LINK).click()
        time.sleep(1)

        # Простой алерт
        driver.find_element(*L.ALERT_BUTTON).click()
        alert = driver.switch_to.alert
        alert.accept()
        allure.attach("Простой алерт принят", name="Alert 1", attachment_type=allure.attachment_type.TEXT)

        # Алерт с таймером
        driver.find_element(*L.TIMER_ALERT_BUTTON).click()
        alert = wait.until(EC.alert_is_present())
        alert.accept()
        allure.attach("Алерт с таймером принят", name="Alert 2", attachment_type=allure.attachment_type.TEXT)

        # Алерт с подтверждением
        driver.find_element(*L.CONFIRM_BUTTON).click()
        alert.dismiss()
        allure.attach("Алерт отклонен", name="Alert 3", attachment_type=allure.attachment_type.TEXT)

        # Алерт с вводом текста
        driver.find_element(*L.PROMPT_BUTTON).click()
        alert.send_keys("Iva.AQA")
        alert.accept()
        allure.attach("Введен текст: Iva.AQA", name="Alert 4", attachment_type=allure.attachment_type.TEXT)
        time.sleep(2)

    @allure.story("Widgets")
    @allure.title("Тест Select Menu")
    @pytest.mark.widgets
    @pytest.mark.select_menu
    def test_select_menu(self, driver):
        driver.get("https://demoqa.com/elements")
        time.sleep(5)
        driver.find_element(*L.WIDGETS_DIV).click()
        time.sleep(5)
        driver.find_element(*L.SELECT_MENU).click()
        time.sleep(1)

        driver.find_element(*L.SELECT_VALUE).click()
        time.sleep(1)
        driver.find_element(*L.ANOTHER_ROOT_OPTION).click()
        time.sleep(2)

        # Old Style Select
        DROPDOWN = Select(driver.find_element(*L.OLD_STYLE_SELECT))
        DROPDOWN.select_by_visible_text("Black")
        time.sleep(2)

        # Multi Select
        select = driver.find_element(*L.MULTI_SELECT_INPUT)
        select.send_keys("Green")
        select.send_keys(Keys.ENTER)
        select.send_keys(Keys.ESCAPE)
        time.sleep(2)
        select.send_keys("Blue")
        select.send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element(*L.MULTI_SELECT_CLEAR).click()

        # Standard Select
        DROPDOWN2 = Select(driver.find_element(*L.STANDARD_SELECT))
        DROPDOWN2.select_by_index(3)
        take_screenshot(driver, "Выбрана опция в Standard Select")
        time.sleep(5)

    @allure.story("Buttons")
    @allure.title("Тест взаимодействия с мышью")
    @pytest.mark.mouse
    @pytest.mark.critical
    def test_mouse_actions(self, driver, action_chains):
        driver.get("https://demoqa.com/elements")
        time.sleep(1)
        driver.find_element(*L.SELECT_MENU_BUTTONS).click()
        time.sleep(2)

        # Двойной клик
        BUTTON = driver.find_element(*L.B_BUTTON_LOCATOR)
        action_chains.double_click(BUTTON).perform()
        allure.attach("Выполнен двойной клик", name="Mouse Action", attachment_type=allure.attachment_type.TEXT)
        time.sleep(2)

        # Клик правой кнопкой
        BUTTON = driver.find_element(*L.RIGHT_CLICK_BUTTON)
        action_chains.context_click(BUTTON).perform()
        allure.attach("Выполнен клик правой кнопкой", name="Mouse Action", attachment_type=allure.attachment_type.TEXT)
        time.sleep(2)

        # Одинарный клик
        element = driver.find_element(*L.CLICK_ME)
        action_chains.click(element).perform()
        allure.attach("Выполнен одинарный клик", name="Mouse Action", attachment_type=allure.attachment_type.TEXT)
        print("Раздел по взаимодействию с мышью успешно пройден ✓.")