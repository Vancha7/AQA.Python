# pytest практика / test_my2.py -sv --lf

import pytest
from selenium import webdriver

class TestLogin:    # Название тестового класса

    def setup_method(self):
        self.driver = webdriver.Chrome()

    @pytest.mark.smoke
    def test_open_login_page(self):     # Тест пройдет
        self.driver.get("https://demoqa.com/login")
        assert self.driver.current_url == "https://demoqa.com/login", "Ошибка"

    @pytest.mark.regression
    def test_open_books_page(self):     # Тест упадет
        self.driver.get("https://demoqa.com/books")
        assert self.driver.current_url == "https://", "Ошибка"

    @pytest.mark.smoke  # Тест относится и к smoke и к sanity
    @pytest.mark.sanity
    def test_open_profile_page(self):     # Тест упадет
        self.driver.get("https://demoqa.com/profile")
        assert self.driver.current_url == "https://", "Ошибка"

    def teardown_method(self):
        self.driver.close()