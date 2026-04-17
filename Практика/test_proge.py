import pytest
import allure
from allure_commons.types import Severity


@allure.epic("Accounts")
@allure.feature("Login")
@allure.story("Pages")
@pytest.mark.usefixtures("driver")
class TestPages:


    @pytest.mark.smoke
    @allure.title("Open login page")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com", name="Documentation")
    def test_open_login_page(self):
        self.driver.get("https://demoqa.com/login")
        assert self.driver.current_url == "https://demoqa.com/login", "Ошибка ULR страницы входа"

    @pytest.mark.regression
    @allure.title("Open book page")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com", name="Documentation")
    def test_open_books_page(self):
        self.driver.get("https://demoqa.com/books")
        assert self.driver.current_url == "https://demoqa.com/books", "Ошибка ULR страницы с книгами"

    @pytest.mark.profile
    @allure.title("Open profile page")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com", name="Documentation")
    def test_open_profile_page(self):
        self.driver.get("https://demoqa.com/profile")
        assert self.driver.current_url == "https://demoqa.com/profile", "Ошибка ULR страницы профиля"