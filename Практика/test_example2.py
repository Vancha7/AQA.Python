import pytest

class TestExample:

    def test_open_page(self):
        self.driver.get("https://google.com") # И никаких явных вызовов фикстуры