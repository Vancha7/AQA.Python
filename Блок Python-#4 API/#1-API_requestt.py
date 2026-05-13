import requests

response = requests.get(
    url="http://2.59.41.2:7320/api/auth/logout",
    headers={
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IlZhbmhjYS03QG1haWwucnUiLCJpZCI6MTQ1MDgsImlhdCI6MTc3ODY5NjQ1MywiZXhwIjoxNzc4NzAwMDUzfQ.qGwpsgB4J3jDpbHL3ksM6OZAiJoO2PAjTdDr7m8HpRg"
    }
)
print(response.json())