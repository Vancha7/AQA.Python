# from faker import Faker
# Генерирует нам фейковые данные, по типу - логины, пароли и т.д.
# faker = Faker()

#(1).
import pytest
from collections import namedtuple
from faker import Faker  # Позволяет генерировать данные, pip3 install faker

fake = Faker()  # Через этот обьект будет генерировать данные


@pytest.fixture
def generate_data():
    login = fake.email()
    password = fake.password()
    NewUser = namedtuple('UserData', ['login', 'password'])  # именованный tuple
    return NewUser(login, password)  # Возвращаем обьект

#(2).

import pytest
import time
from faker import Faker # Позволяет генерировать данные, pip3 install faker

fake = Faker() # Через этот обьект будет генерировать данные

@pytest.fixture
def generate_data(request):
    # Генерируем данные
    request.cls.login = fake.email()
    request.cls.password = fake.password()