import pytest
import time
from selenium import webdriver


@pytest.fixture(autouse=True)
def get_driver(request):
    driver = webdriver.Chrome
    request.cls.driver = driver
    yield # Передается управление тесту
    driver.quit()