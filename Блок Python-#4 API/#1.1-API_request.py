# response.json() # Получение ответа в формате json
# response.status_code # Получение статус-кода
# response.headers # Получение заголовков
# response.text # Получение ответа в формате текста, например html-страница
# response.cookies # Получение куков

import requests

# Пример 1 - GET запрос без параметров
response = requests.get(
    url="https://petstore.swagger.io/v2/store/inventory",
    headers={
        "api_key": "special-key"
    }
)
assert response.status_code == 200 # Проверка стату-кода
assert response.json()["available"] == 162 # Проверка конкретного поля в ответе

# Пример 2 - GET запрос с path-параметром /v1/users/{uuid}
response = requests.get(
    url="https://release-gs.qa-playground.com/api/v1/users/e30f9ed6-a311-42fc-8a6f-362dd42be185", # Указание path-параметра
    headers={
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IlZhbmhjYS03QG1haWwucnUiLCJpZCI6MTQ1MDgsImlhdCI6MTc3ODY5NjQ1MywiZXhwIjoxNzc4NzAwMDUzfQ.qGwpsgB4J3jDpbHL3ksM6OZAiJoO2PAjTdDr7m8HpRg"
    }
)
print(response.json()) # Вывод ответа

# Пример 3 - GET запрос с query-параметрами
response = requests.get(
    url="https://petstore.swagger.io/v2/pet/findByStatus",
    headers={
        "api_key": "special-key"
    },
    params={
        "status": "available" # Передача query-параметров
    }
)
print(response.json()) # Вывод ответа

# Структура POST, PUT, PATCH запросов (метода):
response = requests.post(
	url="",
	headers={},
        json={},
)
