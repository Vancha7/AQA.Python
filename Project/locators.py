from selenium.webdriver.common.by import By


class DemoQALocators:
    """Класс с локаторами для DemoQA"""

    # ========== Главная страница ==========
    ELEMENTS_CARD = (By.XPATH, "//div[@class='card-body']")

    # ========== Elements разделы ==========
    TEXT_BOX = (By.XPATH, "//span[@class='text']")
    UPLOAD_DOWNLOAD = (By.XPATH, "//span[text()='Upload and Download']")
    DYNAMIC_PROPERTIES = (By.XPATH, "//span[text()='Dynamic Properties']")
    BUTTONS = (By.XPATH, "//span[text()='Buttons']")

    # ========== Text Box поля ==========
    FULL_NAME = (By.XPATH, "//input[@id='userName']")
    EMAIL = (By.XPATH, "//input[@type='email']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = (By.XPATH, "//textarea[@id='permanentAddress']")

    # ========== Upload & Download ==========
    UPLOAD_FILE = (By.XPATH, "//input[@id='uploadFile']")

    # ========== Dynamic Properties ==========
    ENABLE_AFTER = (By.XPATH, "//button[@id='enableAfter']")
    VISIBLE_AFTER = (By.XPATH, "//button[@id='visibleAfter']")

    # ========== Alerts разделы ==========
    ALERTS_DIV = (By.XPATH, "//div[contains(@class, 'header-text') and contains(text(), 'Alerts')]")
    ALERTS_LINK = (By.XPATH, "//span[text()='Alerts']")
    ALERT_BUTTON = (By.XPATH, "//button[@id='alertButton']")
    TIMER_ALERT_BUTTON = (By.XPATH, "//button[@id='timerAlertButton']")
    CONFIRM_BUTTON = (By.XPATH, "//button[@id='confirmButton']")
    PROMPT_BUTTON = (By.XPATH, "//button[@id='promtButton']")

    # ========== Widgets разделы ==========
    WIDGETS_DIV = (By.XPATH, "//div[contains(@class, 'header-text') and contains(text(), 'Widgets')]")
    SELECT_MENU = (By.XPATH, "//span[text()='Select Menu']")

    # ========== Select Menu элементы ==========
    SELECT_VALUE = (By.XPATH, "//div[@class='css-19bb58m']")
    ANOTHER_ROOT_OPTION = (By.XPATH, "//div[text()='Another root option']")
    OLD_STYLE_SELECT = (By.XPATH, "//select[@id='oldSelectMenu']")
    MULTI_SELECT_INPUT = (By.XPATH, "//input[@id='react-select-4-input']")
    MULTI_SELECT_CLEAR = (By.XPATH, "//div[@class='css-v7duua']")
    STANDARD_SELECT = (By.XPATH, "//select[@id='cars']")

    # ========== Buttons элементы ==========
    SELECT_MENU_BUTTONS = (By.XPATH, "//span[text()='Buttons']")
    B_BUTTON_LOCATOR = (By.XPATH, "//button[@id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.XPATH, "//button[@id='rightClickBtn']")
    ELEMENTS_MAIN = (By.XPATH, "(//div[@class='header-text'])[1]")
    CLICK_ME = (By.XPATH, "//button[text()='Click Me']")

    # ========== Общие элементы ==========
    ELEMENTS_MAIN = (By.XPATH, "(//div[@class='header-text'])[1]")