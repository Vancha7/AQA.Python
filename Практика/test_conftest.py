import pytest


# Вызываем фикстуру над классом
class TestExample:

    @pytest.mark.usefixtures("generate_data")
    def test_example_cls(self):
        # Обращаясь через self к данным, мы легко получаем к ним доступ
        print(self.login, self.password)
###