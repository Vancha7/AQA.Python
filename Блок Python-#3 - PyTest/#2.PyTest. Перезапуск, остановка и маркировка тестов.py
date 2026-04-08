# pytest --lf - запускает упавшие в прошлом запуске тесты.
# pytest -sv --reruns=2 попробует перезапустить упавший тест n раз, сразу после падения
# pytest -sv --reruns=2 --reruns-delay=3 создает паузу между перезапусками
# pytest -sv --maxfail=2  данный параметр выставляет кол-во упавших тестов при котором, все авто-тесты остановятся. Параметр n - кол-во упавших тестов
# @pytest.mark.имя_маркера - имя маркера может быть любым. smoke, sanity, regression - это лишь простые примеры.
# pytest -sv -m smoke -m маркер - запустит тесты под нужным маркером
# pytest -sv -m "smoke or regression" - запустит кейсы под двумя маркерами.
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
        assert self.driver.current_url == "https://demoqa.com/books", "Ошибка"

    @pytest.mark.smoke  # Тест относится и к smoke и к sanity
    @pytest.mark.sanity
    def test_open_profile_page(self):     # Тест упадет
        self.driver.get("https://demoqa.com/profile")
        assert self.driver.current_url == "https://demoqa.com/profile", "Ошибка"

    def teardown_method(self):
        self.driver.close()