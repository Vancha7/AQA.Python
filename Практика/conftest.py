import pytest
import time
from faker import Faker # Позволяет генерировать данные, pip3 install faker

fake = Faker() # Через этот обьект будет генерировать данные

@pytest.fixture
def generate_data(request):
    # Генерируем данные
    request.cls.login = fake.email()
    request.cls.password = fake.password()