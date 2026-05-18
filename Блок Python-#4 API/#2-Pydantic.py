from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

# Входные JSON-данные
json_data = {"name": "Alex", "age": 41}
# Валидация JSON
validated_data = User.model_validate(json_data)
# Вывод JSON после валидации
print(validated_data.model_dump_json(indent=2))


# Пример: Валидация JSON через Pydantic - оптимальная
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
# Входные JSON-данные
json_data = {"name": "Alex", "age": 41}
# Валидация JSON
validated_data = User(**json_data)

# Если нам нужно валидировать список объектов, то:
# 1. Используем list[Model] в BaseModel
from typing import List

class UserList(BaseModel):
    users: List[User]  # Список пользователей
data = {
    "users": [
        {"name": "Alex", "age": 41},
        {"name": "Yuliana", "age": 40}
    ]
}
users = UserList(**data)
print(users.users[0].name)  # Alex

# 2. Используем TypeAdapter, если нет BaseModel
# Если у нас есть чистый список объектов и мы не хотим оборачивать его в BaseModel
from pydantic import TypeAdapter
adapter = TypeAdapter(list[User])

users = [
    {"name": "Alex", "age": 41},
    {"name": "Yuliana", "age": 40}
]
validated_users = adapter.validate_python(users)
print(validated_users[0].name)  # Alex