import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def action_chains(driver):
    return ActionChains(driver)

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, timeout=10)